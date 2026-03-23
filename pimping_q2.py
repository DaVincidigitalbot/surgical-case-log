#!/usr/bin/env python3
"""Continuation of pimping questions - Part 2"""

QUESTIONS2 = {}

QUESTIONS2["Parathyroidectomy"] = [
    {"question": "The superior and inferior parathyroid glands derive from which pharyngeal pouches, and which has more variable position?",
     "answer": "Superior: 4th pharyngeal pouch (dorsal wing, consistent position behind upper thyroid). Inferior: 3rd pharyngeal pouch (descend with thymus, longer migration = more variable position — from angle of mandible to anterior mediastinum)."},
    {"question": "What percentage of patients have ectopic parathyroid glands, and what are the common locations?",
     "answer": "15-20% have ectopic glands. Common locations: intrathyroidal (3-5%), carotid sheath, tracheoesophageal groove, thymus (most common ectopic site for inferior glands), mediastinum (may require sternotomy or VATS), and retroesophageal. Preoperative sestamibi scan and 4D-CT help localize."},
    {"question": "What is the blood supply to the parathyroid glands, and what is the consequence of devascularization?",
     "answer": "Primarily the inferior thyroid artery (supplies both superior and inferior glands in 80%). The superior thyroid artery contributes to the superior glands. Each gland has a single end-artery — devascularization causes infarction and hypoparathyroidism. If devascularized, mince the gland into 1mm pieces and autotransplant into the sternocleidomastoid or forearm muscle."},
    {"question": "What is the intraoperative PTH protocol (Miami criteria), and when do you consider the operation successful?",
     "answer": "Baseline PTH drawn before incision. After adenoma excision, PTH levels at 5 and 10 minutes. Success: PTH drops >50% from the highest pre-excision value AND falls into the normal range. If PTH doesn't drop adequately, search for multigland disease, ectopic gland, or supernumerary (5th) gland."},
    {"question": "What is the difference between primary, secondary, and tertiary hyperparathyroidism surgically?",
     "answer": "Primary: single adenoma (85%) — focused parathyroidectomy. Secondary: all four glands hyperplastic from chronic kidney disease — subtotal (3.5-gland) parathyroidectomy or total with autotransplant. Tertiary: autonomous PTH secretion after renal transplant (previously secondary) — subtotal parathyroidectomy if hypercalcemia persists >1 year post-transplant."}
]

QUESTIONS2["Laparoscopic Adrenalectomy"] = [
    {"question": "The adrenal cortex and medulla have different embryologic origins. What are they?",
     "answer": "Cortex: mesoderm (intermediate mesoderm/urogenital ridge). Medulla: neural crest cells (ectoderm) that migrate into the developing cortex during weeks 7-8. This dual origin explains why cortical and medullary tumors have completely different biology (cortisol/aldosterone vs catecholamines)."},
    {"question": "What is the key anatomic difference between right and left adrenalectomy regarding venous drainage?",
     "answer": "Right adrenal vein: short (5mm), drains directly into the IVC posterolaterally — extremely dangerous to avulse, causing IVC hemorrhage. Left adrenal vein: longer (2-3cm), drains into the left renal vein with the left inferior phrenic vein. Right adrenalectomy is more technically demanding because of this short right adrenal vein."},
    {"question": "What is the arterial supply to the adrenal glands?",
     "answer": "Three sources: 1) Superior adrenal arteries (from inferior phrenic artery — multiple small branches), 2) Middle adrenal artery (from aorta — single vessel), 3) Inferior adrenal artery (from renal artery). Despite this rich arterial supply, there is typically only ONE adrenal vein per side — the vein is the key structure to control."},
    {"question": "What must be done preoperatively for a suspected pheochromocytoma before ANY surgical manipulation?",
     "answer": "Alpha-blockade for 10-14 days (phenoxybenzamine or doxazosin) BEFORE beta-blockade (added only after alpha-block is established, otherwise unopposed alpha stimulation causes hypertensive crisis). Adequate volume expansion (liberal salt/fluid intake). Failure to block causes intraoperative hypertensive crisis, arrhythmias, and potentially death during tumor manipulation."},
    {"question": "What is the size cutoff for laparoscopic versus open adrenalectomy, and when is open mandatory?",
     "answer": "Laparoscopic: generally <6cm (some extend to 8-10cm for benign tumors). Open: tumors >6cm with radiographic features of malignancy, suspected adrenocortical carcinoma (ACC), or local invasion. ACC has a 40% recurrence rate even after R0 resection — capsular violation during laparoscopic removal worsens outcomes. Size >4cm with imaging features of malignancy warrants open approach."}
]

QUESTIONS2["Open Adrenalectomy"] = [
    {"question": "The fetal adrenal cortex has a large 'fetal zone' that involutes after birth. What does it produce?",
     "answer": "DHEA and DHEA-S (dehydroepiandrosterone sulfate) — the fetal zone comprises 80% of the fetal adrenal mass and produces androgen precursors essential for placental estrogen synthesis. It involutes within the first year of life, replaced by the adult zona glomerulosa, fasciculata, and reticularis."},
    {"question": "For open right adrenalectomy, what surgical approach provides the best exposure to the IVC and short right adrenal vein?",
     "answer": "A right subcostal (Kocher) incision with medial visceral rotation (Cattell-Braasch maneuver — mobilizing the right colon, duodenum, and pancreatic head medially). This exposes the IVC, right renal vein, and the short right adrenal vein at its IVC junction for safe ligation before tumor manipulation."},
    {"question": "What are the three layers of the adrenal cortex (from outside in) and their hormonal products?",
     "answer": "GFR mnemonic: Glomerulosa (mineralocorticoids — aldosterone), Fasciculata (glucocorticoids — cortisol), Reticularis (androgens — DHEA/androstenedione). 'Salt, Sugar, Sex' — the deeper you go, the sweeter it gets. Cortical tumors are classified by which zone they arise from and what they secrete."},
    {"question": "What is the most feared complication of open adrenalectomy for adrenocortical carcinoma?",
     "answer": "Tumor rupture/capsular violation causing peritoneal carcinomatosis. ACC is an aggressive cancer (5-year survival 20-35% overall) and capsule violation upstages disease and dramatically worsens prognosis. En bloc resection with negative margins, potentially including kidney, spleen, or diaphragm, is the standard for ACC."},
    {"question": "After bilateral adrenalectomy, what lifelong medication is required, and what is the acute risk?",
     "answer": "Lifelong glucocorticoid (hydrocortisone) AND mineralocorticoid (fludrocortisone) replacement — the patient has Addisonian crisis risk. Acute adrenal crisis presents with hypotension, hyponatremia, hyperkalemia, and cardiovascular collapse during physiologic stress. Patients must carry emergency injectable hydrocortisone and wear medical alert identification."}
]

# ============================================================
# HERNIA (covers ventral, inguinal, etc.)
# ============================================================

QUESTIONS2["Laparoscopic Paraesophageal Hernia Repair"] = [
    {"question": "What embryologic defect creates the esophageal hiatus?",
     "answer": "The hiatus forms from the right crus of the diaphragm (from pleuroperitoneal membrane/septum transversum) failing to completely close around the esophagus. Type I: sliding (GEJ migrates up). Type II: true paraesophageal (fundus beside fixed GEJ). Type III: combined. Type IV: other organs herniate too."},
    {"question": "What is the key step beyond fundoplication that differentiates paraesophageal repair?",
     "answer": "Complete hernia sac reduction and excision from the mediastinum. The sac must be dissected off pleura, pericardium, and aorta. Leaving the sac increases recurrence. The esophagus must be mobilized for ≥3cm of tension-free intra-abdominal length."},
    {"question": "What blood supply concern exists when the stomach undergoes organoaxial volvulus in a paraesophageal hernia?",
     "answer": "Gastric volvulus compresses the left gastric artery and short gastric vessels, causing ischemia and necrosis. The right gastroepiploic may kink. Acute volvulus with ischemia is a surgical emergency with 30-50% mortality if not treated promptly."},
    {"question": "Does mesh reinforcement reduce hernia recurrence after paraesophageal repair?",
     "answer": "Recurrence: 15-25% radiographic at 5 years (5-10% symptomatic). Biologic mesh reinforcement of the crural closure may help; synthetic mesh is controversial due to esophageal erosion risk. Evidence is mixed — the FLAIR trial is investigating this question."},
    {"question": "What is Borchardt's triad for acute gastric volvulus?",
     "answer": "1) Severe epigastric pain, 2) Retching without vomiting (non-productive), 3) Inability to pass an NG tube. This is a surgical emergency ('acute upside-down stomach') requiring immediate operative decompression and repair."}
]

# ============================================================
# TRAUMA
# ============================================================

QUESTIONS2["Damage Control Laparotomy"] = [
    {"question": "What is the 'lethal triad' of trauma, and what embryologic/physiologic basis drives damage control?",
     "answer": "Hypothermia, acidosis, and coagulopathy — a self-perpetuating cycle. Hypothermia impairs coagulation enzymes (derived from hepatic endoderm). Acidosis (from anaerobic metabolism in hypoperfused mesoderm-derived tissues) worsens coagulopathy. Damage control interrupts this cycle by abbreviating surgery and prioritizing resuscitation."},
    {"question": "What are the three phases of damage control surgery?",
     "answer": "Phase 1: Abbreviated laparotomy (hemorrhage control, contamination control, temporary abdominal closure — 30-60 minutes). Phase 2: ICU resuscitation (rewarm, correct coagulopathy, optimize hemodynamics — 24-72 hours). Phase 3: Definitive repair (return to OR for definitive reconstruction when physiology normalizes). The decision to go damage control is made BEFORE or early in the operation."},
    {"question": "What is the blood supply concern when performing temporary abdominal closure with negative pressure?",
     "answer": "Abdominal packing can compress the IVC and mesenteric vessels, reducing venous return and causing visceral ischemia. The sponge-based VAC system must distribute pressure evenly. Abdominal compartment syndrome (ACS) can develop if closure is too tight — bladder pressure >20 mmHg with organ dysfunction defines ACS."},
    {"question": "What is abdominal compartment syndrome, and what are the thresholds for decompressive laparotomy?",
     "answer": "Sustained intra-abdominal pressure >20 mmHg with new organ dysfunction (renal failure, respiratory failure, cardiac output depression). Measured by intravesical (bladder) pressure. Grade III (>25 mmHg) with organ failure mandates decompressive laparotomy. Risk factors: massive resuscitation (>10L crystalloid), abdominal packing, bowel edema."},
    {"question": "What is the open abdomen management strategy, and when is fascial closure expected?",
     "answer": "Negative pressure wound therapy (ABThera or Barker VAC) with sequential tightening. Fascial closure should be achieved within 5-7 days — after this, visceral adhesion to the abdominal wall makes closure extremely difficult. If primary closure is impossible, absorbable mesh bridge (Vicryl) or component separation can be performed. Planned ventral hernia is acceptable as a salvage strategy."}
]

QUESTIONS2["Diaphragmatic Repair (Trauma)"] = [
    {"question": "The diaphragm develops from four embryologic components. What are they?",
     "answer": "1) Septum transversum (central tendon — most of the diaphragm), 2) Pleuroperitoneal membranes (posterolateral — the site of Bochdalek hernias), 3) Esophageal mesentery (crura), 4) Body wall musculature (peripheral muscular rim). Failure of the pleuroperitoneal membrane closure causes congenital diaphragmatic hernia (left >> right)."},
    {"question": "Why are left-sided diaphragmatic injuries more common in blunt trauma, and why are right-sided injuries often missed?",
     "answer": "Left-sided: 3x more common because the liver 'protects' the right hemidiaphragm. Left-sided injuries allow stomach, spleen, and colon to herniate into the chest. Right-sided injuries are masked by the liver plugging the defect — they present late with hepatic herniation and are often diagnosed on delayed CT or at thoracotomy."},
    {"question": "What is the blood supply to the diaphragm?",
     "answer": "Musculophrenic arteries (from internal mammary), inferior phrenic arteries (from aorta — dominant supply), pericardiophrenic arteries (from internal mammary), and intercostal arteries. The phrenic nerve (C3-C5) provides motor innervation. Injury to the phrenic nerve during repair causes ipsilateral hemidiaphragm paralysis."},
    {"question": "What is the most common delayed complication of a missed diaphragmatic injury?",
     "answer": "Diaphragmatic hernia with visceral strangulation — stomach, colon, or omentum herniates through the defect months to years later. Presents as respiratory distress, bowel obstruction, or strangulation. The defect enlarges over time from the pressure differential between the peritoneal and pleural cavities."},
    {"question": "What suture technique is used for diaphragmatic repair, and can you use mesh?",
     "answer": "Horizontal mattress sutures with #1 non-absorbable (polypropylene or nylon), placed 1cm from the edge and 1cm apart. Primary repair is preferred for acute injuries. Mesh (biologic or synthetic) is used only for chronic injuries with tissue loss where primary repair creates excessive tension. In contaminated fields (bowel injury), use biologic mesh or primary repair only."}
]

