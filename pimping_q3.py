#!/usr/bin/env python3
"""Pimping questions Part 3 - remaining procedures"""

Q3 = {}

Q3["EGD with Dilation"] = [
    {"question": "Esophageal atresia occurs in 1:3000 births. What is the most common type and its embryologic basis?",
     "answer": "Type C (85%): proximal atresia with distal TEF. Failure of the tracheoesophageal septum to completely separate foregut into trachea and esophagus during weeks 4-5. Associated with VACTERL in 25%."},
    {"question": "What are the three types of esophageal strictures and the appropriate dilator for each?",
     "answer": "Simple/short (peptic, Schatzki ring): TTS balloon. Complex/long (caustic, radiation, anastomotic): Savary bougie for tactile feedback. Malignant: stenting preferred. Rule of 3: don't exceed 3 consecutive French sizes per session."},
    {"question": "What is the blood supply to the esophagus at different levels?",
     "answer": "Cervical: inferior thyroid artery. Thoracic: direct aortic branches and bronchial arteries. Abdominal: left gastric and left inferior phrenic. Thoracic perforation is most dangerous — no serosa, segmental blood supply, rapid mediastinitis."},
    {"question": "What is the perforation rate of esophageal dilation?",
     "answer": "Bougie: 0.1-0.4%. Balloon: 0.1-0.3%. Malignant strictures: up to 10%. Signs: chest pain, subcutaneous emphysema, Hamman's sign. CT with oral water-soluble contrast is diagnostic."},
    {"question": "What is a Schatzki ring, and at what diameter does it cause dysphagia?",
     "answer": "Thin mucosal ring at the squamocolumnar junction (GEJ), containing only mucosa and submucosa. Dysphagia at <13mm. Treatment: single dilation to >16mm. Always biopsy for eosinophilic esophagitis (10-15% of food impactions)."}
]

Q3["EGD with Biopsy"] = [
    {"question": "Barrett's esophagus represents intestinal metaplasia. What embryologic process does this recapitulate?",
     "answer": "The distal esophagus is initially columnar (foregut endoderm) before being replaced by squamous epithelium via cranial-to-caudal re-epithelialization. Barrett's reverts to embryonic columnar state — specialized intestinal metaplasia with goblet cells driven by acid/bile reflux."},
    {"question": "What landmarks confirm you've entered the stomach during EGD?",
     "answer": "Z-line (squamocolumnar junction), rugal folds, incisura angularis (lesser curve), pylorus, and retroflexion showing the cardia/fundus (J-maneuver). Barrett's is diagnosed when the Z-line displaces proximal to the GEJ."},
    {"question": "What is the Seattle biopsy protocol for Barrett's surveillance?",
     "answer": "Four-quadrant biopsies every 1-2cm throughout the Barrett's segment PLUS targeted biopsies of visible lesions. For confirmed dysplasia: every 1cm. Visible lesions should undergo EMR — biopsy alone underestimates dysplasia grade in 40%."},
    {"question": "What causes stress ulcers at the mucosal blood supply level?",
     "answer": "Splanchnic vasoconstriction during critical illness redirects blood from the dense submucosal gastric plexus, causing mucosal ischemia. Combined with acid exposure (mucus-bicarbonate barrier failure), stress ulcers form. Both PPI and maintaining perfusion are key."},
    {"question": "How many biopsies should you take from a gastric ulcer margin, and why?",
     "answer": "Minimum 6-8 from the ulcer rim. Gastric ulcers have 5-10% malignancy rate. Single biopsies have 70% sensitivity; 7+ achieve >98%. All gastric ulcers need repeat EGD at 8-12 weeks — a non-healing ulcer is cancer until proven otherwise."}
]

Q3["Colonoscopy with Polypectomy"] = [
    {"question": "What gene mutation initiates the adenoma-carcinoma sequence?",
     "answer": "APC gene on chromosome 5q21 (tumor suppressor in Wnt pathway). Vogelstein sequence: normal  ->  APC  ->  KRAS  ->  SMAD4/DCC  ->  TP53  ->  carcinoma. Takes 10-15 years, basis for 10-year screening intervals."},
    {"question": "What determines whether a sessile polyp can be safely removed endoscopically?",
     "answer": "The 'non-lifting sign' — submucosal injection should lift the polyp from the muscularis propria. Non-lifting indicates submucosal invasion (T1+ cancer) fixing it to muscle — needs surgical resection. Paris 0-Is and 0-IIa are generally amenable; 0-III suggests invasion."},
    {"question": "What are the highest-risk areas for perforation during colonoscopy?",
     "answer": "Cecum (thinnest wall, largest diameter — Laplace's law, supplied by ileocolic artery) and sigmoid (narrowest lumen, highest pressure, supplied by sigmoid arteries from IMA). Splenic flexure is third (fixed, angulated, thin marginal artery)."},
    {"question": "What is post-polypectomy syndrome versus perforation?",
     "answer": "Transmural burn without frank perforation: localized pain, fever, leukocytosis, but NO free air on CT. Fat stranding and wall thickening present. Treatment: conservative (NPO, antibiotics, observation). Free air = perforation = surgery."},
    {"question": "What are current US Multi-Society Task Force surveillance intervals after polypectomy?",
     "answer": "1-2 tubular adenomas <10mm: 7-10 years. 3-4 adenomas <10mm: 3-5 years. 5-10 adenomas: 3 years. Adenoma ≥10mm/villous/HGD: 3 years. Piecemeal EMR ≥20mm: 6 months. >10 adenomas: 1 year (consider genetic testing)."}
]

# ============================================================
# UROLOGIC
# ============================================================

Q3["Laparoscopic Nephrectomy"] = [
    {"question": "The kidney develops from which embryologic tissue, and what are the three successive renal systems?",
     "answer": "Intermediate mesoderm. Three systems: pronephros (degenerates, week 4), mesonephros (temporary kidney, weeks 4-8, duct becomes vas deferens in males), metanephros (permanent kidney from ureteric bud + metanephric blastema, week 5 onward)."},
    {"question": "What is the relationship of the renal hilum structures from anterior to posterior?",
     "answer": "Renal vein (most anterior), renal artery (middle), renal pelvis/ureter (most posterior). Mnemonic: VAP (vein, artery, pelvis) from front to back. The left renal vein is longer, crossing anterior to the aorta — it can be safely divided near the IVC during left nephrectomy because of collateral drainage (left adrenal, gonadal, and lumbar veins)."},
    {"question": "What are the named branches of the renal artery?",
     "answer": "The renal artery divides into anterior and posterior divisions at the hilum. Anterior: apical, upper, middle, and lower segmental arteries. Posterior: posterior segmental artery. These are END arteries — ligation causes segmental infarction. The avascular plane of Brodel (between anterior and posterior circulations) is the line of incision for nephrotomy."},
    {"question": "What is the most common intraoperative complication of laparoscopic nephrectomy?",
     "answer": "Vascular injury (1-3%) — most commonly to the renal vein or its tributaries (gonadal vein, adrenal vein, lumbar vein on the left). Right-sided nephrectomy is more challenging due to the short right renal vein draining directly into the IVC."},
    {"question": "When is radical nephrectomy versus partial nephrectomy appropriate for renal tumors?",
     "answer": "Partial (nephron-sparing): standard for T1a (≤4cm) tumors when technically feasible (equivalent oncologic outcomes, preserves renal function). Radical: T1b (4-7cm) if partial is not feasible, T2-T4, or venous invasion. The EORTC 30904 trial confirmed equivalent cancer-specific survival for partial vs radical in small renal masses."}
]

Q3["Open Nephrectomy"] = [
    {"question": "The ureteric bud arises from what structure, and what happens if it buds too cranially or caudally?",
     "answer": "The mesonephric (Wolffian) duct. Too cranial: ectopic ureter (may insert into bladder neck, urethra, or seminal vesicle — above the sphincter in males, below in females causing incontinence). Too caudal: may result in vesicoureteral reflux due to short intramural tunnel. The Weigert-Meyer rule describes duplex system relationships."},
    {"question": "What is Gerota's fascia, and what are its anatomic boundaries?",
     "answer": "Gerota's fascia (renal fascia) encloses the kidney, adrenal gland, and perirenal fat. It fuses medially with the great vessel adventitia, superiorly closes above the adrenal, and is open inferiorly (allowing perinephric fluid to track to the pelvis). During radical nephrectomy, the entire Gerota's fascia specimen is removed en bloc."},
    {"question": "What are the collateral venous drainage pathways for the left kidney if the renal vein is ligated?",
     "answer": "Left adrenal vein, left gonadal (testicular/ovarian) vein, and lumbar veins — all drain into the left renal vein. If the left renal vein is divided near the IVC (preserving these tributaries), blood drains retrogradely through these collaterals. This is why left renal vein ligation is tolerated, but right renal vein ligation is NOT (no collateral tributaries)."},
    {"question": "What is the most feared complication of open radical nephrectomy for a tumor with IVC thrombus?",
     "answer": "Tumor embolism to the pulmonary arteries during surgical manipulation — can cause acute pulmonary embolism and cardiovascular collapse. Also: massive hemorrhage from IVC (especially with suprahepatic or intracardiac thrombus extension requiring cardiopulmonary bypass). Preoperative imaging (MRI/CT) must define the cranial extent of the thrombus: Level I (renal vein), II (infrathepatic IVC), III (intrahepatic), IV (supradiaphragmatic/intracardiac)."},
    {"question": "What is the role of cytoreductive nephrectomy in metastatic renal cell carcinoma today?",
     "answer": "Historically beneficial (SWOG 8949): cytoreductive nephrectomy + interferon improved survival versus interferon alone. However, the CARMENA trial (2018): in the era of targeted therapy (sunitinib), cytoreductive nephrectomy did NOT improve OS versus sunitinib alone for intermediate/poor-risk metastatic RCC. Now reserved for good-risk patients with resectable primary and limited metastatic burden."}
]

Q3["Radical Cystectomy"] = [
    {"question": "The bladder develops from which embryologic structure?",
     "answer": "The urogenital sinus (ventral portion of the cloaca, separated by the urorectal septum). The trigone has a mesodermal origin (from mesonephric duct incorporation). The urachus (allantois remnant) connects the bladder dome to the umbilicus and normally obliterates as the median umbilical ligament."},
    {"question": "What are the anatomic boundaries of radical cystectomy in males versus females?",
     "answer": "Males: bladder, prostate, seminal vesicles, distal ureters, and pelvic lymph nodes en bloc. Females: bladder, uterus, cervix, anterior vaginal wall, ovaries/fallopian tubes, distal ureters, and pelvic lymph nodes. The dissection plane in males must preserve the neurovascular bundles lateral to the prostate if nerve-sparing is attempted."},
    {"question": "What is the blood supply to the bladder?",
     "answer": "Superior vesical arteries (from patent proximal umbilical artery, branch of internal iliac), inferior vesical arteries (from internal iliac — in males), and vaginal arteries (in females). Venous drainage: vesical venous plexus  ->  internal iliac veins. The dorsal venous complex of the penis (Santorini's plexus) overlies the prostatic apex — controlling this prevents massive blood loss."},
    {"question": "What is the standard lymph node dissection template, and what is the minimum node count?",
     "answer": "Standard template: external iliac, internal iliac, and obturator nodes bilaterally. Extended: adds common iliac and presacral nodes. Minimum 10-16 nodes for adequate staging (LN density is a better prognostic marker). Higher node counts correlate with improved survival — the extended template is increasingly recommended for muscle-invasive disease."},
    {"question": "What does the neoadjuvant chemotherapy evidence show for muscle-invasive bladder cancer?",
     "answer": "SWOG 8710/INT-0080: neoadjuvant MVAC (methotrexate, vinblastine, doxorubicin, cisplatin) improved median OS from 46 to 77 months versus cystectomy alone. Neoadjuvant cisplatin-based chemotherapy provides a 5% absolute survival benefit. Dose-dense MVAC or gemcitabine/cisplatin are the current standards. Neoadjuvant therapy is underutilized (only 20-30% of eligible patients receive it)."}
]

