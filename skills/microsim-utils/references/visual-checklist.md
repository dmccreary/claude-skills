# Visual Checklist for MicroSim Layout Review

Walk this list item-by-item against the screenshot. For each item,
decide PASS / FAIL / N/A and quote what you see.

**Claude Vision is not deterministic.** What gets flagged in a
screenshot depends on what's actively being looked for — a casual
"does this look right?" pass misses defects that a directed "is the
left edge clipped?" question reliably catches. The whole point of
writing this checklist down is to force explicit attention to each
known failure mode, every time.

For every FAIL, write down:
- **What:** the defect (one phrase)
- **Where:** rough pixel region or named element ("left edge of 2×2 grid",
  "title row", "duration label below grid")
- **Evidence:** what you actually see ("the text reads `mpletion: true`,
  the leading `co` is missing")

Then go to `common-fixes.md` to look up the patch.

---

## 1. Text legibility

### 1.1 Clipped text at canvas edges
Any text whose first or last character is partly cut off by the canvas
edge or the boundary of an enclosing rectangle. Common locations:
- Row labels on a 2×2 grid (left edge)
- Long titles (right edge)
- JSON keys at the right boundary of a JSON panel
- Slider labels in the control area at narrow widths

**PASS:** every visible text element shows complete characters, with at
least 2px of padding from any boundary.

### 1.2 Clipped text at panel edges
Like 1.1 but inside a sub-panel (info box, JSON panel, annotation
rectangle). The panel rectangle is drawn but text inside spills past
its border.

### 1.3 Residual text strokes
Text rendered with a black or colored outline because a `stroke()` call
was active when `text()` was invoked. This produces an ugly halo around
every glyph and is the #1 most common p5.js text bug.

**PASS:** body text is rendered as flat fills (no outline halo).

### 1.4 Low-contrast text
Text whose color is too close to its background to be comfortably read.
Examples: light-gray text on a white panel; pale-yellow text on
aliceblue.

**PASS:** body text contrast ratio looks ≥ 4.5:1 (judged visually — you
don't need to compute it).

### 1.5 Text size too small
Body text smaller than ~12px. Title text smaller than ~16px. The course
standard is "readable from the back of a classroom" — labels that look
postage-stamp-small on a 800px screenshot will be illegible there.

---

## 2. Control region

### 2.1 Slider extends past right edge of canvas
The right end of a slider track touches or crosses the canvas right edge
without margin. Should have ~15–25px of visible white between the slider
end and the canvas border.

### 2.2 Slider label overlaps slider track
The text "Speed: 7" overlaps the colored portion of the slider. Indicates
`sliderLeftMargin` is too small for the label width, or the label is
positioned with too high an `x` value.

### 2.3 Buttons overlap each other
Two buttons share pixels. Indicates `position()` calls placed them with
the same or insufficiently-spaced `x` values.

### 2.4 Buttons extend past right edge
A row of buttons runs out of canvas. The control row is too long for the
current canvas width; buttons need to wrap to a second row, or labels
need to be shorter.

### 2.5 Vertical alignment of label / value / slider
For a row containing `[ Label: 7 ] [============slider============]`, the
label baseline and slider track centerline should be visually aligned.
A common bug is text drawn at `drawHeight + 15` while the slider sits at
`drawHeight + 5`, making the label appear "above" the slider instead of
beside it.

### 2.6 Control region top boundary
The control region (white background) starts at exactly `drawHeight`
with no gap from the drawing region above and no controls peeking above
the boundary line.

### 2.7 Control region bottom boundary
No control extends below `canvasHeight`. (This is the failure mode that
the `iframe-tester` utility catches with bounding boxes, but verify it
visually too — sometimes a button label wraps to two lines and the
bounding box doesn't reflect that.)

---

## 3. Drawing region

### 3.1 Title position and overlap
Title is centered and does not collide with right-side panels, axis
labels, or annotation boxes. Common bug: title centered at
`canvasWidth/2` overlaps the right-edge JSON panel.

### 3.2 Draw-order bugs
A background rectangle painted *after* its content erases the content
underneath. Symptoms: the title appears as a white sliver because the
header rectangle was drawn over it; grid lines visible only in some
quadrants because a panel covers others.

### 3.3 Panel overflow
Content drawn inside a panel rectangle (info box, JSON box, annotation)
spills outside the panel border. Either the panel is too small or the
text wrapping is missing.

### 3.4 Misaligned grid axes
For sims with coordinate axes, tick labels should sit aligned to their
ticks, not floating in space. The y-axis label "Imaginary Axis" should
be visually centered on the y-axis, not nudged off to one side.

### 3.5 2×2 grid (or any matrix) row/column labels
Row labels and column labels are fully visible, with enough left/top
margin reserved (`axisOffset` for row labels; row 0 of the grid pushed
down enough for column header text).

### 3.6 Highlighted state visible
If the sim shows a "current state" by highlighting a cell, button, or
node: the highlight is clearly distinguishable from non-highlighted
elements (different fill, border weight, or color), not just a 1px
nudge.

---

## 4. Color and visual hierarchy

### 4.1 Drawing area background present
Drawing region has the standard `aliceblue` fill with `silver` border.
A pure-white drawing area is a code smell — the `fill('aliceblue')` may
have been omitted.

### 4.2 Control area background present
Control region has the standard white fill, distinct from the drawing
region.

### 4.3 Color-coded JSON or syntax-highlighted output legible
For sims that render JSON: keys, strings, numbers, booleans should each
have a distinguishable color. All four colors should be readable on the
panel background.

### 4.4 Single dominant color drives the eye
If everything is the same color, the visual hierarchy collapses — the
learner doesn't know where to look. Conversely, if more than ~5 distinct
colors appear, the design is noisy.

---

## 5. Library-specific elements

These items only apply when the sim uses the named library. For sims
using a library not listed here, fall back to sections 1–4 and note
the gap in the report so future runs can extend coverage.


### 5.1 Mermaid diagrams: subgraph titles not collided with arrows
For TD-layout Mermaid diagrams, an arrow entering the top of a lower
subgraph crosses the subgraph title. The title should be shifted right
(see CLAUDE.md) so the arrow lands clear of it.

### 5.2 vis-network / network graphs: edge labels readable
Edge labels on perfectly horizontal edges have a known rendering bug —
a slight y-offset is required. If edge labels are missing or smeared,
suspect this.

### 5.3 Charts: legend present and labeled
Bar / line / pie charts have a legend, axis labels, and a title. A
naked chart with no legend is incomplete.

### 5.4 Maps: scale, north arrow, attribution
Leaflet maps have at minimum a scale indicator and the OSM attribution
("© OpenStreetMap contributors"). Missing attribution is a license
violation, not just a layout defect.

---

## 6. Sanity checks

### 6.1 Sim renders at all
The screenshot is not blank, not all-white, not all-black. The script
loaded and `setup()` ran. If the screenshot is empty, `bk-capture-screenshot`
captured before JS finished — increase the delay parameter (try 5).

### 6.2 No console-error indicators
Some libraries draw a red error banner on canvas when they crash. If
visible, the sim has a JS error — open browser DevTools or inspect the
console output before continuing.

### 6.3 Aspect ratio matches iframe height
The screenshot height (in pixels) should match the iframe height
declared in `index.md`. If the screenshot is dramatically taller or
shorter, the height passed to `bk-capture-screenshot` is wrong.

---

## How to write the review

After walking the checklist, summarize like this:

```
Sim: result-field-composition-explorer
Iframe height: 577
Screenshot: docs/sims/result-field-composition-explorer/result-field-composition-explorer.png

FAILS:
  1.1 Clipped text at canvas edges — Row labels "completion: true" and
      "completion: false" on the left edge of the 2×2 grid. The leading
      "co" is missing; reads as "mpletion: true".
  3.5 2×2 grid row labels — same as above; insufficient axisOffset.

PASSES (confirmed): 1.3, 1.4, 2.1–2.7, 3.1–3.3, 4.1–4.3, 6.1–6.3.
N/A: 1.2, 3.4, 5.x (no Mermaid/network/chart/map elements).
```

Then go to `common-fixes.md` for the patch.
