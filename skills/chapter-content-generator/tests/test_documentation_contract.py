import os
import unittest
from pathlib import Path


SKILL_DIR = Path(
    os.environ.get("CHAPTER_CONTENT_SKILL_DIR", Path(__file__).resolve().parents[1])
).resolve()
SKILL = (SKILL_DIR / "SKILL.md").read_text()


class ChapterContentDocumentationContractTests(unittest.TestCase):
    def test_sequential_execution_is_the_only_default(self):
        self.assertIn("### Sequential Mode (Default for all use-cases)", SKILL)
        self.assertIn("### Parallel Mode (Only on request)", SKILL)
        self.assertNotIn("### Parallel Mode (Default", SKILL)

    def test_parallel_workflow_is_explicitly_request_gated(self):
        self.assertIn(
            "Plan Parallel Chapter Batches (Only after an explicit request)", SKILL
        )
        self.assertIn(
            "This workflow runs only after the user explicitly requests parallel execution",
            SKILL,
        )

    def test_skill_rejects_automatic_parallel_thresholds(self):
        for stale in (
            "When processing 4+ chapters, always use parallel mode",
            "For sequential mode or fewer than 4 chapters",
            "After all parallel agents complete, aggregate results",
        ):
            self.assertNotIn(stale, SKILL)

    def test_ordinary_all_chapters_example_is_sequential(self):
        example = SKILL.split("## Example Session", 1)[1].split(
            "### Parallel Mode (Explicit request example)", 1
        )[0]
        self.assertIn("### Sequential Mode (Default)", example)
        self.assertIn('**User:** "Generate content for all chapters"', example)
        self.assertIn("Processes each chapter one at a time", example)
        self.assertNotIn("Spawns 6 Task agents", example)

    def test_examples_report_the_current_skill_version(self):
        workflow = SKILL.split("## Workflow", 1)[1]
        for stale in ("v0.04", "v0.05", "v0.06"):
            self.assertNotIn(stale, workflow)
        self.assertIn("Chapter Content Generator Skill v0.09 running", workflow)


if __name__ == "__main__":
    unittest.main()
