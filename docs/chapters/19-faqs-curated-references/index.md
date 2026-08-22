---
title: FAQs and Curated References
description: Covers generating a FAQ set with coverage-gap analysis and chatbot-ready export, building a curated reference list with URL verification, and generating an ISO 11179 glossary.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 16:35:00
version: 0.09
---

# FAQs and Curated References

## Summary

This chapter covers generating a FAQ set from course content, categorizing questions, and identifying coverage gaps, including the chatbot-ready JSON export used for retrieval-augmented generation. It also covers building a curated reference list that credits the authors behind influential explanations, with URL verification and a dedicated references file per chapter. Students will be able to generate a FAQ set and a curated reference list for a chapter after this chapter.

## Concepts Covered

This chapter covers the following 17 concepts from the learning graph:

1. FAQ
2. Chatbot Training JSON
3. Retrieval Augmented Generation
4. FAQ Generator
5. Reference Generator
6. FAQ Categorization
7. Curated Reference List
8. FAQ Coverage Gaps
9. Crediting Pedagogical Authors
10. URL Verification
11. Reference File Separation
12. Wikipedia as a Source
13. Glossary
14. Glossary Generator
15. ISO 11179 Standards
16. Glossary Anchor Links
17. Precise Definition

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [6. Agent Skill Fundamentals](../06-agent-skill-fundamentals/index.md)
- [8. Token Budgets and Usage Limits](../08-token-budgets-usage-limits/index.md)
- [14. Learning Graphs and Concept Enumeration](../14-learning-graphs-concept-enumeration/index.md)

---

!!! mascot-welcome "Now for the material that supports every chapter."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Chapters teach concepts in order. FAQs, references, and a glossary let a reader jump straight to the one thing they're stuck on. This chapter covers all three. Right tool, right task!

## Generating a FAQ Set

A **FAQ** is a collection of common questions with answers, organized to address the difficulties readers most often encounter. The **FAQ generator** is the skill that derives those questions and answers from course material, the idea structure, and defined vocabulary — not invented from scratch, but drawn from the same learning graph and glossary you've already met. Once generated, **FAQ categorization** groups questions by subject and difficulty so a reader can locate the relevant area quickly, rather than scrolling through an undifferentiated list.

!!! mascot-thinking "A good FAQ set proves what it's missing, not just what it covers."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    **FAQ coverage gaps** are areas of a course for which no question exists, identified by comparing questions against the enumerated ideas. The valuable output of that comparison isn't the FAQ itself — it's the gap list, which tells you exactly which concepts still need a question written for them.

#### Diagram: FAQ Question Pattern Analysis

<iframe src="../../sims/faq-pattern-analysis/main.html" width="100%" height="480px" scrolling="no"></iframe>

<details markdown="1">
<summary>FAQ Question Pattern Analysis (reused MicroSim)</summary>
Type: workflow
**sim-id:** faq-pattern-analysis<br/>
**Library:** Mermaid<br/>
**Status:** Reused<br/>
**Source:** docs/sims/faq-pattern-analysis

Reused from this book's own MicroSim catalog. Learning objective: Analyze how FAQ categorization and coverage-gap comparison work together to reveal what a FAQ set is still missing.
</details>

## From FAQ to Chatbot: Retrieval Augmented Generation

A FAQ set written for a human reader can double as training material for a chatbot. **Chatbot training JSON** is a structured export of question-and-answer pairs formatted for consumption by a conversational retrieval system, feeding into **retrieval augmented generation**: a technique in which relevant stored passages are retrieved and supplied to a model so its answers are grounded in specific source material — the same grounding discipline from Chapter 2, applied to a live question-answering system rather than a one-time generation task.

## Curated References

The **reference generator** is the skill that produces curated citation lists for each chapter with short statements of each source's relevance, resulting in a **curated reference list**: a deliberately selected set of sources chosen for quality and relevance rather than assembled by bulk search. Part of that selection is **crediting pedagogical authors**: naming the specific writers responsible for an influential explanation, analogy, or derivation, rather than citing only encyclopedic sources — and part of it is simply starting somewhere reliable, which is why **Wikipedia as a source** treats an encyclopedic reference as a reasonable starting point, placed before more specialized sources in a citation list.

!!! mascot-warning "Verify every URL before it ships."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Remember Chapter 2's hallucination warning — a citation that reads perfectly plausible can still point nowhere real. **URL verification** confirms that a cited web address actually resolves and contains the material attributed to it. Never publish a reference list without checking every single link; a fabricated citation is worse than no citation at all.

## Keeping References Separate

Just like Chapter 9's separate quiz files, references get their own file. **Reference file separation** means storing citations outside chapter prose so they can be reviewed and updated without loading the chapter body — a direct application of the file-layout token strategy you already met, this time applied to citations instead of assessments.

## The Glossary

A **glossary** is an alphabetical collection of terms with definitions, serving as the reference layer for vocabulary used across a book — you've been reaching into this book's own glossary throughout every chapter so far. The **glossary generator** is the skill that converts an enumerated idea list into formatted definitions meeting a defined quality standard, specifically the **ISO 11179 standards**: a metadata registry specification whose definition criteria require entries to be precise, concise, distinct, non-circular, and free of procedural rules. The most fundamental of those criteria is a **precise definition**: one that states exactly what a term means without ambiguity or unnecessary hedging. Once written, each entry becomes reachable through **glossary anchor links**: direct links from body text to a specific definition, letting readers resolve unfamiliar vocabulary without losing their place — the mechanism behind nearly every bolded term you've clicked, or could have clicked, throughout this book.

## Key Takeaways

- The **FAQ generator** produces a **FAQ**, organized by **FAQ categorization**, with **coverage gaps** revealing what's still missing.
- **Chatbot training JSON** turns a FAQ set into fuel for **retrieval augmented generation**.
- The **reference generator** produces a **curated reference list** that **credits pedagogical authors** and treats **Wikipedia** as a reasonable starting source — but only after every URL passes **verification**.
- **Reference file separation** keeps citations cheap to maintain, just like separate quiz files.
- The **glossary generator** produces **ISO 11179**-compliant, **precise definitions**, reachable throughout a book via **glossary anchor links**.

!!! mascot-celebration "You can now build the reference layer for an entire book."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    FAQs that reveal their own gaps, references that are actually verified, and a glossary precise enough to trust — that's a support system a reader can lean on. Right tool, right task!
