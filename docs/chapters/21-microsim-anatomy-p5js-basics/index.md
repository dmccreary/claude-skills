---
title: MicroSim Anatomy and p5.js Basics
description: Introduces the standard MicroSim directory structure and file separation principle, the p5.js setup and draw functions, and iframe embedding with a fullscreen button.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 17:05:00
version: 0.09
---

# MicroSim Anatomy and p5.js Basics

## Summary

This chapter introduces the standard MicroSim directory structure and the file separation principle across `main.html`, `style.css`, `script.js`, `data.json`, and `metadata.json`. It then builds a first interactive simulation with the p5.js library, covering the setup function, the draw loop, and canvas container sizing. Students will be able to scaffold a MicroSim directory and write a basic p5.js sketch after this chapter.

## Concepts Covered

This chapter covers the following 19 concepts from the learning graph:

1. MicroSim
2. MicroSim Directory Structure
3. MicroSim Screen Capture
4. main.html File
5. style.css File
6. script.js File
7. data.json File
8. MicroSim metadata.json
9. MicroSim index.md File
10. File Separation Principle
11. p5.js Library
12. Iframe Embedding
13. MicroSim Index Catalog
14. Inline Code Antipattern
15. p5.js Setup Function
16. p5.js Built-In Controls
17. Fullscreen Sim Button
18. p5.js Draw Loop
19. Canvas Container Sizing

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)

---

!!! mascot-welcome "Every diagram you've clicked so far started here."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    You've interacted with a dozen MicroSims already in this book. This chapter opens one up and shows you exactly how it's built. Right tool, right task!

## What Is a MicroSim?

A **MicroSim** is a small, self-contained interactive simulation embedded in a textbook page, focused on demonstrating one idea — not a general-purpose app, but a narrow, purpose-built widget like the graph viewer from Chapter 14 or the tokenization visualizer from Chapter 1.

## The Standard Directory: Five Separate Files

Every MicroSim in this book follows the same **MicroSim directory structure**: the standard folder holding a simulation's markup, styling, logic, data, metadata, and documentation page as separate files. That separation is deliberate — the **file separation principle** states that structure, presentation, behavior, and data each live in their own file, improving maintainability and caching. Concretely: the **main.html file** defines a simulation's structure and loads its stylesheet, logic, and external libraries; the **style.css file** holds all of a simulation's presentation rules, kept separate from structure and behavior; the **script.js file** holds all of a simulation's behavior, including event handling and rendering logic; a **data.json file** holds a simulation's underlying values separately from its code, so figures can be updated without touching logic; **MicroSim metadata.json** is the structured descriptive record covering authorship, discovery keywords, educational targeting, and technical requirements; and the **MicroSim index.md file** is the documentation page, embedding the simulation in a frame and providing a full-screen link and explanatory text.

#### Diagram: MicroSim File Relationship

<iframe src="../../sims/microsim-file-relationship-diagram/main.html" width="100%" height="500px" scrolling="no"></iframe>

<details markdown="1">
<summary>MicroSim File Relationship Diagram (reused MicroSim)</summary>
Type: diagram
**sim-id:** microsim-file-relationship-diagram<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/microsim-file-relationship-diagram

Reused from this book's own MicroSim catalog. Learning objective: Identify how a MicroSim's index.md, main.html, and metadata.json files relate to each other and to the surrounding MkDocs site.
</details>

!!! mascot-warning "A prototype's shortcuts don't belong in a shipped MicroSim."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    The **inline code antipattern** — embedding styling or logic directly inside a markup file — is acceptable for a five-minute prototype, but it obstructs later maintenance the moment more than one person touches the file. Split it into `style.css` and `script.js` before it goes into a chapter.

## The p5.js Library

Most MicroSims in this book are built with the **p5.js library**: a JavaScript library for drawing and animation that provides a canvas, a render loop, and simple interface controls. Two functions carry almost all of a sketch's behavior. The **p5.js setup function** is the routine that runs once at start to create the canvas and build interface controls. The **p5.js draw loop** is the routine that runs repeatedly to render each frame, producing animation and responding to changing values.

!!! mascot-thinking "Once, then forever — that's the whole mental model."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    `setup()` runs exactly once; `draw()` runs continuously, roughly sixty times a second. Every MicroSim you've clicked in this book follows that same split — one-time setup, then a loop that reacts to whatever changed since the last frame.

Getting the canvas the right size for its surrounding page is **canvas container sizing**: measuring the available width of a surrounding element and sizing the drawing surface to match, so a simulation fits its frame rather than overflowing or leaving empty space — the `updateCanvasSize()` call every MicroSim in this project runs as the first line of `setup()`.

#### Diagram: Basic MicroSim Template Structure

<iframe src="../../sims/basic-microsim-template-structure/main.html" width="100%" height="500px" scrolling="no"></iframe>

<details markdown="1">
<summary>Basic MicroSim Template Structure (reused MicroSim)</summary>
Type: diagram
**sim-id:** basic-microsim-template-structure<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/basic-microsim-template-structure

Reused from this book's own MicroSim catalog. Learning objective: Identify where `setup()`, `draw()`, and the canvas container sit inside a MicroSim's `main.html` document structure.
</details>

## Controls, Not Hand-Drawn Substitutes

When a sketch needs a slider or a button, p5.js already provides one. **p5.js built-in controls** are the interface elements the drawing library supplies directly, used instead of hand-drawn substitutes so behavior stays consistent and accessible.

!!! mascot-tip "Never draw your own slider by hand."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    A hand-drawn rectangle that moves when clicked *looks* like a slider but won't respond to keyboard input or a screen reader. `createSlider()` gives you both for free. This project's global convention is strict about this for exactly that reason.

## Embedding and Discovering MicroSims

A finished MicroSim reaches a reader through **iframe embedding**: placing a self-contained page inside a documentation page so a simulation runs inline without navigating away — exactly what every `<iframe src="../../sims/{sim-id}/main.html">` in this book has been doing. Right beside that iframe sits a **fullscreen sim button**: a link that opens a simulation in its own tab at full size for closer inspection, useful when a reader wants more room than an embedded frame allows. Across an entire book, every simulation is listed in a **MicroSim index catalog**: a generated listing of every simulation with preview images and links, and each preview image comes from **MicroSim screen capture**: producing a still image of a running simulation for use as that catalog preview.

## Key Takeaways

- A **MicroSim** is a small, focused interactive simulation, organized by the **file separation principle** into a standard **directory structure**: **main.html**, **style.css**, **script.js**, **data.json**, **metadata.json**, and an **index.md** — never the **inline code antipattern**.
- The **p5.js library**'s **setup function** runs once; its **draw loop** runs continuously; **canvas container sizing** keeps the result fitting its frame.
- **p5.js built-in controls** replace hand-drawn substitutes, keeping interaction accessible.
- **Iframe embedding** and a **fullscreen sim button** get a MicroSim in front of a reader; a **MicroSim index catalog**, built from **screen capture** previews, helps readers find it.

!!! mascot-celebration "You could scaffold a MicroSim directory right now."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Five files, one setup call, one draw loop, one iframe — that's the entire anatomy behind every interactive diagram you've touched in this book. Right tool, right task!
