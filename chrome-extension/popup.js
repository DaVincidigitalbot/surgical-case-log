// ============================================================
// Clinical Case Log → ACGME Export — Popup Controller
// ============================================================

const API_BASE = 'https://clinicalcaselog.com/api';

// Role mapping: our system → ACGME codes
const ROLE_MAP = {
  'Primary Surgeon': 'SC',
  'primary': 'SC',
  'Chief Surgeon': 'SC',
  'Junior Surgeon': 'SJ',
  'Teaching Assistant': 'TA',
  'teaching': 'TA',
  'First Assistant': 'FA',
  'first_assist': 'FA',
  'assist': 'FA',
};

// ACGME-safe fields only
const ACGME_FIELDS = [
  'dateOfProcedure', 'cptCode', 'role', 'attending',
  'site', 'caseId', 'patientType', 'equipment', 'rrcCodes'
];

let allCases = [];
let selectedIds = new Set();

// ---- Init ----
document.addEventListener('DOMContentLoaded', async () => {
  const settings = await chrome.storage.local.get(['apiToken', 'defaultSite']);
  if (settings.apiToken) {
    document.getElementById('apiToken').value = '••••••••';
    await loadCases(settings.apiToken);
  } else {
    setStatus('disconnected', 'No API token — go to Settings to connect');
    document.getElementById('caseList').innerHTML =
      '<p style="text-align:center;color:#888;padding:20px;font-size:13px;">Connect your Clinical Case Log account in Settings to get started.</p>';
  }
  if (settings.defaultSite) {
    document.getElementById('defaultSite').value = settings.defaultSite;
  }
});

// ---- Load cases from Clinical Case Log API ----
async function loadCases(token) {
  setStatus('loading', 'Loading cases...');
  try {
    const resp = await fetch(`${API_BASE}/cases`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!resp.ok) {
      if (resp.status === 401) {
        setStatus('disconnected', 'Invalid token — update in Settings');
        return;
      }
      throw new Error(`HTTP ${resp.status}`);
    }
    const data = await resp.json();
    allCases = (data.cases || data || []).map(c => ({
      id: c.id,
      date: c.date || c.case_date || c.dateOfProcedure,
      procedure: c.procedure || c.procedure_name || '',
      cptCode: c.cpt_code || c.cptCode || '',
      role: c.role || 'Primary Surgeon',
      attending: c.attending || '',
      site: c.site || c.institution || '',
      caseId: c.case_id || c.caseId || '',
      patientType: c.patient_type || c.patientType || '',
      exported: c.acgme_exported || false,
    }));

    const unexported = allCases.filter(c => !c.exported);
    
    setStatus('connected', `Connected — ${allCases.length} total cases`);
    document.getElementById('caseCountSection').style.display = 'block';
    document.getElementById('unexportedCount').textContent = unexported.length;
    document.getElementById('selectBar').style.display = 'flex';

    renderCaseList(unexported.length > 0 ? unexported : allCases);
  } catch (e) {
    setStatus('disconnected', 'Connection failed — check Settings');
    console.error('Load error:', e);
  }
}

// ---- Render case list ----
function renderCaseList(cases) {
  const list = document.getElementById('caseList');
  if (cases.length === 0) {
    list.innerHTML = '<p style="text-align:center;color:#888;padding:20px;font-size:13px;">No cases to export. Log some cases first!</p>';
    return;
  }
  list.innerHTML = cases.map(c => {
    const checked = selectedIds.has(c.id) ? 'checked' : '';
    const dateStr = c.date ? new Date(c.date).toLocaleDateString('en-US', {month:'short', day:'numeric'}) : '';
    const name = c.procedure || `CPT ${c.cptCode}`;
    return `
      <label class="case-item">
        <input type="checkbox" value="${c.id}" ${checked} onchange="toggleCase(${c.id})">
        <span class="case-name" title="${name}">${name}</span>
        <span class="case-cpt">${c.cptCode || '—'}</span>
        <span class="case-date">${dateStr}</span>
      </label>`;
  }).join('');
  updateExportBtn();
}

// ---- Selection ----
function toggleCase(id) {
  if (selectedIds.has(id)) selectedIds.delete(id);
  else selectedIds.add(id);
  updateExportBtn();
}