QUESTIONS2["Splenic Injury Management"] = [
    {"question": "The spleen develops from mesenchymal condensation in which embryologic mesentery?",
     "answer": "The dorsal mesogastrium (same as the greater omentum). As the stomach rotates, the dorsal mesogastrium extends leftward, and splenic mesenchyme condenses within it. This is why the spleen is connected to the stomach by the gastrosplenic ligament and to the kidney by the splenorenal ligament — both are remnants of the dorsal mesogastrium."},
    {"question": "What are the peritoneal attachments of the spleen that must be divided for mobilization?",
     "answer": "1) Gastrosplenic ligament (contains short gastric arteries), 2) Splenorenal ligament (contains splenic vessels and tail of pancreas), 3) Splenocolic ligament (to splenic flexure), 4) Splenophrenic ligament (to diaphragm). The splenorenal ligament injury can damage the pancreatic tail causing fistula."},
    {"question": "What is the splenic artery's course, and why does it make partial splenectomy possible?",
     "answer": "The splenic artery (from celiac trunk) is the most tortuous artery in the body, running along the superior border of the pancreas. At the hilum, it divides into superior and inferior polar arteries. These segmental branches allow partial splenectomy — individual polar vessels can be ligated preserving the remaining splenic parenchyma."},
    {"question": "What AAST grade of splenic injury can be managed nonoperatively, and what are the criteria for NOM?",
     "answer": "Grades I-III (and selected IV) can be managed nonoperatively if: hemodynamically stable/responding to resuscitation, no peritonitis, no other indications for laparotomy, and available monitoring (ICU). NOM success rate: 90% overall. Angioembolization is used for active extravasation or pseudoaneurysm on CT (Grade IV-V with blush). NOM failure: ~5-10% require delayed operation."},
    {"question": "What is overwhelming post-splenectomy infection (OPSI), and how do you prevent it?",
     "answer": "Fulminant sepsis from encapsulated organisms (Streptococcus pneumoniae #1, Haemophilus influenzae, Neisseria meningitidis) due to loss of splenic macrophage filtration and opsonin production. Mortality: 50-70% once established. Prevention: vaccination (pneumococcal, meningococcal, H. influenzae type b) ideally 14 days post-splenectomy, daily penicillin prophylaxis in children, and patient education about fever urgency."}
]

QUESTIONS2["Liver Laceration Repair"] = [
    {"question": "The liver is the largest solid organ derived from foregut endoderm. What makes it particularly prone to injury in blunt trauma?",
     "answer": "Its large size (occupying the entire right upper quadrant), fixed position (attached by coronary/triangular ligaments and IVC), solid parenchyma with minimal elasticity, and dual blood supply (making it highly vascular — receives 25% of cardiac output). Deceleration injuries cause tearing at the ligamentous attachments, especially at the bare area and hepatic vein insertions."},
    {"question": "What is the bare area of the liver, and what structure lies directly behind it?",
     "answer": "The posterior superior surface of the right lobe between the coronary ligaments — the only portion of the liver not covered by peritoneum. The IVC lies directly posterior in the hepatic fossa. Injuries to the bare area can involve the retrohepatic IVC, which carries 50-80% mortality."},
    {"question": "What is the blood supply to the liver that must be considered in laceration repair?",
     "answer": "Dual supply: hepatic artery (25-30% of blood flow, 50% of oxygen) and portal vein (70-75% of blood flow, 50% of oxygen). The hepatic veins (right, middle, left) drain into the IVC. Massive hepatic hemorrhage comes from the hepatic veins and IVC — the Pringle maneuver (clamping portal triad) controls arterial/portal bleeding but NOT hepatic venous hemorrhage."},
    {"question": "What is hepatic packing, and when is it used versus definitive repair?",
     "answer": "Perihepatic packing with laparotomy pads to tamponade hemorrhage — the cornerstone of damage control for liver injuries. Used when: grade IV-V injuries, coagulopathy (lethal triad), inability to identify bleeding source, and bilobar injuries. Packs are removed at planned re-exploration (24-72 hours). Definitive repair (hepatotomy with selective ligation, hepatic resection) is performed only in stable patients."},
    {"question": "What is the role of angioembolization in hepatic trauma?",
     "answer": "Used for: active arterial extravasation (blush on CT), hepatic artery pseudoaneurysm, or persistent bleeding after packing. Performed by interventional radiology — selective embolization of the offending arterial branch. Success rate: 80-90%. The liver tolerates hepatic artery embolization because the portal vein provides sufficient perfusion. Used as adjunct to NOM or after packing."}
]

QUESTIONS2["Resuscitative Thoracotomy"] = [
    {"question": "The heart develops from splanchnic mesoderm forming the cardiogenic area. At what gestational time does the heart begin beating?",
     "answer": "Day 22-23 of development — the heart tube begins rhythmic contractions before it has completed looping and septation. This is the earliest functioning organ in embryologic development. The primitive heart tube folds rightward (dextral looping) to establish normal cardiac orientation."},
    {"question": "What is the anatomic landmark for the anterolateral thoracotomy incision in resuscitative thoracotomy?",
     "answer": "Left 5th intercostal space — from the sternum to the posterior axillary line. The incision goes through skin, subcutaneous tissue, pectoralis major, serratus anterior, and the intercostal muscles (external, internal, innermost). The internal mammary artery runs 1-2cm lateral to the sternum and must be controlled if transected."},
    {"question": "What are the five immediate maneuvers performed during resuscitative thoracotomy?",
     "answer": "1) Pericardiotomy (relieve tamponade — incise anterior to phrenic nerve), 2) Cross-clamp the descending aorta (augment coronary/cerebral perfusion), 3) Open cardiac massage, 4) Control hemorrhage (cardiac stapling, Foley catheter tamponade, pulmonary hilar twist), 5) Internal defibrillation (30J directly on myocardium). Aortic cross-clamping redistributes the remaining blood volume to the heart and brain."},
    {"question": "What is the survival rate for resuscitative thoracotomy by mechanism?",
     "answer": "Penetrating cardiac injury with signs of life: 10-35% (best outcomes). Penetrating thoracic (non-cardiac): 10-15%. Penetrating abdominal: 5%. Blunt trauma with signs of life: <2%. Blunt trauma without signs of life: essentially 0%. These numbers define the indications — it should NOT be performed for blunt arrest without signs of life."},
    {"question": "What defines 'signs of life' that justify resuscitative thoracotomy?",
     "answer": "Pupillary response, spontaneous breathing/gasping, palpable pulse, measurable blood pressure, extremity movement, or cardiac electrical activity (narrow-complex). Loss of signs of life: penetrating — within 15 minutes of arrest (proceed). Blunt — within 10 minutes (proceed only if witnessed arrest). Beyond these windows, survival is futile and the procedure should not be performed."}
]

# ============================================================
# VASCULAR
# ============================================================

QUESTIONS2["Arteriovenous Fistula Creation"] = [
    {"question": "The radial and ulnar arteries develop from the axis artery of the upper limb. What embryologic vessel is this?",
     "answer": "The axial artery is the 7th cervical intersegmental artery, which gives rise to the subclavian, axillary, brachial, and then divides into the radial and ulnar arteries (interosseous artery is the primitive axial artery continuation). The palmar arches (superficial from ulnar, deep from radial) provide collateral flow that is tested by the Allen test."},
    {"question": "What is the order of preference for AVF creation sites, and why?",
     "answer": "'Fistula First' principle — distal to proximal: 1) Radiocephalic (Brescia-Cimino, at wrist — best patency, lowest steal), 2) Brachiocephalic (at antecubital fossa), 3) Brachiobasilic (with transposition — basilic vein is deep and must be superficialized). Distal sites preserve proximal options if failure occurs. Grafts (PTFE) are second-line. Catheters are last resort."},
    {"question": "What is the blood supply to the hand that must be confirmed before radiocephalic AVF creation?",
     "answer": "Confirmed by a modified Allen test: compress both radial and ulnar arteries, have patient clench fist, release ulnar artery only — palm should reperfuse within 5-6 seconds. This confirms adequate ulnar collateral flow through the palmar arches. If the Allen test is abnormal, do NOT create a radiocephalic fistula (risk of hand ischemia/steal syndrome)."},
    {"question": "What is steal syndrome after AVF creation, and how do you manage it?",
     "answer": "Arterial blood is 'stolen' from the hand into the low-resistance AVF circuit, causing hand ischemia (pain, pallor, coolness, ulceration). More common with proximal fistulas (brachial artery-based). Management: DRIL procedure (Distal Revascularization-Interval Ligation) — ligate the artery just distal to the AVF and bypass to the forearm, restoring hand perfusion while maintaining fistula flow."},
    {"question": "What is the minimum maturation time for an AVF before cannulation, and what is the 'Rule of 6s'?",
     "answer": "Minimum 6 weeks, ideally 8-12 weeks. Rule of 6s: the fistula should be >6mm in diameter, <6mm deep from skin surface, have >600 mL/min flow, and be ≥6cm in usable length. Failure to mature occurs in 25-60% of radiocephalic fistulas (lower rate for brachiocephalic). Non-maturation is managed with balloon angioplasty of the juxta-anastomotic stenosis."}
]

QUESTIONS2["Carotid Endarterectomy"] = [
    {"question": "The internal and external carotid arteries develop from which aortic arch, and what is the embryologic origin of the carotid body?",
     "answer": "The 3rd aortic arch forms the common carotid and proximal internal carotid. The external carotid derives from the ventral aorta. The carotid body (a chemoreceptor) develops from the 3rd pharyngeal arch neural crest and mesoderm — it detects changes in O2, CO2, and pH."},
    {"question": "What are the borders of the carotid triangle, and what structures pass through it?",
     "answer": "Superior: posterior belly of digastric. Anterior: superior belly of omohyoid. Posterior: SCM. Contents: common carotid bifurcation, internal/external carotid, internal jugular vein, vagus nerve (CN X), hypoglossal nerve (CN XII), superior laryngeal nerve, and the ansa cervicalis."},
    {"question": "What is the blood supply to the brain that provides collateral during ICA clamping?",
     "answer": "Circle of Willis: anterior communicating artery (connects ACAs), posterior communicating arteries (connect ICA to PCA). External carotid collaterals: facial artery → ophthalmic artery retrograde flow into ICA. Shunt placement is used if EEG/stump pressure shows inadequate collateral (stump pressure <40 mmHg or EEG changes during clamping)."},
    {"question": "What is the most feared neurologic complication, and what are the two mechanisms?",
     "answer": "Stroke (1-3% for symptomatic stenosis, <1% for asymptomatic). Two mechanisms: 1) Thromboembolism (plaque debris or thrombus at the endarterectomy site), 2) Hypoperfusion (inadequate collateral during clamping). Post-operative hyperperfusion syndrome (headache, seizures, ICH) occurs when a previously hypoperfused brain receives normal flow after CEA — strict BP control (<140 systolic) prevents this."},
    {"question": "What are the NASCET and ACAS criteria for carotid endarterectomy?",
     "answer": "NASCET (symptomatic): CEA beneficial for 50-99% ICA stenosis (NNT = 6 for 70-99%). ACAS/ACST (asymptomatic): CEA beneficial for ≥60-70% stenosis IF perioperative stroke/death rate is <3%. CREST-2 trial is currently comparing CEA + BMT vs BMT alone for asymptomatic stenosis, questioning whether surgery is still needed in the era of modern medical therapy."}
]

QUESTIONS2["Femoral-Popliteal Bypass"] = [
    {"question": "The femoral artery develops from which embryologic vessel, and what transition occurs at the adductor hiatus?",
     "answer": "The external iliac artery (from the 5th lumbar intersegmental artery/umbilical artery system). At the adductor hiatus (opening in adductor magnus), the superficial femoral artery becomes the popliteal artery as it enters the popliteal fossa. This transition point is the most common site of atherosclerotic occlusion in the lower extremity."},
    {"question": "What is the anatomy of the femoral triangle, and what mnemonic helps remember the contents?",
     "answer": "Boundaries: inguinal ligament (superior), sartorius (lateral), adductor longus (medial). Floor: iliopsoas, pectineus. Contents (lateral to medial): NAVEL — Nerve, Artery, Vein, Empty space, Lymphatics. The femoral sheath encloses the artery, vein, and lymphatics but NOT the nerve (it's outside the sheath)."},
    {"question": "What conduit is preferred for femoral-popliteal bypass, and why?",
     "answer": "Autologous greater saphenous vein (reversed or in-situ) is the gold standard — 5-year primary patency 60-80% (above-knee) and 50-65% (below-knee). PTFE graft is acceptable for above-knee bypass (50-60% at 5 years) but significantly worse below-knee (30-40%). Vein is ALWAYS preferred below-knee. Preoperative vein mapping with duplex ultrasound is mandatory."},
    {"question": "What is the most common cause of early graft failure (<30 days) versus late failure (>2 years)?",
     "answer": "Early: technical error — anastomotic stenosis, graft kinking, retained valve leaflet (in-situ), or intimal flap. Late: neointimal hyperplasia (1-24 months) at the anastomotic sites, or progression of native atherosclerotic disease (>2 years). Graft surveillance with duplex ultrasound every 3 months for the first year detects stenoses before occlusion."},
    {"question": "What is the WIfI classification system, and how does it guide limb salvage decisions?",
     "answer": "Wound, Ischemia, and foot Infection staging: each graded 0-3. It predicts major amputation risk and benefit from revascularization. High WIfI scores (stage 4-5) predict >25% amputation risk at 1 year without intervention. It helps decide between revascularization (bypass vs endovascular) and primary amputation."}
]

