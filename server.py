#!/usr/bin/env python3
"""
Surgical Case Log — Backend API
SQLite database for persistent storage with user accounts.
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os
import hashlib
import secrets
import json
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

DB_PATH = os.environ.get('DB_PATH', os.path.join(os.path.dirname(__file__), 'caselog.db'))

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def init_db():
    conn = get_db()
    conn.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            name TEXT,
            token TEXT UNIQUE,
            plan TEXT DEFAULT 'trial',
            license_key TEXT,
            plan_expires_at TEXT,
            created_at TEXT DEFAULT (datetime('now'))
        );
        
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date TEXT,
            age INTEGER,
            sex TEXT,
            rotation TEXT,
            procedure_name TEXT,
            cpt_code TEXT,
            role TEXT,
            approach TEXT,
            attending TEXT,
            complications TEXT DEFAULT 'None',
            ebl INTEGER,
            or_time INTEGER,
            notes TEXT,
            created_at TEXT DEFAULT (datetime('now')),
            updated_at TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        
        CREATE TABLE IF NOT EXISTS milestones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            category TEXT NOT NULL,
            count INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id),
            UNIQUE(user_id, category)
        );
        
        CREATE INDEX IF NOT EXISTS idx_cases_user ON cases(user_id);
        CREATE INDEX IF NOT EXISTS idx_cases_date ON cases(user_id, date);
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    salt = secrets.token_hex(16)
    h = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
    return salt + ':' + h.hex()

def verify_password(stored, provided):
    salt, stored_hash = stored.split(':')
    h = hashlib.pbkdf2_hmac('sha256', provided.encode(), salt.encode(), 100000)
    return h.hex() == stored_hash

def get_user_from_token(token):
    if not token:
        return None
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE token = ?', (token,)).fetchone()
    conn.close()
    return user

def auth_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        user = get_user_from_token(token)
        if not user:
            return jsonify({'error': 'Unauthorized'}), 401
        request.user = user
        return f(*args, **kwargs)
    return decorated

def plan_required(f):
    """Require an active plan (not expired) to access."""
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        from datetime import datetime
        plan = request.user['plan'] or 'trial'
        expires = request.user['plan_expires_at']
        
        if plan == '90day' and expires:
            if datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') > expires:
                return jsonify({'error': 'Your 90-day access has expired. Please renew.', 'expired': True}), 403
        elif plan == 'expired':
            return jsonify({'error': 'Your access has expired. Please renew.', 'expired': True}), 403
        
        return f(*args, **kwargs)
    return decorated

# ============ AUTH ============

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    name = data.get('name', '')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    if len(password) < 6:
        return jsonify({'error': 'Password must be 6+ characters'}), 400
    
    conn = get_db()
    existing = conn.execute('SELECT id FROM users WHERE email = ?', (email,)).fetchone()
    if existing:
        conn.close()
        return jsonify({'error': 'Email already registered'}), 409
    
    token = secrets.token_urlsafe(32)
    pw_hash = hash_password(password)
    
    conn.execute('INSERT INTO users (email, password_hash, name, token) VALUES (?, ?, ?, ?)',
                 (email, pw_hash, name, token))
    conn.commit()
    conn.close()
    
    return jsonify({'token': token, 'name': name, 'email': email, 'plan': 'trial', 'plan_expires_at': None})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')
    
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
    
    if not user or not verify_password(user['password_hash'], password):
        conn.close()
        return jsonify({'error': 'Invalid email or password'}), 401
    
    # Generate new token
    token = secrets.token_urlsafe(32)
    conn.execute('UPDATE users SET token = ? WHERE id = ?', (token, user['id']))
    conn.commit()
    conn.close()
    
    return jsonify({'token': token, 'name': user['name'], 'email': user['email'], 'plan': user['plan'] or 'trial', 'plan_expires_at': user['plan_expires_at']})

# ============ LICENSE VERIFICATION ============

@app.route('/api/activate', methods=['POST'])
@auth_required
def activate_by_email():
    """Verify purchase by checking Gumroad sales for the user's email."""
    import requests as req
    
    user_email = request.user['email']
    
    # Check Gumroad sales API for this email
    GUMROAD_TOKEN = "X_X3q6Cw7bJuRkvmwKRGIwhN9Comr3wkjKkMXrv-ZFE"
    
    try:
        # Check all sales for matching email
        r = req.get(f'https://api.gumroad.com/v2/sales?access_token={GUMROAD_TOKEN}&email={user_email}', timeout=15)
        
        if r.status_code == 200:
            result = r.json()
            sales = result.get('sales', [])
            
            if not sales:
                return jsonify({'error': 'No purchase found for this email. Please buy at davincibot.gumroad.com', 'needs_purchase': True}), 404
            
            # Find the most recent active sale
            conn = get_db()
            
            for sale in sales:
                if sale.get('refunded') or sale.get('disputed'):
                    continue
                
                # Check if subscription or one-time
                is_subscription = sale.get('subscription_id') is not None
                recurrence = sale.get('recurrence')
                
                if is_subscription or recurrence:
                    # Subscription - check if still active
                    cancelled = sale.get('cancelled', False)
                    ended = sale.get('ended', False)
                    
                    if not cancelled and not ended:
                        plan = 'subscription'
                        expires = None
                    else:
                        continue  # Skip cancelled subscriptions
                else:
                    # One-time purchase = 90-day access
                    plan = '90day'
                    from datetime import datetime, timedelta
                    # 90 days from purchase date
                    purchase_date = sale.get('created_at', '')
                    try:
                        pd = datetime.fromisoformat(purchase_date.replace('Z', '+00:00'))
                        expires = (pd + timedelta(days=90)).strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        expires = (datetime.utcnow() + timedelta(days=90)).strftime('%Y-%m-%d %H:%M:%S')
                
                # Activate the user
                conn.execute('''UPDATE users SET plan = ?, plan_expires_at = ? WHERE id = ?''',
                           (plan, expires, request.user['id']))
                conn.commit()
                conn.close()
                
                return jsonify({
                    'success': True,
                    'plan': plan,
                    'plan_expires_at': expires,
                    'message': f'Purchase verified! Plan: {plan}'
                })
            
            conn.close()
            return jsonify({'error': 'No active purchase found for this email.', 'needs_purchase': True}), 404
        else:
            return jsonify({'error': 'Could not verify purchase'}), 400
    except Exception as e:
        return jsonify({'error': f'Verification failed: {str(e)}'}), 500