function selectAll() {
  const checkboxes = document.querySelectorAll('#caseList input[type="checkbox"]');
  checkboxes.forEach(cb => { cb.checked = true; selectedIds.add(parseInt(cb.value)); });
  updateExportBtn();
}

function selectNone() {
  const checkboxes = document.querySelectorAll('#caseList input[type="checkbox"]');
  checkboxes.forEach(cb => { cb.checked = false; });
  selectedIds.clear();
  updateExportBtn();
}

function updateExportBtn() {
  const btn = document.getElementById('exportBtn');
  const count = selectedIds.size;
  btn.disabled = count === 0;
  btn.textContent = count > 0 ? `Export ${count} Case${count > 1 ? 's' : ''} to ACGME` : 'Export Selected to ACGME';
}

// ---- Export ----
async function exportSelected() {
  if (selectedIds.size === 0) return;

  const settings = await chrome.storage.local.get(['defaultSite']);
  const defaultSite = settings.defaultSite || '';

  // Run ALL cases through the ACGME filter — strips non-ACGME fields
  const selectedCases = allCases.filter(c => selectedIds.has(c.id));
  const casesToExport = selectedCases.map(c => {
    // Map to ACGME-safe format — ONLY these fields pass through
    return {
      dateOfProcedure: c.date || null,
      cptCode: c.cptCode || null,
      role: ROLE_MAP[c.role] || ROLE_MAP[(c.role||'').toLowerCase()] || 'SC',
      attending: c.attending || null,
      site: c.site || defaultSite || null,
      caseId: c.caseId || null,
      patientType: c.patientType || null,
    };
    // BLOCKED: age, sex, rotation, diagnosis, icd10, approach, ebl, orTime, complications, notes
  });

  // Validate required ACGME fields
  const invalid = casesToExport.filter(c => !c.dateOfProcedure || !c.cptCode || !c.role || !c.attending);
  if (invalid.length > 0) {
    showMsg('error', `${invalid.length} case(s) missing required ACGME fields (Date, CPT Code, Role, or Attending). Complete them in Clinical Case Log first.`);
    return;
  }

  // Store for content script to pick up
  await chrome.storage.local.set({
    pendingExport: casesToExport,
    exportTimestamp: Date.now()
  });

  showMsg('success', `${casesToExport.length} case(s) ready! Opening ACGME Case Log System...`);

  // Open ACGME in new tab
  setTimeout(() => {
    chrome.tabs.create({ url: 'https://apps.acgme.org/ads/caselog' });
  }, 1000);

  // Mark as exported in our system
  const token = (await chrome.storage.local.get(['apiToken'])).apiToken;
  if (token) {
    try {
      await fetch(`${API_BASE}/cases/mark-exported`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ caseIds: [...selectedIds] })
      });
    } catch (e) {
      console.warn('Could not mark as exported:', e);
    }
  }
}

// ---- ACGME ----
function openACGME() {
  chrome.tabs.create({ url: 'https://apps.acgme.org/ads/caselog' });
}

// ---- Settings ----
async function saveSettings() {
  const tokenInput = document.getElementById('apiToken').value;
  const site = document.getElementById('defaultSite').value;

  const toSave = { defaultSite: site };

  // Only save token if it's not the masked placeholder
  if (tokenInput && !tokenInput.startsWith('••')) {
    toSave.apiToken = tokenInput;
  }

  await chrome.storage.local.set(toSave);

  // Test connection with token
  const stored = await chrome.storage.local.get(['apiToken']);
  if (stored.apiToken) {
    await loadCases(stored.apiToken);
  }

  showMsg('success', 'Settings saved!');
  setTimeout(() => switchTab('export'), 1500);
}

// ---- Tabs ----
function switchTab(tab) {
  document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
  document.querySelector(`.tab[data-tab="${tab}"]`).classList.add('active');
  document.getElementById('exportView').className = tab === 'export' ? 'active' : '';
  document.getElementById('settingsView').className = tab === 'settings' ? 'active' : '';
}

// ---- UI Helpers ----
function setStatus(state, text) {
  const dot = document.getElementById('statusDot');
  dot.className = `status-dot ${state}`;
  document.getElementById('statusText').textContent = text;
}

function showMsg(type, text) {
  const box = document.getElementById('msgBox');
  box.className = `msg ${type}`;
  box.textContent = text;
  if (type === 'success') setTimeout(() => { box.className = 'msg'; }, 5000);
}
