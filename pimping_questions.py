#!/usr/bin/env python3
"""
Add 5 procedure-specific pimping questions to every procedure in procedures.json.
Questions: embryology, anatomy, blood supply, complication, clinical pearl.
Written like a seasoned attending surgeon who's been pimping residents for 20+ years.
"""
import json

QUESTIONS = {}

# ============================================================
# HEPATOPANCREATOBILIARY
# ============================================================

QUESTIONS["Laparoscopic Cholecystectomy"] = [
    {"question": "The falciform ligament is a remnant of what embryologic structure?",
     "answer": "The ventral mesentery (specifically the umbilical vein within it becomes the ligamentum teres)."},
    {"question": "What three criteria define the critical view of safety in cholecystectomy?",
     "answer": "1) Hepatocystic triangle cleared of all fibrous and fatty tissue, 2) Only two structures (cystic duct and cystic artery) seen entering the gallbladder, 3) The lower third of the cystic plate (liver bed) is exposed."},
    {"question": "The cystic artery typically arises from which vessel, and what is the most common variant?",
     "answer": "Right hepatic artery within the hepatocystic triangle. Most common variant is origin from the left hepatic artery or a replaced right hepatic artery off the SMA (~25%)."},
    {"question": "What is Mirizzi syndrome and how does it complicate cholecystectomy?",
     "answer": "Extrinsic compression of the common hepatic duct by an impacted stone in the cystic duct or Hartmann's pouch. Type II-IV involve cholecystocholedochal fistula, making dissection treacherous and often requiring bile duct reconstruction."},
    {"question": "What is Rouviere's sulcus and how does it help prevent bile duct injury?",
     "answer": "A 2-5cm cleft on the inferior surface of the right liver lobe running anterior to the caudate process. Dissection should remain anterior and to the right of this sulcus to stay safely above the bile duct."}
]

QUESTIONS["Open Cholecystectomy"] = [
    {"question": "From what embryologic structure does the gallbladder develop?",
     "answer": "The caudal bud of the hepatic diverticulum from the foregut endoderm during week 4 of development."},
    {"question": "What is the triangle of Calot versus the hepatocystic triangle, and which is more surgically relevant?",
     "answer": "Calot's triangle: cystic duct, cystic artery, and common hepatic duct. The hepatocystic triangle (cystic duct, CHD, and inferior liver edge) is more surgically relevant because it encompasses the area of dissection and potential injury."},
    {"question": "What is the 'caterpillar hump' and why must you identify it during open cholecystectomy?",
     "answer": "A tortuous right hepatic artery that loops into the hepatocystic triangle, mimicking the cystic artery. Failure to recognize it risks ligation of the right hepatic artery causing right liver ischemia."},
    {"question": "What is a bile duct of Luschka and what complication does it cause?",
     "answer": "Small accessory bile ductules draining directly from the liver bed into the gallbladder fossa. If not recognized, they cause postoperative bile leak (biloma) even when the cystic duct stump is secure."},
    {"question": "When performing a fundus-first cholecystectomy, what is the key advantage in a hostile hilum?",
     "answer": "It allows identification from known anatomy (fundus) toward unknown (hilum), reducing risk of CBD injury in severe inflammation. The cystic duct-CBD junction is defined last when surrounding anatomy is clearer."}
]

QUESTIONS["Cholecystectomy with Intraoperative Cholangiogram"] = [
    {"question": "What is the embryologic explanation for a choledochal cyst?",
     "answer": "Anomalous pancreaticobiliary ductal junction (APBDJ) — the pancreatic duct joins the CBD outside the duodenal wall, creating a long common channel allowing pancreatic juice reflux that weakens the bile duct wall. Todani classification types I-V."},
    {"question": "During IOC, what structures should you identify on the fluoroscopic image?",
     "answer": "1) Right and left hepatic duct bifurcation, 2) Common hepatic duct, 3) Cystic duct insertion, 4) CBD (normal ≤8mm), 5) Free flow into duodenum. Absent duodenal filling suggests distal obstruction — give glucagon 1mg IV to differentiate spasm from stone."},
    {"question": "What percentage of patients have 'classic' biliary anatomy, and what are the dangerous variants?",
     "answer": "Only 55-60% have classic anatomy. Dangerous variants: low-inserting right posterior sectoral duct (mistaken for cystic duct), aberrant right hepatic duct crossing the hepatocystic triangle, and short cystic duct with medial CBD insertion."},
    {"question": "If IOC shows a retained CBD stone, what are your intraoperative options?",
     "answer": "1) Laparoscopic transcystic CBD exploration with choledochoscope (stones <8mm), 2) Fogarty balloon retrieval, 3) Glucagon + saline flush, 4) Formal choledochotomy for larger/multiple stones, 5) Postoperative ERCP. Transcystic exploration succeeds in 85-95%."},
    {"question": "What is the evidence for routine versus selective intraoperative cholangiography?",
     "answer": "Routine IOC detects unsuspected CBD stones (3-5%) and identifies aberrant anatomy. Sweden's mandatory IOC registry shows lower bile duct injury rates (0.1% vs 0.3%). However, no RCTs confirm superiority. It adds 10-15 minutes and has a 1-2% false positive rate."}
]

QUESTIONS["Choledochojejunostomy"] = [
    {"question": "What congenital anomaly results from failure of the ventral pancreatic bud to rotate around the duodenum?",
     "answer": "Annular pancreas — the ventral bud encircles D2 causing duodenal obstruction. Presents in neonates (double-bubble sign) or adults (pancreatitis, obstruction). Associated with Down syndrome."},
    {"question": "What is the minimum bile duct diameter for a safe choledochojejunostomy, and why?",
     "answer": "≥1cm (ideally ≥1.5cm). Small ducts increase stricture risk. The duct must be spatulated to increase the anastomotic circumference. For small ducts, hepaticojejunostomy is preferred — the CHD is usually more dilated above an obstruction."},
    {"question": "What is the blood supply to the supraduodenal CBD, and why is excessive mobilization dangerous?",
     "answer": "The 3 and 9 o'clock arteries — small branches from the GDA, right hepatic artery, and cystic artery running axially along the lateral CBD walls. Excessive circumferential mobilization strips these vessels, causing ischemic stricture."},
    {"question": "What is the most important late complication of choledochojejunostomy?",
     "answer": "Ascending cholangitis from enteric bacteria refluxing up a short Roux limb. The Roux limb must be 40-60cm to prevent this. Presents with Charcot's triad (fever, jaundice, RUQ pain). Managed with IV antibiotics and interventional drainage if needed."},
    {"question": "What is the long-term patency rate, and how do you manage anastomotic stricture?",
     "answer": "85-90% patency at 10 years. Stricture is managed with percutaneous transhepatic cholangiography (PTC) and balloon dilation, or via double-balloon enteroscopy to access the Roux limb endoscopically. Refractory strictures require surgical revision."}
]

QUESTIONS["Kasai Procedure (Hepatic Portoenterostomy)"] = [
    {"question": "What are the two proposed embryologic theories for biliary atresia?",
     "answer": "1) Defective ductal plate remodeling (embryonic form, 15%, associated with laterality defects/polysplenia), 2) Perinatal viral infection (reovirus, CMV) triggering autoimmune bile duct destruction. Most evidence supports genetic susceptibility plus perinatal viral trigger."},
    {"question": "At what level is the transection made in Kasai, and what guides the plane?",
     "answer": "Flush with the liver capsule at the porta hepatis bifurcation plate. Microscopic bile ductules (<150 micrometers) within this fibrous plate communicate with intrahepatic ducts and drain into the Roux limb. The transection must be precisely at the liver surface — too shallow misses the ductules, too deep injures portal structures."},
    {"question": "What structures immediately posterior to the bile duct remnant must be preserved during Kasai?",
     "answer": "The portal vein bifurcation and hepatic artery branches (right and left). These run directly behind the fibrous remnant. Injury to either is catastrophic and may preclude future liver transplantation."},
    {"question": "What is the critical timing window for Kasai, and what are success rates by age?",
     "answer": "Must be performed before 60-90 days of age. Bile clearance rates: <30 days: 70-80%, 30-60 days: 50-60%, 60-90 days: 25-40%, >90 days: <20%. Even after successful Kasai, 50% need liver transplant by age 5 and 70% by age 20."},
    {"question": "What unique complication occurs in 40-50% of post-Kasai patients?",
     "answer": "Ascending cholangitis — enteric bacteria ascend the Roux limb into intrahepatic bile ducts. Treated with IV antibiotics (gram-negative and anaerobic coverage). Prophylactic TMP-SMX is given for 1-2 years. Recurrent cholangitis accelerates hepatic fibrosis and hastens need for transplantation."}
]

QUESTIONS["Common Bile Duct Exploration"] = [
    {"question": "The hepatopancreatic ampulla of Vater forms from the fusion of which two embryologic ductal systems?",
     "answer": "The CBD (from hepatic diverticulum/foregut) and the ventral pancreatic duct (from ventral pancreatic bud). They fuse during ventral bud rotation. A long common channel (>15mm, APBDJ) predisposes to choledochal cysts and gallbladder cancer."},
    {"question": "What are the four portions of the CBD, and which segment is accessed during supraduodenal choledochotomy?",
     "answer": "1) Supraduodenal (accessed for choledochotomy — 2-3cm, anterior to portal vein), 2) Retroduodenal, 3) Intrapancreatic, 4) Intraduodenal (ampulla). The choledochotomy is a longitudinal anterior incision to avoid the lateral axial blood supply."},
    {"question": "Why is the choledochotomy made longitudinally rather than transversely on the CBD?",
     "answer": "The 3 and 9 o'clock axial arteries run along the lateral CBD walls. A longitudinal anterior midline incision preserves these vessels. A transverse incision would divide them, causing ischemia and stricture — the most devastating long-term complication."},
    {"question": "What is the difference between transcystic and transductal approaches to CBDE?",
     "answer": "Transcystic: stones <8mm, few in number, dilated cystic duct. Avoids choledochotomy, no T-tube. Transductal: stones >8mm, multiple stones, small/tortuous cystic duct, or intrahepatic stones. Requires choledochotomy with primary closure or T-tube."},
    {"question": "What does current evidence show about T-tube versus primary closure after choledochotomy?",
     "answer": "Multiple RCTs show primary closure has shorter hospital stay, less bile leak, and equivalent stone clearance. T-tube complications include bile leak on removal (1-5%), accidental dislodgement causing biliary peritonitis, and tract cholangitis. Primary closure is now preferred."}
]

QUESTIONS["Hepatic Resection"] = [
    {"question": "The hepatic sinusoidal endothelium derives from which embryologic venous system?",
     "answer": "The vitelline (omphalomesenteric) veins. Hepatic cords from foregut endoderm interdigitate with the vitelline vein plexus forming sinusoids. The portal vein is a vitelline vein remnant — this dual origin explains the liver's dual blood supply from its earliest development."},
    {"question": "Describe the Couinaud segmental anatomy — what defines each of the 8 segments?",
     "answer": "Each segment has its own portal pedicle (portal vein, hepatic artery, bile duct) and hepatic venous drainage. Right hepatic vein separates segments 6/7 from 5/8. Middle hepatic vein separates right from left lobe. Left hepatic vein separates segment 4 from 2/3. Segment 1 (caudate) has independent IVC drainage. Cantlie's line (gallbladder fossa to IVC) divides right from left."},
    {"question": "What is the most common hepatic arterial variant relevant to liver resection?",
     "answer": "Replaced right hepatic artery from SMA (10-15%), coursing posterior to the portal vein through the portacaval space. A replaced left hepatic artery from the left gastric artery (10%) runs in the gastrohepatic ligament. Failure to identify these risks inadvertent ligation and hepatic lobe ischemia."},
    {"question": "What is post-hepatectomy liver failure, and how do you predict adequate future liver remnant?",
     "answer": "PHLF: INR >1.7 and bilirubin >3.0 on POD5 (ISGLS). Minimum FLR: >20% (normal liver), >30% (chemotherapy-treated), >40% (cirrhotic) — measured by CT volumetry. If insufficient: portal vein embolization (PVE, 4-6 weeks to hypertrophy), ALPPS (faster but higher morbidity), or staged hepatectomy."},
    {"question": "What is the Pringle maneuver, and what is its safe duration?",
     "answer": "Clamping the hepatoduodenal ligament to occlude hepatic artery and portal vein inflow. Safe for 15-20 minutes continuous (up to 60-120 minutes intermittent: 15 on/5 off). Does NOT control hepatic vein back-bleeding — maintain low CVP (<5 cmH2O) to reduce venous hemorrhage during parenchymal transection."}
]