QUESTIONS2["Arterial Embolectomy"] = [
    {"question": "Acute limb ischemia presents with the '6 Ps.' What are they, and which indicates irreversible damage?",
     "answer": "Pain, Pallor, Pulselessness, Poikilothermia (cool), Paresthesia, Paralysis. Paralysis and absent sensation indicate irreversible ischemia (Rutherford IIb-III) — muscle rigor and mottled non-blanching skin (class III) mean the limb is non-salvageable, and revascularization risks reperfusion injury with rhabdomyolysis, hyperkalemia, and death."},
    {"question": "What is the Fogarty catheter, and how does it work?",
     "answer": "A balloon-tipped catheter inserted through an arteriotomy (typically at the common femoral artery) and advanced past the embolus. The balloon is inflated and withdrawn, extracting the clot. Invented by Thomas Fogarty in 1963 — it revolutionized embolectomy by eliminating the need for direct exposure of the occlusion site. Available in sizes 2-7 Fr."},
    {"question": "What is the blood supply to the lower extremity distal to the popliteal trifurcation?",
     "answer": "The popliteal artery divides into: 1) Anterior tibial artery (becomes dorsalis pedis), 2) Tibioperoneal trunk → posterior tibial artery (becomes medial/lateral plantar arteries) and peroneal artery. At least one tibial vessel must be patent for limb viability. Embolectomy catheters are passed into each tibial vessel to ensure complete clot extraction."},
    {"question": "What is reperfusion injury after embolectomy, and what is the most dangerous systemic complication?",
     "answer": "Reperfusion of ischemic muscle releases myoglobin (rhabdomyolysis), potassium, lactate, and reactive oxygen species. Most dangerous: hyperkalemia causing cardiac arrest — can occur within minutes of restoring flow. Management: prophylactic calcium, bicarbonate, aggressive IV fluids, and continuous cardiac monitoring. Compartment syndrome (see below) is the most common local complication."},
    {"question": "What percentage of arterial emboli originate from the heart, and what is the most common cardiac source?",
     "answer": "80-85% are cardiac in origin. Most common source: left atrial appendage thrombus from atrial fibrillation. Other sources: mural thrombus (post-MI), valvular disease, endocarditis, paradoxical embolus (PFO). The remaining 15-20% are from arterial sources (aortic atheroma, aneurysm). Echocardiography is mandatory to identify the embolic source and guide anticoagulation."}
]

QUESTIONS2["Below Knee Amputation"] = [
    {"question": "The tibia and fibula develop from the limb bud mesoderm. What is the clinical significance of the anterior and posterior compartments for BKA wound healing?",
     "answer": "The anterior compartment (tibialis anterior, extensors) has relatively poor blood supply and thin muscle mass. The posterior compartment (gastrocnemius, soleus) has robust blood supply from the posterior tibial and peroneal arteries with thick muscle bulk. This is why BKA uses a long posterior myocutaneous flap (Burgess technique) — the well-vascularized posterior compartment provides the best healing tissue."},
    {"question": "What is the optimal tibial bone length for a BKA, and what landmark determines this?",
     "answer": "10-15cm below the tibial tubercle (or one hand-breadth below the knee). This length provides adequate lever arm for prosthetic fitting while leaving enough soft tissue for a well-padded stump. The fibula is divided 1-2cm shorter than the tibia to prevent lateral pressure on the prosthetic socket."},
    {"question": "What is the blood supply to the posterior flap in a BKA?",
     "answer": "Sural arteries (branches of the popliteal artery supplying the gastrocnemius), posterior tibial artery branches (supplying soleus), and peroneal artery branches. The posterior flap is designed 1.5x the AP diameter of the leg to provide adequate coverage. Adequate perfusion (ABI >0.5, TcPO2 >30 mmHg at the amputation level) predicts healing."},
    {"question": "What is the most common reason for BKA failure requiring revision to above-knee amputation?",
     "answer": "Wound dehiscence/non-healing from inadequate blood supply (40-50% of failed BKAs). Predictors: ABI <0.5, diabetes with calcified vessels (ABI falsely elevated), end-stage renal disease, non-ambulatory status, and severe infection. If the patient cannot walk on a BKA prosthesis, some argue that AKA is more appropriate because it heals more reliably."},
    {"question": "What is phantom limb pain versus residual limb pain, and how do you manage it?",
     "answer": "Phantom pain: pain perceived in the amputated limb (60-80% incidence), caused by cortical reorganization and neuronal hyperexcitability. Residual limb pain: pain at the stump from neuroma, bone spur, or poor prosthetic fit. Phantom pain management: mirror therapy, gabapentin/pregabalin, TENS, targeted muscle reinnervation (TMR), or dorsal root ganglion stimulation. TMR is increasingly used prophylactically at the time of amputation."}
]

# ============================================================
# THORACIC
# ============================================================

QUESTIONS2["VATS Lobectomy"] = [
    {"question": "The lungs develop from the respiratory diverticulum of the foregut. At what embryologic stage do the lobar bronchi form?",
     "answer": "Week 5: the respiratory bud divides into right (3 secondary bronchi → 3 lobes) and left (2 secondary bronchi → 2 lobes) primary bronchi. The right lung has 3 lobes because of asymmetric branching driven by cardiac positioning. By week 6, tertiary (segmental) bronchi form, establishing the bronchopulmonary segments."},
    {"question": "What is the hilar anatomy from anterior to posterior for the right versus left lung?",
     "answer": "Right hilum (anterior to posterior): superior pulmonary vein, pulmonary artery branches, bronchus (eparterial — above the artery for the upper lobe). Left hilum: superior pulmonary vein, pulmonary artery (highest structure), bronchus (hyparterial — below the artery). Mnemonic: Right = ABV (artery, bronchus, vein from superior to inferior). Left = APB."},
    {"question": "What is the bronchial artery blood supply, and why does it matter after lobectomy?",
     "answer": "Bronchial arteries (1 right, 2 left — from thoracic aorta or intercostal arteries) supply the bronchial wall, peribronchial tissue, and visceral pleura. After lobectomy, the bronchial stump heals via bronchial artery blood supply. If devascularized (excessive skeletonization), bronchial stump dehiscence/bronchopleural fistula occurs — the most feared complication (2-5% incidence, 20-70% mortality)."},
    {"question": "What is the most common complication after VATS lobectomy?",
     "answer": "Prolonged air leak (>5 days) — occurs in 8-15% of patients. Caused by incomplete fissure division or parenchymal injury. Managed with chest tube on water seal, chemical pleurodesis, or Heimlich valve for outpatient management. Other complications: atrial fibrillation (10-20%), pneumonia (5%), and bronchopleural fistula (1-2%)."},
    {"question": "What is the evidence for VATS versus open lobectomy for NSCLC?",
     "answer": "Multiple retrospective studies and the VIOLET RCT (2019): VATS lobectomy has equivalent oncologic outcomes (survival, node harvest, recurrence) with less pain, shorter hospital stay (3-4 vs 5-7 days), fewer complications, and better preserved pulmonary function. VATS is now the standard approach for early-stage NSCLC at experienced centers."}
]

QUESTIONS2["VATS Wedge Resection"] = [
    {"question": "The visceral pleura develops from which embryologic germ layer?",
     "answer": "Splanchnic mesoderm (same as the pulmonary parenchyma's connective tissue). The parietal pleura develops from somatic mesoderm of the body wall. This distinction explains why visceral pleural pain is poorly localized (visceral afferents via vagus) while parietal pleural pain is sharp and well-localized (somatic intercostal nerve innervation)."},
    {"question": "What is the '2-cm rule' for wedge resection of peripheral lung nodules?",
     "answer": "The surgical margin should be ≥2cm or ≥ the diameter of the nodule (whichever is greater) for oncologic adequacy. The JCOG0802/WJOG4607L trial (2022) showed sublobar resection (including wedge) was non-inferior to lobectomy for ≤2cm peripheral NSCLC — a landmark change. However, segmentectomy is preferred over wedge for oncologic sublobar resection."},
    {"question": "What is the blood supply to a pulmonary segment, and how does wedge resection differ from segmentectomy in this regard?",
     "answer": "Each bronchopulmonary segment has its own segmental pulmonary artery, bronchus, and vein. Wedge resection ignores segmental anatomy — it simply excises a peripheral wedge of parenchyma across segments. Segmentectomy follows the anatomic plane between segments, dividing the segmental vessels individually, which is more oncologically complete but technically harder."},
    {"question": "What technique is used to localize small or subpleural nodules for VATS wedge resection?",
     "answer": "Options: 1) CT-guided hook wire/coil placement (most common, done immediately preop), 2) Methylene blue injection (CT-guided), 3) Technetium-99m radiotracer injection with gamma probe detection, 4) ICG fluorescence (emerging), 5) Intraoperative ultrasound. Without localization, small (<1cm) or deep nodules may be impossible to find thoracoscopically."},
    {"question": "What is the air leak management algorithm after wedge resection?",
     "answer": "POD 0-1: chest tube to suction (-20 cmH2O). POD 1-2: convert to water seal if no air leak. If air leak persists: water seal (most stop within 3-5 days), Heimlich valve for outpatient management (if patient is otherwise well), autologous blood patch pleurodesis, or reoperation for persistent leak >7 days. Digital air leak monitoring quantifies the leak and predicts resolution."}
]

QUESTIONS2["Open Lobectomy"] = [
    {"question": "The right lung has 10 bronchopulmonary segments versus how many on the left, and why?",
     "answer": "Left lung: 8-9 segments (the lingula corresponds to the right middle lobe, and segments 1+2 often share a common bronchus as the apicoposterior segment, and segments 7+8 may share as the anteromedial basal). The cardiac notch reduces left lung volume. Knowledge of segmental anatomy is critical for identifying intersegmental planes during lobectomy."},
    {"question": "What is the major (oblique) fissure landmark, and what structures cross it?",
     "answer": "The major fissure runs from T3-T4 posteriorly to the 6th costal cartilage anteriorly, separating the upper from lower lobe (and upper from middle on the right). The pulmonary artery branches and pulmonary veins cross or lie within the fissure — an incomplete fissure (common) requires fissure completion using staplers before vessel isolation."},
    {"question": "During open lobectomy, what is the order of vessel ligation for a right upper lobectomy?",
     "answer": "Classically: 1) Ligate the right upper lobe (truncus anterior) pulmonary artery branch, 2) Divide the right upper lobe bronchus, 3) Ligate the superior pulmonary vein upper lobe tributaries, 4) Complete the fissure. Some surgeons prefer 'fissureless' technique: vein → artery → bronchus → fissure stapling, which avoids extensive fissure dissection and reduces air leak."},
    {"question": "What is a bronchopleural fistula, and what is its mortality?",
     "answer": "Communication between the bronchial stump and pleural space, presenting as air leak, empyema, fever, and potentially massive aspiration of empyema fluid into the contralateral lung. Mortality: 20-70%. Risk factors: right pneumonectomy (long stump) > right lower lobectomy, neoadjuvant chemoradiation, diabetes, and devascularized bronchial stump. Treatment: muscle flap buttressing (intercostal, latissimus, serratus, omentum)."},
    {"question": "What is the predicted postoperative FEV1 (ppoFEV1) threshold for lobectomy, and how is it calculated?",
     "answer": "ppoFEV1 >40% predicted (or >0.8L absolute) is required for lobectomy. Calculated: ppoFEV1 = preop FEV1 × (1 - functional segments removed / total functional segments). Quantitative V/Q scan provides the most accurate segment-level function. If borderline, cardiopulmonary exercise testing (VO2max >15 mL/kg/min = safe, <10 = prohibitive) determines surgical risk."}
]

QUESTIONS2["Pneumonectomy"] = [
    {"question": "What embryologic feature explains why the right main bronchus is more commonly intubated and aspirated?",
     "answer": "The right main bronchus is wider, shorter, and more vertically oriented than the left (due to the aortic arch pushing the left bronchus laterally and inferiorly during development). This anatomic asymmetry from differential embryologic growth makes the right bronchus the path of least resistance for foreign bodies and endotracheal tubes."},
    {"question": "What is the critical step in managing the bronchial stump after pneumonectomy?",
     "answer": "The bronchial stump must be: 1) Divided flush with the carina (no long stump — long stumps collect secretions and increase BPF risk), 2) Closed with stapler or hand-sewn interrupted sutures, 3) Tested for air leak under saline, 4) Covered/buttressed with a vascularized tissue flap (intercostal muscle, pericardial fat, serratus, or pleural flap) to reinforce healing and prevent fistula."},
    {"question": "What is the blood supply to the bronchial stump that determines healing after pneumonectomy?",
     "answer": "Bronchial arteries (from thoracic aorta). After pneumonectomy, the stump is completely dependent on the remaining bronchial artery supply. Excessive skeletonization or devascularization of the stump during lymph node dissection causes ischemic stump necrosis and bronchopleural fistula. Tissue flap buttressing provides additional blood supply."},
    {"question": "What is postpneumonectomy syndrome, and on which side does it occur?",
     "answer": "Right pneumonectomy (mostly in children) → mediastinal shift to the right → left main bronchus compression against the thoracic spine or aorta → progressive dyspnea and recurrent pneumonia. Less common after left pneumonectomy. Treatment: tissue expander or saline-filled prosthesis in the empty hemithorax to re-center the mediastinum."},
    {"question": "What is the operative mortality of pneumonectomy, and what predicts poor outcome?",
     "answer": "Operative mortality: 5-10% (right pneumonectomy higher than left — 10-12% vs 5-6%). Predictors: right-sided resection, neoadjuvant chemoradiation (increases BPF risk 2-3x), ppoFEV1 <40%, DLCO <40%, cardiac disease. The high mortality is why alternatives (sleeve lobectomy preserving lung parenchyma) are preferred when oncologically feasible."}
]

