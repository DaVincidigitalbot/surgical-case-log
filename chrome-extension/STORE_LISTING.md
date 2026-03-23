# Chrome Web Store Listing

## Name
Clinical Case Log → ACGME Export

## Short Description (132 chars max)
Export surgical cases from Clinical Case Log Pro to the ACGME Case Log System. ACGME-filtered. Built by a practicing surgeon.

## Detailed Description

**Stop double-entering your surgical cases.**

Clinical Case Log → ACGME Export connects your Clinical Case Log Pro account directly to the ACGME Case Log System (ADS). Select cases, click export, and auto-fill the ACGME entry form — in seconds, not minutes.

**How it works:**

1. Connect your Clinical Case Log Pro account (clinicalcaselog.com)
2. Select cases you want to report to ACGME
3. Click "Export to ACGME" — the extension opens ADS and shows a helper panel
4. Click "Fill Next Case" to auto-populate the ACGME form fields
5. Review and submit. Done.

**ACGME-compliant field filtering:**

This extension exports ONLY the fields accepted by the ACGME Case Log System:
• Date of Procedure
• CPT Code
• Role (SC, SJ, TA, FA)
• Attending Surgeon
• Site/Institution
• Case ID
• Patient Type

Non-ACGME fields (patient age, sex, diagnosis, ICD-10 codes, EBL, OR time, complications, notes) are automatically stripped to prevent data corruption in ADS.

**Features:**
✓ One-click export from Clinical Case Log to ACGME
✓ Auto-fill ACGME case entry forms
✓ ACGME field filtering — only valid fields are exported
✓ Role mapping (Primary Surgeon → SC/SJ, First Assist → FA)
✓ Tracks exported cases to prevent duplicates
✓ Works with the ACGME ADS Case Log System
✓ Supports General Surgery, Trauma, Critical Care, and all surgical subspecialties

**Built for surgical residents, by a practicing surgeon.**

Clinical Case Log Pro is the only case logging platform built by a surgeon who understands the pain of ACGME reporting. Log cases in 30 seconds from your phone, then export to ACGME with this extension.

Learn more at clinicalcaselog.com

**Privacy:**
• No patient data is collected or transmitted
• All data stays between your Clinical Case Log account and ACGME
• We do not track browsing activity
• Extension only activates on clinicalcaselog.com and apps.acgme.org

## Category
Productivity

## Language
English

## Website
https://clinicalcaselog.com

## Privacy Policy URL
https://clinicalcaselog.com/legal

## Single Purpose Description (for Chrome review)
This extension exports surgical case data from the Clinical Case Log Pro web application (clinicalcaselog.com) to the ACGME Case Log System (apps.acgme.org) by auto-filling case entry forms with ACGME-compliant filtered data.

## Justification for Permissions

### activeTab
Required to interact with the ACGME Case Log System page when the user initiates an export. The extension auto-fills form fields on the active tab.

### storage
Required to store the user's API token for connecting to their Clinical Case Log account, their default site/institution preference, and pending case export data between the popup and content script.

### Host permissions: clinicalcaselog.com
Required to fetch the user's case data from their Clinical Case Log Pro account via API.

### Host permissions: apps.acgme.org
Required to inject the helper panel and auto-fill case entry forms on the ACGME ADS Case Log System.

---

## Screenshots Needed (provide 1280x800 or 640x400)

1. **Popup — Connected State**: Show popup with cases listed, ready to export
2. **Popup — Export Selected**: Show cases checked with "Export 5 Cases to ACGME" button
3. **ACGME Helper Panel**: Show the floating panel on the ACGME ADS page with case details
4. **Settings Tab**: Show the settings page with API token and site fields
5. **ACGME Button in App**: Show the teal 🎯 ACGME button in the Clinical Case Log toolbar
