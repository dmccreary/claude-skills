# Iframe Height Pinning — Why It Works This Way

> **Historical snapshot — non-authoritative.** This archived reference
> describes an older DOM and runtime contract that was never implemented by
> the consolidated skill. Do not use it to generate or modify overlays. The
> current source of truth is
> `skills/microsim-generator/references/overlay-iframe-height-pinning.md`.

**Audience:** future-you (or another contributor) trying to understand,
debug, or modify the `reportHeight()` logic in
`docs/sims/shared-libs/diagram.js`. Read this *before* changing anything
in that method, because the design has several non-obvious constraints
working at the same time.

## The Problem in One Sentence

A diagram-overlay sim has variable-height content (the `#infobox` text
swaps in and out as the student clicks different callouts), but the
embedding iframe must have a fixed height that does not jump around
mid-interaction.

## The Two Failure Modes We're Avoiding

If we just measured `document.body.scrollHeight` once at load and posted
it, we'd hit one of these two bad outcomes:

1. **Iframe too short.** The student clicks a callout with a long
   description and the infobox text overflows the iframe, causing a
   scroll bar inside the iframe and partially hidden controls.
2. **Iframe too tall.** The student is on a callout with a short
   description (or just the "Click a marker..." prompt) and there is a
   wide empty band of dead space below the controls, because the iframe
   was sized for a worst-case that isn't currently displayed.

A naïve "re-measure on every callout click" approach avoids both, but
introduces a *third* failure: the iframe pops up and down by 30–80 px
every time the student clicks. For a Grade 5 reader, this is jarring —
the page literally moves under the cursor mid-click.

## The Solution: Worst-Case Measure + Pin the Infobox

`reportHeight()` does three things in a precise order:

1. **Find the worst-case content.** It scans `data.callouts` and picks
   the one whose `description.length + ap_tip.length` is largest. That
   callout is the one that will produce the tallest infobox box.

2. **Temporarily fill the infobox with that worst-case content.** It
   writes the longest callout's label, description, and (if present)
   ap_tip into the infobox elements. The DOM rerenders and the infobox
   takes its maximum possible visual height.

3. **Capture two heights and pin the infobox.** While the infobox is
   still filled with the worst-case content:
   - Read `infoboxEl.offsetHeight` and assign it as an inline
     `style.minHeight = "{px}px"` on the infobox element.
   - Read `document.body.scrollHeight + 30` and post that as the
     iframe's target height via `postMessage`.

4. **Restore the original infobox content.** The label, description,
   and ap_tip are written back to whatever they were before
   `reportHeight()` was called (typically the "Click a marker..."
   prompt).

The trick is **step 3**: the inline `min-height` survives step 4. When
the infobox content shrinks back to the prompt, the *content* inside
the infobox is now small, but the *box itself* still occupies the
worst-case pixel height because of the pinned `min-height`. The infobox
just has whitespace below the prompt text now.

## Why Pinning the Infobox Keeps the Controls Stationary

DOM order in `main.html` is fixed and must not be changed:

```
#layout      ← image + label panels (height is constant)
#infobox     ← text content (height varies → now pinned)
#controls    ← Explore/Quiz buttons (height is constant)
#edit-panel  ← hidden in normal mode
```

Every element below `#infobox` in the document flow inherits its
position from "the bottom of the infobox." Before pinning:

| Callout selected | `#infobox` height | `#controls` Y position |
|---|---|---|
| Short prompt     | 110 px | layout + 110 |
| Short description | 140 px | layout + 140 |
| Long description + ap_tip | 240 px | layout + 240 |

The controls jumped 130 px between the shortest and tallest states.

After pinning to the worst case (240 px in the example):

| Callout selected | `#infobox` height | `#controls` Y position |
|---|---|---|
| Short prompt     | 240 px (110 of content + 130 whitespace) | layout + 240 |
| Short description | 240 px (140 of content + 100 whitespace) | layout + 240 |
| Long description + ap_tip | 240 px (240 of content + 0 whitespace) | layout + 240 |

The controls are nailed in place. The iframe height is also a single
constant value, so the parent page never has to resize the iframe after
the first message arrives — there is no jump on click, no scroll bar,
no dead band below the controls.

## The Critical Constraint: DO NOT Reorder the DOM

Several pieces of this design assume the order
`#layout → #infobox → #controls → #edit-panel`. If a future template
moves `#controls` *above* `#infobox`, the pinning trick still works
(controls stay at a fixed Y), but a different problem appears: short
content leaves whitespace *below* the controls instead of above them,
which is harder to disguise visually.

The `interactive-infographic-overlay` skill enforces this DOM order in
`assets/main-template.html` and documents it in `SKILL.md` Step 5.
**Do not reorder these elements when generating new sims.**

## The Self-Correcting Resize Path

`reportHeight()` is called from two places:

1. **Once at end of `init()`** — sets the initial pin and reports the
   initial iframe height.
