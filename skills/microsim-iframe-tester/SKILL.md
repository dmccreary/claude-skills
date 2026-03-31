---
name: microsim-iframe-tester
description: Test whether MicroSim controls (buttons, sliders, dropdowns) are fully visible inside their iframe without being clipped. Uses Playwright to load each MicroSim's main.html, measure actual content height, and compare against the iframe height declared in index.md. Use this skill whenever the user mentions iframe height testing, MicroSim visibility checking, controls being cut off, iframe sizing, or wants to verify that MicroSims render correctly at their configured heights. Also trigger when the user says things like "check if my sims fit", "are the controls visible", "test iframe heights", or "fix clipped controls".
---

# MicroSim Iframe Height Tester

## Purpose

MicroSims are embedded in MkDocs pages via `<iframe>` tags with fixed heights and `scrolling="no"`. If the iframe height is too short, controls at the bottom (sliders, buttons, dropdowns) get clipped and students can't interact with them. This skill automates checking that every MicroSim's controls are fully visible at the declared iframe height.

## How It Works

The test script is available in both Python (`scripts/test-iframe-heights.py`) and Node.js (`scripts/test-iframe-heights.js`). Both produce identical results. The Python version is recommended as it has no `node_modules` dependency. It uses Playwright to:

1. Find all MicroSim directories under `docs/sims/`
2. Read each `index.md` to extract the declared iframe height
3. Load `main.html` in a browser viewport constrained to that height
4. Wait for p5.js (or other libraries) to finish rendering controls
5. Find all interactive elements (buttons, sliders, selects, inputs, checkboxes)
6. Check whether each element's bounding box fits within the iframe height
7. Measure the actual content height needed
8. Report pass/fail with recommended height for failures

## Prerequisites

Playwright must be installed with Chromium:

```bash
# Python (recommended)
pip install playwright
playwright install chromium

# Node.js (alternative)
npm install playwright
npx playwright install chromium
```

## Running the Tests

### Python (recommended)

```bash
# Test all MicroSims
python scripts/test-iframe-heights.py --sims-dir docs/sims

# Test a single MicroSim
python scripts/test-iframe-heights.py --sims-dir docs/sims --sim energy-pyramid

# Test with a custom height override (ignores index.md heights)
python scripts/test-iframe-heights.py --sims-dir docs/sims --height 530

# Generate a markdown report
python scripts/test-iframe-heights.py --sims-dir docs/sims --report report.md
```

### Node.js (alternative)

```bash
node scripts/test-iframe-heights.js --sims-dir docs/sims
node scripts/test-iframe-heights.js --sims-dir docs/sims --sim energy-pyramid
node scripts/test-iframe-heights.js --sims-dir docs/sims --height 530
node scripts/test-iframe-heights.js --sims-dir docs/sims --report report.md
```

## Reading the Output

The script outputs a table like:

```
MicroSim                    | Iframe Height | Content Height | Status | Suggested Height
----------------------------|---------------|----------------|--------|------------------
energy-pyramid              |           532 |            528 | PASS   |              532
predator-prey               |           697 |            720 | FAIL   |              730
greenhouse-effect           |           500 |            498 | PASS   |              500
```

- **PASS**: All controls fit within the iframe height (with 5px tolerance)
- **FAIL**: One or more controls extend below the iframe boundary
- **Suggested Height**: The actual content height rounded up to the nearest 10px, plus a 10px safety margin

## Fixing Failures

For each failing MicroSim, update the iframe height in `index.md`:

```html
<!-- Before -->
<iframe src="main.html" height="500" width="100%" scrolling="no"></iframe>

<!-- After — use the suggested height from the report -->
<iframe src="main.html" height="540" width="100%" scrolling="no"></iframe>
```

Also update the `// CANVAS_HEIGHT:` comment in the JavaScript file if present, and any chapter markdown files that embed the same sim.

## Step-by-Step for Claude

When the user asks to test iframe heights:

1. Confirm the project root contains `docs/sims/` with MicroSim directories
2. Check that `scripts/test-iframe-heights.py` exists in the skill directory at `~/.claude/skills/microsim-iframe-tester/scripts/`
3. Run `playwright install chromium` if not already installed
4. Copy or reference the test script and run it from the project root
5. Present the results to the user
6. For failures, offer to update the iframe heights in the affected `index.md` files
7. If chapter markdown files also embed the failing sims, update those too