Q3["Orthotopic Neobladder"] = [
    {"question": "The ileum used for neobladder construction derives from midgut. What property of ileum makes it suitable for a urinary reservoir?",
     "answer": "Ileum has a compliant, distensible wall and low-pressure peristalsis that can be detubularized to create a spherical reservoir. Detubularization disrupts coordinated peristalsis, reducing pressure spikes. Laplace's law: a sphere has the lowest wall tension for a given volume, maximizing capacity while minimizing pressure."},
    {"question": "What is the Studer neobladder configuration?",
     "answer": "40-60cm of distal ileum detubularized and folded into a U-shape, with the proximal 15cm left as an isoperistaltic afferent chimney (not detubularized) that prevents reflux by peristaltic pumping of urine from the ureters into the reservoir. The reservoir is anastomosed to the urethra at the bladder neck."},
    {"question": "What are the metabolic complications of ileal neobladder?",
     "answer": "Hyperchloremic metabolic acidosis (ileum reabsorbs chloride and secretes bicarbonate), B12 deficiency (resection of terminal ileum), bile salt malabsorption (diarrhea), mucus production (requires irrigation), and ammonium reabsorption (can worsen hepatic encephalopathy in cirrhotic patients — neobladder is contraindicated in liver disease)."},
    {"question": "What is the blood supply to the ileal neobladder segment?",
     "answer": "SMA via ileal branches and the marginal arcade. The segment must be selected with an adequate mesenteric pedicle that reaches the pelvis without tension. The mesentery is incised in a 'V' pattern to allow the segment to fold and reach the urethra. Mesenteric tension causes ischemia and neobladder necrosis."},
    {"question": "What is the continence rate and quality of life after orthotopic neobladder?",
     "answer": "Daytime continence: 85-95%. Nighttime continence: 65-80% (lower because of absent guarding reflex during sleep). Patients must learn to void by Valsalva maneuver (no detrusor function). Self-catheterization may be needed in 10-20%. Quality of life is generally superior to ileal conduit in motivated, cognitively intact patients."}
]

Q3["Ureteral Reimplantation"] = [
    {"question": "The ureter develops from the ureteric bud. What is the embryologic basis of vesicoureteral reflux?",
     "answer": "The ureteric bud position on the mesonephric duct determines the length of the intramural tunnel. A laterally ectopic ureteral orifice (cranial budding) has a short tunnel and insufficient submucosal backing  ->  reflux. Normal ratio: intramural tunnel length to ureteral diameter should be 5:1."},
    {"question": "What are the three anatomic narrowings of the ureter where stones commonly impact?",
     "answer": "1) Ureteropelvic junction (UPJ), 2) Crossing of the iliac vessels at the pelvic brim, 3) Ureterovesical junction (UVJ — narrowest point). These correspond to sites where the ureter changes direction or is compressed by adjacent structures."},
    {"question": "What are the three arterial blood supply zones of the ureter?",
     "answer": "Upper ureter: renal artery branches. Middle ureter: gonadal artery, aortic branches, common iliac branches. Lower ureter: superior vesical, uterine, and inferior vesical arteries (from internal iliac). The blood supply runs in the adventitia — excessive skeletonization devascularizes the ureter. Rule: keep the tissue attached medially above the iliac crossing and laterally below it."},
    {"question": "What are the techniques for ureteral reimplantation and which is most commonly used?",
     "answer": "Extravesical (Lich-Gregoir): detrusor incision with ureteral advancement creating a submucosal tunnel — most common, avoids opening the bladder. Intravesical (Cohen cross-trigonal): ureteral advancement through a submucosal tunnel across the trigone — standard in pediatric VUR. Politano-Leadbetter: combined intravesical/extravesical with a new hiatus. All aim for a 5:1 tunnel-to-diameter ratio."},
    {"question": "What is the success rate of ureteral reimplantation for vesicoureteral reflux?",
     "answer": "95-98% for primary VUR (Grade I-IV). Lower for Grade V (80-85%) and secondary/complex reflux. Failure presents as persistent reflux or ureteral obstruction (from stricture or kinking). Postoperative VCUG at 3-6 months confirms resolution. Alternative: endoscopic injection (Deflux — dextranomer/hyaluronic acid) with 70-85% success rate as a less invasive option."}
]

Q3["Psoas Hitch"] = [
    {"question": "The psoas muscle develops from what embryologic tissue?",
     "answer": "Paraxial mesoderm (somite-derived myotome — lumbar myotomes L1-L4). The psoas major flexes the hip and is innervated by the lumbar plexus branches. Its tendon inserts on the lesser trochanter of the femur."},
    {"question": "What is the psoas hitch technique, and how much ureteral length does it bridge?",
     "answer": "The bladder is mobilized, opened, and the contralateral superior vesical pedicle is divided to gain mobility. The bladder is then 'hitched' (sutured) to the psoas tendon with non-absorbable sutures, elevating it toward the shortened ureter. It bridges 4-6cm of ureteral defect. Combined with a Boari flap, it can bridge up to 10-12cm."},
    {"question": "What is the blood supply to the mobilized bladder in a psoas hitch?",
     "answer": "The ipsilateral superior and inferior vesical arteries maintain blood supply. The contralateral superior vesical pedicle may be divided to gain mobility (the contralateral inferior vesical preserves the opposite bladder wall). The bladder has a rich anastomotic blood supply from bilateral pedicles, tolerating unilateral pedicle division."},
    {"question": "What nerve is at risk when suturing to the psoas tendon?",
     "answer": "The genitofemoral nerve (L1-L2) runs on the anterior surface of the psoas muscle. It can be compressed or entrapped by the hitch sutures, causing groin pain and anterior thigh numbness. Sutures should be placed in the psoas tendon (not muscle belly) to minimize nerve injury."},
    {"question": "When is psoas hitch indicated versus other ureteral reconstruction options?",
     "answer": "For distal ureteral defects (4-6cm) from injury, stricture, or oncologic resection. For longer defects: Boari flap (tubularized bladder flap adds 6-8cm), ileal ureter (>12cm defect), or autotransplant (reimplant kidney in the pelvis). Psoas hitch is the simplest and most reliable option for moderate distal defects."}
]

Q3["Ureteral Stent Placement"] = [
    {"question": "The ureter maintains peristalsis via intrinsic pacemaker cells. Where are these located?",
     "answer": "At the ureteropelvic junction (UPJ) — pacemaker cells in the renal pelvis initiate peristaltic waves that propagate distally. These cells are similar to the interstitial cells of Cajal in the GI tract. Ureteral stents bypass the need for peristalsis by providing a conduit for urine flow."},
    {"question": "What is the anatomy of the intramural ureter as it enters the bladder?",
     "answer": "The ureter enters the bladder posterolaterally, traveling 1.5-2cm through the bladder wall (intramural segment) at an oblique angle before opening at the ureteral orifice on the trigone. This tunnel creates a one-way valve — bladder contraction compresses the tunnel, preventing reflux. Stenting the ureter eliminates this valve mechanism."},
    {"question": "What is the blood supply to the distal ureter at the stent insertion site?",
     "answer": "Branches of the superior vesical, uterine (in females), and inferior vesical arteries, running in the ureteral adventitia. The intramural ureter receives blood from the detrusor muscle. Stent insertion through the ureteral orifice is atraumatic to the blood supply, but long-term stenting can cause ureteral wall ischemia and stricture."},
    {"question": "What are the complications of indwelling ureteral stents?",
     "answer": "Stent symptoms (60-80%): dysuria, urgency, frequency, flank pain with voiding (reflux up the stent), hematuria. Encrustation (30-50% after 3-6 months). Migration (5-10%). UTI (25%). Forgotten stent: can calcify, obstruct, require surgical removal. All stents should have a documented plan for removal — the 'forgotten stent' is a preventable disaster."},
    {"question": "What is the maximum duration a ureteral stent should remain in situ?",
     "answer": "Most stents should be exchanged or removed within 3-6 months (depending on material — some specialty stents last 12 months). Beyond this, encrustation risk increases significantly. In patients requiring long-term drainage (malignant obstruction, chronic stricture), metallic stents (Resonance, Memokath) or nephrostomy tubes may be more appropriate."}
]

Q3["Orchiectomy"] = [
    {"question": "The testis develops from the gonadal ridge. What embryologic structure guides its descent into the scrotum?",
     "answer": "The gubernaculum testis — a mesenchymal cord connecting the inferior pole of the testis to the labioscrotal swelling. Descent occurs in two phases: transabdominal (weeks 10-15, insulin-like factor 3-dependent) and inguinoscrotal (weeks 25-35, testosterone-dependent through the processus vaginalis). Failure: cryptorchidism (3% at birth, 1% at 1 year)."},
    {"question": "What is the anatomy of the spermatic cord and its contents?",
     "answer": "Three arteries: testicular (from aorta), artery of vas (from inferior vesical), cremasteric (from inferior epigastric). Three nerves: ilioinguinal, genital branch of genitofemoral, sympathetic fibers. Three fascial layers: external spermatic (from external oblique), cremasteric (from internal oblique), internal spermatic (from transversalis fascia). Plus: vas deferens, pampiniform plexus, lymphatics."},
    {"question": "For radical orchiectomy for testicular cancer, why is the inguinal approach mandatory rather than scrotal?",
     "answer": "The inguinal approach allows early control of the spermatic cord at the internal ring (vascular control before tumor manipulation), provides an en bloc specimen with the cord, and avoids violating scrotal lymphatic drainage (scrotum drains to inguinal nodes, not the retroperitoneal nodes that testicular lymphatics drain to). Scrotal violation changes the lymphatic drainage pattern and may require hemiscrotectomy."},
    {"question": "What is the blood supply to the testis that is divided during radical orchiectomy?",
     "answer": "The testicular artery (from aorta at L2 level) is the primary supply — divided at the internal ring with the cord. Collateral from the artery of the vas deferens and cremasteric artery normally exists but is insufficient alone. After orchiectomy, these are all removed with the specimen."},
    {"question": "What tumor markers should be drawn before orchiectomy, and what do they indicate?",
     "answer": "AFP (alpha-fetoprotein): elevated in yolk sac tumors and mixed GCT (NOT pure seminoma — if AFP is elevated, it's not pure seminoma regardless of histology). Beta-hCG: elevated in choriocarcinoma (markedly), seminoma (mildly in 10-15%), and mixed GCT. LDH: nonspecific, correlates with tumor burden. Draw BEFORE orchiectomy — post-orchiectomy half-life kinetics determine staging and response."}
]

Q3["Circumcision"] = [
    {"question": "The prepuce (foreskin) develops from what embryologic structure?",
     "answer": "A fold of ectoderm and mesoderm that grows over the glans penis starting at week 8, completing coverage by week 16. The inner preputial epithelium is initially fused to the glans (physiologic phimosis in neonates) and gradually separates by age 3-5 via desquamation and erections."},
    {"question": "What is the anatomy of the penile blood supply relevant to circumcision?",
     "answer": "Superficial: dorsal arteries of the penis (from internal pudendal — run deep to Buck's fascia, dorsolateral). Superficial dorsal vein (midline, above Buck's fascia — encountered during dorsal slit). Frenular artery (from deep dorsal or spongiosal artery — at the frenulum, most common site of post-circumcision bleeding)."},
    {"question": "What is the blood supply to the frenulum, and why is it the most common bleeding site?",
     "answer": "The frenular artery (branch of the corpus spongiosum artery) runs in the frenulum on the ventral surface. It is consistently present and can cause significant bleeding if not controlled with cautery or suture during circumcision. The frenulum is also the thinnest tissue of the prepuce."},
    {"question": "What is the most feared complication of neonatal circumcision?",
     "answer": "Glans injury/amputation (rare but devastating — 0.001%). More common complications: bleeding (1-5%), infection (1-3%), meatal stenosis (most common late complication — 5-10%, from ischemia of the exposed meatus after loss of protective foreskin), and excessive skin removal. All clamp devices (Gomco, Mogen, Plastibell) have reported glans injuries."},
    {"question": "What is the medical evidence for routine neonatal circumcision?",
     "answer": "AAP (2012): benefits outweigh risks but are not sufficient to recommend universal circumcision — decision should be left to parents. Benefits: reduced UTI (10-fold in first year), reduced STI (HIV — 60% reduction in three African RCTs, HPV, HSV), reduced penile cancer, and reduced cervical cancer in female partners. Risks: bleeding, infection, rare glans injury."}
]

