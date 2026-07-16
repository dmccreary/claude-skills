import copy
import importlib.util
import io
import json
import re
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "microsim-generator"
VALIDATOR = SKILL / "scripts" / "validate_concept_classifier.py"
TEMPLATE = SKILL / "assets" / "concept-classifier" / "data-template.json"
GUIDE = SKILL / "references" / "concept-classifier-guide.md"
SCRIPT_TEMPLATE = SKILL / "assets" / "concept-classifier" / "concept-classifier-template.js"
PUBLISHED_DESCRIPTION = ROOT / "docs" / "skill-descriptions" / "microsims" / "concept-classifier.md"

spec = importlib.util.spec_from_file_location("validate_concept_classifier", VALIDATOR)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class ConceptClassifierContractTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TEMPLATE.read_text(encoding="utf-8"))

    def test_bundled_template_is_structurally_valid(self):
        self.assertEqual(validator.validate(self.data), [])

    def test_rejects_duplicate_ids_missing_answer_and_oversized_quiz(self):
        broken = copy.deepcopy(self.data)
        broken["config"]["questionsPerQuiz"] = 9
        broken["scenarios"][1]["id"] = broken["scenarios"][0]["id"]
        broken["scenarios"][2]["correctAnswer"] = "Not an option"
        errors = validator.validate(broken)
        self.assertIn("config.questionsPerQuiz must not exceed the scenario count", errors)
        self.assertTrue(any("duplicates" in error for error in errors))
        self.assertTrue(any("must appear exactly in options" in error for error in errors))

    def test_rejects_undefined_categories_and_invalid_scoring(self):
        broken = copy.deepcopy(self.data)
        broken["categoryDescriptions"].pop("Category D")
        broken["config"]["pointsWithHint"] = 11
        broken["endScreen"]["performanceMessages"]["good"]["threshold"] = 95
        errors = validator.validate(broken)
        self.assertTrue(any("Category D" in error for error in errors))
        self.assertIn("config.pointsWithHint must not exceed config.pointsCorrect", errors)
        self.assertIn(
            "performance thresholds must descend: excellent > good > fair > needsWork",
            errors,
        )

    def test_rejects_categories_without_a_correct_scenario(self):
        broken = copy.deepcopy(self.data)
        broken["scenarios"][3]["correctAnswer"] = "Category C"
        errors = validator.validate(broken)
        self.assertIn(
            "every category must appear as a correct answer; uncovered: ['Category D']",
            errors,
        )

    def test_rejects_non_scalar_ids_without_crashing(self):
        broken = copy.deepcopy(self.data)
        broken["scenarios"][0]["id"] = ["not", "hashable"]
        self.assertIn(
            "scenarios[0].id must be a string or integer",
            validator.validate(broken),
        )

    def test_rejects_unsupported_option_counts_and_malformed_display_config(self):
        broken = copy.deepcopy(self.data)
        broken["config"]["scenarioLabel"] = None
        broken["config"]["instructionText"] = []
        broken["scenarios"][0]["options"] = ["Category A"]
        errors = validator.validate(broken)
        self.assertIn("config.scenarioLabel must be a non-empty string", errors)
        self.assertIn("config.instructionText must be a non-empty string", errors)
        self.assertIn("scenarios[0].options must contain between 2 and 4 choices", errors)

    def test_rejects_whitespace_disguised_duplicate_options(self):
        broken = copy.deepcopy(self.data)
        broken["scenarios"][0]["options"] = [
            "Category A",
            " category a ",
            "Category C",
            "Category D",
        ]
        errors = validator.validate(broken)
        self.assertIn(
            "scenarios[0].options must be unique ignoring case and surrounding whitespace",
            errors,
        )
        self.assertIn("scenarios[0].options[1] must not have surrounding whitespace", errors)

    def test_rejects_empty_ids_oversized_numbers_and_nonzero_fallback(self):
        broken = copy.deepcopy(self.data)
        broken["scenarios"][0]["id"] = "  "
        broken["config"]["pointsCorrect"] = 10**10000
        broken["endScreen"]["performanceMessages"]["needsWork"]["threshold"] = 1
        errors = validator.validate(broken)
        self.assertIn("scenarios[0].id must be a string or integer", errors)
        self.assertIn("config.pointsCorrect must be greater than zero", errors)
        self.assertIn("endScreen.performanceMessages.needsWork.threshold must equal 0", errors)

    def test_cli_reports_non_utf8_input_without_traceback(self):
        output = io.StringIO()
        decode_error = UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid start byte")
        with (
            patch.object(sys, "argv", [str(VALIDATOR), "invalid.json"]),
            patch.object(Path, "read_text", side_effect=decode_error),
            redirect_stdout(output),
        ):
            result = validator.main()
        self.assertEqual(result, 1)
        self.assertIn("INVALID:", output.getvalue())

    def test_guide_states_accessibility_and_metadata_boundaries(self):
        guide = " ".join(GUIDE.read_text(encoding="utf-8").split())
        script = SCRIPT_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn("real HTML button", guide)
        self.assertIn("assets/templates/p5/metadata-template.json", guide)
        self.assertIn("structural consistency, not instructional truth", guide)
        self.assertIn("% of available points", script)
        self.assertIn("let correctCount = 0", script)
        self.assertIn("correctCount++", script)
        self.assertIn("text(correctPercent + '% correct'", script)
        self.assertIn("text(pointPercent + '% of available points'", script)
        self.assertIn("correctPercent >= perfMessages.excellent.threshold", script)

    def test_canonical_guide_dataset_passes_the_validator(self):
        guide = GUIDE.read_text(encoding="utf-8")
        match = re.search(r"```json\n(.*?)\n```", guide, re.DOTALL)
        self.assertIsNotNone(match)
        self.assertEqual(validator.validate(json.loads(match.group(1))), [])

    def test_published_description_routes_to_the_active_contract(self):
        description = PUBLISHED_DESCRIPTION.read_text(encoding="utf-8")
        self.assertIn("`microsim-generator` -> `concept-classifier`", description)
        self.assertIn("scripts/validate_concept_classifier.py", description)
        self.assertIn("real HTML controls", description)
        self.assertNotIn("/skills/concept-classifier/templates/", description)


if __name__ == "__main__":
    unittest.main()
