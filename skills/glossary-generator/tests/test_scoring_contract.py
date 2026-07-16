import os
import re
import unittest
from pathlib import Path


SKILL_DIR = Path(
    os.environ.get("GLOSSARY_SKILL_DIR", Path(__file__).resolve().parents[1])
).resolve()
SKILL = (SKILL_DIR / "SKILL.md").read_text()
REFERENCE = (SKILL_DIR / "references" / "iso-11179-standards.md").read_text()

EXPECTED_WEIGHTS = {
    "Precision": 20,
    "Conciseness": 20,
    "Distinctiveness": 20,
    "Non-circularity": 20,
    "Unencumbered by business rules": 20,
}


def rubric_weights(text: str) -> dict[str, int]:
    match = re.search(
        r"<!-- glossary-quality-rubric:start -->(.*?)"
        r"<!-- glossary-quality-rubric:end -->",
        text,
        re.DOTALL,
    )
    if not match:
        return {}
    rows = re.findall(r"^\| ([^|]+?) \| (\d+) \|$", match.group(1), re.MULTILINE)
    return {name.strip(): int(weight) for name, weight in rows}


class GlossaryScoringContractTests(unittest.TestCase):
    def test_skill_declares_one_five_criterion_100_point_rubric(self):
        weights = rubric_weights(SKILL)
        self.assertEqual(weights, EXPECTED_WEIGHTS)
        self.assertEqual(sum(weights.values()), 100)

    def test_reference_uses_the_same_weights(self):
        weights = rubric_weights(REFERENCE)
        self.assertEqual(weights, EXPECTED_WEIGHTS)
        self.assertEqual(sum(weights.values()), 100)

    def test_stale_denominator_and_criterion_count_are_absent(self):
        combined = SKILL + REFERENCE
        for stale in (
            "25 points each",
            "all 4 criteria",
            "The Four Core Criteria",
            "**Precision (25 points):**",
            "**Conciseness (25 points):**",
            "**Distinctiveness (25 points):**",
            "**Non-circularity (25 points):**",
        ):
            self.assertNotIn(stale, combined)

    def test_local_weighting_is_not_attributed_to_iso(self):
        for text in (SKILL, REFERENCE):
            self.assertIn("local evaluation rubric", text)
        self.assertNotIn("ISO 11179 Metadata Registry Compliance Metrics", SKILL)
        self.assertNotIn("ISO criteria", SKILL)


if __name__ == "__main__":
    unittest.main()
