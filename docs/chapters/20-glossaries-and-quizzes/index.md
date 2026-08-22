---
title: Glossaries and Quizzes
description: Covers the remaining ISO 11179 definition criteria, glossary term extraction and ordering, and generating Bloom's-distributed quizzes with well-designed distractors.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 16:50:00
version: 0.09
---

# Glossaries and Quizzes

## Summary

This chapter covers writing glossary definitions that meet the ISO 11179 standard -- precise, concise, distinct, non-circular, and free of business rules -- along with glossary term ordering and anchor links. It then covers generating multiple-choice quiz questions with a Bloom's-aligned distribution, plausible distractors, and balanced answer placement. Students will be able to write an ISO 11179-compliant definition and a well-formed quiz question after this chapter.

## Concepts Covered

This chapter covers the following 17 concepts from the learning graph:

1. Concise Definition
2. Distinct Definition
3. Non-Circular Definition
4. Definitions Without Rules
5. Term Extraction
6. Glossary Quality Report
7. Glossary Term Ordering
8. Quiz
9. Quiz Generator
10. Multiple-Choice Question
11. Quiz Bloom Distribution
12. Quiz Analytics
13. Distractor Design
14. Answer Distribution Balance
15. Quiz Bank JSON
16. Distractor Plausibility
17. Quiz Explanation Text

## Prerequisites

This chapter builds on concepts from:

- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [6. Agent Skill Fundamentals](../06-agent-skill-fundamentals/index.md)
- [13. Bloom's Taxonomy and Instructional Design](../13-blooms-taxonomy-instructional-design/index.md)
- [14. Learning Graphs and Concept Enumeration](../14-learning-graphs-concept-enumeration/index.md)
- [19. FAQs and Curated References](../19-faqs-curated-references/index.md)

---

!!! mascot-welcome "Definitions, then the questions that test them."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Chapter 19 introduced the glossary and its precision requirement. This chapter finishes the ISO 11179 criteria and shows how a well-built glossary feeds directly into a well-built quiz. Right tool, right task!

## Finishing the ISO 11179 Criteria

Chapter 19 covered a precise definition; four more criteria complete the ISO 11179 standard. A **concise definition** is expressed in the fewest words that still convey the full meaning, typically twenty to fifty. A **distinct definition** clearly separates its term from related terms rather than blurring into them — this book's own entries for "Level 3 Adaptive Content" and "Level 4 Chatbot Integration" have to name what specifically each adds, or the two definitions collapse into each other. A **non-circular definition** does not rely on the term being defined, nor on another term whose own definition depends on it. **Definitions without rules** describe what something is rather than prescribing how it must be used or who may use it.

| Criterion | What It Rules Out |
|-----------|---------------------|
| Precise | Ambiguity or hedging |
| Concise | Padding, over-explanation |
| Distinct | Blurring into a related term |
| Non-circular | Defining a term using itself |
| Without rules | Procedural instructions instead of meaning |

## Building a Glossary: Extraction, Ordering, and Quality

Before any definition gets written, the vocabulary has to be identified. **Term extraction** is identifying the vocabulary requiring definition, drawn from an enumerated idea list and from wording used across the written material — the concept list from every chapter you've read is exactly this book's own term-extraction input. Once written, entries follow **glossary term ordering**: arranging entries alphabetically without regard to case, category, or topic, so any term can be located directly, regardless of which chapter introduced it.

!!! mascot-tip "Alphabetical, not by importance."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    It's tempting to group glossary entries by topic so related ideas sit near each other. Resist it — a reader searching for one specific term needs strict alphabetical order, not a curated reading experience. That's what chapter prose is for.

A **glossary quality report** is a generated assessment scoring definitions against the ISO 11179 criteria and listing entries that need revision — the same kind of automated quality gate you met for learning graphs in Chapter 16, applied to prose instead of graph structure.

#### Diagram: ISO 11179 Principles Comparison

<iframe src="../../sims/iso-11179-principles-comparison-table-infographic/main.html" width="100%" height="480px" scrolling="no"></iframe>

<details markdown="1">
<summary>ISO 11179 Principles Comparison (reused MicroSim)</summary>
Type: infographic
**sim-id:** iso-11179-principles-comparison-table-infographic<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/iso-11179-principles-comparison-table-infographic

Reused from this book's own MicroSim catalog. Learning objective: Compare the five ISO 11179 criteria side by side against example definitions that pass or fail each one.
</details>

## Quizzes: Testing More Than Recall

A **quiz** is a set of questions used to check whether a reader has grasped a chapter's material, produced by the **quiz generator**: the skill that creates chapter assessments aligned to assigned ideas and distributed across cognitive categories. Most items take the form of a **multiple-choice question**: an assessment item presenting one correct answer among several alternatives.

!!! mascot-thinking "A quiz all at the Remember level tests memory, not mastery."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Just like Chapter 13's cognitive level distribution for a whole course, **quiz Bloom distribution** — the allocation of assessment items across cognitive categories, ensuring a quiz tests more than recall — applies the same discipline at the scale of a single chapter's quiz. A quiz of ten Remember-level questions is easy to write and easy to pass without real understanding.

## Writing Good Distractors

The wrong answers matter as much as the right one. **Distractor design** is the construction of incorrect alternatives that represent genuine misunderstandings rather than obvious filler, measured by **distractor plausibility**: the degree to which an incorrect alternative could reasonably be selected by a reader holding a specific misconception. Beyond content, **answer distribution balance** spreads correct answers evenly across the available positions so position alone gives no advantage — a quiz where the correct answer is "C" nine times out of ten teaches readers to guess "C," not to know the material.

!!! mascot-warning "A distractor no one would ever pick tests nothing."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    "Which of these is a fruit: Apple, Bulldozer, Thursday, Seventeen?" has zero diagnostic value — every wrong answer is obviously wrong. A good distractor should be the answer a reader who half-understood the material would actually choose.

## Explanations and Analytics

Every well-formed item closes with **quiz explanation text**: the rationale accompanying each item that states why the correct answer is right and why each alternative is wrong — turning a quiz from a pass/fail gate into one more piece of instructional content. Aggregated across many readers, **quiz analytics** is analysis of assessment results to identify material readers consistently struggle with, feeding back into which chapters might need revision. All of a book's items together form a **quiz bank JSON**: a structured export of all assessment items across a book, usable by external systems — the same file-format thinking from Chapter 15's learning graph JSON, applied to assessments.

## Key Takeaways

- The five ISO 11179 criteria are **precise**, **concise**, **distinct**, **non-circular**, and **without rules** — Chapter 19 covered the first, this chapter the other four.
- **Term extraction** feeds a glossary; **alphabetical term ordering** and a **glossary quality report** keep it usable and accurate.
- The **quiz generator** produces **multiple-choice questions** following a **Bloom distribution**, not clustered at recall.
- **Distractor design** and **plausibility** make wrong answers diagnostic; **answer distribution balance** removes positional guessing.
- **Quiz explanation text** teaches even after the question is answered; **quiz analytics** and the **quiz bank JSON** turn many chapters' worth of items into a feedback loop.

!!! mascot-celebration "You can now write a definition and a quiz question that both hold up to scrutiny."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Five precise criteria, six cognitive levels, and distractors that actually mean something — that's the whole discipline behind every glossary entry and quiz question in this book. Right tool, right task!