QUESTIONS["Pancreaticoduodenectomy (Whipple)"] = [
    {"question": "The pancreatic head and duodenum share blood supply because they share embryologic origin. From which foregut buds does the pancreas develop?",
     "answer": "Ventral pancreatic bud (becomes uncinate process and inferior head, rotates posteriorly) and dorsal pancreatic bud (becomes body, tail, and superior head). They fuse at week 7. The shared pancreaticoduodenal arcades make en bloc resection mandatory."},
    {"question": "Name the six structures divided during a classic Whipple procedure.",
     "answer": "1) Common hepatic/bile duct, 2) Stomach at antrum (or duodenum if pylorus-preserving), 3) Pancreatic neck, 4) Proximal jejunum (10-15cm distal to Treitz), 5) Gastroduodenal artery, 6) Uncinate process attachments along SMA/SMV."},
    {"question": "What are the anterior and posterior pancreaticoduodenal arcades and their parent vessels?",
     "answer": "Anterior: anterior superior PDA (from GDA) anastomoses with anterior inferior PDA (from SMA/first jejunal branch). Posterior: posterior superior PDA (from GDA) anastomoses with posterior inferior PDA (from SMA). These arcades are divided during resection."},
    {"question": "What is the most common cause of morbidity after Whipple, and how is it graded?",
     "answer": "Pancreatic fistula (15-30%). ISGPF grading: Grade A (biochemical leak, drain amylase >3x serum on POD3), Grade B (requires management change — drainage, antibiotics), Grade C (organ failure, reoperation, death). Risk factors: soft gland, small duct (<3mm), high EBL."},
    {"question": "What is the SMA margin, and why is it the most critical margin in pancreatic head cancer?",
     "answer": "The retroperitoneal/uncinate margin along the right lateral SMA. Most frequently positive (R1) because tumors abut the SMA adventitia. A positive SMA margin significantly worsens survival. The 'artery-first' approach dissects the SMA early to assess resectability before committing to reconstruction."}
]

QUESTIONS["Distal Pancreatectomy"] = [
    {"question": "The body and tail of the pancreas develop from which embryologic bud, and what marks the junction with the head?",
     "answer": "The dorsal pancreatic bud. The junction is at the pancreatic neck, which overlies the SMV/portal vein confluence. The duct of Wirsung forms from fusion of the ventral duct with the distal dorsal duct."},
    {"question": "What is the relationship of the splenic vein to the pancreatic body/tail during distal pancreatectomy?",
     "answer": "The splenic vein runs along the posterior surface of the pancreatic body/tail, receiving multiple short, fragile pancreatic tributaries. Avulsion of these tributaries during mobilization causes hemorrhage. This intimate relationship is why splenectomy typically accompanies distal pancreatectomy for cancer."},
    {"question": "What is the Warshaw versus Kimura technique for spleen-preserving distal pancreatectomy?",
     "answer": "Kimura: preserves splenic artery and vein by ligating each pancreatic branch — technically demanding, maintains normal perfusion. Warshaw: sacrifices splenic vessels, relying on short gastric and gastroepiploic collaterals. Warshaw has 15-25% splenic infarction/abscess rate."},
    {"question": "What is the pancreatic fistula rate after distal pancreatectomy, and what predicts it?",
     "answer": "20-30% (higher than Whipple). The stump is the source — soft gland texture, small duct, and BMI >30 are risk factors. Stapler transection versus hand-sewn closure show equivalent fistula rates (DISPACT trial). Stump reinforcement with falciform patch or fibrin sealant may help."},
    {"question": "What is RAMPS and what is its oncologic advantage for left-sided pancreatic cancer?",
     "answer": "Radical Antegrade Modular Pancreatosplenectomy: standardized lymphadenectomy along celiac, splenic, and SMA axes with posterior dissection anterior or posterior to the left adrenal. Improves R0 rates to >80% (vs 50-70% standard) and lymph node yield. Posterior RAMPS used when posterior invasion is suspected."}
]

QUESTIONS["ERCP with Sphincterotomy"] = [
    {"question": "The sphincter of Oddi develops from mesenchyme surrounding the ampulla. What is its normal resting pressure relative to CBD pressure?",
     "answer": "Sphincter: 10-15 mmHg above duodenal pressure. CBD: 5-10 mmHg. The sphincter has phasic contractions (2-6/min). SOD is diagnosed when basal pressure exceeds 40 mmHg on manometry."},
    {"question": "Where is the major papilla located in the duodenum, and what landmark helps identify it?",
     "answer": "Posteromedial wall of D2, at the junction of middle and distal third. Identified by the longitudinal duodenal fold (plica longitudinalis) and a nipple-like protrusion. The minor papilla (Santorini) is 2cm proximal and anterior."},
    {"question": "Why is sphincterotomy made between 11 and 1 o'clock, and what vessel is at risk?",
     "answer": "The posterior superior pancreaticoduodenal artery runs behind the ampulla at ~11 o'clock. Cutting in this direction avoids the vessel, but anatomic variation can place it in the cut zone. Post-sphincterotomy bleeding occurs in 1-2%."},
    {"question": "What is post-ERCP pancreatitis, and how is it prevented?",
     "answer": "Incidence 3-7%, up to 15% in high-risk patients. Prevention: 1) Rectal indomethacin 100mg (NEJM 2012), 2) Prophylactic pancreatic duct stent, 3) Aggressive IV LR hydration, 4) Wire-guided cannulation. Risk factors: young female, SOD, difficult cannulation, pancreatic duct injection, precut."},
    {"question": "What is a precut sphincterotomy, and when should you consider it?",
     "answer": "A technique for biliary access when standard cannulation fails (>5-10 min or >5 PD cannulations). Options: needle-knife fistulotomy, needle-knife precut, or transpancreatic sphincterotomy. Increases perforation and PEP risk. Early precut is now preferred over prolonged traumatic cannulation attempts."}
]

# ============================================================
# COLORECTAL
# ============================================================

QUESTIONS["Laparoscopic Appendectomy"] = [
    {"question": "The appendix derives from which embryologic gut division, and how does midgut malrotation affect appendiceal position?",
     "answer": "Midgut. The midgut undergoes 270-degree counterclockwise rotation around the SMA. Incomplete rotation (malrotation) places the appendix in the left upper quadrant, causing atypical appendicitis presentation."},
    {"question": "What is the most common position of the appendix, and which position mimics urologic pathology?",
     "answer": "Retrocecal (65%). Pelvic appendix mimics UTI or gynecologic pathology; retrocecal can cause flank pain mimicking renal colic. The tip position determines symptom presentation."},
    {"question": "The appendicular artery is a branch of what vessel, and what makes it clinically significant?",
     "answer": "Branch of the ileocolic artery (from SMA). It is an end artery running in the free edge of the mesoappendix — thrombosis causes gangrenous appendicitis, and inadequate ligation causes hemorrhage, the most common reason for re-operation."},
    {"question": "What is stump appendicitis and how do you prevent it?",
     "answer": "Recurrent appendicitis from a retained appendiceal stump >0.5cm. Prevented by complete transection at the cecal base. Occurs in 1/50,000 cases, more common after laparoscopic approach where the base may not be fully visualized."},
    {"question": "What does the CODA trial (2020, NEJM) show about antibiotics versus surgery for appendicitis?",
     "answer": "Antibiotics alone were non-inferior to surgery for uncomplicated appendicitis but had 29% crossover to surgery by 90 days. Appendicolith on CT predicted failure of antibiotic therapy. For complicated appendicitis (phlegmon/abscess), drainage + antibiotics with consideration of interval appendectomy remains standard."}
]

QUESTIONS["Open Appendectomy"] = [
    {"question": "At what gestational age does the appendix first become recognizable as a cecal diverticulum?",
     "answer": "The appendix appears as a diverticulum of the cecal bud at week 8, from the caudal limb of the midgut loop (post-arterial segment), becoming clearly recognizable by week 12 of development."},
    {"question": "Describe McBurney's point and all the layers encountered in a McBurney muscle-splitting incision.",
     "answer": "McBurney's point: junction of lateral and middle thirds of a line from ASIS to umbilicus. Layers: skin, Scarpa's fascia, external oblique aponeurosis (split along fibers), internal oblique (split), transversus abdominis (split), transversalis fascia, preperitoneal fat, peritoneum."},
    {"question": "The appendicular artery is an end artery. What is the clinical consequence of this?",
     "answer": "Thrombosis of the appendicular artery (from inflammation or fecalith obstruction) causes gangrenous appendicitis because there are no collateral vessels. This is why appendicitis progresses to gangrene and perforation rather than resolving — the vascular anatomy seals its fate."},
    {"question": "What is the wound complication rate in open appendectomy for perforated appendicitis, and how do you reduce it?",
     "answer": "SSI rate 10-20% for perforated cases. Reduced by leaving the skin open for delayed primary closure (DPC) at day 4-5 if wound is clean. DPC reduces SSI from 20% to <5% in contaminated cases."},
    {"question": "What is the Alvarado score and its clinical utility?",
     "answer": "A clinical scoring system: Migration of pain (1), Anorexia (1), Nausea (1), RLQ tenderness (2), Rebound (1), Elevation of temp (1), Leukocytosis (2), Shift to left (1). Score ≥7 strongly suggests appendicitis. <5 effectively rules it out. It reduces unnecessary imaging and guides surgical decision-making in resource-limited settings."}
]

QUESTIONS["Laparoscopic Ileocecectomy"] = [
    {"question": "The ileocecal valve develops at the junction of midgut and hindgut. What controls its competence?",
     "answer": "Thickening of the circular smooth muscle layer at the ileocecal junction. An incompetent valve (seen in ~15% of adults) allows colonic reflux into the ileum and can cause small bowel bacterial overgrowth."},
    {"question": "What is the bloodless fold of Treves and how does it guide ileocecal mobilization?",
     "answer": "An avascular peritoneal fold between the terminal ileum and base of the appendix/cecum. It serves as a reliable landmark to identify the appendix and begin medial-to-lateral mobilization of the ileocecal region."},
    {"question": "Which named vessel must be ligated at its origin for oncologic ileocecectomy?",
     "answer": "The ileocolic artery — the most constant branch of the SMA. It must be ligated at its SMA origin to ensure adequate lymph node harvest along the entire ileocolic pedicle."},
    {"question": "What factors increase the risk of ileocecal anastomotic leak?",
     "answer": "Tension on anastomosis, malnutrition (albumin <3.0), emergency surgery, immunosuppression (especially steroids in Crohn's), and inadequate blood supply to the staple line. Leak causes fecal peritonitis with mortality up to 10-15%."},
    {"question": "In Crohn's disease, what is the recommended resection margin and why is radical resection contraindicated?",
     "answer": "Grossly normal margins (2cm from visible disease). Microscopic positive margins do NOT increase recurrence. Radical resection wastes small bowel risking short gut syndrome — Crohn's recurs at the anastomosis regardless of margin status."}
]

QUESTIONS["Laparoscopic Right Hemicolectomy"] = [
    {"question": "The right colon derives from midgut. What is Griffiths' point and what arterial watershed does it represent?",
     "answer": "The watershed area near the splenic flexure where SMA territory (midgut) meets IMA territory (hindgut). The marginal artery may be absent here in 5% of patients, making the splenic flexure vulnerable to ischemia."},
    {"question": "During medial-to-lateral mobilization, what is the 'holy plane' and what structures lie posterior to it?",
     "answer": "The avascular embryologic fusion plane between the mesocolon and Gerota's fascia. Posterior structures at risk: right ureter, gonadal vessels, duodenum (C-loop), and right kidney. The duodenum is the most commonly injured structure."},
    {"question": "Name the three arteries ligated during standard right hemicolectomy.",
     "answer": "1) Ileocolic artery (from SMA), 2) Right colic artery (from SMA — absent in 10-20%), 3) Right branch of middle colic artery (from SMA). All SMA branches confirm the midgut origin."},
    {"question": "What is the 'ring of death' in a stapled ileocolic anastomosis?",
     "answer": "The circle of staples at a side-to-side functional end-to-end anastomosis. If the crotch (apex) of the staple lines is ischemic, it leaks at this weakest point. This is the most common cause of early anastomotic failure."},
    {"question": "What is complete mesocolic excision (CME), and what evidence supports it?",
     "answer": "Sharp dissection of the visceral mesocolic fascia from the parietal plane with central vascular ligation — analogous to TME for rectal cancer. Hohenberger's data showed ~15% improvement in 5-year survival and higher lymph node yield. Becoming standard for colon cancer."}
]

QUESTIONS["Open Right Hemicolectomy"] = [
    {"question": "Why does the ascending colon lack a mesentery while the transverse colon retains one?",
     "answer": "During midgut rotation, the ascending colon's mesentery fuses with the posterior body wall (Toldt's fusion fascia), making it retroperitoneal. The transverse colon retains its dorsal mesentery (transverse mesocolon) because it doesn't fuse posteriorly."},
    {"question": "During a Kocher maneuver for right hemicolectomy, what structures are at risk?",
     "answer": "IVC (directly posterior to D2/D3), right gonadal vein, right ureter, and the pancreatic head. The Kocher mobilizes the duodenum and pancreatic head medially off the retroperitoneum."},
    {"question": "Where is the marginal artery of Drummond most tenuous near the right colon?",
     "answer": "Near the cecum (between ileocolic and right colic arteries) and at the splenic flexure. These gaps are relevant for ensuring adequate blood supply to the anastomosis after right hemicolectomy."},
    {"question": "What is the risk of internal hernia through the mesenteric defect after right hemicolectomy?",
     "answer": "Small bowel can herniate through the ileocolic mesenteric defect causing obstruction. Prevention: close the defect with running absorbable suture, though debate exists on whether closure increases stricture risk."},
    {"question": "What is the Turnbull 'no-touch' technique?",
     "answer": "Early ligation of the vascular pedicle and lymphatic drainage before tumor manipulation, to prevent intraoperative tumor cell dissemination. Turnbull's data from Cleveland Clinic showed improved survival, though modern RCTs haven't confirmed benefit. Many surgeons still practice early pedicle ligation."}
]

