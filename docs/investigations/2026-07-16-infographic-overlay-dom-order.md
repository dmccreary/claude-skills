---
title: Infographic Overlay Guidance Contradicts the Active DOM Contract
date: 2026-07-16
status: current
severity: high
component: skills/microsim-generator/references/overlay-iframe-height-pinning.md
trello: https://trello.com/c/0ujxPalV/221-investigation-infographic-overlay-guide-contradicts-template-dom-order
---

# Infographic Overlay Guidance Contradicts the Active DOM Contract

## Symptom

The active callout template and generation guide require
`#layout → #controls → #infobox → #edit-panel`. The adjacent iframe-height
reference instead calls `#layout → #infobox → #controls → #edit-panel`
canonical and warns that the template's actual order causes bad whitespace and
height measurements.

The reference also describes pinning `#infobox` with
`style.minHeight`. The active `diagram.js` runtime never sets that property.

## Preserved evidence

- Commit `67bd669f` intentionally moved `#controls` below the image and above
  `#infobox`; its commit title and guide change both state that intent.
- `assets/infographic-overlay/main-template.html` still implements that order.
- `infographic-overlay-guide.md` still documents that order.
- `diagram.js::reportHeight()` temporarily renders the longest callout,
  measures `document.body.scrollHeight + 30`, restores the prior infobox state,
  and posts the measured height. It does not pin the infobox.
- Git history shows the contradictory reference was introduced later in
  commit `1e3206a2`, when a stale local standalone-skill reference was salvaged
  during consolidation.
- The archived standalone copy contains the same stale reference and has no
  file-local warning that it is non-authoritative.

## Initial hypotheses

| Hypothesis | Prior | Evidence | Status |
| --- | ---: | --- | --- |
| The active template accidentally drifted from the intended pinning design | 40% | Template and guide changed together intentionally in `67bd669f` | Refuted |
| The salvaged reference describes an older, unshipped runtime | 50% | It requires DOM order and `minHeight` behavior absent from active history | Confirmed |
| The current runtime needs an infobox min-height pin | 5% | Controls precede variable content and therefore do not move with it | Refuted |
| None of the listed causes | 5% | Reserved for browser evidence that contradicts source/history | Still possible |

## Root cause

Consolidation treated a stale local reference as richer documentation and
salvaged it without validating its behavioral claims against the template and
runtime that became authoritative. The guide and template preserved the March
31 controls-placement decision, while the July 10 reference reintroduced an
older incompatible design as a canonical constraint.

## Remediation

1. Keep the intentional active order:
   `#layout → #controls → #infobox → #edit-panel`.
2. Rewrite the active iframe-height reference around the runtime's actual
   worst-case-body-height measurement rather than an unimplemented infobox pin.
3. Mark the archived height reference explicitly historical and
   non-authoritative, pointing readers to the consolidated active reference.
4. Add a contract test covering template order, active guide agreement,
   runtime claims, archived status, and a representative callout fixture.
5. Load the representative fixture in a real browser and verify that controls
   remain stationary when short and long callouts are selected, the longest
   content is not clipped, and no inner scrollbar appears.

## Validation evidence

- The new static contract first failed on the three preserved defects: the
  active references disagreed, the stale reference claimed an unimplemented
  `style.minHeight` pin, and the archived copy lacked a non-authoritative
  warning. It passes after the documentation alignment.
- The complete microsim-generator Python suite passes: 21 tests.
- The existing Docker Python lab timing contract and both changed/runtime
  JavaScript syntax checks pass.
- The Playwright contract passes at 1280 x 900 and 390 x 844. At both sizes,
  switching from the short callout to the long callout changes the controls'
  top coordinate by less than 0.5 pixels, produces no inner overflow, and emits
  no page errors.
- Desktop and mobile screenshot inspection shows the image, labels, controls,
  and infobox remain readable without overlap or clipping.

## Closure criteria

- Active guide, reference, template, and runtime state one compatible design.
- Archived contradictory guidance cannot be mistaken for current authority.
- Contract coverage fails if the DOM order or height narrative drifts again.
- A representative callout overlay passes desktop and mobile browser checks.
- The fix is merged, independently read back from the target branch, and the
  reusable consolidation lesson is compounded.