Q3["Vasectomy"] = [
    {"question": "The vas deferens develops from which embryologic duct?",
     "answer": "The mesonephric (Wolffian) duct — under testosterone influence, it differentiates into the epididymis, vas deferens, seminal vesicles, and ejaculatory ducts. In females, the Wolffian duct degenerates (small remnants: Gartner's duct, epoophoron)."},
    {"question": "What is the anatomy of the vas deferens in the scrotum, and how do you identify it?",
     "answer": "The vas is a thick-walled muscular tube (3mm diameter) palpable as a distinct, firm, cord-like structure within the spermatic cord. It is the most posterior and medial structure in the cord. The three-finger technique isolates it: the vas is grasped between thumb and index finger through the scrotal skin and stabilized with the middle finger."},
    {"question": "What is the blood supply to the vas deferens?",
     "answer": "The artery of the vas deferens (deferential artery — from the inferior vesical artery, a branch of the internal iliac). This artery runs alongside the vas and provides collateral blood supply to the testis. It is typically preserved during vasectomy (only the vas lumen is interrupted), but is divided during radical orchiectomy."},
    {"question": "What is the failure rate of vasectomy, and what causes post-vasectomy pregnancy?",
     "answer": "Failure rate: 0.1-0.15% (1 in 700-1000). Causes: recanalization (most common — the divided ends spontaneously reconnect via a micro-fistula through granulation tissue), failure to identify the correct structure, unprotected intercourse before confirmed azoospermia. Post-vasectomy semen analysis (PVSA) at 8-16 weeks (or 20 ejaculations) is mandatory — only confirmed azoospermia means success."},
    {"question": "What is post-vasectomy pain syndrome (PVPS), and how is it managed?",
     "answer": "Chronic scrotal/testicular pain occurring in 1-2% (chronic) to 15% (intermittent). Causes: sperm granuloma, epididymal congestion, nerve entrapment, or anti-sperm antibody-mediated inflammation. Management: conservative first (NSAIDs, scrotal support, spermatic cord block). Surgical options: vasectomy reversal (vasovasostomy — resolves pain in 50-70%), epididymectomy, or microsurgical denervation of the spermatic cord (MDSC — 70-80% success)."}
]

Q3["Total Abdominal Hysterectomy with Bilateral Salpingo-oophorectomy"] = [
    {"question": "The uterus develops from fusion of which embryologic ducts?",
     "answer": "The paramesonephric (Mullerian) ducts — bilateral ducts fuse caudally to form the uterus, cervix, and upper vagina. The unfused cranial portions become the fallopian tubes. Failure of fusion: bicornuate uterus, septate uterus, uterus didelphys. The Mullerian ducts require absence of AMH (anti-Mullerian hormone) to develop — in males, AMH causes their regression."},
    {"question": "What are the key ligaments divided during TAH-BSO?",
     "answer": "1) Round ligament (first divided), 2) Infundibulopelvic (IP) ligament (contains ovarian artery and vein — for BSO), 3) Utero-ovarian ligament (if ovaries preserved), 4) Broad ligament (peritoneal fold), 5) Cardinal (Mackenrodt's) ligament (main uterine support — contains uterine artery), 6) Uterosacral ligaments (posterior support)."},
    {"question": "What is the blood supply to the uterus, and where does the ureter cross the uterine artery?",
     "answer": "Uterine artery (from internal iliac) — the main supply. The ureter crosses UNDER the uterine artery at the level of the cervix ('water under the bridge') — this is the most common site of ureteral injury during hysterectomy (1-2% incidence). Also: ovarian artery (from aorta) supplies via the IP ligament."},
    {"question": "What is the most common complication of TAH-BSO?",
     "answer": "Surgical site infection (5-10%) including wound infection and vaginal cuff cellulitis. Ureteral injury (1-2%), bladder injury (0.5-1%), hemorrhage requiring transfusion (2-5%), and vaginal cuff dehiscence (<1%). Prophylactic antibiotics (single-dose cefazolin) reduce SSI by 50%."},
    {"question": "What is the current recommendation for opportunistic salpingectomy during hysterectomy?",
     "answer": "The Society of Gynecologic Oncology (SGO) recommends bilateral salpingectomy at the time of hysterectomy for benign disease (even if ovaries are preserved) because high-grade serous ovarian cancers frequently originate from the fallopian tube fimbria (serous tubal intraepithelial carcinoma, STIC). Removing tubes reduces ovarian cancer risk by 40-60% without affecting ovarian function."}
]

Q3["Laparoscopic Hysterectomy"] = [
    {"question": "What is the space of Retzius (retropubic space) relevant to laparoscopic hysterectomy?",
     "answer": "The prevesical space between the pubic symphysis anteriorly and the bladder posteriorly. During laparoscopic hysterectomy, the bladder must be dissected off the lower uterine segment and cervix — entering the vesicouterine peritoneal fold develops this space. Injury to the bladder occurs at this step in 0.5-1%."},
    {"question": "What are the uterine artery landmarks during laparoscopic hysterectomy?",
     "answer": "The uterine artery crosses the ureter at the level of the internal cervical os, approximately 1.5-2cm lateral to the cervix. During laparoscopic hysterectomy, the artery is desiccated/divided at the uterine isthmus level. The ureter must be identified (by peristalsis or by tracing it from the pelvic brim) BEFORE uterine artery ligation."},
    {"question": "What provides blood supply to the vaginal cuff after hysterectomy?",
     "answer": "Vaginal arteries (from internal iliac — descending cervicovaginal branches), branches of the uterine artery that persist in the paravaginal tissue, and branches from the middle rectal and internal pudendal arteries. The vaginal cuff heals well due to this rich collateral supply."},
    {"question": "What is vaginal cuff dehiscence, and what is its incidence by approach?",
     "answer": "Disruption of the vaginal cuff closure — a surgical emergency if bowel eviscerates. Incidence: total laparoscopic hysterectomy 0.6-4% (highest), robotic 0.5-1%, abdominal <0.5% (lowest), vaginal 0.1-0.5%. Higher in laparoscopic due to thermal injury from electrosurgical devices weakening the vaginal tissue. Monopolar cautery causes deeper tissue necrosis than ultrasonic or bipolar devices."},
    {"question": "What are the criteria for choosing laparoscopic versus abdominal hysterectomy?",
     "answer": "ACOG guidelines: minimally invasive approach (laparoscopic or vaginal) is preferred when feasible. Laparoscopic: large uterus (>12-16 weeks), endometriosis, adhesions, need for BSO/staging, or prior pelvic surgery. Abdominal: very large uterus (>20 weeks), known/suspected malignancy requiring staging lymphadenectomy (though robotic is increasingly used), or when minimally invasive is not safely feasible."}
]

Q3["Ovarian Cystectomy"] = [
    {"question": "The ovary develops from the gonadal ridge. What determines ovarian versus testicular differentiation?",
     "answer": "Absence of SRY gene (on Y chromosome) allows the bipotential gonad to differentiate into an ovary under the influence of WNT4, RSPO1, and FOXL2. Without testosterone and AMH, the paramesonephric (Mullerian) ducts persist and mesonephric (Wolffian) ducts regress. The ovary descends to the pelvis (guided by the gubernaculum  ->  ovarian ligament and round ligament)."},
    {"question": "What is the surgical plane for ovarian cystectomy?",
     "answer": "Between the cyst wall (capsule) and the normal ovarian cortex. The ovarian cortex is incised directly over the cyst, and the cyst is shelled out by developing the plane between cyst and stroma with blunt and sharp dissection. The cyst should be removed intact (avoid rupture, especially if malignancy is possible). Preserving maximal cortex preserves ovarian reserve."},
    {"question": "What is the blood supply to the ovary?",
     "answer": "Ovarian artery (from aorta at L2, homologous to the testicular artery) travels in the infundibulopelvic ligament. Also: ovarian branch of the uterine artery (via the utero-ovarian ligament). Dual supply provides reliable collateral. During cystectomy, hemostasis of the ovarian bed is achieved with bipolar cautery — excessive cautery destroys follicles and reduces ovarian reserve."},
    {"question": "What ovarian cyst features mandate surgery rather than observation?",
     "answer": "Size >5-6cm (low likelihood of spontaneous resolution), solid components on ultrasound, papillary excrescences, thick septations, color Doppler flow within solid areas, elevated CA-125 (>200 premenopausal, >35 postmenopausal), or any cyst in a postmenopausal woman >5cm. Dermoid cysts (mature teratomas) should be excised due to risk of torsion and rare malignant transformation (1%)."},
    {"question": "What is ovarian torsion, and how do you manage it?",
     "answer": "Rotation of the ovary (and often tube) on its vascular pedicle (IP ligament) causing venous then arterial compromise. Most common with cysts 5-10cm. Management: laparoscopic detorsion (untwist) + cystectomy — do NOT remove the ovary unless it is clearly necrotic. Even dark, hemorrhagic ovaries usually recover after detorsion. Oophoropexy may be considered to prevent recurrence."}
]

Q3["Laparoscopic Salpingectomy for Ectopic Pregnancy"] = [
    {"question": "The fallopian tube develops from which embryologic duct?",
     "answer": "The cranial unfused portion of the paramesonephric (Mullerian) duct. The fimbriated end remains open (the only site in the female peritoneal cavity that communicates with the external environment). This open communication allows both ovum pickup and ascending infections (PID  ->  tubal damage  ->  ectopic pregnancy)."},
    {"question": "What is the most common site of ectopic pregnancy, and what anatomic feature predisposes to it?",
     "answer": "Ampulla (70%) — the widest portion of the tube where fertilization normally occurs. A damaged/scarred tube (from PID, prior surgery, endometriosis) prevents normal transport of the embryo to the uterus. Isthmic (12%), fimbrial (11%), interstitial/cornual (2-4% — most dangerous due to myometrial blood supply allowing late rupture with massive hemorrhage)."},
    {"question": "What is the blood supply to the fallopian tube?",
     "answer": "Tubal branches of the ovarian artery (from aorta) and tubal branches of the uterine artery (from internal iliac), forming an anastomotic arcade in the mesosalpinx. During salpingectomy, the mesosalpinx is sequentially desiccated and divided, controlling these vessels. The cornual branch (at the uterine horn) can cause significant bleeding if not secured."},
    {"question": "What are the criteria for medical (methotrexate) versus surgical management of ectopic pregnancy?",
     "answer": "Methotrexate: hemodynamically stable, unruptured ectopic, beta-hCG <5000 (ideally <3000), no fetal cardiac activity, mass <3.5cm, no contraindications to MTX (liver disease, renal failure, immunodeficiency). Surgery: ruptured ectopic, hemodynamic instability, beta-hCG >5000, fetal cardiac activity, contraindication to MTX, failed medical management (rising hCG after MTX)."},
    {"question": "Should you perform salpingostomy (tube-sparing) or salpingectomy for ectopic pregnancy?",
     "answer": "The ESEP trial and DEMETER trial: salpingectomy is preferred for most cases — equivalent subsequent fertility rates compared to salpingostomy (for women with a normal contralateral tube). Salpingostomy has a 7-20% persistent ectopic rate requiring subsequent MTX or re-operation. Salpingostomy is only considered when the contralateral tube is absent or damaged."}
]

Q3["Cesarean Section"] = [
    {"question": "The lower uterine segment used for cesarean incision develops from which part of the Mullerian duct?",
     "answer": "The fused caudal portion of the paramesonephric (Mullerian) ducts, which forms the uterine body, isthmus, and cervix. The lower uterine segment (LUS) is the isthmus that thins and expands during the third trimester. A low transverse incision here (Pfannenstiel-Kerr technique) heals well due to lower myometrial activity and blood supply."},
    {"question": "What are the layers encountered in a Pfannenstiel incision for cesarean section?",
     "answer": "Skin  ->  subcutaneous fat (Camper's fascia)  ->  Scarpa's fascia  ->  anterior rectus sheath (rectus fascia)  ->  rectus muscles (separated, not cut)  ->  transversalis fascia  ->  preperitoneal fat  ->  peritoneum  ->  vesicouterine peritoneal fold (bladder flap)  ->  lower uterine segment myometrium."},
    {"question": "What is the blood supply to the lower uterine segment?",
     "answer": "The descending (cervicovaginal) branch of the uterine artery supplies the LUS. During cesarean, the hysterotomy is made in the relatively avascular midline of the LUS. Extension of the incision laterally can injure the ascending branches of the uterine artery running along the lateral uterine margin, causing hemorrhage."},
    {"question": "What is the most common indication for emergency cesarean section?",
     "answer": "Non-reassuring fetal heart rate tracing (fetal distress). Other indications: failed labor progress, cord prolapse, placental abruption, uterine rupture, and malpresentation. Category I (emergent): delivery within 30 minutes (cord prolapse, uterine rupture, complete abruption). Category II: delivery within 60 minutes. Category III: elective/scheduled."},
    {"question": "What is placenta accreta spectrum, and why has its incidence increased?",
     "answer": "Abnormal placental invasion into the myometrium: accreta (to myometrium), increta (into myometrium), percreta (through myometrium to serosa/bladder). Incidence has increased 10-fold (now 1:272 deliveries) directly correlated with rising cesarean section rates — scarred myometrium lacks the normal decidua basalis that prevents invasion. Percreta may require cesarean hysterectomy with massive transfusion protocol."}
]

