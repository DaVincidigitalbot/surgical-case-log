#!/usr/bin/env python3
"""
Clinical Case Log — Backend API
PostgreSQL database for persistent storage with user accounts.
"""
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import hashlib
import secrets
import json
from datetime import datetime
import psycopg2
from psycopg2.extras import RealDictCursor
import urllib.parse

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# PostgreSQL connection
DB_PASSWORD = urllib.parse.quote(os.environ.get('DB_PASSWORD', 'CaseLog2026!'))
DATABASE_URL = os.environ.get('DATABASE_URL', 
    f"postgresql://postgres.qooenxfumvitimfbuocp:{DB_PASSWORD}@aws-1-us-east-1.pooler.supabase.com:5432/postgres")

def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def init_db():
    """Initialize database tables if they don't exist."""
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                name TEXT,
                token TEXT UNIQUE,
                plan TEXT DEFAULT 'trial',
                license_key TEXT,
                plan_expires_at TEXT,
                created_at TIMESTAMP DEFAULT NOW()
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS cases (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
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
                diagnosis TEXT,
                created_at TIMESTAMP DEFAULT NOW(),
                updated_at TIMESTAMP DEFAULT NOW()
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS milestones (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                category TEXT NOT NULL,
                count INTEGER DEFAULT 0,
                UNIQUE(user_id, category)
            )
        ''')
        cur.execute('''
            CREATE TABLE IF NOT EXISTS user_attendings (
                id SERIAL PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES users(id),
                name TEXT NOT NULL,
                specialty TEXT,
                UNIQUE(user_id, name)
            )
        ''')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_cases_user ON cases(user_id)')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_cases_date ON cases(user_id, date)')
        cur.execute('CREATE INDEX IF NOT EXISTS idx_user_attendings_user ON user_attendings(user_id)')
        conn.commit()
        conn.close()
        print("[INIT] PostgreSQL database initialized successfully", flush=True)
    except Exception as e:
        print(f"[INIT] DB init error: {e}", flush=True)

init_db()

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
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM users WHERE token = %s', (token,))
        user = cur.fetchone()
        conn.close()
        return user
    except:
        return None

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
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT id FROM users WHERE email = %s', (email,))
    existing = cur.fetchone()
    if existing:
        conn.close()
        return jsonify({'error': 'Email already registered'}), 409
    
    token = secrets.token_urlsafe(32)
    pw_hash = hash_password(password)
    
    cur.execute('INSERT INTO users (email, password_hash, name, token) VALUES (%s, %s, %s, %s)',
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
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users WHERE email = %s', (email,))
    user = cur.fetchone()
    
    if not user or not verify_password(user['password_hash'], password):
        conn.close()
        return jsonify({'error': 'Invalid email or password'}), 401
    
    # Reuse existing token if present, otherwise generate new one
    token = user['token']
    if not token:
        token = secrets.token_urlsafe(32)
        cur.execute('UPDATE users SET token = %s WHERE id = %s', (token, user['id']))
        conn.commit()
    conn.close()
    
    return jsonify({'token': token, 'name': user['name'], 'email': user['email'], 'plan': user['plan'] or 'trial', 'plan_expires_at': user['plan_expires_at']})

# ============ TOKEN CHECK ============

@app.route('/api/me', methods=['GET'])
def check_token():
    token = request.headers.get('Authorization', '').replace('Bearer ', '')
    user = get_user_from_token(token)
    if not user:
        return jsonify({'error': 'Invalid token'}), 401
    return jsonify({'name': user['name'], 'email': user['email'], 'plan': user['plan'] or 'trial'})

# ============ LICENSE VERIFICATION ============

@app.route('/api/activate', methods=['POST'])
@auth_required
def activate_by_email():
    import requests as req
    user_email = request.user['email']
    GUMROAD_TOKEN = "X_X3q6Cw7bJuRkvmwKRGIwhN9Comr3wkjKkMXrv-ZFE"
    
    try:
        r = req.get(f'https://api.gumroad.com/v2/sales?access_token={GUMROAD_TOKEN}&email={user_email}', timeout=15)
        if r.status_code == 200:
            result = r.json()
            sales = result.get('sales', [])
            if not sales:
                return jsonify({'error': 'No purchase found for this email.', 'needs_purchase': True}), 404
            
            conn = get_db()
            cur = conn.cursor()
            for sale in sales:
                if sale.get('refunded') or sale.get('disputed'):
                    continue
                is_subscription = sale.get('subscription_id') is not None
                recurrence = sale.get('recurrence')
                if is_subscription or recurrence:
                    cancelled = sale.get('cancelled', False)
                    ended = sale.get('ended', False)
                    if not cancelled and not ended:
                        plan = 'subscription'
                        expires = None
                    else:
                        continue
                else:
                    plan = '90day'
                    from datetime import timedelta
                    purchase_date = sale.get('created_at', '')
                    try:
                        pd = datetime.fromisoformat(purchase_date.replace('Z', '+00:00'))
                        expires = (pd + timedelta(days=90)).strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        expires = (datetime.utcnow() + timedelta(days=90)).strftime('%Y-%m-%d %H:%M:%S')
                
                cur.execute('UPDATE users SET plan = %s, plan_expires_at = %s WHERE id = %s',
                           (plan, expires, request.user['id']))
                conn.commit()
                conn.close()
                return jsonify({'success': True, 'plan': plan, 'plan_expires_at': expires})
            
            conn.close()
            return jsonify({'error': 'No active purchase found.', 'needs_purchase': True}), 404
        else:
            return jsonify({'error': 'Could not verify purchase'}), 400
    except Exception as e:
        return jsonify({'error': f'Verification failed: {str(e)}'}), 500

@app.route('/api/plan', methods=['GET'])
@auth_required
def get_plan():
    plan = request.user['plan'] or 'trial'
    expires = request.user['plan_expires_at']
    if plan == '90day' and expires:
        if datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') > expires:
            plan = 'expired'
    return jsonify({'plan': plan, 'plan_expires_at': expires, 'active': plan in ('monthly', '90day', 'trial')})

# ============ CASES ============

@app.route('/api/cases', methods=['GET'])
@auth_required
def get_cases():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM cases WHERE user_id = %s ORDER BY date DESC, id DESC', (request.user['id'],))
    cases = cur.fetchall()
    conn.close()
    # Convert datetime objects to strings
    for c in cases:
        if c.get('created_at') and hasattr(c['created_at'], 'isoformat'):
            c['created_at'] = c['created_at'].isoformat()
        if c.get('updated_at') and hasattr(c['updated_at'], 'isoformat'):
            c['updated_at'] = c['updated_at'].isoformat()
    return jsonify(cases)

@app.route('/api/cases', methods=['POST'])
@auth_required
def add_case():
    data = request.json
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('''
        INSERT INTO cases (user_id, date, age, sex, rotation, procedure_name, cpt_code, 
                          role, approach, attending, complications, ebl, or_time, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING *
    ''', (
        request.user['id'],
        data.get('date'), data.get('age') or None, data.get('sex'),
        data.get('rotation'), data.get('procedure'), data.get('cpt'),
        data.get('role'), data.get('approach'), data.get('attending'),
        data.get('complications', 'None'), data.get('ebl') or None, data.get('orTime') or None,
        data.get('notes')
    ))
    case = cur.fetchone()
    conn.commit()
    conn.close()
    if case.get('created_at') and hasattr(case['created_at'], 'isoformat'):
        case['created_at'] = case['created_at'].isoformat()
    if case.get('updated_at') and hasattr(case['updated_at'], 'isoformat'):
        case['updated_at'] = case['updated_at'].isoformat()
    return jsonify(case), 201

@app.route('/api/cases/<int:case_id>', methods=['PUT'])
@auth_required
def update_case(case_id):
    data = request.json
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM cases WHERE id = %s AND user_id = %s', (case_id, request.user['id']))
    case = cur.fetchone()
    if not case:
        conn.close()
        return jsonify({'error': 'Not found'}), 404
    
    cur.execute('''
        UPDATE cases SET date=%s, age=%s, sex=%s, rotation=%s, procedure_name=%s, cpt_code=%s,
        role=%s, approach=%s, attending=%s, complications=%s, ebl=%s, or_time=%s, notes=%s,
        updated_at=NOW()
        WHERE id = %s AND user_id = %s RETURNING *
    ''', (
        data.get('date'), data.get('age') or None, data.get('sex'),
        data.get('rotation'), data.get('procedure'), data.get('cpt'),
        data.get('role'), data.get('approach'), data.get('attending'),
        data.get('complications', 'None'), data.get('ebl') or None, data.get('orTime') or None,
        data.get('notes'), case_id, request.user['id']
    ))
    updated = cur.fetchone()
    conn.commit()
    conn.close()
    if updated.get('created_at') and hasattr(updated['created_at'], 'isoformat'):
        updated['created_at'] = updated['created_at'].isoformat()
    if updated.get('updated_at') and hasattr(updated['updated_at'], 'isoformat'):
        updated['updated_at'] = updated['updated_at'].isoformat()
    return jsonify(updated)

@app.route('/api/cases/<int:case_id>', methods=['DELETE'])
@auth_required
def delete_case(case_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM cases WHERE id = %s AND user_id = %s', (case_id, request.user['id']))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

# ============ MILESTONES ============

@app.route('/api/milestones', methods=['GET'])
@auth_required
def get_milestones():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM milestones WHERE user_id = %s', (request.user['id'],))
    milestones = cur.fetchall()
    conn.close()
    return jsonify(milestones)

@app.route('/api/milestones', methods=['POST'])
@auth_required
def update_milestone():
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO milestones (user_id, category, count) VALUES (%s, %s, %s)
        ON CONFLICT(user_id, category) DO UPDATE SET count = %s
    ''', (request.user['id'], data['category'], data['count'], data['count']))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

# ============ ATTENDINGS ============

@app.route('/api/attendings', methods=['GET'])
@auth_required
def get_attendings():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT id, name, specialty FROM user_attendings WHERE user_id = %s ORDER BY name ASC', (request.user['id'],))
    attendings = cur.fetchall()
    conn.close()
    return jsonify(attendings)

@app.route('/api/attendings', methods=['POST'])
@auth_required
def add_attending():
    data = request.json
    name = (data.get('name') or '').strip()
    specialty = (data.get('specialty') or '').strip() or None
    if not name:
        return jsonify({'error': 'Name is required'}), 400
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('INSERT INTO user_attendings (user_id, name, specialty) VALUES (%s, %s, %s) RETURNING id, name, specialty',
                     (request.user['id'], name, specialty))
        attending = cur.fetchone()
        conn.commit()
        conn.close()
        return jsonify(attending), 201
    except psycopg2.errors.UniqueViolation:
        return jsonify({'error': 'Attending already saved'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/attendings/<int:attending_id>', methods=['DELETE'])
@auth_required
def delete_attending(attending_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM user_attendings WHERE id = %s AND user_id = %s', (attending_id, request.user['id']))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    if deleted == 0:
        return jsonify({'error': 'Not found'}), 404
    return jsonify({'success': True})

# ============ STATS ============

@app.route('/api/stats', methods=['GET'])
@auth_required
def get_stats():
    conn = get_db()
    cur = conn.cursor()
    uid = request.user['id']
    
    cur.execute('SELECT COUNT(*) FROM cases WHERE user_id=%s', (uid,))
    total = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM cases WHERE user_id=%s AND role='Primary Surgeon'", (uid,))
    primary = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM cases WHERE user_id=%s AND role='First Assist'", (uid,))
    assist = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM cases WHERE user_id=%s AND complications != 'None' AND complications IS NOT NULL", (uid,))
    comps = cur.fetchone()[0]
    cur.execute("SELECT AVG(or_time) FROM cases WHERE user_id=%s AND or_time > 0", (uid,))
    avg_or = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM cases WHERE user_id=%s AND approach='Laparoscopic'", (uid,))
    lap = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM cases WHERE user_id=%s AND approach='Robotic'", (uid,))
    robotic = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM cases WHERE user_id=%s AND approach='Open'", (uid,))
    open_cases = cur.fetchone()[0]
    
    cur2 = conn.cursor(cursor_factory=RealDictCursor)
    cur2.execute("SELECT rotation, COUNT(*) as count FROM cases WHERE user_id=%s GROUP BY rotation ORDER BY count DESC", (uid,))
    rotations = cur2.fetchall()
    
    conn.close()
    
    return jsonify({
        'total': total, 'primary': primary, 'assist': assist,
        'complications': comps,
        'compRate': round((comps/total)*100, 1) if total > 0 else 0,
        'avgOR': round(float(avg_or)) if avg_or else 0,
        'laparoscopic': lap, 'robotic': robotic, 'open': open_cases,
        'rotations': rotations
    })

# ============ ADMIN PANEL ============

ADMIN_SECRET = 'stallard2026admin'

@app.route('/admin')
def admin_panel():
    key = request.args.get('key', '')
    if key != ADMIN_SECRET:
        return '<h1>Access Denied</h1>', 403
    return send_from_directory('.', 'admin.html')

@app.route('/api/admin/overview', methods=['GET'])
def admin_overview():
    key = request.args.get('key', '') or request.headers.get('X-Admin-Key', '')
    if key != ADMIN_SECRET:
        return jsonify({'error': 'Access denied'}), 403
    
    try:
        conn = get_db()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute('SELECT id, email, name, plan, plan_expires_at, created_at FROM users ORDER BY created_at DESC')
        users = cur.fetchall()
        
        cur.execute('SELECT * FROM cases ORDER BY created_at DESC')
        cases_raw = cur.fetchall()
        
        cases = []
        for c in cases_raw:
            cur.execute('SELECT email, name FROM users WHERE id = %s', (c.get('user_id'),))
            user = cur.fetchone()
            c['user_email'] = user['email'] if user else 'unknown'
            c['user_name'] = user['name'] if user else 'unknown'
            if c.get('created_at') and hasattr(c['created_at'], 'isoformat'):
                c['created_at'] = c['created_at'].isoformat()
            if c.get('updated_at') and hasattr(c['updated_at'], 'isoformat'):
                c['updated_at'] = c['updated_at'].isoformat()
            cases.append(c)
        
        # Fix user timestamps too
        for u in users:
            if u.get('created_at') and hasattr(u['created_at'], 'isoformat'):
                u['created_at'] = u['created_at'].isoformat()
        
        conn.close()
        
        return jsonify({
            'total_users': len(users),
            'total_cases': len(cases),
            'users': users,
            'cases': cases
        })
    except Exception as e:
        import traceback
        return jsonify({'error': str(e), 'trace': traceback.format_exc(), 'total_users': 0, 'total_cases': 0, 'users': [], 'cases': []})

# ============ STATIC FILES ============

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/preview')
def preview():
    return send_from_directory('.', 'index.html')

@app.route('/api/preview-login', methods=['POST'])
def preview_login():
    conn = get_db()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    email = 'admin@clinicalcaselog.com'
    cur.execute('SELECT * FROM users WHERE email = %s', (email,))
    user = cur.fetchone()
    
    if not user:
        token = secrets.token_urlsafe(32)
        pw_hash = hash_password('preview123')
        cur.execute('INSERT INTO users (email, password_hash, name, token, plan) VALUES (%s, %s, %s, %s, %s)',
                     (email, pw_hash, 'Admin Preview', token, 'subscription'))
        conn.commit()
    else:
        token = user['token']
    
    conn.close()
    return jsonify({'token': token, 'name': 'Admin Preview', 'email': email, 'plan': 'subscription'})

if __name__ == '__main__':
    print(f"🚀 Server starting on port 8080...")
    app.run(host='0.0.0.0', port=8080, debug=False)
