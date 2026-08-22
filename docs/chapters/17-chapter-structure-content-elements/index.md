---
title: Chapter Structure and Content Elements
description: Covers the book-chapter-generator and chapter-content-generator workflows, the two rules that keep a book honest, admonitions, and MathJax equation support.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 16:05:00
version: 0.09
---

# Chapter Structure and Content Elements

## Summary

This chapter introduces the book-chapter-generator workflow -- assigning concepts to chapters so each is covered exactly once in dependency order -- and the markdown content elements available inside a chapter, including admonitions and MathJax-rendered equations. Students will be able to design a dependency-respecting chapter outline for a small learning graph after this chapter.

## Concepts Covered

This chapter covers the following 17 concepts from the learning graph:

1. Admonition Blocks
2. Math Equation Support
3. Note and Tip Admonitions
4. Question Admonition
5. Details Disclosure Block
6. MathJax Configuration
7. LaTeX Equation Syntax
8. Equation Numbering
9. Book Chapter Generator
10. Chapter Structure Design
11. Chapter Concept Assignment
12. Chapter Index File
13. Concept Coverage Exactly Once
14. Dependency-Ordered Chapters
15. Chapter Summary
16. Chapter Concept List
17. Chapter Content Generator

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [4. Development Tools: Editor, Terminal, and Git Basics](../04-dev-tools-editor-git-basics/index.md)
- [6. Agent Skill Fundamentals](../06-agent-skill-fundamentals/index.md)
- [14. Learning Graphs and Concept Enumeration](../14-learning-graphs-concept-enumeration/index.md)

---

!!! mascot-welcome "How a graph becomes a book."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    You've spent three chapters inside the learning graph. This one shows exactly how that graph turned into the 31 chapters you're reading — this one included. Right tool, right task!

## From Graph to Chapters: The Book Chapter Generator

The **Book Chapter Generator** is the skill that designs a chapter outline from a dependency structure, assigning ideas to chapters in an order that respects prerequisites — the exact skill that produced this book's own table of contents from its 570-concept graph. Doing that well is **chapter structure design**: determining how many chapters a book needs and which material belongs in each, guided by the ordering relationships between ideas rather than an arbitrary target count. The actual placement step is **chapter concept assignment**: allocating each teachable idea to the single chapter responsible for introducing it.

## Two Rules That Keep a Book Honest

Two rules govern every valid chapter assignment. **Concept coverage exactly once** is the rule that every enumerated idea is introduced in one chapter and only one, preventing both gaps and duplication. **Dependency-ordered chapters** means sequencing chapters so no chapter relies on material introduced only in a later chapter — exactly what every "Prerequisites" section you've read so far in this book has been proving, chapter by chapter.

!!! mascot-thinking "570 concepts, zero violations, one pass each."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Both rules together mean a valid chapter structure is really a topological sort of the graph, cut into readable pieces. This book's own structure was checked against exactly this pair of rules — every one of its 570 concepts appears in exactly one chapter, and every dependency edge points from a later chapter back to an earlier or equal one.

#### Diagram: Chapter Organization Workflow

<iframe src="../../sims/chapter-organization-workflow/main.html" width="100%" height="480px" scrolling="no"></iframe>

<details markdown="1">
<summary>Chapter Organization Workflow (reused MicroSim)</summary>
Type: workflow
**sim-id:** chapter-organization-workflow<br/>
**Library:** Mermaid<br/>
**Status:** Reused<br/>
**Source:** docs/sims/chapter-organization-workflow

Reused from this book's own MicroSim catalog. Learning objective: Trace the decisions the Book Chapter Generator makes when organizing content into a dependency-ordered chapter.
</details>

## Anatomy of a Chapter Index File

Every chapter in this book lives in a **chapter index file**: the main markdown file for a chapter, holding its title, summary, assigned ideas, and eventually its full text — the same file structure you've now seen 17 times over. It opens with a **chapter summary**: a brief statement of what the chapter covers, used for navigation, previews, and generation context, followed by a **chapter concept list**: the enumerated ideas that specific chapter is responsible for introducing, numbered exactly as you've seen at the top of this one.

## From Outline to Full Text: The Chapter Content Generator

A chapter index file with just a title, summary, and concept list is a skeleton, not a chapter. The **Chapter Content Generator** is the skill that expands a chapter outline into full instructional text with examples, diagrams, and exercises at appropriate cognitive levels.

!!! mascot-tip "You're reading its output right now."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Every paragraph, admonition, and diagram spec in this chapter — including this exact tip — was produced by the Chapter Content Generator skill, working from nothing more than this chapter's original title, summary, and 17-item concept list. That's the whole pipeline, demonstrated on itself.

## Admonitions: Note, Tip, and Question Callouts

The building blocks that break up plain prose are **admonition blocks**: set-apart callout boxes that highlight notes, warnings, tips, or questions distinctly from body text — the same family of boxes Kit's own admonitions belong to, alongside plainer variants. **Note and tip admonitions** are callout variants used for supplementary information and practical advice respectively, while a **question admonition** poses a question to the reader, often with a concealed answer. That concealment is handled by a **details disclosure block**: a collapsible region that hides supporting material until a reader expands it, keeping a page readable while retaining depth.

??? question "What rule guarantees every concept appears in exactly one chapter? — Click to expand"
    Concept Coverage Exactly Once.

## Typesetting Math: MathJax and LaTeX

Some concepts are best expressed as equations rather than prose. **Math equation support** is site configuration that renders mathematical notation from source markup into properly typeset formulas, enabled through **MathJax configuration**: the settings that enable and control that typesetting on a generated site. The source markup itself is written in **LaTeX equation syntax**: the notation used to express mathematical expressions in plain text for later typesetting.

!!! mascot-warning "Use backslash delimiters, never dollar signs."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    This project's MathJax configuration expects `\( \)` for inline math and `\[ \]` for display math — not `$` or `$$`. Mixing in dollar-sign delimiters from a different project's conventions will render as literal text instead of a formula.

An inline example: the marginal token cost from Chapter 9 can be written as \( c_{marginal} = \frac{C_{total} - C_{fixed}}{n} \), where \(n\) is the number of terms. As a display equation with **equation numbering** — assigning identifiers to displayed formulas so they can be referenced from surrounding text — the same relationship reads:

\[
c_{marginal} = \frac{C_{total} - C_{fixed}}{n} \tag{1}
\]

Equation (1) is exactly the calculation behind Chapter 9's glossary token benchmark.

## Key Takeaways

- The **Book Chapter Generator** performs **chapter structure design** and **chapter concept assignment**, producing chapters that obey **concept coverage exactly once** and **dependency ordering**.
- A **chapter index file** holds a **chapter summary** and **chapter concept list**; the **Chapter Content Generator** expands that skeleton into full text — like this chapter itself.
- **Admonition blocks**, including **note**, **tip**, and **question** variants, plus **details disclosure blocks**, break up prose without hiding depth.
- **Math equation support**, via **MathJax configuration** and **LaTeX syntax**, renders formulas; use backslash delimiters and **equation numbering** to reference them from surrounding text.

!!! mascot-celebration "You just watched this book explain how it was built."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Every rule in this chapter was demonstrated by the chapter itself — coverage, ordering, admonitions, even the equation. That's as close to a live demo as a book gets. Right tool, right task!
