/**
 * Tests for ACGME Field Filtering System
 * Run: node acgme-filter.test.js
 */

const {
  mapRole,
  mapToACGME,
  filterForACGMEExport,
  isACGMEReady,
  getMissingACGMEFields,
  stripNonACGMEFields,
  BLOCKED_FIELDS,
} = require('./acgme-filter');

let passed = 0;
let failed = 0;

function assert(condition, name) {
  if (condition) {
    passed++;
    console.log(`  ✅ ${name}`);
  } else {
    failed++;
    console.log(`  ❌ ${name}`);
  }
}

// ============================================================
console.log('\n🔬 Role Mapping Tests');
// ============================================================

assert(mapRole('SC') === 'SC', 'SC stays SC');
assert(mapRole('SJ') === 'SJ', 'SJ stays SJ');
assert(mapRole('TA') === 'TA', 'TA stays TA');
assert(mapRole('FA') === 'FA', 'FA stays FA');
assert(mapRole('Teaching Assistant') === 'TA', 'Teaching Assistant → TA');
assert(mapRole('First Assistant') === 'FA', 'First Assistant → FA');
assert(mapRole('Primary Surgeon', 5, true) === 'SC', 'Primary Surgeon in chief year → SC');
assert(mapRole('Primary Surgeon', 3, false) === 'SJ', 'Primary Surgeon in junior year → SJ');
assert(mapRole('Primary', null, true) === 'SC', 'Primary in chief year → SC');
assert(mapRole('Primary', 2) === 'SJ', 'Primary in PGY2 → SJ');

// ============================================================
console.log('\n🔬 Field Mapping Tests');
// ============================================================

const fullCase = {
  id: 42,
  user_id: 1,
  date: '2026-03-15',
  age: 65,
  sex: 'M',
  rotation: 'Trauma',
  procedure_name: 'Laparoscopic Cholecystectomy',
  cpt_code: '47562',
  role: 'Primary Surgeon',
  approach: 'Laparoscopic',
  attending: 'Dr. Smith',
  complications: 'None',
  ebl: 50,
  or_time: 45,
  notes: 'Routine case',
  diagnosis: 'Acute cholecystitis',
  case_id: 'CCL-2026-0042',
  site: 'CaroMont Regional Medical Center',
  created_at: '2026-03-15T10:00:00Z',
};

const result = mapToACGME(fullCase, { pgyYear: 3, isChiefYear: false });

assert(result.acgmeCase.dateOfProcedure === '2026-03-15', 'Date mapped correctly');
assert(result.acgmeCase.cptCode === '47562', 'CPT code mapped correctly');
assert(result.acgmeCase.role === 'SJ', 'Role mapped to SJ for junior year');
assert(result.acgmeCase.attending === 'Dr. Smith', 'Attending mapped correctly');
assert(result.acgmeCase.site === 'CaroMont Regional Medical Center', 'Site mapped correctly');
assert(result.acgmeCase.caseId === 'CCL-2026-0042', 'Case ID mapped correctly');

// Verify blocked fields are NOT in output
assert(result.acgmeCase.age === undefined, 'Age blocked from export');
assert(result.acgmeCase.sex === undefined, 'Sex blocked from export');
assert(result.acgmeCase.rotation === undefined, 'Rotation blocked from export');
assert(result.acgmeCase.procedure_name === undefined, 'Procedure name blocked');
assert(result.acgmeCase.diagnosis === undefined, 'Diagnosis blocked');
assert(result.acgmeCase.ebl === undefined, 'EBL blocked');
assert(result.acgmeCase.or_time === undefined, 'OR time blocked');
assert(result.acgmeCase.complications === undefined, 'Complications blocked');
assert(result.acgmeCase.notes === undefined, 'Notes blocked');

// Verify blocked fields are reported
assert(result.blocked.includes('age'), 'Age reported as blocked');
assert(result.blocked.includes('sex'), 'Sex reported as blocked');
assert(result.blocked.includes('ebl'), 'EBL reported as blocked');
assert(result.blocked.length > 0, 'Blocked fields list is populated');
assert(result.warnings.length === 0, 'No warnings for complete case');

// ============================================================
console.log('\n🔬 Missing Field Validation');
// ============================================================

const incompleteCase = {
  date: '2026-03-15',
  cpt_code: '47562',
  // Missing: role, attending, site
};

const incomplete = mapToACGME(incompleteCase);
assert(incomplete.warnings.length > 0, 'Warns about missing fields');
assert(!isACGMEReady(incompleteCase), 'Incomplete case is not ACGME-ready');

const missing = getMissingACGMEFields(incompleteCase);
assert(missing.some(m => m.includes('Role')), 'Reports missing Role');
assert(missing.some(m => m.includes('Attending')), 'Reports missing Attending');
assert(missing.some(m => m.includes('Site')), 'Reports missing Site');

// ============================================================
console.log('\n🔬 Critical Care (99292) Validation');
// ============================================================

const critCareNoRRC = {
  date: '2026-03-15',
  cpt_code: '99292',
  role: 'SC',
  attending: 'Dr. Jones',
  site: 'CaroMont',
};

const ccResult = mapToACGME(critCareNoRRC);
assert(
  ccResult.warnings.some(w => w.includes('RRC code')),
  'Warns when 99292 missing RRC codes'
);

// ============================================================
console.log('\n🔬 Batch Export Filter');
// ============================================================

const cases = [
  fullCase,
  incompleteCase,
  { ...fullCase, date: '2026-03-16', case_id: 'CCL-2026-0043' },
];

const batch = filterForACGMEExport(cases, { 
  pgyYear: 3, 
  defaultSite: 'CaroMont',
  strict: true 
});

assert(batch.exported.length === 2, 'Strict mode: 2 valid cases exported');
assert(batch.skipped.length === 1, 'Strict mode: 1 incomplete case skipped');
assert(batch.report.totalFieldsBlocked > 0, 'Reports blocked fields count');

const batchLenient = filterForACGMEExport(cases, { pgyYear: 3, defaultSite: 'CaroMont' });
assert(batchLenient.exported.length === 3, 'Lenient mode: all 3 cases exported');

// ============================================================
console.log('\n🔬 Strip Non-ACGME Fields');
// ============================================================

const dirty = {
  dateOfProcedure: '2026-03-15',
  cptCode: '47562',
  role: 'SJ',
  attending: 'Dr. Smith',
  site: 'CaroMont',
  age: 65,           // should be stripped
  ebl: 50,           // should be stripped
  rotation: 'Trauma' // should be stripped
};

const clean = stripNonACGMEFields(dirty);
assert(clean.dateOfProcedure === '2026-03-15', 'Keeps dateOfProcedure');
assert(clean.cptCode === '47562', 'Keeps cptCode');
assert(clean.age === undefined, 'Strips age');
assert(clean.ebl === undefined, 'Strips ebl');
assert(clean.rotation === undefined, 'Strips rotation');

// ============================================================
console.log('\n📊 Results');
console.log(`   ${passed} passed, ${failed} failed\n`);
// ============================================================

process.exit(failed > 0 ? 1 : 0);
