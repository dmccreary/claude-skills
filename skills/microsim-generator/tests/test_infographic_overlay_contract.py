import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "microsim-generator"
TEMPLATE = SKILL / "assets" / "infographic-overlay" / "main-template.html"
GUIDE = SKILL / "references" / "infographic-overlay-guide.md"
HEIGHT_GUIDE = SKILL / "references" / "overlay-iframe-height-pinning.md"
RUNTIME = SKILL / "assets" / "infographic-overlay" / "shared-libs" / "diagram.js"
ARCHIVED_HEIGHT_GUIDE = (
    ROOT
    / "skills"
    / "archived"
    / "interactive-infographic-overlay"
    / "references"
    / "iframe-height-pinning.md"
)
FIXTURE = (
    SKILL / "tests" / "fixtures" / "callout-overlay" / "main.html"
)

CANONICAL_IDS = ("layout", "controls", "infobox", "edit-panel")
CANONICAL_ORDER = "`#layout → #controls → #infobox → #edit-panel`"
STALE_ORDER = "`#layout → #infobox → #controls → #edit-panel`"


def assert_element_order(test_case: unittest.TestCase, html: str) -> None:
    positions = []
    for element_id in CANONICAL_IDS:
        marker = f'<div id="{element_id}">'
        test_case.assertEqual(html.count(marker), 1, marker)
        positions.append(html.index(marker))
    test_case.assertEqual(positions, sorted(positions))


class InfographicOverlayContractTests(unittest.TestCase):
    def setUp(self):
        self.template = TEMPLATE.read_text(encoding="utf-8")
        self.guide = GUIDE.read_text(encoding="utf-8")
        self.height_guide = HEIGHT_GUIDE.read_text(encoding="utf-8")
        self.runtime = RUNTIME.read_text(encoding="utf-8")
        self.archived_height_guide = ARCHIVED_HEIGHT_GUIDE.read_text(
            encoding="utf-8"
        )
        self.fixture = FIXTURE.read_text(encoding="utf-8")

    def test_template_and_browser_fixture_use_the_canonical_dom_order(self):
        assert_element_order(self, self.template)
        assert_element_order(self, self.fixture)

    def test_active_guides_describe_the_runtime_order(self):
        self.assertIn(CANONICAL_ORDER, self.guide)
        self.assertIn(CANONICAL_ORDER, self.height_guide)
        self.assertNotIn(STALE_ORDER, self.height_guide)

    def test_height_guide_does_not_claim_an_unimplemented_infobox_pin(self):
        self.assertNotIn("style.minHeight", self.runtime)
        self.assertNotIn("style.minHeight", self.height_guide)
        self.assertNotIn("Pinning the Infobox", self.height_guide)
        self.assertIn("worst-case body height", self.height_guide)

    def test_archived_height_guide_is_explicitly_non_authoritative(self):
        opening = "\n".join(self.archived_height_guide.splitlines()[:12])
        self.assertIn("Historical snapshot — non-authoritative", opening)
        self.assertIn(
            "microsim-generator/references/overlay-iframe-height-pinning.md",
            opening,
        )


if __name__ == "__main__":
    unittest.main()
