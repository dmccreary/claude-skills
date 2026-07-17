#!/usr/bin/env python3
"""Inspect repository license evidence without selecting legal terms."""

import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


KNOWN_LICENSES: Tuple[Tuple[str, Tuple[str, ...]], ...] = (
    (
        "MIT",
        (
            "permission is hereby granted, free of charge",
            "the software is provided \"as is\"",
        ),
    ),
    ("Apache-2.0", ("apache license", "version 2.0")),
    ("GPL-3.0", ("gnu general public license", "version 3")),
    (
        "CC-BY-NC-SA-4.0",
        ("creative commons attribution-noncommercial-sharealike 4.0",),
    ),
    (
        "CC-BY-NC-4.0",
        ("creative commons attribution-noncommercial 4.0",),
    ),
    (
        "CC-BY-SA-4.0",
        ("creative commons attribution-sharealike 4.0",),
    ),
    ("CC-BY-4.0", ("creative commons attribution 4.0",)),
)


def _is_root_license_file(path: Path) -> bool:
    name = path.name.lower()
    return any(
        name == prefix
        or name.startswith(f"{prefix}.")
        or name.startswith(f"{prefix}-")
        or name.startswith(f"{prefix}_")
        for prefix in ("license", "licence", "copying")
    )


def _relative_files(paths: List[Path], root: Path) -> List[str]:
    return sorted(path.relative_to(root).as_posix() for path in paths)


def _is_regular_repository_file(path: Path, root: Path) -> bool:
    """Reject symlink evidence so authority cannot escape the repository."""
    try:
        resolved = path.resolve(strict=True)
    except OSError:
        return False
    return (
        not path.is_symlink()
        and resolved.is_file()
        and resolved.is_relative_to(root.resolve())
    )


def discover_license_evidence(repo_root: Path) -> Dict[str, List[str]]:
    """Return repository-root and explicitly scoped license evidence paths."""
    root_files = [
        path
        for path in repo_root.iterdir()
        if _is_regular_repository_file(path, repo_root) and _is_root_license_file(path)
    ]

    licenses_dir = repo_root / "LICENSES"
    if licenses_dir.is_dir() and not licenses_dir.is_symlink():
        root_files.extend(
            path
            for path in licenses_dir.rglob("*")
            if _is_regular_repository_file(path, repo_root)
        )

    scoped_files: List[Path] = []
    docs_dir = repo_root / "docs"
    if docs_dir.is_dir() and not docs_dir.is_symlink():
        scoped_files.extend(
            path
            for path in docs_dir.iterdir()
            if _is_regular_repository_file(path, repo_root)
            and _is_root_license_file(path)
        )

    return {
        "root": _relative_files(root_files, repo_root),
        "scoped": _relative_files(scoped_files, repo_root),
    }


def identify_known_license(path: Path) -> Optional[str]:
    """Identify a small, conservative allowlist of textual signatures."""
    if path.is_symlink():
        return None
    try:
        content = path.read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return None

    spdx_match = re.search(
        r"spdx-license-identifier:\s*([^\r\n]+)",
        content,
        flags=re.IGNORECASE,
    )
    if spdx_match:
        detected = spdx_match.group(1).strip().removesuffix("*/").strip()
        for license_id, _ in KNOWN_LICENSES:
            if detected.lower() == license_id.lower():
                return license_id
        # Unknown identifiers and compound SPDX expressions require review.
        return None

    for license_id, signatures in KNOWN_LICENSES:
        if all(signature in content for signature in signatures):
            return license_id
    return None


def inspect_repository(
    repo_root: Path,
    authorized_license: Optional[str] = None,
) -> Dict[str, object]:
    """Classify evidence without creating, changing, or choosing license terms."""
    root = repo_root.resolve()
    if not root.is_dir():
        raise ValueError(f"Repository root is not a directory: {repo_root}")

    evidence = discover_license_evidence(root)
    root_evidence = evidence["root"]
    scoped_evidence = evidence["scoped"]
    known_ids = {
        relative_path: identify_known_license(root / relative_path)
        for relative_path in root_evidence
    }

    authorized = (authorized_license or "").strip()
    if authorized:
        state = "explicitly-authorized"
        claim_allowed = True
        requires_manual_review = False
    elif len(root_evidence) > 1:
        state = "ambiguous"
        claim_allowed = False
        requires_manual_review = True
    elif len(root_evidence) == 1:
        detected_id = known_ids[root_evidence[0]]
        state = "single-evidence" if detected_id else "nonstandard-or-unresolved"
        claim_allowed = True
        requires_manual_review = detected_id is None
    elif scoped_evidence:
        state = "scoped"
        claim_allowed = False
        requires_manual_review = True
    else:
        state = "absent"
        claim_allowed = False
        requires_manual_review = False

    return {
        "state": state,
        "repo_root": str(root),
        "root_evidence": root_evidence,
        "scoped_evidence": scoped_evidence,
        "known_license_ids": known_ids,
        "authorized_license": authorized or None,
        "claim_allowed": claim_allowed,
        "requires_manual_review": requires_manual_review,
        "mutates_repository": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Classify repository license evidence without selecting terms."
    )
    parser.add_argument("repo_root", type=Path)
    parser.add_argument("--authorized-license")
    args = parser.parse_args()

    try:
        result = inspect_repository(args.repo_root, args.authorized_license)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
