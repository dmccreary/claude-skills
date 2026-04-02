# Chapter Content Generator Skill Update — Instructional Scaffolding

**Date:** 2026-04-02
**Skill:** chapter-content-generator
**Version:** 0.06 → 0.07
**Project:** claude-skills
**Triggered by:** Student feedback from University of St. Thomas (SEIS666: Digital Transformation with Generative AI)

## Background

A student using the Intelligent Textbook framework reported that generated chapter content consistently introduces concepts, diagrams, and code examples before the reader has the vocabulary to interpret them. The student described this as the generator producing the "content of reading rather than the experience of reading" — a gap between the framework's stated scaffolding goals and actual output.

The student is a Product Manager with no prior Claude Code experience who generated a textbook in their first week of class. They provided three specific examples from their Digital Transformation textbook (Chapters 5 and 6).

## Problem Analysis

### Three Specific Issues Identified

1. **Diagrams use undefined terms**
   - Example: A RAG pipeline diagram uses "vectors" and "embeddings" before either term is defined
   - The reader has no anchor for what the diagram is showing
   - A human expert would say "before we look at this diagram, let me explain two terms you'll need"

2. **Code examples contain unexplained parameters**
   - Example: A REST API code example contains `temperature` and `max_tokens` parameters with no bridge to the sections that explain them several pages later
   - The explanation exists in the chapter but comes after the code, not before it

3. **Tables introduce concepts cold**
   - Tables present new concepts that haven't been explained in prose yet
   - The reader has to reverse-engineer meaning from table cells
   - Tables should reinforce and organize information the reader already understands

### Root Cause

The chapter content generator's Step 2.4 (Generate Detailed Chapter Content) had rules for concept ordering (simple to complex) and non-text element frequency (no more than 3 paragraphs without a visual), but no rules governing the relationship between prose and non-text elements. The generator ensured concepts appeared in the right order but didn't ensure bridging language existed between prose explanations and the visual/code elements that depend on them.

## Changes Made to SKILL.md

### 1. New Content Generation Principle (Step 2.4, Principle 3)

Added **"Scaffolding — define before you display"** as a new numbered principle in the content generation section, inserted between "Concept ordering" (principle 2) and "Non-text elements" (renumbered to principle 4). Contains four sub-rules:

- **Vocabulary before visuals:** Every diagram, code example, or table must be preceded by prose that defines all technical terms it contains. A reader should never encounter a term for the first time inside a non-text element.
- **Bridge sentences before code:** Before any code example, include a plain-language sentence explaining what the code does and what its key parameters mean. Never present code and defer the explanation to a later section.
- **Prose first, tables reinforce:** Tables summarize or compare information the reader already understands. Never use a table to introduce new concepts. Pattern: (1) explain in prose, (2) then table.
- **Signpost what's coming:** Before complex elements, add a navigation cue like "Before we examine this diagram, let's define two key terms."

### 2. New Best Practice (#9)

Added **"Scaffolding — the experience of reading"** to the Best Practices section with a litmus test: "If a student reads linearly from top to bottom, will they have the vocabulary and context to understand each element when they reach it?"

### 3. New Common Pitfalls Section

Added a **"Scaffolding (CRITICAL — reader experience)"** pitfalls block before the existing "Content Quality" pitfalls. Contains eight specific do/don't items:

**Don'ts:**
- Diagram uses terms that haven't been defined in preceding prose
- Code example contains parameters explained only in a later section
- Table introduces new concepts instead of summarizing concepts already explained
- Complex element appears without a bridging sentence

**Do's:**
- Every technical term in a non-text element is defined in prose immediately before it
- Code examples preceded by plain-language explanations of parameters
- Tables reinforce and organize — they never introduce
- Navigation cues guide the reader through transitions

### 4. Updated Agent Prompt Template

Added a `SCAFFOLDING (CRITICAL)` section to the parallel agent prompt template so that agents spawned in parallel mode also enforce these rules. The four key rules are included inline in the prompt.

### 5. Version Bump

- Version number updated from 0.06 to 0.07 in all locations:
  - Header version field
  - Version features list (added scaffolding as first feature)
  - Both metadata template instances (`version: 0.07`)

## Files Modified

| File | Change |
|------|--------|
| `skills/chapter-content-generator/SKILL.md` | Added scaffolding principle, best practice, pitfalls, agent prompt update, version bump |

## Design Decisions

1. **Inserted scaffolding as a content generation principle rather than a separate phase** — Scaffolding isn't a post-processing step; it must be considered during generation. Placing it alongside concept ordering and non-text element rules ensures it's part of the same mental model.

2. **Added to agent prompt template, not just the main skill** — In parallel mode, agents receive a condensed prompt. Without explicit scaffolding rules in that prompt, parallel agents would miss the new guidelines.

3. **Used concrete examples from the feedback** — The pitfalls section references specific patterns (terms in diagrams, parameters in code, tables introducing concepts) rather than abstract principles, making violations easier to spot during generation.

4. **Did not create a separate skill** — The student suggested a separate "instructional design patterns" skill. Instead, the scaffolding rules were embedded directly in the content generator, since they govern how content is structured during generation rather than being a separate post-processing concern.

## Impact Assessment

- **All future chapter generation** will enforce define-before-display rules
- **Parallel agents** receive scaffolding guidance in their prompt template
- **Existing textbooks** are not affected — this only changes future generation
- **No breaking changes** — all existing workflow steps and file formats are unchanged
- **Token cost:** Minimal increase — bridging sentences add ~5-10% more prose per chapter but dramatically improve readability

## Acknowledgment

Thanks to the University of St. Thomas student for detailed, actionable feedback with specific examples. The observation that the generator produces "the content of reading rather than the experience of reading" precisely identified the gap and informed the fix.
