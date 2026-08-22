---
title: Session Logs and Book Metrics
description: Covers session logging and design decision records, reading-level and skill-usage measurement, and book-metrics.json as the single canonical hub every publishing skill reads.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 19:20:00
version: 0.09
---

# Session Logs and Book Metrics

## Summary

This chapter covers writing session logs and design decision records that document why a MicroSim or feature was built the way it was, plus the skill usage report and reading-level analysis that accompany them. It introduces `book-metrics.json` as the single canonical hub of book statistics -- word count, equation count, chapter metrics -- that every publishing skill reads. Students will be able to generate and interpret a book's canonical metrics file after this chapter.

## Concepts Covered

This chapter covers the following 15 concepts from the learning graph:

1. Session Logging
2. Session Log Format
3. Design Decision Record
4. analyze-reading-levels.py
5. Skill Usage Report
6. Book Metrics
7. book-metrics.json Hub
8. Word Count Metric
9. Equation Count
10. Chapter Metrics Report
11. Site Metrics Collection
12. Book Status Report
13. Book Publisher Skill
14. Canonical Metrics Principle
15. Equivalent Page Count

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [5. MkDocs Site Features, Deployment, and Analytics](../05-mkdocs-deployment-analytics/index.md)
- [7. Progressive Disclosure and Meta-Skill Routing](../07-progressive-disclosure-meta-skills/index.md)
- [9. Measuring and Optimizing Token Usage](../09-measuring-optimizing-tokens/index.md)
- [10. Building and Testing Portable Skills](../10-building-testing-portable-skills/index.md)
- [13. Bloom's Taxonomy and Instructional Design](../13-blooms-taxonomy-instructional-design/index.md)
- [17. Chapter Structure and Content Elements](../17-chapter-structure-content-elements/index.md)
- [18. Chapter Content Quality and Review](../18-chapter-content-quality-review/index.md)

---

!!! mascot-welcome "One chapter left after this — let's measure what you've built."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    You're two chapters from the end of this book. This one is about proving, in numbers, exactly how much you've actually built. Right tool, right task!

## Recording a Working Session

**Session logging** means recording what was produced during a working session and the decisions that shaped it, following a consistent **session log format**: the agreed structure of a working record, covering the request, the choices made, the revisions applied, and the result. Inside that log, a **design decision record** is a written account of why a particular approach was chosen over alternatives, preserved so the reasoning survives long after the session that made the choice has ended.

!!! mascot-thinking "The log isn't for today's you. It's for six-months-from-now you."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A design decision that felt obvious while you were making it will not feel obvious when you revisit the same MicroSim a year later wondering "why is this canvas 620 pixels tall specifically?" A design decision record answers that question without making you reconstruct the reasoning from scratch.

## Measuring What a Skill Cost

Two measurement scripts close the loop on quality and cost across a whole book. **analyze-reading-levels.py** measures textual difficulty per chapter and reports variation across the book, the automated version of Chapter 13's Flesch-Kincaid check applied to every chapter at once instead of one at a time. A **skill usage report** is a generated summary showing which skills ran, how long they took, and what they consumed — the human-readable output built from the JSONL usage logs and hooks you met back in Chapter 9.

## Book Metrics: One Hub, Many Numbers

Every number a finished book publishes about itself needs to come from somewhere consistent. **Book metrics** are quantitative measurements describing a finished book, such as its word count, illustration count, and equivalent page count, collected into the **book-metrics.json hub**: the generated file holding a book's measurements in structured form, serving as the single source every publishing route reads.

!!! mascot-warning "Two different announcements citing two different word counts is a real failure."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Without a single source of truth, a README might say "50,000 words" while a LinkedIn post says "62,000 words" for the same book, because each was generated separately and drifted. The **canonical metrics principle** — the rule that all published figures derive from one generated measurement file, so different announcements never disagree — exists specifically to prevent that embarrassment.

## What Gets Measured

Several specific numbers live inside that hub. The **word count metric** is the total quantity of written text in a book, used as a basic measure of scale. The **equation count** is the number of mathematical expressions in a book, indicating how quantitative the material is — Chapter 17's LaTeX equations each add to this number. A **chapter metrics report** is a generated table of measurements per chapter, used to identify uneven depth across a book, the same per-chapter comparison from Chapter 18 applied at the scale of an entire finished book. For a reader trying to gauge scale intuitively, an **equivalent page count** estimates how many printed pages a book's content would occupy — "570 concepts" means little to a new reader, but "roughly 300 printed pages" gives them an immediate sense of size.

## Site-Wide Numbers and Status

Beyond the text itself, **site metrics collection** gathers counts of published pages, simulations, and assets from a built site — how many MicroSims this book actually shipped, not just how many words it contains. All of it rolls up into a **book status report**: a generated overview of how complete a book is and which stages of its production remain, the read-only progress check from Chapter 11's `ibook` runbook, expressed as numbers instead of a next-step recommendation.

## The Book Publisher Meta-Skill

All of these measurements exist to feed one final consumer. The **Book Publisher Skill** is the meta-skill that produces repository summaries, announcement posts, slideshows, and press releases from a book's recorded measurements — every one of those outputs reading from the same `book-metrics.json` hub, guaranteeing the canonical metrics principle holds all the way to publication.

!!! mascot-tip "Generate the metrics file once, then let every announcement read it."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Never hand-type a book's word count into a README or a LinkedIn post. Regenerate `book-metrics.json` and let the publishing skills pull from it — that's the only way the canonical metrics principle actually holds in practice, not just in theory.

## Key Takeaways

- **Session logging**, in a consistent **session log format**, preserves **design decision records** so reasoning survives past the session that made it.
- **analyze-reading-levels.py** and a **skill usage report** measure quality and cost across a whole book, not just one chapter.
- **Book metrics**, collected into the **book-metrics.json hub**, follow the **canonical metrics principle**: one source, no disagreeing numbers.
- **Word count**, **equation count**, a **chapter metrics report**, and **equivalent page count** describe a book's scale; **site metrics collection** and a **book status report** describe its completeness.
- The **Book Publisher Skill** turns all of it into README summaries, announcements, and press releases — all reading from the same hub.

!!! mascot-celebration "You can now prove exactly how much book you've built."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Every number in this book's own announcements, if it ever publishes them, will trace back to exactly the pipeline you just learned. One chapter left — let's finish the job. Right tool, right task!
