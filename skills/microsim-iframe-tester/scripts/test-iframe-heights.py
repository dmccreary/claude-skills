#!/usr/bin/env python3
"""
MicroSim Iframe Height Tester

Uses Playwright to load each MicroSim's main.html inside a viewport
constrained to the iframe height declared in index.md, then checks
whether all interactive controls (buttons, sliders, selects, etc.)
are fully visible without clipping.

Usage:
    python test-iframe-heights.py --sims-dir docs/sims [--sim name] [--height N] [--report file.md]

Prerequisites:
    pip install playwright
    playwright install chromium
"""

import argparse
import math
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from playwright.sync_api import sync_playwright

TOLERANCE = 5        # px — controls within this margin still count as visible
SAFETY_MARGIN = 10   # px — added to suggested height
VIEWPORT_WIDTH = 800 # standard test width

CONTROL_SELECTORS = ", ".join([
    "button",
    'input[type="range"]',
    'input[type="checkbox"]',
    'input[type="text"]',
    'input[type="number"]',
    "select",
    "textarea",
    ".p5Canvas",
    "canvas",
])

# JavaScript executed in the browser to measure control positions
MEASURE_CONTROLS_JS = """
({ sel, viewportHeight, tolerance }) => {
    const elements = document.querySelectorAll(sel);
    const results = [];
    for (const el of elements) {
        const rect = el.getBoundingClientRect();
        if (rect.width === 0 && rect.height === 0) continue;
        if (rect.height === 0) continue;
        results.push({
            tag: el.tagName.toLowerCase(),
            type: el.getAttribute('type') || '',
            label: (el.textContent || '').trim().slice(0, 30),
            top: Math.round(rect.top),
            bottom: Math.round(rect.bottom),
            isVisible: rect.bottom <= viewportHeight + tolerance,
        });
    }
    return results;
}
"""

# JavaScript to find the actual content height
MEASURE_CONTENT_JS = """
() => {
    const target = document.querySelector('main') || document.body;
    let maxBottom = target.getBoundingClientRect().bottom;
    for (const el of target.querySelectorAll('*')) {
        const rect = el.getBoundingClientRect();
        if (rect.height > 0 && rect.bottom > maxBottom) {
            maxBottom = rect.bottom;
        }
    }
    return Math.round(maxBottom);
}
"""


@dataclass
class SimResult:
    sim: str
    iframe_height: int | None
    content_height: int | None
    status: str  # PASS, FAIL, ERROR, SKIP
    suggested_height: int | None
    clipped_elements: list[str] = field(default_factory=list)
    error: str | None = None


def extract_iframe_height(index_md: Path) -> int | None:
    """Extract the iframe height from an index.md file."""
    text = index_md.read_text()
    match = re.search(r'<iframe[^>]*\bheight="(\d+)(px)?"', text, re.IGNORECASE)
    return int(match.group(1)) if match else None


def discover_sims(base_dir: Path) -> list[dict]:
    """Find MicroSim directories containing both main.html and index.md."""
    if not base_dir.is_dir():
        print(f"Sims directory not found: {base_dir}", file=sys.stderr)
        sys.exit(1)
    sims = []
    for entry in sorted(base_dir.iterdir()):
        if not entry.is_dir():
            continue
        if (entry / "main.html").exists() and (entry / "index.md").exists():
            sims.append({"name": entry.name, "dir": entry})
    return sims


def round_up(value: int, step: int) -> int:
    return math.ceil(value / step) * step


def test_sim(page, sim: dict, iframe_height: int) -> SimResult:
    """Test a single MicroSim at the given iframe height."""
    html_path = sim["dir"] / "main.html"
    file_url = f"file://{html_path.resolve()}"

    page.set_viewport_size({"width": VIEWPORT_WIDTH, "height": iframe_height})

    try:
        page.goto(file_url, wait_until="networkidle", timeout=15000)
    except Exception as e:
        return SimResult(
            sim=sim["name"],
            iframe_height=iframe_height,
            content_height=None,
            status="ERROR",
            suggested_height=None,
            error=f"Failed to load: {e}",
        )

    # Wait for p5.js / vis-network / Chart.js to render controls
    page.wait_for_timeout(2000)

    # Measure control positions
    measurements = page.evaluate(
        MEASURE_CONTROLS_JS,
        {"sel": CONTROL_SELECTORS, "viewportHeight": iframe_height, "tolerance": TOLERANCE},
    )

    # Measure actual content height
    content_height = page.evaluate(MEASURE_CONTENT_JS)

    clipped = [m for m in measurements if not m["isVisible"] and m["tag"] != "canvas"]
    suggested = round_up(content_height + SAFETY_MARGIN, 10)
    status = "PASS" if not clipped else "FAIL"

    return SimResult(
        sim=sim["name"],
        iframe_height=iframe_height,
        content_height=content_height,
        status=status,
        suggested_height=suggested if status == "FAIL" else iframe_height,
        clipped_elements=[
            f"{c['tag']}{'[' + c['type'] + ']' if c['type'] else ''} \"{c['label']}\" bottom={c['bottom']}px"
            for c in clipped
        ],
    )


