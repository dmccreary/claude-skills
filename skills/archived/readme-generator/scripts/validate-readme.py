#!/usr/bin/env python3
"""Compatibility wrapper for the authoritative book-publisher validator."""

import importlib.util
from pathlib import Path


ACTIVE_SCRIPT = (
    Path(__file__).resolve().parents[3]
    / "book-publisher"
    / "scripts"
    / "validate-readme.py"
)
SPEC = importlib.util.spec_from_file_location(
    "active_book_publisher_validate_readme",
    ACTIVE_SCRIPT,
)
active_validator = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(active_validator)

for name in dir(active_validator):
    if not name.startswith("_"):
        globals()[name] = getattr(active_validator, name)


if __name__ == "__main__":
    active_validator.main()