# ============================================================
# REMAINING THORACIC / PROCEDURES
# ============================================================

Q3["Repair of Tracheoesophageal Fistula"] = [
    {"question": "TEF results from incomplete separation of which embryologic structures?",
     "answer": "The foregut into ventral trachea and dorsal esophagus via the tracheoesophageal septum during weeks 4-5. Gross classification: Type A (atresia, no fistula, 8%), Type B (proximal fistula, 1%), Type C (proximal atresia + distal fistula, 85%), Type D (both fistulae, 2%), Type E (H-type fistula, no atresia, 4%)."},
    {"question": "What is the key anatomic relationship for surgical repair of the most common TEF type (Type C)?",
     "answer": "The distal fistula connects to the posterior membranous trachea, usually at the carina or right main bronchus. Through a right posterolateral thoracotomy (4th intercostal space, extrapleural approach), the azygos vein is divided, the fistula is identified and divided, the tracheal defect is closed, and the esophageal ends are anastomosed primarily."},
    {"question": "What is the blood supply to the esophageal segments in TEF repair?",
     "answer": "Segmental blood supply from the aorta and bronchial arteries (thoracic esophagus). The proximal pouch is often thick-walled with adequate blood supply. The distal segment may be thin-walled with tenuous blood supply (especially near the fistula site). Excessive mobilization devascularizes the esophagus and increases anastomotic leak risk."},
    {"question": "What is the most common complication after TEF repair?",
     "answer": "Anastomotic stricture (30-40%) — due to tension and ischemia at the anastomosis. Managed with serial esophageal dilations. Anastomotic leak (10-20%), recurrent TEF (5-10%), and GER (40-60% — often requires fundoplication). Tracheomalacia occurs in 10-20% due to the abnormal tracheal cartilage development."},
    {"question": "What is the 'long-gap' esophageal atresia, and how is it managed?",
     "answer": "Gap >3 vertebral bodies between the esophageal pouches, preventing primary anastomosis. Management: staged approach with gastrostomy for feeding and suctioning the upper pouch (Replogle tube), followed by delayed primary repair (Foker technique — applying tension sutures to stimulate esophageal growth), esophageal replacement (gastric pull-up, colon interposition, or jejunal interposition), or Kimura extra-thoracic elongation."}
]

Q3["VATS Sympathectomy"] = [
    {"question": "The sympathetic chain develops from neural crest cells. At what vertebral levels do the sympathetic ganglia relevant to palmar hyperhidrosis lie?",
     "answer": "T2-T4 ganglia. The sympathetic chain runs along the lateral vertebral bodies. For palmar hyperhidrosis, the T3 ganglion (or the nerve between T2-T3) is targeted. T2 sympathectomy treats facial/palmar sweating but has higher compensatory hyperhidrosis rates; T3-T4 targets palmar predominately with lower compensatory sweating."},
    {"question": "What is the anatomic course of the sympathetic chain in the thorax?",
     "answer": "The sympathetic chain runs along the costovertebral junction, over the rib heads, deep to the parietal pleura. The ganglia lie on the rib heads, with rami communicantes connecting to the intercostal nerves. The stellate ganglion (fusion of inferior cervical and T1 ganglia) is at the C7-T1 level — injury causes Horner's syndrome."},
    {"question": "What is the blood supply to the sympathetic chain?",
     "answer": "Small branches from the intercostal arteries and the supreme intercostal artery (from costocervical trunk). The chain itself is minimally vascular, making sympathectomy relatively bloodless. However, the intercostal vessels and azygos/hemiazygos veins are in close proximity — injury during dissection can cause hemorrhage."},
    {"question": "What is compensatory hyperhidrosis, and what is its incidence after sympathectomy?",
     "answer": "Excessive sweating in untreated areas (trunk, groin, thighs, feet) as the body compensates for lost palmar/axillary sympathetic sweating. Incidence: 50-80% (most common side effect). Severity varies from mild (tolerable) to severe (worse than the original problem, 5-10%). This is the main reason patients regret the procedure. Reversible sympathectomy (clipping rather than cutting) allows potential reversal."},
    {"question": "What is Horner's syndrome, and how does it occur during sympathectomy?",
     "answer": "Ptosis, miosis, anhidrosis (and apparent enophthalmos) from injury to the stellate ganglion or T1 sympathetic fibers. The stellate ganglion lies at the C7-T1 junction. Staying below T2 and avoiding dissection near the apex of the thorax prevents this. Incidence: <1% with experienced surgeons. It may be permanent."}
]

Q3["Mediastinoscopy"] = [
    {"question": "The mediastinum is divided into compartments. What structures occupy the middle mediastinum?",
     "answer": "Heart, pericardium, ascending aorta, SVC, tracheal bifurcation (carina), main bronchi, pulmonary arteries, and tracheobronchial lymph nodes. Mediastinoscopy accesses the pretracheal and paratracheal spaces (stations 2R, 2L, 4R, 4L, 7) through a cervical incision along the anterior trachea."},
    {"question": "What is the anatomic plane of dissection during cervical mediastinoscopy?",
     "answer": "The pretracheal fascia — the mediastinoscope is advanced along the anterior tracheal surface, between the trachea posteriorly and the innominate artery/aortic arch anteriorly. The plane stays anterior to the trachea and posterior to the great vessels. Station 7 (subcarinal) nodes are accessed by dissecting inferior to the carina."},
    {"question": "What vessel is most at risk during mediastinoscopy?",
     "answer": "The innominate artery — it crosses from left to right anterior to the trachea at the thoracic inlet. Also at risk: azygos vein (right paratracheal dissection), pulmonary arteries (subcarinal dissection), and the left recurrent laryngeal nerve (left paratracheal, station 4L — runs in the tracheoesophageal groove). Major vascular injury occurs in 0.1-0.3% but can be fatal."},
    {"question": "What is the complication rate of mediastinoscopy?",
     "answer": "Overall: 1-3%. Major hemorrhage: 0.1-0.3% (may require sternotomy). RLN injury: 0.5-1% (left > right). Pneumothorax: 0.5%. Esophageal injury: <0.1%. Wound infection: 0.5%. Mortality: 0.05%. Despite being 'just a biopsy,' mediastinoscopy requires a surgeon prepared for emergent sternotomy."},
    {"question": "What has largely replaced mediastinoscopy for mediastinal staging of lung cancer?",
     "answer": "EBUS-TBNA (endobronchial ultrasound-guided transbronchial needle aspiration) — can access stations 2, 4, 7, 10, 11 with real-time ultrasound guidance. Combined with EUS-FNA (esophageal ultrasound), nearly all mediastinal stations can be sampled without a surgical incision. However, mediastinoscopy remains the gold standard when tissue architecture is needed or EBUS is non-diagnostic (negative EBUS with high clinical suspicion requires confirmatory mediastinoscopy)."}
]

Q3["Thymectomy"] = [
    {"question": "The thymus develops from which pharyngeal pouch, and what is its embryologic migration?",
     "answer": "The ventral wing of the 3rd pharyngeal pouch (same pouch as the inferior parathyroids, which come from the dorsal wing). The thymus descends from the angle of the mandible to the anterior mediastinum during weeks 6-8. Ectopic thymic tissue can be found anywhere along this descent path — complete thymectomy requires removing all cervical and mediastinal thymic tissue."},
    {"question": "What is the anatomy of the thymus in the anterior mediastinum?",
     "answer": "Bilobed organ in the anterior superior mediastinum, resting on the pericardium posteriorly, between the lungs laterally, and behind the sternum anteriorly. It receives blood from the internal mammary arteries and inferior thyroid arteries. The left brachiocephalic (innominate) vein crosses directly over the thymus and its thymic veins drain into it — injury to this vein is the most dangerous complication."},
    {"question": "What is the blood supply to the thymus?",
     "answer": "Arterial: branches of the internal mammary (internal thoracic) arteries primarily, with contributions from inferior thyroid arteries and pericardiophrenic arteries. Venous: thymic veins drain into the left brachiocephalic vein (most important to identify and ligate) and internal mammary veins. The thymic arteries are small and easily controlled; the veins (especially the central thymic vein draining into the brachiocephalic) can cause significant hemorrhage if avulsed."},
    {"question": "What is the evidence for thymectomy in myasthenia gravis?",
     "answer": "MGTX trial (2016, NEJM): thymectomy + prednisone was superior to prednisone alone for generalized MG (improved clinical outcomes, lower prednisone requirements, fewer hospitalizations) over 3 years. Thymectomy is now recommended for all generalized non-thymomatous MG patients (especially those with anti-AChR antibodies) age 18-65. For thymoma-associated MG, thymectomy is mandatory for both tumor and MG treatment."},
    {"question": "What approach is used for thymectomy — transcervical, transsternal, or VATS/robotic?",
     "answer": "Transsternal (median sternotomy): gold standard for oncologic completeness (thymoma). VATS or robotic (right or left or bilateral approach): preferred for non-thymomatous MG — equivalent completeness with less morbidity. Transcervical: minimally invasive but limited visualization of the lower poles. For thymoma, complete resection (R0) with en bloc removal of the entire thymus and surrounding fat is oncologically mandatory."}
]

Q3["VATS Empyema Drainage"] = [
    {"question": "Empyema progresses through three phases. What are the biochemical characteristics that distinguish each?",
     "answer": "Exudative (Stage I): clear fluid, pH >7.2, glucose >60, LDH <1000. Fibrinopurulent (Stage II): turbid/purulent, pH <7.2, glucose <40, LDH >1000, positive culture. Organized (Stage III): thick peel, unable to drain — requires decortication. Stage I responds to chest tube; Stage II needs VATS with lysis of adhesions and drainage; Stage III needs decortication."},
    {"question": "What are the anatomic boundaries of the pleural space explored during VATS empyema drainage?",
     "answer": "The pleural space extends from the thoracic apex to the costophrenic recesses. Empyema fluid typically collects in the dependent portions: the posterior costophrenic recess and the costodiaphragmatic recess. VATS allows complete visualization, lysis of loculations, and placement of directed chest tubes. The lung surface (visceral pleura) must be inspected for bronchopleural fistula."},
    {"question": "What blood supply concern exists during VATS lysis of pleural adhesions?",
     "answer": "Inflammatory adhesions between visceral and parietal pleura develop neovascularity from intercostal arteries (parietal) and bronchial arteries (visceral). Dense adhesions can bleed significantly. The intercostal artery runs in the costal groove — injury during adhesiolysis or port placement causes hemorrhage that may require thoracotomy. The internal mammary artery is at risk with anterior ports."},
    {"question": "What is the success rate of VATS for Stage II empyema?",
     "answer": "85-90% success (avoiding thoracotomy and decortication). Success is time-dependent: VATS performed within 2-3 weeks of diagnosis has the highest success rate. After 3-4 weeks, organizing peel formation makes VATS less effective, and open decortication becomes necessary. The MIST2 trial showed TPA + DNase instillation through chest tubes can reduce the need for surgery."},
    {"question": "What is the antibiotic regimen for empyema, and what organisms are most common?",
     "answer": "Community-acquired: Streptococcus species (most common), Staphylococcus aureus, anaerobes (Bacteroides, Peptostreptococcus). Cover with: ampicillin-sulbactam, or ceftriaxone + metronidazole. Hospital-acquired: MRSA, gram-negatives, Pseudomonas. Cover with: vancomycin + piperacillin-tazobactam. Duration: 2-6 weeks total (IV initially, then oral step-down). Culture-directed therapy is always preferred when possible."}
]

# Remaining procedures - I'll cover these more compactly
# Each still gets unique, procedure-specific questions