def write_report(path: Path, results: list[SimResult], sims_dir: str):
    """Write a markdown report of the test results."""
    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    skipped = sum(1 for r in results if r.status == "SKIP")

    lines = [
        "# MicroSim Iframe Height Test Report",
        "",
        f"Tested: {datetime.now(timezone.utc).isoformat()}",
        f"Sims directory: `{sims_dir}`",
        "",
        "| MicroSim | Iframe Height | Content Height | Status | Suggested Height |",
        "|----------|---------------|----------------|--------|------------------|",
    ]

    for r in results:
        ih = r.iframe_height or "\u2014"
        ch = r.content_height or "\u2014"
        sh = r.suggested_height or "\u2014"
        st = "**FAIL**" if r.status == "FAIL" else r.status
        lines.append(f"| {r.sim} | {ih} | {ch} | {st} | {sh} |")

    failures = [r for r in results if r.status == "FAIL"]
    if failures:
        lines += ["", "## Failures Detail", ""]
        for r in failures:
            lines.append(f"### {r.sim}")
            lines.append(f"- Iframe height: {r.iframe_height}px")
            lines.append(f"- Content height: {r.content_height}px")
            lines.append(f"- Suggested height: {r.suggested_height}px")
            lines.append("- Clipped elements:")
            for el in r.clipped_elements:
                lines.append(f"  - {el}")
            lines.append("")

    lines += ["", f"Summary: {passed} pass, {failed} fail, {errors} error, {skipped} skip out of {len(results)} total"]
    path.write_text("\n".join(lines))
    print(f"\nReport written to {path}")


def main():
    parser = argparse.ArgumentParser(description="Test MicroSim iframe heights with Playwright")
    parser.add_argument("--sims-dir", default="docs/sims", help="Path to sims directory")
    parser.add_argument("--sim", default=None, help="Test a single sim by name")
    parser.add_argument("--height", type=int, default=None, help="Override iframe height for all sims")
    parser.add_argument("--report", default=None, help="Write markdown report to this path")
    args = parser.parse_args()

    sims_dir = Path(args.sims_dir)
    sims = discover_sims(sims_dir)

    if args.sim:
        sims = [s for s in sims if s["name"] == args.sim]
        if not sims:
            print(f'MicroSim "{args.sim}" not found in {sims_dir}', file=sys.stderr)
            sys.exit(1)

    print(f"Testing {len(sims)} MicroSim(s) in {sims_dir}\n")

    results: list[SimResult] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for sim in sims:
            iframe_height = args.height or extract_iframe_height(sim["dir"] / "index.md")

            if not iframe_height:
                print(f"  SKIP  {sim['name']} \u2014 no iframe height found in index.md")
                results.append(SimResult(
                    sim=sim["name"], iframe_height=None, content_height=None,
                    status="SKIP", suggested_height=None, error="No iframe height in index.md",
                ))
                continue

            print(f"  Testing {sim['name']} ({iframe_height}px)...", end="", flush=True)
            result = test_sim(page, sim, iframe_height)
            results.append(result)

            if result.status == "PASS":
                print(" PASS")
            elif result.status == "FAIL":
                print(f" FAIL \u2014 content {result.content_height}px, suggest {result.suggested_height}px")
                for el in result.clipped_elements:
                    print(f"         Clipped: {el}")
            else:
                print(f" ERROR \u2014 {result.error}")

        browser.close()

    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    errors = sum(1 for r in results if r.status == "ERROR")
    skipped = sum(1 for r in results if r.status == "SKIP")

    print(f"\n--- Summary ---")
    print(f"  PASS: {passed}  FAIL: {failed}  ERROR: {errors}  SKIP: {skipped}  Total: {len(results)}")

    if args.report:
        write_report(Path(args.report), results, str(sims_dir))

    if failed > 0 or errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