QUESTIONS["Robotic Right Hemicolectomy"] = [
    {"question": "The hepatic flexure is tethered by which peritoneal attachments, and what is their embryologic origin?",
     "answer": "Hepatocolic, nephrocolic, and duodenocolic ligaments — remnants of dorsal mesentery fusion with the retroperitoneum (Toldt's fascia). The hepatocolic ligament often contains an accessory right colic vein that bleeds if torn."},
    {"question": "What is the 'SMV-first' approach in robotic right hemicolectomy?",
     "answer": "Identifying the SMV at the inferior pancreatic border as the first step of medial dissection. The ileocolic pedicle is traced to its SMV/SMA origin for high ligation — the SMV serves as the medial boundary of dissection for complete mesocolic excision."},
    {"question": "What is the gastrocolic trunk of Henle and why is it dangerous during robotic right hemicolectomy?",
     "answer": "A short trunk (1-2cm) formed by the right gastroepiploic vein, right colic vein, and/or anterior SPDV draining into the SMV behind the pancreas. It's thin-walled — avulsion from the SMV causes major venous hemorrhage extremely difficult to control robotically."},
    {"question": "What complication is more commonly reported with intracorporeal versus extracorporeal anastomosis?",
     "answer": "Staple line bleeding from the intracorporeally-sewn common enterotomy. However, intracorporeal anastomosis has lower incisional hernia rates, less narcotic use, and faster return of bowel function due to reduced mesenteric twist."},
    {"question": "What is a D3 lymph node dissection in right colon cancer?",
     "answer": "Dissection of nodes along the surgical trunk (feeding vessel origins from SMA/SMV), adding nodes at the ileocolic and right colic pedicle roots. Japanese data suggests improved staging and possible survival benefit. It is integral to CME and facilitated by robotic magnification."}
]

QUESTIONS["Extended Right Hemicolectomy"] = [
    {"question": "The splenic flexure is the junction of midgut and hindgut. What two different parasympathetic nerve supplies meet here?",
     "answer": "Midgut: vagus nerve. Hindgut: pelvic splanchnic nerves (S2-S4). This dual autonomic supply mirrors the dual arterial watershed (SMA/IMA) at this embryologic junction."},
    {"question": "What specific ligament must be divided to mobilize the splenic flexure, and what organ is most at risk?",
     "answer": "Splenocolic ligament. The spleen is at greatest risk — traction injury to the splenic capsule can cause hemorrhage requiring splenectomy. Iatrogenic splenic injury incidence: 1-8% during splenic flexure mobilization."},
    {"question": "In extended right hemicolectomy, the middle colic artery is ligated. What becomes the sole blood supply to the remaining descending colon?",
     "answer": "The left colic artery (from IMA) via the marginal artery. If Griffiths' point is deficient, the proximal descending colon may be ischemic. Always assess for pulsatile bleeding at the cut edge and consider ICG fluorescence."},
    {"question": "What specific risk does the ileodescending anastomosis carry compared to a standard ileocolic anastomosis?",
     "answer": "Higher ischemic risk because the descending colon depends solely on IMA flow after middle colic ligation. The descending colon also has a less robust submucosal plexus than the ileum. Leak rates are higher if the marginal artery at Griffiths' point is tenuous."},
    {"question": "When is extended right hemicolectomy indicated over standard right for a hepatic flexure cancer?",
     "answer": "Cancers at the hepatic flexure or proximal transverse colon require extended resection to include the middle colic artery pedicle and its lymphatic basin. The oncologic principle: resection must include the primary feeding vessel and all draining nodes to its origin."}
]

QUESTIONS["Laparoscopic Left Colectomy"] = [
    {"question": "The left colon derives from hindgut. How does its blood supply differ from the midgut-derived right colon?",
     "answer": "The IMA has fewer named branches and a less robust marginal artery than the SMA system, making the left colon more vulnerable to ischemia. The IMA gives off the left colic, sigmoid arteries, and terminates as the superior rectal artery."},
    {"question": "In medial-to-lateral left colectomy, what is the first structure identified?",
     "answer": "The IMA at its aortic origin, just below D3/D4 junction. The left ureter and gonadal vessels are identified posterior to the IMA pedicle before ligation. The IMV is identified separately running along the ligament of Treitz."},
    {"question": "Where are the left ureter and IMA closest, and why is this the #1 site of ureteral injury?",
     "answer": "The left ureter crosses posterior to the IMA at the pelvic brim near the common iliac artery bifurcation. It can be tented up with the IMA pedicle during ligation — always visualize the ureter peristalsing before dividing the pedicle."},
    {"question": "What are Griffiths' point and Sudeck's point, and why do they matter in left colectomy?",
     "answer": "Griffiths' point: splenic flexure watershed between middle colic (SMA) and left colic (IMA) — marginal artery absent in 5%. Sudeck's critical point: last sigmoid artery before superior rectal artery — ligation below this risks rectal stump ischemia. Both predict anastomotic blood supply."},
    {"question": "In left colectomy for diverticular disease, where should the distal margin be and why?",
     "answer": "On the upper rectum (below sacral promontory), NOT the distal sigmoid. The sigmoid has the same structural deficiency (thickened taenia, high pressure) that caused diverticulosis. Sigmoid-to-sigmoid anastomosis has recurrence up to 12% versus <3% for colorectal."}
]

QUESTIONS["Extended Left Colectomy"] = [
    {"question": "How does the embryologic fusion plane (Toldt's fascia) facilitate extended left colectomy?",
     "answer": "The avascular fusion plane between descending mesocolon and Gerota's fascia can be developed bluntly, allowing rapid mobilization of the entire left colon while protecting the ureter, gonadal vessels, and kidney posteriorly."},
    {"question": "After dividing both the middle colic left branch and IMA, what remains to supply the anastomosis?",
     "answer": "The right branch of middle colic (for the proximal transverse colon) and superior rectal artery (for the rectal stump). ICG angiography is highly valuable to confirm adequate perfusion at both ends."},
    {"question": "What is the arc of Riolan, and when is it most clinically relevant?",
     "answer": "A large, inconsistent arterial anastomosis connecting SMA and IMA through the mesentery base. Most developed when one system is chronically stenotic. Ligating it in such patients can cause catastrophic ischemia of remaining colon."},
    {"question": "What causes the higher leak rate (8-12%) at the transverse colon-to-rectal anastomosis?",
     "answer": "The long mesenteric reach required — the transverse colon must reach the pelvis without tension. This requires full hepatic flexure mobilization and often middle colic artery division, creating a dual risk of tension and ischemia."},
    {"question": "When is extended left colectomy preferred over subtotal colectomy for obstructing left colon cancer?",
     "answer": "When the proximal colon is not significantly dilated and is viable. If the cecum is dilated >12cm, thin-walled, or questionably viable, subtotal colectomy with ileorectal anastomosis is safer. Extended left colectomy preserves the ileocecal valve, reducing chronic diarrhea."}
]

QUESTIONS["Laparoscopic Sigmoid Colectomy"] = [
    {"question": "The sigmoid has a true mesentery unlike the descending colon. What embryologic event explains this?",
     "answer": "The sigmoid retains its dorsal mesentery because it does not fuse with the posterior abdominal wall during development. The descending colon's mesentery fuses (Toldt's fascia), making it retroperitoneal, while the sigmoid remains intraperitoneal and mobile."},
    {"question": "Before dividing the IMA pedicle, what three structures must you identify as your 'critical view'?",
     "answer": "1) Left ureter (confirm peristalsis), 2) Left gonadal vessels sweeping posteriorly, 3) Hypogastric nerve plexus (presacral nerves) posterior to the IMA. Failure to identify these leads to ureteral injury or sexual/bladder dysfunction."},
    {"question": "Should the IMA be ligated high (at aorta) or low (preserving left colic artery) for sigmoid cancer?",
     "answer": "For cancer: high ligation for lymph node yield. For diverticulitis: preserving the left colic artery is acceptable. The HIGHLOW trial (2023) showed no difference in node yield or oncologic outcomes, so the debate continues."},
    {"question": "What are the hypogastric nerves, and what happens if they're injured during sigmoid mobilization?",
     "answer": "The superior hypogastric plexus runs over the sacral promontory, bifurcating into left and right hypogastric nerves. Injury causes retrograde ejaculation and bladder dysfunction in men, and sexual/bladder dysfunction in women."},
    {"question": "What is the Hinchey classification for complicated diverticulitis and how does it guide surgery?",
     "answer": "I: pericolic abscess (antibiotics ± drainage). II: pelvic abscess (percutaneous drainage). III: purulent peritonitis (resection ± anastomosis, or laparoscopic lavage per LOLA/SCANDIV). IV: fecal peritonitis (Hartmann's or resection with diversion). The LADIES trial showed lavage was non-inferior to resection for Hinchey III."}
]

QUESTIONS["Open Sigmoid Colectomy"] = [
    {"question": "A long sigmoid mesocolon with a narrow base predisposes to what condition, and what populations are at highest risk?",
     "answer": "Sigmoid volvulus — variable dorsal mesentery retention creates a redundant sigmoid on a narrow pedicle. Most common in high-fiber diet populations (longer colons), elderly, and neuropsychiatric patients with chronic constipation (especially institutionalized)."},
    {"question": "When you enter the peritoneal reflection at the 'white line of Toldt,' what anatomic layer are you dissecting?",
     "answer": "The avascular fusion plane between visceral peritoneum of the sigmoid mesocolon and parietal peritoneum overlying the retroperitoneum. This is the lateral-to-medial equivalent of the embryologic plane used in medial-to-lateral approaches."},
    {"question": "How many sigmoid arteries typically exist, and what is Sudeck's critical point?",
     "answer": "2-4 branches from the IMA between the left colic and superior rectal arteries. Sudeck's critical point is the last sigmoid branch before the superior rectal artery — its preservation determines rectal stump blood supply."},
    {"question": "What percentage of Hartmann's patients never get reversed, and what predicts permanent stoma?",
     "answer": "30-50% never undergo reversal. Predictors: age >70, ASA III-IV, malignancy, Hinchey IV, complications from index operation. Reversal carries 4-16% leak rate and 15-25% morbidity."},
    {"question": "For sigmoid volvulus, what success rate does endoscopic decompression achieve and what mandates urgent surgery?",
     "answer": "Decompression succeeds in 60-80% but recurrence is 40-60%. Urgent surgery is mandated by: mucosal necrosis on endoscopy, perforation, peritonitis, or failed decompression. Gangrenous sigmoid requires resection without decompression attempt."}
]

QUESTIONS["Robotic Sigmoid Colectomy"] = [
    {"question": "Why is the IMV's relationship to the ligament of Treitz important during robotic sigmoid colectomy?",
     "answer": "The IMV runs along the left side of the ligament of Treitz before joining the splenic vein behind the pancreas. During IMA ligation, the IMV may need separate division — its injury near the pancreas causes difficult-to-control retroperitoneal hemorrhage."},
    {"question": "What is the anatomic relationship between the sigmoid colon and the left gonadal vessels?",
     "answer": "The gonadal vessels descend retroperitoneally from the mesonephric ridge, passing posterior to the sigmoid mesocolon. During robotic medial-to-lateral dissection, 3D magnification allows precise identification before inadvertent division."},
    {"question": "The superior rectal artery is the terminal branch of what vessel?",
     "answer": "The IMA — it continues as the superior rectal artery after the last sigmoid branch. Rectal stump perfusion after IMA ligation depends on middle rectal arteries (from internal iliac) and inferior rectal arteries (from internal pudendal)."},
    {"question": "What is the specific advantage of the robotic platform for low pelvic dissection in sigmoid colectomy?",
     "answer": "Wristed instruments allow precise dissection in the narrow pelvis, better visualization of autonomic nerves (hypogastric and pelvic splanchnic), and ergonomic stapler placement. This translates to lower conversion rates and potentially lower genitourinary dysfunction."},
    {"question": "What are the five requirements for a safe colorectal anastomosis before firing the circular stapler?",
     "answer": "1) No tension, 2) Adequate blood supply (ICG or bleeding), 3) Complete donuts, 4) Negative air leak test (proctoscopy with insufflation under saline), 5) Well-perfused, non-irradiated tissue. Incomplete donuts mandate re-stapling or hand-sewn reinforcement."}
]

QUESTIONS["Laparoscopic Low Anterior Resection"] = [
    {"question": "The rectum develops from which portion of the cloaca, and what separates it from the urogenital sinus?",
     "answer": "The dorsal hindgut cloaca. The urorectal septum (Tourneaux and Rathke folds) separates rectum posteriorly from the urogenital sinus anteriorly by week 7. Failure causes persistent cloaca or rectourethral/rectovaginal fistulae."},
    {"question": "What defines the TME dissection plane, and what is the 'holy plane' of Heald?",
     "answer": "TME follows the areolar plane between the visceral mesorectal fascia (encasing rectum and lymphovascular supply) and parietal presacral fascia (Waldeyer's). The 'holy plane' is entered behind the superior rectal artery — staying here avoids presacral venous hemorrhage and nerve injury."},
    {"question": "What are the three 'columns' of rectal blood supply, and which is sacrificed in LAR?",
     "answer": "Superior rectal (from IMA) — sacrificed. Middle rectal (from internal iliac) — preserved, supplies mid-rectum. Inferior rectal (from internal pudendal) — preserved, supplies anal canal. The stump depends on middle and inferior rectal arteries after IMA ligation."},
    {"question": "What is LARS (low anterior resection syndrome) and what is its incidence?",
     "answer": "Disordered bowel function: urgency, frequency, clustering, incontinence, incomplete evacuation. Affects 50-90% after ultralow LAR. Results from loss of rectal reservoir, nerve injury, and sphincter dysfunction. LARS score quantifies severity. J-pouch or coloplasty can reduce symptoms."},
    {"question": "What does the RAPIDO trial (2021) show about neoadjuvant therapy for rectal cancer?",
     "answer": "Short-course radiation (5x5 Gy) followed by chemotherapy then TME showed lower disease-related treatment failure and higher pCR versus standard long-course chemoradiation. TNT (total neoadjuvant therapy) is now preferred for locally advanced rectal cancer, with watch-and-wait for complete responders."}
]