QUESTIONS2["VATS Pleurodesis"] = [
    {"question": "The pleural cavity forms from the intraembryonic coelom. What embryologic membrane separates the pleural from the peritoneal cavity?",
     "answer": "The pleuroperitoneal membrane — one of the four components of the diaphragm. Failure of this membrane to close causes a Bochdalek hernia (congenital diaphragmatic hernia, posterolateral, left > right). The pleuropericardial membrane separates the pleural from the pericardial cavity."},
    {"question": "What is the anatomy of the pleural space, and what maintains negative intrapleural pressure?",
     "answer": "The pleural space is a potential space between the visceral (on lung) and parietal (on chest wall/diaphragm/mediastinum) pleura. Normal: 5-15 mL of serous fluid. Negative pressure (-5 cmH2O at FRC) is maintained by elastic recoil of the lung pulling inward and chest wall springing outward. Disruption of either pleural surface allows air entry (pneumothorax) or fluid accumulation (effusion)."},
    {"question": "What is the blood supply to the parietal pleura, and why is mechanical pleurodesis painful?",
     "answer": "Parietal pleura: intercostal arteries, internal mammary, musculophrenic (somatic blood supply = somatic innervation by intercostal nerves = sharp, localizable pain). Visceral pleura: bronchial arteries (visceral innervation = dull, poorly localized pain). Mechanical pleurodesis (abrasion) irritates the parietal pleura's somatic nerve endings, causing significant postoperative pain."},
    {"question": "What are the two types of pleurodesis, and what is the success rate for preventing recurrent pneumothorax?",
     "answer": "Chemical: talc poudrage (insufflation of sterile talc — 95% success rate for malignant effusion) or talc slurry via chest tube. Mechanical: pleural abrasion with a scratch pad, partial pleurectomy, or electrocautery. For spontaneous pneumothorax: mechanical pleurodesis + bleb resection (stapled wedge) achieves <5% recurrence. Talc: 90-95% success for malignant effusions."},
    {"question": "What is the feared complication of talc pleurodesis, and how has it been mitigated?",
     "answer": "ARDS (acute respiratory distress syndrome) — historically reported in 1-9% with non-graded (small particle) talc. The mechanism: small talc particles (<15 micrometers) are absorbed systemically, causing widespread inflammation. Mitigation: use large-particle graded talc (>25 micrometers, e.g., Steritalc), which stays in the pleural space. With graded talc, ARDS risk is <1%."}
]

QUESTIONS2["VATS Decortication"] = [
    {"question": "An empyema progresses through three stages. What are they, and at which stage is decortication indicated?",
     "answer": "Stage I (Exudative, days 1-3): thin fluid, lung expandable — chest tube drainage sufficient. Stage II (Fibrinopurulent, days 4-14): fibrin strands, loculations — VATS with lysis of adhesions. Stage III (Organized, >14 days): thick pleural peel (cortex) trapping the lung — decortication is required. The fibrous peel prevents lung expansion, creating a fixed restrictive defect."},
    {"question": "What is the anatomic plane of decortication — where exactly do you dissect?",
     "answer": "Between the fibrous cortex (peel) and the visceral pleura. This extrapleural plane is avascular when correctly identified. If you enter the lung parenchyma, you cause massive air leak and hemorrhage. The cortex is grasped with ring forceps and carefully peeled off the visceral pleura — like peeling the skin off an orange."},
    {"question": "What is the blood supply to the pleural cortex, and why does it develop?",
     "answer": "The cortex develops neovascularity from the parietal pleural blood supply (intercostal arteries). Fibrin deposition organizes into collagen with ingrowth of capillaries from the parietal pleura. This is why the parietal cortex is often more vascular (and bleeds more) than the visceral cortex. Parietal decortication must be done carefully to avoid intercostal artery injury."},
    {"question": "What is the expected improvement in pulmonary function after successful decortication?",
     "answer": "FEV1 improves 300-500 mL (20-40% improvement) as the trapped lung re-expands. Maximum improvement occurs over 3-6 months as the lung parenchyma remodels. If the lung has been trapped >6 months, the parenchyma may be permanently fibrotic and not fully re-expand — earlier decortication yields better functional results."},
    {"question": "What is re-expansion pulmonary edema, and when does it occur after decortication?",
     "answer": "Non-cardiogenic pulmonary edema in the re-expanded lung, presenting within 24-48 hours with hypoxia and unilateral infiltrate. Occurs in 1-5% after decortication, more common when the lung has been collapsed >3 days. Mechanism: increased capillary permeability from ischemia-reperfusion injury. Treatment: supportive (O2, CPAP/BiPAP, diuretics). Usually self-limited."}
]

# ============================================================
# PROCEDURES / BEDSIDE / ACCESS
# ============================================================

QUESTIONS2["Cricothyroidotomy"] = [
    {"question": "The cricothyroid membrane develops between which two cartilages, and what embryologic pharyngeal arches form these structures?",
     "answer": "Between the thyroid cartilage (4th pharyngeal arch) and cricoid cartilage (6th pharyngeal arch). The cricothyroid membrane is the easiest access point for emergency surgical airway because it is subcutaneous, avascular in the midline, and located between palpable landmarks."},
    {"question": "What are the surface landmarks for identifying the cricothyroid membrane?",
     "answer": "Palpate the thyroid notch (Adam's apple) → slide finger inferiorly over the thyroid cartilage prominence → feel the depression between thyroid and cricoid cartilages (the membrane). In obese patients, the 'laryngeal handshake' (stabilizing the larynx between thumb and middle finger while index finger palpates the membrane) improves identification."},
    {"question": "What vessels run along the superior and inferior borders of the cricothyroid membrane?",
     "answer": "The superior cricothyroid artery (branch of the superior thyroid artery) runs along the superior border. The inferior cricothyroid artery runs along the inferior border. The MIDLINE of the membrane is relatively avascular — the incision should be horizontal through the lower third of the membrane to avoid the superior vessels."},
    {"question": "Why is cricothyroidotomy contraindicated in children under 10-12 years?",
     "answer": "The cricothyroid membrane is very small in children, and the cricoid cartilage is the narrowest and only complete cartilaginous ring in the airway — damage causes subglottic stenosis, which is the most devastating long-term airway complication in pediatrics. Needle cricothyroidotomy with jet ventilation is the preferred emergency surgical airway in children <10-12 years."},
    {"question": "What is the complication rate of surgical cricothyroidotomy in emergency settings?",
     "answer": "Overall complication rate: 10-40% (higher in emergency than elective). Complications: false passage (most common technical error), bleeding, posterior tracheal wall injury, subglottic stenosis (5-10% if not converted to formal tracheostomy within 48-72 hours), voice changes, and esophageal perforation. Convert to tracheostomy within 48-72 hours when the patient is stable."}
]

QUESTIONS2["Open Tracheostomy"] = [
    {"question": "The trachea develops from the ventral foregut, separating from the esophagus via the tracheoesophageal septum. At what level do the tracheal rings begin?",
     "answer": "The trachea extends from C6 (cricoid cartilage) to T4-T5 (carina). It has 16-20 C-shaped hyaline cartilage rings (incomplete posteriorly — the posterior membrane is shared with the esophagus). The isthmus of the thyroid typically overlies tracheal rings 2-4, which is the standard tracheostomy site."},
    {"question": "Between which tracheal rings is the tracheostomy typically placed, and what structure overlies this area?",
     "answer": "Between rings 2-3 or 3-4 (below the thyroid isthmus or after dividing/retracting it). The thyroid isthmus must be divided or retracted superiorly. Placing the tracheostomy too high (ring 1) risks subglottic stenosis. Too low (ring 5+) risks innominate artery erosion — the most catastrophic late complication."},
    {"question": "What is the blood supply to the anterior tracheal wall at the tracheostomy site?",
     "answer": "Lateral tracheal blood supply from the inferior thyroid arteries. The anterior trachea between the rings is relatively avascular (supplied by small branches). The thyroid ima artery (present in 3-10%, arising from the brachiocephalic trunk) may course in the midline anterior to the trachea — this is a dangerous vessel if not anticipated."},
    {"question": "What is the most feared late complication of tracheostomy?",
     "answer": "Tracheo-innominate artery fistula (TIF) — erosion of the tracheostomy tube or cuff into the innominate artery, causing massive hemorrhage (mortality 75-85%). Occurs 3-42 days post-tracheostomy. Sentinel bleed (small pulsatile bleed) precedes massive hemorrhage in 50%. Emergency management: hyperinflate cuff, digital pressure through the stoma, median sternotomy for innominate artery ligation/repair."},
    {"question": "When should tracheostomy be performed in the critically ill patient — early versus late?",
     "answer": "Early tracheostomy (≤7-10 days of intubation) may reduce ICU stay, sedation requirements, and ventilator days, but does NOT reduce mortality (TracMan trial, 2013). Benefits: improved patient comfort, easier secretion management, reduced laryngeal injury, and facilitated weaning. Most ICU practice: consider tracheostomy if extubation is not expected within 10-14 days."}
]

QUESTIONS2["Percutaneous Tracheostomy"] = [
    {"question": "What embryologic relationship between the trachea and esophagus makes posterior tracheal wall injury possible during percutaneous tracheostomy?",
     "answer": "The trachea and esophagus develop from the common foregut tube, separated by the tracheoesophageal septum. The posterior tracheal wall (membranous portion) shares a common wall with the anterior esophagus. The dilator can penetrate through this membranous wall into the esophagus — bronchoscopic guidance prevents this by confirming anterior/midline needle placement."},
    {"question": "What is the Ciaglia technique, and how does it differ from the Griggs technique?",
     "answer": "Ciaglia (most common): serial dilators (Blue Rhino single-step dilator) over a guidewire after Seldinger needle access into the trachea. Griggs: guide wire dilating forceps (Howard-Kelly forceps) to create the stoma. Ciaglia is more popular due to its simplicity and safety profile. Both require bronchoscopic guidance for safe needle placement."},
    {"question": "What is the pretracheal vascular anatomy that must be considered?",
     "answer": "The anterior jugular veins and their communicating veins cross the midline in the pretracheal space. The inferior thyroid veins drain into the brachiocephalic veins in the midline. The thyroid ima artery (3-10%) courses directly in front of the trachea. Ultrasound-guided preprocedure assessment identifies these vessels and prevents hemorrhage."},
    {"question": "What are the absolute contraindications to percutaneous tracheostomy?",
     "answer": "1) Pediatric patients (<12 years — small trachea), 2) Inability to identify landmarks (massive neck swelling, morbid obesity, prior neck surgery/radiation), 3) Emergency airway (cricothyroidotomy faster), 4) Coagulopathy that cannot be corrected, 5) High ventilatory requirements (PEEP >15, FiO2 >0.8 — risk during brief disconnection). Relative: cervical spine instability, tumor/vascular anomaly over the access site."},
    {"question": "What is the complication rate of percutaneous versus open tracheostomy?",
     "answer": "Percutaneous: wound infection 0-4% (lower than open), bleeding 2-5%, posterior wall injury 1%, pneumothorax <1%. Open: wound infection 5-10%, bleeding 3-5%, tracheal stenosis 1-2%. Meta-analyses show percutaneous has lower wound infection rates and comparable overall complications, with the advantage of bedside ICU performance (avoiding transport to OR)."}
]

QUESTIONS2["Central Venous Access"] = [
    {"question": "The subclavian vein develops from which embryologic venous system?",
     "answer": "The anterior cardinal vein system. The subclavian vein forms from the caudal portion of the anterior cardinal vein. The left brachiocephalic vein bridges between the left anterior cardinal system and the right (forming the SVC). This embryologic asymmetry explains why the SVC is right-sided and why the left-sided approach has a longer course to the SVC."},
    {"question": "What are the anatomic landmarks for subclavian vein access?",
     "answer": "The subclavian vein runs anterior to the anterior scalene muscle (and subclavian artery, which is posterior to the scalene). Landmark: junction of the medial and middle thirds of the clavicle. Needle directed toward the sternal notch, walking under the clavicle. Vein is between the clavicle and first rib. The subclavian vein is NOT compressible (between bone), so it cannot be US-guided as easily as IJ, and bleeding complications are managed differently."},
    {"question": "What is the blood supply/anatomy that makes the internal jugular vein preferred for central access?",
     "answer": "The IJ runs within the carotid sheath, lateral to the carotid artery and vagus nerve, under the sternocleidomastoid muscle. Ultrasound-guided IJ access is now the standard (2003 NICE guidelines). The IJ is compressible (unlike subclavian), and inadvertent carotid puncture can be managed with direct pressure. Landmarks: apex of the triangle formed by the two heads of the SCM."},
    {"question": "What is the most feared immediate complication of subclavian central line placement?",
     "answer": "Pneumothorax (1-6% landmark-guided, <1% US-guided) — the cupola of the pleura rises above the first rib. Also: subclavian artery puncture (cannot compress between clavicle and rib, may need endovascular intervention), hemothorax, and air embolism. Post-procedure CXR is mandatory to confirm tip position (at the cavo-atrial junction) and rule out pneumothorax."},
    {"question": "What is the optimal CVC tip position, and what complication results from malposition?",
     "answer": "Cavo-atrial junction (lower SVC) — confirmed by CXR (tip at or just above the carina). Too high (brachiocephalic): catheter thrombosis, venous stenosis. Too deep (right atrium): arrhythmia, cardiac perforation, tamponade. Left-sided lines must cross the midline and can impinge on the left brachiocephalic-SVC junction — higher thrombosis risk."}
]

