import os
import unittest
from pathlib import Path


REPO_ROOT = Path(
    os.environ.get(
        "SUPPLEMENTARY_NAV_REPO_ROOT", Path(__file__).resolve().parents[3]
    )
).resolve()
WORKFLOW = (
    REPO_ROOT
    / "skills/book-installer/references/supplementary-content-generator.md"
).read_text()
NAV_GUIDE = (
    REPO_ROOT / "skills/book-installer/references/mkdocs-nav-editing.md"
).read_text()


def section(start, end):
    return WORKFLOW.split(start, 1)[1].split(end, 1)[0]


def normalized(text):
    return " ".join(text.split())


PRE_NAV_STEPS = section(
    "## Step 2: Generate the About Page",
    "## Step 12: Update mkdocs.yml Navigation",
)
QUIZ_STEP = section(
    "## Step 5: Generate Per-Chapter Quizzes",
    "## Step 6: Generate Per-Chapter References",
)
NAV_STEP = section(
    "## Step 12: Update mkdocs.yml Navigation",
    "## Step 13: Verification",
)


def workflow_step(number, next_number):
    return section(f"## Step {number}:", f"## Step {next_number}:")


class SupplementaryNavigationContractTests(unittest.TestCase):
    def test_canonical_guide_requires_one_batch_edit(self):
        self.assertIn("collect the nav changes", NAV_GUIDE)
        self.assertIn("apply them\n   in ONE edit at the end", NAV_GUIDE)

    def test_quiz_step_defers_navigation_and_uses_canonical_label(self):
        quiz_contract = normalized(QUIZ_STEP)
        self.assertIn("Do not edit `mkdocs.yml` in this step", quiz_contract)
        self.assertIn("one serialized navigation edit in Step 12", quiz_contract)
        self.assertIn("- N. Title:", QUIZ_STEP)
        self.assertNotIn("Chapter N - Title", QUIZ_STEP)
        self.assertNotIn("After creating each `quiz.md`, add", QUIZ_STEP)

    def test_all_pre_navigation_steps_queue_instead_of_mutating(self):
        for stale_instruction in (
            "Add to `mkdocs.yml` nav",
            "add a **Quizzes** sub-entry",
            "If it writes a file, add it to the nav",
        ):
            self.assertNotIn(stale_instruction, PRE_NAV_STEPS)

        for artifact in (
            "About",
            "Glossary",
            "FAQ",
            "Quiz",
            "Annotated References",
            "Book Metrics",
            "Diagram Specifications",
        ):
            self.assertIn(artifact, NAV_STEP)

    def test_each_navigation_producing_step_defers_to_step_twelve(self):
        expectations = {
            (2, 3): ("Do not edit mkdocs.yml", "Step 12"),
            (3, 4): ("Do not edit mkdocs.yml", "Step 12"),
            (4, 5): ("Do not edit mkdocs.yml", "Step 12"),
            (5, 6): ("Do not edit `mkdocs.yml` in this step", "Step 12"),
            (6, 7): ("Do not edit `mkdocs.yml` in this step", "Step 12"),
            (8, 9): ("do not edit navigation here", "Step 12"),
            (9, 10): ("Defer navigation to Step 12",),
        }

        for (number, next_number), required in expectations.items():
            contract = normalized(workflow_step(number, next_number))
            for phrase in required:
                self.assertIn(phrase, contract, f"Step {number} must defer navigation")

    def test_step_twelve_is_the_single_navigation_writer(self):
        nav_contract = normalized(NAV_STEP)
        self.assertIn("sole navigation writer", nav_contract)
        self.assertIn(
            "Read the current `mkdocs.yml` immediately before editing", nav_contract
        )
        self.assertIn("ONE serialized edit", nav_contract)
        self.assertIn("only for files that now exist", nav_contract)
        self.assertIn("Preserve any other child entries", nav_contract)
        self.assertIn("references/mkdocs-nav-editing.md", NAV_STEP)


if __name__ == "__main__":
    unittest.main()
