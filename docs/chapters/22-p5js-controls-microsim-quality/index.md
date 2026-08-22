---
title: p5.js Controls and MicroSim Quality
description: Covers the five built-in p5.js controls, CANVAS_HEIGHT and iframe height synchronization, responsive and accessible layout, and the automated batch tools that score MicroSim quality.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 17:20:00
version: 0.09
---

# p5.js Controls and MicroSim Quality

## Summary

This chapter covers the built-in p5.js control widgets -- sliders, buttons, checkboxes, dropdowns, and text inputs -- along with responsive iframe embedding and the fullscreen sim button. It closes with MicroSim standardization, accessible color schemes, and the quality-scoring checks every simulation must pass before publication. Students will be able to add interactive controls to a p5.js MicroSim and evaluate its quality score after this chapter.

## Concepts Covered

This chapter covers the following 19 concepts from the learning graph:

1. Slider Control
2. Button Control
3. Checkbox Control
4. Dropdown Select Control
5. Text Input Control
6. MicroSim Quality Score
7. Celebration Animation
8. CANVAS_HEIGHT Directive
9. Responsive Sim Layout
10. MicroSim Standardization
11. Visual Layout Review
12. Iframe Height Synchronization
13. Accessible Color Schemes
14. Font Size for Readability
15. Iframe Control Visibility
16. add-iframes-to-chapter.py
17. validate-sims.py Script
18. calculate-quality-score.py
19. generate-sims-index.py

## Prerequisites

This chapter builds on concepts from:

- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [7. Progressive Disclosure and Meta-Skill Routing](../07-progressive-disclosure-meta-skills/index.md)
- [21. MicroSim Anatomy and p5.js Basics](../21-microsim-anatomy-p5js-basics/index.md)

---

!!! mascot-welcome "From working to trustworthy."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Chapter 21 got a MicroSim running. This chapter makes it accessible, correctly sized, and provably good enough to publish. Right tool, right task!

## The Five Built-In Controls

Chapter 21 introduced p5.js's built-in controls as a category; here are the five you'll reach for most. A **slider control** is a draggable interface element for selecting a value from a continuous range, used for parameters such as speed or size. A **button control** is a clickable element that triggers a discrete action such as resetting or starting a simulation. A **checkbox control** toggles a setting between two states, used for optional display features. A **dropdown select control** presents a list of options from which one is chosen, used for selecting modes or datasets. A **text input control** accepts typed values, used where a reader supplies a number or short string.

| Control | p5.js Function | Used For |
|---------|-----------------|----------|
| Slider | `createSlider()` | Continuous parameters (speed, size) |
| Button | `createButton()` | Actions (reset, start, randomize) |
| Checkbox | `createCheckbox()` | On/off toggles |
| Dropdown | `createSelect()` | Choosing a mode or dataset |
| Text input | `createInput()` | Short numeric or text values |

## CANVAS_HEIGHT and Iframe Height Synchronization

An embedded MicroSim needs its surrounding frame sized correctly, and that height shouldn't be guessed in two places. The **CANVAS_HEIGHT directive** is a recorded height value inside a simulation's source that serves as the single authority for how tall its embedding frame should be — you've seen the `// CANVAS_HEIGHT: 500` comment convention throughout this book's own MicroSims. **Iframe height synchronization** propagates that recorded value into every place the simulation is embedded, so frames neither clip content nor leave blank space. The program that does this work automatically is **add-iframes-to-chapter.py**: inserting the actual embedding markup for a generated simulation into the chapter that requested it.

!!! mascot-tip "One number, read everywhere."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Never hand-edit an iframe's `height` attribute to fix a clipping problem. Fix the `CANVAS_HEIGHT` comment in the simulation's own source instead, and let synchronization propagate the corrected value everywhere that simulation is embedded.

#### Diagram: MicroSim Design Quality Checklist

<iframe src="../../sims/microsim-design-quality-checklist/main.html" width="100%" height="480px" scrolling="no"></iframe>

