import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).parents[3]
LICENSE_GUIDANCE_PATHS = (
    REPO_ROOT / "skills" / "book-publisher" / "references" / "readme-guide.md",
    REPO_ROOT / "skills" / "archived" / "readme-generator" / "SKILL.md",
    REPO_ROOT / "docs" / "prompts" / "readme-generator-skill.md",
)


class ReadmeLicenseGuidanceContractTests(unittest.TestCase):
    def test_guidance_never_invents_a_default_license(self):
        forbidden_patterns = (
            r"default[^\n]*creative commons",
            r"always will use[^\n]*creative commons",
            r"this work is licensed under the \[creative commons",
        )

        for path in LICENSE_GUIDANCE_PATHS:
            content = path.read_text(encoding="utf-8").lower()
            with self.subTest(path=path):
                for pattern in forbidden_patterns:
                    self.assertIsNone(re.search(pattern, content))

    def test_active_guide_fails_closed_without_license_evidence(self):
        guide = LICENSE_GUIDANCE_PATHS[0].read_text(encoding="utf-8").lower()

        self.assertRegex(guide, r"no license\s+detected")
        self.assertIn("never invent or select a license", guide)
        self.assertIn("omit the license badge", guide)
        self.assertIn("omit the badge and license section", guide)
        self.assertIn("license_authority.py", guide)
        self.assertIn("validate-readme.py /path/to/repository/readme.md", guide)
        self.assertIn("license-authority error is a hard failure", guide)


if __name__ == "__main__":
    unittest.main()
