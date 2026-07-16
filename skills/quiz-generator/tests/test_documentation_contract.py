import os
import unittest
from pathlib import Path


SKILL_DIR = Path(
    os.environ.get("QUIZ_SKILL_DIR", Path(__file__).resolve().parents[1])
).resolve()
SKILL = (SKILL_DIR / "SKILL.md").read_text()
README = (SKILL_DIR / "README.md").read_text()


class QuizDocumentationContractTests(unittest.TestCase):
    def test_operating_skill_and_readme_publish_the_same_version(self):
        self.assertIn("**Version:** 0.4", SKILL)
        self.assertIn("**Version 0.4 Features:**", README)

    def test_both_surfaces_define_serial_execution_as_the_default(self):
        self.assertIn("## Token Efficiency: Serial Execution Only", SKILL)
        self.assertIn("### Serial Mode (Default)", README)
        self.assertIn("one agent", README.lower())

    def test_readme_rejects_the_superseded_parallel_default(self):
        for stale in (
            "Now with parallel execution support",
            "Parallel Mode (Default",
            "Same token usage",
            "plans chapter batches for parallel processing",
            "spawns 4-6 Task agents",
        ):
            self.assertNotIn(stale, README)

    def test_required_and_optional_outputs_match_the_operating_skill(self):
        required_section = README.split("### Required (Per Chapter)", 1)[1].split(
            "### Recommended (Aggregate)", 1
        )[0]
        recommended_section = README.split("### Recommended (Aggregate)", 1)[1].split(
            "### Optional", 1
        )[0]
        optional_section = README.split("### Optional", 1)[1].split(
            "## Quality Standards", 1
        )[0]

        self.assertIn("docs/chapters/[chapter-name]/quiz.md", required_section)
        self.assertNotIn("Embedded:", required_section)
        self.assertNotIn("Quiz Metadata JSON", required_section)
        self.assertNotIn("Quiz Bank JSON", required_section)
        self.assertIn("Quality Report", recommended_section)
        self.assertIn("Session Log", recommended_section)
        self.assertIn("Quiz Metadata JSON", optional_section)
        self.assertIn("Quiz Bank JSON", optional_section)

    def test_skill_does_not_describe_parallel_generation_as_current_workflow(self):
        self.assertNotIn("generated for many chapters in parallel", SKILL)
        self.assertNotIn("Unless the User Explicitly Requests It", SKILL)
        self.assertNotIn("without the user explicitly requesting it", SKILL)


if __name__ == "__main__":
    unittest.main()