QUESTIONS["Open Low Anterior Resection"] = [
    {"question": "What is Waldeyer's fascia, and where does it attach?",
     "answer": "The rectosacral fascia — a condensation of presacral endopelvic fascia extending from S2-S4 to the posterior mesorectum at the anorectal junction. It must be divided sharply during posterior TME to enter the presacral space."},
    {"question": "What is Denonvilliers' fascia, and what happens if you dissect anterior versus posterior to it?",
     "answer": "A fascial plane between rectum and prostate/seminal vesicles (or vagina). Anterior dissection risks neurovascular bundles and prostate. Posterior dissection (closer to rectum) is oncologically appropriate for anterior tumors and preserves autonomic nerves."},
    {"question": "What is the presacral venous plexus, and how do you manage catastrophic hemorrhage from it?",
     "answer": "A valveless plexus (Batson's) communicating with internal vertebral veins, directly on sacral periosteum. Veins retract into foramina and can't be sutured. Management: direct pressure/packing, thumbtack into sacral foramen, oxidized cellulose, or muscle fragment welding."},
    {"question": "What is the leak rate after open LAR, and what are the consequences of a pelvic anastomotic leak?",
     "answer": "5-15% (higher for ultralow). Consequences: pelvic sepsis, need for diversion (25% permanent stoma), increased local recurrence, and long-term pelvic fibrosis with poor functional outcomes. A pelvic leak has significantly worse oncologic outcomes."},
    {"question": "What are the indications for a diverting loop ileostomy in LAR?",
     "answer": "Anastomosis ≤6cm from anal verge, neoadjuvant radiation, male pelvis, positive air leak test, technical difficulty, tension or questionable blood supply, immunosuppression. The ileostomy is reversed at 8-12 weeks after confirming integrity with contrast enema."}
]

QUESTIONS["Robotic Low Anterior Resection"] = [
    {"question": "What is the 'lateral ligament' of the rectum, and what critical nerve runs within it?",
     "answer": "A condensation of endopelvic fascia from the lateral pelvic sidewall to the mesorectum. It contains the pelvic splanchnic nerves (nervi erigentes, S2-S4). Overzealous division causes parasympathetic nerve injury leading to bladder and sexual dysfunction."},
    {"question": "What advantage does the robot offer for autonomic nerve preservation during TME?",
     "answer": "Wristed instruments and 10x 3D visualization allow precise identification of hypogastric nerves at the IMA origin, the hypogastric plexus over the promontory, and pelvic splanchnic nerves at the sidewall. ROLARR subanalysis suggests lower genitourinary dysfunction rates."},
    {"question": "How do you confirm adequate blood supply to the rectal stump after IMA ligation robotically?",
     "answer": "ICG (indocyanine green) fluorescence angiography via the Firefly system on the da Vinci — shows real-time perfusion. The rectal stump is supplied by middle rectal arteries (present in ~50%) and inferior rectal arteries from the internal pudendal system."},
    {"question": "What were the key findings of the ROLARR trial (2017, JAMA)?",
     "answer": "Robotic vs laparoscopic rectal resection: no significant overall difference in conversion to open. However, robotic had significantly lower conversion rates in male and obese patients with narrow pelvis. No differences in oncologic outcomes, complications, or QOL at 6 months."},
    {"question": "What is the 'watch and wait' protocol for rectal cancer?",
     "answer": "For patients achieving clinical complete response after neoadjuvant chemoradiation, close surveillance replaces surgery. The International Watch & Wait Database shows 75-80% sustained cCR at 2 years. Regrowth is mostly luminal and salvageable surgically. Preserves rectum, avoids stoma, maintains quality of life."}
]

QUESTIONS["Hartmann Procedure"] = [
    {"question": "Henri Hartmann originally described this procedure in 1921 for which pathology?",
     "answer": "Obstructing rectal cancer — not diverticulitis, which is its most common indication today. It was designed for situations where primary anastomosis was too risky."},
    {"question": "Where should the rectal stump be divided, and how do you mark it for future reversal?",
     "answer": "At the rectosigmoid junction (sacral promontory level). Mark the stump with a long non-absorbable suture tacked to the anterior abdominal wall for identification at reversal. Staple (not oversew) and leave it long enough for re-anastomosis."},
    {"question": "What causes Hartmann stump blowout?",
     "answer": "Ischemia of the staple line (too distal division or excessive devascularization), retained fecal material below the staple line, or ongoing sepsis. The stump's blood supply depends on middle and inferior rectal arteries. It presents as pelvic sepsis requiring washout and revision."},
    {"question": "What percentage of Hartmann patients eventually undergo reversal?",
     "answer": "Only 40-60%. Predictors of permanent stoma: age >70, ASA III-IV, malignancy, Hinchey IV, complications from index operation. Reversal carries 4-16% leak rate and 15-25% overall morbidity."},
    {"question": "What is the evidence for primary anastomosis versus Hartmann's in perforated diverticulitis?",
     "answer": "DIVERTI and LADIES trials: primary anastomosis with diverting ileostomy had lower morbidity, comparable mortality, and higher stoma reversal rates (70-80% vs 40-60%) than Hartmann's. Primary anastomosis is now preferred in hemodynamically stable Hinchey III patients."}
]

QUESTIONS["Total Abdominal Colectomy"] = [
    {"question": "Total abdominal colectomy removes tissue from which two embryologic gut divisions?",
     "answer": "Midgut (cecum through proximal 2/3 transverse, SMA-supplied) and hindgut (distal 1/3 transverse through sigmoid, IMA-supplied). The watershed is at the splenic flexure."},
    {"question": "When ligating the IMA, what structure's relationship to the IMA origin must you identify?",
     "answer": "The left ureter — it crosses the common iliac near the IMA origin and can be tented up with the pedicle. Also, the superior hypogastric nerve plexus lies directly posterior to the IMA at the aortic bifurcation."},
    {"question": "Both SMA branches and the IMA are divided during total colectomy. What maintains blood supply to the ileorectal anastomosis?",
     "answer": "The ileal side: SMA via jejunal/ileal branches. The rectal side: middle and inferior rectal arteries from the internal iliac. The marginal artery is entirely removed with the specimen."},
    {"question": "In fulminant C. difficile colitis, what intraoperative finding mandates colectomy over loop ileostomy with lavage?",
     "answer": "Full-thickness colonic necrosis, perforation, or megacolon. The 2011 Pittsburgh study (Neal et al.) showed diverting loop ileostomy with intraoperative colonic vancomycin lavage reduced mortality from 50% to 19% in patients WITHOUT perforation or necrosis."},
    {"question": "After total colectomy with ileorectal anastomosis, what is the expected stool frequency?",
     "answer": "4-6 loose bowel movements per day with clustering. Managed with fiber, loperamide, and dietary modification. Most patients adapt over 6-12 months but never achieve normal formed stools. Warn about nocturnal urgency and perianal skin irritation."}
]

QUESTIONS["Abdominoperineal Resection"] = [
    {"question": "The anal canal below the dentate line develops from what embryologic structure?",
     "answer": "Ectoderm of the proctodeum. Below the dentate, lymphatic drainage goes to inguinal nodes (not mesenteric), and tumors have squamous histology. This dual embryologic origin explains the different tumor biology and spread patterns of low rectal/anal cancers."},
    {"question": "What is the 'cylindrical APR' technique described by Holm, and how does it differ from traditional APR?",
     "answer": "Wider perineal excision with levator muscles divided from below, creating a cylinder rather than a 'waist' at the levator level. Traditional APR narrows at the levators (highest CRM+ rate area). Holm's technique reduces CRM+ from 40% to <15%."},
    {"question": "What is the blood supply to the perineum during the perineal phase of APR?",
     "answer": "Inferior rectal arteries (from internal pudendal, branch of internal iliac), middle rectal arteries (internal iliac), and perineal branch of internal pudendal. The presacral venous plexus (Batson's) is the most dangerous hemorrhage risk posteriorly."},
    {"question": "What is the perineal wound complication rate after APR, and what is the biggest risk factor?",
     "answer": "25-50% (delayed healing, wound breakdown, abscess, sinus, perineal hernia). Neoadjuvant radiation is the single biggest risk factor. Many surgeons use VRAM or gracilis myocutaneous flaps for irradiated perineal wounds."},
    {"question": "What is the current role of APR given sphincter-sparing approaches?",
     "answer": "Reserved for tumors invading external sphincter/levators, tumors within 1-2cm of anal verge where distal margin is impossible, pre-existing incontinence, or failed watch-and-wait with sphincter-involving regrowth. APR has decreased from 40% to <10% of rectal cancer resections."}
]

QUESTIONS["Robotic Abdominoperineal Resection"] = [
    {"question": "What anatomic landmark does the puborectalis muscle create, and why is its complete excision important in APR?",
     "answer": "The anorectal angle (80-110 degrees). Incomplete excision leaves tumor-bearing tissue — the 'waist' at the puborectalis/levator level is the most common site of positive CRM. Cylindrical technique excises the levators en bloc."},
    {"question": "What advantage does the robotic platform provide for APR deep pelvic dissection?",
     "answer": "Enhanced 3D visualization and articulation below the peritoneal reflection where laparoscopic instruments lose mechanical advantage. Facilitates precise dissection of Denonvilliers' fascia anteriorly, hypogastric nerve preservation laterally, and sharp Waldeyer's division posteriorly."},
    {"question": "After IMA division during APR, what maintains blood flow to the remaining pelvic structures?",
     "answer": "The internal iliac system (middle and inferior rectal arteries, internal pudendal artery). The superior rectal artery goes with the specimen. The SMA-IMA collateral is no longer relevant since the colon is divided and rectum removed."},
    {"question": "What is the incidence of perineal hernia after APR, and how is it prevented?",
     "answer": "5-10%, higher after laparoscopic/robotic APR. Prevention: close pelvic peritoneum, biologic mesh over the pelvic floor, omental pedicle flap to fill dead space, or myocutaneous flap (VRAM)."},
    {"question": "What neoadjuvant strategy should be considered for a T3N1 low rectal cancer before APR?",
     "answer": "Total neoadjuvant therapy (TNT): short-course RT (5x5 Gy) + FOLFOX/CAPOX 4-6 months, then restage. If cCR → consider watch-and-wait to potentially avoid APR. If partial/no response → APR. Goal: maximum tumor response to possibly preserve the sphincter complex."}
]

QUESTIONS["End Colostomy Creation"] = [
    {"question": "What embryologic feature makes the descending/sigmoid colon suitable for end colostomy?",
     "answer": "The descending colon is secondarily retroperitoneal (providing a natural tunnel through the abdominal wall). The sigmoid has a retained mesentery allowing it to reach the surface without tension. Both have reliable IMA blood supply."},
    {"question": "Through which layers should the colostomy trephine pass, and what is the ideal size?",
     "answer": "Skin → subcutaneous fat → anterior rectus sheath → rectus abdominis (split, not divided) → posterior rectus sheath → peritoneum. Trephine admits two fingers (~2.5-3cm). Too tight: ischemia/stenosis. Too wide: parastomal hernia."},
    {"question": "What blood supply maintains the stoma, and how do you assess for ischemia at 24 hours?",
     "answer": "Sigmoid branch of the IMA via the marginal artery. A dusky, blue-black, or pale stoma indicates ischemia. Use a transparent tube to examine mucosal color at depth — if deep mucosa is pink, it will survive. Ischemia below fascial level requires revision."},
    {"question": "What is the most common long-term complication, and what does the PREVENT trial show?",
     "answer": "Parastomal hernia (up to 50% at 5 years). Risk factors: obesity, COPD, steroids, lateral-to-rectus placement. PREVENT trial: prophylactic mesh at index operation reduces hernia incidence to ~15%."},
    {"question": "How does Brooke maturation differ for a colostomy versus an ileostomy?",
     "answer": "For ileostomies, 2-3cm eversion (Brooke technique) is essential to prevent enzyme-rich effluent from contacting skin. For colostomies, a flush or slightly raised stoma is adequate because formed stool is less caustic. Most surgeons still mature colostomies with slight eversion for easier appliance fitting."}
]