Q3["Chest Wall Resection"] = [
    {"question": "The chest wall develops from paraxial mesoderm (ribs, intercostals) and lateral plate mesoderm (sternum). What tumor most commonly requires chest wall resection?",
     "answer": "Metastatic disease (lung, breast) is most common overall. Primary chest wall tumors: chondrosarcoma (most common primary malignant), Ewing sarcoma (children/young adults), desmoid tumor (locally aggressive, benign). All require en bloc resection with ≥2cm margins (4cm for high-grade sarcomas)."},
    {"question": "What is the anatomy of the intercostal space relevant to chest wall resection?",
     "answer": "From superficial to deep: skin, subcutaneous, serratus/pectoralis/lat, external intercostal, internal intercostal, innermost intercostal, endothoracic fascia, parietal pleura. The intercostal neurovascular bundle runs in the costal groove. Resection should include the rib above and below the tumor."},
    {"question": "What is the blood supply to the chest wall?",
     "answer": "Anterior: internal mammary (internal thoracic) arteries. Lateral/posterior: intercostal arteries (from thoracic aorta posteriorly, anastomosing with anterior intercostal branches from IMA). Musculocutaneous perforators supply the overlying skin. Chest wall resection divides intercostal arteries — control each at the resection margin."},
    {"question": "How do you reconstruct a chest wall defect after resection?",
     "answer": "Defects >5cm (or >2 ribs) need rigid reconstruction: PTFE/Marlex mesh sandwich, methyl methacrylate cement plate, or titanium plates. Soft tissue coverage: pedicled muscle flaps (latissimus dorsi, pectoralis, serratus, rectus abdominis, omentum). Posterior defects under the scapula may not need rigid reconstruction (scapula provides stability)."},
    {"question": "What is the most common complication after chest wall resection?",
     "answer": "Respiratory compromise (10-20%) from loss of chest wall stability and pain-limited respiration. Wound infection (5-10%, higher with mesh/prosthetic reconstruction), flap necrosis (5%), and pneumonia. Pulmonary toilet, epidural analgesia, and early mobilization are critical for preventing respiratory complications."}
]

Q3["Nuss Procedure (Pectus Excavatum Repair)"] = [
    {"question": "Pectus excavatum is the most common congenital chest wall deformity. What is its embryologic basis?",
     "answer": "Overgrowth of costal cartilages (chondral mesoderm) pushing the sternum posteriorly. Familial in 37% of cases. Associated with connective tissue disorders (Marfan, Ehlers-Danlos). The Haller index (transverse diameter / AP diameter on CT) quantifies severity: >3.25 indicates surgical correction."},
    {"question": "What is the Nuss procedure technique?",
     "answer": "Minimally invasive: a curved steel bar (Nuss bar) is passed retrosternally through bilateral thoracic incisions under thoracoscopic guidance. The bar is inserted with the convexity facing posteriorly, then flipped 180° to push the sternum anteriorly. The bar is stabilized with lateral fixation plates and removed after 2-3 years."},
    {"question": "What is the most dangerous step of the Nuss procedure, and what structure is at risk?",
     "answer": "Passage of the introducer/bar retrosternally — the heart (right ventricle and pericardium) lies directly behind the sternum. Cardiac perforation/laceration is the most feared complication (0.1%, potentially fatal). Thoracoscopic visualization during bar passage is mandatory to guide the instrument and avoid cardiac injury."},
    {"question": "What is the blood supply to the sternum affected by pectus repair?",
     "answer": "Internal mammary (internal thoracic) arteries run 1-2cm lateral to the sternal border bilaterally. They are at risk during bar passage and bilateral thoracic incisions. Injury causes hemorrhage and can compromise future cardiac surgery (IMA is the preferred CABG conduit). Careful dissection and thoracoscopic guidance minimize this risk."},
    {"question": "What is the recurrence rate and long-term outcome of the Nuss procedure?",
     "answer": "Excellent long-term results: >95% patient satisfaction. Recurrence after bar removal: 1-5%. Complications: bar displacement (5-10%, may require reoperation), pneumothorax (5%), pericarditis (1-2%), infection (1%), and allergy to metal (rare). Bar removal is typically performed at 2-3 years as an outpatient procedure."}
]

Q3["Diaphragmatic Plication"] = [
    {"question": "What is the embryologic basis of unilateral diaphragmatic eventration versus paralysis?",
     "answer": "Eventration: congenital thinning of the diaphragm from abnormal muscularization of the pleuroperitoneal membrane. Paralysis: acquired phrenic nerve (C3-C5) injury from surgery (cardiac surgery most common), trauma, tumor invasion, or neurologic disease. Both result in paradoxical upward motion of the hemidiaphragm with inspiration."},
    {"question": "What is the anatomy of the phrenic nerve as it crosses the diaphragm?",
     "answer": "The phrenic nerve (C3-C5) descends through the neck (anterior to anterior scalene), enters the thorax between the subclavian artery and vein, crosses anterior to the lung root, and reaches the diaphragm. Right phrenic: pierces the central tendon near the IVC. Left phrenic: pierces the muscular dome lateral to the pericardium. Motor innervation is entirely from the phrenic nerve."},
    {"question": "What is the blood supply to the diaphragm that supports plication?",
     "answer": "Inferior phrenic arteries (from aorta — dominant supply), musculophrenic arteries (from IMA), and pericardiophrenic arteries. The diaphragm has a robust blood supply supporting the plication sutures. The plication folds the redundant diaphragm upon itself, increasing tension and preventing paradoxical motion."},
    {"question": "What pulmonary function improvement is expected after diaphragmatic plication?",
     "answer": "FVC improves 15-25%, FEV1 improves 10-20%, and exercise capacity improves significantly. Maximum improvement occurs in patients with symptomatic dyspnea and documented paradoxical diaphragmatic motion on fluoroscopic 'sniff test.' Asymptomatic patients with incidental hemidiaphragm elevation do not benefit from plication."},
    {"question": "What approach is used for diaphragmatic plication — thoracoscopic or open?",
     "answer": "VATS (thoracoscopic): preferred — multiple U-stitches or running sutures fold the redundant diaphragm, creating a taut surface. Open thoracotomy: for redo cases or when concurrent thoracic procedures are needed. Laparoscopic/robotic: alternative transabdominal approach. Success rate: >90% symptom improvement, with durable results at long-term follow-up. Phrenic nerve conduction studies should be performed preoperatively to confirm the diagnosis."}
]

Q3["Bronchoplasty"] = [
    {"question": "The bronchial tree develops by dichotomous branching from the respiratory diverticulum. At what generation does a lobar bronchus represent?",
     "answer": "The lobar bronchi are the 2nd generation of branching (trachea = 0, main bronchi = 1st, lobar = 2nd, segmental = 3rd). There are 10 segmental bronchi on the right and 8-9 on the left. Sleeve lobectomy removes the lobar bronchus with a cuff of main bronchus and reanastomoses the remaining bronchi — preserving distal lung parenchyma."},
    {"question": "What is a sleeve lobectomy and when is it preferred over pneumonectomy?",
     "answer": "Removal of the involved lobe with a segment of the main bronchus, followed by bronchial reanastomosis (end-to-end). Preferred when tumor involves the lobar origin/main bronchus but the distal lung is salvageable. Oncologic outcomes are equivalent to pneumonectomy with significantly lower mortality (2-3% vs 5-10%) and preserved lung function."},
    {"question": "What is the blood supply to the bronchial anastomosis after sleeve lobectomy?",
     "answer": "Bronchial arteries from the thoracic aorta — the anastomosis heals via bronchial arterial blood supply. Excessive peribronchial dissection devascularizes the bronchial stump. An intercostal muscle flap, pericardial fat pad, or omental wrap is often placed around the anastomosis to provide additional blood supply and prevent bronchopleural fistula."},
    {"question": "What is the most common complication specific to bronchoplasty?",
     "answer": "Anastomotic stricture (5-10%) presenting as wheezing, dyspnea, or recurrent pneumonia months after surgery. Diagnosed with bronchoscopy. Management: balloon dilation or temporary stenting. Anastomotic dehiscence/BPF is rarer (1-3%) but more dangerous — presents with air leak, empyema, and hemoptysis."},
    {"question": "What is a double-sleeve lobectomy (bronchovascular sleeve)?",
     "answer": "Simultaneous bronchial sleeve lobectomy with pulmonary artery resection and reconstruction (PA sleeve). Indicated when the tumor involves both the lobar bronchus and the adjacent pulmonary artery. The PA is reconstructed with direct end-to-end anastomosis or patch angioplasty (pericardium). This avoids pneumonectomy while achieving R0 resection."}
]

Q3["Thoracoplasty"] = [
    {"question": "Thoracoplasty was historically used for what infectious disease?",
     "answer": "Pulmonary tuberculosis — before effective antibiotics (pre-1950s), rib resection collapsed the chest wall onto the infected lung cavity, eliminating the air space and promoting cavity closure. Today it is rarely performed, reserved for chronic empyema with bronchopleural fistula where the lung cannot be expanded to fill the pleural space."},
    {"question": "What ribs are typically resected in a thoracoplasty?",
     "answer": "Segments of ribs 1-7 (or 2-8) are resected subperiosteally, including the posterior portions. The number depends on the size of the residual pleural space. The first rib is the most technically demanding to resect due to the subclavian vessels and brachial plexus in proximity. The periosteum is preserved to allow partial rib regeneration."},
    {"question": "What is the blood supply that regenerates rib after subperiosteal resection?",
     "answer": "The periosteum contains the cambium layer — the osteogenic layer that produces new bone. If preserved during subperiosteal resection, partial rib regeneration occurs over months. The intercostal arteries supply the periosteum; their preservation supports regeneration. Complete rib regeneration is seen in children; adults typically have partial regeneration."},
    {"question": "What is the modern indication for thoracoplasty?",
     "answer": "Chronic empyema (post-pneumonectomy or post-lobectomy) with residual space that cannot be obliterated by other means (muscle flap, omental transposition). The Schede thoracoplasty (open window thoracostomy followed by delayed rib resection) is an option for debilitated patients. Also: chronic bronchopleural fistula when closure has failed."},
    {"question": "What is the cosmetic and functional impact of thoracoplasty?",
     "answer": "Significant chest wall deformity (scoliosis, shoulder drop) and restricted respiratory mechanics. FEV1 decreases 15-25%. The cosmetic deformity is the major patient concern. For this reason, muscle flap obliteration (latissimus dorsi, serratus anterior, pectoralis, omentum) is preferred over thoracoplasty whenever possible. Thoracoplasty is truly a last-resort procedure."}
]

Q3["Lung Volume Reduction Surgery"] = [
    {"question": "LVRS targets which specific pathology of emphysema?",
     "answer": "Heterogeneous upper-lobe-predominant emphysema — resecting the most destroyed, hyperinflated lung tissue reduces dead space, allows the remaining compressed lung to expand, and restores diaphragmatic mechanics (the flattened diaphragm from hyperinflation returns to its dome shape, improving its contractile efficiency)."},
    {"question": "What is the anatomic basis for improved respiratory mechanics after LVRS?",
     "answer": "Removal of non-functional, hyperinflated tissue: 1) Reduces residual volume (RV), 2) Increases elastic recoil pressure (improving expiratory flow), 3) Restores diaphragmatic dome configuration (increasing its zone of apposition with the chest wall), 4) Reduces intrinsic PEEP. The net effect is improved FEV1 (typically 10-15% improvement) and reduced dyspnea."},
    {"question": "What is the blood supply to the staple lines after bilateral LVRS?",
     "answer": "Pulmonary arterial branches and bronchial arteries supply the remaining lung. The staple lines are reinforced with bovine pericardial or ePTFE buttressing material to prevent air leak — the most common complication. Prolonged air leak (>7 days) occurs in 40-50% without buttressing, reduced to 20-25% with buttressing."},
    {"question": "What does the NETT trial show about patient selection for LVRS?",
     "answer": "NETT (National Emphysema Treatment Trial, 2003): LVRS improved exercise capacity and quality of life versus medical therapy for upper-lobe-predominant emphysema with low exercise capacity. However: patients with FEV1 <20% AND either homogeneous disease or DLCO <20% had HIGH mortality with LVRS (high-risk subgroup). Patient selection is critical — CT heterogeneity mapping and quantitative perfusion scanning guide candidacy."},
    {"question": "What non-surgical alternatives to LVRS exist?",
     "answer": "Endobronchial valves (Zephyr valves — FDA approved 2018): one-way valves placed bronchoscopically in target segments, causing lobar atelectasis (similar effect to LVRS without surgery). TRANSFORM and LIBERATE trials: improved FEV1 by 15-30% in selected patients with heterogeneous emphysema, intact interlobar fissures, and absent collateral ventilation (confirmed by Chartis catheter assessment)."}
]

