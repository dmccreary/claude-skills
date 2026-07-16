import os
import unittest
from pathlib import Path


REPO_ROOT = Path(
    os.environ.get("REFERENCE_GENERATOR_REPO_ROOT", Path(__file__).resolve().parents[3])
).resolve()
SKILL = (REPO_ROOT / "skills/reference-generator/SKILL.md").read_text()
DESCRIPTION = (
    REPO_ROOT / "docs/skill-descriptions/book/reference-generator.md"
).read_text()
DESCRIPTION_INDEX = (
    REPO_ROOT / "docs/skill-descriptions/book/index.md"
).read_text()
HISTORICAL_RUN = (REPO_ROOT / "docs/prompts/generate-references.md").read_text()
HISTORICAL_CREATION = (
    REPO_ROOT / "docs/prompts/references-generator-skill.md"
).read_text()
HISTORICAL_UPDATE = (
    REPO_ROOT / "docs/prompts/update-skill-descriptions.md"
).read_text()
MKDOCS = (REPO_ROOT / "mkdocs.yml").read_text()
SUPPLEMENTARY = (
    REPO_ROOT
    / "skills/book-installer/references/supplementary-content-generator.md"
).read_text()
NAV_GUIDE = (
    REPO_ROOT / "skills/book-installer/references/mkdocs-nav-editing.md"
).read_text()
BOOK_INSTALLER = (REPO_ROOT / "skills/book-installer/SKILL.md").read_text()
IBOOK = (REPO_ROOT / "commands/ibook.md").read_text()


def normalized(text):
    return " ".join(text.split()).lower()


DESCRIPTION_INDEX_SECTION = DESCRIPTION_INDEX.split(
    "### 9. Reference Generator", 1
)[1].split("### 10.", 1)[0]
SUPPLEMENTARY_REFERENCE_STEP = SUPPLEMENTARY.split(
    "## Step 6: Generate Per-Chapter References", 1
)[1].split("## Step 7:", 1)[0]