QUESTIONS["Loop Colostomy"] = [
    {"question": "Why is the transverse colon preferred for loop colostomy?",
     "answer": "The retained transverse mesocolon provides a long, mobile mesentery allowing the colon to reach the anterior abdominal wall without tension. The descending colon is retroperitoneal (fixed) and the sigmoid has variable mesentery length."},
    {"question": "What is the purpose of the supporting rod/bridge, and when is it removed?",
     "answer": "Prevents retraction of the loop into the abdomen during the first 5-10 days while adhesions form between bowel serosa and abdominal wall. Removed once adherent (7-10 days). Premature removal risks stoma retraction and peritonitis."},
    {"question": "Which limb is proximal in a loop colostomy, and how should it be oriented?",
     "answer": "The proximal (afferent) limb is positioned superiorly/cranially so stool exits into the upper appliance pouch. The distal (efferent/defunctioned) limb sits inferiorly. Incorrect orientation makes appliance management extremely difficult."},
    {"question": "What is the most common reason for loop colostomy failure to divert the fecal stream?",
     "answer": "Incomplete division of the posterior wall — the 'spur' between limbs is too low, allowing stool to pass into the distal limb. This defeats diversion. Management: revision with complete posterior wall division or conversion to end stoma."},
    {"question": "When is a loop colostomy preferred over a loop ileostomy for fecal diversion?",
     "answer": "When protecting a distal colorectal anastomosis where ileostomy effluent bypasses too much absorptive colon, obstructing distal colonic lesion needing decompression, or perianal/perineal sepsis (Fournier's). Loop ileostomy is generally preferred for temporary diversion due to easier reversal and lower parastomal hernia rates."}
]

QUESTIONS["Loop Ileostomy"] = [
    {"question": "The ileum derives from midgut. If you encounter a Meckel's diverticulum near the stoma site, what should you do?",
     "answer": "Note it but do NOT routinely resect unless symptomatic or pathologic (ectopic gastric mucosa, mass). Meckel's diverticulum (remnant of omphalomesenteric/vitelline duct) occurs 60cm from the ileocecal valve in 2% of the population. Resecting it unnecessarily complicates a straightforward diversion."},
    {"question": "Where should a loop ileostomy be sited, and what landmarks must it avoid?",
     "answer": "Through the rectus abdominis in the right lower quadrant, at the apex of the infraumbilical fat fold. Avoid: skin creases, belt line, umbilicus, bony prominences (ASIS, costal margin), previous scars, and midline incision. Preoperative stoma marking by an ET nurse is mandatory."},
    {"question": "How do you prevent mesenteric twist when creating the ileostomy?",
     "answer": "Ensure the mesentery is oriented correctly (no twists) before passing the bowel through the abdominal wall. Create an adequately sized trephine. Confirm pink viable mucosa after maturation. The blood supply is from ileal branches of the SMA via the vasa recta."},
    {"question": "At what output threshold does a high-output ileostomy become dangerous, and how do you manage it?",
     "answer": ">1500-2000 mL/day. Causes dehydration, hyponatremia, hypokalemia, hypomagnesemia, and AKI. Management: loperamide (up to 16mg/day), codeine, oral rehydration solution (NOT free water), dietary modification. Refractory: octreotide or IV fluids. Ileostomy dehydration AKI is the #1 cause of readmission after LAR."},
    {"question": "What is the complication rate of loop ileostomy reversal?",
     "answer": "15-30% morbidity including: anastomotic leak (1-3%), wound infection (5-15%), SBO (5-10% — most common readmission cause), and prolonged ileus. Timing: 8-12 weeks after index operation, after confirming anastomotic integrity with water-soluble contrast enema. Reversal rate: 70-80%."}
]

QUESTIONS["Ostomy Reversal"] = [
    {"question": "After prolonged fecal diversion, what histologic changes occur in the defunctionalized colon?",
     "answer": "Diversion colitis — mucosal atrophy, lymphoid hyperplasia, and inflammation from lack of short-chain fatty acid (SCFA) nutrition. Occurs in virtually all diverted segments. Treatment is reversal itself; SCFA enemas can temporize."},
    {"question": "What is the most dangerous step during stoma mobilization from the abdominal wall?",
     "answer": "Freeing the bowel from the posterior rectus sheath where it is most adherent. Steps: circumferential skin incision, sharp dissection to fascia, careful separation from fascial ring. Enterotomy at this point causes contamination of the wound."},
    {"question": "What determines whether you can do a local (peristomal) versus formal laparotomy reversal?",
     "answer": "Local: loop ileostomy with adequate mobility, no suspected adhesions, anastomosis feasible through the stoma site. Formal laparotomy: end stoma (Hartmann's reversal), significant adhesions, need for intra-abdominal dissection, or unidentifiable distal segment."},
    {"question": "What is the mortality of Hartmann's reversal, and what makes it so difficult?",
     "answer": "Mortality 1-4%, morbidity 25-50%. The difficulty is finding and mobilizing the short, retracted rectal stump in a scarred, often irradiated pelvis. Leak rate 4-16%. Small bowel injury during adhesiolysis occurs in 10%."},
    {"question": "What preoperative study is mandatory before any ostomy reversal with a distal anastomosis?",
     "answer": "Water-soluble contrast enema (Gastrografin, NOT barium) to confirm: 1) anastomotic integrity, 2) no stricture, 3) distal segment patency. Also endoscopy if malignancy was the original indication. Never proceed if there's a leak or significant stricture."}
]

# ============================================================
# GASTRIC / ESOPHAGEAL
# ============================================================

QUESTIONS["Total Gastrectomy"] = [
    {"question": "The stomach undergoes what embryologic rotation, and how does this explain the final vagus nerve positions?",
     "answer": "90-degree clockwise rotation on its longitudinal axis. The left vagus (originally anterior to esophagus) becomes the anterior trunk, right vagus becomes the posterior trunk. This rotation also creates the lesser sac posterior to the stomach."},
    {"question": "Name the five arterial supplies to the stomach.",
     "answer": "1) Left gastric (celiac trunk — largest), 2) Right gastric (proper/common hepatic), 3) Left gastroepiploic (splenic artery), 4) Right gastroepiploic (GDA), 5) Short gastrics (splenic artery). ALL five are divided in total gastrectomy."},
    {"question": "For D2 lymphadenectomy, which artery's nodes (station 7) must be cleared at its celiac origin?",
     "answer": "The left gastric artery. Station 7 nodes surround its celiac trunk origin. D2 also includes stations along the splenic artery (11), common hepatic artery (8), and celiac axis (9). Minimum 15 lymph nodes for adequate staging."},
    {"question": "What is the most feared long-term metabolic complication of total gastrectomy?",
     "answer": "B12 deficiency causing megaloblastic anemia and subacute combined degeneration of the spinal cord. Without intrinsic factor (parietal cells), B12 cannot be absorbed. Patients need lifelong parenteral B12. Also: iron deficiency anemia, calcium malabsorption, and dumping syndrome."},
    {"question": "What is the minimum Roux limb length after total gastrectomy, and why?",
     "answer": "40-60cm to prevent bile reflux esophagitis. Short limbs allow bile to reach the esophageal anastomosis, causing severe inflammation and Barrett's-like changes. A jejunal J-pouch (10-15cm) can be added to improve reservoir function and quality of life."}
]

QUESTIONS["Laparoscopic Total Gastrectomy"] = [
    {"question": "The greater omentum develops from which embryologic mesentery?",
     "answer": "The dorsal mesogastrium — as the stomach rotates, it elongates and drapes inferiorly forming the omentum. It must be resected (omentectomy) for T3-T4 gastric cancers because it contains station 4 lymph nodes and may harbor tumor deposits."},
    {"question": "What is the 'infrapyloric space' and why is it a critical dissection zone?",
     "answer": "The space below the pylorus containing station 6 nodes along the right gastroepiploic artery. The GDA, right gastroepiploic vessels, and anterior superior PDA are all in proximity. Pancreatic injury here causes fistula (2-5% incidence)."},
    {"question": "What maintains blood supply to the Roux limb after total gastrectomy?",
     "answer": "Jejunal branches of the SMA via the marginal jejunal arcade. The Roux limb's viability depends on its intact mesentery — excessive skeletonization causes ischemia at the esophagojejunal anastomosis, the most devastating leak location."},
    {"question": "What techniques are available for intracorporeal esophagojejunostomy?",
     "answer": "1) Circular stapler with OrVil (anvil delivered transorally), 2) Linear stapler (overlap/functional end-to-end), 3) Hand-sewn (rare). Leak rates 3-5%. Linear stapler is gaining favor due to lower stricture rates than circular stapler."},
    {"question": "What does JCOG0501 tell us about splenectomy during total gastrectomy?",
     "answer": "Spleen-preserving D2 is non-inferior to splenectomy for OS in proximal gastric cancer not involving the greater curvature. Splenectomy increases morbidity (infection, pancreatic fistula, thrombocytosis) without oncologic benefit. Only indicated for direct splenic invasion or bulky station 10 nodes."}
]

QUESTIONS["Robotic Total Gastrectomy"] = [
    {"question": "The lesser omentum develops from which embryologic mesentery, and what critical structure traverses it?",
     "answer": "The ventral mesogastrium. The hepatoduodenal ligament (part of the lesser omentum) contains the portal triad: CBD (right), hepatic artery proper (left), portal vein (posterior). Also contains left/right gastric vessels and station 1, 3, 5 lymph nodes."},
    {"question": "What is station 12a in robotic D2 lymphadenectomy, and why is it challenging?",
     "answer": "Hepatoduodenal ligament nodes along the proper hepatic artery. Requires skeletonizing the hepatic artery, portal vein, and CBD — injury to any is catastrophic. Robotic wristed instruments excel here for precise dissection in this confined space."},
    {"question": "What is the most common celiac trunk variant relevant to gastrectomy?",
     "answer": "A replaced left hepatic artery from the left gastric artery (10-15%). If unrecognized and ligated with the left gastric during gastrectomy, it causes left hepatic lobe ischemia. Must be identified in the gastrohepatic ligament and preserved."},
    {"question": "What causes post-gastrectomy pancreatic fistula (3-8% incidence)?",
     "answer": "Thermal or mechanical injury to pancreatic body/tail during station 11 (splenic artery) node dissection, omentectomy along the inferior pancreatic border, or retraction injury. Defined by drain amylase >3x serum on POD3 (ISGPF). Most are grade A/B managed conservatively."},
    {"question": "What does the FLOT4 trial (2019, Lancet) establish for gastric cancer treatment?",
     "answer": "Perioperative FLOT (5-FU, leucovorin, oxaliplatin, docetaxel) x4 pre- and post-op significantly improved OS versus ECF/ECX (median 50 vs 35 months). FLOT4 is now the Western standard for ≥T2 or node-positive gastric cancer."}
]

QUESTIONS["Subtotal Gastrectomy with Billroth I"] = [
    {"question": "Which part of the duodenum remains intraperitoneal and is used for the Billroth I anastomosis?",
     "answer": "D1 (duodenal bulb) — covered by peritoneum anteriorly and superiorly, remaining mobile. D2-D4 are retroperitoneal and fixed, making them unsuitable for direct gastroduodenostomy."},
    {"question": "What minimum proximal margin is required for gastric cancer, and how does Lauren classification affect this?",
     "answer": "Intestinal type: 3cm (well-circumscribed). Diffuse type (linitis plastica): 5-8cm due to submucosal spread. Frozen section of the proximal margin is mandatory — if positive, extend to total gastrectomy."},
    {"question": "After ligating the left gastric artery for D2 lymphadenectomy, what maintains the gastric remnant's blood supply?",
     "answer": "Short gastric arteries and left gastroepiploic artery (both from splenic artery). The fundal remnant has a robust submucosal plexus providing excellent collateral flow despite loss of the dominant left gastric artery."},
    {"question": "What is the advantage of Billroth I over Billroth II regarding afferent loop syndrome?",
     "answer": "Afferent loop syndrome is unique to Billroth II (not Billroth I) because Billroth I has a direct gastroduodenostomy without afferent/efferent limbs. This is a significant advantage — no blind loop, no bile stasis, more physiologic food passage through the duodenum."},
    {"question": "What is the long-term cancer risk in the gastric remnant, and when should surveillance begin?",
     "answer": "Stump cancer develops in 1-3% of patients, usually >15-20 years post-surgery. Results from chronic bile reflux, atrophic gastritis, and intestinal metaplasia at the anastomosis. Begin endoscopic surveillance at 15-20 years with anastomotic and remnant biopsies."}
]

QUESTIONS["Subtotal Gastrectomy with Billroth II"] = [
    {"question": "The Billroth II creates a gastrojejunostomy connecting which two embryologic gut segments?",
     "answer": "Foregut (gastric remnant) to midgut (proximal jejunum). The duodenal stump is closed, creating a blind loop — this non-anatomic reconstruction explains the unique metabolic complications of Billroth II."},
    {"question": "What is the optimal afferent limb length in Billroth II?",
     "answer": "15-20cm from the ligament of Treitz. Too long: increased afferent loop syndrome risk (obstruction, bilious vomiting, pancreatitis from stasis). Too short: tension, kinking, inability to reach the gastric remnant."},
    {"question": "What causes duodenal stump blowout, and what is its mortality?",
     "answer": "Ischemia of the closure, distal obstruction (afferent loop), or drain erosion. Incidence 2-4%, mortality 20-30%. Presents as sudden bilious drainage, sepsis, and RUQ pain on POD 3-7. Managed with drainage, antibiotics, and often re-operation."},
    {"question": "How does early dumping differ mechanistically from late dumping after Billroth II?",
     "answer": "Early (15-30 min): hyperosmolar chyme in jejunum → fluid shift → hypovolemia, tachycardia, cramping. Late (1-3 hours): rapid glucose absorption → hyperinsulinemia → reactive hypoglycemia → diaphoresis, confusion. Treatment: small meals, avoid simple sugars. Refractory: octreotide or Roux-en-Y conversion."},
    {"question": "What is alkaline reflux gastritis, and what is the definitive treatment?",
     "answer": "Bile reflux into the gastric remnant causing chronic inflammation, pain, and bilious vomiting — worse in Billroth II because bile enters directly without a pyloric mechanism. Conservative: sucralfate, cholestyramine, PPIs. Definitive: conversion to Roux-en-Y (diverts bile 40-60cm downstream)."}
]

