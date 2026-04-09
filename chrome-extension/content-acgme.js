// ============================================================
// Clinical Case Log → ACGME Export — Content Script
// Runs on apps.acgme.org to assist with case entry
// ============================================================

(async function() {
  // Check if we have pending cases to export
  const response = await chrome.runtime.sendMessage({ type: 'GET_PENDING_EXPORT' });
  
  if (!response || !response.cases || response.cases.length === 0) return;
  
  // Run through ACGME filter — strip any non-ACGME fields that may have leaked through
  const cases = response.cases.map(c => {
    // ONLY pass ACGME-accepted fields — everything else is dropped
    return {
      dateOfProcedure: c.dateOfProcedure || null,
      cptCode: c.cptCode || null,
      role: c.role || null,
      attending: c.attending || null,
      site: c.site || null,
      caseId: c.caseId || null,
      patientType: c.patientType || null,
      equipment: c.equipment || null,
      rrcCodes: c.rrcCodes || null,
    };
  });
  
  // Create floating helper panel
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
        Click "Fill Next Case" to auto-populate the ACGME form with your case data.
        Review each entry before submitting.
      </div>
      <div class="ccl-case-info" id="ccl-current-case"></div>
      <button class="ccl-btn ccl-btn-primary" id="ccl-fill-btn">
        Fill Next Case
      </button>
      <div class="ccl-progress" id="ccl-progress">
        Case <span id="ccl-current-num">0</span> of ${cases.length}
      </div>
    </div>
  `;
  document.body.appendChild(panel);
  
  let currentIndex = 0;
  
  // Fill next case into ACGME form
  window.__cclFillNext = function() {
    if (currentIndex >= cases.length) {
      document.getElementById('ccl-fill-btn').textContent = 'All Done! ✓';
      document.getElementById('ccl-fill-btn').disabled = true;
      return;
    }
    
    const c = cases[currentIndex];
    currentIndex++;
    document.getElementById('ccl-current-num').textContent = currentIndex;
    
    // Display current case info
    document.getElementById('ccl-current-case').innerHTML = `
      <div class="ccl-case-detail"><strong>Date:</strong> ${c.dateOfProcedure}</div>
      <div class="ccl-case-detail"><strong>CPT:</strong> ${c.cptCode}</div>
      <div class="ccl-case-detail"><strong>Role:</strong> ${c.role}</div>
      <div class="ccl-case-detail"><strong>Attending:</strong> ${c.attending}</div>
      ${c.site ? `<div class="ccl-case-detail"><strong>Site:</strong> ${c.site}</div>` : ''}
    `;
    
    // Try to auto-fill ACGME form fields
    // These selectors target the ACGME ADS Case Log form
    tryFill('input[name*="date" i], input[id*="date" i], input[placeholder*="date" i]', c.dateOfProcedure);
    tryFill('input[name*="cpt" i], input[id*="cpt" i], input[placeholder*="cpt" i]', c.cptCode);
    tryFill('input[name*="attending" i], input[id*="attending" i], select[name*="attending" i]', c.attending);
    tryFill('select[name*="role" i], select[id*="role" i]', c.role);
    tryFill('select[name*="site" i], input[name*="site" i], select[id*="site" i]', c.site);
    tryFill('input[name*="caseid" i], input[id*="caseid" i]', c.caseId);
    
    // Update button text
    if (currentIndex >= cases.length) {
      document.getElementById('ccl-fill-btn').textContent = 'All Cases Filled ✓';
    } else {
      document.getElementById('ccl-fill-btn').textContent = `Fill Next Case (${cases.length - currentIndex} remaining)`;
    }
  };

  const fillBtn = document.getElementById('ccl-fill-btn');
  if (fillBtn) {
    fillBtn.addEventListener('click', () => window.__cclFillNext());
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
      if (el.shadowRoot) {
        roots.push(...getSearchRoots(el.shadowRoot, seen));
      }
      if (el.tagName === 'IFRAME') {
        try {
          if (el.contentDocument) {
            roots.push(...getSearchRoots(el.contentDocument, seen));
          }
        } catch (e) {
          // Cross-origin or inaccessible frame, skip
        }
      }
    }

    return roots;
  }

  function findField(selector) {
    const roots = getSearchRoots(document);
    for (const root of roots) {
      try {
        const el = root.querySelector(selector);
        if (el) return el;
      } catch (e) {}
    }
    return null;
  }

  function tryFill(selector, value) {
    if (!value) return;
    const el = findField(selector);
    if (!el) return;
    
    if (el.tagName === 'SELECT') {
      // Try to find matching option
      const options = Array.from(el.options);
      const match = options.find(o => 
        o.value.toLowerCase() === value.toLowerCase() || 
        o.textContent.toLowerCase().includes(value.toLowerCase())
      );
      if (match) {
        el.value = match.value;
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
      }
    } else {
      el.value = value;
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    }
  }
})();