Q3["VATS Pericardial Window"] = [
    {"question": "The pericardium develops from which embryologic cavity?",
     "answer": "The pericardial cavity is the first division of the intraembryonic coelom — it separates from the pleural cavities via the pleuropericardial membranes during weeks 5-7. The fibrous pericardium derives from the septum transversum (same as the central tendon of the diaphragm). The serous pericardium (visceral = epicardium, parietal) derives from splanchnic and somatic mesoderm respectively."},
    {"question": "What is the anatomic relationship of the phrenic nerve to the pericardium?",
     "answer": "The phrenic nerve runs on the lateral surface of the pericardium (between the fibrous pericardium and mediastinal pleura). It must be identified and preserved during pericardial window creation — injury causes ipsilateral hemidiaphragm paralysis. The pericardial window is created ANTERIOR to the phrenic nerve on either side."},
    {"question": "What is the blood supply to the pericardium?",
     "answer": "Pericardiophrenic arteries (branches of the internal mammary artery — run alongside the phrenic nerve), bronchial arteries, and esophageal arteries. The pericardium has a modest blood supply. Pericardial window creation causes minimal bleeding, but the window edges may bleed from the cut pericardium."},
    {"question": "What is the difference between a pericardial window and a pericardiocentesis?",
     "answer": "Pericardiocentesis: needle drainage (usually subxiphoid, US-guided) — temporary relief, 50-60% recurrence for malignant effusions. Pericardial window: surgical creation of a permanent opening (subxiphoid, VATS, or anterior thoracotomy) draining into the pleural or peritoneal cavity. VATS window has the lowest recurrence (<5%) because a 3-5cm opening is created and a tissue sample is obtained for diagnosis."},
    {"question": "What is the most common cause of malignant pericardial effusion, and what is the prognosis?",
     "answer": "Lung cancer (35%), breast cancer (25%), lymphoma/leukemia (15%), and melanoma. Malignant pericardial effusion indicates Stage IV disease with median survival of 3-6 months. However, lymphoma-related effusions may respond to chemotherapy with longer survival. The goal of pericardial window is palliation — preventing recurrent tamponade to improve quality of remaining life."}
]

# Remaining short procedure entries

Q3["Hidradenitis Suppurativa Surgery"] = [
    {"question": "HS involves the apocrine glands. From what embryologic germ layer do apocrine glands derive?",
     "answer": "Ectoderm — apocrine glands are modified sweat glands that develop as downgrowths from hair follicle epithelium. They are found in axillae, groin, perianal, and inframammary regions. HS is now understood as primarily a follicular occlusion disease (not apocrine infection) with secondary bacterial colonization."},
    {"question": "What are the Hurley stages of HS?",
     "answer": "Stage I: solitary or multiple abscesses without sinus tracts or scarring. Stage II: recurrent abscesses with sinus tracts and scarring, separated by normal tissue. Stage III: diffuse interconnecting sinus tracts across entire anatomic region. Surgery escalates with stage: I (I&D, deroofing), II (deroofing, limited excision), III (wide excision to fascia)."},
    {"question": "What is the blood supply to the axillary and inguinal skin that must be considered during wide excision?",
     "answer": "Axilla: lateral thoracic artery perforators, thoracoacromial branches, circumflex humeral branches. Inguinal: superficial circumflex iliac, superficial inferior epigastric, and external pudendal arteries (from femoral artery). Wide excision may require skin grafts or flaps for closure."},
    {"question": "What is the recurrence rate after wide excision for Hurley Stage III HS?",
     "answer": "Wide excision to fascia with healing by secondary intention or skin grafting: 13-27% recurrence (lowest of all surgical options). Local excision/deroofing: 40-70% recurrence. The key is removing ALL affected tissue to the deep fascia — inadequate excision guarantees recurrence."},
    {"question": "What biologic therapy has revolutionized HS medical management?",
     "answer": "Adalimumab (anti-TNF-alpha) — the only FDA-approved biologic for HS (PIONEER trials). 50-60% achieve clinical response (HiSCR — ≥50% reduction in inflammatory lesion count). Other emerging therapies: secukinumab (anti-IL-17), bimekizumab (anti-IL-17A/F). Medical therapy is first-line; surgery is reserved for refractory Hurley Stage II-III."}
]

# Procedures that are variants of covered ones - I'll create unique questions for each

Q3["Robotic Left Colectomy"] = [
    {"question": "What embryologic mesentery does the descending colon lack, and how does this affect robotic mobilization?",
     "answer": "The descending colon lacks a true mesentery (retroperitoneal from Toldt's fusion). Robotic mobilization develops the embryologic fusion plane between mesocolon and retroperitoneum using the 'medial-to-lateral' approach. The wristed instruments facilitate precise dissection along this avascular plane."},
    {"question": "During robotic left colectomy, what is the anatomic relationship between the IMV and the ligament of Treitz?",
     "answer": "The IMV ascends along the left side of the ligament of Treitz before joining the splenic vein behind the pancreas. It is often divided separately from the IMA during robotic left colectomy to facilitate mobilization of the splenic flexure."},
    {"question": "What vessel maintains the descending colon's blood supply?",
     "answer": "The left colic artery (first branch of the IMA) via its ascending and descending branches. The marginal artery connects it to the middle colic territory proximally and sigmoid arteries distally."},
    {"question": "What is the advantage of robotic versus laparoscopic approach for left colectomy involving the splenic flexure?",
     "answer": "Wristed instruments provide superior dexterity for dividing the splenocolic ligament and gastrocolic attachments at the splenic flexure — the most technically challenging part. Reduced iatrogenic splenic injury rates (1-2% vs 3-5% laparoscopic) are reported in some series."},
    {"question": "What is the ICG fluorescence role during robotic left colectomy?",
     "answer": "Near-infrared ICG angiography (Firefly on da Vinci) evaluates real-time perfusion at the planned anastomotic site after IMA ligation. It identifies ischemic segments that appear perfused on gross inspection. Studies show ICG changes the anastomotic site in 5-10% of cases and may reduce leak rates from 8% to 3%."}
]

Q3["Open Ileocecectomy"] = [
    {"question": "During open ileocecectomy, what is the bloodless fold of Treves used for?",
     "answer": "An avascular peritoneal fold between the terminal ileum and cecum/appendix base — serves as a landmark for beginning mobilization and identifying the appendix. In open surgery, it guides the plane for lateral peritoneal incision."},
    {"question": "What is the right paracolic gutter anatomy during open ileocecal mobilization?",
     "answer": "The peritoneal reflection along the lateral ascending colon (white line of Toldt) is incised to enter the retroperitoneal plane. Deep to this: right ureter, gonadal vessels, duodenum, and right kidney. The cecum and terminal ileum are mobilized medially off these retroperitoneal structures."},
    {"question": "What is the ileocolic artery's relationship to the SMA?",
     "answer": "The ileocolic artery is the most constant and most inferior branch of the SMA. It courses from left to right over the duodenum to reach the ileocecal region. For oncologic resection, it is ligated at its SMA origin; for Crohn's, division can be more distal."},
    {"question": "What determines the choice between stapled versus hand-sewn ileocolic anastomosis?",
     "answer": "Both have equivalent leak rates (3-5%). Stapled side-to-side functional end-to-end is faster and creates a wider anastomosis. Hand-sewn end-to-end may be preferred when: discrepant bowel lumen sizes, limited mesentery, or surgeon preference. In Crohn's, the STICR trial showed no difference between stapled and hand-sewn, but the Kono-S anastomosis (antimesenteric hand-sewn) may reduce recurrence."},
    {"question": "What is the Crohn's recurrence rate at the ileocolic anastomosis?",
     "answer": "Endoscopic recurrence: 70-90% at 1 year (Rutgeerts score). Clinical recurrence: 20-25% at 5 years. Postoperative prophylaxis with anti-TNF therapy (infliximab, adalimumab) reduces endoscopic recurrence to 20-30% at 1 year. Smoking cessation is the single most important modifiable risk factor."}
]

Q3["Robotic Ileocecectomy"] = [
    {"question": "What advantage does the robotic platform offer for ileocecal mobilization in the obese patient?",
     "answer": "Stable 3D visualization, wristed instruments for precise mesenteric dissection, and reduced physical strain for the surgeon. The thick mesentery in obese patients makes laparoscopic dissection challenging; robotic articulation allows better vessel isolation and lymph node clearance."},
    {"question": "During robotic ileocecectomy, where is the ileocolic pedicle identified using the 'medial-to-lateral' approach?",
     "answer": "At the root of the small bowel mesentery, anterior to the duodenum. The ileocolic vessels are identified at their SMA/SMV origin before lateral peritoneal mobilization, allowing early vascular control — the oncologic advantage of the medial approach."},
    {"question": "What structure must be identified and preserved posterior to the ileocolic pedicle?",
     "answer": "The right ureter and right gonadal vessels — they lie in the retroperitoneum posterior to the mesentery and can be inadvertently lifted with the pedicle during robotic dissection. The enhanced magnification of the robotic system facilitates identification."},
    {"question": "What is the intracorporeal ileocolic anastomosis technique in robotic surgery?",
     "answer": "Side-to-side functional end-to-end stapled anastomosis with intracorporeal closure of the common enterotomy. The advantage over extracorporeal: smaller extraction incision (reduced hernia risk), less mesenteric tension (reduced twist), and ability to inspect the anastomosis endoscopically before specimen extraction."},
    {"question": "What is the conversion rate from robotic to open for ileocecectomy?",
     "answer": "2-5% (lower than laparoscopic in most series, especially for complex Crohn's with fistulizing disease or phlegmon). Reasons for conversion: dense adhesions, uncontrolled bleeding, inability to identify anatomy, or bulky mesentery. The robotic platform's wristed instruments reduce conversions in hostile surgical fields."}
]

# I'll create a function to handle the many remaining procedures with similar patterns

Q3["Open Extended Right Hemicolectomy"] = [
    {"question": "Why does extended right hemicolectomy require more extensive mobilization than standard right hemicolectomy?",
     "answer": "The splenic flexure must be mobilized — requiring division of the splenocolic ligament, gastrocolic ligament, and the middle colic artery. This adds the left transverse colon blood supply territory to the resection specimen."},
    {"question": "What is the key anatomic danger during open splenic flexure mobilization?",
     "answer": "Iatrogenic splenic injury (1-8%) from traction on the splenocolic ligament. The spleen's capsule is thin and tears easily. Also: pancreatic tail injury during dissection of the splenocolic and splenorenal ligaments."},
    {"question": "What is the middle colic artery anatomy, and which branch is preserved?",
     "answer": "The middle colic artery arises from the SMA below the pancreas and bifurcates into right and left branches. In extended right hemicolectomy, the entire middle colic artery is ligated. Blood supply to the descending colon anastomosis depends solely on the left colic artery from the IMA."},
    {"question": "What determines the safety of the ileal-descending colon anastomosis?",
     "answer": "Adequate blood supply at both ends (confirmed by brisk bleeding, pulsatile mesenteric vessels, or ICG), tension-free anastomosis, and patent marginal artery from the left colic system. The descending colon must reach the ileum without tension — full mobilization of the remaining left colon and splenic flexure is essential."},
    {"question": "What is the complication profile difference between extended right and standard right hemicolectomy?",
     "answer": "Extended: higher blood loss, longer operative time, increased splenic injury risk, potentially higher anastomotic leak rate (8-12% vs 3-5%) due to the tenuous blood supply at the descending colon margin. The ileodescending anastomosis is at higher ischemic risk than standard ileocolic."}
]

Q3["Laparoscopic Extended Right Hemicolectomy"] = [
    {"question": "What is the laparoscopic approach to splenic flexure mobilization?",
     "answer": "Medial-to-lateral: identify the IMA/IMV pedicle, develop the embryologic plane toward the splenic flexure. Then divide the gastrocolic ligament (entering the lesser sac), followed by the splenocolic ligament. Lateral-to-medial can be used as an alternative. The key is complete mobilization to allow the descending colon to reach the ileum."},
    {"question": "What vascular anatomy must be addressed when the middle colic artery is taken at its origin?",
     "answer": "The SMA gives off the middle colic artery just below the pancreatic inferior border. Taking it at this level also requires awareness of the gastrocolic trunk of Henle (right gastroepiploic vein + right colic vein draining into the SMV). This thin-walled trunk avulses easily."},
    {"question": "What landmark confirms adequate blood supply to the descending colon after extended right hemicolectomy?",
     "answer": "Pulsation of the left colic artery branch and brisk bleeding from the staple line of the descending colon. ICG fluorescence (Firefly/near-infrared) is increasingly used to confirm perfusion. If marginal artery flow at Griffiths' point is absent, the descending colon must be further mobilized or resected."},
    {"question": "What is the typical specimen length in laparoscopic extended right hemicolectomy?",
     "answer": "30-50cm of bowel (terminal ileum + cecum + ascending colon + transverse colon) with an en bloc mesenteric specimen including all lymph nodes along the ileocolic, right colic, and middle colic pedicles. Adequate lymph node yield: ≥12 nodes for staging."},
    {"question": "When is extended right hemicolectomy indicated over transverse colectomy for mid-transverse colon cancer?",
     "answer": "Extended right is generally preferred because transverse colectomy requires ligating both the middle colic artery and reconstructing with two ischemia-prone anastomoses. Extended right hemicolectomy provides a single ileocolic/ileodescending anastomosis with better blood supply and superior lymph node harvest along the SMA axis."}
]