QUESTIONS["Roux-en-Y Gastric Bypass"] = [
    {"question": "What embryologic landmark marks the starting point for measuring Roux limb lengths?",
     "answer": "The ligament of Treitz — a musculofibrous band from the right crus of the diaphragm marking the duodenojejunal junction. This landmark is the critical first step in RYGB construction. The jejunum distal to Treitz is midgut."},
    {"question": "What are the three limb configurations in RYGB and their standard lengths?",
     "answer": "1) Biliopancreatic limb: Treitz to jejunojejunostomy (40-50cm), 2) Roux (alimentary) limb: gastrojejunostomy to jejunojejunostomy (100-150cm), 3) Common channel: jejunojejunostomy to ileocecal valve. Longer Roux = more malabsorption but more nutritional deficiency."},
    {"question": "What is the blood supply to the gastric pouch, and why is ischemia rare?",
     "answer": "Left gastric artery branches along the lesser curve. Despite dividing all other gastric vessels, the rich submucosal plexus makes pouch ischemia extremely rare (<1%). In contrast, the Roux limb depends on its mesentery — tension here causes the clinically significant ischemia."},
    {"question": "What is a marginal ulcer after RYGB, and what is the most important cause to rule out?",
     "answer": "Ulceration at the gastrojejunal anastomosis (1-16%). Causes: acid exposure, NSAIDs, smoking, H. pylori, ischemia. The most important cause to rule out is gastro-gastric fistula — it exposes the anastomosis to acid from the bypassed stomach's full parietal cell mass."},
    {"question": "What are the three internal hernia sites after RYGB, and which is most common?",
     "answer": "1) Petersen's defect (between Roux limb mesentery and transverse mesocolon) — most common, 2) Jejunojejunostomy mesenteric defect, 3) Transverse mesocolon defect (retrocolic route). All should be closed with non-absorbable suture. CT shows 'mesenteric swirl sign.' Incidence: 3-5%."}
]

QUESTIONS["Laparoscopic Sleeve Gastrectomy"] = [
    {"question": "The greater curvature receives blood from branches of the celiac trunk. How does sleeve gastrectomy alter gastric blood supply?",
     "answer": "Short gastric and left gastroepiploic arteries are divided, leaving the sleeve dependent on right gastric artery (lesser curve) and left gastric artery branches. Ischemia at the proximal staple line near the GEJ is the most feared vascular complication."},
    {"question": "What is the correct distance from the pylorus to begin stapling, and what happens if you start too close?",
     "answer": "4-6cm. Starting <2cm narrows the antrum causing functional gastric outlet obstruction, prolonged vomiting, and increased intraluminal pressure leading to staple line leak. Starting >6cm leaves a large antral pouch reducing the restrictive effect."},
    {"question": "What size bougie is used and how does it relate to the left gastric artery?",
     "answer": "32-40 French (commonly 36Fr). The staple line parallels the left gastric artery's lesser curve branches. Staying on the bougie prevents stapling too close to these vessels, which would devascularize the sleeve."},
    {"question": "Where does the staple line leak most commonly occur and why?",
     "answer": "The proximal staple line near the GEJ (angle of His) — thinnest gastric wall, highest intraluminal pressure (LES high-pressure zone), and most tenuous blood supply. Leak rate: 1-3%. Proximal leaks are notoriously difficult to manage and may require stenting or esophagojejunostomy."},
    {"question": "What is the hormonal mechanism of weight loss beyond simple restriction?",
     "answer": "Fundus removal eliminates 80% of ghrelin-producing cells, dramatically reducing appetite. Accelerated gastric emptying increases GLP-1 and PYY release from the distal ileum (incretin effect), improving insulin sensitivity independently of weight loss. This is why sleeve resolves T2DM in 60-70%."}
]

QUESTIONS["Gastrorrhaphy for Perforated Ulcer"] = [
    {"question": "Anterior duodenal ulcers perforate freely. What embryologic feature makes the anterior surface vulnerable compared to the posterior?",
     "answer": "The anterior duodenum is intraperitoneal with only visceral peritoneum — no retroperitoneal reinforcement. Posterior ulcers erode into the retroperitoneum and GDA (hemorrhage). Anterior ulcers perforate into the peritoneal cavity because no tissue barrier exists."},
    {"question": "What tissue is used in a Graham patch repair, and why is the ulcer itself NOT excised?",
     "answer": "Pedicled omentum sutured over the perforation with interrupted sutures. The omentum provides blood supply, fibrinous seal, and inflammatory containment. The ulcer is biopsied but not excised (unless malignancy suspected) — excision enlarges the defect and risks narrowing the duodenum."},
    {"question": "What arterial vessel supplies the omental patch, and what alternative is available if the omentum is absent?",
     "answer": "Right and left gastroepiploic arteries forming the gastroepiploic arcade along the greater curvature. In re-operations with omental loss, a falciform ligament patch or jejunal serosal patch can be used as alternatives."},
    {"question": "Why is definitive ulcer surgery (vagotomy) rarely performed with perforation repair today?",
     "answer": "H. pylori eradication (triple therapy) and PPIs have reduced ulcer recurrence to <5%. Simple patch repair + H. pylori treatment + PPI is now standard. Historical vagotomy with pyloroplasty added morbidity without benefit in the PPI era."},
    {"question": "What percentage of perforated ulcers will NOT show free air on upright CXR?",
     "answer": "15-20%. CT detects free air in >95%. If clinical suspicion is high despite negative films, get CT. Do NOT delay surgery waiting for imaging in a patient with peritonitis and hemodynamic instability — the diagnosis is clinical."}
]

QUESTIONS["Laparoscopic Nissen Fundoplication"] = [
    {"question": "What embryologic event creates the angle of His, and how does it contribute to the anti-reflux barrier?",
     "answer": "Differential growth of the greater curvature (dorsal mesogastrium side) outpacing the lesser curvature creates the acute angle of His between esophagus and fundus. This angle functions as a flap valve — its obliteration by hiatal hernia or obesity contributes to GERD."},
    {"question": "What are the five key steps of hiatal dissection for Nissen fundoplication?",
     "answer": "1) Divide gastrohepatic ligament (watch for replaced left hepatic artery), 2) Identify/preserve anterior vagus, 3) Circumferential esophageal mobilization, 4) Identify/preserve posterior vagus, 5) Close crura posteriorly with non-absorbable suture."},
    {"question": "The short gastric arteries must be divided for a floppy Nissen wrap. What maintains fundal blood supply after division?",
     "answer": "Retrograde flow through the left gastroepiploic artery and the rich submucosal gastric plexus. The short gastric arteries (2-6 branches from the splenic artery) are divided to allow tension-free wrapping."},
    {"question": "What is a 'slipped Nissen' and how does it present?",
     "answer": "The wrap migrates distally off the GEJ and sits around the proximal stomach body, creating a two-compartment stomach. Presents with dysphagia, inability to vomit, and recurrent reflux. Caused by inadequate wrap fixation to the esophagus or failure to close the hiatus. Requires reoperation."},
    {"question": "What preoperative workup is mandatory, and what finding should make you choose a Toupet instead?",
     "answer": "Mandatory: EGD, esophageal manometry, 24hr pH study. If manometry shows ineffective esophageal motility (>50% failed contractions or DCI <450), a partial Toupet (270°) is preferred over Nissen (360°) to reduce postoperative dysphagia. DeMeester score >14.72 confirms pathologic reflux."}
]

QUESTIONS["Laparoscopic Toupet Fundoplication"] = [
    {"question": "What four components create the lower esophageal anti-reflux barrier?",
     "answer": "1) Intrinsic LES smooth muscle tone (2-4cm zone), 2) Crural diaphragm (extrinsic compression, from septum transversum embryologically), 3) Angle of His (flap valve from differential foregut growth), 4) Phrenoesophageal ligament. The Toupet augments LES pressure without complete encirclement."},
    {"question": "In a Toupet 270-degree posterior wrap, what is the relationship of the wrap to the vagus nerves?",
     "answer": "The wrap is posterior, with each tail sutured to the right and left esophageal walls. The posterior vagus sits between wrap and esophagus — it must be identified and NOT incorporated into wrap sutures. The anterior vagus on the esophageal surface must also be preserved."},
    {"question": "Why must crural sutures be placed carefully in relation to the left gastric artery?",
     "answer": "The left gastric artery ascends in the lesser omentum near the left crus. Aggressive crural closure can incorporate or kink this artery, compromising lesser curve blood supply. Place sutures in crural muscle only, well away from the artery."},
    {"question": "What is the theoretical advantage of Toupet over Nissen for esophageal dysmotility patients?",
     "answer": "The 270° wrap leaves the anterior esophagus unwrapped, creating less outflow resistance than 360° Nissen. In weak peristalsis patients, Nissen causes severe dysphagia because the esophagus can't generate pressure to overcome the complete wrap. Toupet provides comparable reflux control with significantly lower dysphagia (5% vs 15-20%)."},
    {"question": "What is the GERD recurrence rate of Toupet versus Nissen at long-term follow-up?",
     "answer": "Toupet 10-15% vs Nissen 5-10% at >5 years. The tradeoff is accepted because Toupet has significantly less dysphagia, gas-bloat syndrome, and inability to belch. The LOTUS trial and meta-analyses show comparable overall patient satisfaction."}
]

QUESTIONS["Laparoscopic Heller Myotomy"] = [
    {"question": "Achalasia results from degeneration of which specific neural structure, and from what embryologic cell population do these neurons derive?",
     "answer": "Myenteric (Auerbach's) plexus inhibitory neurons (releasing NO and VIP) in the LES. These neurons derive from vagal neural crest cells that migrate into the gut wall during weeks 4-7. Loss of inhibitory input leaves excitatory cholinergic neurons unopposed."},
    {"question": "How far does the Heller myotomy extend proximally and distally, and what happens if you go too far onto the stomach?",
     "answer": "6-8cm proximally on the esophagus, 2-2.5cm onto the gastric cardia past the GEJ. Extending >3cm onto stomach causes iatrogenic GERD. Not extending far enough leaves residual LES hypertension and persistent dysphagia."},
    {"question": "What submucosal vessels are encountered during myotomy, and how do you manage bleeding from them?",
     "answer": "Ascending branches of the left gastric artery and esophageal branches of the left inferior phrenic artery form a GEJ plexus visible in the submucosa. Control with gentle pressure — NOT cautery, which risks mucosal perforation through the thin exposed submucosa."},
    {"question": "What is the most feared intraoperative complication and how do you detect it?",
     "answer": "Mucosal perforation (5-10%). Detected by intraoperative endoscopy with air insufflation while the myotomy site is submerged in irrigation — bubbles indicate perforation. If found, repair primarily with absorbable suture and cover with the fundoplication wrap."},
    {"question": "Why is a Dor fundoplication added after Heller, and what does POEM omit?",
     "answer": "The myotomy destroys the LES, predisposing to GERD. Dor (anterior 180°) prevents reflux and covers the exposed myotomy site. POEM omits the fundoplication — GERD rates 40-60% vs 10-15% with Heller + Dor. This is POEM's main disadvantage."}
]

QUESTIONS["Ivor Lewis Esophagectomy"] = [
    {"question": "The esophagus is the only GI organ lacking what outer layer, and how does this affect anastomotic healing?",
     "answer": "No serosa — only adventitia. The serosa provides tensile strength for suture holding and promotes rapid healing via serosal apposition. Without it, esophageal anastomoses heal slowly and leak in 5-15%. The blood supply is also segmental without a named mesenteric vessel."},
    {"question": "Describe the two surgical phases and the level of the anastomosis in Ivor Lewis.",
     "answer": "Phase 1 (Abdominal): gastric mobilization, conduit creation, pyloroplasty, feeding jejunostomy. Phase 2 (Right thoracotomy/VATS): esophageal mobilization, en bloc lymphadenectomy, intrathoracic esophagogastric anastomosis at or above the azygos vein level."},
    {"question": "What is the sole blood supply to the gastric conduit after esophagectomy?",
     "answer": "The right gastroepiploic artery (from GDA). All other gastric vessels are divided. The conduit tip has the most tenuous perfusion — ICG angiography guides the optimal anastomotic site. This is why the conduit must not be twisted or stretched."},
    {"question": "What is the most common cause of death after Ivor Lewis esophagectomy?",
     "answer": "Pneumonia and respiratory failure (not anastomotic leak). Pulmonary complications: 15-30% due to one-lung ventilation, thoracotomy pain, aspiration from conduit dysfunction, and recurrent laryngeal nerve injury. Mortality: 2-5% at high-volume centers (>20/year), >10% at low-volume centers."},
    {"question": "What does the CROSS trial (2012) establish for esophageal cancer neoadjuvant therapy?",
     "answer": "Neoadjuvant chemoradiation (carboplatin + paclitaxel + 41.4 Gy) followed by surgery improved 5-year OS by 13% (47% vs 34%) versus surgery alone. CROSS is the worldwide standard for locally advanced esophageal cancer."}
]

