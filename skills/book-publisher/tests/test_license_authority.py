import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPTS_DIR = Path(__file__).parents[1] / "scripts"


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS_DIR / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


license_authority = load_module("license_authority_test", "license_authority.py")
validate_readme = load_module("validate_readme_authority_test", "validate-readme.py")


BASE_README = """# Demo

## Overview

Fixture.

## Getting Started

Use it.

## Contact

Fixture owner.
"""

MIT_TEXT = """MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy.
THE SOFTWARE IS PROVIDED "AS IS".
"""


class TempRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def write(self, relative_path: str, content: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def snapshot(self):
        return {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }


class LicenseAuthorityTests(TempRepoTestCase):
    def test_absent_evidence_is_explicit_and_does_not_mutate(self):
        before = self.snapshot()

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "absent")
        self.assertFalse(result["claim_allowed"])
        self.assertFalse(result["mutates_repository"])
        self.assertEqual(self.snapshot(), before)

    def test_docs_only_evidence_is_scoped_not_repository_wide(self):
        self.write("docs/license.md", "Documentation terms only.")

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "scoped")
        self.assertEqual(result["root_evidence"], [])
        self.assertEqual(result["scoped_evidence"], ["docs/license.md"])
        self.assertFalse(result["claim_allowed"])

    def test_one_known_root_license_is_single_evidence(self):
        self.write("LICENSE", MIT_TEXT)

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "single-evidence")
        self.assertEqual(result["known_license_ids"], {"LICENSE": "MIT"})
        self.assertTrue(result["claim_allowed"])

    def test_known_spdx_identifier_is_canonicalized(self):
        self.write("LICENSE", "SPDX-License-Identifier: mit\n")

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["known_license_ids"], {"LICENSE": "MIT"})

    def test_compound_spdx_expression_requires_manual_review(self):
        self.write("LICENSE", "SPDX-License-Identifier: MIT OR Apache-2.0\n")

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "nonstandard-or-unresolved")
        self.assertEqual(result["known_license_ids"], {"LICENSE": None})
        self.assertTrue(result["requires_manual_review"])

    def test_unknown_spdx_identifier_requires_manual_review(self):
        self.write("LICENSE", "SPDX-License-Identifier: LicenseRef-Proprietary\n")

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "nonstandard-or-unresolved")
        self.assertEqual(result["known_license_ids"], {"LICENSE": None})

    def test_symlink_license_is_not_repository_authority(self):
        outside = Path(self.temp_dir.name).parent / f"{self.root.name}-outside-license"
        outside.write_text(MIT_TEXT, encoding="utf-8")
        self.addCleanup(outside.unlink, missing_ok=True)
        (self.root / "LICENSE").symlink_to(outside)

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "absent")
        self.assertEqual(result["root_evidence"], [])

    def test_symlinked_licenses_directory_cannot_escape_repository(self):
        outside = Path(self.temp_dir.name).parent / f"{self.root.name}-outside-licenses"
        outside.mkdir()
        self.addCleanup(outside.rmdir)
        self.addCleanup(lambda: (outside / "MIT.txt").unlink(missing_ok=True))
        (outside / "MIT.txt").write_text(MIT_TEXT, encoding="utf-8")
        (self.root / "LICENSES").symlink_to(outside, target_is_directory=True)

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "absent")
        self.assertEqual(result["root_evidence"], [])

    def test_one_custom_root_license_remains_unresolved(self):
        self.write("LICENSE", "Classroom display only. Redistribution prohibited.")

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "nonstandard-or-unresolved")
        self.assertTrue(result["claim_allowed"])
        self.assertTrue(result["requires_manual_review"])

    def test_multiple_root_license_files_are_ambiguous(self):
        self.write("LICENSE-MIT", MIT_TEXT)
        self.write("LICENSE-OTHER", "Custom terms.")

        result = license_authority.inspect_repository(self.root)

        self.assertEqual(result["state"], "ambiguous")
        self.assertFalse(result["claim_allowed"])

    def test_explicit_authorization_is_a_distinct_state(self):
        result = license_authority.inspect_repository(
            self.root,
            authorized_license="CC-BY-4.0",
        )

        self.assertEqual(result["state"], "explicitly-authorized")
        self.assertEqual(result["authorized_license"], "CC-BY-4.0")
        self.assertTrue(result["claim_allowed"])