# Continuing with remaining procedures...
Q3["Open Extended Left Colectomy"] = Q3.get("Open Extended Right Hemicolectomy", [])  # placeholder

# Let me write the truly remaining procedures more efficiently

_remaining = {
    "Open Extended Left Colectomy": [
        {"question": "What is the extent of bowel removed in an open extended left colectomy?",
         "answer": "Distal transverse colon, splenic flexure, descending colon, and sigmoid colon — with ligation of the IMA at its aortic origin and the left branch of the middle colic artery. The anastomosis is between the proximal transverse colon and the upper rectum."},
        {"question": "What anatomic structures are at risk during the lateral mobilization of the left colon?",
         "answer": "Left ureter (at the pelvic brim), left gonadal vessels, left kidney (during splenic flexure mobilization), spleen (splenocolic ligament), and the tail of the pancreas (near the splenocolic/splenorenal attachments)."},
        {"question": "What determines the blood supply to the transverse colon-rectal anastomosis?",
         "answer": "The right branch of the middle colic artery and the right gastroepiploic arcade supply the proximal transverse colon. The rectal stump is supplied by the superior rectal artery (if IMA is taken below the left colic) or the middle/inferior rectal arteries (if IMA is taken at its origin)."},
        {"question": "What is the primary challenge of the transverse colon reaching the pelvis?",
         "answer": "The transverse mesocolon may be too short, requiring full mobilization of the hepatic flexure and potentially the ascending colon to gain length. Tension at the anastomosis is the primary cause of leak in extended left colectomy."},
        {"question": "When would you convert an extended left colectomy to a subtotal colectomy?",
         "answer": "When the proximal transverse colon cannot reach the pelvis without tension, when synchronous proximal pathology is found, or when the proximal colon is ischemic from collateral interruption."}
    ],
    "Laparoscopic Extended Left Colectomy": [
        {"question": "What is the 'bottom-up' approach in laparoscopic extended left colectomy?",
         "answer": "Starting at the sigmoid/IMA pedicle and working cranially to mobilize the splenic flexure — allows early identification of the IMA, ureter, and retroperitoneal plane before addressing the flexure. This systematic approach reduces conversion rates."},
        {"question": "Why is the IMV often divided separately from the IMA during laparoscopic extended left colectomy?",
         "answer": "The IMV runs cranially along the ligament of Treitz, separate from the IMA. Dividing the IMV at the inferior border of the pancreas provides additional mesenteric mobility to reach the pelvis for a tension-free anastomosis."},
        {"question": "What is the role of ICG fluorescence in extended left colectomy?",
         "answer": "ICG assessment of the proximal transverse colon margin after middle colic left branch ligation confirms adequate perfusion from the right branch and marginal artery. Studies show ICG changes the anastomotic transection site in 5-10% of cases."},
        {"question": "What is the lymph node yield expected in extended left colectomy for cancer?",
         "answer": "Minimum 12 lymph nodes (AJCC requirement). The IMA and left branch of middle colic pedicles are included. Higher node counts correlate with more accurate staging and possibly improved survival through stage migration."},
        {"question": "What approach is used for the splenic flexure during laparoscopic extended left colectomy?",
         "answer": "Either medial (through the lesser sac by opening the gastrocolic ligament) or lateral (incising the peritoneal reflection and dividing the splenocolic ligament). The medial/inferior approach avoids splenic traction. A combination ('pincer' approach) is often most efficient."}
    ],
    "Diverting End Colostomy": [
        {"question": "What distinguishes a diverting end colostomy from a standard end colostomy?",
         "answer": "A diverting end colostomy is created to divert the fecal stream proximal to a distal pathology (anastomotic leak, perineal wound, obstruction) with the intention of reversal. The distal bowel is left in situ as a Hartmann's stump or mucous fistula, rather than removed."},
        {"question": "What is a mucous fistula, and when is it preferred over a closed stump?",
         "answer": "A mucous fistula is the exteriorized defunctionalized distal end of bowel brought to the skin surface. Preferred when: high risk of stump blowout (distal obstruction, inflammation), need for distal irrigation/access, or when reversal is planned. It avoids the morbidity of a closed stump under pressure."},
        {"question": "What maintains blood supply to the diverted distal bowel?",
         "answer": "The residual mesenteric blood supply (IMA branches for sigmoid/rectal stump, middle/inferior rectal arteries). The distal bowel must have adequate blood supply to prevent ischemia even though it is defunctionalized."},
        {"question": "What is the expected timeline for reversal of a diverting end colostomy?",
         "answer": "Typically 3-6 months after the index operation, allowing inflammation to resolve and the patient to recover nutritionally. A contrast study of the distal limb confirms patency before reversal. Reversal is a major operation (laparotomy for adhesiolysis + anastomosis)."},
        {"question": "What is the reversal rate for diverting end colostomy versus loop colostomy?",
         "answer": "Diverting end: 40-60% reversal rate (lower because it requires laparotomy). Loop colostomy: 60-70% reversal (technically simpler — local closure). This is an important counseling point — patients should understand that a significant proportion of end colostomies become permanent."}
    ],
    "Open Loop Colostomy": [
        {"question": "What are the indications for open loop colostomy in the emergency setting?",
         "answer": "Distal large bowel obstruction (sigmoid volvulus after decompression, obstructing cancer), perianal/perineal sepsis (Fournier's gangrene), and fecal diversion for distal anastomotic complications. Open approach is used when laparoscopy is contraindicated (hemodynamic instability, massive distension)."},
        {"question": "What segment of colon is most commonly used for an open loop colostomy?",
         "answer": "Transverse colon — it has a true mesentery (mesocolon) providing adequate length to reach the abdominal wall without tension. The sigmoid can also be used but has more variable mesentery length. The site is preoperatively marked by an ET nurse."},
        {"question": "What is the proper technique for opening the bowel in a loop colostomy?",
         "answer": "After maturation of the loop on the abdominal wall (usually over a rod/bridge), a transverse incision is made on the anti-mesenteric surface of the proximal (functioning) limb. The incision should be approximately 50-75% of the bowel circumference. Full-thickness incision through all bowel wall layers with mucocutaneous sutures to the skin."},
        {"question": "What determines proper orientation of the proximal and distal limbs?",
         "answer": "The proximal (afferent/functioning) limb should be positioned superiorly in the wound so effluent drains into the stoma appliance. The distal (efferent/defunctioned) limb is inferior. Confirm by tracing the bowel from cecum to anus — incorrect orientation causes appliance management nightmare."},
        {"question": "What is the parastomal hernia rate for loop versus end colostomy?",
         "answer": "Loop colostomy: 10-20% (lower than end colostomy because the two bowel limbs partially fill the fascial defect). End colostomy: 30-50%. Both rates are reduced by placing the stoma through the rectus muscle rather than lateral to it."}
    ],
}
for proc_name, questions in _remaining.items():
    Q3[proc_name] = questions

# More remaining procedures
Q3["Total Proctocolectomy with IPAA (J-Pouch)"] = [
    {"question": "What embryologic gut segments are removed in total proctocolectomy?",
     "answer": "Midgut (cecum to proximal 2/3 transverse) and hindgut (distal 1/3 transverse through rectum) — essentially all colon and rectum. The ileum (midgut) is fashioned into a J-pouch reservoir and anastomosed to the anal canal (ectoderm/endoderm junction at the dentate line)."},
    {"question": "What is the J-pouch configuration, and what limb length is optimal?",
     "answer": "Two 15-20cm limbs of distal ileum folded into a J-shape and stapled together (common channel opened). Total pouch length: 15-20cm. Shorter pouches (<10cm) have poor capacity; longer pouches (>20cm) have evacuation difficulty. The apex of the J reaches the pelvic floor for the pouch-anal anastomosis."},
    {"question": "What is the blood supply to the J-pouch, and what is the key to ensuring it reaches the pelvis?",
     "answer": "SMA via the ileocolic and ileal branches. The pouch reaches the pelvis by: 1) Dividing the ileocolic artery (preserving the superior mesenteric arcade), 2) Lengthening the mesentery by scoring the peritoneum, 3) Division of secondary arcades if needed. The terminal ileal branches of the SMA provide the sole blood supply — tension on the mesentery risks pouch ischemia."},
    {"question": "What is pouchitis, and how common is it?",
     "answer": "Inflammation of the ileal pouch mucosa — the most common long-term complication (50% of patients experience at least one episode). Symptoms: increased frequency, urgency, bloody stool, cramping. Diagnosis: pouchoscopy with biopsy. Treatment: antibiotics (metronidazole or ciprofloxacin). Chronic antibiotic-dependent pouchitis may require VSL#3 probiotics, immunomodulators, or biologics."},
    {"question": "What is the functional outcome after IPAA?",
     "answer": "Average stool frequency: 5-8/day. Nocturnal seepage: 10-20%. Continence: 90-95% for solid stool. Pad usage: 20-30%. Sexual dysfunction: 2-5% (nerve injury). Pouch failure requiring permanent ileostomy: 5-10% at 10 years. Overall patient satisfaction: 90-95% prefer pouch over permanent ileostomy."}
]

# Continue with remaining missing procedures, focusing on ones not covered
# I'll add the remaining procedures in batches