<details markdown="1">
<summary>MicroSim Design Quality Checklist (reused MicroSim)</summary>
Type: infographic
**sim-id:** microsim-design-quality-checklist<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/microsim-design-quality-checklist

Reused from this book's own MicroSim catalog. Learning objective: Evaluate a MicroSim against the checklist items that later feed its automated quality score.
</details>

## Responsive Layout and Accessibility

A MicroSim has to work at whatever width its frame actually gets. **Responsive sim layout** means designing a simulation so it adapts to the width available, remaining usable on narrow screens and inside frames of different sizes. Readability depends on two more choices: **accessible color schemes** — color selections that remain distinguishable to readers with color vision differences and maintain sufficient contrast — and **font size for readability**: text sizing chosen so labels remain legible even when a simulation is displayed in a reduced frame. Finally, **iframe control visibility** confirms that a simulation's interface elements remain reachable when displayed at the frame height a page actually assigns, not just at the height it was designed and tested at.

!!! mascot-warning "Color alone is not a label."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A MicroSim that distinguishes categories by color alone excludes readers with color vision differences. Always pair color with a second cue — a shape, a pattern, or a text label — so the distinction survives even if the color doesn't come through.

## Automated Batch Tools: Validate, Score, Index

Checking every MicroSim in a book by hand doesn't scale, so three scripts do it instead. **validate-sims.py** checks simulations against structural standards and reports violations. **calculate-quality-score.py** computes a numeric rating for a simulation from measurable properties, producing the **MicroSim quality score**: a computed rating of a simulation against structural and presentation standards — the same `quality_score` field you've seen in nearly every reused MicroSim's frontmatter throughout this book. **generate-sims-index.py** builds the catalog page listing every simulation with its preview image, the automated counterpart to the manual MicroSim index catalog from Chapter 21.

## Standardization and Visual Review

Not every MicroSim in a growing library was built to today's conventions. **MicroSim standardization** means bringing existing simulations into conformance with the current file layout, control, and metadata conventions, so an older sim doesn't quietly fall out of step with a book's newer ones.

!!! mascot-thinking "A library only stays consistent if you re-check it."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Standards drift is easy to miss one simulation at a time but adds up across hundreds. This book's own catalog — the same one you searched through Chapter 4 onward to find reusable MicroSims — depends on periodic standardization passes to stay trustworthy as a reuse source.

Automated checks catch structural problems; they don't catch everything a human eye would. **Visual layout review** is inspecting a rendered simulation for presentation defects such as overlapping elements, clipped labels, or controls positioned off-screen — exactly the kind of defect a script measuring pixel counts can miss but a screenshot review catches immediately.

## A Small Flourish: Celebration Animation

Not every MicroSim element needs to be a control or a warning. A **celebration animation** is a brief visual effect acknowledging completion of an activity, used to mark progress — the same instructional purpose as Kit's own `mascot-celebration` admonition, expressed as an on-canvas visual instead of a callout box.

## Key Takeaways

- The five built-in controls — **slider**, **button**, **checkbox**, **dropdown**, and **text input** — cover almost every interaction a MicroSim needs.
- The **CANVAS_HEIGHT directive** is the single source of truth for frame sizing, propagated by **iframe height synchronization** and inserted by **add-iframes-to-chapter.py**.
- **Responsive layout**, **accessible color schemes**, **readable font sizes**, and confirmed **iframe control visibility** keep a simulation usable everywhere it's embedded.
- **validate-sims.py**, **calculate-quality-score.py**, and **generate-sims-index.py** automate what would otherwise be manual checking across an entire library.
- **MicroSim standardization** and **visual layout review** catch what automated checks alone can't; a **celebration animation** is a small, optional flourish for marking progress.

!!! mascot-celebration "You can now ship a MicroSim, not just build one."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Accessible, correctly sized, automatically scored — that's the difference between a working prototype and a MicroSim ready for a reader you'll never meet. Right tool, right task!