QUESTIONS["Gastric Pull-up Reconstruction"] = [
    {"question": "What embryologic vascular axis allows the stomach to serve as an esophageal substitute?",
     "answer": "The celiac trunk axis — specifically the right gastroepiploic artery (from GDA, a celiac trunk branch) runs the entire greater curvature, providing a reliable axial blood supply. The stomach's rich submucosal plexus allows it to survive on this single pedicle after dividing all other vessels."},
    {"question": "What is the gastric conduit length, and through which mediastinal route is it positioned?",
     "answer": "The tubularized stomach (3-5cm wide) reaches the neck (60-70cm). Routes: posterior mediastinal (orthotopic, in the esophageal bed — shortest, preferred), substernal (retrosternal — used if posterior mediastinum is hostile), or subcutaneous (rarely, for salvage). Posterior is anatomically shortest with best conduit perfusion."},
    {"question": "What is the blood supply hierarchy of esophageal conduit options?",
     "answer": "Stomach (right gastroepiploic): best blood supply, most robust. Colon (marginal artery): reliable but segmental, higher leak rates. Jejunum (SMA branches): microvascular free flap needed for long gaps, most technically demanding. Stomach is the first-choice conduit for esophageal replacement."},
    {"question": "What is conduit necrosis, and what is its mortality?",
     "answer": "Ischemic necrosis of the gastric conduit — devastating complication with 30-50% mortality. Presents with sepsis, mediastinitis, and conduit breakdown. Caused by tension, twist, or inadequate right gastroepiploic flow. Requires emergent takedown, cervical esophagostomy, and feeding access."},
    {"question": "What is the role of the pyloroplasty or pyloromyotomy in gastric pull-up?",
     "answer": "The vagus nerves are divided during esophagectomy, causing pyloric spasm and delayed gastric conduit emptying. Pyloroplasty/pyloromyotomy prevents outlet obstruction, aspiration, and conduit distension. Some surgeons inject botulinum toxin into the pylorus as an alternative."}
]

QUESTIONS["Colonic Interposition"] = [
    {"question": "Which colonic segment is most commonly used for esophageal replacement, and what embryologic blood supply makes it suitable?",
     "answer": "Left colon (descending/transverse) based on the ascending branch of the left colic artery (from IMA) is most commonly used. The marginal artery provides a reliable arcade. Right colon on the ileocolic pedicle is an alternative. Isoperistaltic placement (proximal colon anastomosed to esophagus) matches normal motility direction."},
    {"question": "What preoperative study is essential before harvesting colon for interposition?",
     "answer": "Mesenteric angiography or CT angiography to confirm the adequacy of the vascular arcade (marginal artery) and identify anatomic variants. Colonoscopy to exclude intrinsic colonic disease. An inadequate marginal artery or colonic pathology is a contraindication."},
    {"question": "The interposed colon segment has three anastomoses. What are they and which has the highest leak rate?",
     "answer": "1) Cervical esophago-colonic (highest leak rate — 10-20% — due to tension and precarious blood supply at the tip), 2) Colo-gastric or colo-jejunal (distal), 3) Colo-colonic (restoring GI continuity). The cervical anastomosis leaks most because the conduit tip has the most tenuous perfusion."},
    {"question": "What is the most common late complication of colonic interposition?",
     "answer": "Redundancy of the interposed segment causing dysphagia, regurgitation, and food stasis as the colon dilates over years. Unlike the stomach, the colon is not designed for peristaltic bolus transport. May require surgical tailoring (colonic plication or replacement)."},
    {"question": "When is colonic interposition preferred over gastric pull-up?",
     "answer": "When the stomach is unavailable (prior gastrectomy, gastric cancer), caustic injury involving both esophagus and stomach, or when the stomach's blood supply is compromised. Also preferred in children with long-gap esophageal atresia because the colon grows with the child and has a more reliable long-term conduit."}
]

QUESTIONS["Laparoscopic Paraesophageal Hernia Repair"] = [
    {"question": "What embryologic defect creates the hiatal opening, and what distinguishes a type I from a type IV paraesophageal hernia?",
     "answer": "The esophageal hiatus forms from failure of the right crus of the diaphragm (derived from the pleuroperitoneal membrane/septum transversum) to completely close around the esophagus. Type I: sliding (GEJ migrates upward). Type II: true paraesophageal (fundus herniates alongside fixed GEJ). Type III: combined. Type IV: herniation of additional organs (colon, spleen, omentum)."},
    {"question": "What is the key surgical step that differentiates paraesophageal hernia repair from standard fundoplication?",
     "answer": "Complete reduction of the hernia sac and excision of the sac from the mediastinum. The sac must be dissected off the pleura, pericardium, and aorta. Leaving the sac increases recurrence. Additionally, the esophagus must be mobilized to obtain ≥3cm of intra-abdominal length without tension."},
    {"question": "What is the blood supply concern when the stomach is chronically herniated and undergoes organoaxial volvulus?",
     "answer": "Gastric volvulus causes compression of the left gastric artery and short gastric vessels, leading to gastric ischemia and potential necrosis. The right gastroepiploic may be kinked. Acute gastric volvulus with ischemia is a surgical emergency with 30-50% mortality if not treated promptly."},
    {"question": "What is the recurrence rate of paraesophageal hernia repair, and does mesh reduce it?",
     "answer": "Recurrence: 15-25% (radiographic) at 5 years, though symptomatic recurrence is lower (5-10%). Biologic mesh reinforcement of the crural closure may reduce recurrence (FLAIR trial ongoing), but synthetic mesh at the hiatus is controversial due to erosion risk into the esophagus."},
    {"question": "What is the most feared acute complication of a large paraesophageal hernia that can present without surgery?",
     "answer": "Incarceration with gastric volvulus causing obstruction, ischemia, and perforation — the 'acute upside-down stomach.' Borchardt's triad: epigastric pain, retching without vomiting (non-productive), and inability to pass an NG tube. This is a surgical emergency requiring immediate operative repair."}
]

QUESTIONS["Zenker Diverticulectomy"] = [
    {"question": "What is the embryologic/anatomic weakness that allows Zenker's diverticulum to form?",
     "answer": "Killian's triangle (dehiscence) — a muscular gap between the oblique fibers of the inferior pharyngeal constrictor and the transverse fibers of the cricopharyngeus muscle. This posterior hypopharyngeal weakness allows mucosal herniation (pulsion diverticulum) from increased intraluminal pressure."},
    {"question": "Zenker's is a FALSE diverticulum. What does that mean anatomically?",
     "answer": "It contains only mucosa and submucosa (no muscularis propria), unlike a true diverticulum (Meckel's) which contains all layers. It herniates through the muscular defect (Killian's triangle). Its posterior location means it presents to the left of the midline cervically."},
    {"question": "What is the blood supply to the posterior hypopharynx at the Zenker's site?",
     "answer": "Branches of the inferior thyroid artery (from thyrocervical trunk) and ascending pharyngeal artery (from external carotid). During diverticulectomy, the inferior thyroid artery's branches are at risk during the cervical approach. The recurrent laryngeal nerve runs in close proximity."},
    {"question": "What is the critical step beyond diverticulectomy, and what happens if you omit it?",
     "answer": "Cricopharyngeal myotomy — division of the cricopharyngeus muscle for 3-5cm. Without myotomy, the underlying cause (UES dysfunction/incomplete relaxation) persists and recurrence is nearly guaranteed. Myotomy alone (without diverticulectomy) may suffice for small pouches (<2cm)."},
    {"question": "What endoscopic alternatives exist for Zenker's, and what is their recurrence rate?",
     "answer": "Endoscopic stapler-assisted diverticulotomy (divides the common wall between diverticulum and esophagus, including the cricopharyngeus) and flexible endoscopic myotomy (Z-POEM). Recurrence: 10-15% (vs 3-5% for open). Advantages: no external incision, shorter recovery, lower RLN injury risk. Preferred for elderly or high-risk patients."}
]

# ============================================================
# BREAST
# ============================================================

QUESTIONS["Total Mastectomy"] = [
    {"question": "The breast develops from what embryologic structure, and when does it first appear?",
     "answer": "The mammary ridge (milk line) — a thickened strip of ectoderm extending from the axilla to the inguinal region during week 6. The breast develops from the pectoral portion of this ridge. Failure of regression causes accessory nipples (polythelia) or accessory breast tissue (polymastia) along this line."},
    {"question": "What are the boundaries of a total mastectomy dissection?",
     "answer": "Superior: clavicle/2nd rib. Inferior: rectus sheath/inframammary fold. Medial: sternal border. Lateral: latissimus dorsi anterior border. Deep: pectoralis major fascia (which is included). The axillary tail (of Spence) extends toward the axilla and must be included."},
    {"question": "What is the blood supply to the breast, and which perforating vessels are most important?",
     "answer": "Internal mammary artery perforators (60% of supply — 2nd, 3rd, 4th intercostal perforators are dominant), lateral thoracic artery, thoracoacromial artery, and intercostal artery perforators. During mastectomy, the internal mammary perforators are divided at the sternal border."},
    {"question": "What are the key nerves at risk during mastectomy?",
     "answer": "Long thoracic nerve (C5-C7, runs on serratus anterior surface — injury causes winged scapula). Thoracodorsal nerve (C6-C8, runs to latissimus dorsi — injury weakens shoulder adduction/internal rotation). Intercostobrachial nerve (T2 lateral cutaneous branch — almost always divided, causing inner arm numbness)."},
    {"question": "What is the most common indication for total mastectomy over breast-conserving surgery?",
     "answer": "Multicentric disease (cancer in >1 quadrant), diffuse suspicious calcifications, inability to achieve negative margins after re-excision, prior radiation to the chest, inflammatory breast cancer, large tumor-to-breast ratio, and patient preference. BRCA mutation carriers may elect prophylactic bilateral mastectomy."}
]

QUESTIONS["Modified Radical Mastectomy"] = [
    {"question": "What distinguishes the Halsted radical mastectomy from the modified radical mastectomy embryologically and surgically?",
     "answer": "Halsted (1882) removed the pectoralis major and minor en bloc with axillary nodes. The modified radical mastectomy (Patey/Madden) preserves the pectoralis major (and minor in Madden), recognizing that these muscles are not part of the lymphatic drainage pathway. The Patey modification removes pectoralis minor; Madden preserves both."},
    {"question": "What are the anatomic boundaries of the level I, II, and III axillary lymph node dissection?",
     "answer": "Level I: lateral to pectoralis minor. Level II: behind pectoralis minor. Level III: medial to pectoralis minor (infraclavicular/subclavicular). Level II access requires retracting pectoralis minor. Level III requires dividing pectoralis minor (Patey) or reaching medial to it. MRM typically includes levels I and II."},
    {"question": "What is the blood supply to the axilla, and which vessel is the 'vessel of axillary dissection'?",
     "answer": "The axillary artery branches: thoracoacromial, lateral thoracic, subscapular (gives off thoracodorsal and circumflex scapular). The lateral thoracic artery runs on the chest wall surface and is frequently encountered/ligated during axillary dissection."},
    {"question": "What is the incidence of lymphedema after modified radical mastectomy with axillary dissection?",
     "answer": "15-25% lifelong risk (increases with radiation, obesity, and extent of nodal disease). Caused by disruption of axillary lymphatic drainage. Sentinel lymph node biopsy has reduced this to 5-8% for SLN-negative patients. Lymphedema is irreversible once established — prevention and early intervention are critical."},
    {"question": "What landmark trial changed the management of the axilla for clinically node-negative breast cancer?",
     "answer": "ACOSOG Z0011 (2011, JAMA): patients with T1-T2, clinically node-negative breast cancer with 1-2 positive SLN undergoing lumpectomy did NOT benefit from completion ALND. No difference in OS or DFS. This practice-changing trial eliminated ALND for many SLN-positive patients receiving whole-breast radiation."}
]

QUESTIONS["Bilateral Mastectomy"] = [
    {"question": "What percentage of BRCA1 versus BRCA2 carriers develop contralateral breast cancer?",
     "answer": "BRCA1: 40-60% lifetime risk of contralateral breast cancer. BRCA2: 25-40%. This high contralateral risk (vs 5-10% in non-carriers) justifies prophylactic contralateral mastectomy in carriers. Risk-reducing bilateral mastectomy reduces breast cancer risk by 90-95%."},
    {"question": "What is the tissue plane for bilateral mastectomy, and how do you ensure complete glandular excision?",
     "answer": "Between the breast parenchyma and subcutaneous fat (superficial plane) and between the breast and pectoralis fascia (deep plane). Skin flap thickness of 5-7mm preserves dermal blood supply. The retromammary bursa (between breast and pectoralis fascia) is the natural deep dissection plane."},
    {"question": "During bilateral mastectomy, what is the blood supply to the skin flaps?",
     "answer": "Subdermal plexus fed by internal mammary perforators medially, lateral thoracic branches laterally, and intercostal perforators. Flap necrosis (5-15%) occurs when flaps are too thin, cautery is excessive, or the skin envelope is too tight over an implant. More common in smokers and after prior radiation."},
    {"question": "What is the complication rate difference between bilateral mastectomy and unilateral?",
     "answer": "Bilateral mastectomy has higher overall complication rates (30-40% vs 15-20%), including: longer operative time, higher blood loss, bilateral flap necrosis risk, bilateral seroma, and longer recovery. When combined with immediate reconstruction, surgical site infection and implant loss rates are compounded bilaterally."},
    {"question": "What is the evidence for contralateral prophylactic mastectomy (CPM) in non-BRCA patients with unilateral breast cancer?",
     "answer": "CPM reduces contralateral breast cancer risk but has NOT been shown to improve overall survival in non-BRCA patients (whose contralateral risk is only 0.5-1%/year). SEER data shows no OS benefit. CPM rates have tripled despite lack of survival benefit, driven by patient preference, MRI detection of incidental findings, and anxiety reduction."}
]

