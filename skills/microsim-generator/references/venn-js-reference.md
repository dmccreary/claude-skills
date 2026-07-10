# venn.js Reference

API and syntax details for `venn.js` (v0.2.20, https://github.com/benfred/venn.js), used by the
venn-diagram-generator workflow (`references/venn-guide.md`). This file covers the library's
rendering API — data format and educational-tooltip design are covered in the guide itself.

## Loading the Library

`venn.js` renders through D3, so both scripts are required and D3 must load first:

```html
<script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/venn.js@0.2.20/venn.js"></script>
```

## Rendering a Diagram

```javascript
var chart = venn.VennDiagram()
    .width(600)
    .height(450);

d3.select('#venn-diagram')
    .datum(sets)      // the sets array — see venn-guide.md Step 2 for the data format
    .call(chart);
```

`venn.VennDiagram()` returns a reusable chart function. Calling `.width()`/`.height()` before
`.call()` sets the SVG dimensions; call `chart.width(w).height(h)` again and re-`.call()` to
resize (see the resize handler in `assets/templates/venn/script.js`).

## Selecting Regions

After rendering, each set and intersection is a `<g class="venn-area">` containing one `<path>`
(the filled region) and one `<text>` (the label). The bound datum `d` on each `.venn-area` is
`{sets: ["A", "B"], size: N}` — the same object passed in via the `sets` array.

```javascript
d3.selectAll('.venn-area')
    .style('cursor', 'pointer');

// Regions for a single named set only (not an intersection):
d3.selectAll('.venn-circle path')
    .filter(function (d) { return d.sets.length === 1 && d.sets[0] === 'Python'; });
```

Useful selectors:

| Selector | Selects |
|----------|---------|
| `.venn-area` | Every region (sets and intersections) — the `<g>` wrapper |
| `.venn-circle` | Only single-set (non-intersection) regions |
| `.venn-area path` | The filled shape for a region |
| `.venn-area text` | The label for a region |

## Styling

`venn.js` does not apply colors itself — style the `<path>` elements after rendering:

```javascript
d3.selectAll('.venn-area path')
    .style('fill-opacity', 0.7)
    .style('stroke-width', 2);
```

Recommended opacity range is 0.70–0.85: high enough that overlap colors visibly blend, low
enough that labels stay readable. Font size is set in CSS (`#venn-diagram text`), not through
the JS API — keep it at the repository's 16px accessibility minimum.

## Hover Interactions

Use standard D3 event binding on `.venn-area`; `d` in the handler is the region's datum:

```javascript
d3.selectAll('.venn-area')
    .on('mouseover', function (event, d) {
        // d.sets is the array of set names for this region, e.g. ["AI", "ML"]
    })
    .on('mouseout', function (event, d) { /* ... */ });
```

`venn.js` ships a `venn.sortAreas()` and hover-highlight helper (`venn.wrapText`, deprecated
in some forks) but the repository template does not depend on them — plain D3 event handlers
are more portable across the several forks of `venn.js` published to npm.

## Sizing Rules (Library Constraints)

- Every intersection's `size` must be ≤ the smallest `size` of the sets it intersects. Violating
  this produces a diagram venn.js still renders, but with visually wrong proportions.
- `venn.js` uses a best-fit layout (not exact set-theoretic geometry) when more than 3 circles
  are requested — expect visible approximation error above 3 sets. Prefer 2–3 sets when
  proportional accuracy matters; use symbolic equal sizes for 4-set diagrams.

## Troubleshooting (Library-Specific)

- **Diagram renders as a single point/collapsed circle**: usually an intersection `size` larger
  than one of its parent sets — see sizing rule above.
- **`venn is not defined`**: the venn.js `<script>` tag loaded before D3, or D3 failed to load.
  D3 must be present on `window.d3` before venn.js executes.
- **Labels overlap circles awkwardly**: `venn.js` centers labels automatically; if a small
  intersection's label collides with a neighboring circle, shorten the label text rather than
  trying to reposition it — the library does not expose a per-label offset API.

## External Resources

- venn.js GitHub: https://github.com/benfred/venn.js
- venn.js Examples: https://benfred.github.io/venn.js/
- D3.js Documentation: https://d3js.org/