QUESTIONS2["Arterial Line Placement"] = [
    {"question": "The radial artery is the continuation of which embryologic vessel, and what makes it ideal for arterial monitoring?",
     "answer": "The radial artery develops from the superficial brachial artery system. It is ideal for arterial line because: 1) superficial location (easily palpated/visualized with US), 2) collateral circulation from the ulnar artery via the palmar arches (confirmed by Allen test), 3) no major nerves/veins adjacent, and 4) accessible without moving the patient."},
    {"question": "What is the collateral circulation to the hand if the radial artery thromboses?",
     "answer": "The ulnar artery via the superficial palmar arch (dominant, from ulnar artery) and deep palmar arch (dominant, from radial artery). In 3-5% of patients, the palmar arches are incomplete — if the ulnar artery cannot supply the entire hand alone, radial artery cannulation risks hand ischemia. The modified Allen test or Doppler assessment confirms adequacy."},
    {"question": "What are the alternative sites for arterial line placement beyond the radial artery?",
     "answer": "2nd choice: femoral artery (easy access, larger vessel, but higher infection risk and requires patient immobility). 3rd: dorsalis pedis (small, often absent in 5-10%). 4th: axillary/brachial (risk of median nerve injury at the brachial site). 5th: ulnar artery (avoid if the hand depends on it for collateral flow)."},
    {"question": "What is the most common complication of arterial line placement?",
     "answer": "Thrombosis of the radial artery (10-20% incidence, but symptomatic ischemia <1% due to collateral flow). Risk factors: prolonged cannulation (>4 days), large catheter relative to artery size, female sex, peripheral vascular disease. Prevention: use 20-gauge catheter (smallest effective), continuous heparinized flush, and remove as soon as no longer needed."},
    {"question": "What causes 'arterial line dampening,' and how do you differentiate it from true hypotension?",
     "answer": "Dampening: flattened waveform with falsely low systolic and falsely high diastolic readings. Causes: air bubbles, clot at the catheter tip, kinking, overly compliant tubing, or catheter against the vessel wall. Differentiate: 1) flush test (square wave test — should return to baseline within 1-2 oscillations), 2) compare with NIBP cuff reading, 3) aspirate/flush the line. A dampened waveform does NOT equal hypotension."}
]

QUESTIONS2["Chest Tube Insertion"] = [
    {"question": "The pleural cavity develops from the intraembryonic coelom. What maintains the pleural space as a potential space?",
     "answer": "Surface tension of a thin layer (5-15 mL) of serous fluid between the visceral and parietal pleura, plus negative intrapleural pressure (-5 cmH2O at FRC) generated by the elastic recoil of the lung and outward spring of the chest wall. Loss of negative pressure (air/fluid entry) collapses the lung."},
    {"question": "What is the 'safe triangle' for chest tube insertion, and what structures must you avoid?",
     "answer": "The safe triangle is bordered by: anterior border of latissimus dorsi (posterior), lateral border of pectoralis major (anterior), a line at the level of the nipple/5th intercostal space (inferior), and the axillary apex (superior). Insert ABOVE the rib (neurovascular bundle runs in the costal groove BELOW each rib: vein-artery-nerve from superior to inferior)."},
    {"question": "What is the intercostal neurovascular bundle's relationship to the rib?",
     "answer": "The intercostal vein, artery, and nerve (VAN, superior to inferior) run in the costal groove along the INFERIOR border of each rib. The tube must be inserted just ABOVE the rib to avoid these structures. However, collateral intercostal vessels run along the SUPERIOR border of the rib below — the true 'safest' zone is the mid-intercostal space."},
    {"question": "What size chest tube should be used for pneumothorax versus hemothorax?",
     "answer": "Pneumothorax: 14-24 Fr (smaller, pigtail catheters 14 Fr are increasingly used and are equally effective per the MIST2 and other trials). Hemothorax: 28-36 Fr (large bore to prevent clot obstruction — retained hemothorax leads to empyema in 5-7%). Massive hemothorax (>1500 mL initial output or >200 mL/hr) mandates thoracotomy."},
    {"question": "What is the threshold for chest tube output that mandates surgical exploration for hemothorax?",
     "answer": "Initial output >1500 mL, OR >200 mL/hr for 2-4 consecutive hours. Also: hemodynamic instability despite resuscitation, or retained hemothorax >500 mL after tube placement. These criteria reflect ongoing hemorrhage requiring surgical control (thoracotomy or VATS). The source is typically an intercostal artery (60%), lung parenchyma (30%), or major vessel (10%)."}
]

QUESTIONS2["Flexible Bronchoscopy"] = [
    {"question": "The tracheal bifurcation (carina) is at what vertebral level, and which main bronchus is the target for foreign body aspiration?",
     "answer": "T4-T5 (at the sternal angle of Louis). The right main bronchus is more commonly the site of foreign body aspiration because it is wider (1.2 vs 1.0 cm), shorter (2.5 vs 5.0 cm), and more vertically oriented (25° vs 45° from tracheal axis) — all due to the aortic arch displacing the left bronchus."},
    {"question": "What is the bronchial anatomy that the bronchoscopist must identify — name the right-sided segmental bronchi of the upper lobe.",
     "answer": "Right upper lobe: Apical (B1), Posterior (B2), Anterior (B3). The right upper lobe bronchus is 'eparterial' (arises above the right pulmonary artery). The right middle lobe has Lateral (B4) and Medial (B5). Right lower lobe: Superior (B6), Medial basal (B7), Anterior basal (B8), Lateral basal (B9), Posterior basal (B10)."},
    {"question": "What is the blood supply to the bronchial tree visible during bronchoscopy?",
     "answer": "Bronchial arteries (1 right, 2 left from thoracic aorta) supply the bronchial mucosa and wall. These are visible as submucosal vessels on bronchoscopy. In chronic inflammatory conditions (bronchiectasis, TB, cystic fibrosis), bronchial arteries hypertrophy massively and can cause life-threatening hemoptysis. Bronchial artery embolization is the treatment for massive hemoptysis."},
    {"question": "What is the most common complication of transbronchial biopsy during flexible bronchoscopy?",
     "answer": "Pneumothorax (1-5%) from puncturing the visceral pleura during peripheral parenchymal biopsy. Also: hemorrhage (1-2%, usually self-limited), desaturation, and bronchospasm. Always obtain CXR post-transbronchial biopsy. Fluoroscopic guidance during biopsy reduces pneumothorax rate. Navigational bronchoscopy (electromagnetic navigation) improves peripheral lesion access."},
    {"question": "What are the indications for rigid versus flexible bronchoscopy?",
     "answer": "Rigid: massive hemoptysis (better suction, airway control), foreign body removal (better grasping tools), tracheal/bronchial stenting, tumor debulking, airway dilation. Flexible: diagnostic evaluation, BAL (bronchoalveolar lavage), transbronchial biopsy, EBUS-TBNA (endobronchial ultrasound), ICU bedside evaluation, difficult intubation adjunct. Rigid requires general anesthesia; flexible can be done with moderate sedation."}
]

QUESTIONS2["Incision and Drainage of Abscess"] = [
    {"question": "What is the difference between an abscess and a phlegmon from a tissue development standpoint?",
     "answer": "An abscess has a mature fibrous capsule (fibroblast-deposited collagen) surrounding liquefied necrotic tissue and pus — it's walled off and will not respond to antibiotics alone. A phlegmon is a diffuse inflammatory process without a formed capsule — it represents an earlier stage that may respond to antibiotics. Only true abscesses require I&D."},
    {"question": "What is the anatomy of the subcutaneous tissue that determines abscess cavity extent?",
     "answer": "Superficial fascia (Camper's fascia — fatty layer) allows abscess spread. Deep fascia (Scarpa's fascia/investing fascia of muscles) limits deep extension. Abscesses following fascial planes can extend much farther than the surface appearance suggests — always explore the cavity with a finger to break up all loculations and assess true extent."},
    {"question": "What is the blood supply to the wound edges after I&D, and why is primary closure sometimes acceptable?",
     "answer": "The subdermal plexus from perforating arteries of the underlying named vessels. Primary closure after I&D (with or without loop drainage) has been shown in RCTs (Singer 2013, JAMA) to accelerate healing with equivalent recurrence rates for small (≤5cm) abscesses. The key: adequate drainage of the cavity and breaking up loculations before closure."},
    {"question": "What is the most common organism in skin abscesses, and when should you add antibiotics?",
     "answer": "MRSA (methicillin-resistant Staph aureus) is now the #1 cause of community-acquired skin abscesses in the US. I&D alone is curative for most simple abscesses. Add antibiotics when: cellulitis extends beyond the abscess, systemic signs (fever, WBC), immunocompromised, device-adjacent, or abscess >5cm. TMP-SMX or doxycycline cover community MRSA."},
    {"question": "When should you NOT perform a simple bedside I&D, and what should you do instead?",
     "answer": "Do NOT perform bedside I&D for: perianal/perirectal abscess (OR under anesthesia — may have fistula requiring exam under anesthesia), hand/deep space infections (flexor sheath — OR with proper exposure), breast abscess (may need US-guided drainage or OR), and any abscess near major neurovascular structures. Also suspect necrotizing fasciitis if pain is out of proportion, crepitus, or hemodynamic instability — this needs emergent OR debridement, not I&D."}
]

QUESTIONS2["Excisional Biopsy"] = [
    {"question": "What are the embryologic tissue layers encountered during excisional biopsy of a subcutaneous mass?",
     "answer": "Epidermis (ectoderm) → dermis (mesoderm) → subcutaneous fat (Camper's fascia, mesoderm) → deep fascia (mesoderm). Most subcutaneous masses (lipomas, sebaceous cysts, fibromas) arise from mesodermal tissue. Dermoid cysts uniquely contain ectodermal elements (hair, sebaceous glands) because they form from trapped ectoderm during embryonic closure."},
    {"question": "What is the correct incision orientation for excisional biopsy, and why?",
     "answer": "Along Langer's lines (relaxed skin tension lines) — these follow the orientation of dermal collagen fibers. Incisions parallel to Langer's lines heal with less scar widening and better cosmesis. On the extremities, longitudinal incisions are used to avoid compromising future definitive surgery. For suspected melanoma, orient the incision longitudinally on the extremity to facilitate future wide local excision."},
    {"question": "What is the blood supply to the skin that must be preserved to ensure wound healing?",
     "answer": "Subdermal (subpapillary) arterial plexus fed by musculocutaneous, septocutaneous, or direct cutaneous perforators from underlying named arteries. Undermining the wound edges at the dermal-subcutaneous junction preserves this plexus while allowing wound closure without tension. Excessive undermining devascularizes the wound edges."},
    {"question": "What is the difference between excisional, incisional, core needle, and fine needle aspiration biopsy?",
     "answer": "Excisional: removes entire mass with margin (diagnostic AND therapeutic for small benign masses). Incisional: removes a portion (for large masses where excision would be morbid — preserves architecture). Core needle: tissue cylinder with preserved architecture (best for breast, soft tissue). FNA: cells only (no architecture — good for thyroid, lymph nodes). Excisional biopsy is preferred when the mass is small enough to remove entirely."},
    {"question": "For a suspected sarcoma, why should you NEVER perform excisional biopsy without preoperative imaging?",
     "answer": "Unplanned excision ('whoops' surgery) of a sarcoma contaminates tissue planes, makes definitive re-excision much larger (needs to remove the entire biopsy track and surrounding contaminated tissue), may compromise limb salvage, and worsens oncologic outcomes. Any soft tissue mass >5cm, deep to fascia, or rapidly growing needs MRI BEFORE biopsy, and biopsy should be core needle (not excisional) oriented along the planned definitive surgical approach."}
]

QUESTIONS2["Skin Graft"] = [
    {"question": "What are the embryologic origins of the epidermis versus dermis, and how does this relate to skin graft take?",
     "answer": "Epidermis: surface ectoderm. Dermis: mesoderm (dermatome). A skin graft survives by: 1) Plasmatic imbibition (24-48h — passive absorption of plasma nutrients from the wound bed), 2) Inosculation (48-72h — anastomosis of graft and bed capillaries), 3) Neovascularization (day 3-5 — ingrowth of new vessels). The wound bed must have adequate blood supply — grafts do NOT take on bare bone, tendon without peritenon, or avascular tissue."},
    {"question": "What is the difference between split-thickness and full-thickness skin grafts in terms of dermal content?",
     "answer": "STSG: epidermis + partial dermis (0.010-0.018 inches). Takes more readily (thinner = easier imbibition) but contracts more (30-50%), has worse cosmesis, and has less sensation. FTSG: epidermis + full dermis (including all appendages). Takes less readily but contracts less (10-15%), has better cosmesis, color match, and durability. Donor site: STSG heals by re-epithelialization from adnexal remnants; FTSG donor must be closed primarily."},
    {"question": "What is the blood supply to a skin graft recipient site, and what causes graft failure?",
     "answer": "The recipient wound bed must have a vascularized surface (granulation tissue, muscle, periosteum, perichondrium). Causes of failure (the 'enemies of graft take'): 1) Hematoma/seroma (prevents contact — #1 cause), 2) Infection (bacteria destroy the vascular interface), 3) Shear forces (disrupts inosculation), 4) Avascular bed (bare bone, tendon, irradiated tissue)."},
    {"question": "What is the 'pie-crusting' or meshing technique for STSGs, and when is it used?",
     "answer": "Passing the STSG through a mesher to create a net-like pattern (1:1.5 or 1:3 expansion ratio). Advantages: covers larger area with less donor tissue, allows fluid drainage (prevents seroma/hematoma beneath graft), conforms to irregular surfaces. Disadvantages: meshed appearance (poorer cosmesis), cannot be used on face/hands. Non-meshed (sheet) grafts are used for cosmetically important areas."},
    {"question": "What is a negative pressure wound therapy (VAC) bolster over a skin graft, and what does it do?",
     "answer": "A sponge connected to continuous suction (-75 to -125 mmHg) placed over the skin graft. It: 1) Prevents shear and hematoma/seroma accumulation (eliminates the #1 and #3 causes of failure), 2) Increases contact with wound bed, 3) Promotes neovascularization through mechanical stimulation. Graft take rates improve from 85% to >95% with VAC bolster, especially over irregular surfaces."}
]