QUESTIONS["Breast Lumpectomy"] = [
    {"question": "What is the embryologic basis for breast tissue extending into the axillary tail of Spence?",
     "answer": "The mammary ridge extends from axilla to groin during development. The axillary tail represents the most lateral extent of persistent mammary ridge tissue. Cancers can arise in the tail, and it must be included in the surgical field. Accessory breast tissue in the axilla is a remnant of incomplete ridge regression."},
    {"question": "What are the current minimum negative margin requirements for invasive cancer versus DCIS after lumpectomy?",
     "answer": "Invasive cancer: 'no ink on tumor' (2014 SSO-ASTRO consensus — wider margins do NOT reduce recurrence when combined with radiation). DCIS: 2mm negative margin (2016 SSO-ASTRO-ASCO consensus). These guidelines ended the era of re-excision for 'close' margins in invasive cancer."},
    {"question": "What is the blood supply to the breast quadrant containing the tumor, and how does lumpectomy affect it?",
     "answer": "The breast is supplied by a segmental pattern: medial quadrants by internal mammary perforators, lateral quadrants by lateral thoracic and intercostal arteries. Lumpectomy disrupts the local blood supply to the cavity, which fills with seroma. Oncoplastic techniques can redistribute remaining tissue to fill the defect."},
    {"question": "What is the local recurrence rate after lumpectomy alone versus lumpectomy with radiation?",
     "answer": "Lumpectomy alone: 25-40% at 10 years. Lumpectomy + radiation: 5-10% at 10 years. This is why whole-breast radiation is mandatory after lumpectomy (NSABP B-06, 20-year data). The sole exception: PRIME II trial showed omission of radiation may be acceptable in low-risk women >65 with ER+, T1, node-negative tumors on endocrine therapy."},
    {"question": "When must you perform an intraoperative specimen radiograph, and what are you looking for?",
     "answer": "For any lesion identified by imaging (calcifications, architectural distortion, or image-detected mass) — especially wire-localized or seed-localized lesions. You're confirming the target is in the specimen (calcifications, clip, or seed). If the target is not in the specimen, re-excise immediately. Also assess for specimen orientation to guide margin re-excision if needed."}
]

QUESTIONS["Nipple-Sparing Mastectomy"] = [
    {"question": "What is the embryologic origin of the nipple-areolar complex, and why can it be preserved oncologically?",
     "answer": "The nipple develops from the primary mammary bud — invagination of the ectodermal mammary ridge into underlying mesenchyme. The NAC contains only skin and minimal terminal duct tissue. Retroareolar margin biopsy (frozen section of the tissue behind the nipple) confirms no cancer involvement, making oncologic preservation safe when negative."},
    {"question": "What anatomic plane is used for NAC-sparing dissection, and what determines nipple viability?",
     "answer": "The subcutaneous plane just deep to the dermis of the NAC. Nipple viability depends on the subdermal vascular plexus, which is supplied by perforators from the internal mammary, lateral thoracic, and intercostal arteries. The skin flaps must be thick enough (5-7mm) to preserve this plexus."},
    {"question": "What is the blood supply to the nipple-areolar complex specifically?",
     "answer": "A rich subdermal plexus fed by perforators from all four quadrants. The dominant supply is from medial internal mammary perforators and the lateral thoracic artery. The areola has a circular arterial ring (Halsted's circulus arteriosus). NAC necrosis (5-15%) occurs when the subdermal plexus is disrupted by thin flap dissection or large breast skin envelope."},
    {"question": "What is the NAC necrosis rate, and what patient factors increase it?",
     "answer": "Partial necrosis: 5-15%. Complete necrosis: 2-5%. Risk factors: smoking (3-5x increased risk), BMI >30, large ptotic breasts (G > D cup), prior breast radiation, diabetes, and incision placement (inframammary fold incision has lowest NAC necrosis rates vs periareolar)."},
    {"question": "What are the oncologic indications and contraindications for nipple-sparing mastectomy?",
     "answer": "Indications: tumor >2cm from NAC, prophylactic mastectomy in BRCA carriers, and patient preference. Contraindications: clinical nipple involvement, bloody nipple discharge, retroareolar tumor, positive retroareolar frozen section, inflammatory breast cancer, and Paget's disease of the nipple."}
]

QUESTIONS["Sentinel Lymph Node Biopsy"] = [
    {"question": "What embryologic pathway explains why breast lymphatic drainage goes to the axilla?",
     "answer": "Breast tissue develops from the pectoral mammary ridge, and lymphatic development follows the mesenchymal tissue between the breast and axilla. 75% of breast lymph drains to the axillary nodes (following the lateral thoracic vessels). The remaining 25% drains to internal mammary nodes (following the IMA perforators) — this drainage is often under-appreciated."},
    {"question": "What defines the sentinel lymph node, and what is the false-negative rate of SLNB?",
     "answer": "The first node(s) receiving lymphatic drainage from the tumor site. Identified by dual tracer (technetium-99m sulfur colloid + isosulfan blue/ICG). False-negative rate: 5-10% (defined as negative SLN with positive non-SLN nodes). This is why ≥2 SLN should be removed when possible — removing 3+ nodes reduces the FNR to <5%."},
    {"question": "What is the blood supply to the axillary lymph node basin, and what vessel runs through the nodal tissue?",
     "answer": "Branches of the lateral thoracic artery, subscapular artery, and thoracoacromial trunk. The thoracodorsal artery/vein runs through the level I/II nodes and must be preserved during SLNB. The intercostobrachial nerve (T2) crosses the axilla and is at risk during dissection."},
    {"question": "What is the clinical significance of ACOSOG Z0011 for SLNB-positive patients?",
     "answer": "Z0011 (2011): T1-T2, clinically node-negative patients with 1-2 positive SLN undergoing lumpectomy + whole-breast RT do NOT benefit from completion ALND. 10-year OS was equivalent. This eliminated routine ALND for most SLNB-positive patients and reduced morbidity (lymphedema, nerve injury) dramatically."},
    {"question": "When is SLNB contraindicated, and when should you go straight to ALND?",
     "answer": "SLNB contraindicated: inflammatory breast cancer, clinically palpable/biopsy-proven N2-N3 disease, and after failed prior SLN mapping. Straight to ALND: proven axillary metastasis (FNA/core biopsy positive node) in patients not receiving neoadjuvant therapy. After neoadjuvant chemo, targeted axillary dissection (TAD = SLN + clipped node) is the new standard."}
]

QUESTIONS["Axillary Lymph Node Dissection"] = [
    {"question": "The axillary lymph nodes develop from which embryologic tissue, and how many nodes are typically in the axilla?",
     "answer": "Mesenchymal tissue (mesoderm) that differentiates into lymphoid tissue during weeks 9-12. The axilla contains 20-40 lymph nodes organized into three levels relative to the pectoralis minor muscle. An adequate ALND should yield ≥10 nodes for proper staging."},
    {"question": "What are the anatomic boundaries of a standard (level I-II) axillary lymph node dissection?",
     "answer": "Superior: axillary vein. Inferior: tail of the breast. Medial: chest wall (serratus anterior). Lateral: latissimus dorsi. The dissection clears tissue lateral to (Level I) and behind (Level II) the pectoralis minor. Level III (medial to pectoralis minor) is included only for gross disease."},
    {"question": "What three nerves must be identified and preserved during ALND?",
     "answer": "1) Long thoracic nerve (on serratus anterior — injury: winged scapula), 2) Thoracodorsal nerve (to latissimus — injury: weakness of shoulder adduction/internal rotation), 3) Medial pectoral nerve (enters pectoralis minor — injury: pectoralis atrophy). The intercostobrachial nerve (sensory, T2) is usually sacrificed."},
    {"question": "What is the lymphedema risk after ALND versus SLNB, and what is LYMPHA?",
     "answer": "ALND: 15-25%. SLNB only: 5-8%. LYMPHA (lymphatic microsurgical preventive healing approach): intraoperative lymphatic-to-venous anastomosis at the time of ALND, reducing lymphedema from 25% to 4-8%. This is emerging as a standard adjunct to ALND."},
    {"question": "What landmark trial showed ALND could be safely omitted in the neoadjuvant setting?",
     "answer": "ACOSOG Z1071 and SENTINA: after neoadjuvant chemotherapy in initially node-positive patients, SLNB alone (with ≥3 SLN retrieved and dual tracer) had an acceptable FNR of <10%. Targeted axillary dissection (TAD — removing the clipped node + SLN) further reduces FNR to <2%."}
]

# ============================================================
# ENDOCRINE
# ============================================================

QUESTIONS["Total Thyroidectomy"] = [
    {"question": "The thyroid gland develops from what embryologic structure, and what is the thyroglossal duct?",
     "answer": "A median endodermal thickening at the foramen cecum (base of tongue), descending through the thyroglossal duct to its final pretracheal position by week 7. The thyroglossal duct normally obliterates. Failure: thyroglossal duct cyst (most common midline neck mass in children, moves with swallowing AND tongue protrusion)."},
    {"question": "What is the relationship of the recurrent laryngeal nerve to the inferior thyroid artery?",
     "answer": "Variable and dangerous: the RLN may pass anterior, posterior, or between branches of the ITA. On the right, the RLN is more lateral (loops around the subclavian artery). A non-recurrent right laryngeal nerve (0.5-1%) runs directly from the vagus to the larynx — associated with retroesophageal right subclavian artery (arteria lusoria)."},
    {"question": "What is the blood supply to the parathyroid glands, and how do you preserve it during thyroidectomy?",
     "answer": "The inferior parathyroids are supplied by the inferior thyroid artery (most critical to preserve). The superior parathyroids are supplied by the superior thyroid artery or an anastomosis with the ITA. During thyroidectomy, ligate the ITA branches close to the thyroid capsule (not the trunk) to preserve parathyroid blood supply. If devascularized, autotransplant the gland into the sternocleidomastoid."},
    {"question": "What is the most feared immediate complication of bilateral thyroidectomy?",
     "answer": "Bilateral RLN injury causing bilateral vocal cord paralysis, airway obstruction, and need for emergent tracheostomy. Unilateral RLN injury (1-5%): hoarseness. Bilateral injury (<1% with nerve monitoring): stridor, inability to protect airway. Intraoperative nerve monitoring (IONM) does not prevent but helps identify nerve injury in real-time."},
    {"question": "What is the Berry ligament and why is it the most dangerous point of thyroidectomy?",
     "answer": "The ligament of Berry is a condensation of pretracheal fascia fixing the thyroid to the cricoid cartilage. The RLN passes within 1-2mm of or through this ligament before entering the larynx at the cricothyroid joint. This is where the nerve is at greatest risk — meticulous capsular dissection and nerve identification is mandatory at this point."}
]

QUESTIONS["Hemithyroidectomy"] = [
    {"question": "What percentage of thyroid nodules are malignant, and what Bethesda category mandates lobectomy?",
     "answer": "5-15% of thyroid nodules are malignant. Bethesda IV (follicular neoplasm/suspicious for follicular neoplasm) mandates lobectomy because FNA cannot distinguish follicular adenoma from carcinoma — the distinction requires histologic assessment of capsular/vascular invasion."},
    {"question": "During hemithyroidectomy, what is the relationship of the superior laryngeal nerve's external branch to the superior thyroid artery?",
     "answer": "The external branch of the SLN runs with the superior thyroid artery in Joll's triangle (bounded by the sternothyroid, superior thyroid pole, and superior thyroid artery). Injury causes loss of cricothyroid function — inability to produce high-pitched sounds. Ligate the artery individually close to the capsule, not the pedicle en masse."},
    {"question": "What is the blood supply to a thyroid lobe, and which vessels are divided during hemithyroidectomy?",
     "answer": "Superior thyroid artery (first branch of external carotid — supplies upper pole), inferior thyroid artery (from thyrocervical trunk — supplies lower pole and parathyroids). Both are ligated/divided on the operative side. The thyroid ima artery (from brachiocephalic, present in 3-10%) may supply the isthmus and lower poles."},
    {"question": "What is the risk of permanent hypoparathyroidism after hemithyroidectomy versus total thyroidectomy?",
     "answer": "Hemithyroidectomy: <1% (two glands on the contralateral side are undisturbed). Total thyroidectomy: 1-5% permanent (requiring lifelong calcium + calcitriol). Transient hypoparathyroidism after total thyroidectomy: 10-30%. This difference in parathyroid morbidity is a key reason to consider hemithyroidectomy for low-risk cancers."},
    {"question": "What is the current ATA guideline for hemithyroidectomy versus total thyroidectomy for papillary thyroid cancer 1-4cm?",
     "answer": "2015 ATA guidelines: lobectomy is sufficient for unifocal PTC 1-4cm without extrathyroidal extension, clinical lymph node involvement, or prior radiation. Total thyroidectomy is not mandatory. Completion thyroidectomy can be performed later if final pathology is unfavorable. This was a major paradigm shift from prior practice of total thyroidectomy for all PTC."}
]

# Parathyroidectomy is in pimping_q2.py