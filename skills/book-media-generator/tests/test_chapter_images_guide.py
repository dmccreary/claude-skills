import unittest
import importlib.util
import io
import json
import urllib.error
from unittest import mock
from pathlib import Path


GUIDE = Path(__file__).resolve().parents[1] / "references/chapter-images-guide.md"
HELPER = Path(__file__).resolve().parents[1] / "scripts/images/commons_metadata.py"
TEXT = GUIDE.read_text()
NORMALIZED = " ".join(TEXT.split()).lower()

SPEC = importlib.util.spec_from_file_location("commons_metadata", HELPER)
commons_metadata = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(commons_metadata)


def page(license_id="CC BY 4.0", license_url="https://creativecommons.org/licenses/by/4.0/", artist="Example Creator"):
    return {
        "title": "File:Example.jpg",
        "imageinfo": [
            {
                "url": "https://upload.wikimedia.org/example.jpg",
                "thumburl": "https://upload.wikimedia.org/example-1280px.jpg",
                "descriptionurl": "https://commons.wikimedia.org/wiki/File:Example.jpg",
                "extmetadata": {
                    "Artist": {"value": artist},
                    "LicenseShortName": {"value": license_id},
                    "LicenseUrl": {"value": license_url},
                    "UsageTerms": {"value": license_id},
                    "Credit": {"value": "Example collection"},
                },
            }
        ],
    }


class ChapterImagesGuideContractTests(unittest.TestCase):
    def test_commons_example_uses_supported_api_and_metadata(self):
        helper = HELPER.read_text()
        self.assertIn('API_URL = "https://commons.wikimedia.org/w/api.php"', helper)
        self.assertIn('"iiprop": "url|extmetadata"', helper)
        self.assertIn('"formatversion": 2', helper)
        self.assertIn("urllib.parse.urlencode", helper)
        self.assertNotIn("urllib.request.quote", helper)

    def test_helper_normalizes_html_and_requires_reviewable_creator(self):
        record = commons_metadata.normalize_page(
            page(artist='<a href="/wiki/User:Example">Example Creator</a>')
        )
        self.assertEqual(record["creator"], "Example Creator")
        with self.assertRaises(commons_metadata.MetadataError):
            commons_metadata.normalize_page(page(artist='<span class="icon"></span>'))

    def test_helper_requires_official_url_for_creative_commons_license(self):
        with self.assertRaises(commons_metadata.MetadataError):
            commons_metadata.normalize_page(page(license_url=""))
        with self.assertRaises(commons_metadata.MetadataError):
            commons_metadata.normalize_page(
                page(license_url="https://example.com/licenses/by/4.0/")
            )

    def test_helper_routes_non_allowlisted_licenses_to_manual_review(self):
        with self.assertRaises(commons_metadata.ManualRightsReviewRequired):
            commons_metadata.normalize_page(
                page(
                    license_id="CC BY-SA 4.0",
                    license_url="https://creativecommons.org/licenses/by-sa/4.0/",
                )
            )

    def test_helper_retries_429_with_retry_after_and_a_bounded_attempt(self):
        error = urllib.error.HTTPError(
            "https://commons.wikimedia.org/w/api.php",
            429,
            "Too Many Requests",
            {"Retry-After": "0"},
            None,
        )
        response = io.BytesIO(
            json.dumps({"query": {"pages": [page()]}}).encode("utf-8")
        )
        with mock.patch.object(
            commons_metadata.urllib.request,
            "urlopen",
            side_effect=[error, response],
        ) as urlopen, mock.patch.object(commons_metadata.time, "sleep") as sleep:
            result = commons_metadata.fetch_page(
                "File:Example.jpg", "mailto:maintainer@example.org"
            )
        self.assertEqual(result["title"], "File:Example.jpg")
        self.assertEqual(urlopen.call_count, 2)
        sleep.assert_called_once_with(0.0)

    def test_helper_requires_contactable_user_agent_identity(self):
        with self.assertRaises(commons_metadata.MetadataError):
            commons_metadata.fetch_page("File:Example.jpg", "anonymous")

    def test_rights_policy_fails_closed(self):
        self.assertIn("manual rights review required", NORMALIZED)
        self.assertIn("do not infer that cc by-sa material is compatible", NORMALIZED)
        self.assertIn("commons provides no warranty", NORMALIZED)
        self.assertIn("contractor, grantee, donated, transferred", NORMALIZED)
        self.assertNotIn("public domain — no restrictions", NORMALIZED)
        self.assertNotIn("the license shown on commons is what matters", NORMALIZED)

    def test_provenance_contract_is_auditable(self):
        for field in (
            "source_page",
            "direct_url",
            "creator",
            "license_id",
            "license_url",
            "retrieved_at",
            "modifications",
            "sha256",
        ):
            self.assertIn(field, TEXT)

    def test_instructional_value_precedes_image_count(self):
        self.assertIn("zero new images is a valid", NORMALIZED)
        self.assertIn("what will the learner be able to notice", NORMALIZED)
        self.assertNotIn("identify 3-6 insertion points", NORMALIZED)
        self.assertNotIn("immediately after every h2", NORMALIZED)

    def test_verification_exceeds_a_successful_build(self):
        self.assertIn("desktop and mobile widths", NORMALIZED)
        self.assertIn("license links resolve", NORMALIZED)
        self.assertIn("matches the committed file's sha-256", NORMALIZED)
        self.assertIn("a successful build proves only", NORMALIZED)

    def test_published_attribution_links_source_and_license(self):
        self.assertIn("[Creator and source file](https://example.com/source-file)", TEXT)
        self.assertIn("[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)", TEXT)


if __name__ == "__main__":
    unittest.main()