QUESTIONS2["Fasciotomy for Compartment Syndrome"] = [
    {"question": "The four compartments of the lower leg develop from embryologic myotome divisions. What are they, and what muscle/nerve is in each?",
     "answer": "1) Anterior: tibialis anterior, extensors, deep peroneal nerve. 2) Lateral: peroneus longus/brevis, superficial peroneal nerve. 3) Deep posterior: tibialis posterior, flexors, posterior tibial artery, tibial nerve. 4) Superficial posterior: gastrocnemius, soleus, sural nerve. The anterior compartment is most commonly affected (least compliant fascia)."},
    {"question": "What is the pathophysiology of compartment syndrome at the microvascular level?",
     "answer": "Rising intracompartmental pressure exceeds capillary perfusion pressure (not arterial pressure — distal pulses remain present). The critical threshold: absolute pressure >30 mmHg OR delta pressure <30 mmHg (diastolic BP - compartment pressure). Ischemia → muscle necrosis → myoglobin release → renal failure. The 'golden window' is 6 hours — irreversible necrosis occurs after this."},
    {"question": "What is the blood supply to the lower leg compartments, and why does compartment syndrome preserve palpable pulses?",
     "answer": "Anterior tibial artery (anterior compartment), posterior tibial artery (deep posterior), peroneal artery (deep posterior/lateral). Compartment syndrome occludes capillaries/venules (pressure 30-40 mmHg) but NOT arteries (systolic pressure 90-120 mmHg). This is why palpable distal pulses do NOT rule out compartment syndrome — it's a microvascular, not macrovascular, problem."},
    {"question": "How many incisions are needed for a complete four-compartment lower leg fasciotomy?",
     "answer": "TWO incisions: 1) Anterolateral incision (over the intermuscular septum between anterior and lateral compartments — releases both), 2) Medial incision (2cm posterior to the tibial border — releases deep and superficial posterior compartments). Each incision must be full length of the compartment. Partial fasciotomy is NEVER adequate."},
    {"question": "What is the management of the fasciotomy wound after decompression?",
     "answer": "Leave open with wet dressings or VAC therapy. Reassess at 48-72 hours for muscle viability (debride necrotic muscle). Delayed primary closure or skin grafting typically at 5-7 days once swelling resolves. Vessel loop shoelace technique allows gradual wound approximation. If left open too long, the wound edges retract and primary closure becomes impossible — requiring STSG."}
]

QUESTIONS2["Necrotizing Fasciitis Debridement"] = [
    {"question": "Necrotizing fasciitis (NF) spreads along which tissue plane, and what embryologic layer does this correspond to?",
     "answer": "The superficial fascia (between the subcutaneous fat and deep fascia) — this plane corresponds to the mesoderm-derived investing fascia. The fascia has relatively poor blood supply compared to overlying dermis or underlying muscle, allowing bacterial spread with thrombosis of perforating vessels. Type I (polymicrobial) and Type II (Group A Strep/monomicrobial) are the two classifications."},
    {"question": "What are the clinical signs that distinguish NF from simple cellulitis?",
     "answer": "Pain out of proportion to exam (#1 early sign), rapidly spreading erythema, skin discoloration (gray, dusky, necrotic), crepitus (gas gangrene variant), bullae/blisters, cutaneous anesthesia (nerve necrosis), systemic toxicity (fever, tachycardia, hypotension). The LRINEC score (WBC, CRP, glucose, hemoglobin, sodium, creatinine) >6 suggests NF but should NOT delay surgery when clinical suspicion is high."},
    {"question": "What is the blood supply disruption that causes the overlying skin necrosis in NF?",
     "answer": "Thrombosis of the perforating arteries that pass through the fascia to supply the dermis and epidermis. As bacteria spread along the fascia, they produce enzymes and toxins (hyaluronidase, collagenase, lipase, streptokinase) that cause microvascular thrombosis. The overlying skin becomes necrotic because its blood supply from the deep perforators is destroyed from below."},
    {"question": "What is the operative endpoint of NF debridement?",
     "answer": "Healthy, bleeding tissue at all wound margins. The fascia should resist tearing with gentle traction (necrotic fascia separates easily from underlying muscle with a finger — the 'finger test'). Multiple trips to the OR (every 24-48 hours) for re-inspection and further debridement are the rule, not the exception. Average: 3-4 debridements. Inadequate initial debridement is the #1 predictor of mortality."},
    {"question": "What is the mortality rate of NF, and what is Fournier's gangrene?",
     "answer": "Mortality: 20-40% overall (higher with delayed diagnosis, immunosuppression, or truncal involvement). Fournier's gangrene is NF of the perineum/genitalia — mortality 20-40%. It spreads along Colles' fascia (perineum), Dartos fascia (scrotum), and Scarpa's fascia (anterior abdominal wall). Emergency debridement of all necrotic tissue is mandatory, often requiring orchiectomy (testes are usually spared — they have independent blood supply from the testicular arteries)."}
]

QUESTIONS2["Lipoma Excision"] = [
    {"question": "Lipomas arise from which embryologic tissue, and what genetic alteration is most commonly associated?",
     "answer": "Mesodermal adipose tissue. The most common genetic alteration is rearrangement of the HMGA2 gene on chromosome 12q14-15 (found in ~65% of solitary lipomas). Lipomas are the most common soft tissue tumor. Malignant transformation to liposarcoma is extremely rare in superficial lipomas."},
    {"question": "What is the surgical plane for lipoma excision?",
     "answer": "Lipomas have a thin fibrous capsule that separates them from surrounding tissue. Dissection in the plane between the capsule and surrounding fat allows en bloc removal. Staying on the capsule prevents bleeding from surrounding tissue perforators. Squeezing the lipoma through a small incision (enucleation technique) works for small (<5cm) superficial lipomas."},
    {"question": "What is the blood supply to a lipoma, and why do large/deep lipomas bleed more?",
     "answer": "Lipomas receive blood supply from perforating vessels that enter the capsule. Small superficial lipomas have minimal vascularity. Large or deep (subfascial) lipomas develop more robust blood supply from muscular perforators and can bleed significantly. Intramuscular lipomas (within the muscle belly) are particularly vascular and may require deeper dissection with hemostasis."},
    {"question": "When should you be concerned that a 'lipoma' is actually a liposarcoma?",
     "answer": "Red flags: >5cm, deep to fascia (subfascial/intramuscular), rapidly growing, painful, heterogeneous on imaging (non-uniform fat signal on MRI). Any deep soft tissue mass >5cm should have MRI before excision and may need core needle biopsy. Well-differentiated liposarcoma (atypical lipomatous tumor) can be indistinguishable from lipoma on physical exam."},
    {"question": "What is the recurrence rate after lipoma excision?",
     "answer": "1-3% for complete excision (including capsule). Higher for: intramuscular lipomas (incomplete excision due to infiltrative borders — 20%), multiple lipomatosis (familial, Dercum's disease, Madelung disease), and angiolipomas. Recurrence usually represents incomplete capsule removal rather than true recurrence."}
]

# ============================================================
# ADDITIONAL COLORECTAL
# ============================================================

QUESTIONS2["Excisional Hemorrhoidectomy"] = [
    {"question": "The hemorrhoidal cushions develop from what embryologic tissue, and what is their normal physiologic function?",
     "answer": "Submucosal vascular cushions (sinusoidal arteriovenous communications) from splanchnic mesoderm, located in the left lateral, right anterolateral, and right posterolateral anal canal. Normal function: contribute to fine continence (15-20% of resting anal pressure) and protect the anal sphincter during defecation by cushioning the canal."},
    {"question": "What is the anatomic landmark that distinguishes internal from external hemorrhoids?",
     "answer": "The dentate (pectinate) line — the embryologic junction of hindgut endoderm (columnar epithelium above, visceral innervation = painless) and proctodeal ectoderm (squamous epithelium below, somatic innervation = painful). Internal hemorrhoids: above the dentate (painless bleeding). External hemorrhoids: below the dentate (painful thrombosis)."},
    {"question": "What is the blood supply to the hemorrhoidal plexus?",
     "answer": "Superior rectal artery (from IMA — supplies internal hemorrhoids above the dentate), middle rectal artery (from internal iliac), and inferior rectal artery (from internal pudendal — supplies external hemorrhoids below the dentate). The hemorrhoidal plexus is arteriovenous — this is why hemorrhoidal bleeding is bright red (arterial), not dark venous blood."},
    {"question": "What is the most feared complication of excisional hemorrhoidectomy?",
     "answer": "Anal stenosis — from excessive tissue excision without preserving adequate mucosal bridges between excision sites. The Ferguson (closed) technique closes the wound primarily; the Milligan-Morgan (open) technique leaves wounds open. Both require preserving mucosal bridges between the three hemorrhoidal columns. Maximum 3 columns excised; always leave adequate bridges."},
    {"question": "What is the Goligher classification for internal hemorrhoids, and which grades require surgery?",
     "answer": "Grade I: bleed but don't prolapse. Grade II: prolapse with straining, spontaneously reduce. Grade III: prolapse, require manual reduction. Grade IV: irreducible prolapse. Grades I-II: conservative (fiber, rubber band ligation). Grade III: RBL or surgery. Grade IV: surgical excision (Ferguson, Milligan-Morgan, or stapled hemorrhoidopexy). Thrombosed external hemorrhoids with acute pain benefit from excision within 72 hours."}
]

QUESTIONS2["Seton Placement for Anal Fistula"] = [
    {"question": "Anal fistulas most commonly arise from infection of which embryologic glandular structure?",
     "answer": "The anal glands (of Hermann and Desfosses) — intersphincteric glands at the level of the dentate line that drain into the anal crypts. Cryptoglandular infection is the etiology in 90% of fistulas. The glands originate from endodermal budding at the dentate line during fetal development."},
    {"question": "What is Goodsall's rule for predicting the internal opening of an anal fistula?",
     "answer": "Fistulas with external openings anterior to the transverse anal line track radially to the nearest crypt. Fistulas with external openings posterior to this line track curvilinearly to the posterior midline crypt. Exception: anterior openings >3cm from the anal verge may also track to the posterior midline. Goodsall's rule is correct approximately 80% of the time."},
    {"question": "What is the blood supply to the anal sphincter complex that a seton preserves?",
     "answer": "The internal anal sphincter (smooth muscle, from circular muscle layer of the rectum) receives blood from the superior and middle rectal arteries. The external anal sphincter (skeletal muscle) is supplied by the inferior rectal artery (from internal pudendal). A seton slowly cuts through the sphincter while stimulating fibrosis BEHIND it, preventing sudden loss of sphincter integrity."},
    {"question": "What is the difference between a cutting seton and a draining seton?",
     "answer": "Cutting seton: a tight suture (or elastic band) that gradually cuts through the sphincter muscle by pressure necrosis while fibrosis seals the tract behind it, preserving continence (tightened sequentially over weeks). Draining seton: a loose loop (vessel loop) left in the tract long-term to prevent abscess formation without cutting through muscle. Used for complex fistulas or Crohn's disease where continence is at high risk."},
    {"question": "What classification system describes anal fistula types, and which type carries the highest incontinence risk with fistulotomy?",
     "answer": "Parks classification: 1) Intersphincteric (45% — between internal and external sphincter), 2) Trans-sphincteric (30% — through both sphincters), 3) Suprasphincteric (20% — above external sphincter), 4) Extrasphincteric (5% — outside sphincter complex). High trans-sphincteric and suprasphincteric carry the highest incontinence risk — these are the primary indications for seton placement rather than fistulotomy."}
]

