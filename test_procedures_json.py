import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parent
PROCEDURES = ROOT / "procedures.json"
REQUIRED_FIELDS = {
    "id", "name", "category", "overview", "indications", "keyAnatomy",
    "preOpConsiderations", "positioning", "portPlacementOrIncision",
    "criticalSteps", "commonPitfalls", "majorComplications", "pearlsHighYield",
    "postOpPriorities", "relatedProcedures", "pimpingQuestions",
}


class ProcedureEducationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.procedures = json.loads(PROCEDURES.read_text(encoding="utf-8"))
        cls.by_id = {item["id"]: item for item in cls.procedures}

    def test_thyroid_taxonomy_is_total_vs_lobectomy(self):
        self.assertIn("total-thyroidectomy", self.by_id)
        self.assertIn("thyroid-lobectomy", self.by_id)
        self.assertNotIn("robotic-thyroidectomy", self.by_id)
        self.assertNotIn("hemithyroidectomy", self.by_id)
        self.assertNotIn("hemithyroidectomy-lobectomy", self.by_id)

        total = self.by_id["total-thyroidectomy"]
        lobectomy = self.by_id["thyroid-lobectomy"]
        self.assertEqual("Total Thyroidectomy", total["name"])
        self.assertEqual("Thyroid Lobectomy", lobectomy["name"])
        self.assertEqual(5, len(total["pimpingQuestions"]))
        self.assertEqual(10, len(lobectomy["pimpingQuestions"]))
        self.assertIn("thyroid-lobectomy", total["relatedProcedures"])
        for procedure in (total, lobectomy):
            self.assertEqual(1, len(procedure["approachEducation"]))
            approach = procedure["approachEducation"][0]
            self.assertEqual("remote-access-robotic-thyroid-approach", approach["id"])
            self.assertEqual("Remote-access robotic approach", approach["name"])
            self.assertEqual("Robotic Thyroidectomy", approach["sourceName"])
            self.assertEqual(5, len(approach["pimpingQuestions"]))
            self.assertEqual(
                {
                    "What is the transaxillary approach for robotic thyroidectomy?",
                    "What nerve is additionally at risk in the transaxillary approach?",
                    "What is the blood supply encountered during subcutaneous flap creation?",
                    "What are the contraindications to robotic transaxillary thyroidectomy?",
                    "What does the evidence show for robotic versus conventional thyroidectomy outcomes?",
                },
                {item["question"] for item in approach["pimpingQuestions"]},
            )

    def test_all_available_case_education_remains_complete(self):
        self.assertEqual(232, len(self.procedures))
        self.assertEqual(20, len({item["category"] for item in self.procedures}))
        self.assertEqual(1165, sum(len(item["pimpingQuestions"]) for item in self.procedures))
        approaches = {
            approach["id"]: approach
            for procedure in self.procedures
            for approach in procedure.get("approachEducation", [])
        }
        self.assertEqual(5, sum(len(item["pimpingQuestions"]) for item in approaches.values()))
        for procedure in self.procedures:
            self.assertTrue(REQUIRED_FIELDS.issubset(procedure), procedure["id"])
            self.assertTrue(procedure["pimpingQuestions"], procedure["id"])


if __name__ == "__main__":
    unittest.main()
