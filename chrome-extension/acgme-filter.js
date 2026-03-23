/**
 * ACGME Field Filtering System for Clinical Case Log Pro
 * 
 * This module ensures ONLY ACGME-required fields are exported/synced.
 * Non-ACGME fields are stripped to prevent data corruption in the
 * ACGME Case Log System (ADS).
 * 
 * Reference: ACGME Case Log Coding Guidelines (280), 03/2021
 */

// ============================================================
// ACGME FIELD DEFINITIONS
// ============================================================

/**
 * The ONLY fields accepted by the ACGME Case Log System.
 * Any field not in this list MUST be blocked from export.
 */
const ACGME_REQUIRED_FIELDS = Object.freeze({
  dateOfProcedure: { required: true,  type: 'date',   acgmeName: 'Date of Procedure' },
  cptCode:         { required: true,  type: 'string', acgmeName: 'CPT Code' },
  role:            { required: true,  type: 'string', acgmeName: 'Role' },
  attending:       { required: true,  type: 'string', acgmeName: 'Attending' },
  site:            { required: true,  type: 'string', acgmeName: 'Site/Institution' },
  caseId:          { required: false, type: 'string', acgmeName: 'Case ID' },
  patientType:     { required: false, type: 'string', acgmeName: 'Patient Type' },
  equipment:       { required: false, type: 'string', acgmeName: 'Equipment' },
  rrcCodes:        { required: false, type: 'array',  acgmeName: 'RRC Codes (Critical Care)' },
});

/**
 * Fields that exist in our system but MUST NEVER be sent to ACGME.
 * Sending these would cause validation errors or data corruption.
 */
const BLOCKED_FIELDS = Object.freeze([
  'age',
  'sex',
  'rotation',
  'procedure_name',  // ACGME uses CPT codes, not procedure names
  'procedureName',
  'diagnosis',
  'icdCode',
  'ebl',
  'orTime',
  'or_time',
  'approach',        // Captured implicitly by CPT code
  'complications',
  'notes',
  'id',              // Internal DB ID
  'user_id',
  'userId',
  'created_at',
  'updated_at',
  'createdAt',
  'updatedAt',
]);

// ============================================================
// ROLE MAPPING
// ============================================================

/**
 * Maps our internal role values to ACGME role codes.
 * ACGME only accepts: SC, SJ, TA, FA
 */
const ROLE_MAP = Object.freeze({
  // Our values → ACGME codes
  'Primary Surgeon':      null,  // Needs PGY year context → SC or SJ
  'Primary':              null,  // Needs PGY year context → SC or SJ
  'Surgeon Chief':        'SC',
  'Surgeon Junior':       'SJ',
  'Chief':                'SC',
  'Junior':               'SJ',
  'SC':                   'SC',
  'SJ':                   'SJ',
  'Teaching Assistant':   'TA',
  'Teaching':             'TA',
  'TA':                   'TA',
  'First Assistant':      'FA',
  'Assistant':            'FA',
  'FA':                   'FA',
});

/**
 * Maps our role + PGY year to the correct ACGME role code.
 * "Primary Surgeon" becomes SC in chief year, SJ otherwise.
 * 
 * @param {string} ourRole - Role from our system
 * @param {number|null} pgyYear - Post-graduate year (1-5), null if unknown
 * @param {boolean} isChiefYear - Whether resident is in chief year
 * @returns {string} ACGME role code (SC, SJ, TA, FA)
 */
function mapRole(ourRole, pgyYear = null, isChiefYear = false) {
  if (!ourRole) return null;
  
  const normalized = ourRole.trim();
  const mapped = ROLE_MAP[normalized];
  
  if (mapped) return mapped;
  
  // Handle "Primary Surgeon" / "Primary" — needs chief year context
  if (normalized === 'Primary Surgeon' || normalized === 'Primary') {
    if (isChiefYear || pgyYear === 5) return 'SC';
    return 'SJ';
  }
  
  console.warn(`[ACGME Filter] Unknown role: "${ourRole}". Defaulting to SJ.`);
  return 'SJ';
}

// ============================================================
// FIELD MAPPING (Our DB → ACGME)
// ============================================================

/**
 * Maps a case from our internal format to ACGME-safe export format.
 * 
 * @param {Object} caseData - Raw case data from our database
 * @param {Object} options - { pgyYear, isChiefYear, defaultSite }
 * @returns {{ acgmeCase: Object, warnings: string[], blocked: string[] }}
 */
function mapToACGME(caseData, options = {}) {
  const { pgyYear = null, isChiefYear = false, defaultSite = null } = options;
  const warnings = [];
  const blocked = [];

  // 1. Map our fields to ACGME fields
  const acgmeCase = {
    dateOfProcedure: caseData.date || null,
    cptCode: caseData.cpt_code || caseData.cptCode || caseData.cpt || null,
    role: mapRole(
      caseData.role, 
      pgyYear, 
      isChiefYear
    ),
    attending: caseData.attending || null,
    site: caseData.site || caseData.institution || defaultSite || null,
    caseId: caseData.case_id || caseData.caseId || null,
    patientType: caseData.patient_type || caseData.patientType || null,
    equipment: caseData.equipment || null,
    rrcCodes: caseData.rrc_codes || caseData.rrcCodes || null,
  };

  // 2. Track which fields were blocked
  for (const field of BLOCKED_FIELDS) {
    if (caseData[field] !== undefined && caseData[field] !== null) {
      blocked.push(field);
    }
  }

  // 3. Validate required fields
  for (const [field, spec] of Object.entries(ACGME_REQUIRED_FIELDS)) {
    if (spec.required && !acgmeCase[field]) {
      warnings.push(`Missing required ACGME field: ${spec.acgmeName} (${field})`);
    }
  }

  // 4. Validate date format
  if (acgmeCase.dateOfProcedure) {
    const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateRegex.test(acgmeCase.dateOfProcedure)) {
      warnings.push(`Date format should be YYYY-MM-DD, got: ${acgmeCase.dateOfProcedure}`);
    }
  }

  // 5. Validate role
  if (acgmeCase.role && !['SC', 'SJ', 'TA', 'FA'].includes(acgmeCase.role)) {
    warnings.push(`Invalid ACGME role: ${acgmeCase.role}. Must be SC, SJ, TA, or FA.`);
  }

  // 6. Handle Critical Care special case (CPT 99292)
  if (acgmeCase.cptCode === '99292' && !acgmeCase.rrcCodes) {
    warnings.push('CPT 99292 (Critical Care) requires RRC code selection (8410-8470)');
  }

  return { acgmeCase, warnings, blocked };
}