QUESTIONS2["Lateral Internal Sphincterotomy"] = [
    {"question": "The internal anal sphincter is a continuation of which intestinal muscle layer, and from which embryologic germ layer?",
     "answer": "A thickened continuation of the circular smooth muscle layer of the rectum, derived from splanchnic mesoderm. It provides 70-80% of resting anal tone. The external sphincter (striated muscle from somatic mesoderm) provides voluntary squeeze. The internal sphincter's high resting tone is what causes chronic anal fissures."},
    {"question": "Where is the classic location of a chronic anal fissure, and what anatomic feature explains this?",
     "answer": "Posterior midline (90% of fissures, 80% in women). The posterior midline has the poorest blood supply — the inferior rectal arteries enter the sphincter laterally, and the posterior commissure is a relative watershed zone. This ischemia impairs healing, perpetuating the chronic fissure cycle: pain → sphincter spasm → ischemia → non-healing."},
    {"question": "What is the blood supply to the anoderm at the fissure site?",
     "answer": "The inferior rectal artery branches (from internal pudendal) enter the external sphincter and internal sphincter laterally, with terminal branches reaching the anoderm. Doppler studies show the posterior midline anoderm has the lowest blood flow. Lateral internal sphincterotomy increases blood flow to the posterior midline by reducing sphincter spasm, enabling fissure healing."},
    {"question": "What is the technique of lateral internal sphincterotomy, and how far do you divide the muscle?",
     "answer": "A small incision is made at the lateral intersphincteric groove. The internal sphincter is divided from its distal edge to the level of the dentate line (fissure apex) — approximately 50-75% of its length. NEVER divide above the dentate line. The external sphincter is NOT divided. Can be performed open (direct visualization) or closed (using a blade under the mucosa)."},
    {"question": "What is the long-term incontinence risk after lateral internal sphincterotomy?",
     "answer": "Minor incontinence (flatus, seepage): 8-30% (varies by study). Major incontinence (solid stool): <1%. Healing rate: 95-98%. Risk factors for incontinence: female sex, prior vaginal delivery, prior anal surgery, and excessive sphincter division. This is why conservative therapy (nitroglycerin 0.4% ointment, diltiazem 2%, botulinum toxin injection) should be tried first for 6-8 weeks before surgery."}
]

QUESTIONS2["Fistulotomy"] = [
    {"question": "Cryptoglandular fistulas develop from anal glands that penetrate into which sphincter space?",
     "answer": "The intersphincteric space — anal glands (of Hermann and Desfosses) originate at the dentate line and penetrate through the internal sphincter into the intersphincteric groove. Infection tracks through this space and can then traverse the external sphincter (trans-sphincteric) or exit various paths (Parks classification)."},
    {"question": "What anatomic assessment must be performed before fistulotomy to determine if it is safe?",
     "answer": "Assessment of how much sphincter muscle the fistula traverses. Exam under anesthesia with probe passage and/or MRI/endoanal ultrasound. Fistulotomy is safe for: intersphincteric fistulas and low trans-sphincteric fistulas (involving <30% of external sphincter). High trans-sphincteric (>30%), suprasphincteric, and extrasphincteric require sphincter-sparing approaches (seton, LIFT, advancement flap)."},
    {"question": "What is the blood supply to the anoderm and perianal skin that must be considered during fistulotomy?",
     "answer": "Inferior rectal artery (from internal pudendal) supplies the anal canal and perianal skin. The external rectal plexus drains below the dentate line. During fistulotomy, laying open the tract divides a portion of the internal sphincter — the wound heals by secondary intention from the base up, requiring adequate blood supply at the wound edges."},
    {"question": "What is the recurrence rate after fistulotomy, and what causes failure?",
     "answer": "Recurrence: 2-8%. Causes: unidentified internal opening (most common), unrecognized secondary tracts or horseshoe extension, Crohn's disease (always biopsy fistula tissue for granulomas), and inadequate drainage of the primary tract. Hydrogen peroxide injection through the external opening during EUA can help identify internal openings."},
    {"question": "In Crohn's disease, why is fistulotomy generally contraindicated?",
     "answer": "Crohn's impairs wound healing, and the sphincter muscle may already be compromised by chronic inflammation. Fistulotomy in Crohn's patients has unacceptably high non-healing and incontinence rates. Management: draining seton (long-term), anti-TNF therapy (infliximab — ACCENT II trial), and sphincter-sparing approaches. Proctectomy may ultimately be needed for refractory perineal Crohn's disease."}
]

QUESTIONS2["Fistulectomy"] = [
    {"question": "How does fistulectomy differ from fistulotomy anatomically?",
     "answer": "Fistulotomy: laying open the tract by cutting the tissue above it (unroofing). Fistulectomy: complete excision (coring out) of the entire fistula tract including the fibrous wall. Fistulectomy creates a larger wound, takes longer to heal, and removes more sphincter tissue — but provides the entire tract for histologic analysis (important if malignancy or Crohn's suspected)."},
    {"question": "What tissue planes are involved in coring out a fistula tract?",
     "answer": "The tract is surrounded by a fibrous capsule (chronic granulation tissue) embedded in the intersphincteric, trans-sphincteric, or perianal adipose tissue. Dissection follows the capsule plane — similar to excising a tube from surrounding tissue. The internal opening must be identified and excised with a small cuff of rectal mucosa."},
    {"question": "What is the blood supply concern with fistulectomy versus fistulotomy?",
     "answer": "Fistulectomy creates a larger tissue defect and divides more of the sphincter complex blood supply (from inferior rectal artery branches). The resulting wound heals more slowly by secondary intention. Fistulotomy leaves the tract walls in situ and creates a shallower wound that epithelializes faster."},
    {"question": "When is fistulectomy preferred over fistulotomy?",
     "answer": "When histologic examination of the entire tract is needed (suspected Crohn's, TB, malignancy arising in a chronic fistula). For simple intersphincteric fistulas where the tract is short and the tissue loss is minimal. For recurrent fistulas where prior fistulotomy has failed and the tract architecture needs to be completely assessed."},
    {"question": "What is the healing time difference between fistulectomy and fistulotomy?",
     "answer": "Fistulectomy: 8-12 weeks (larger wound). Fistulotomy: 4-8 weeks. Multiple RCTs show fistulotomy has faster healing, less pain, equivalent recurrence rates, and less sphincter damage. For this reason, fistulotomy is preferred for most simple fistulas, and fistulectomy is reserved for when tissue diagnosis is needed."}
]

QUESTIONS2["Pilonidal Cyst Excision"] = [
    {"question": "Pilonidal disease is NOT a congenital condition despite historical teaching. What is the current understanding of its pathogenesis?",
     "answer": "Acquired disease: hair penetrates the skin of the natal cleft through follicular occlusion → creates a sinus tract → foreign body reaction to embedded hair → abscess formation. Evidence: it occurs in non-hair-bearing areas (interdigital in barbers), is rare before puberty, and is more common in hirsute individuals. The term 'pilonidal' (Latin: 'nest of hair') describes the finding, not the embryology."},
    {"question": "What is the anatomy of the natal cleft that predisposes to pilonidal disease?",
     "answer": "The deep, narrow, moist intergluteal cleft creates an anaerobic, friction-prone environment. The gluteal skin has dense hair follicles, and the depth of the cleft traps loose hairs. The midline raphe has relatively poor blood supply compared to the lateral buttock skin. This anatomy explains why off-midline closure (Karydakis flap, Limberg flap) has lower recurrence than midline closure."},
    {"question": "What is the blood supply to the gluteal skin and flap options for pilonidal closure?",
     "answer": "Superior and inferior gluteal arteries (from internal iliac) supply the gluteal musculature, with perforators to the overlying skin. Flap options: Karydakis flap (asymmetric off-midline closure — eccentric elliptical excision with advancement), Limberg (rhomboid) flap (rotation flap from lateral buttock), Bascom cleft lift (flattens the natal cleft). All move the suture line off the midline."},
    {"question": "What is the recurrence rate with midline versus off-midline closure?",
     "answer": "Midline primary closure: 20-30% recurrence. Open healing (secondary intention): 1-5% recurrence but takes 6-12 weeks to heal. Off-midline flap (Karydakis/Limberg): 3-5% recurrence with primary healing in 2-3 weeks. Systematic reviews confirm off-midline closure is superior. The key principle: remove the midline wound from the depth of the natal cleft."},
    {"question": "What non-surgical treatments exist for pilonidal disease?",
     "answer": "For acute abscess: incision and drainage (lateral to midline). Chronic/recurrent: phenol injection (chemical ablation — 60-80% success), laser hair removal (reduces recurrence by 60-70% as adjunct), endoscopic pilonidal sinus treatment (EPSiT — video-assisted debridement through the pit), and fibrin glue obliteration. Conservative approaches are gaining traction for mild/moderate disease."}
]

QUESTIONS2["Transanal Excision of Rectal Mass"] = [
    {"question": "The rectum has no serosal covering below the peritoneal reflection. At what level does the peritoneal reflection occur?",
     "answer": "Anterior: 7-9cm from the anal verge in men, 5-7cm in women (lower in women because the rectouterine pouch/pouch of Douglas dips lower). Posterior/lateral: the rectum is extraperitoneal below 12-15cm. Transanal excision of lesions above the anterior peritoneal reflection risks entering the peritoneal cavity."},
    {"question": "What are the layers of the rectal wall that a full-thickness transanal excision should include?",
     "answer": "Mucosa, submucosa, muscularis propria (inner circular + outer longitudinal), and perirectal fat (if full-thickness). For T1 rectal cancers meeting specific criteria, full-thickness excision with ≥1cm margins and clear deep margin is the standard for transanal excision."},
    {"question": "What is the blood supply to the distal rectum that is relevant during transanal excision?",
     "answer": "Middle rectal arteries (from internal iliac — variable, present in ~50%) and inferior rectal arteries (from internal pudendal). The superior rectal artery (terminal IMA branch) supplies the upper rectum. During transanal excision, the submucosal plexus bleeds — electrocautery and suture ligation control this. Full-thickness excision may encounter mesorectal vessels."},
    {"question": "What are the criteria for transanal local excision of a rectal cancer (without radical resection)?",
     "answer": "T1 cancer only (limited to submucosa). Additional favorable features: well-differentiated, no lymphovascular invasion, <3cm diameter, <30% of rectal circumference, no perineural invasion, negative margins (≥1cm). If ANY unfavorable feature is present, radical resection (LAR or APR) is recommended due to 10-20% lymph node metastasis risk for unfavorable T1 lesions."},
    {"question": "What is TAMIS and how does it differ from traditional transanal excision?",
     "answer": "Transanal Minimally Invasive Surgery — uses a single-port platform (GelPOINT) inserted into the anal canal with laparoscopic instruments and CO2 insufflation. Advantages over traditional transanal excision: better visualization of proximal rectum (up to 15cm), more precise dissection, ability to perform full-thickness excision with better margin assessment. TEM (transanal endoscopic microsurgery) is the predecessor using a specialized rigid platform."}
]

# ============================================================
# HERNIA (ROBOTIC/OPEN/SPECIAL)
# ============================================================

QUESTIONS2["Robotic Ventral Hernia Repair (rTAR)"] = [
    {"question": "The transversus abdominis muscle develops from which embryologic myotome, and what is the transversus abdominis release (TAR)?",
     "answer": "The lateral plate mesoderm (body wall musculature). TAR involves dividing the transversus abdominis muscle lateral to the rectus sheath, entering the preperitoneal space (space of Retzius anteriorly, Bogros space laterally). This releases the posterior rectus sheath medially, allowing tension-free midline fascial closure and wide mesh overlap in the retromuscular (sublay) position."},
    {"question": "What is the anatomy of the retromuscular (Rives-Stoppa) space?",
     "answer": "The space between the rectus abdominis muscle (anterior) and the posterior rectus sheath (posterior). Above the arcuate line, the posterior sheath is formed by the aponeuroses of the internal oblique and transversus abdominis. Below the arcuate line, there IS no posterior sheath — all aponeuroses pass anterior, leaving only transversalis fascia and peritoneum posteriorly."},
    {"question": "What nerves are at risk during TAR, and what are the consequences of injury?",
     "answer": "Intercostal nerves (T7-T12) and the subcostal nerve (T12) — they run between the internal oblique and transversus abdominis (where the TAR division occurs). Injury causes abdominal wall denervation: bulging (pseudo-hernia) without a fascial defect. The nerves must be identified and preserved during lateral dissection of the transversus abdominis."},
    {"question": "What type of mesh and position is used in robotic TAR, and why is this position biomechanically superior?",
     "answer": "Wide-pore polypropylene mesh in the retromuscular (sublay) position. This is superior because: 1) Pascal's law — intra-abdominal pressure pushes the mesh against the abdominal wall (self-reinforcing), 2) The mesh is between two vascularized tissue layers promoting incorporation, 3) No intraperitoneal mesh (avoids adhesions and bowel complications). Mesh overlap: ≥5cm beyond the fascial defect in all directions."},
    {"question": "What is the recurrence rate of rTAR compared to other ventral hernia repair techniques?",
     "answer": "rTAR recurrence: 2-5% at 2-3 years (early data, promising). Open Rives-Stoppa: 5-10%. Laparoscopic IPOM (intraperitoneal onlay mesh): 10-15%. Open onlay: 15-25%. Primary suture repair: 30-50%. The retromuscular position with TAR component separation has the lowest recurrence rate for complex ventral hernias, and the robotic approach reduces wound complications compared to open."}
]

