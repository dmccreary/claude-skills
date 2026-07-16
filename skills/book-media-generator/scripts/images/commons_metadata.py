#!/usr/bin/env python3
"""Fetch and normalize reviewable Wikimedia Commons image metadata."""

from __future__ import annotations

import argparse
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path


API_URL = "https://commons.wikimedia.org/w/api.php"
ROUTINE_LICENSES = {
    "CC0 1.0",
    "CC BY 2.0",
    "CC BY 2.5",
    "CC BY 3.0",
    "CC BY 4.0",
    "Public domain",
}


class MetadataError(RuntimeError):
    """The candidate lacks metadata required for review."""


class ManualRightsReviewRequired(MetadataError):
    """The candidate license is outside the routine-reuse allowlist."""


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def plain_text(value: str) -> str:
    parser = _TextExtractor()
    parser.feed(value or "")
    parser.close()
    text = " ".join(" ".join(parser.parts).split())
    return re.sub(r"\s+([,.;:!?])", r"\1", text)


def _field(metadata: dict, name: str) -> str:
    return plain_text(metadata.get(name, {}).get("value", ""))


def _creative_commons_url_matches(license_id: str, license_url: str) -> bool:
    parsed = urllib.parse.urlparse(license_url)
    if parsed.scheme != "https" or parsed.netloc not in {
        "creativecommons.org",
        "www.creativecommons.org",
    }:
        return False
    normalized_path = parsed.path.rstrip("/").lower()
    if license_id == "CC0 1.0":
        return normalized_path == "/publicdomain/zero/1.0"
    match = re.fullmatch(r"CC BY (\d\.\d)", license_id)
    return bool(match and normalized_path == f"/licenses/by/{match.group(1)}")


def normalize_page(page: dict) -> dict:
    if page.get("missing") or "imageinfo" not in page:
        raise MetadataError(f"Commons file not found: {page.get('title', 'unknown')}")

    info = page["imageinfo"][0]
    metadata = info.get("extmetadata", {})
    creator = _field(metadata, "Artist")
    license_id = _field(metadata, "LicenseShortName")
    license_url = metadata.get("LicenseUrl", {}).get("value", "").strip()
    source_page = info.get("descriptionurl", "").strip()

    if not creator or not any(character.isalnum() for character in creator):
        raise MetadataError("Candidate lacks a reviewable plain-text creator")
    if not source_page:
        raise MetadataError("Candidate lacks a Commons source page")
    if license_id not in ROUTINE_LICENSES:
        raise ManualRightsReviewRequired(
            f"Manual rights review required for license: {license_id or 'missing'}"
        )
    if license_id != "Public domain" and not _creative_commons_url_matches(
        license_id, license_url
    ):
        raise MetadataError(
            f"Candidate lacks the official license URL for {license_id}"
        )

    return {
        "title": page["title"],
        "source_page": source_page,
        "direct_url": info.get("thumburl", info["url"]),
        "creator": creator,
        "license_id": license_id,
        "license_url": license_url,
        "usage_terms": _field(metadata, "UsageTerms"),
        "credit": _field(metadata, "Credit"),
    }


def fetch_page(title: str, contact: str, attempts: int = 3) -> dict:
    if not contact.startswith(("mailto:", "https://", "http://")):
        raise MetadataError(
            "Contact must be a monitored mailto: or HTTP(S) URL"
        )
    params = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "imageinfo",
            "iiprop": "url|extmetadata",
            "iiurlwidth": 1280,
            "format": "json",
            "formatversion": 2,
        }
    )
    request = urllib.request.Request(
        f"{API_URL}?{params}",
        headers={
            "User-Agent": f"IntelligentTextbookMediaAudit/1.0 ({contact})"
        },
    )

    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)["query"]["pages"][0]
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == attempts:
                raise
            retry_after = error.headers.get("Retry-After", "1")
            try:
                delay = float(retry_after)
            except ValueError:
                delay = 1.0
            time.sleep(min(max(delay, 0.0), 60.0))

    raise RuntimeError("Unreachable retry state")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--contact", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    record = normalize_page(fetch_page(args.title, args.contact))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
