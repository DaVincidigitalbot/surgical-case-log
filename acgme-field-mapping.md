# ACGME Case Log Field Mapping — General Surgery

## Source Documentation
- ACGME Case Log Coding Guidelines (280_case_log_coding_guidelines.pdf, 03/2021)
- ACGME Defined Category Minimum Numbers for General Surgery (05/2024)
- ACGME-I General Surgery Resident Guide (08/2018)
- UCSF General Surgery Operative Log Guidelines
- Stanford Operative Logging Guidelines
- Johns Hopkins EHR-ACGME Integration Study (PMC9380618)

---

## ACGME Case Log System — Required Fields (Starred * in ADS)

The ACGME Case Log System within ADS requires these fields for a valid case entry.
Fields marked with * are **required** (starred) — the case cannot be saved without them.

| # | ACGME Field Name       | Required? | Description |
|---|------------------------|-----------|-------------|
| 1 | **Date of Procedure*** | ✅ YES    | Date the procedure was performed |
| 2 | **CPT Code***          | ✅ YES    | Current Procedural Terminology code(s) |
| 3 | **Role***              | ✅ YES    | SC (Surgeon Chief), SJ (Surgeon Junior), TA (Teaching Asst), FA (First Asst) |
| 4 | **Attending***         | ✅ YES    | Attending surgeon supervising the case |
| 5 | **Site/Institution***  | ✅ YES    | Hospital/facility where procedure occurred |
| 6 | **Case ID**            | ⚠️ Recommended | Unique identifier for the case (required for E-codes, strongly recommended) |
| 7 | **Patient Type**       | Optional  | Inpatient/Outpatient |
| 8 | **Equipment**          | Optional  | Special equipment used (lasers, etc.) — recently added |
| 9 | **RRC Code**           | Conditional | Required only for CPT 99292 (Critical Care) — maps to 7 categories |

### Critical Care (CPT 99292) Additional Required Fields:
- RRC Code selection (8410-8470) mapping to the 7 critical care categories

---

## What ACGME Does NOT Require

These fields are **NOT part of the ACGME Case Log System**:

| Field | ACGME Status | Notes |
|-------|-------------|-------|
| Patient Age | ❌ NOT required | Not an ACGME field — useful for internal tracking only |
| Patient Sex | ❌ NOT required | Not an ACGME field — useful for internal tracking only |
| Rotation | ❌ NOT required | Program-internal tracking, not submitted to ACGME |
| Diagnosis/ICD Codes | ❌ NOT required | ACGME uses CPT codes, not ICD diagnosis codes for surgery |
| EBL (Est. Blood Loss) | ❌ NOT required | Clinical detail, not part of case log |
| OR Time | ❌ NOT required | Clinical detail, not part of case log |
| Complications | ❌ NOT required | Not part of ACGME case log entry |
| Approach | ❌ NOT required | Captured via CPT code selection (lap vs open) |
| Notes | ❌ NOT required | Free text, not submitted to ACGME |

---

## Field Mapping: Our System → ACGME

| Our Field (`cases` table) | ACGME Field | Sync to ACGME? | Notes |
|---------------------------|-------------|----------------|-------|
| `date` | Date of Procedure | ✅ YES | Direct map, format: YYYY-MM-DD |
| `cpt_code` | CPT Code | ✅ YES | Must be valid ACGME-recognized CPT |
| `role` | Role | ✅ YES | Map: "Primary Surgeon" → SC/SJ, "First Assistant" → FA, "Teaching" → TA |
| `attending` | Attending | ✅ YES | Must match ACGME attending list |
| `case_id` | Case ID | ✅ YES | Format: CCL-YYYY-NNNN, supports E-codes |
| *(missing)* | Site/Institution | ⚠️ NEEDS ADDING | Required by ACGME, not in our schema |
| `age` | — | ❌ BLOCK | Not an ACGME field |
| `sex` | — | ❌ BLOCK | Not an ACGME field |
| `rotation` | — | ❌ BLOCK | Not an ACGME field |
| `procedure_name` | — | ❌ BLOCK | ACGME uses CPT codes, not procedure names |
| `diagnosis` | — | ❌ BLOCK | Not an ACGME field |
| `ebl` | — | ❌ BLOCK | Not an ACGME field |
| `or_time` | — | ❌ BLOCK | Not an ACGME field |
| `approach` | — | ❌ BLOCK | Implicit in CPT code |
| `complications` | — | ❌ BLOCK | Not an ACGME field |
| `notes` | — | ❌ BLOCK | Not an ACGME field |

---

## Role Mapping Table

| Our Value | ACGME Code | ACGME Name | Counts Toward |
|-----------|-----------|------------|---------------|
| Primary Surgeon (Chief Year) | SC | Surgeon Chief | 200 chief min, 850 total |
| Primary Surgeon (Junior Year) | SJ | Surgeon Junior | 850 total |
| Teaching Assistant | TA | Teaching Assistant | First 50 count toward total |
| First Assistant | FA | First Assistant | 250 PGY2 cases |

---

## Missing Field: Site/Institution

**Action Required:** Add `site` or `institution` column to the `cases` table.

```sql
ALTER TABLE cases ADD COLUMN site TEXT;
```

This is required by ACGME and currently missing from our schema. Each program has registered sites in ADS, and the case must specify where it was performed.

---

## ACGME-Safe Export Format

When syncing to ACGME (or exporting for ACGME submission), the payload should contain ONLY:

```json
{
  "dateOfProcedure": "2026-03-15",
  "cptCode": "47562",
  "role": "SC",
  "attending": "Dr. Smith",
  "site": "CaroMont Regional Medical Center",
  "caseId": "CCL-2026-0042",
  "patientType": "inpatient",
  "equipment": null,
  "rrcCodes": null
}
```

**Any field not in this list MUST be stripped before export.**