QUESTIONS2["Robotic eTEP Inguinal Hernia Repair"] = [
    {"question": "The inguinal canal develops from the processus vaginalis. What is it, and what pathology results from its failure to close?",
     "answer": "The processus vaginalis is a peritoneal outpouching that follows the testis through the inguinal canal during descent (weeks 28-32). Failure to close: patent processus vaginalis → indirect inguinal hernia (peritoneal sac through the internal ring along the spermatic cord). Complete patency: communicating hydrocele. Partial: encysted hydrocele of the cord."},
    {"question": "What is the eTEP (enhanced totally extraperitoneal) approach, and how does it differ from standard TEP?",
     "answer": "eTEP uses a crossover technique: ports are placed on the contralateral side, and a retromuscular (retrorectus) plane is developed crossing the midline to reach the affected groin. This provides a larger working space than standard TEP (which enters the preperitoneal space directly), allowing better visualization and mesh deployment. It is also ideal for bilateral inguinal hernias in one setting."},
    {"question": "What is the 'triangle of doom' and 'triangle of pain' in the myopectineal orifice?",
     "answer": "Triangle of doom: bounded by the vas deferens (medially) and gonadal vessels (laterally) — contains the external iliac artery and vein. Tacking/stapling here causes vascular injury. Triangle of pain: lateral to the gonadal vessels, bounded by the iliopubic tract — contains the lateral femoral cutaneous nerve, femoral branch of genitofemoral nerve, and femoral nerve. Tacking here causes chronic neuralgia."},
    {"question": "What is the blood supply to the spermatic cord structures that must be preserved?",
     "answer": "Three arteries: 1) Testicular artery (from aorta — in the cord), 2) Artery of the vas (from inferior vesical artery), 3) Cremasteric artery (from inferior epigastric). The pampiniform venous plexus provides venous drainage. During hernia repair, at least one arterial supply must be preserved or the testis may atrophy (ischemic orchitis: 0.5-1% after inguinal hernia repair)."},
    {"question": "What mesh size is used in eTEP inguinal repair, and what is the critical overlap over the myopectineal orifice?",
     "answer": "Medium-weight polypropylene, minimum 10 x 15 cm (often 12 x 17 cm). Must cover the entire myopectineal orifice with ≥5cm overlap over the direct, indirect, and femoral spaces. The mesh is placed in the preperitoneal position and held by intra-abdominal pressure (no fixation needed in most cases — reducing chronic pain). The mesh must extend medially past the pubic symphysis."}
]

QUESTIONS2["Open Shouldice Repair"] = [
    {"question": "The transversalis fascia is the key structure repaired in the Shouldice technique. What embryologic layer does it represent?",
     "answer": "The transversalis fascia is the deep investing fascia of the transversus abdominis muscle — derived from the somatic mesoderm body wall. It forms the posterior wall of the inguinal canal. In direct hernias, the transversalis fascia has attenuated/failed in the Hesselbach triangle; the Shouldice repair reconstructs this layer with a multi-layer imbrication."},
    {"question": "What are the four layers of the Shouldice repair?",
     "answer": "After opening the transversalis fascia and exploring the preperitoneal space: Layer 1: medial flap of transversalis fascia sutured to the iliopubic tract (shelving edge of inguinal ligament). Layer 2: return stitch — lateral flap to conjoint tendon. Layer 3: internal oblique/conjoined tendon to inguinal ligament. Layer 4: return stitch. All with continuous non-absorbable monofilament (stainless steel wire at the original Shouldice Hospital)."},
    {"question": "What is the blood supply to the inguinal canal floor, and why does the Shouldice repair work?",
     "answer": "The transversalis fascia receives blood supply from the deep circumflex iliac artery, inferior epigastric artery, and cremasteric artery branches. The Shouldice works by imbrication (overlapping repair) of these fascial layers, creating a multi-layered reinforcement of the posterior wall. The continuous running suture distributes tension evenly. At the Shouldice Hospital, the recurrence rate is 0.5-1% (compared to 2-4% for Lichtenstein mesh repair in some series)."},
    {"question": "What is the main advantage and disadvantage of the Shouldice compared to mesh repair?",
     "answer": "Advantage: no mesh (no foreign body complications — chronic pain from mesh, mesh infection, mesh migration, orchitis). The Shouldice Hospital has lower chronic pain rates (1-2%) than mesh repair (5-10%). Disadvantage: the technique is difficult to reproduce outside the Shouldice Hospital — in general surgical practice, recurrence rates with Shouldice are higher (4-10%) versus Lichtenstein (1-2%)."},
    {"question": "For which patient populations is a pure tissue repair (Shouldice) preferred over mesh?",
     "answer": "Young active patients (<30), women (low recurrence risk, mesh complications disproportionately affect women), contaminated/infected fields (mesh contraindicated), strangulated hernias with bowel resection, and patients who refuse mesh. The European Hernia Society (EHS) guidelines recommend mesh for most adult male inguinal hernias but acknowledge tissue repair for selected patients."}
]

QUESTIONS2["Sports Hernia Repair (Athletic Pubalgia)"] = [
    {"question": "What is a 'sports hernia' — does it involve an actual fascial defect?",
     "answer": "No — athletic pubalgia is NOT a true hernia. It's a chronic musculotendinous injury involving the pubic symphysis region: rectus abdominis insertion, adductor longus origin, or the conjoint tendon attachment on the pubic tubercle. There is no fascial defect or peritoneal sac. The term 'sports hernia' is a misnomer that persists in common usage."},
    {"question": "What is the anatomy of the pubic symphysis region relevant to athletic pubalgia?",
     "answer": "The pubic symphysis is the central anchor point where opposing force vectors meet: the rectus abdominis/obliques pull superiorly, and the adductor longus/brevis pull inferiorly. The conjoint tendon, inguinal ligament, and transversalis fascia all attach here. Chronic shearing stress at these attachments causes micro-tears and chronic pain. The 'pubic plate' concept describes this shared tendinous insertion."},
    {"question": "What is the blood supply to the pubic region, and why does it heal poorly?",
     "answer": "The pubic symphysis and tendinous attachments are supplied by branches of the obturator artery, inferior epigastric artery, and medial femoral circumflex artery. The tendon-bone junction (enthesis) has relatively poor vascularity — similar to rotator cuff tendinopathy, this watershed zone heals slowly and is prone to chronic degeneration."},
    {"question": "What surgical approach is used for athletic pubalgia repair?",
     "answer": "Options: 1) Minimal repair (Muschaweck technique): reinforcement of the posterior inguinal wall with mesh and reinforcement of the conjoint tendon. 2) Laparoscopic/robotic preperitoneal mesh placement (TEP/TAPP). 3) Adductor tenotomy (if adductor longus is the primary pathology). Often combined: inguinal floor reinforcement + adductor longus release. Return to sport: 6-12 weeks."},
    {"question": "What is the non-operative success rate, and when should you operate?",
     "answer": "Conservative therapy (rest, physical therapy focusing on core/hip stabilization, anti-inflammatories) succeeds in 50-60% at 3-6 months. Surgery is indicated when 3-6 months of conservative management fails in a patient who needs to return to high-level athletics. Surgical success rate: 85-95% return to sport. MRI is important to rule out: osteitis pubis, femoral acetabular impingement, labral tear, and true inguinal hernia."}
]

QUESTIONS2["Parastomal Hernia Repair"] = [
    {"question": "What is the incidence of parastomal hernia after end colostomy creation, and what anatomic factor is most predictive?",
     "answer": "30-50% at 5 years (the most common stoma complication). Most predictive factor: stoma placement lateral to the rectus muscle (2-3x higher risk than through the rectus). Other factors: obesity, COPD, steroids, malnutrition, and large fascial defect at stoma creation."},
    {"question": "What is the anatomy of a parastomal hernia — what herniates and through what defect?",
     "answer": "Abdominal contents (omentum, small bowel, colon) herniate through the fascial defect around the stoma, alongside the bowel. The defect enlarges over time as the fascia stretches around the stoma conduit. The hernia sac follows the path of least resistance — usually lateral to the stoma where the lateral fascial support is weakest."},
    {"question": "What is the blood supply concern when repairing a parastomal hernia?",
     "answer": "The stoma's mesentery and its marginal artery must be preserved during repair — devascularization causes stoma necrosis or ischemia. During mesh placement, the mesh aperture around the stoma must be sized correctly: too tight compresses the mesentery (ischemia), too loose allows hernia recurrence."},
    {"question": "What are the surgical options for parastomal hernia repair?",
     "answer": "1) Local fascial repair (primary suture — recurrence 50-70%, not recommended). 2) Stoma relocation (moving to a new site — recurrence 30% at the new site). 3) Mesh repair: Sugarbaker (intraperitoneal mesh, bowel lateralized under mesh flap), Keyhole (mesh with aperture for bowel — high recurrence at keyhole), or modified Sugarbaker-Keyhole hybrid. 4) Retromuscular mesh (open or robotic — lowest recurrence 5-15%)."},
    {"question": "What does the PREVENT trial show about prophylactic mesh placement at the time of index stoma creation?",
     "answer": "The PREVENT trial (and STOMAMESH trial): prophylactic mesh (placed in the retromuscular or preperitoneal position) at the time of end colostomy creation reduces parastomal hernia rates from 40-50% to 10-15% at 2 years. The mesh does not increase surgical site infection or stoma complications. Prophylactic mesh is now recommended by the European Hernia Society for permanent end colostomies."}
]

QUESTIONS2["Open Hiatal Hernia Repair"] = [
    {"question": "The esophageal hiatus is formed by the right crus of the diaphragm in most people. What percentage have contributions from the left crus?",
     "answer": "15-20% have contributions from the left crus or have bilateral crural involvement. The right crus alone forms the hiatus in 80-85%. This is clinically relevant because the crural anatomy determines the repair strategy — asymmetric or weak crura require more extensive reconstruction."},
    {"question": "What is the anatomy of the phrenoesophageal ligament, and how does its failure contribute to hiatal hernia?",
     "answer": "The phrenoesophageal ligament (Laimer's membrane) is a fibroelastic membrane connecting the esophagus circumferentially to the diaphragmatic hiatus. It anchors the GEJ at the hiatus. Age-related degeneration, increased intra-abdominal pressure, and connective tissue weakness cause this ligament to attenuate, allowing the GEJ (Type I) or stomach (Type II-IV) to herniate."},
    {"question": "During open hiatal hernia repair, what is the blood supply to the vagus nerves, and why is their preservation important?",
     "answer": "The vagus nerves receive blood supply from the vasa nervorum (small arteries accompanying the nerve trunk from the esophageal arterial plexus). Injury to the vagus causes gastroparesis, dumping syndrome, and diarrhea. The anterior vagus (left, often a single trunk at the hiatus) is most at risk during anterior dissection. The posterior vagus runs on the posterior esophageal surface."},
    {"question": "When is open repair preferred over laparoscopic for hiatal hernias?",
     "answer": "Open approach preferred when: giant paraesophageal hernia with significant mediastinal adhesions/incarceration, concurrent procedure requiring laparotomy, hostile abdomen from prior surgery, and surgeon preference/experience. However, most evidence shows laparoscopic repair has equivalent outcomes with less morbidity — open approach is increasingly reserved for the most complex cases."},
    {"question": "What is the short esophagus, and how do you manage it during hiatal hernia repair?",
     "answer": "A foreshortened esophagus (from chronic inflammation/fibrosis, Barrett's, or previous surgery) that cannot be reduced to ≥3cm of intra-abdominal length without tension. True short esophagus occurs in 5-15% of giant hiatal hernias. Management: Collis gastroplasty — a longitudinal staple line along the lesser curve creates a neo-esophagus from the gastric cardia, adding 3-5cm of length. The fundoplication is then wrapped around the neo-esophagus."}
]

QUESTIONS2["Robotic Hiatal Hernia Repair"] = [
    {"question": "What is the embryologic origin of the diaphragmatic crura?",
     "answer": "The crura develop from the dorsal mesentery of the esophagus (mesoesophagus) — not from the septum transversum or pleuroperitoneal membranes. This unique origin explains why the crura are striated muscle (unlike the diaphragmatic dome which is mixed) and are innervated by the phrenic nerve separately from the costal diaphragm."},
    {"question": "What specific advantage does the robotic platform offer for hiatal hernia repair?",
     "answer": "Wristed instruments allow precise crural suturing in the deep, narrow space behind the esophagus (posterior cruroplasty). The 3D magnification enables identification and preservation of the vagus nerves and visualization of the short gastric vessels. The stable camera platform eliminates assistant-dependent visualization issues. These advantages are most evident in large paraesophageal hernia repairs."},
    {"question": "What is the blood supply to the crural muscle used for repair?",
     "answer": "The crura receive blood supply from the inferior phrenic arteries (from aorta) and musculophrenic arteries. The crural muscle is generally well-vascularized, supporting suture-based repair. However, attenuated crura in large chronic hernias may have poor tissue quality, necessitating mesh reinforcement."},
    {"question": "What is the recurrence rate after robotic hiatal hernia repair, and how does mesh affect it?",
     "answer": "Recurrence: 5-15% (radiographic) at 5 years, comparable to laparoscopic rates. Biologic mesh reinforcement over the crural repair may reduce recurrence (some studies show reduction from 22% to 9%), but evidence is conflicting. Synthetic mesh is controversial due to erosion risk into the esophagus. The crural repair itself (posterior cruroplasty with pledgets) is the most important factor."},
    {"question": "What is the 'short gastric vessels' assessment during robotic hiatal hernia repair?",
     "answer": "Division of the short gastric vessels (from the splenic artery, 2-6 vessels) is performed to fully mobilize the gastric fundus for a tension-free fundoplication wrap. Robotically, this is facilitated by the articulating energy device. Failure to divide the short gastrics creates a tight wrap → dysphagia. The fundus must reach the right crus without tension (the 'shoe-shine' test: the fundus should easily pass behind the esophagus and return)."}
]

print(f"Part 2 loaded: {len(QUESTIONS2)} procedures")