2. **From the `ResizeObserver` on `#layout`** — fires whenever the
   layout container resizes (parent page scrolls a sidebar, browser
   window resizes, mobile orientation flip, etc.).

On the second and subsequent calls, the existing pin from the previous
call would lock the measurement to a stale value. To prevent this,
**the very first thing `reportHeight()` does after the safety guards is
clear the pin**:

```js
if (infoboxEl) infoboxEl.style.minHeight = '';
```

Without that line, narrowing the browser would never re-measure the
worst-case (since the old pin would force the infobox to its old height),
and the iframe would slowly drift out of sync with the actual content
needs as the viewport changes.

**If you ever see the iframe height failing to recompute after a window
resize, the first thing to check is whether that `style.minHeight = ''`
line is still being executed before the new measurement.**

## What Each Number Means

- `+ 30` in `document.body.scrollHeight + 30` — small breathing room for
  the iframe border and a 1–2px scrollbar fudge factor. Don't reduce
  it below ~10; some browsers undercount `scrollHeight` by a pixel or
  two on subpixel layouts and you get a scrollbar.
- `infoboxEl.offsetHeight` (not `clientHeight`) — `offsetHeight`
  includes padding and border, which is what we want because the
  infobox has its own border in the shared `style.css`. Using
  `clientHeight` here would underestimate by the border width and
  let the infobox shrink by 2 px on restore.

## Failure Modes and How to Recognize Them

| Symptom | Likely cause |
|---|---|
| Dead space below `#controls` after first load | `reportHeight()` measured a longer worst-case than is actually possible. Check that no callout has stale `description` text from an earlier draft. |
| Iframe scrollbar appears when clicking certain callouts | A callout's content exceeds the worst-case `offsetHeight`. Likely cause: a description contains long unbreakable strings (URLs, code) that wrap differently than the longest one chosen by `description.length`. |
| Controls visibly jump when switching modes | Mode switch is calling `setMode()` which calls `resetInfobox()` which can collapse content. The pin should hold; if it doesn't, check whether something is clearing `infoboxEl.style.minHeight` outside of `reportHeight()`. |
| Iframe never resizes after window resize | The `style.minHeight = ''` clearing line was removed or moved after the measurement. Restore it as the first action inside the data-present branch. |
| Iframe height is off by ~20 px | The DOM order has been changed (probably `#controls` moved above `#infobox`), and `body.scrollHeight` is now slightly different from what the measurement assumed. Restore the canonical order. |

## Future Escape Hatch: A `data.json` Override Field

If a particular sim hits a case the auto-measurement cannot handle —
e.g., an interactive element that legitimately needs more vertical room
than any callout's description, or a custom annotation layer added to
`main.html` that breaks the worst-case assumption — the right fix is
**not** to remove the pinning logic. The right fix is to add an
override field to `data.json` and have `reportHeight()` honor it.

The recommended shape (not yet implemented):

```json
{
  "title": "...",
  "iframeHeight": 720,
  ...
}
```

When `data.iframeHeight` is a positive number, `reportHeight()` should
**skip** both the worst-case measurement and the infobox pinning, and
post that exact pixel value as the iframe height. The infobox would
fall back to its natural CSS `min-height` (set in `style.css`), which
means the controls *might* shift slightly on callout changes — but the
sim author has explicitly opted into manual sizing and accepted that
trade-off.

Suggested implementation when needed (sketch only):

```js
reportHeight() {
  if (window.self === window.top) return;

  // Manual override path — sim author has set an explicit iframe height.
  if (this.data && typeof this.data.iframeHeight === 'number'
                && this.data.iframeHeight > 0) {
    window.parent.postMessage(
      { type: 'microsim-resize', height: this.data.iframeHeight },
      '*'
    );
    return;
  }

  // ... existing worst-case measurement and pinning logic ...
}
```

The escape hatch should be **last-resort**. Before adding it to a sim,
verify that the auto-measurement actually fails. The auto path is
preferable because it adapts to viewport changes, font-size changes, and
content edits without requiring the sim author to recompute a magic
number.

If you do implement the escape hatch, document it in
`references/data-json-schema.md` alongside the existing top-level
fields.

## Quick Reference: The Three Lines That Matter

```js
// 1. Clear any previous pin so the new measurement is fresh.
if (infoboxEl) infoboxEl.style.minHeight = '';

// 2. (After filling infobox with longest content)
//    Pin the infobox to its worst-case height.
infoboxEl.style.minHeight = infoboxEl.offsetHeight + 'px';

// 3. Measure the body and post.
const height = document.body.scrollHeight + 30;
window.parent.postMessage({ type: 'microsim-resize', height }, '*');
```

If something is broken with iframe sizing in a diagram-overlay sim, look
at these three lines first. If they are intact and in this order, the
bug is somewhere else (DOM order, CSS specificity, the `extra.js` parent
listener, or a callout description containing markup that breaks
`scrollHeight`).