class ReadmeLicenseValidationTests(TempRepoTestCase):
    def validate(self, content: str, authorized_license=None):
        readme = self.write("README.md", content)
        return validate_readme.validate_readme(
            str(readme),
            authorized_license=authorized_license,
        )

    def test_no_claim_is_valid_when_license_evidence_is_absent(self):
        report = self.validate(BASE_README)

        self.assertTrue(report["license_authority"]["valid"])
        self.assertEqual(report["license_authority"]["state"], "absent")

    def test_claim_is_rejected_when_license_evidence_is_absent(self):
        report = self.validate(
            BASE_README + "\n## License\n\nLicensed under MIT.\n"
        )

        self.assertFalse(report["valid"])
        self.assertIn("state: absent", report["license_authority"]["issues"][0])

    def test_affirmative_claim_outside_license_section_is_rejected(self):
        report = self.validate(
            BASE_README.replace("Fixture.", "This project is licensed under the MIT License.")
        )

        self.assertFalse(report["valid"])
        self.assertTrue(report["license_authority"]["has_license_text_claim"])

    def test_nonclaiming_license_tooling_reference_is_not_a_claim(self):
        report = self.validate(
            BASE_README.replace("Fixture.", "This tool detects MIT License files.")
            + "\n[![Build](https://img.shields.io/badge/build-passing-green)](https://example.com)\n"
        )

        self.assertTrue(report["license_authority"]["valid"])
        self.assertFalse(report["license_authority"]["has_license_badge"])
        self.assertFalse(report["license_authority"]["has_license_text_claim"])

    def test_matching_claim_must_link_exact_evidence(self):
        self.write("LICENSE", MIT_TEXT)

        missing_link = self.validate(
            BASE_README + "\n## License\n\nLicensed under the MIT License.\n"
        )
        linked = self.validate(
            BASE_README
            + "\n## License\n\nLicensed under the [MIT License](LICENSE).\n"
        )

        self.assertFalse(missing_link["valid"])
        self.assertTrue(linked["license_authority"]["valid"])
        self.assertEqual(linked["links"]["invalid"], [])

    def test_mismatched_common_license_is_rejected(self):
        self.write("LICENSE", MIT_TEXT)

        report = self.validate(
            BASE_README
            + "\n## License\n\nLicensed under [CC BY-NC-SA 4.0](LICENSE).\n"
        )

        self.assertFalse(report["valid"])
        self.assertTrue(
            any("does not match" in issue for issue in report["license_authority"]["issues"])
        )

    def test_extra_contradictory_license_claim_is_rejected(self):
        self.write("LICENSE", MIT_TEXT)

        report = self.validate(
            BASE_README
            + "\n## License\n\n[MIT](LICENSE), also CC-BY-4.0.\n"
        )

        self.assertFalse(report["valid"])

    def test_license_badge_without_license_alt_text_is_still_a_claim(self):
        report = self.validate(
            BASE_README
            + "\n[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)\n"
        )

        self.assertFalse(report["valid"])
        self.assertTrue(report["license_authority"]["has_license_badge"])

    def test_custom_terms_allow_only_a_generic_exact_link(self):
        self.write("LICENSE", "Classroom display only. Redistribution prohibited.")

        generic = self.validate(
            BASE_README + "\n## License\n\nSee [LICENSE](LICENSE) for terms.\n"
        )
        invented = self.validate(
            BASE_README
            + "\n## License\n\nLicensed under the [MIT License](LICENSE).\n"
        )

        self.assertTrue(generic["license_authority"]["valid"])
        self.assertFalse(invented["valid"])

    def test_bare_known_identifier_in_license_section_is_a_claim(self):
        self.write("LICENSE", "Classroom display only. Redistribution prohibited.")

        report = self.validate(
            BASE_README + "\n## License\n\nSee [MIT](LICENSE).\n"
        )

        self.assertFalse(report["valid"])
        self.assertEqual(report["license_authority"]["claimed_license_ids"], ["MIT"])

    def test_bare_identifier_in_setext_license_section_is_a_claim(self):
        self.write("LICENSE", "Classroom display only. Redistribution prohibited.")

        report = self.validate(
            BASE_README + "\nLicense\n-------\n\nSee [MIT](LICENSE).\n"
        )

        self.assertFalse(report["valid"])
        self.assertEqual(report["license_authority"]["claimed_license_ids"], ["MIT"])

    def test_ambiguous_evidence_rejects_a_single_license_claim(self):
        self.write("LICENSE-MIT", MIT_TEXT)
        self.write("LICENSE-OTHER", "Custom terms.")

        report = self.validate(
            BASE_README
            + "\n## License\n\nLicensed under [MIT](LICENSE-MIT).\n"
        )

        self.assertFalse(report["valid"])
        self.assertIn("state: ambiguous", report["license_authority"]["issues"][0])

    def test_explicit_authorization_allows_a_claim_without_creating_files(self):
        before = self.snapshot()

        report = self.validate(
            BASE_README + "\n## License\n\nLicensed under CC-BY-4.0.\n",
            authorized_license="CC-BY-4.0",
        )

        self.assertTrue(report["license_authority"]["valid"])
        after = self.snapshot()
        self.assertEqual(set(after) - set(before), {"README.md"})
        self.assertFalse(any(name.lower().startswith("license") for name in after))

    def test_explicit_authorization_rejects_a_different_claim(self):
        report = self.validate(
            BASE_README + "\n## License\n\nLicensed under MIT License.\n",
            authorized_license="CC-BY-4.0",
        )

        self.assertFalse(report["valid"])
        self.assertTrue(
            any("explicitly authorized" in issue for issue in report["license_authority"]["issues"])
        )


if __name__ == "__main__":
    unittest.main()