class ReferenceGeneratorDocumentationContractTests(unittest.TestCase):
    def test_current_surfaces_require_exactly_ten_references_per_chapter(self):
        for surface in (
            SKILL,
            DESCRIPTION,
            DESCRIPTION_INDEX_SECTION,
            SUPPLEMENTARY_REFERENCE_STEP,
        ):
            contract = normalized(surface)
            self.assertIn("exactly 10", contract)
            self.assertTrue(
                any(
                    phrase in contract
                    for phrase in (
                        "per chapter",
                        "for each chapter",
                        "for each textbook chapter",
                        "for every chapter",
                    )
                )
            )

        for surface in (
            SKILL,
            DESCRIPTION,
            DESCRIPTION_INDEX_SECTION,
            SUPPLEMENTARY_REFERENCE_STEP,
        ):
            for stale in ("10/20/30/40", "10, 20, 30, or 40", "40 (graduate)"):
                self.assertNotIn(stale, surface)

    def test_current_surfaces_publish_the_same_source_positions(self):
        self.assertIn("**Positions 1-3: Wikipedia Articles**", SKILL)
        self.assertIn("**Positions 4-5: Textbooks (No URL)**", SKILL)
        self.assertIn("**Positions 6-10: Online Resources**", SKILL)
        self.assertIn("### Positions 1-3: Wikipedia", DESCRIPTION)
        self.assertIn("### Positions 4-5: Authoritative Textbooks", DESCRIPTION)
        self.assertIn("### Positions 6-10: Verified Online Resources", DESCRIPTION)
        self.assertIn(
            "Wikipedia articles in positions 1-3", SUPPLEMENTARY_REFERENCE_STEP
        )
        self.assertIn(
            "authoritative textbooks without URLs in positions 4-5",
            SUPPLEMENTARY_REFERENCE_STEP,
        )
        self.assertIn(
            "verified online resources in positions 6-10",
            SUPPLEMENTARY_REFERENCE_STEP,
        )
        self.assertIn("Textbooks (No URL)", SKILL)
        self.assertIn("Do not add URLs", DESCRIPTION)
        self.assertIn("textbooks without URLs", SUPPLEMENTARY_REFERENCE_STEP)
        self.assertIn("verify each url", normalized(SKILL))
        self.assertIn("verify each url", normalized(DESCRIPTION))
        self.assertIn("verified online resources", SUPPLEMENTARY_REFERENCE_STEP)

    def test_direct_integrator_invokes_the_skill_once_with_explicit_scope(self):
        self.assertIn(
            "invoke the\n`reference-generator` skill once",
            SUPPLEMENTARY_REFERENCE_STEP,
        )
        self.assertIn("for these chapter paths only", SUPPLEMENTARY_REFERENCE_STEP)
        self.assertNotIn("for each chapter that lacks", SUPPLEMENTARY_REFERENCE_STEP)
        self.assertIn("When the user or an invoking workflow supplies", SKILL)
        self.assertIn("process only those chapters", SKILL)
        self.assertIn("When a user or invoking workflow supplies", DESCRIPTION)
        self.assertIn("process only those chapters", DESCRIPTION)
        self.assertIn("If the list is empty", SUPPLEMENTARY_REFERENCE_STEP)
        self.assertIn("skip the skill entirely", SUPPLEMENTARY_REFERENCE_STEP)

    def test_current_surfaces_match_the_file_and_navigation_contract(self):
        self.assertIn("docs/chapters/XX-chapter-name/references.md", SKILL)
        self.assertIn("docs/chapters/<chapter-slug>/references.md", DESCRIPTION)
        self.assertIn(
            "docs/chapters/<chapter-slug>/references.md",
            SUPPLEMENTARY_REFERENCE_STEP,
        )

        for surface in (SKILL, DESCRIPTION, SUPPLEMENTARY_REFERENCE_STEP):
            self.assertIn("[See Annotated References](./references.md)", surface)
            self.assertIn("Annotated References:", surface)

        self.assertIn("This is the only supported placement mode", DESCRIPTION)

        for surface in (SKILL, DESCRIPTION, SUPPLEMENTARY_REFERENCE_STEP):
            contract = normalized(surface)
            self.assertNotIn("book-level references", contract)
            self.assertNotIn("book level references", contract)
            self.assertNotIn("append to each chapter file", contract)

    def test_current_surfaces_follow_canonical_serial_navigation(self):
        self.assertIn("serialize edits", normalized(SKILL))
        self.assertIn("apply them in one edit at the end", normalized(DESCRIPTION))
        self.assertNotIn("one chapter navigation change at a time", DESCRIPTION)
        self.assertIn("apply them in one edit at the end", normalized(NAV_GUIDE))
        self.assertIn(
            "one serialized navigation edit in step 12",
            normalized(SUPPLEMENTARY_REFERENCE_STEP),
        )
        for surface in (SKILL, DESCRIPTION):
            contract = normalized(surface)
            self.assertIn("defer navigation", contract)
            self.assertIn("do not edit `mkdocs.yml`", contract)
            self.assertIn("annotated references", contract)
        self.assertIn("defer all mkdocs.yml changes", normalized(SUPPLEMENTARY_REFERENCE_STEP))
        self.assertIn(
            "return the annotated references navigation entries",
            normalized(SUPPLEMENTARY_REFERENCE_STEP),
        )
        self.assertIn(
            "do not edit `mkdocs.yml` in this step",
            normalized(SUPPLEMENTARY_REFERENCE_STEP),
        )
        self.assertNotIn("Chapter N - Title", SUPPLEMENTARY_REFERENCE_STEP)

    def test_current_surfaces_do_not_require_dates(self):
        for surface in (SKILL, DESCRIPTION, SUPPLEMENTARY_REFERENCE_STEP):
            for stale in (
                "yyyy-mm-dd",
                "iso format dates",
                "publication dates included",
            ):
                self.assertNotIn(stale, normalized(surface))

    def test_current_surfaces_share_the_annotation_length(self):
        for surface in (SKILL, DESCRIPTION, SUPPLEMENTARY_REFERENCE_STEP):
            self.assertIn("20-40 word", normalized(surface))

    def test_book_installer_pipeline_uses_the_same_reference_contract(self):
        reference_step = SUPPLEMENTARY_REFERENCE_STEP

        self.assertIn("exactly 10 curated sources", reference_step)
        self.assertIn("Wikipedia articles in positions 1-3", reference_step)
        self.assertIn(
            "authoritative textbooks without URLs in positions 4-5", reference_step
        )
        self.assertIn("verified online resources in positions 6-10", reference_step)
        self.assertIn("[See Annotated References](./references.md)", reference_step)
        self.assertIn(
            "Annotated References: chapters/<slug>/references.md", reference_step
        )
        self.assertNotIn("8–15", reference_step)
        self.assertNotIn("grouped by type", reference_step)
        self.assertNotIn("book-level references", normalized(reference_step))
        self.assertNotIn("book level references", normalized(reference_step))

    def test_current_integration_authorities_publish_per_chapter_output(self):
        self.assertIn("`docs/chapters/*/references.md`", IBOOK)
        self.assertIn("`docs/chapters/*/references.md`", BOOK_INSTALLER)
        self.assertIn("`reference-generator`", IBOOK)
        self.assertIn("`reference-generator`", BOOK_INSTALLER)

    def test_historical_transcripts_are_unmistakably_superseded(self):
        self.assertIn("Superseded workflow", HISTORICAL_RUN)
        self.assertIn(
            "does not define the current skill contract", normalized(HISTORICAL_RUN)
        )
        self.assertIn("Superseded creation transcript", HISTORICAL_CREATION)
        self.assertIn(
            "historical evidence, not current operating guidance",
            normalized(HISTORICAL_CREATION),
        )
        self.assertIn("Superseded documentation transcript", HISTORICAL_UPDATE)
        self.assertIn(
            "does not define the current `reference-generator` contract",
            normalized(HISTORICAL_UPDATE),
        )
        self.assertIn(
            "Historical Reference Generation Transcript: prompts/generate-references.md",
            MKDOCS,
        )
        self.assertIn(
            "Historical Reference Generator Creation Transcript: prompts/references-generator-skill.md",
            MKDOCS,
        )
        self.assertIn(
            "Historical Skill Description Generation Transcript: prompts/update-skill-descriptions.md",
            MKDOCS,
        )


if __name__ == "__main__":
    unittest.main()
