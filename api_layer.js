// ============ API LAYER ============
const API_BASE = window.location.origin + '/api';

let authToken = localStorage.getItem('authToken');
let currentUser = JSON.parse(localStorage.getItem('currentUser') || 'null');

async function apiCall(endpoint, method = 'GET', body = null) {
    const opts = {
        method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + (authToken || '')
        }
    };
    if (body) opts.body = JSON.stringify(body);
    const r = await fetch(API_BASE + endpoint, opts);
    if (r.status === 401) {
        showAuth();
        throw new Error('Unauthorized');
    }
    return r.json();
}

async function syncCasesToServer() {
    // Upload local cases that aren't on server yet
    const localCases = JSON.parse(localStorage.getItem('surgicalCases') || '[]');
    if (localCases.length > 0 && authToken) {
        for (const c of localCases) {
            if (!c.synced) {
                try {
                    await apiCall('/cases', 'POST', c);
                    c.synced = true;
                } catch(e) { console.error('Sync failed:', e); }
            }
        }
        localStorage.setItem('surgicalCases', JSON.stringify(localCases));
    }
}

async function loadCasesFromServer() {
    try {
        const serverCases = await apiCall('/cases');
        cases = serverCases.map(c => ({
            id: c.id,
            date: c.date,
            age: c.age,
            sex: c.sex,
            rotation: c.rotation,
            procedure: c.procedure_name,
            cpt: c.cpt_code,
            role: c.role,
            approach: c.approach,
            attending: c.attending,
            complications: c.complications,
            ebl: c.ebl,
            orTime: c.or_time,
            notes: c.notes,
            synced: true
        }));
        saveCases();
        updateDashboard();
        renderCases();
    } catch(e) { console.error('Load failed:', e); }
}