// ============================================================
// BATCH EXPORT FILTER
// ============================================================

/**
 * Filters a batch of cases for ACGME-safe export.
 * Returns only valid cases with only ACGME fields.
 * 
 * @param {Object[]} cases - Array of raw case data
 * @param {Object} options - { pgyYear, isChiefYear, defaultSite, strict }
 * @returns {{ exported: Object[], skipped: Object[], report: Object }}
 */
function filterForACGMEExport(cases, options = {}) {
  const { strict = false } = options;
  const exported = [];
  const skipped = [];
  let totalBlocked = 0;
  let totalWarnings = 0;

  for (const caseData of cases) {
    const { acgmeCase, warnings, blocked } = mapToACGME(caseData, options);
    totalBlocked += blocked.length;
    totalWarnings += warnings.length;

    // In strict mode, skip cases with missing required fields
    if (strict && warnings.some(w => w.startsWith('Missing required'))) {
      skipped.push({
        originalCase: caseData,
        reason: warnings.filter(w => w.startsWith('Missing required')),
      });
      continue;
    }

    exported.push(acgmeCase);
  }

  const report = {
    totalCases: cases.length,
    exportedCount: exported.length,
    skippedCount: skipped.length,
    totalFieldsBlocked: totalBlocked,
    totalWarnings: totalWarnings,
    blockedFieldTypes: [...new Set(
      cases.flatMap(c => 
        BLOCKED_FIELDS.filter(f => c[f] !== undefined && c[f] !== null)
      )
    )],
  };

  return { exported, skipped, report };
}

// ============================================================
// VALIDATION HELPERS
// ============================================================

/**
 * Validates a single case for ACGME readiness.
 * Returns true if case has all required fields.
 */
function isACGMEReady(caseData) {
  const { warnings } = mapToACGME(caseData);
  return warnings.filter(w => w.startsWith('Missing required')).length === 0;
}

/**
 * Returns a list of missing required fields for a case.
 */
function getMissingACGMEFields(caseData) {
  const { warnings } = mapToACGME(caseData);
  return warnings
    .filter(w => w.startsWith('Missing required'))
    .map(w => w.replace('Missing required ACGME field: ', ''));
}

/**
 * Strips ALL non-ACGME fields from a case object.
 * This is the nuclear option — ensures nothing leaks.
 */
function stripNonACGMEFields(obj) {
  const allowedKeys = Object.keys(ACGME_REQUIRED_FIELDS);
  const clean = {};
  for (const key of allowedKeys) {
    if (obj[key] !== undefined) {
      clean[key] = obj[key];
    }
  }
  return clean;
}

// ============================================================
// VALID CPT CODES (General Surgery Subset)
// ============================================================

/**
 * Common CPT codes tracked by ACGME for General Surgery.
 * This is not exhaustive — ACGME accepts any valid CPT code.
 * These are the ones that map to defined categories.
 */
const ACGME_SURGERY_CPT_CATEGORIES = Object.freeze({
  criticalCare: ['99292'],
  nonOpTrauma: ['99199'],
  // Vascular E-codes
  vascularExposure: ['35201', '35206', '35216', '35221', '35226'],
  // Team leader resuscitation
  teamLeader: ['92920'],
});

// ============================================================
// RRC CODES (Critical Care)
// ============================================================

const RRC_CODES = Object.freeze({
  '8410': 'Ventilatory management (>24h on ventilator)',
  '8420': 'Bleeding (non-trauma patient >3 units)',
  '8430': 'Hemodynamic instability (req. inotropic/pressor support)',
  '8440': 'Organ dysfunction (renal, hepatic, cardiac failure)',
  '8450': 'Dysrhythmias (requiring drug management)',
  '8460': 'Invasive line management/monitoring (Swan-Ganz, arterial lines, etc.)',
  '8470': 'Parenteral/enteral nutrition',
});

// ============================================================
// EXPORTS
// ============================================================

// For Chrome Extension (content script / background)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    ACGME_REQUIRED_FIELDS,
    BLOCKED_FIELDS,
    ROLE_MAP,
    RRC_CODES,
    ACGME_SURGERY_CPT_CATEGORIES,
    mapRole,
    mapToACGME,
    filterForACGMEExport,
    isACGMEReady,
    getMissingACGMEFields,
    stripNonACGMEFields,
  };
}

// For browser / ES modules
if (typeof window !== 'undefined') {
  window.ACGMEFilter = {
    ACGME_REQUIRED_FIELDS,
    BLOCKED_FIELDS,
    ROLE_MAP,
    RRC_CODES,
    ACGME_SURGERY_CPT_CATEGORIES,
    mapRole,
    mapToACGME,
    filterForACGMEExport,
    isACGMEReady,
    getMissingACGMEFields,
    stripNonACGMEFields,
  };
}
