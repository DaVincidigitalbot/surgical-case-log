#!/usr/bin/env python3
"""Add procedure-specific pimping questions to procedures.json"""
import json

# Map procedure name -> 5 pimping questions
# Format: [embryology, anatomy, blood supply, complication, clinical pearl]
PIMPING = {

"Laparoscopic Cholecystectomy": [
    {"question": "The falciform ligament is a remnant of what embryologic structure?",
     "answer": "The ventral mesentery (specifically the umbilical vein within it becomes the ligamentum teres)."},
    {"question": "What three criteria define the critical view of safety in cholecystectomy?",
     "answer": "1) Hepatocystic triangle cleared of all fibrous and fatty tissue, 2) Only two structures (cystic duct and cystic artery) seen entering the gallbladder, 3) The lower third of the cystic plate (liver bed) is exposed."},
    {"question": "The cystic artery typically arises from which vessel, and what is the most common variant?",
     "answer": "Right hepatic artery within the hepatocystic triangle. Most common variant is origin from the left hepatic artery or a replaced right hepatic artery off the SMA (~25%)."},
    {"question": "What is a Mirizzi syndrome and how does it complicate cholecystectomy?",
     "answer": "Extrinsic compression of the common hepatic duct by an impacted stone in the cystic duct or Hartmann's pouch. Type II-IV involve cholecystocholedochal fistula, making dissection treacherous and often requiring bile duct reconstruction."},
    {"question": "What is Rouviere's sulcus and how does it help prevent bile duct injury?",
     "answer": "A 2-5cm cleft on the inferior surface of the right liver lobe running anterior to the caudate process. It serves as a landmark — dissection should remain anterior and to the right of this sulcus to stay safely above the bile duct."}
],

"Open Cholecystectomy": [
    {"question": "From what embryologic structure does the gallbladder develop?",
     "answer": "The caudal bud of the hepatic diverticulum from the foregut endoderm during week 4 of development."},
    {"question": "What is the triangle of Calot versus the hepatocystic triangle, and which is more surgically relevant?",
     "answer": "Calot's triangle: cystic duct, cystic artery, and common hepatic duct. The hepatocystic triangle (cystic duct, CHD, and inferior liver edge) is more surgically relevant because it encompasses the area of dissection and potential injury."},
    {"question": "What is the caterpillar hump and why must you identify it during open cholecystectomy?",
     "answer": "A tortuous right hepatic artery that loops into the hepatocystic triangle, mimicking the cystic artery. Failure to recognize it risks ligation of the right hepatic artery causing right liver ischemia."},
    {"question": "What is a bile duct of Luschka and what complication does it cause?",
     "answer": "Small accessory bile ductules draining directly from the liver bed into the gallbladder fossa. If not recognized, they cause postoperative bile leak (biloma) even when the cystic duct stump is secure."},
    {"question": "When performing a 'fundus-first' or top-down cholecystectomy, what is the key advantage in a hostile hilum?",
     "answer": "It allows identification of structures from a known anatomy (fundus) toward unknown (hilum), reducing risk of CBD injury in the setting of severe inflammation or Mirizzi syndrome. The cystic duct-CBD junction is defined last, when surrounding anatomy is clearer."}
],

"Laparoscopic Appendectomy": [
    {"question": "The appendix, cecum, and ascending colon all derive from which embryologic gut division, and what is the clinical significance of midgut rotation for appendiceal position?",
     "answer": "Midgut. The midgut undergoes a 270-degree counterclockwise rotation around the SMA axis. Incomplete rotation (malrotation) places the appendix in the left upper quadrant, causing atypical presentation of appendicitis."},
    {"question": "What is the most common position of the appendix, and which position most commonly mimics urologic pathology?",
     "answer": "Retrocecal (65%). The pelvic position can mimic UTI or gynecologic pathology; retrocecal can cause flank/back pain mimicking renal colic."},
    {"question": "What is the appendicular artery a branch of, and what is the consequence of inadequate ligation?",
     "answer": "A branch of the ileocolic artery (which comes off the SMA). Inadequate ligation leads to mesoappendix hematoma or intraperitoneal hemorrhage, the most common reason for re-operation after appendectomy."},
    {"question": "What is the stump appendicitis phenomenon and how do you avoid it?",
     "answer": "Recurrent appendicitis from a retained appendiceal stump >0.5cm. Prevented by ensuring complete transection at the cecal base. Occurs in 1/50,000 appendectomies and is more common after laparoscopic approach."},
    {"question": "In a patient with appendicitis and a phlegmon on CT, what landmark randomized trial guides your management?",
     "answer": "The CODA trial (2020, NEJM) showed antibiotics alone were non-inferior to surgery for uncomplicated appendicitis but had a 29% crossover to surgery by 90 days. For phlegmon/abscess, interval appendectomy after percutaneous drainage and antibiotics is standard, though ACCURE trial data questions necessity of interval appendectomy."}
],

"Open Appendectomy": [
    {"question": "The appendix develops from which part of the midgut loop, and at what gestational week does it become recognizable?",
     "answer": "The caudal limb of the midgut loop (post-arterial segment). It first appears as a diverticulum of the cecal bud at week 8, becoming clearly recognizable by week 12."},
    {"question": "Describe McBurney's point and the layers encountered in a McBurney (muscle-splitting) incision.",
     "answer": "McBurney's point: junction of the lateral and middle thirds of a line from ASIS to umbilicus. Layers: skin, Scarpa's fascia, external oblique aponeurosis (split along fibers), internal oblique (split), transversus abdominis (split), transversalis fascia, preperitoneal fat, peritoneum."},
    {"question": "The ileocolic artery gives off which terminal branches that are relevant during appendectomy?",
     "answer": "Anterior and posterior cecal arteries, appendicular artery, ileal branch, and colic branch. The appendicular artery runs in the free edge of the mesoappendix — it is an end artery, meaning thrombosis causes gangrenous appendicitis."},
    {"question": "What is the most feared wound complication specific to open appendectomy for perforated appendicitis?",
     "answer": "Surgical site infection (SSI), occurring in 10-20% of perforated cases. This is why many surgeons leave the skin open for delayed primary closure (DPC) at day 4-5 if the wound is clean."},
    {"question": "What is the 'hamburger sign' and the 'Dunphy sign' in evaluating appendicitis?",
     "answer": "Hamburger sign: a child who refuses to eat (anorexia) almost always has appendicitis — high sensitivity. Dunphy sign: increased abdominal pain with coughing, indicating peritoneal irritation. Both have high clinical utility in equivocal cases."}
],

"Laparoscopic Ileocecectomy": [
    {"question": "The ileocecal valve develops from which embryologic gut junction, and what controls its competence?",
     "answer": "The junction of the midgut and hindgut. The ileocecal valve's competence is maintained by a thickening of the circular smooth muscle layer — an incompetent valve allows colonic reflux and is seen in ~15% of normal adults."},
    {"question": "What is the bloodless fold of Treves and why is it relevant during ileocecal mobilization?",
     "answer": "An avascular peritoneal fold between the terminal ileum and base of the appendix/cecum. It serves as a reliable landmark to identify the appendix and begin medial-to-lateral mobilization of the ileocecal region."},
    {"question": "During ileocecectomy, which named vessel must be identified and ligated at its origin, and from where does it arise?",
     "answer": "The ileocolic artery, the most constant branch of the SMA. It must be ligated at its origin from the SMA for oncologic resection to ensure adequate lymph node harvest along the ileocolic pedicle."},
    {"question": "What is the dreaded complication of an ileocecal anastomotic leak, and what factors increase its risk?",
     "answer": "Fecal peritonitis and sepsis, with mortality up to 10-15%. Risk factors include tension on the anastomosis, malnutrition (albumin <3.0), emergency surgery, immunosuppression (steroids in Crohn's), and inadequate blood supply to the staple line."},
    {"question": "In Crohn's disease, what is the recommended proximal margin of resection, and why is 'radical' resection contraindicated?",
     "answer": "Grossly normal-appearing margins (2cm from visible disease). Microscopic positive margins do NOT increase recurrence rates. Radical resection wastes small bowel, risking short gut syndrome — Crohn's recurs at the anastomosis regardless of margin status."}
],

"Laparoscopic Right Hemicolectomy": [
    {"question": "The right colon derives from which embryologic gut division, and what is the arterial watershed area that results?",
     "answer": "Midgut (cecum to proximal 2/3 of transverse colon). The watershed area is at Griffiths' point near the splenic flexure where SMA territory meets IMA territory — though the right colon's own watershed is Sudeck's point concept applied to the marginal artery near the ileocolic region."},
    {"question": "During medial-to-lateral mobilization, what is the 'holy plane' and what structures must you stay anterior to?",
     "answer": "The avascular embryologic fusion plane between the mesocolon and Gerota's fascia/retroperitoneum. You must stay anterior to the right ureter, gonadal vessels, duodenum (C-loop), and right kidney. The duodenum is the most commonly injured structure."},
    {"question": "Name the three named arteries ligated during a standard right hemicolectomy and their origin.",
     "answer": "1) Ileocolic artery (from SMA), 2) Right colic artery (from SMA — absent in 10-20%), 3) Right branch of middle colic artery (from SMA). All arise from the SMA, confirming the midgut origin of the right colon."},
    {"question": "What is the most common cause of early anastomotic leak after ileocolic anastomosis, and what is the 'ring of death'?",
     "answer": "Inadequate blood supply to the staple line is the #1 cause. The 'ring of death' refers to the circle of staples at a side-to-side functional end-to-end anastomosis — if the crotch of the staple lines is ischemic, it leaks at the weakest point."},
    {"question": "What is a complete mesocolic excision (CME) and what evidence supports it in right colon cancer?",
     "answer": "CME involves sharp dissection of the visceral mesocolic fascia from the parietal plane with central vascular ligation, analogous to TME for rectal cancer. Hohenberger's data showed improved 5-year survival (15% improvement) and higher lymph node yield. It's becoming standard oncologic practice."}
],

"Open Right Hemicolectomy": [
    {"question": "Why does the ascending colon lack a mesentery while the transverse colon has one, embryologically?",
     "answer": "During midgut rotation, the ascending colon's mesentery fuses with the posterior body wall (Toldt's fusion fascia), making it retroperitoneal. The transverse colon retains its dorsal mesentery (transverse mesocolon) because it doesn't fuse with the posterior wall."},
    {"question": "When performing a Kocher maneuver during open right hemicolectomy, what key structures are at risk?",
     "answer": "The IVC (directly posterior to D2/D3 duodenum), right gonadal vein, right ureter, and the head of the pancreas. The Kocher mobilizes the duodenum and pancreatic head medially off the retroperitoneum."},
    {"question": "What is the marginal artery of Drummond and where is it most tenuous near the right colon?",
     "answer": "A continuous arterial arcade along the mesenteric border of the colon formed by anastomoses between ileocolic, right colic, and middle colic arteries. It is most tenuous (or absent) near the cecum and at the splenic flexure — relevant for ensuring adequate blood supply to the anastomosis."},
    {"question": "What is an internal hernia through the ileocolic mesenteric defect, and how do you prevent it?",
     "answer": "After right hemicolectomy, a mesenteric defect at the ileocolic anastomosis can allow small bowel herniation, causing obstruction. Prevention: close the mesenteric defect with a running absorbable suture, though debate exists on whether this increases stricture risk."},
    {"question": "What is the Turnbull 'no-touch' technique and what is its relevance to right hemicolectomy?",
     "answer": "Early ligation of the vascular pedicle and lymphatic drainage before tumor manipulation, to prevent tumor cell dissemination. Turnbull's original data from the Cleveland Clinic showed improved survival, though modern RCTs have not confirmed the benefit. Many surgeons still practice early pedicle ligation as standard oncologic technique."}
],

"Robotic Right Hemicolectomy": [
    {"question": "The hepatic flexure is tethered by which peritoneal attachments that must be divided, and what is their embryologic origin?",
     "answer": "The hepatocolic ligament, nephrocolic ligament, and duodenocolic ligament — all remnants of the dorsal mesentery fusion with the retroperitoneum (Toldt's fascia). The hepatocolic ligament often contains an accessory right colic vein."},
    {"question": "During robotic dissection, what is the 'superior mesenteric vein (SMV) first' approach?",
     "answer": "Identifying the SMV at the inferior border of the pancreas as the first step of medial dissection. The ileocolic pedicle is traced to its origin on the SMV/SMA, ensuring a high tie for complete mesocolic excision. The SMV serves as the medial boundary of dissection."},
    {"question": "What is the gastrocolic trunk of Henle, and why is its injury particularly dangerous during robotic right hemicolectomy?",
     "answer": "A short trunk formed by the right gastroepiploic vein, right colic vein, and/or anterior superior pancreaticoduodenal vein draining into the SMV. It's 1-2cm long, thin-walled, and hidden behind the pancreas — avulsion from the SMV causes major venous hemorrhage that is extremely difficult to control robotically."},
    {"question": "What specific complication is more commonly reported with intracorporeal anastomosis during robotic right hemicolectomy compared to extracorporeal?",
     "answer": "Staple line bleeding from the common enterotomy closure, since it's sewn intracorporeally. However, intracorporeal anastomosis has lower rates of incisional hernia, less narcotic use, and faster return of bowel function (reduced mesenteric twist and traction compared to exteriorization)."},
    {"question": "What is the D3 lymph node dissection in the context of right-sided colon cancer, and what does it add?",
     "answer": "Dissection of lymph nodes along the surgical trunk (origin of the feeding vessels from SMA/SMV), adding nodes along the root of the ileocolic and right colic pedicles. Japanese data suggests improved staging and possible survival benefit; it is integral to CME and more precisely performed robotically due to magnified visualization."}
],

"Extended Right Hemicolectomy": [
    {"question": "The splenic flexure represents the embryologic junction of which two gut divisions, and what nerve supplies each?",
     "answer": "Midgut (vagus nerve, parasympathetic) and hindgut (pelvic splanchnic nerves S2-S4, parasympathetic). The splenic flexure is the 'watershed' where two different autonomic and arterial supplies meet."},
    {"question": "What specific ligament must be divided to mobilize the splenic flexure, and what organ is at greatest risk?",
     "answer": "The splenocolic ligament. The spleen is at greatest risk — traction injury to the splenic capsule or short gastric vessels can cause hemorrhage requiring splenectomy. Reported incidence of iatrogenic splenic injury during splenic flexure mobilization is 1-8%."},
    {"question": "In an extended right hemicolectomy, the middle colic artery is ligated. Where does it arise and what does the left branch supply?",
     "answer": "The middle colic artery arises from the SMA just below the inferior border of the pancreas. The left branch supplies the distal transverse colon and contributes to the marginal artery at the splenic flexure. Its ligation makes the descending colon dependent on the left colic artery (from IMA) via the marginal artery."},
    {"question": "After extended right hemicolectomy, what is the risk of anastomotic ischemia at the ileodescending anastomosis?",
     "answer": "Higher than standard right hemicolectomy because the descending colon now depends solely on IMA blood supply via the left colic artery. If the marginal artery is tenuous (Griffiths' point), the proximal descending colon may be ischemic. Always assess for pulsatile bleeding at the cut edge and consider ICG fluorescence angiography."},
    {"question": "What is the indication for extended right hemicolectomy over standard right hemicolectomy for a hepatic flexure cancer?",
     "answer": "Cancers at the hepatic flexure or proximal transverse colon require extended right hemicolectomy to include the middle colic artery pedicle and its lymphatic basin. The oncologic principle: the resection must include the primary feeding vessel and all draining lymph nodes to its origin."}
],

"Laparoscopic Left Colectomy": [
    {"question": "The hindgut gives rise to which colonic segments, and what is the key difference in blood supply compared to the midgut-derived colon?",
     "answer": "Distal 1/3 of transverse colon, descending colon, sigmoid, and upper rectum. Blood supply is from the IMA (not SMA), with fewer named branches and a less robust marginal artery — making the left colon more vulnerable to ischemia."},
    {"question": "During left colectomy, what is the 'medial-to-lateral' approach and what is the first structure identified?",
     "answer": "Starting dissection at the IMA pedicle in the midline, developing the embryologic plane between mesocolon and retroperitoneum before dividing lateral attachments. The first structure identified is the IMA at its origin from the aorta, just below the duodenum (D3/D4 junction)."},
    {"question": "What is the relationship between the IMA and the left ureter, and at what point are they closest?",
     "answer": "The left ureter crosses posterior to the IMA at the pelvic brim, near the bifurcation of the common iliac artery. They are closest where the ureter passes under the IMA pedicle — this is the #1 site for ureteral injury during left colectomy."},
    {"question": "What is the clinical significance of Griffiths' point and Sudeck's point in left colectomy?",
     "answer": "Griffiths' point: watershed area at the splenic flexure between middle colic (SMA) and left colic (IMA) — marginal artery may be absent here in 5%. Sudeck's critical point: the last sigmoid artery branch before the superior rectal artery — ligation below this risks rectal stump ischemia. Both are critical for predicting anastomotic blood supply."},
    {"question": "In a left colectomy for diverticular disease, where should you place your distal margin and why?",
     "answer": "On the upper rectum (below the sacral promontory), NOT the distal sigmoid. The distal sigmoid has the same structural deficiency (thickened taenia, high intraluminal pressure) that caused diverticulosis. Anastomosing sigmoid to sigmoid has a significantly higher recurrence rate (up to 12% vs <3%)."}
],

"Extended Left Colectomy": [
    {"question": "During fetal development, the left colon mesentery fuses posteriorly forming Toldt's fascia. How does this embryologic plane facilitate extended left colectomy?",
     "answer": "The fusion plane between the descending mesocolon and Gerota's fascia/retroperitoneum is avascular and can be developed bluntly, allowing rapid mobilization of the entire left colon from the retroperitoneum while protecting the ureter, gonadal vessels, and kidney."},
    {"question": "In extended left colectomy, the middle colic artery's left branch and the IMA are both divided. What remains to supply the anastomosis?",
     "answer": "The right branch of the middle colic artery and the marginal artery (of Drummond) from the right side supply the remaining proximal transverse colon. The rectal stump is supplied by the superior rectal artery. ICG angiography is highly valuable here to confirm perfusion."},
    {"question": "What is the arc of Riolan (meandering mesenteric artery) and when is it most clinically relevant?",
     "answer": "A large, inconsistent arterial anastomosis connecting the SMA and IMA circulations, running through the base of the mesentery. It is most developed when one system is chronically occluded (e.g., IMA stenosis) — ligating it during extended resection in such patients can cause catastrophic ischemia of the remaining colon."},
    {"question": "What is the most dangerous complication specific to the transverse colon-rectal anastomosis in extended left colectomy?",
     "answer": "Anastomotic leak due to the long mesenteric reach required — the transverse colon must reach the pelvis without tension. This requires full mobilization of the hepatic flexure and often division of the right branch of the middle colic artery. Leak rates are higher (8-12%) than standard left colectomy."},
    {"question": "When is an extended left colectomy preferred over subtotal colectomy for obstructing left colon cancer?",
     "answer": "When the proximal colon is not significantly dilated and is viable. If the cecum is dilated >12cm, thin-walled, or questionably viable from back-pressure, a subtotal colectomy with ileorectal anastomosis is safer. Extended left colectomy preserves the right colon and ileocecal valve, reducing diarrhea."}
],

"Laparoscopic Sigmoid Colectomy": [
    {"question": "The sigmoid colon has a true mesentery unlike the descending colon. What embryologic event accounts for this difference?",
     "answer": "The sigmoid retains its dorsal mesentery because, unlike the descending colon, it does not fuse with the posterior abdominal wall during development. This is why the sigmoid is intraperitoneal (mobile) while the descending colon is secondarily retroperitoneal."},
    {"question": "What is the 'critical view' in sigmoid colectomy — specifically, what must you identify before dividing the IMA pedicle?",
     "answer": "The left ureter and left gonadal vessels must be visualized sweeping posteriorly in the retroperitoneum, confirmed by peristalsis of the ureter. The hypogastric nerve plexus (presacral nerves) should also be identified and preserved posterior to the IMA."},
    {"question": "Should you ligate the IMA at its origin or preserve the left colic artery for sigmoid colectomy? What's the evidence?",
     "answer": "For cancer: high ligation at the aortic origin (for lymph node yield). For diverticular disease: preserving the left colic artery is acceptable and may reduce anastomotic leak by maintaining better proximal perfusion. The HIGHLOW trial (2023) showed no difference in lymph node yield or oncologic outcomes between high and low IMA ligation."},
    {"question": "What are the hypogastric nerves and what happens if they are injured during sigmoid mobilization?",
     "answer": "The superior hypogastric plexus (presacral nerves) runs over the sacral promontory and bifurcates into left and right hypogastric nerves. Injury causes retrograde ejaculation and bladder dysfunction in men, and sexual/bladder dysfunction in women. They are at greatest risk during posterior rectal mobilization and IMA pedicle dissection."},
    {"question": "For diverticular disease, what is the Hinchey classification and how does it dictate operative strategy?",
     "answer": "Hinchey I: pericolic abscess (antibiotics ± drainage). Hinchey II: pelvic abscess (percutaneous drainage). Hinchey III: purulent peritonitis (resection with anastomosis ± diversion, or laparoscopic lavage per LOLA/SCANDIV trials). Hinchey IV: fecal peritonitis (Hartmann's procedure or resection with anastomosis and proximal diversion). The LADIES trial showed laparoscopic lavage was non-inferior to sigmoid resection for Hinchey III."}
],

"Open Sigmoid Colectomy": [
    {"question": "What is the embryologic basis for the variable length of the sigmoid mesocolon, and how does a long sigmoid predispose to volvulus?",
     "answer": "Variable retention of the dorsal mesentery during development. A long, redundant sigmoid mesocolon with a narrow base creates a predisposition to axial rotation (volvulus) — this is more common in populations with high-fiber diets (longer colons) and in neuropsychiatric patients with chronic constipation."},
    {"question": "During open sigmoid colectomy, you enter the peritoneal reflection at the 'white line of Toldt.' What anatomic layer are you entering?",
     "answer": "The avascular fusion plane between the visceral peritoneum of the sigmoid mesocolon and the parietal peritoneum overlying the retroperitoneum. This is the lateral-to-medial equivalent of the embryologic plane."},
    {"question": "What are the sigmoid arteries and how many typically exist?",
     "answer": "2-4 branches arising from the IMA between the left colic artery and the superior rectal artery. They form arcades in the sigmoid mesocolon. The most distal sigmoid artery (Sudeck's critical point) is the last branch before the superior rectal artery — its preservation determines rectal stump blood supply."},
    {"question": "In Hartmann's reversal after open sigmoid colectomy, what is the most common complication, and what percentage of patients never get reversed?",
     "answer": "Anastomotic leak (4-16%). Approximately 30-50% of patients who undergo Hartmann's procedure never undergo reversal, due to comorbidities, patient preference, or surgical complexity of the re-operation."},
    {"question": "When managing sigmoid volvulus, what is the success rate of endoscopic decompression and what mandates urgent surgery?",
     "answer": "Endoscopic decompression succeeds in 60-80% but recurrence is 40-60%. Urgent surgery is mandated by: mucosal necrosis on endoscopy (black/dusky mucosa), perforation, peritonitis, or failed decompression. A gangrenous sigmoid requires resection without decompression attempt."}
],

"Robotic Sigmoid Colectomy": [
    {"question": "What is the relationship of the sigmoid colon to the left gonadal vessels embryologically, and why is this relevant robotically?",
     "answer": "The gonadal vessels descend retroperitoneally from the mesonephric ridge during development, passing posterior to the sigmoid mesocolon. During robotic medial-to-lateral dissection, the enhanced 3D magnification allows precise identification of the gonadals beneath the mesocolon before they can be inadvertently divided."},
    {"question": "What is the inferior mesenteric vein's relationship to the ligament of Treitz, and why does it matter during robotic sigmoid colectomy?",
     "answer": "The IMV runs along the left side of the ligament of Treitz (duodenojejunal flexure) before joining the splenic vein behind the pancreas. During high ligation of the IMA, the IMV may need separate division; its injury near the pancreas can cause difficult-to-control retroperitoneal hemorrhage."},
    {"question": "The superior rectal artery is the terminal branch of which vessel, and how do you ensure adequate rectal stump perfusion?",
     "answer": "Terminal continuation of the IMA after the last sigmoid branch. Rectal stump perfusion is confirmed by brisk bleeding from the rectal stump, preserved pulsation of the mesorectum, and ideally ICG fluorescence angiography. The middle rectal arteries (from internal iliac) provide collateral supply."},
    {"question": "What is the advantage of robotic surgery for low pelvic dissection in sigmoid colectomy with a low rectal anastomosis?",
     "answer": "Wristed instruments allow precise dissection in the narrow male pelvis, better visualization of the autonomic nerve plexus (hypogastric and pelvic splanchnic nerves), and ergonomic stapler placement. This translates to lower conversion rates and potentially lower rates of genitourinary dysfunction."},
    {"question": "What is the 'critical view' before firing a rectal stapler, and what are the requirements for a safe colorectal anastomosis?",
     "answer": "Requirements: 1) No tension on the anastomosis, 2) Adequate blood supply (confirmed by ICG or bleeding), 3) Complete donuts from the circular stapler, 4) Negative air leak test (proctoscopy with insufflation under saline), 5) Well-perfused, non-irradiated tissue. Incomplete donuts mandate re-stapling or hand-sewn reinforcement."}
],

"Laparoscopic Low Anterior Resection": [
    {"question": "The rectum develops from which portion of the cloaca, and what embryologic structure separates it from the urogenital sinus?",
     "answer": "The dorsal portion of the hindgut cloaca. The urorectal septum (Tourneaux and Rathke folds) separates the rectum posteriorly from the urogenital sinus anteriorly by week 7. Failure of septation causes persistent cloaca or rectourethral/rectovaginal fistulae."},
    {"question": "What is the total mesorectal excision (TME) plane, and what landmark defines the correct posterior dissection plane?",
     "answer": "TME follows the avascular areolar plane between the visceral mesorectal fascia (encasing the rectum and its lymphovascular supply) and the parietal presacral fascia (Waldeyer's fascia). Posteriorly, the 'holy plane' of Heald is entered just behind the superior rectal artery — staying in this plane avoids presacral venous plexus hemorrhage and autonomic nerve injury."},
    {"question": "What are the 'columns of blood supply' to the rectum, and which is sacrificed in LAR?",
     "answer": "Superior rectal artery (from IMA) — sacrificed in LAR. Middle rectal arteries (from internal iliac) — preserved, supply mid-rectum laterally. Inferior rectal arteries (from internal pudendal) — preserved, supply anal canal. After IMA ligation, the rectal stump depends on middle and inferior rectal arteries."},
    {"question": "What is the low anterior resection syndrome (LARS), and what is its incidence after ultralow LAR?",
     "answer": "Disordered bowel function including urgency, frequency, clustering, incontinence, and incomplete evacuation after rectal resection. LARS affects 50-90% of patients after ultralow LAR. It results from loss of the rectal reservoir, nerve injury, and sphincter dysfunction from stapling. The LARS score quantifies severity; J-pouch or transverse coloplasty can reduce it."},
    {"question": "What is the current evidence for neoadjuvant therapy in rectal cancer, and what does the RAPIDO trial show?",
     "answer": "RAPIDO trial (2021): short-course radiation (5x5 Gy) followed by chemotherapy then TME surgery showed significantly lower disease-related treatment failure and higher pCR rates versus standard long-course chemoradiation. TNT (total neoadjuvant therapy) is now the preferred approach for locally advanced rectal cancer, with the added benefit of watch-and-wait for complete responders."}
],

"Open Low Anterior Resection": [
    {"question": "Waldeyer's fascia is a condensation of what embryologic tissue, and where does it attach?",
     "answer": "The rectosacral fascia (Waldeyer's) is a condensation of presacral endopelvic fascia from the parietal peritoneum. It extends from S2-S4 to the posterior mesorectum at the level of the anorectal junction. It must be divided sharply during posterior TME dissection to enter the presacral space."},
    {"question": "What is Denonvilliers' fascia and what happens if you dissect anterior to versus posterior to it?",
     "answer": "A thin fascial plane between the rectum and prostate/seminal vesicles (or vagina). Dissecting anterior to Denonvilliers' (closer to the prostate) risks injury to the neurovascular bundles and prostate. Dissecting posterior to it (closer to the rectum) is oncologically appropriate for anterior tumors and preserves autonomic nerves."},
    {"question": "What is the presacral venous plexus, and how do you manage catastrophic presacral hemorrhage?",
     "answer": "A valveless venous plexus (Batson's plexus) communicating with the internal vertebral venous system, directly on the sacral periosteum. Bleeding is torrential and cannot be sutured (veins retract into sacral foramina). Management: direct pressure with a pelvic pack, thumbtack/sterile pin into the sacral foramen, oxidized cellulose packing, or muscle fragment welding."},
    {"question": "What is an anastomotic leak rate after open LAR, and what are the consequences of a pelvic leak specifically?",
     "answer": "Leak rates: 5-15% (higher for ultralow resections). Pelvic leak consequences: pelvic sepsis/abscess, need for diverting stoma or Hartmann's, increased risk of permanent stoma (up to 25%), significantly worse oncologic outcomes (increased local recurrence), and long-term pelvic fibrosis with poor functional outcomes."},
    {"question": "What are the indications for a diverting loop ileostomy in LAR?",
     "answer": "Anastomosis ≤6cm from anal verge, neoadjuvant radiation, male pelvis, positive air leak test, technical difficulty, tension or questionable blood supply, immunosuppression. The GRECCAR 5 trial suggested selective omission is safe in favorable cases, but most surgeons still divert for ultralow anastomoses. The ileostomy is typically reversed at 8-12 weeks after confirming anastomotic integrity with contrast enema."}
],

"Robotic Low Anterior Resection": [
    {"question": "What is the 'lateral ligament' of the rectum, and what structure within it must be preserved?",
     "answer": "A condensation of endopelvic fascia extending from the lateral pelvic sidewall to the mesorectum. It contains the middle rectal artery (inconsistently) and, critically, the pelvic splanchnic nerves (nervi erigentes) from S2-S4. Overzealous division causes parasympathetic nerve injury leading to bladder and sexual dysfunction."},
    {"question": "What specific advantage does the robotic platform offer for autonomic nerve preservation during TME?",
     "answer": "Wristed instruments and 10x magnified 3D visualization allow precise identification and preservation of the hypogastric nerves at the IMA origin, the hypogastric plexus over the sacral promontory, and the pelvic splanchnic nerves at the lateral pelvic sidewall. Studies show lower rates of genitourinary dysfunction with robotic versus laparoscopic TME (ROLARR trial subanalysis)."},
    {"question": "What is the blood supply to the rectal stump after IMA ligation in robotic LAR, and how do you confirm it?",
     "answer": "Middle rectal arteries (from internal iliac, present in ~50%) and inferior rectal arteries (from internal pudendal). Confirm with: ICG (indocyanine green) fluorescence angiography — the most reliable intraoperative method, showing real-time perfusion. Firefly technology on the da Vinci system is standard for this assessment."},
    {"question": "What is the ROLARR trial and what were its key findings?",
     "answer": "Robotic vs Laparoscopic Resection for Rectal Cancer (2017, JAMA): no significant difference in conversion to open surgery overall, but robotic approach showed significantly lower conversion rates in male patients and obese patients with narrow pelvis. No differences in oncologic outcomes, complications, or quality of life at 6 months."},
    {"question": "What is the 'watch and wait' protocol for rectal cancer and when can you avoid LAR entirely?",
     "answer": "For patients achieving clinical complete response (cCR) after neoadjuvant chemoradiation (no residual tumor on MRI, endoscopy, or biopsy), close surveillance can replace surgery. The International Watch & Wait Database shows 75-80% sustained cCR at 2 years. Regrowth is mostly luminal and salvageable. This approach preserves the rectum, avoids stoma, and maintains quality of life."}
],

"Hartmann Procedure": [
    {"question": "The Hartmann procedure was originally described for which pathology, not the indication it's most commonly used for today?",
     "answer": "Henri Hartmann described it in 1921 for obstructing rectal cancer (not diverticulitis). Today it's most commonly performed for complicated diverticulitis (Hinchey III/IV), sigmoid perforation, or obstructing left colon cancer with an unprepared bowel."},
    {"question": "Where should the rectal stump be divided and how should it be managed to facilitate future reversal?",
     "answer": "At the rectosigmoid junction (sacral promontory level) or proximal rectum. The stump should be: 1) stapled (not oversewn), 2) marked with a long non-absorbable suture to the anterior abdominal wall for identification at reversal, 3) left long enough to allow safe re-anastomosis. Some surgeons place a drain adjacent to the stump."},
    {"question": "What is the blood supply to the Hartmann rectal stump, and what causes stump blowout?",
     "answer": "Middle rectal arteries (from internal iliac) and inferior rectal arteries (from internal pudendal). Stump blowout occurs from: ischemia of the staple line (if divided too distally or excessive devascularization), retained fecal material below the staple line, or breakdown from ongoing sepsis. It presents as pelvic sepsis and may require washout and stump revision."},
    {"question": "What is the reversal rate after Hartmann's, and what factors predict a permanent stoma?",
     "answer": "Only 40-60% of patients ever undergo reversal. Factors predicting permanent stoma: age >70, ASA III-IV, malignancy (vs diverticulitis), Hinchey IV, complications from the index operation, and surgeon/patient reluctance. Reversal itself carries 4-16% leak rate and 15-25% morbidity."},
    {"question": "In the emergency setting, what is the evidence for primary anastomosis with diversion versus Hartmann's for perforated diverticulitis?",
     "answer": "The DIVERTI (French) and LADIES trials showed primary anastomosis with diverting ileostomy had lower morbidity than Hartmann's, with comparable mortality. Primary anastomosis achieves higher stoma reversal rates (70-80% vs 40-60%) and avoids the difficult pelvic re-operation of Hartmann reversal. It is now considered the preferred approach in hemodynamically stable patients with Hinchey III disease."}
],

"Total Abdominal Colectomy": [
    {"question": "Total abdominal colectomy removes tissue derived from which two embryologic gut divisions?",
     "answer": "Midgut (cecum through proximal 2/3 of transverse colon, supplied by SMA) and hindgut (distal 1/3 transverse through sigmoid, supplied by IMA). The watershed is at the splenic flexure."},
    {"question": "During total colectomy, both the SMA branches (ileocolic, right colic, middle colic) and IMA are divided. What structure's relationship to the IMA origin must you identify before ligation?",
     "answer": "The left ureter — it crosses the common iliac artery near the IMA origin and can be tented up with the IMA pedicle. Also, the presacral (superior hypogastric) nerve plexus lies directly posterior to the IMA at the aortic bifurcation and must be preserved."},
    {"question": "In an emergency total colectomy for fulminant C. difficile colitis, what intraoperative finding mandates colectomy over diverting loop ileostomy with colonic lavage?",
     "answer": "Full-thickness colonic necrosis, perforation, or megacolon. However, the 2011 Pittsburgh study (Neal et al.) showed that diverting loop ileostomy with intraoperative colonic vancomycin lavage reduced mortality from 50% to 19% in patients WITHOUT perforation or frank necrosis. Patient selection is critical."},
    {"question": "After total colectomy with ileorectal anastomosis, what is the expected long-term stool frequency and how do you counsel patients?",
     "answer": "4-6 loose bowel movements per day, often clustering. Fiber supplementation and loperamide help. Patients should be warned about nocturnal urgency and perianal skin irritation. Most adapt over 6-12 months but never achieve normal formed stool patterns. Adequate rectal compliance develops over time."},
    {"question": "What is the indication for total colectomy in a patient with an obstructing left colon cancer?",
     "answer": "When there is a synchronous right colon lesion, when the proximal colon is massively dilated/ischemic (cecal diameter >12cm), or in Lynch syndrome patients where the remaining colon is at high cancer risk. In the standard case of obstruction with a viable proximal colon, an extended left colectomy or on-table lavage with primary anastomosis is preferred."}
],

"Abdominoperineal Resection": [
    {"question": "The anal canal below the dentate line develops from what embryologic structure, and how does this relate to APR tumor spread?",
     "answer": "Ectoderm of the proctodeum (hindgut cloaca's external component). Below the dentate, lymphatic drainage goes to inguinal nodes (not mesenteric), and tumors have squamous histology. This dual embryologic origin explains why low rectal/anal cancers require APR — they can spread both cephalad (mesorectal) and laterally to inguinal basins."},
    {"question": "What is the 'cylindrical APR' technique described by Holm, and how does it differ from the traditional approach?",
     "answer": "Cylindrical APR involves a wider perineal excision with more perianal tissue (levator muscles divided from below, creating a cylinder rather than a 'waist' at the levator level). The traditional approach narrows at the levators, creating the highest positive CRM rate. Holm's technique reduces CRM+ rates from 40% to <15% for low rectal cancers."},
    {"question": "What is the blood supply to the perineum that must be controlled during the perineal phase of APR?",
     "answer": "Inferior rectal arteries (from internal pudendal artery, branch of internal iliac), middle rectal arteries (from internal iliac), and the perineal branch of the internal pudendal artery. The levator ani receives blood from the inferior gluteal artery. Presacral venous bleeding (Batson's plexus) is the most dangerous hemorrhage risk posteriorly."},
    {"question": "What is the perineal wound complication rate after APR, and what increases it?",
     "answer": "Perineal wound complications occur in 25-50% of patients: delayed healing, wound breakdown, abscess, sinus formation, and perineal hernia. Risk factors: neoadjuvant radiation (the single biggest risk factor), diabetes, obesity, malnutrition. Many surgeons now use myocutaneous flaps (VRAM or gracilis) for irradiated perineal wounds."},
    {"question": "What is the current role of APR given the success of sphincter-sparing approaches?",
     "answer": "APR is reserved for: tumors invading the external sphincter or levator muscles, tumors within 1-2cm of the anal verge where a distal margin cannot be achieved, patients with pre-existing fecal incontinence, and patients who fail watch-and-wait after neoadjuvant therapy with regrowth involving the sphincter. The rate of APR has decreased from 40% to <10% of rectal cancer resections."}
],

"Robotic Abdominoperineal Resection": [
    {"question": "The puborectalis muscle creates what anatomic landmark, and why is its complete excision important in APR for low rectal cancer?",
     "answer": "The puborectalis creates the anorectal angle (80-110 degrees) at the anorectal junction. Incomplete excision leaves tumor-bearing tissue behind, as the 'waist' of the specimen at the puborectalis/levator level is the most common site of positive circumferential resection margin (CRM). The cylindrical technique excises the levators en bloc."},
    {"question": "What specific advantage does the robotic platform provide for the abdominal phase of APR in the deep pelvis?",
     "answer": "Enhanced visualization and articulation in the deep narrow pelvis below the peritoneal reflection, where laparoscopic instruments lose their mechanical advantage. The robot facilitates precise dissection of Denonvilliers' fascia anteriorly, preservation of the hypogastric nerves laterally, and sharp division of Waldeyer's fascia posteriorly with reduced conversion rates."},
    {"question": "During APR, the inferior mesenteric artery is divided. What collateral pathway maintains blood flow to the remaining pelvic structures?",
     "answer": "The internal iliac artery system (middle and inferior rectal arteries, internal pudendal artery) maintains pelvic blood supply. The superior rectal artery (terminal IMA branch) is divided with the specimen. The SMA-to-IMA collateral (Arc of Riolan/marginal artery) is no longer relevant since the colon is divided and the rectum is removed."},
    {"question": "What is the incidence of perineal hernia after APR and how can it be prevented?",
     "answer": "5-10% incidence, higher after laparoscopic/robotic APR (due to intact peritoneum providing less adhesion barrier). Prevention: primary closure of the pelvic peritoneum, biologic mesh closure of the pelvic floor, omental pedicle flap to fill the dead space, or myocutaneous flap (VRAM). Symptomatic hernias require surgical repair."},
    {"question": "What are the current NCCN guidelines for neoadjuvant therapy before APR for a T3N1 distal rectal cancer?",
     "answer": "Total neoadjuvant therapy (TNT): short-course radiation (5x5 Gy) followed by FOLFOX/CAPOX x 4-6 months, then restage. If cCR → consider watch-and-wait. If partial/no response → APR. Alternatively, long-course chemoradiation (50.4 Gy + capecitabine) followed by consolidation chemo. The goal is maximum tumor response to potentially avoid APR entirely."}
],

"End Colostomy Creation": [
    {"question": "What embryologic feature makes the descending/sigmoid colon ideal for end colostomy — specifically regarding its peritoneal relationship?",
     "answer": "The descending colon is secondarily retroperitoneal (fused mesentery), providing a natural retroperitoneal tunnel for stoma creation through the abdominal wall. The sigmoid has a mesentery, allowing it to be brought to the surface without tension. Both maintain reliable blood supply from IMA branches."},
    {"question": "Through which abdominal wall layers should the colostomy trephine pass, and what is the ideal size?",
     "answer": "Skin (circular excision) → subcutaneous fat → anterior rectus sheath → rectus abdominis muscle (split, not divided) → posterior rectus sheath → peritoneum. The trephine should admit two fingers (approximately 2.5-3cm) — too tight causes ischemia and stenosis, too wide causes parastomal hernia."},
    {"question": "What is the blood supply to the stoma, and what clinical finding at 24 hours indicates ischemia?",
     "answer": "The sigmoid branch of the IMA via the marginal artery. At 24 hours: a dusky, blue-black, or pale stoma (not the normal beefy red/pink) indicates ischemia. Use a test tube or transparent device to examine mucosal color at depth — if only superficial and the deeper mucosa is pink, it will likely survive. If ischemia extends below fascial level, revision is needed."},
    {"question": "What is the most common long-term complication of end colostomy, and what are the risk factors?",
     "answer": "Parastomal hernia (up to 50% at 5 years). Risk factors: obesity, COPD/chronic cough, steroid use, lateral to rectus placement, large fascial defect, malnutrition. Placement through the rectus muscle (not lateral to it) reduces but does not eliminate risk. Prophylactic mesh at index operation (PREVENT trial) reduces incidence to ~15%."},
    {"question": "What is the Brooke maturation technique for a colostomy, and how does it differ from a flush stoma?",
     "answer": "Brooke maturation: the bowel is everted 2-3cm above skin level and sutured to the dermis (not just the epidermis), creating a rosebud appearance. This is actually more relevant for ileostomies (to prevent enzyme-rich effluent from contacting skin). For colostomies, a flush or slightly raised stoma is adequate because the effluent is formed and less caustic. Most surgeons mature colostomies with slight eversion."}
],

"Loop Colostomy": [
    {"question": "The transverse colon retains its dorsal mesentery. Why does this make it the preferred site for a loop colostomy?",
     "answer": "The retained transverse mesocolon provides a long, mobile mesentery allowing the colon to reach the anterior abdominal wall without tension. The descending colon (fixed retroperitoneum) and sigmoid (variable mesentery length) have less reliable mobility for loop formation."},
    {"question": "What is the purpose of the supporting rod or bridge in a loop colostomy, and when is it removed?",
     "answer": "The rod prevents retraction of the loop back into the abdomen during the first 5-10 days while adhesions form between the bowel serosa and the abdominal wall. It is removed once the stoma is adherent (typically 7-10 days). Premature removal risks stoma retraction and peritonitis."},
    {"question": "In a loop colostomy, which limb is the proximal (functioning) limb, and how do you orient it?",
     "answer": "The proximal (afferent) limb should be positioned superiorly/cranially so stool exits into the appliance's upper pouch. The distal (efferent/defunctioned) limb sits inferiorly. Incorrect orientation makes appliance management extremely difficult. The proximal limb is confirmed by tracing the colon from cecum distally."},
    {"question": "What is the most common reason for loop colostomy failure to divert fecal stream, and how do you manage it?",
     "answer": "Incomplete division of the posterior wall (the 'spur' between limbs is too low), allowing stool to pass into the distal limb. This defeats the purpose of diversion (e.g., for distal anastomotic protection or perineal wound healing). Management: revision to completely divide the posterior wall or conversion to end stoma."},
    {"question": "When is a loop colostomy preferred over a loop ileostomy for fecal diversion?",
     "answer": "Loop colostomy is preferred when: 1) protecting a distal colorectal anastomosis where ileostomy effluent would bypass too much absorptive colon, 2) obstructing distal colonic lesion needing proximal decompression, 3) perianal/perineal sepsis (Fournier's). Loop ileostomy is generally preferred for most temporary diversions due to easier reversal and lower parastomal hernia rates."}
],

"Loop Ileostomy": [
    {"question": "The ileum derives from which embryologic gut segment, and what is the clinical significance of Meckel's diverticulum near a loop ileostomy?",
     "answer": "Midgut (post-arterial segment). Meckel's diverticulum (remnant of the omphalomesenteric/vitelline duct) occurs in 2% of the population, ~60cm from the ileocecal valve. If encountered during ileostomy creation, it should be noted but not routinely resected unless symptomatic or pathologic — resecting it complicates an otherwise straightforward diversion."},
    {"question": "Where should a loop ileostomy be sited preoperatively, and what landmarks must it avoid?",
     "answer": "Through the rectus abdominis muscle, in the right lower quadrant, at the apex of the infraumbilical fat fold. Must avoid: skin creases, belt line, umbilicus, bony prominences (ASIS, costal margin), previous scars, and the planned midline incision. Preoperative stoma marking by an enterostomal therapist is mandatory when possible."},
    {"question": "What is the blood supply to the loop ileostomy, and how do you prevent mesenteric twist?",
     "answer": "Ileal branches of the SMA via the vasa recta and marginal arcade. Mesenteric twist (180° or 360°) is prevented by: ensuring the mesentery is oriented correctly before passing through the abdominal wall (no twists), creating an adequately sized trephine, and confirming pink viable mucosa after maturation."},
    {"question": "What is high-output ileostomy, and at what threshold does it become dangerous?",
     "answer": "Output >1500-2000 mL/day. Causes severe dehydration, hyponatremia, hypokalemia, hypomagnesemia, and acute kidney injury. Management: loperamide (up to 16mg/day), codeine phosphate, oral rehydration solution (WHO recipe — NOT free water), dietary modification (avoid hypotonic fluids), and in refractory cases, octreotide or IV fluid supplementation. AKI from ileostomy dehydration is the most common cause of readmission after LAR."},
    {"question": "What is the closure rate and complication rate of loop ileostomy reversal?",
     "answer": "Reversal rate: 70-80% (higher than loop colostomy). Complication rate: 15-30%, including anastomotic leak (1-3%), wound infection (5-15%), small bowel obstruction (5-10% — the most common cause of readmission), and prolonged ileus. Timing: 8-12 weeks after index operation, after confirming anastomotic integrity with water-soluble contrast enema."}
],

"Ostomy Reversal": [
    {"question": "After prolonged fecal diversion, the defunctionalized colon undergoes what histologic changes, and what is this called?",
     "answer": "Diversion colitis — mucosal atrophy, lymphoid follicular hyperplasia, and inflammation caused by lack of short-chain fatty acid (SCFA) nutrition from the fecal stream. It occurs in virtually all diverted segments. Treatment is reversal itself; short-chain fatty acid enemas can temporize symptoms."},
    {"question": "During ostomy reversal, what are the critical steps in mobilizing the stoma from the abdominal wall?",
     "answer": "1) Circumferential skin incision around the mucocutaneous junction, 2) Sharp dissection through subcutaneous tissue to the fascial level, 3) Careful separation of bowel from fascia (adhesions here risk enterotomy), 4) Division of any adhesions to the fascial ring, 5) Delivery of bowel with adequate length for fresh anastomosis. The most dangerous step is freeing the bowel from the posterior rectus sheath where it is most adherent."},
    {"question": "What determines whether you can do a local (peristomal) reversal versus a formal laparotomy?",
     "answer": "Local reversal is appropriate for: loop ileostomy with adequate mobility, no suspected intra-abdominal adhesions, and ability to perform a hand-sewn or stapled anastomosis through the stoma site. Formal laparotomy is needed for: end stoma (Hartmann's reversal), significant adhesions, need for intra-abdominal dissection, or when the distal segment cannot be identified locally."},
    {"question": "What is the most common complication after Hartmann's reversal specifically, and what is the mortality?",
     "answer": "Anastomotic leak (4-16%), with an overall morbidity of 25-50% and mortality of 1-4%. The difficulty is finding and mobilizing the short, retracted rectal stump in a scarred, irradiated pelvis. Other complications: small bowel injury during adhesiolysis (10%), wound infection, and prolonged ileus."},
    {"question": "What preoperative study must be obtained before any ostomy reversal involving a distal anastomosis?",
     "answer": "Water-soluble contrast enema (Gastrografin, NOT barium) to confirm: 1) anastomotic integrity (no leak), 2) no anastomotic stricture, 3) patency of the distal segment. Additionally, endoscopic evaluation if malignancy was the original indication. Reversal should NEVER proceed if there is an anastomotic leak or significant stricture."}
],

"Total Gastrectomy": [
    {"question": "The stomach develops from the foregut. What embryologic rotation does it undergo, and how does this explain the position of the vagus nerves?",
     "answer": "The stomach rotates 90° clockwise along its longitudinal axis. The left vagus (originally anterior to esophagus) becomes the anterior vagal trunk, and the right vagus becomes the posterior trunk. This rotation also creates the lesser sac (omental bursa) posterior to the stomach."},
    {"question": "Name the five arterial supplies to the stomach and their origins.",
     "answer": "1) Left gastric artery (celiac trunk — largest supply), 2) Right gastric artery (proper hepatic/common hepatic), 3) Left gastroepiploic (splenic artery), 4) Right gastroepiploic (gastroduodenal artery), 5) Short gastric arteries (splenic artery). During total gastrectomy, ALL five are divided."},
    {"question": "What named artery must be specifically identified and ligated for a D2 lymphadenectomy during total gastrectomy?",
     "answer": "The left gastric artery at its origin from the celiac trunk — station 7 nodes surround it. Also the splenic artery nodes (station 11) and common hepatic artery nodes (station 8). A D2 dissection includes stations 1-12 and requires ≥15 lymph nodes for adequate staging."},
    {"question": "What is the most feared metabolic complication of total gastrectomy that presents years later?",
     "answer": "Vitamin B12 deficiency leading to megaloblastic anemia and subacute combined degeneration of the spinal cord. Without intrinsic factor (produced by gastric parietal cells), B12 cannot be absorbed. Patients need lifelong parenteral B12 supplementation (monthly IM injections). Also: iron deficiency anemia (loss of acid for iron absorption), calcium malabsorption, and dumping syndrome."},
    {"question": "In constructing a Roux-en-Y esophagojejunostomy after total gastrectomy, what is the minimum Roux limb length and why?",
     "answer": "40-60cm to prevent bile reflux esophagitis/esophagojejunal anastomotic injury. Bile reflux into the esophageal remnant causes severe inflammation and increases Barrett's-like changes. The afferent limb should be 40-50cm. A jejunal J-pouch (10-15cm) can be created to improve reservoir function and quality of life."}
],

"Laparoscopic Total Gastrectomy": [
    {"question": "The greater omentum develops from which embryologic mesentery, and what is its clinical significance in gastric cancer surgery?",
     "answer": "The dorsal mesogastrium. As the stomach rotates, the dorsal mesogastrium elongates and drapes inferiorly to form the greater omentum. It must be included in the resection (omentectomy) for gastric cancer because it contains lymph nodes (station 4) and may harbor tumor deposits. En bloc omentectomy is standard for T3-T4 tumors."},
    {"question": "What is the 'infrapyloric space' and why is it a critical dissection zone during laparoscopic total gastrectomy?",
     "answer": "The space below the pylorus containing station 6 lymph nodes along the right gastroepiploic artery. The right gastroepiploic vessels, gastroduodenal artery, and the anterior superior pancreaticoduodenal artery are all in close proximity. Injury to the GDA causes hemorrhage; injury to the pancreas causes fistula (2-5% incidence)."},
    {"question": "What is the arterial supply that must remain intact to ensure viability of the Roux limb after total gastrectomy?",
     "answer": "The jejunal branches of the SMA and specifically the marginal jejunal arcade. When creating the Roux limb, ensure adequate mesenteric length without tension by dividing mesentery only at the proximal transection site. The Roux limb's blood supply comes from its intact mesentery — excessive skeletonization causes ischemia at the esophagojejunal anastomosis."},
    {"question": "What is an intracorporeal esophagojejunostomy, and what are the techniques available laparoscopically?",
     "answer": "The anastomosis performed entirely inside the abdomen: 1) Circular stapler (OrVil device — anvil delivered transorally), 2) Linear stapler (overlap or functional end-to-end technique), 3) Hand-sewn (rarely). The OrVil technique delivers the circular stapler anvil through the mouth and esophageal stump. Leak rates are comparable (3-5%) but the linear stapler method is gaining favor due to lower stricture rates."},
    {"question": "What does the JCOG0501 trial tell us about splenectomy during total gastrectomy for proximal gastric cancer?",
     "answer": "JCOG0501 (2021): spleen-preserving D2 dissection is non-inferior to splenectomy for overall survival in proximal gastric cancer not involving the greater curvature. Splenectomy increases morbidity (infection, pancreatic fistula, thrombocytosis) without oncologic benefit. Splenectomy is only indicated when tumor directly invades the spleen or there are bulky station 10 (splenic hilum) nodes."}
],

"Robotic Total Gastrectomy": [
    {"question": "The lesser omentum develops from which embryologic mesentery, and what critical structure runs within it?",
     "answer": "The ventral mesogastrium. The hepatoduodenal ligament (part of the lesser omentum) contains the portal triad: common bile duct (right), hepatic artery proper (left), and portal vein (posterior). The lesser omentum also contains the left and right gastric vessels and station 1, 3, and 5 lymph nodes."},
    {"question": "During robotic D2 lymphadenectomy, what is station 12a and why is it particularly challenging?",
     "answer": "Station 12a is the hepatoduodenal ligament nodes along the proper hepatic artery. Dissection requires skeletonizing the hepatic artery, portal vein, and CBD — injury to any causes catastrophic complications. The robotic wristed instruments excel here because of the precise dissection required around these delicate structures in a confined space."},
    {"question": "What is the celiac trunk anatomy and its most common variant encountered during robotic gastrectomy?",
     "answer": "Classic celiac trunk: left gastric, common hepatic, and splenic arteries (Haller's tripod, present in ~85%). Most common variant: hepatogastric trunk with the splenic artery arising independently from the aorta. A replaced left hepatic artery from the left gastric artery occurs in 10-15% — if not recognized and ligated, it causes left hepatic lobe ischemia."},
    {"question": "What is the pancreatic fistula rate after robotic total gastrectomy, and what causes it?",
     "answer": "3-8%, caused by thermal or mechanical injury to the pancreatic body/tail during dissection of station 11 (splenic artery) nodes, omentectomy along the inferior pancreatic border, or retraction injury. It presents as amylase-rich drain output (>3x serum amylase on POD3, per ISGPF definition). Most are grade A/B managed conservatively; grade C (sepsis, hemorrhage) requires intervention."},
    {"question": "What is the role of perioperative chemotherapy for gastric cancer, and what regimen does the FLOT4 trial support?",
     "answer": "FLOT4 (2019, Lancet): perioperative FLOT (5-FU, leucovorin, oxaliplatin, docetaxel) x 4 cycles pre- and post-op showed significantly improved overall survival versus ECF/ECX (median OS 50 vs 35 months). FLOT4 is now the standard of care for ≥T2 or node-positive gastric cancer in the West. In the East, adjuvant S-1 (ACTS-GC) or adjuvant CAPOX (CLASSIC trial) after D2 gastrectomy is standard."}
],

"Subtotal Gastrectomy with Billroth I": [
    {"question": "During embryologic foregut rotation, the duodenum becomes secondarily retroperitoneal. Which part of the duodenum remains intraperitoneal and is used for the Billroth I anastomosis?",
     "answer": "The first part of the duodenum (D1, or the duodenal bulb) remains intraperitoneal, covered by peritoneum anteriorly and superiorly. This mobility allows it to be anastomosed directly to the gastric remnant. D2-D4 are retroperitoneal and fixed."},
    {"question": "In a Billroth I reconstruction, what is the minimum proximal margin required for gastric cancer, and how does it differ by Lauren classification?",
     "answer": "Intestinal type: 3cm gross margin (well-circumscribed). Diffuse type (linitis plastica): 5-8cm margin due to submucosal spread that is not visible grossly. Frozen section of the proximal margin is mandatory — if positive, extend resection or convert to total gastrectomy."},
    {"question": "What happens to the left gastric artery blood supply after subtotal gastrectomy, and what maintains the remnant's viability?",
     "answer": "The left gastric artery is ligated at its origin (D2 lymphadenectomy). The gastric remnant survives on the short gastric arteries (from splenic artery) and left gastroepiploic artery (from splenic artery). The fundal remnant has a robust submucosal plexus that provides excellent collateral flow."},
    {"question": "What is the afferent loop syndrome and how does it present after Billroth I versus Billroth II?",
     "answer": "Afferent loop syndrome is unique to Billroth II (not Billroth I) because Billroth I has a direct gastroduodenostomy without afferent/efferent limbs. In Billroth II, the afferent limb (duodenal/jejunal) can become obstructed, causing bilious vomiting, RUQ pain, and elevated amylase. This is an advantage of Billroth I — no afferent loop syndrome."},
    {"question": "What is the long-term cancer risk in the gastric remnant after Billroth I, and when should surveillance begin?",
     "answer": "Remnant gastric cancer (stump cancer) develops in 1-3% of patients, usually >15-20 years post-surgery. It results from chronic bile reflux, chronic atrophic gastritis, and intestinal metaplasia at the anastomosis. Endoscopic surveillance should begin 15-20 years post-gastrectomy, with biopsies of the anastomotic line and gastric remnant."}
],

"Subtotal Gastrectomy with Billroth II": [
    {"question": "The Billroth II reconstruction creates a gastrojejunostomy. What embryologic gut segments are being anastomosed?",
     "answer": "Foregut (gastric remnant) to midgut (proximal jejunum). The duodenal stump is closed, creating a blind loop. This non-anatomic reconstruction is why Billroth II has more metabolic complications than Billroth I."},
    {"question": "What is the optimal length of the afferent limb in a Billroth II, and what happens if it's too long?",
     "answer": "15-20cm (measured from the ligament of Treitz). Too long: increased risk of afferent loop syndrome (obstruction, bilious vomiting, pancreatitis from stasis). Too short: tension on the anastomosis, kinking, and inability to reach the gastric remnant without tension."},
    {"question": "What is the blood supply to the closed duodenal stump, and what causes stump blowout?",
     "answer": "The gastroduodenal artery (from common hepatic), anterior and posterior superior pancreaticoduodenal arteries. Stump blowout (2-4% incidence, 20-30% mortality) occurs from: ischemia of the duodenal closure, distal duodenal obstruction (afferent loop), or erosion from adjacent drain/tube. It presents as sudden bilious drainage, sepsis, and RUQ pain on POD 3-7."},
    {"question": "What is dumping syndrome, and how does its mechanism differ between early and late dumping?",
     "answer": "Early dumping (15-30 min after eating): hyperosmolar chyme rapidly enters jejunum → fluid shift into bowel lumen → hypovolemia, tachycardia, cramping, diarrhea. Late dumping (1-3 hours): rapid glucose absorption → hyperinsulinemia → reactive hypoglycemia → diaphoresis, weakness, confusion. Treatment: small frequent meals, avoid simple sugars, lie down after meals. Refractory cases: octreotide or conversion to Roux-en-Y."},
    {"question": "What is the 'alkaline reflux gastritis' unique to Billroth II, and how do you manage it?",
     "answer": "Bile reflux into the gastric remnant causes chronic inflammation, pain, nausea, and bilious vomiting — worse than Billroth I because bile enters the stomach directly without a pyloric mechanism. Conservative management: sucralfate, cholestyramine, PPIs. Surgical management: conversion to Roux-en-Y gastrojejunostomy (definitive treatment, diverts bile 40-60cm downstream from the gastric remnant)."}
],

"Roux-en-Y Gastric Bypass": [
    {"question": "The jejunal Roux limb used in RYGB develops from which embryologic segment, and what is the clinical relevance of the ligament of Treitz?",
     "answer": "Midgut. The ligament of Treitz (suspensory ligament of the duodenum) marks the duodenojejunal junction and is the starting point for measuring the Roux limb and biliopancreatic limb. It is a musculofibrous band from the right crus of the diaphragm — its identification is the critical first step in RYGB construction."},
    {"question": "What are the three Roux limb configurations and their standard lengths in RYGB?",
     "answer": "1) Biliopancreatic (BP) limb: from Treitz to jejunojejunostomy (40-50cm), 2) Roux (alimentary) limb: from gastrojejunostomy to jejunojejunostomy (75-150cm, standard 100-150cm), 3) Common channel: from jejunojejunostomy to ileocecal valve (remainder of small bowel). Longer Roux limbs = more malabsorption/weight loss but more nutritional deficiency risk."},
    {"question": "What is the blood supply to the gastric pouch in RYGB, and why is it usually reliable?",
     "answer": "Left gastric artery branches and small lesser curve submucosal vessels. The pouch (15-30mL) is created along the lesser curve, preserving the left gastric artery's ascending branches. Despite dividing the main gastric blood supply, the rich submucosal plexus of the stomach makes ischemia extremely rare (<1%). This is in contrast to the jejunal Roux limb, where mesenteric tension can cause ischemia."},
    {"question": "What is a marginal ulcer after RYGB, and what are its causes?",
     "answer": "Ulceration at the gastrojejunal anastomosis (1-16% incidence). Causes: acid exposure (pouch too large, gastro-gastric fistula allowing parietal cell mass exposure), NSAIDs, smoking, Helicobacter pylori, ischemia, foreign body (retained suture/staples). Gastro-gastric fistula is the most important cause to rule out — it exposes the anastomosis to acid from the bypassed stomach."},
    {"question": "What are the three internal hernia sites after RYGB, and which is most common?",
     "answer": "1) Petersen's defect (between Roux limb mesentery and transverse mesocolon) — most common, 2) Jejunojejunostomy mesenteric defect, 3) Transverse mesocolon defect (if retrocolic Roux limb). All should be closed with non-absorbable suture. Internal hernias occur in 3-5% of patients and present with intermittent, crampy abdominal pain — CT shows mesenteric swirl sign. Untreated, they cause bowel ischemia."}
],

"Laparoscopic Sleeve Gastrectomy": [
    {"question": "The stomach's greater curvature receives blood from branches of which embryologic artery, and how does sleeve gastrectomy alter gastric blood supply?",
     "answer": "The celiac trunk via the left and right gastroepiploic arteries and short gastric arteries (all from the dorsal mesogastrium's vascular axis). Sleeve gastrectomy divides the short gastric and left gastroepiploic vessels, leaving the sleeve dependent on the right gastric artery (along lesser curve) and remaining left gastric artery branches. This is why ischemia at the proximal staple line near the GEJ is the most feared vascular complication."},
    {"question": "What is the distance from the pylorus where stapling should begin, and what happens if you start too close?",
     "answer": "4-6cm from the pylorus. Starting too close (<2cm) narrows the antrum, causing functional gastric outlet obstruction, prolonged nausea/vomiting, and increased intraluminal pressure leading to staple line leak. Starting too far (>6cm) leaves a large antral pouch that reduces restrictive weight loss effect."},
    {"question": "What size bougie should be used and how does it relate to the left gastric artery?",
     "answer": "32-40 French (most commonly 36Fr). The bougie guides the stapler parallel to the lesser curve. The left gastric artery runs in the lesser omentum, and the staple line parallels its branches — staying on the bougie prevents stapling too close to the lesser curve vessels, which would devascularize the sleeve."},
    {"question": "What is the staple line leak rate after sleeve gastrectomy, and where does it most commonly occur?",
     "answer": "1-3% overall. Most common location: the proximal staple line near the gastroesophageal junction (angle of His) — this area has the thinnest gastric wall, highest intraluminal pressure (high-pressure zone of LES), and most tenuous blood supply. Leaks here are notoriously difficult to manage and may require endoscopic stenting, drainage, or rarely esophagojejunostomy."},
    {"question": "What is the hormonal mechanism of weight loss after sleeve gastrectomy beyond simple restriction?",
     "answer": "Removal of the gastric fundus eliminates 80% of ghrelin-producing cells (the 'hunger hormone'), dramatically reducing appetite. Additionally: accelerated gastric emptying increases GLP-1 and PYY release from the distal ileum (incretin effect), improving insulin sensitivity independently of weight loss. This is why sleeve gastrectomy resolves type 2 diabetes in 60-70% of patients (comparable to RYGB for mild-moderate DM)."}
],

"Gastrorrhaphy for Perforated Ulcer": [
    {"question": "Peptic ulcers most commonly perforate at the anterior duodenum (D1). What embryologic feature makes the anterior surface vulnerable?",
     "answer": "The anterior duodenum is intraperitoneal and covered only by visceral peritoneum (no retroperitoneal reinforcement). Posterior ulcers erode into the retroperitoneum and the gastroduodenal artery (causing hemorrhage), while anterior ulcers perforate freely into the peritoneal cavity because there is no retroperitoneal tissue barrier."},
    {"question": "What is the Graham patch repair and what tissue is used?",
     "answer": "A pedicled omental (Graham) patch sutured over the perforation using 3-0 silk sutures placed through the healthy tissue on either side of the ulcer, with omentum laid over the defect and sutures tied over it. The omentum provides: blood supply for healing, fibrinous seal, and inflammatory response to contain contamination. The ulcer itself is NOT excised (unless concern for malignancy — must biopsy)."},
    {"question": "What is the blood supply to the omental patch, and what vessel supplies the greater omentum?",
     "answer": "The right and left gastroepiploic arteries (from GDA and splenic artery respectively), forming the gastroepiploic arcade along the greater curvature. The omentum has a rich vascular network allowing pedicled flaps to be mobilized extensively. In reoperations with prior omental loss, a falciform ligament patch can be used as an alternative."},
    {"question": "What is the 'definitive ulcer surgery' that was historically combined with perforation repair, and why is it rarely done today?",
     "answer": "Truncal vagotomy with pyloroplasty or highly selective vagotomy — performed to reduce acid secretion and prevent recurrence. Rarely done now because H. pylori eradication (triple therapy) and PPIs have reduced ulcer recurrence to <5%. Simple patch repair + H. pylori treatment + PPI is now standard. Exception: unstable patients where definitive surgery is contraindicated anyway."},
    {"question": "A perforated ulcer presents with pneumoperitoneum. What percentage of perforated ulcers will NOT show free air on upright CXR?",
     "answer": "15-20% of perforated ulcers will not show pneumoperitoneum on plain films. CT scan detects free air in >95%. If clinical suspicion is high despite negative plain films, get a CT. Do NOT delay surgery waiting for imaging in a patient with peritonitis and hemodynamic instability — the diagnosis is clinical."}
],

"Laparoscopic Nissen Fundoplication": [
    {"question": "The fundus of the stomach and the gastroesophageal junction develop from the foregut. What embryologic event creates the angle of His?",
     "answer": "Differential growth of the greater curvature (dorsal mesogastrium side) outpacing the lesser curvature creates the acute angle of His between the esophagus and gastric fundus. This angle creates a 'flap valve' that contributes to the lower esophageal sphincter mechanism. Its obliteration (by hiatal hernia or obesity) contributes to GERD."},
    {"question": "What are the five key steps of hiatal dissection for Nissen fundoplication?",
     "answer": "1) Division of the gastrohepatic ligament (pars flaccida approach — watch for replaced left hepatic artery), 2) Identification and preservation of anterior vagus nerve, 3) Circumferential esophageal mobilization creating a window behind the esophagus, 4) Identification and preservation of posterior vagus nerve, 5) Closure of the crural defect posterior to the esophagus with non-absorbable suture."},
    {"question": "What is the blood supply to the gastric fundus used for the wrap, and what must be divided to mobilize it?",
     "answer": "Short gastric arteries (2-6 branches from the splenic artery). These are divided to mobilize the fundus and allow a tension-free, 'floppy' wrap. Failure to divide short gastrics creates a tight wrap causing dysphagia. The fundus remains viable because of retrograde flow through the left gastroepiploic and submucosal gastric plexus."},
    {"question": "What is the 'slipped Nissen' and 'two-compartment stomach'?",
     "answer": "Occurs when the wrap migrates distally off the GEJ and sits around the proximal stomach body, creating two compartments: the gastric cardia/fundus above the wrap and the body below. Presents with dysphagia, inability to vomit, and recurrent reflux. It results from inadequate fixation of the wrap to the esophagus or failure to close the hiatus. Requires reoperation."},
    {"question": "What preoperative workup is mandatory before Nissen fundoplication, and what finding would make you choose a partial (Toupet) wrap instead?",
     "answer": "Mandatory: 1) EGD (rule out Barrett's, stricture, cancer), 2) Esophageal manometry, 3) 24-hour pH study (or BRAVO capsule). If manometry shows ineffective esophageal motility (>50% failed contractions or DCI <450 mmHg·s·cm), a partial posterior (Toupet, 270°) wrap is preferred over Nissen (360°) to reduce postoperative dysphagia. The DeMeester score on pH study confirms pathologic reflux (>14.72)."}
],

"Laparoscopic Toupet Fundoplication": [
    {"question": "The lower esophageal sphincter is not a true anatomic sphincter. What embryologic and physiologic components create the anti-reflux barrier?",
     "answer": "1) Intrinsic smooth muscle tone of the distal esophagus (LES pressure zone, 2-4cm), 2) Crural diaphragm (extrinsic compression, from septum transversum embryologically), 3) Angle of His (flap valve from differential foregut growth), 4) Phrenoesophageal ligament (membrane). The Toupet wrap augments the intrinsic LES pressure without completely encircling it."},
    {"question": "In a Toupet (270° posterior partial) wrap, what is the relationship of the wrap to the vagus nerves?",
     "answer": "The wrap is constructed posterior to the esophagus, with each tail sutured to the right and left esophageal walls. The posterior vagus nerve sits between the wrap and the esophagus — it must be identified and preserved, not incorporated into the wrap sutures. The anterior vagus is visible on the anterior esophageal surface and should be protected during hiatal dissection."},
    {"question": "What is the left gastric artery's relationship to the crural closure, and why is this relevant?",
     "answer": "The left gastric artery ascends in the lesser omentum toward the lesser curve, passing near the left crus. During posterior crural closure, aggressive suturing can inadvertently incorporate or kink the left gastric artery, potentially compromising blood supply to the lesser curve. Sutures should be placed in the crural muscle only, well away from the artery."},
    {"question": "What is the theoretical advantage of Toupet over Nissen for patients with esophageal dysmotility?",
     "answer": "The 270° wrap leaves the anterior esophagus unwrapped, creating less outflow resistance than a 360° Nissen. In patients with weak esophageal peristalsis, a Nissen can cause severe dysphagia because the esophagus cannot generate enough pressure to overcome the complete wrap. Toupet provides adequate reflux control (comparable to Nissen in most studies) with significantly lower dysphagia rates (5% vs 15-20%)."},
    {"question": "What is the recurrence rate of GERD after Toupet fundoplication compared to Nissen?",
     "answer": "GERD recurrence: Toupet 10-15% vs Nissen 5-10% at long-term follow-up (>5 years). The tradeoff is accepted because Toupet has significantly less dysphagia, gas-bloat syndrome, and inability to belch/vomit. The LOTUS trial and subsequent meta-analyses suggest comparable overall patient satisfaction between the two approaches."}
],

"Laparoscopic Heller Myotomy": [
    {"question": "Achalasia results from degeneration of what specific neural structure in the esophageal wall, and what embryologic cell population gives rise to these neurons?",
     "answer": "Degeneration of the myenteric (Auerbach's) plexus inhibitory neurons (which release nitric oxide and VIP) in the LES region. These neurons derive from vagal neural crest cells that migrate into the gut wall during weeks 4-7 of development. Loss of inhibitory input leaves excitatory (cholinergic) neurons unopposed, causing failure of LES relaxation."},
    {"question": "During Heller myotomy, the myotomy extends how far onto the gastric cardia and how far proximally on the esophagus?",
     "answer": "The myotomy extends 6-8cm proximally on the esophageal body and 2-2.5cm onto the gastric cardia (past the GEJ). The proximal extent treats the high-pressure zone of the LES. Extending too far onto the stomach (>3cm) causes iatrogenic GERD; not extending far enough leaves residual LES hypertension and persistent dysphagia."},
    {"question": "What is the blood supply at the gastroesophageal junction that must be preserved during myotomy?",
     "answer": "An ascending branch of the left gastric artery and the esophageal branches of the left inferior phrenic artery form a vascular plexus at the GEJ. These submucosal vessels are visible once the myotomy is performed — they run in the submucosa beneath the circular muscle. Injury causes bleeding that can be controlled with gentle pressure (not cautery, which risks mucosal perforation)."},
    {"question": "What is the most feared intraoperative complication of Heller myotomy, and how do you detect it?",
     "answer": "Esophageal or gastric mucosal perforation (5-10% incidence). Detected by: intraoperative endoscopy with air insufflation while the myotomy site is submerged in irrigation fluid — bubbles indicate perforation. Also perform direct visualization of the submucosa for mucosal bluish discoloration or visible lumen. If a perforation is found, repair it primarily with absorbable suture and cover with the fundoplication wrap."},
    {"question": "Why is a partial fundoplication (typically Dor anterior) added after Heller myotomy, and what does the POEM procedure omit?",
     "answer": "The myotomy destroys the intrinsic LES mechanism, predisposing to severe GERD. A Dor (anterior 180°) fundoplication prevents reflux and covers the exposed myotomy site (protecting against leak). POEM (peroral endoscopic myotomy) omits the fundoplication — resulting in GERD rates of 40-60% vs 10-15% with Heller + Dor. This is the main disadvantage of POEM and why many surgeons prefer Heller + partial fundoplication."}
],

"Pancreaticoduodenectomy (Whipple)": [
    {"question": "The head of the pancreas and duodenum share a common embryologic origin from which foregut buds, and what does this explain about the shared blood supply?",
     "answer": "The ventral pancreatic bud (which becomes the uncinate process and inferior head) rotates posteriorly to fuse with the dorsal bud. The duodenum and pancreatic head both derive from the foregut and share the pancreaticoduodenal arterial arcades (anterior and posterior, from GDA superiorly and SMA inferiorly) — this is why you cannot resect one without the other."},
    {"question": "Name the six structures that are divided or transected during a classic Whipple procedure.",
     "answer": "1) Common hepatic duct (or common bile duct), 2) Stomach/duodenum (at the antrum for classic Whipple or at the duodenum for pylorus-preserving), 3) Pancreatic neck, 4) Proximal jejunum (10-15cm distal to ligament of Treitz), 5) Gastroduodenal artery, 6) Uncinate process tissue/retroperitoneal margin off the SMA/SMV."},
    {"question": "What are the anterior and posterior pancreaticoduodenal arcades, and from which parent vessels do they arise?",
     "answer": "Anterior arcade: anterior superior PDA (from GDA) + anterior inferior PDA (from SMA/first jejunal branch). Posterior arcade: posterior superior PDA (from GDA) + posterior inferior PDA (from SMA). These arcades are within the pancreatic head parenchyma and are divided during the Whipple. The SMA's branches must be preserved — injury causes small bowel ischemia."},
    {"question": "What is the most common cause of morbidity after Whipple, and how is it graded?",
     "answer": "Pancreatic fistula (PF), occurring in 15-30%. Graded by ISGPF: Grade A (biochemical leak — drain amylase >3x serum on POD3, no clinical impact), Grade B (requires change in management — persistent drainage, antibiotics, or percutaneous drainage), Grade C (organ failure, reoperation, or death). Risk factors: soft gland texture, small pancreatic duct (<3mm), high-risk pathology (ampullary, duodenal, cystic), and excessive blood loss."},
    {"question": "What is the SMA margin (retroperitoneal/uncinate margin), and why is it the most important margin in Whipple?",
     "answer": "The tissue resected from the right lateral aspect of the SMA — this is the margin most likely to be positive (R1) because pancreatic head tumors frequently abut or invade the SMA adventitia. A positive SMA margin is associated with significantly worse survival. Some surgeons use the 'artery-first' approach, dissecting the SMA early to determine resectability before committing to reconstruction."}
],

"Distal Pancreatectomy": [
    {"question": "The body and tail of the pancreas develop from which embryologic bud, and what structure marks the junction with the head?",
     "answer": "The dorsal pancreatic bud. The junction with the ventral bud (head/uncinate) is at the neck of the pancreas, which overlies the SMV/portal vein confluence. The main pancreatic duct of Wirsung is formed by fusion of the ventral duct with the distal dorsal duct."},
    {"question": "What is the relationship of the splenic vein to the pancreatic body and tail, and why does this matter during distal pancreatectomy?",
     "answer": "The splenic vein runs along the posterior surface of the pancreatic body/tail, receiving multiple small pancreatic tributaries. These short, fragile veins tether the pancreas to the splenic vein — avulsion during mobilization causes hemorrhage that is difficult to control. For benign disease, spleen-preserving techniques (Kimura or Warshaw) can be attempted."},
    {"question": "What is the Warshaw technique versus the Kimura technique for spleen-preserving distal pancreatectomy?",
     "answer": "Kimura: preserves the splenic artery and vein by meticulously ligating each pancreatic branch — technically demanding but maintains normal splenic perfusion. Warshaw: sacrifices the splenic artery and vein, relying on the short gastric and left gastroepiploic collaterals to perfuse the spleen. Warshaw has a 15-25% splenic infarction/abscess rate."},
    {"question": "What is the DISTAL trial and what technique does it address?",
     "answer": "A multicenter RCT comparing stapler transection versus scalpel transection with main duct ligation (hand-sewn closure) of the pancreatic stump. Results showed no significant difference in pancreatic fistula rates. The key to reducing fistula is stump management — regardless of transection method, reinforcement with a falciform/omental patch or fibrin sealant may reduce fistula rates."},
    {"question": "For left-sided pancreatic cancer, what is the Radical Antegrade Modular Pancreatosplenectomy (RAMPS) and what is its advantage?",
     "answer": "RAMPS: a standardized approach with N1 lymphadenectomy along the celiac, splenic, and SMA axes, and posterior dissection either anterior to (anterior RAMPS) or posterior to (posterior RAMPS) the left adrenal gland. It improves R0 resection rates (>80% vs 50-70% with standard distal pancreatectomy) and lymph node yield. Posterior RAMPS is used when there is posterior invasion."}
],

"Cholecystectomy with Intraoperative Cholangiogram": [
    {"question": "The extrahepatic biliary tree develops from the hepatic diverticulum (foregut endoderm). What is the embryologic explanation for a choledochal cyst?",
     "answer": "Anomalous pancreaticobiliary ductal junction (APBDJ) — the pancreatic duct joins the CBD outside the duodenal wall, creating a long common channel that allows pancreatic juice reflux into the bile duct. This enzymatic damage weakens the bile duct wall, causing cystic dilation. Todani classification types I-V describe the variants."},
    {"question": "During cholangiogram, what anatomic structures should you identify on the film?",
     "answer": "1) Right and left hepatic ducts (bifurcation), 2) Common hepatic duct, 3) Cystic duct insertion point, 4) Common bile duct (normal ≤8mm, or ≤10mm post-cholecystectomy), 5) Pancreatic duct (if opacified), 6) Free flow of contrast into the duodenum. Absence of duodenal filling suggests distal obstruction (stone, stricture, or spasm — give glucagon 1mg IV to differentiate)."},
    {"question": "What are the biliary anatomic variants most likely to cause injury, and what percentage of patients have 'classic' biliary anatomy?",
     "answer": "Only 55-60% have 'classic' anatomy. Dangerous variants: 1) Low insertion of right posterior sectoral duct into CHD (misidentified as cystic duct), 2) Aberrant right hepatic duct crossing the hepatocystic triangle, 3) Parallel course of cystic duct along CBD (cystic duct appears to be CBD), 4) Short cystic duct with medial insertion. IOC identifies these variants before clip placement."},
    {"question": "If IOC shows a retained CBD stone, what are your intraoperative options?",
     "answer": "1) Laparoscopic CBD exploration with choledochoscopy (transcystic or choledochotomy approach — 85-95% success), 2) Glucagon + saline flush to encourage spontaneous passage, 3) Fogarty balloon catheter retrieval through cystic duct, 4) Leave a drain and refer for postoperative ERCP. The choice depends on stone size, surgeon experience, and available equipment. Transcystic exploration is preferred for stones <8mm."},
    {"question": "What is the evidence for routine versus selective IOC during cholecystectomy?",
     "answer": "Controversial. Proponents: routine IOC detects unsuspected CBD stones (3-5%), identifies aberrant anatomy preventing injury, and provides a real-time anatomic roadmap. Opponents: adds 10-15 minutes, costs money, has 1-2% false positive rate leading to unnecessary interventions. Meta-analyses suggest IOC reduces CBD injury rates when performed routinely (0.1% vs 0.3%), but this has not been confirmed in RCTs. Sweden's mandatory IOC registry shows lower injury rates."}
],

"Choledochojejunostomy": [
    {"question": "The common bile duct develops from the ventral foregut at the junction of the hepatic diverticulum and duodenum. What congenital anomaly results from failure of the ventral pancreatic bud to rotate?",
     "answer": "Annular pancreas — the ventral pancreatic bud fails to rotate posteriorly and instead encircles the duodenum (usually D2), causing duodenal obstruction. It may present in neonates (double-bubble sign) or adults (pancreatitis, obstruction). It is associated with Down syndrome and other midline anomalies."},
    {"question": "What is the minimum bile duct diameter considered adequate for choledochojejunostomy, and why?",
     "answer": "≥1cm (ideally ≥1.5cm). A small duct increases the technical difficulty of creating a mucosa-to-mucosa anastomosis and has a higher stricture rate. In small ducts, hepaticojejunostomy (at the common hepatic duct, which is usually more dilated above an obstruction) is preferred. The duct must be fish-mouthed (spatulated) to increase the anastomotic circumference."},
    {"question": "What is the blood supply to the supraduodenal CBD, and why is excessive mobilization dangerous?",
     "answer": "The supraduodenal CBD receives its blood supply axially from the 3 and 9 o'clock arteries — small branches from the GDA (inferiorly), right hepatic artery (superiorly), and cystic artery. These run along the lateral walls of the CBD. Excessive circumferential mobilization strips these vessels, causing ischemic stricture — a devastating complication."},
    {"question": "What is the Roux limb length for biliary reconstruction and what happens if bile reflux occurs?",
     "answer": "40-60cm Roux limb to prevent bile reflux into the biliary tree. If too short: reflux cholangitis (ascending infection from enteric bacteria). Symptoms: Charcot's triad (fever, jaundice, RUQ pain) or Reynold's pentad (add hypotension and altered mental status). A properly constructed Roux limb creates a one-way valve that prevents jejunal content reflux."},
    {"question": "What is the long-term patency rate of choledochojejunostomy, and what is the most common cause of failure?",
     "answer": "Long-term patency: 85-90% at 10 years. Most common cause of failure: anastomotic stricture from ischemia, tension, or fibrosis. Presents with recurrent cholangitis or obstructive jaundice years later. Management: percutaneous transhepatic cholangiography (PTC) with balloon dilation or surgical revision. Stenting through the Roux limb (percutaneous or endoscopic via double-balloon enteroscopy) is technically challenging but feasible."}
],

"Kasai Procedure (Hepatic Portoenterostomy)": [
    {"question": "Biliary atresia results from destruction of the extrahepatic bile ducts. What are the two proposed embryologic theories?",
     "answer": "1) Defective morphogenesis: abnormal development of the biliary plate from the hepatic diverticulum (failure of ductal plate remodeling), 2) Perinatal inflammatory theory: viral infection (reovirus, CMV, rotavirus) triggering autoimmune destruction of previously normal bile ducts. Most evidence supports a combination — genetic susceptibility + perinatal viral trigger. The embryonic form (~15%) is associated with laterality defects (situs inversus, polysplenia)."},
    {"question": "At what level is the transection made in the Kasai procedure, and what anatomic landmark guides it?",
     "answer": "Transection at the porta hepatis — the fibrous remnant of the extrahepatic bile ducts is divided flush with the liver capsule at the bifurcation plate (where the portal vein branches). Microscopic bile ductules (<150μm) within this fibrous plate communicate with the intrahepatic biliary system and drain bile into the Roux limb. This is why the transection must be precisely at the liver surface."},
    {"question": "What is the blood supply to the porta hepatis region, and what must be preserved during the Kasai?",
     "answer": "The hepatic artery proper and its branches (right and left hepatic arteries), portal vein bifurcation, and small peribiliary arterioles. The portal vein and hepatic arteries run immediately posterior to the bile duct remnant — injury to either is catastrophic. Careful dissection of the fibrous bile duct remnant away from these vessels is the most technically demanding step."},
    {"question": "What is the critical timing for Kasai, and what is the success rate based on age at surgery?",
     "answer": "Kasai must be performed before 60-90 days of age. Success (adequate bile drainage, clearance of jaundice): <30 days: 70-80%, 30-60 days: 50-60%, 60-90 days: 25-40%, >90 days: <20%. After 90 days, progressive biliary fibrosis and cirrhosis make Kasai ineffective. Even successful Kasai patients may need liver transplantation — 50% will require transplant by age 5, 70% by age 20."},
    {"question": "What complication unique to Kasai is caused by bacterial contamination of the biliary-enteric anastomosis?",
     "answer": "Ascending cholangitis — occurs in 40-50% of post-Kasai patients. Enteric bacteria ascend the Roux limb into the intrahepatic biliary system, causing fever, acholic stools, and rising bilirubin. Treated with IV antibiotics covering gram-negatives and anaerobes. Prophylactic oral antibiotics (TMP-SMX) are given for 1-2 years post-operatively. Recurrent cholangitis accelerates hepatic fibrosis and the need for transplantation."}
],

"Common Bile Duct Exploration": [
    {"question": "The hepatopancreatic ampulla (of Vater) forms from the fusion of which two embryologic ductal systems?",
     "answer": "The common bile duct (from the hepatic diverticulum/ventral foregut) and the ventral pancreatic duct (from the ventral pancreatic bud). They fuse as the ventral bud rotates posteriorly to join the dorsal bud. The sphincter of Oddi (from mesenchyme surrounding the ampulla) regulates bile and pancreatic juice flow. APBDJ (long common channel >15mm) predisposes to choledochal cysts and gallbladder cancer."},
    {"question": "What are the four portions of the CBD, and which is explored during supraduodenal choledochotomy?",
     "answer": "1) Supraduodenal (most accessible — this is where choledochotomy is performed), 2) Retroduodenal (behind D1), 3) Intrapancreatic (within pancreatic head), 4) Intraduodenal (ampulla). The supraduodenal portion is 2-3cm long, anterior to the portal vein, and accessed after Kocherization if needed. Choledochotomy is made longitudinally on the anterior surface."},
    {"question": "What provides the blood supply to the CBD at the choledochotomy site, and why is a longitudinal incision used?",
     "answer": "The 3 and 9 o'clock arteries run axially along the lateral walls of the CBD. A longitudinal choledochotomy avoids dividing these vessels (whereas a transverse incision would). The incision should be placed on the anterior midline of the duct, between the axial vessels, and kept as short as possible (1-1.5cm)."},
    {"question": "What is the difference between transcystic and transductal (choledochotomy) approaches to CBDE, and when is each indicated?",
     "answer": "Transcystic: stones ≤8mm, few in number, cystic duct dilated enough for choledochoscope. Avoids choledochotomy, lower morbidity, no T-tube needed. Transductal: stones >8mm, multiple stones, small/tortuous cystic duct, stones above the cystic duct insertion, intrahepatic stones. Requires choledochotomy and either primary closure (over a transcystic drain) or T-tube placement."},
    {"question": "What is the current evidence on T-tube versus primary closure after choledochotomy?",
     "answer": "Multiple RCTs and meta-analyses show primary closure (± transcystic biliary drain) is associated with shorter hospital stay, less bile leak, and equivalent stone clearance compared to T-tube. T-tube complications include: bile leak after removal (1-5%), T-tube tract choledochofistula, accidental dislodgement causing biliary peritonitis, and cholangitis. Primary closure is now the preferred approach in most centers."}
],

"Hepatic Resection": [
    {"question": "The liver develops from the hepatic diverticulum of the foregut. What embryologic structure gives rise to the hepatic sinusoidal endothelium?",
     "answer": "The vitelline veins (omphalomesenteric veins) — hepatic cords from the foregut endoderm interdigitate with the vitelline vein plexus, which forms the hepatic sinusoids. This is why the liver has a dual blood supply (hepatic artery + portal vein) from its earliest development — the portal vein is a remnant of the vitelline venous system."},
    {"question": "Describe the Couinaud segmental anatomy and what defines each segment.",
     "answer": "8 functionally independent segments, each with its own portal pedicle (portal vein, hepatic artery, bile duct) and hepatic venous drainage. The portal vein divides the liver into upper and lower segments; the hepatic veins divide it into sectors. The right hepatic vein separates segments 6/7 from 5/8; the middle hepatic vein separates right from left lobe (segments 5/8 from 4a/4b); the left hepatic vein separates segment 4 from 2/3. Segment 1 (caudate) is unique — has independent drainage directly into the IVC."},
    {"question": "What is the hepatic arterial blood supply, and what is the most common variant relevant to liver resection?",
     "answer": "Standard: common hepatic artery → proper hepatic artery → right and left hepatic arteries. Most common variant: replaced right hepatic artery from the SMA (10-15%) — it courses posterior to the portal vein and through the portacaval space. If unrecognized during right hepatectomy, it may be inadvertently ligated causing right lobe ischemia. A replaced left hepatic artery from the left gastric artery (10%) runs in the gastrohepatic ligament."},
    {"question": "What is post-hepatectomy liver failure (PHLF), and how do you predict it preoperatively?",
     "answer": "PHLF: inability of the liver remnant to maintain synthetic, excretory, and detoxifying functions (ISGLS criteria: INR >1.7 and bilirubin >3.0 on POD5). Prevention: ensure future liver remnant (FLR) volume >20% (normal liver), >30% (chemotherapy-treated), or >40% (cirrhotic). Measured by CT volumetry. If FLR is insufficient, options include portal vein embolization (PVE), ALPPS procedure, or staged hepatectomy."},
    {"question": "What is the Pringle maneuver, what is the safe duration, and what structure makes the liver tolerant?",
     "answer": "Clamping the hepatoduodenal ligament (portal triad) to occlude hepatic artery and portal vein inflow, reducing bleeding during parenchymal transection. Safe for 15-20 minutes continuous (up to 60-120 minutes with intermittent clamping: 15 min on, 5 min off). The liver tolerates ischemia because of its dual blood supply and rich glycogen stores. The Pringle maneuver does NOT control hepatic vein back-bleeding — low CVP anesthesia (<5 cmH2O) reduces this."}
],

"EGD with Dilation": [
    {"question": "Esophageal atresia occurs in 1:3000 births. What is the most common type (Gross classification) and what embryologic failure causes it?",
     "answer": "Type C (85%): proximal esophageal atresia with distal tracheoesophageal fistula. Caused by failure of the tracheoesophageal septum to completely separate the foregut into ventral (trachea) and dorsal (esophagus) compartments during week 4-5. The VACTERL association (Vertebral, Anorectal, Cardiac, TE fistula, Renal, Limb) occurs in 25%."},
    {"question": "What are the three types of esophageal strictures and the appropriate dilator for each?",
     "answer": "1) Simple/short/straight strictures (peptic, Schatzki ring): through-the-scope (TTS) balloon dilation, 2) Complex/long/angulated strictures (caustic, radiation, anastomotic): bougie dilation (Savary-Gilliard) — provides tactile feedback, 3) Malignant strictures: stenting preferred over dilation alone. Rule of 3: don't dilate more than 3 consecutive French sizes per session (e.g., 36Fr → 42Fr max)."},
    {"question": "What is the blood supply to the esophagus at different levels, and where is perforation most dangerous?",
     "answer": "Cervical: inferior thyroid artery. Thoracic: direct aortic branches and bronchial arteries (segmental, no named vessels). Abdominal: left gastric and left inferior phrenic arteries. Perforation is most dangerous in the thoracic esophagus — no serosa, segmental blood supply, and mediastinal contamination causes rapidly fatal mediastinitis (30% mortality if delayed >24 hours)."},
    {"question": "What is the perforation rate of esophageal dilation and what are the signs of perforation?",
     "answer": "Bougie: 0.1-0.4%. Balloon: 0.1-0.3%. Malignant strictures: up to 5-10%. Signs: chest pain, subcutaneous emphysema (crepitus), fever, tachycardia, pneumomediastinum on CXR, pleural effusion (left > right). Hamman's sign (mediastinal crunch with heartbeat) is classic but insensitive. CT with oral water-soluble contrast is diagnostic."},
    {"question": "What is a Schatzki ring, and what is the critical diameter that causes dysphagia?",
     "answer": "A thin mucosal ring at the squamocolumnar junction (GEJ/Z-line), composed of mucosa and submucosa (not muscle). Dysphagia occurs when the lumen is <13mm (symptomatic). Treatment: single balloon or bougie dilation to >16mm with excellent long-term results. Steakhouse syndrome (food impaction) is the classic presentation — always biopsy for eosinophilic esophagitis (present in 10-15% of patients with food impaction)."}
],

"EGD with Biopsy": [
    {"question": "Barrett's esophagus represents intestinal metaplasia of the squamous epithelium. What embryologic process does this recapitulate?",
     "answer": "The distal esophagus is initially lined by columnar epithelium (from foregut endoderm) before being replaced by stratified squamous epithelium via a cranial-to-caudal re-epithelialization during fetal development. Barrett's essentially represents a reversion to the embryonic columnar state — specialized intestinal metaplasia with goblet cells, driven by chronic acid/bile reflux."},
    {"question": "During EGD, where is the Z-line and what landmarks confirm you've entered the stomach?",
     "answer": "The Z-line (squamocolumnar junction, or SCJ) is the visible transition from pale squamous esophageal mucosa to salmon-pink columnar gastric mucosa. Gastric landmarks: 1) Rugal folds, 2) Incisura angularis (lesser curve angulation separating body from antrum), 3) Pylorus, 4) Retroflexion view showing the cardia and fundus around the scope (J-maneuver). Barrett's is diagnosed when the Z-line is displaced proximal to the GEJ."},
    {"question": "What is the Seattle biopsy protocol for Barrett's surveillance?",
     "answer": "Four-quadrant biopsies every 1-2cm throughout the Barrett's segment, PLUS targeted biopsies of any visible lesions (nodules, ulcers, color changes). This systematic approach reduces sampling error. For confirmed dysplasia, biopsies every 1cm. Visible lesions should undergo endoscopic mucosal resection (EMR) for both diagnosis and treatment — biopsies alone may undergrade dysplasia in 40% of cases."},
    {"question": "What is the blood supply to the gastric mucosa that accounts for stress ulcer formation?",
     "answer": "The gastric mucosal blood supply comes from a dense submucosal plexus fed by all five gastric arteries. During critical illness (shock, sepsis, burns), splanchnic vasoconstriction redirects blood away from the mucosa, causing ischemic mucosal breakdown. Combined with acid exposure (normally neutralized by the mucus-bicarbonate barrier), stress ulcers form. This is why both acid suppression (PPI) and maintaining perfusion are key to prophylaxis."},
    {"question": "When you biopsy a gastric ulcer, how many biopsies should you take and why?",
     "answer": "Minimum 6-8 biopsies from the ulcer margin (rim), PLUS biopsies from the base if safe. Gastric ulcers have a 5-10% malignancy rate (vs duodenal ulcers which are almost never malignant). Single biopsies have only 70% sensitivity for cancer; 7+ biopsies achieve >98% sensitivity. All gastric ulcers require repeat EGD in 8-12 weeks to confirm healing and rebiopsy if not healed — a non-healing gastric ulcer is cancer until proven otherwise."}
],

"Colonoscopy with Polypectomy": [
    {"question": "The colonic epithelium turns over every 3-5 days from stem cells in the crypt base. What is the adenoma-carcinoma sequence, and what gene mutation initiates it?",
     "answer": "Normal epithelium → aberrant crypt focus → tubular adenoma → advanced adenoma → carcinoma. The initiating mutation is APC (adenomatous polyposis coli) gene on chromosome 5q21, a tumor suppressor in the Wnt signaling pathway. This was elucidated by Vogelstein (1990). Subsequent mutations: KRAS, SMAD4/DCC (18q), TP53 (17p). The entire sequence takes 10-15 years, which is the basis for 10-year screening intervals."},
    {"question": "During polypectomy, what anatomic feature determines whether a sessile polyp can be safely removed endoscopically?",
     "answer": "The 'non-lifting sign' — submucosal injection (saline/methylene blue) should lift the polyp away from the muscularis propria. If the polyp does not lift, submucosal invasion (T1+ cancer) has fixed it to the muscle layer, making endoscopic resection risky (perforation) and oncologically inadequate. Non-lifting polyps require surgical resection. Paris classification 0-Is and 0-IIa are generally amenable to polypectomy; 0-III (excavated) suggests invasive cancer."},
    {"question": "What are the arterial branches that supply the right versus left colon at the points of greatest perforation risk during colonoscopy?",
     "answer": "The cecum (thinnest wall, largest diameter — Laplace's law) is supplied by the ileocolic artery. The sigmoid colon (narrowest lumen, highest intraluminal pressure) is supplied by sigmoid arteries from the IMA. These are the two highest-risk areas for perforation: cecum from overdistension and sigmoid from mechanical looping/torque. The splenic flexure is the third risk area (fixed, angulated, with the thinnest marginal artery supply)."},
    {"question": "What is the post-polypectomy syndrome (transmural burn syndrome), and how do you differentiate it from perforation?",
     "answer": "Electrocoagulation injury extending through the muscularis propria without frank perforation. Presents with localized pain, fever, leukocytosis, and peritoneal signs 1-5 days post-polypectomy. CT shows focal wall thickening and fat stranding but NO free air or extraluminal contrast. Treatment is conservative: NPO, IV antibiotics, observation. If free air is present → perforation → surgery."},
    {"question": "What are the current guidelines for surveillance intervals after polypectomy?",
     "answer": "US Multi-Society Task Force (2020): 1-2 tubular adenomas <10mm → 7-10 years. 3-4 adenomas <10mm → 3-5 years. 5-10 adenomas → 3 years. Adenoma ≥10mm, villous, or HGD → 3 years. Piecemeal EMR of ≥20mm → 6 months (to check for residual). >10 adenomas → 1 year (consider genetic testing for attenuated FAP/MUTYH). Serrated polyps ≥10mm or with dysplasia → 3 years."}
],

"ERCP with Sphincterotomy": [
    {"question": "The sphincter of Oddi develops from mesenchymal cells surrounding the junction of the bile duct and duodenum. What is its normal resting pressure compared to CBD pressure?",
     "answer": "Sphincter of Oddi resting pressure: 10-15 mmHg above duodenal pressure. CBD resting pressure: 5-10 mmHg. The sphincter cycles with phasic contractions (2-6/min) coordinated with the migrating motor complex. Sphincter of Oddi dysfunction (SOD) Type I: dilated CBD >12mm + elevated LFTs + dilated duct + pain. Manometry (gold standard for Type III) shows pressures >40 mmHg."},
    {"question": "During ERCP cannulation, what anatomic landmark identifies the major papilla, and what is its typical location in the duodenum?",
     "answer": "The major papilla (ampulla of Vater) is located on the posteromedial wall of the second part of the duodenum (D2), typically at the junction of the middle and distal third. It is identified by: the longitudinal duodenal fold (plica longitudinalis), a small nipple-like protrusion, and often a hooding fold. The minor papilla (accessory duct of Santorini) is 2cm proximal and anterior."},
    {"question": "What is the blood supply to the ampullary region, and why does sphincterotomy occasionally cause significant bleeding?",
     "answer": "The posterior superior pancreaticoduodenal artery runs behind the ampulla at the 11 o'clock position (relative to the papillary orifice en face). Sphincterotomy is made between 11 and 1 o'clock to avoid this vessel, but anatomic variation can place it in the cut zone. Post-sphincterotomy bleeding occurs in 1-2% and is usually mild (oozing), but arterial bleeding from the PDA requires endoscopic hemostasis or angiographic embolization."},
    {"question": "What is post-ERCP pancreatitis, its incidence, and how do you prevent it?",
     "answer": "Incidence: 3-7% overall, up to 15% in high-risk patients. Prevention: 1) Rectal indomethacin 100mg (NEJM 2012 — reduced PEP from 16% to 9%), 2) Prophylactic pancreatic duct stent (for high-risk cases: SOD, difficult cannulation, precut sphincterotomy), 3) Aggressive IV hydration with lactated Ringer's, 4) Wire-guided cannulation (reduces PEP vs contrast injection). Risk factors: young female, SOD, difficult cannulation, pancreatic duct injection, precut, prior PEP."},
    {"question": "What is a precut (access) sphincterotomy, and when is it indicated?",
     "answer": "A technique to gain biliary access when standard cannulation fails (>5-10 minutes or >5 pancreatic duct cannulations). Options: 1) Needle-knife fistulotomy (cutting directly into CBD above the papilla), 2) Needle-knife precut sphincterotomy (cutting from the orifice upward), 3) Transpancreatic sphincterotomy (cutting through the septum after PD access). Increases perforation and pancreatitis risk. Should be performed by experienced endoscopists — early precut is now preferred over prolonged traumatic attempts at cannulation."}
],

"Ivor Lewis Esophagectomy": [
    {"question": "The esophagus develops from the foregut, separating from the trachea via the tracheoesophageal septum. What is unique about the esophageal wall that makes it prone to anastomotic leak?",
     "answer": "The esophagus is the only GI organ without a serosa — it has only adventitia (loose connective tissue). The serosa provides tensile strength for suture/staple holding and promotes rapid healing through serosal apposition. Without it, esophageal anastomoses heal more slowly and are more prone to leak (5-15% incidence). The blood supply is also segmental without a named mesenteric vessel."},
    {"question": "Describe the two surgical phases of an Ivor Lewis esophagectomy and the level of the anastomosis.",
     "answer": "Phase 1 (Abdominal): gastric mobilization, creation of gastric conduit (tube), pyloroplasty or pyloromyotomy, feeding jejunostomy. Phase 2 (Right thoracotomy/VATS): esophageal mobilization, en bloc lymphadenectomy, esophageal transection, intrathoracic esophagogastric anastomosis at or above the azygos vein level. The anastomosis is in the right chest (above the azygos)."},
    {"question": "What is the blood supply to the gastric conduit after esophagectomy?",
     "answer": "The entire conduit depends on the right gastroepiploic artery (from GDA). The left gastric, left gastroepiploic, and short gastric arteries are all divided during conduit creation. The right gastroepiploic arcade runs along the greater curvature and provides the sole blood supply — this is why the conduit tip (at the anastomosis) has the most tenuous perfusion. ICG angiography at the conduit tip can guide the anastomotic site."},
    {"question": "What is the most common cause of death after Ivor Lewis esophagectomy?",
     "answer": "Pneumonia and respiratory failure (not anastomotic leak, though leak is the most feared surgical complication). Pulmonary complications occur in 15-30% due to: one-lung ventilation, right thoracotomy pain limiting respiration, aspiration from conduit dysfunction, and recurrent laryngeal nerve injury (left > right) causing vocal cord paralysis. Mortality: 2-5% at high-volume centers (>20/year), but >10% at low-volume centers."},
    {"question": "What is the minimum number of lymph nodes needed for adequate staging in esophageal cancer, and what does the CROSS trial recommend for neoadjuvant therapy?",
     "answer": "Minimum 15 lymph nodes (AJCC 8th edition recommends optimal examination of ≥15 nodes). CROSS trial (2012): neoadjuvant chemoradiation (carboplatin + paclitaxel + 41.4 Gy) followed by surgery showed 13% improvement in 5-year OS (47% vs 34%) compared to surgery alone for esophageal and GEJ cancers. CROSS is the standard neoadjuvant regimen for locally advanced esophageal cancer worldwide."}
],

"Gastric Pull-up Reconstruction": [
    {"question": "What embryologic vascular axis allows the stomach to be used as an esoph