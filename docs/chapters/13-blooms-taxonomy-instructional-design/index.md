---
title: Bloom's Taxonomy and Instructional Design
description: Details the five higher Bloom's cognitive levels, cognitive-level distribution, worked examples, the capstone project, and the full pedagogical mascot system.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 15:05:00
version: 0.09
---

# Bloom's Taxonomy and Instructional Design

## Summary

This chapter details all six Bloom's cognitive levels -- remember, understand, apply, analyze, evaluate, and create -- with their action verbs and cognitive-level distribution. It covers instructional-design conventions used to write chapter content: scaffolding, the define-before-display rule, reading-level consistency, and pedagogical mascot voice and placement. Students will be able to write a learning outcome at a specified Bloom's level after this chapter.

## Concepts Covered

This chapter covers the following 18 concepts from the learning graph:

1. Action Verbs for Outcomes
2. Flesch-Kincaid Grade Level
3. Mascot Voice and Placement
4. Understand Level
5. Mascot Admonition Types
6. Apply Level
7. Mascot Self-Introduction
8. Analyze Level
9. Worked Examples
10. Evaluate Level
11. Practice Exercises
12. Create Level
13. Cognitive Level Distribution
14. Capstone Project
15. Course Description Rubric
16. Assessing Student Understanding
17. Course Description Score
18. Course Description Analyzer

## Prerequisites

This chapter builds on concepts from:

- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [6. Agent Skill Fundamentals](../06-agent-skill-fundamentals/index.md)
- [12. Writing a Course Description](../12-writing-course-description/index.md)

---

!!! mascot-welcome "The rest of the ladder."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Chapter 12 got you to the Remember level. This chapter climbs the other five rungs, and finally explains exactly how I've been showing up in these margins the whole time. Right tool, right task!

## The Six Bloom's Levels

Above Remember, each Bloom's level demands more of a learner than the one below it. The **Understand level** covers construction of meaning, expressed through actions like explaining, summarizing, and classifying. The **Apply level** covers using a procedure in a given situation — implementing, solving, using. The **Analyze level** covers breaking material into parts and determining how they relate — differentiating, comparing. The **Evaluate level** covers judgment against criteria — critiquing, assessing, justifying. The **Create level** covers assembling elements into a new coherent whole — designing, constructing.

None of that means anything for a learning outcome until it's written as an **action verb for outcomes**: the observable verb that makes an outcome measurable, chosen to match the intended cognitive category. "Understand learning graphs" isn't measurable; "explain why a learning graph must be acyclic" is — and it's a deliberate Understand-level choice of verb, not Remember or Apply.

| Level | Sample Verbs | Example Outcome |
|-------|--------------|-------------------|
| Remember | define, list, identify | List the required SKILL.md fields |
| Understand | explain, summarize, classify | Explain why a graph must be acyclic |
| Apply | implement, solve, use | Apply the CSV-to-JSON script to a new graph |
| Analyze | differentiate, compare | Compare serial and parallel agent costs |
| Evaluate | critique, assess, justify | Assess whether a skill description triggers reliably |
| Create | design, construct | Design a meta-skill's routing table |

## Checking the Spread: Cognitive Level Distribution

A course that only ever asks learners to define and list things never asks them to actually use the material. **Cognitive level distribution** is the spread of material across the six cognitive categories, used to check that a course isn't concentrated in recall alone.

!!! mascot-warning "All-Remember courses look easy and teach nothing durable."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    It's tempting to write outcomes that are easy to test — mostly Remember and Understand. Check your distribution deliberately; a course with no Apply, Analyze, Evaluate, or Create outcomes is teaching facts, not capability.

## Worked Examples and Practice Exercises

Two techniques build the Apply level specifically. **Worked examples** are fully solved illustrations that show each step of a procedure, used to build competence before independent practice — you've seen several already, like Chapter 3's `re.search` example walked through line by line. **Practice exercises** are problems a learner attempts without a shown solution, used to consolidate a newly presented procedure once a worked example has demonstrated the pattern.

## The Capstone Project

At the top of both the taxonomy and a course's structure sits the **capstone project**: a culminating assignment requiring learners to combine most of a course's material into one substantial piece of work. This book's own capstone, per its course description, is building a complete intelligent textbook from scratch — every concept in all 31 chapters, applied at once.

!!! mascot-thinking "A capstone is where separate chapters become one skill."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Reading 31 chapters teaches 31 sets of ideas. A capstone is the only place those sets actually have to work together — a learning graph that respects a course description, chapters that respect the graph, content that respects the chapters. That integration is the real skill, and it only shows up under capstone conditions.

## Keeping Reading Level Honest: Flesch-Kincaid

Chapter 12 introduced reading level consistency as a goal; the **Flesch-Kincaid grade level** is how you actually check it — a readability measure derived from sentence and word length, used to compare chapters against a declared target. A chapter that scores well above or below the book's declared level is a signal to revise, not a fact to ignore.

## Assessing Student Understanding

None of these levels matter if you never check whether they landed. **Assessing student understanding** means determining what a learner has actually grasped, through questions and activities aligned to the stated outcomes — the whole reason a quiz question (which you'll meet in a later chapter) is written against a specific Bloom's level rather than picked at random.

## The Mascot System, Fully Explained

You've watched Kit work for twelve chapters now; here's the design behind it. **Mascot voice and placement** are the rules governing how a recurring character speaks and how often it appears, preventing overuse from diluting its effect — the reason you've never seen more than six Kit admonitions in a single chapter, and never two in a row. Those appearances aren't interchangeable: **mascot admonition types** are the distinct callout roles a recurring character occupies, such as warning, encouragement, or summary, each with its own visual treatment.

!!! mascot-tip "Six roles, one character, zero decoration."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Welcome, thinking, tip, warning, encourage, celebration — that's the complete set. If an admonition doesn't clearly fit one of those six jobs, the right move is to cut it, not to invent a seventh.

And Chapter 1's opening admonition wasn't an accident of format — it was a deliberate **mascot self-introduction**: the first appearance of a recurring character, in which it names itself and previews the roles it will play later in the book, so every appearance since has needed no re-explanation.

## Scoring a Course Description

Closing the loop back to Chapter 12, a course description isn't graded by feel. The **course description rubric** is the point-allocated scoring guide that assesses whether a course description contains every element needed for downstream generation, producing a **course description score**: the numeric result of applying that rubric, used as a gate before concept enumeration begins — a low score here should stop the pipeline before it wastes a single token generating concepts from an incomplete input. The **course description analyzer** is the skill that scores an existing course description against the rubric, or drafts one that satisfies it from scratch.

## Key Takeaways

- **Understand**, **Apply**, **Analyze**, **Evaluate**, and **Create** each carry their own **action verbs**; a course should show a real **cognitive level distribution**, not cluster at Remember.
- **Worked examples** build the pattern; **practice exercises** consolidate it; a **capstone project** forces everything to work together at once.
- **Flesch-Kincaid grade level** measures reading-level consistency objectively; **assessing student understanding** checks whether outcomes actually landed.
- **Mascot voice and placement**, the six **mascot admonition types**, and a one-time **mascot self-introduction** are the complete design behind a pedagogical mascot like Kit.
- A **course description rubric** produces a **course description score** that gates the pipeline, computed by the **course description analyzer**.

!!! mascot-celebration "You now understand every rule I've been following."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can name every Bloom's level, write an outcome at any of them, and explain exactly why I show up when I do. That's real Analyze-level understanding of how this whole book is built. Right tool, right task!
