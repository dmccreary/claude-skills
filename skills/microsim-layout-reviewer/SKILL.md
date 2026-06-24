---
name: microsim-layout-reviewer
description: Reviews a MicroSim's visual layout using Claude Vision — screenshots at the declared iframe height and checks for clipped labels, overlapping controls, and library-specific rendering bugs. Use after generating a new MicroSim or when something looks off.
---

# MicroSim Layout Reviewer

## Purpose

A "MicroSim" is any interactive program embedded in an iframe and built
to educational-content standards (`docs/sims/<sim-id>/main.html` plus
metadata, screenshot, index page). The library doesn't matter — p5.js,
Mermaid, Chart.js, vis-network, vis-timeline, Leaflet, or hand-rolled HTML/SVG are all
valid implementations. What they share is the iframe contract: fixed
height, no scroll, embedded inside an MkDocs page.

`microsim-iframe-tester` uses Playwright to verify every interactive
control sits *inside* the iframe boundary. That catches "the slider got
cut off at the bottom" but it does not catch "the row label says
`mpletion: false` because the axis-offset is too small", "the title
overlaps the JSON panel", "every text element has an ugly black outline
because someone forgot a `noStroke()`", or "the bar chart's tolerance
band rises into the chart title". Those defects are obvious to a human
looking at the sim — and obvious to **Claude Vision** looking at the
screenshot — but invisible to geometric checks.

This skill is the visual-review counterpart. It captures the sim at its
real iframe height, looks at the image with intent, and patches the
source where the rendering is wrong.

## When to use

- Right after generating a new MicroSim (proactive QA)
- When the user pastes a screenshot and says "this looks off"
- When iframe height is correct but the layout still looks broken
- When a sim worked at one width and now looks wrong at another

If the issue is "controls clipped at the bottom of the iframe" only,
prefer `microsim-iframe-tester` first — it gives a precise suggested
height. Use this skill when the issue is *inside* the canvas, not at
its edges.

## Workflow

### 1. Resolve the target sim

The user will give you a sim directory, a sim-id, or just say "the one
I just made". Resolve to an absolute path. The path must contain
`main.html` and `index.md`. Most sims also have one or more source
files alongside (`*.js`, `*.css`, sometimes `*.mmd` or `data.json`),
but Mermaid and pure-HTML sims may have all the layout logic inside
`main.html` itself.

### 2. Identify the source file you'll patch if needed

Open `main.html` and note:

- Which `<script src="...">` tags it loads from local files (those
  `.js` files are likely candidates for layout fixes).
- Whether the rendering library is configured inline (Mermaid's
  `mermaid.initialize({...})`, Chart.js options object, etc.) — in
  which case the patch may live in `main.html` itself.
- Whether a `data.json` or `*.mmd` file holds the structural content
  (some defects are in data, not code).

You don't need to read the source yet — just know where to look.

### 3. Read the iframe height from `index.md`

Find `<iframe src="main.html" height="NNNpx" ...>`. Extract `NNN`. This
is the height the sim renders at in the textbook, so this is what you
must screenshot at — not the tool's default. If `index.md` has no
iframe (rare, on new scaffolds), fall back to the `// CANVAS_HEIGHT:`
comment in the JS source plus 2.

### 4. Capture a screenshot

```bash
bk-capture-screenshot <sim-dir> 3 <iframe-height>
```

Renders headless Chrome at 800 px wide × the requested height, waits
the delay seconds for JS to settle, writes `<sim-dir>/<sim-id>.png`.

If `bk-capture-screenshot` is not on PATH, tell the user — don't write
your own headless Chrome wrapper.

### 5. Read the screenshot

Use the `Read` tool on the PNG. The image is passed into context as
visual content for **Claude Vision** to analyze directly — no OCR, no
image-processing libraries. Claude Vision sees pixels the way a human
reviewer does: text legibility, color contrast, alignment, overlap,
clipping at edges. Capability tracks the model version, so when this
skill is invoked under a newer model it should produce sharper review
output without changes here. Note the active model version (e.g.
"Claude Vision (Opus 4.7)") when you write the review summary in
step 10.

### 6. Apply the visual checklist

Read `references/visual-checklist.md` and walk every item against the
screenshot you just loaded. Don't skim — go item by item. Claude
Vision is **not deterministic**: what gets flagged depends on what
you're actively looking for. The checklist disciplines review into
reliable output by forcing explicit inspection of every known failure
mode rather than a vague "does this look OK?".

For each item, decide: **PASS**, **FAIL**, or **N/A** (e.g., "no JSON
panel in this sim", "no Mermaid in this sim"). Quote the specific
evidence — *what you see* — for any FAIL.

The checklist's library-specific section (5.x) covers Mermaid,
vis-network, Chart.js, and Leaflet patterns. If the sim uses a library
not yet covered, fall back to the general items (1–4) and note the
gap.

### 7. Diagnose and patch

For each FAIL, consult `references/common-fixes.md`. It maps each
visual symptom to the likely root cause(s) and the specific edit that
fixes it. Some fixes are library-agnostic (draw order, panel overflow,
text contrast), others are library-specific and labeled as such (p5.js
stroke-state, Mermaid subgraph-title collisions, vis-network edge-label
y-offset).

Make the smallest change that resolves the defect. Edit the source
file you identified in step 2 — that's typically a `.js` for p5.js /
Chart.js / vis-network / Leaflet sims, or `main.html` for Mermaid and
inline-config sims, or a `data.json` / `*.mmd` for content-driven
defects.

If the defect is iframe-height-related (content extends past the
iframe edge), do *not* fix it here — hand off to
`microsim-iframe-tester` and `fix-iframe-heights.py`.

### 8. Re-capture and verify

Re-run the screenshot, re-read it, walk the same checklist. The fixes
should turn FAILs into PASSes without introducing new FAILs.

If a fix doesn't resolve the issue, *do not* keep widening the same
parameter (e.g., ratcheting `axisOffset` from 60 → 110 → 160 → 200).
Stop and think: the lever you're pulling may not be the right one.
Re-read the source around the suspect area and look for an unrelated
cause.

### 9. Stop after 3 review-patch cycles

If the third re-capture still shows issues, stop and report what's
left. More tweaking usually means the design has a deeper issue that
needs human judgement — better to surface that than to quietly produce
something subtly worse.

### 10. Report

For each sim reviewed:

- Library / source file(s) touched
- Initial defects found (one line per FAIL with quoted evidence)
- Edits applied (`file:line`, what changed)
- Final state (clean / partial / unfixed) with a one-sentence reason
- Active **Claude Vision** model version (anchors the judgment for
  future re-reads)

## What this skill does *not* do

- Does not replace `microsim-iframe-tester`. If the iframe is the
  wrong height, run that first.
- Does not redesign sims. If the layout is fundamentally poorly
  conceived (e.g., 12 controls crammed into one row), surface the
  symptoms and stop.
- Does not modify approved sims. If `index.md` frontmatter has
  `status: approved`, skip the sim and tell the user — approved sims
  are locked from incidental edits.

## Reference files

- `references/visual-checklist.md` — every item to inspect, with what
  PASS/FAIL look like, and a library-specific section.
- `references/common-fixes.md` — symptom → root-cause → edit, with
  library-specific fixes labeled (p5.js, Mermaid, vis-network, etc.).
  Read this when diagnosing a FAIL, not before.
