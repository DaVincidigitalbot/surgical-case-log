// ============================================================
// Clinical Case Log → ACGME Export — Content Script
// Runs on apps.acgme.org to assist with case entry
// ============================================================

(async function() {
  const response = await chrome.runtime.sendMessage({ type: 'GET_PENDING_EXPORT' });
  if (!response || !response.cases || response.cases.length === 0) return;

  const cases = response.cases.map(c => ({
    dateOfProcedure: c.dateOfProcedure || null,
    cptCode: c.cptCode || null,
    role: c.role || null,
    attending: c.attending || null,
    site: c.site || null,
    caseId: c.caseId || null,
    patientType: c.patientType || null,
    equipment: c.equipment || null,
    rrcCodes: c.rrcCodes || null,
  }));

  const state = {
    currentIndex: 0,
    cases,
    lastFillReport: null,
  };

  const panel = document.createElement('div');
  panel.id = 'ccl-export-panel';
  panel.innerHTML = `
    <div class="ccl-header">
      <span class="ccl-logo">CL</span>
      <span class="ccl-title">Clinical Case Log Export</span>
      <button class="ccl-close" onclick="document.getElementById('ccl-export-panel').remove()">✕</button>
    </div>
    <div class="ccl-body">
      <div class="ccl-count">${cases.length} case${cases.length > 1 ? 's' : ''} ready to enter</div>
      <div class="ccl-instructions">
        Click <strong>Fill Next Case</strong> on the ACGME entry page. The extension will match visible fields,
        fill what it can, and tell you exactly what still needs manual review.
      </div>
      <div class="ccl-case-info" id="ccl-current-case"></div>
      <button class="ccl-btn ccl-btn-primary" id="ccl-fill-btn">Fill Next Case</button>
      <div class="ccl-progress" id="ccl-progress">Case <span id="ccl-current-num">0</span> of ${cases.length}</div>
      <div class="ccl-case-info" id="ccl-fill-report" style="margin-top:10px;"></div>
    </div>
  `;
  document.body.appendChild(panel);

  const FIELDS = [
    {
      key: 'dateOfProcedure',
      label: 'Date of Procedure',
      valueType: 'text',
      selectors: [
        'input[type="date"]',
        'input[name*="date" i]',
        'input[id*="date" i]',
        'input[placeholder*="date" i]',
        'input[aria-label*="date" i]'
      ]
    },
    {
      key: 'cptCode',
      label: 'CPT Code',
      valueType: 'text',
      selectors: [
        'input[name*="cpt" i]',
        'input[id*="cpt" i]',
        'input[placeholder*="cpt" i]',
        'input[aria-label*="cpt" i]',
        'input[name*="procedure" i]',
        'input[id*="procedure" i]'
      ]
    },
    {
      key: 'role',
      label: 'Role',
      valueType: 'select',
      selectors: [
        'select[name*="role" i]',
        'select[id*="role" i]',
        'select[aria-label*="role" i]'
      ]
    },
    {
      key: 'attending',
      label: 'Attending',
      valueType: 'smart',
      selectors: [
        'select[name*="attending" i]',
        'select[id*="attending" i]',
        'select[aria-label*="attending" i]',
        'input[name*="attending" i]',
        'input[id*="attending" i]',
        'input[aria-label*="attending" i]',
        'input[placeholder*="attending" i]'
      ]
    },
    {
      key: 'site',
      label: 'Site',
      valueType: 'smart',
      selectors: [
        'select[name*="site" i]',
        'select[id*="site" i]',
        'select[aria-label*="site" i]',
        'select[name*="institution" i]',
        'select[id*="institution" i]',
        'input[name*="site" i]',
        'input[id*="site" i]',
        'input[aria-label*="site" i]',
        'input[name*="institution" i]',
        'input[id*="institution" i]'
      ]
    },
    {
      key: 'caseId',
      label: 'Case ID',
      valueType: 'text',
      selectors: [
        'input[name*="caseid" i]',
        'input[id*="caseid" i]',
        'input[name*="case id" i]',
        'input[id*="case id" i]'
      ]
    },
    {
      key: 'patientType',
      label: 'Patient Type',
      valueType: 'smart',
      selectors: [
        'select[name*="patient" i]',
        'select[id*="patient" i]',
        'input[name*="patient" i]',
        'input[id*="patient" i]'
      ]
    }
  ];

  window.__cclFillNext = function() {
    const fillBtn = document.getElementById('ccl-fill-btn');
    const reportEl = document.getElementById('ccl-fill-report');

    if (state.currentIndex >= state.cases.length) {
      fillBtn.textContent = 'All Done! ✓';
      fillBtn.disabled = true;
      return;
    }

    const c = state.cases[state.currentIndex];
    state.currentIndex += 1;
    document.getElementById('ccl-current-num').textContent = state.currentIndex;

    document.getElementById('ccl-current-case').innerHTML = `
      <div class="ccl-case-detail"><strong>Date:</strong> ${escapeHtml(c.dateOfProcedure || '—')}</div>
      <div class="ccl-case-detail"><strong>CPT:</strong> ${escapeHtml(c.cptCode || '—')}</div>
      <div class="ccl-case-detail"><strong>Role:</strong> ${escapeHtml(c.role || '—')}</div>
      <div class="ccl-case-detail"><strong>Attending:</strong> ${escapeHtml(c.attending || '—')}</div>
      ${c.site ? `<div class="ccl-case-detail"><strong>Site:</strong> ${escapeHtml(c.site)}</div>` : ''}
    `;

    const fillResults = FIELDS.map(field => fillField(field, c[field.key]));
    state.lastFillReport = fillResults;

    const filled = fillResults.filter(r => r.status === 'filled');
    const unresolved = fillResults.filter(r => r.status !== 'filled' && r.value);

    reportEl.innerHTML = `
      <div class="ccl-case-detail"><strong>Filled:</strong> ${filled.map(r => escapeHtml(r.label)).join(', ') || 'None'}</div>
      <div class="ccl-case-detail"><strong>Needs review:</strong> ${unresolved.map(r => `${escapeHtml(r.label)} (${escapeHtml(r.reason)})`).join(', ') || 'None'}</div>
    `;

    if (state.currentIndex >= state.cases.length) {
      fillBtn.textContent = 'All Cases Filled ✓';
    } else {
      fillBtn.textContent = `Fill Next Case (${state.cases.length - state.currentIndex} remaining)`;
    }
  };

  const fillBtn = document.getElementById('ccl-fill-btn');
  if (fillBtn) fillBtn.addEventListener('click', () => window.__cclFillNext());

  function escapeHtml(value) {
    return String(value)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#39;');
  }

  function getSearchRoots(root = document, seen = new Set()) {
    const roots = [];
    if (!root || seen.has(root)) return roots;
    seen.add(root);
    roots.push(root);

    let elements = [];
    try {
      elements = Array.from(root.querySelectorAll('*'));
    } catch (e) {
      return roots;
    }

    for (const el of elements) {
      if (el.shadowRoot) roots.push(...getSearchRoots(el.shadowRoot, seen));
      if (el.tagName === 'IFRAME') {
        try {
          if (el.contentDocument) roots.push(...getSearchRoots(el.contentDocument, seen));
        } catch (e) {}
      }
    }
    return roots;
  }

  function getCandidateElements(selectorList) {
    const roots = getSearchRoots(document);
    const matches = [];
    const seen = new Set();
    for (const root of roots) {
      for (const selector of selectorList) {
        let found = [];
        try {
          found = Array.from(root.querySelectorAll(selector));
        } catch (e) {
          continue;
        }
        for (const el of found) {
          if (seen.has(el)) continue;
          seen.add(el);
          matches.push(el);
        }
      }
    }
    return matches.filter(isUsableField);
  }

  function isUsableField(el) {
    if (!el) return false;
    if (el.disabled || el.readOnly) return false;
    if (!(el instanceof HTMLElement)) return false;
    const style = window.getComputedStyle(el);
    if (style.display === 'none' || style.visibility === 'hidden') return false;
    const rect = el.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  }

  function scoreElement(el, expectedLabel) {
    const text = [
      el.name,
      el.id,
      el.placeholder,
      el.getAttribute('aria-label'),
      el.labels ? Array.from(el.labels).map(l => l.textContent).join(' ') : '',
      el.closest('label')?.textContent,
      el.closest('[role="group"], .form-group, .field, td, tr, div')?.textContent,
    ].filter(Boolean).join(' ').toLowerCase();

    let score = 0;
    const label = expectedLabel.toLowerCase();
    if (text.includes(label)) score += 10;
    for (const word of label.split(/\s+/)) {
      if (word && text.includes(word)) score += 2;
    }
    if (el.tagName === 'SELECT') score += 1;
    return score;
  }

  function fillField(field, value) {
    if (!value) return { key: field.key, label: field.label, status: 'skipped', reason: 'no value', value };

    const candidates = getCandidateElements(field.selectors)
      .map(el => ({ el, score: scoreElement(el, field.label) }))
      .sort((a, b) => b.score - a.score);

    if (!candidates.length) {
      return { key: field.key, label: field.label, status: 'unfilled', reason: 'field not found', value };
    }

    for (const { el } of candidates) {
      const ok = applyValue(el, value, field.valueType);
      if (ok) {
        highlight(el);
        return { key: field.key, label: field.label, status: 'filled', reason: 'matched', value };
      }
    }

    return { key: field.key, label: field.label, status: 'unfilled', reason: 'no matching option', value };
  }

  function applyValue(el, value, valueType) {
    if (el.tagName === 'SELECT' || valueType === 'select') {
      return fillSelect(el, value);
    }
    if (valueType === 'smart' && el.tagName === 'SELECT') {
      return fillSelect(el, value);
    }
    return fillInput(el, value);
  }

  function fillInput(el, value) {
    try {
      el.focus();
      const nativeSetter = Object.getOwnPropertyDescriptor(Object.getPrototypeOf(el), 'value')?.set;
      if (nativeSetter) nativeSetter.call(el, value);
      else el.value = value;
      dispatchInputEvents(el);
      return normalizeText(el.value) === normalizeText(value) || normalizeText(el.value).includes(normalizeText(value));
    } catch (e) {
      return false;
    }
  }

  function fillSelect(el, value) {
    const normalized = normalizeText(value);
    const options = Array.from(el.options || []);
    const exact = options.find(o => normalizeText(o.value) === normalized || normalizeText(o.textContent) === normalized);
    const contains = options.find(o => normalizeText(o.textContent).includes(normalized) || normalized.includes(normalizeText(o.textContent)));
    const match = exact || contains;
    if (!match) return false;
    el.value = match.value;
    dispatchInputEvents(el);
    return true;
  }

  function normalizeText(value) {
    return String(value || '').trim().toLowerCase().replace(/\s+/g, ' ');
  }

  function dispatchInputEvents(el) {
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
    el.dispatchEvent(new Event('blur', { bubbles: true }));
  }

  function highlight(el) {
    const original = el.style.outline;
    el.style.outline = '2px solid #2EA8FF';
    setTimeout(() => { el.style.outline = original; }, 2000);
  }
})();
