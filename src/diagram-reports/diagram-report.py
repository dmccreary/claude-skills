#!/usr/bin/env python3
"""Compatibility entry point for the canonical microsim-utils diagram report."""

from pathlib import Path
import runpy


SCRIPT = (
    Path(__file__).resolve().parents[2]
    / "skills"
    / "microsim-utils"
    / "scripts"
    / "diagram-report.py"
)


if __name__ == "__main__":
    runpy.run_path(str(SCRIPT), run_name="__main__")
