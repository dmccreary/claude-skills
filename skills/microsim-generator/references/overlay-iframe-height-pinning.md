# Callout Overlay Iframe Height — Runtime Contract

**Audience:** contributors changing `reportHeight()` in
`assets/infographic-overlay/shared-libs/diagram.js`, the callout template, or
the parent-page resize listener. This file describes the active implementation.

The filename is retained for compatibility with existing links. The active
runtime does **not** pin the infobox with an inline minimum height.

## The Problem

A callout overlay has variable-height content: the prompt, short descriptions,
and long descriptions with tips all occupy different amounts of space. The
parent page embeds the overlay in an iframe, so it needs one height that avoids
both clipped content and a page jump whenever the learner selects a callout.

Two naive strategies fail:

1. Measuring only the initial prompt can make the iframe too short for a later
   callout and introduce an inner scrollbar.
2. Measuring after every callout selection makes the surrounding textbook page
   move while the learner is interacting with it.

## The Active Contract

The callout template has one canonical top-level order:

`#layout → #controls → #infobox → #edit-panel`

- `#layout` contains the image, markers, leader lines, and label panels.
- `#controls` contains Explore and Quiz mode controls.
- `#infobox` contains the prompt or selected callout content.
- `#edit-panel` is hidden outside edit mode.

The controls deliberately come **before** the variable-height infobox. Their
vertical position therefore depends on the layout, not on whichever callout is
visible. Shorter content may leave unused space at the bottom of the allocated
iframe, after the infobox; it does not create a moving gap between the diagram
and its controls.

The authoritative template is
`assets/infographic-overlay/main-template.html`. The matching generation rule
is in `infographic-overlay-guide.md` under **Controls Placement**.

## How `reportHeight()` Works

When data is available, `reportHeight()`:

1. Saves the current prompt, label, description, tip, and display states.
2. Chooses the callout with the largest
   `description.length + tip.length` value.
3. Temporarily renders that callout in the infobox.
4. Reads the worst-case body height as
   `document.body.scrollHeight + 30`.
5. Restores the original infobox state.
6. Posts `{ type: 'microsim-resize', height }` to the parent page.

The parent listener matches the message source to its iframe and applies the
reported height. The result is one worst-case body height for the current
responsive layout. Selecting a callout does not trigger another height report,
so the parent page stays still during interaction.

If callout data or the infobox is unavailable, the method reports the current
body height plus the same 30-pixel allowance instead of attempting the
worst-case substitution.

## Responsive Recalculation

The method runs at the end of initialization and from a `ResizeObserver` on
`#layout`. A viewport change can alter image dimensions, label wrapping, and
the space available to the infobox. The observer causes a fresh worst-case
measurement for that responsive layout without tying recalculation to learner
clicks.

Do not move the observer to `#infobox`. Temporarily rendering the longest
callout would then observe its own measurement mutation and could create a
feedback loop.

## Why There Is No Infobox Pin

The active runtime never assigns an inline minimum height to `#infobox`.
It does not need one to keep controls stationary because `#controls` precedes
the infobox in document flow. The parent iframe retains the reported worst-case
height after the infobox state is restored.

An older archived reference described a different order with controls below the
infobox and proposed pinning the infobox to prevent those controls from moving.
That description was salvaged from a stale standalone-skill copy during
consolidation; it does not describe `diagram.js` or the active template.

## What the 30 Pixels Mean

`document.body.scrollHeight + 30` adds breathing room for the iframe boundary
and small browser rounding differences. It is part of the current runtime
contract, not a substitute for measuring representative content.

## Known Limitation

The runtime uses source-text length to choose the likely tallest callout. Text
length is a practical heuristic, not a layout proof: a shorter string with an
unbreakable URL or long code token can wrap taller than a longer sentence. Keep
callout prose naturally breakable. If a specific overlay still clips, reproduce
the actual rendered widths before changing the shared algorithm.

## Failure Modes

| Symptom | Check |
|---|---|
| Controls move when a callout changes | Confirm the top-level order is `#layout → #controls → #infobox → #edit-panel`; no generated page should put controls after the infobox. |
| A long callout creates an inner scrollbar | Check for unbreakable strings and verify the longest rendered callout was represented by the length heuristic. |
| The parent iframe never resizes | Confirm the overlay is embedded, `reportHeight()` runs, and the parent page has the `microsim-resize` message listener. |
| The iframe is wrong after a viewport change | Confirm the `ResizeObserver` still observes `#layout` and invokes `reportHeight()`. |
| There is space below short content | This is the expected tradeoff of allocating the worst-case body height once so the page does not jump during interaction. |

## Change Checklist

Before changing iframe-height behavior:

1. Preserve the canonical DOM order unless a separately reviewed design
   replaces the full interaction contract.
2. Test both a short and a deliberately long callout.
3. Verify that the controls' top coordinate does not change after selection.
4. Verify no inner vertical scrollbar appears for the longest callout.
5. Resize to desktop and mobile widths and confirm a fresh height is reported.
6. Update the template, runtime, guide, this reference, and contract tests as
   one change when the contract intentionally changes.

The repository fixture at
`tests/fixtures/callout-overlay/` contains short and long callouts for this
verification.
