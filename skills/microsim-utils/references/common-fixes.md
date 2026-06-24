# Common Fixes — Symptom → Source Patch

Each entry maps a checklist FAIL to its likely cause and the smallest
edit that resolves it. The "why" line explains the underlying bug
pattern so you can recognize it next time, even if it manifests
slightly differently.

**Where the patch lives** depends on the library:

| Library | Patch file | Notes |
|---------|------------|-------|
| p5.js | `<sim-id>.js` | Canvas drawing in `draw()` / `setup()` |
| Chart.js | `<sim-id>.js` | Chart options object |
| vis-network / vis-timeline | `<sim-id>.js` | Network options / data |
| Leaflet | `<sim-id>.js` | Map config + layers |
| Mermaid | `main.html` | Inline `mermaid.initialize({...})` and graph |
| Hand-rolled HTML/SVG | `main.html` and/or CSS | DOM + styles |
| Content-driven | `data.json` or `*.mmd` | Data-shape defects |

Items below are **library-agnostic** unless their heading is tagged
with a library name (e.g. *(p5.js)*). The library-specific patterns
live in their own sections at the bottom.

---

## Clipped row/column labels on a grid

**Likely cause:** The grid drawing code reserves a fixed offset
(`axisOffset`, `gridLeft`, `marginLeft`) for axis labels, and the
reservation is smaller than the widest label's `textWidth()`.

**Find:** in the function that draws the grid, look for a constant like
`const axisOffset = 60` or `const gridX = 80`. Identify the longest
row/column label your sim renders.

**Fix:** increase the offset to at least `textWidth(longestLabel) + 8`
at the current text size. For 13-pt text and a label like
"completion: false" (~96px wide), 110 is a safe value.

**Why:** the label is right-aligned to `gridArea.x - 4`, so if the
label width exceeds `gridArea.x`, it spills off the canvas. Anchoring
to a hard-coded number assumes label widths that may not hold.

---

## Title overlaps a right-side panel

**Likely cause:** title centered at `canvasWidth/2`, but a JSON / info
panel occupies the right ~40% of the canvas. The center-x falls inside
the panel.

**Find:** look for `text(titleString, canvasWidth / 2, ...)` near the
top of `draw()`.

**Fix options (in order of preference):**
1. Move the title to top-left: `textAlign(LEFT, TOP); text(title, margin, 8);`
2. Center over the *left* panel only: `text(title, leftPanelX + leftPanelW/2, 8);`
3. Shrink the title size so it fits between the left edge and the panel.

**Why:** centering at canvas-midpoint assumes a single full-width
content region. As soon as you split into 2-column layouts, the
midpoint is no longer "above your content".

---

## Text has an ugly black outline (residual stroke) *(p5.js)*

**Likely cause:** a `stroke()` call (often inside a `rect()` or `line()`
draw) is still active when `text()` is called. p5 strokes glyphs by
default if a stroke color is set.

**Find:** scan the `draw()` function for the sequence `stroke(...) →
... → text(...)`. Find every `text()` call and check whether `noStroke()`
appears within the previous handful of lines.

**Fix:** add `noStroke();` immediately before the `text()` call.

**Why:** p5 keeps the stroke state global across draw calls. A single
missing `noStroke()` propagates through every subsequent `text()` until
another `stroke()`/`noStroke()` toggles it. The CLAUDE.md rule "Always
place a `noStroke();` before each `text()` element" exists for this
reason — it's a stateful API where the easy default is wrong.

---

## Slider extends past the right edge of the canvas *(p5.js)*

**Likely cause:** the slider's `size()` was set in `setup()` only and
not updated in `windowResized()`. When the canvas grew or shrunk, the
slider track did not match.

**Find:** look at `windowResized()`. Every horizontal slider should
have a `slider.size(canvasWidth - sliderLeftMargin - margin)` line.

**Fix:** add the missing `size()` call. Use the same formula every
slider in the sim uses (don't invent a new one).

**Why:** p5 controls are HTML elements positioned absolutely; they
don't auto-resize with the canvas. The widthresponsive pattern requires
explicitly resizing every slider whenever the canvas resizes.

---

## Slider label overlaps slider track *(p5.js)*

**Likely cause:** `sliderLeftMargin` is too small for the label width,
so the slider starts before the label ends. Or the label is being
positioned with `x` ≥ `sliderLeftMargin`.

**Find:** check the value of `sliderLeftMargin` and the `text(...)`
calls for slider labels. Measure the longest label string.

**Fix:** widen `sliderLeftMargin` until it exceeds the longest label's
right edge by at least 10px. Default is 140; for sims with verbose
labels like "Min: 0  Scaled: 0.70", bump to 220.

**Why:** every slider in the row must clear the longest label across
all rows, not just its own row's label. The constant
`sliderLeftMargin` is shared.

---

## Buttons overlap each other *(p5.js — manual positioning)*

**Likely cause:** two `button.position(x, y)` calls have the same `x`,
or `x` values that are closer than the button widths. (For HTML-based
sims, this manifests differently — usually as missing `gap` in flexbox
or insufficient column count in a grid.)

**Find:** grep for `.position(` in `setup()`. Track the `x` values for
each button and compute the gap.

**Fix:** assign each button a unique `x` based on cumulative width.
Pattern: `let px = 10; ... preset1.position(px, ...); px += preset1Width + 10;`

**Why:** p5 doesn't lay out buttons automatically — every position is
manual. A copy-paste mistake easily produces overlapping `x` values
that are not caught at compile time.

---

## Buttons run off the right edge of the canvas

**Likely cause:** total button-row width exceeds `canvasWidth` at the
test viewport (800px).

**Fix options:**
1. Shorten the button labels ("Passed Cleanly" → "Pass") if the
   shorter label is still self-explanatory.
2. Wrap buttons to a second row by increasing `controlHeight` and
   placing the second-row buttons at `drawHeight + 35 + (rowIdx × 35)`.
3. Reduce per-button width via `button.size(width, 26)`.

**Why:** the 800px viewport in `bk-capture-screenshot` is intentionally
narrower than a desktop browser window — it represents the embedded
content column in MkDocs. Buttons that fit in the p5 editor preview at
1200px may not fit in the embedded iframe.

---

## Title clipped or invisible

**Likely cause (a):** the background rectangle covers the title. Draw
order is wrong — `rect(...)` was called *after* `text(title, ...)`.

**Likely cause (b):** the title's `y` position is negative or above
the canvas. Check for `text(title, x, -5)` or similar.

**Fix:** confirm the draw order is: background fill → grid/axes →
title → content → controls. Move `text(title, ...)` after all
background `rect(...)` calls.

**Why:** p5 draws in z-order = call order. A background drawn last
goes on top, hiding everything underneath. The CLAUDE.md note "draw
title AFTER grid/axes" is the explicit fix.

---

## Panel content overflows panel border

**Likely cause:** the panel's height is fixed but its content (e.g.,
JSON lines) exceeds it. Content draws past the bottom edge of the
panel rectangle.