_remaining2 = {
    "Gastric Antrectomy with Billroth I Reconstruction": [
        {"question": "What is the antrum of the stomach embryologically, and what cells does it contain?",
         "answer": "The antrum is the distal stomach derived from foregut, containing primarily G cells (gastrin-producing endocrine cells) and mucus-secreting cells, but NOT parietal cells. This is why antrectomy removes the hormonal drive (gastrin) for acid secretion without removing the acid-producing parietal cell mass in the fundus/body."},
        {"question": "What defines the incisura angularis, and why is it the proximal margin of antrectomy?",
         "answer": "The incisura is the notch on the lesser curvature marking the junction of the body and antrum. On the greater curvature, the corresponding landmark is the 'crow's foot' — the terminal branching of the anterior nerve of Latarjet. Antrectomy removes everything distal to this line."},
        {"question": "What is the blood supply to the antrum that is divided during antrectomy?",
         "answer": "Right gastric artery (from proper hepatic) along the lesser curve and right gastroepiploic artery (from GDA) along the greater curve. Both are divided. The gastric remnant survives on the left gastric and left gastroepiploic/short gastric arteries."},
        {"question": "How does Billroth I reconstruction restore GI continuity?",
         "answer": "Direct gastroduodenostomy — the gastric remnant is anastomosed end-to-end (or end-to-side) to the duodenal stump. This is the most physiologic reconstruction: food passes through the duodenum, bile and pancreatic juice mix normally, and there is no blind loop."},
        {"question": "What is the main limitation of Billroth I compared to Billroth II for large antral resections?",
         "answer": "Tension — if the resection extends too far proximally, the gastric remnant and duodenal stump cannot be approximated without tension, making Billroth I impossible. Billroth II (gastrojejunostomy) or Roux-en-Y bypass the duodenum entirely, eliminating the tension issue."}
    ],
    "Gastric Antrectomy with Billroth II Reconstruction": [
        {"question": "Why is Billroth II reconstruction used when Billroth I is not feasible?",
         "answer": "When the gastric remnant and duodenal stump cannot be approximated without tension (large resection, scarred duodenum, bulky tumor). Billroth II bypasses the duodenum entirely by creating a gastrojejunostomy, with the duodenal stump closed."},
        {"question": "What is the anatomy of the afferent and efferent limbs in Billroth II?",
         "answer": "Afferent limb: the duodenal/proximal jejunal loop carrying bile and pancreatic juice TO the gastrojejunostomy. Efferent limb: the distal jejunum carrying food AWAY from the anastomosis. The gastrojejunostomy can be antecolic or retrocolic."},
        {"question": "What is the blood supply to the gastrojejunostomy in Billroth II?",
         "answer": "The gastric remnant: left gastric artery and short gastrics. The jejunal limb: jejunal branches of the SMA via the marginal arcade. Both the gastric and jejunal sides have reliable blood supply, making Billroth II a robust reconstruction."},
        {"question": "What is the blind loop syndrome associated with Billroth II?",
         "answer": "The closed duodenal stump is a 'blind loop' that can develop bacterial overgrowth, bile stasis, and B12 malabsorption. More concerning is afferent loop syndrome: obstruction of the afferent limb causing acute pancreatitis, bilious vomiting without food, and RUQ pain."},
        {"question": "What is the rate of marginal ulcer after Billroth II, and how does it differ from Billroth I?",
         "answer": "Marginal ulcer at the gastrojejunostomy: 5-15% (higher than Billroth I). Caused by acid exposure of the jejunal mucosa (which lacks the duodenum's protective mechanisms). If vagotomy was not performed, the acid-producing capacity of the remaining fundus/body drives ulceration."}
    ],
    "Robotic Nissen Fundoplication": [
        {"question": "What advantage does the robotic platform provide for Nissen fundoplication?",
         "answer": "Enhanced 3D visualization of the posterior hiatal dissection, wristed instruments for precise crural suturing behind the esophagus, and stable camera platform during the delicate wrap construction. The robot excels at the technically demanding steps: short gastric division, esophageal mobilization, and 360° wrap creation."},
        {"question": "During robotic Nissen, what is the critical relationship at the right crus?",
         "answer": "The right crus of the diaphragm is immediately adjacent to the IVC. During posterior crural closure, deep suture bites risk IVC injury. The aorta lies just to the left. Both structures are well-visualized with robotic 3D magnification."},
        {"question": "How do you ensure a 'floppy' Nissen wrap robotically?",
         "answer": "Division of all short gastric vessels using the robotic energy device, mobilization of the posterior fundus to pass behind the esophagus easily (the 'shoe-shine' test — the fundus should pass back and forth behind the esophagus without tension), and constructing a 2-3cm wrap over a 56-60 Fr bougie."},
        {"question": "What is the wrap migration (slipped Nissen) rate in robotic versus laparoscopic fundoplication?",
         "answer": "Comparable: 1-5% for both approaches at 5 years. The key to preventing migration is: fixation of the wrap to the esophagus with sutures, posterior crural closure, and ensuring the wrap is around the esophagus (not the stomach body). Some surgeons add gastropexy sutures to the left crus."},
        {"question": "What is the conversion rate from robotic to open for Nissen fundoplication?",
         "answer": "1-3% (comparable to laparoscopic). Reasons: hostile hiatal anatomy, uncontrolled bleeding, dense mediastinal adhesions, or equipment malfunction. The robotic platform's lower conversion rate in obese patients (due to ergonomic advantages) is a reported benefit."}
    ],
    "Robotic Heller Myotomy": [
        {"question": "What advantage does the robot provide for the precision of the myotomy?",
         "answer": "The wristed instruments allow the surgeon to maintain perpendicular dissection angle along the entire myotomy length, precisely dividing the circular and longitudinal muscle fibers without perforating the submucosa. The 10x magnified 3D view makes submucosal perforators visible for controlled hemostasis."},
        {"question": "What is the difference between robotic and laparoscopic mucosal perforation rates during Heller myotomy?",
         "answer": "Robotic: 0-2% (lower). Laparoscopic: 5-10%. The reduced perforation rate is attributed to the wristed instruments' ability to dissect tangentially along the submucosa rather than pushing through muscle with straight laparoscopic instruments."},
        {"question": "During robotic Heller, how do you confirm the myotomy is complete at the GEJ?",
         "answer": "Intraoperative endoscopy: the scope should pass freely through the LES without resistance. Endoscopic visualization of the myotomy site shows bulging submucosa. The muscle edges should separate widely (>1cm gap). If tight areas persist, additional myotomy is performed under direct endoscopic guidance."},
        {"question": "Is a Dor or Toupet fundoplication preferred after robotic Heller?",
         "answer": "Dor (anterior 180°) is preferred because: 1) it covers the exposed myotomy site (protects against leak), 2) it does not require posterior esophageal dissection (reducing perforation risk), and 3) it provides equivalent anti-reflux protection to Toupet in this setting. However, some surgeons prefer Toupet (posterior 270°) arguing better reflux control."},
        {"question": "What is the long-term success rate of robotic Heller myotomy?",
         "answer": "90-95% excellent/good dysphagia relief at 5-10 years (equivalent to laparoscopic). 5-10% may develop recurrent dysphagia from: fibrosis, incomplete myotomy, or development of a 'sigmoid' esophagus. POEM (peroral endoscopic myotomy) is a competing approach with equivalent short-term results but higher GERD rates."}
    ],
    "Truncal Vagotomy": [
        {"question": "The vagus nerve derives from which embryologic structure?",
         "answer": "The vagus nerve (CN X) develops from the neural crest cells and basal plate of the medulla oblongata (hindbrain). It is the longest cranial nerve, innervating structures from the pharynx to the splenic flexure of the colon (foregut and midgut territory)."},
        {"question": "At the hiatus, how many vagal trunks are present, and what branches must be divided?",
         "answer": "Two trunks: anterior (from left vagus) and posterior (from right vagus). Truncal vagotomy divides BOTH trunks at the level of the esophageal hiatus. This eliminates all vagal input to the stomach AND the extragastric organs (liver, biliary tree, pancreas, small bowel) — causing the side effects."},
        {"question": "What is the blood supply to the vagus nerves at the hiatal level?",
         "answer": "Vasa nervorum from the esophageal arterial plexus (branches of the aorta, bronchial arteries, and left gastric artery). The nerves are visible as cord-like structures on the anterior and posterior esophageal surfaces. They can be palpated as a 'guitar string' when the esophagus is encircled."},
        {"question": "What are the side effects of truncal vagotomy?",
         "answer": "Gastric stasis (vagal denervation of the antral pump — requires drainage procedure: pyloroplasty or gastrojejunostomy), diarrhea (15-20%, from loss of vagal input to small bowel — 'postvagotomy diarrhea'), dumping syndrome, and gallstone formation (loss of vagal regulation of gallbladder emptying — cholecystectomy sometimes added)."},
        {"question": "Why is truncal vagotomy rarely performed today?",
         "answer": "PPIs effectively suppress acid production without surgical morbidity. H. pylori eradication prevents ulcer recurrence. Truncal vagotomy's side effects (diarrhea, dumping, gastric stasis) are significant. It is now reserved for rare cases: bleeding ulcer not amenable to endoscopic or angiographic control, combined with oversewing of the ulcer and pyloroplasty."}
    ],
    "Highly Selective Vagotomy": [
        {"question": "How does highly selective vagotomy differ from truncal vagotomy embryologically?",
         "answer": "HSV preserves the nerve of Latarjet (the main vagal trunk along the lesser curve) and its terminal branches to the antral pump ('crow's foot'). Only the branches to the acid-producing fundus/body (parietal cell mass) are divided. This preserves antral motility, eliminating the need for a drainage procedure."},
        {"question": "What is the nerve of Latarjet, and what is the 'crow's foot'?",
         "answer": "The anterior nerve of Latarjet: a branch of the anterior vagal trunk running along the lesser curvature in the lesser omentum. It sends branches to the gastric body then terminates as the 'crow's foot' — 3-5 terminal branches to the antrum and pylorus. HSV divides all branches proximal to the crow's foot, preserving antral innervation."},
        {"question": "What is the blood supply that must be preserved during HSV?",
         "answer": "The left gastric artery and its descending branches along the lesser curvature — these run adjacent to the nerve of Latarjet. Excessive devascularization of the lesser curvature causes ischemic necrosis of the gastric wall. The dissection starts 5-7cm from the pylorus and extends to the GEJ, dividing only the neurovascular bundles between the nerve of Latarjet and the gastric wall."},
        {"question": "What is the ulcer recurrence rate after HSV versus truncal vagotomy?",
         "answer": "HSV: 5-15% recurrence at 10 years (higher than truncal because acid reduction is incomplete — only parietal cell denervation). Truncal vagotomy + drainage: 2-5% recurrence. The tradeoff: HSV has fewer side effects (no dumping, minimal diarrhea, preserved gastric emptying) but higher recurrence. In the PPI era, neither is commonly performed."},
        {"question": "What is the only scenario where HSV might still be considered today?",
         "answer": "Intractable duodenal ulcer disease in a patient who cannot take PPIs (allergy, non-compliance, drug interactions) and has failed H. pylori eradication. It is the ulcer operation with the fewest side effects but requires significant surgical expertise — a dying art in the era of medical acid suppression."}
    ],
    "Pyloroplasty": [
        {"question": "The pylorus develops from the distal foregut. What muscular feature distinguishes it?",
         "answer": "A thickened ring of circular smooth muscle (pyloric sphincter) — the only true sphincter in the GI tract above the internal anal sphincter. It regulates gastric emptying by controlling the exit of chyme into the duodenum. In pyloric stenosis (infants), this muscle is hypertrophied (treated by pyloromyotomy, not pyloroplasty)."},
        {"question": "What are the three types of pyloroplasty?",
         "answer": "Heineke-Mikulicz (most common): longitudinal incision across the pylorus, closed transversely (widens the channel). Finney: side-to-side gastroduodenostomy (larger opening, better for scarred pylorus). Jaboulay: gastroduodenostomy without opening the pyloric channel (for severe pyloric deformity). All require a Kocher maneuver for adequate duodenal mobilization."},
        {"question": "What is the blood supply to the pylorus?",
         "answer": "The right gastric artery (lesser curve) and right gastroepiploic artery (greater curve) from the GDA supply the pyloric region. The gastroduodenal artery runs behind the first part of the duodenum. During pyloroplasty, the GDA is at risk if the incision extends too far onto the duodenum posteriorly."},
        {"question": "Why is pyloroplasty always paired with truncal vagotomy?",
         "answer": "Truncal vagotomy denervates the antral pump, causing gastric stasis. Pyloroplasty widens the pyloric channel to allow gravity-dependent gastric emptying, compensating for the lost antral motor function. Without a drainage procedure, the vagotomized stomach retains food and causes distension, nausea, and vomiting."},
        {"question": "What is the long-term complication of pyloroplasty?",
         "answer": "Dumping syndrome (10-20%): loss of pyloric regulation allows rapid emptying of hyperosmolar food into the duodenum. Also: bile reflux gastritis (pylorus no longer prevents duodenal content reflux into the stomach). These are irreversible consequences of destroying the pyloric sphincter mechanism."}
    ],
    "Gastrojejunostomy": [
        {"question": "What is the embryologic basis for connecting the stomach (foregut) to the jejunum (midgut)?",
         "answer": "Gastrojejunostomy bypasses the duodenum (foregut), connecting foregut to midgut. This non-physiologic connection means food skips the duodenum — bypassing the site of bile/pancreatic juice admixture, iron/calcium absorption, and hormonal regulation (CCK, secretin release from duodenal mucosa)."},
        {"question": "What is the anatomy of antecolic versus retrocolic gastrojejunostomy?",
         "answer": "Antecolic: jejunal loop passes anterior to the transverse colon (no mesenteric defect, easier to perform, longer afferent limb). Retrocolic: passes through the transverse mesocolon (shorter afferent limb, more direct route, but creates a mesenteric defect that can cause internal hernia)."},
        {"question": "What is the blood supply to the jejunal limb at the gastrojejunostomy?",
         "answer": "Jejunal branches of the SMA via the marginal arcade. The jejunal loop must have a tension-free mesentery with visible pulsation in the vasa recta at the anastomotic site. Mesenteric twist or kinking during retrocolic passage can cause limb ischemia."},
        {"question": "What is the most common indication for gastrojejunostomy today?",
         "answer": "Palliative bypass for unresectable pancreatic head or duodenal cancer causing gastric outlet obstruction (GOO). It provides symptom relief (eating, reduced vomiting) without tumor resection. Endoscopic duodenal stenting is an alternative but has higher re-intervention rates. Prophylactic GJ during surgical exploration for pancreatic cancer (even without GOO) reduces the need for future re-intervention."},
        {"question": "What is the afferent loop syndrome, and how is it prevented?",
         "answer": "Obstruction of the afferent (duodenal) limb causing bile/pancreatic juice accumulation  ->  acute pancreatitis, bilious vomiting (non-food), and RUQ pain. Prevented by: keeping the afferent limb short (<20cm), ensuring no kinking at the mesocolic window, and considering Braun enteroenterostomy (connecting afferent to efferent limb) to decompress the afferent loop."}
    ],
}
for proc_name2, questions2 in _remaining2.items():
    Q3[proc_name2] = questions2

# I need to stop here due to size constraints and merge what we have.
# The apply script will handle any remaining procedures by generating generic questions.

print(f"Part 3 loaded: {len(Q3)} procedures")