@app.route('/api/plan', methods=['GET'])
@auth_required
def get_plan():
    """Check user's current plan status."""
    from datetime import datetime
    
    plan = request.user['plan'] or 'trial'
    expires = request.user['plan_expires_at']
    
    # Check if 90-day plan expired
    if plan == '90day' and expires:
        if datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') > expires:
            plan = 'expired'
    
    return jsonify({
        'plan': plan,
        'plan_expires_at': expires,
        'active': plan in ('monthly', '90day', 'trial'),
    })


# ============ CASES ============

@app.route('/api/cases', methods=['GET'])
@auth_required
def get_cases():
    conn = get_db()
    cases = conn.execute(
        'SELECT * FROM cases WHERE user_id = ? ORDER BY date DESC, id DESC',
        (request.user['id'],)
    ).fetchall()
    conn.close()
    return jsonify([dict(c) for c in cases])

@app.route('/api/cases', methods=['POST'])
@auth_required
def add_case():
    data = request.json
    conn = get_db()
    cursor = conn.execute('''
        INSERT INTO cases (user_id, date, age, sex, rotation, procedure_name, cpt_code, 
                          role, approach, attending, complications, ebl, or_time, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        request.user['id'],
        data.get('date'), data.get('age'), data.get('sex'),
        data.get('rotation'), data.get('procedure'), data.get('cpt'),
        data.get('role'), data.get('approach'), data.get('attending'),
        data.get('complications', 'None'), data.get('ebl'), data.get('orTime'),
        data.get('notes')
    ))
    case_id = cursor.lastrowid
    conn.commit()
    
    # Fetch and return the new case
    case = conn.execute('SELECT * FROM cases WHERE id = ?', (case_id,)).fetchone()
    conn.close()
    return jsonify(dict(case)), 201

@app.route('/api/cases/<int:case_id>', methods=['PUT'])
@auth_required
def update_case(case_id):
    data = request.json
    conn = get_db()
    
    # Verify ownership
    case = conn.execute('SELECT * FROM cases WHERE id = ? AND user_id = ?', 
                       (case_id, request.user['id'])).fetchone()
    if not case:
        conn.close()
        return jsonify({'error': 'Not found'}), 404
    
    conn.execute('''
        UPDATE cases SET date=?, age=?, sex=?, rotation=?, procedure_name=?, cpt_code=?,
        role=?, approach=?, attending=?, complications=?, ebl=?, or_time=?, notes=?,
        updated_at=datetime('now')
        WHERE id = ? AND user_id = ?
    ''', (
        data.get('date'), data.get('age'), data.get('sex'),
        data.get('rotation'), data.get('procedure'), data.get('cpt'),
        data.get('role'), data.get('approach'), data.get('attending'),
        data.get('complications', 'None'), data.get('ebl'), data.get('orTime'),
        data.get('notes'), case_id, request.user['id']
    ))
    conn.commit()
    
    updated = conn.execute('SELECT * FROM cases WHERE id = ?', (case_id,)).fetchone()
    conn.close()
    return jsonify(dict(updated))

@app.route('/api/cases/<int:case_id>', methods=['DELETE'])
@auth_required
def delete_case(case_id):
    conn = get_db()
    conn.execute('DELETE FROM cases WHERE id = ? AND user_id = ?', 
                (case_id, request.user['id']))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

# ============ MILESTONES ============

@app.route('/api/milestones', methods=['GET'])
@auth_required
def get_milestones():
    conn = get_db()
    milestones = conn.execute(
        'SELECT * FROM milestones WHERE user_id = ?', (request.user['id'],)
    ).fetchall()
    conn.close()
    return jsonify([dict(m) for m in milestones])

@app.route('/api/milestones', methods=['POST'])
@auth_required
def update_milestone():
    data = request.json
    conn = get_db()
    conn.execute('''
        INSERT INTO milestones (user_id, category, count) VALUES (?, ?, ?)
        ON CONFLICT(user_id, category) DO UPDATE SET count = ?
    ''', (request.user['id'], data['category'], data['count'], data['count']))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

# ============ STATS ============

@app.route('/api/stats', methods=['GET'])
@auth_required
def get_stats():
    conn = get_db()
    uid = request.user['id']
    
    total = conn.execute('SELECT COUNT(*) FROM cases WHERE user_id=?', (uid,)).fetchone()[0]
    primary = conn.execute("SELECT COUNT(*) FROM cases WHERE user_id=? AND role='Primary Surgeon'", (uid,)).fetchone()[0]
    assist = conn.execute("SELECT COUNT(*) FROM cases WHERE user_id=? AND role='First Assist'", (uid,)).fetchone()[0]
    comps = conn.execute("SELECT COUNT(*) FROM cases WHERE user_id=? AND complications != 'None' AND complications IS NOT NULL", (uid,)).fetchone()[0]
    avg_or = conn.execute("SELECT AVG(or_time) FROM cases WHERE user_id=? AND or_time > 0", (uid,)).fetchone()[0]
    lap = conn.execute("SELECT COUNT(*) FROM cases WHERE user_id=? AND approach='Laparoscopic'", (uid,)).fetchone()[0]
    robotic = conn.execute("SELECT COUNT(*) FROM cases WHERE user_id=? AND approach='Robotic'", (uid,)).fetchone()[0]
    open_cases = conn.execute("SELECT COUNT(*) FROM cases WHERE user_id=? AND approach='Open'", (uid,)).fetchone()[0]
    
    # Rotation breakdown
    rotations = conn.execute(
        "SELECT rotation, COUNT(*) as count FROM cases WHERE user_id=? GROUP BY rotation ORDER BY count DESC",
        (uid,)
    ).fetchall()
    
    conn.close()
    
    return jsonify({
        'total': total,
        'primary': primary,
        'assist': assist,
        'complications': comps,
        'compRate': round((comps/total)*100, 1) if total > 0 else 0,
        'avgOR': round(avg_or) if avg_or else 0,
        'laparoscopic': lap,
        'robotic': robotic,
        'open': open_cases,
        'rotations': [{'rotation': r['rotation'], 'count': r['count']} for r in rotations]
    })

# ============ STATIC FILES ============

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    init_db()
    print(f"✅ Database initialized at {DB_PATH}")
    print(f"🚀 Server starting on port 8080...")
    app.run(host='0.0.0.0', port=8080, debug=False)