**Find:** locate the panel's height value and the loop that emits the
content. Count the lines or measure the content height.

**Fix options:**
1. Increase panel height to fit the content + padding.
2. Truncate the content (e.g., long strings → first 30 chars + "…").
3. Reduce the line-height in the rendering loop.

**Why:** p5 has no clipping by default — content drawn outside a
`rect()` boundary just renders past it. There's no scroll bar to
warn you. The footgun: `overflow: hidden` on the parent div hides the
overflow visually in the iframe (because the iframe has fixed height
and `scrolling="no"`), but the content is still rendering past the
panel — students at narrow viewports see it.

---

## Drawing area background is white instead of aliceblue *(p5.js)*

**Likely cause:** the `fill('aliceblue')` call before the drawing-area
`rect(...)` was omitted, or the wrong fill is set when the rect is
drawn.

**Find:** search for `rect(0, 0, canvasWidth, drawHeight)`. Verify
the immediately-preceding lines set the right fill and stroke.

**Fix:** add `fill('aliceblue'); stroke('silver');` before the
drawing-area rect.

**Why:** the standard color scheme (aliceblue draw / white control /
silver border) is what makes the two regions visually distinct. A
white-on-white sim looks like the control area swallowed the drawing
region.

---

## Highlight state is invisible or barely visible

**Likely cause:** highlight color is too close to the unhighlighted
fill, or only a 1px stroke change.

**Find:** the conditional that toggles highlight (`isCurrent`,
`isSelected`, etc.) and the fill/stroke values it sets.

**Fix:** make the highlight visually prominent — different fill color
(e.g., `'#fff3bf'` light yellow), thicker stroke (`strokeWeight(2)`),
or contrasting border color (`stroke('#f08c00')`).

**Why:** the whole point of highlighting is to direct attention. A
subtle highlight defeats its own purpose.

---

## 2×2 grid column header collides with row 0 of cells

**Likely cause:** the column header text is drawn at `cellArea.y - 4`
(just above the cells), but the cell rect is drawn at `cellArea.y`.
If the header text is taller than 4 px, it overlaps the cell border.

**Fix:** increase the gap. Move the header to `cellArea.y - 8` or
`cellArea.y - 10`, and either bump `cellArea.y` down by the same amount
or accept slightly less cell height.

---

## Mermaid TD subgraph title under an incoming arrow

This is documented in the project's CLAUDE.md. The fix is a small
post-render JavaScript shim that nudges the title's `transform`
attribute (not CSS `transform`). See the working reference at
`docs/sims/full-pipeline-architecture/main.html`.

---

## Sim doesn't render (blank screenshot)

**Likely cause (a):** `bk-capture-screenshot` captured before JS
finished. Increase the delay (3 → 5 seconds).

**Likely cause (b):** a JS error in the sim. Run the sim in a real
browser and check the DevTools console.

**Likely cause (c, p5.js):** the canvas was created with zero width
because `updateCanvasSize()` ran before the container existed. Confirm
`updateCanvasSize()` is the first line of `setup()`.

**Likely cause (d, library load):** the CDN script in `main.html`
points at a version that no longer exists, or the page is offline.
Check the browser console; pin the library version and re-test.

---

## When in doubt

If a defect doesn't match any pattern here, do this:

1. Read the relevant section of the source file (the function or
   block that produces the affected region — for p5.js that's a
   `draw()` segment, for Mermaid it's the graph definition or
   `mermaid.initialize` config, for Chart.js it's the options object,
   etc.).
2. Look for hardcoded constants that ought to be derived (a magic
   `60` that should be `textWidth(label) + 8`; a fixed pixel offset
   that should be relative to a parent's measured size).
3. Look for missing state resets — for p5.js that's `noStroke()`,
   `textAlign()`, `textSize()` between sections; for canvas-based
   charting libraries it's `ctx.save()` / `ctx.restore()` around
   custom plugins.
4. Look for draw-order errors (background drawn after content; CSS
   `z-index` inverted; SVG element added late so it stacks on top of
   labels).

Then add a new entry to this file — labeled with the library if it's
library-specific — so the next reviewer doesn't have to rediscover
it.
