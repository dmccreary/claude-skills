---
name: textbook-to-presentation-generator
description: >
  Generate a compelling PowerPoint lecture presentation from an intelligent textbook 
  (MkDocs project with chapters, learning graph, and course description). The presentation 
  embodies McLuhan's "the medium IS the message" — every slide exemplifies the principle 
  it teaches. Uses pptxgenjs to create .pptx files with speaker notes, visual design, and 
  4-act storytelling structure. Use this skill whenever the user wants to create a 
  presentation, lecture deck, slide deck, or PowerPoint from a textbook, course, or 
  educational content. Also use when converting book content into presentation format, 
  or when the user says "create slides", "make a deck", "build a presentation", 
  "lecture slides", or "presentation from the textbook".
---

# Presentation Generator

**Version:** 1.0

Generate a lecture-ready PowerPoint presentation from an intelligent textbook project. The presentation is designed for live delivery — visual, story-driven, with progressive disclosure, audience interaction beats, and speaker notes that script the entire performance.

## Core Philosophy: The Medium IS the Message

The presentation doesn't *teach about* communication or subject-matter frameworks. It *is* the framework in action. The audience should experience principles before being told about them. Every slide must answer: **"Is this slide itself an example of the principle it discusses?"**

This means:
- When teaching structure, the presentation IS structured (Pyramid Principle — governing thought in minute 2, not minute 55)
- When teaching brevity, the slide has seven words maximum
- When teaching storytelling, the lecture IS a story (4-act arc)
- When teaching about cognitive load, no slide overloads the audience
- **Meta-moments**: The speaker reveals "what I just did was [framework name]" AFTER demonstrating it. The audience learns through experience, then gets the vocabulary.

## When to Use This Skill

Use when:
- An intelligent textbook exists (MkDocs project with chapters, course-description.md, learning graph)
- The user wants a lecture presentation for live delivery
- The user wants to convert textbook content into a slide deck
- The user says "create a presentation", "make slides", "build a deck", "lecture slides"

Do NOT use when:
- No textbook content exists yet (use course-description-analyzer and chapter generators first)
- The user wants a document, not a presentation (use docx skill)
- The user wants to edit an existing presentation (use the pptx editing workflow)

## Prerequisites

- Node.js installed
- `npm install pptxgenjs` (install locally in the output directory)
- An intelligent textbook project with:
  - `docs/course-description.md`
  - `docs/chapters/` with chapter content
  - `CLAUDE.md` with project conventions (optional but helpful)

## Workflow

### Step 1: Read the Textbook

Read these files to understand the content:

1. **Course description** (`docs/course-description.md`) — extract title, audience, key topics, learning outcomes
2. **CLAUDE.md** — extract tone, style, color palette, mascot info
3. **Chapter index files** — scan `docs/chapters/*/index.md` for chapter titles, key concepts, and the pedagogical flow
4. **Student feedback** (if available in `input-knowledge/`) — what resonated with prior audiences
5. **Original lecture notes** (if available) — the speaker's natural flow and stories

### Step 2: Design the Presentation Structure

Design a **4-act structure** following Klein's storytelling model applied to the lecture itself:

| Act | Purpose | Slides | Time |
|-----|---------|--------|------|
| **I: The Wake-Up Call** | Hook, establish stakes, live challenge | 6-8 | ~10 min |
| **II: The Toolkit** | Core frameworks with before/after demos | 10-14 | ~20 min |
| **III: The Power Tools** | Advanced techniques, persuasion, AI | 6-10 | ~12 min |
| **IV: The Close** | Action plan, textbook link, final quote | 4-6 | ~8 min |

**Target: 25-35 slides for a 50-60 minute lecture.** At ~1.5 min/slide average. Fewer slides = more speaker time per slide = more engaging.

Present the proposed structure to the user for approval before generating.

### Step 3: Design the Visual System

Extract or create a color palette from the textbook's CLAUDE.md:

```javascript
const C = {
  primary: "XXXXXX",      // From CLAUDE.md palette
  primaryDark: "XXXXXX",
  primaryLight: "XXXXXX",
  accent: "XXXXXX",       // Highlight color
  white: "FFFFFF",
  offWhite: "F5F5F5",
  black: "212121",
  gray: "757575",
  red: "C62828",           // For "before" / negative examples
  green: "2E7D32",         // For "after" / positive examples
};
```

**Typography:**
- Title font: Georgia (or serif from CLAUDE.md)
- Body font: Calibri (or sans-serif from CLAUDE.md)
- Title size: 32-44pt
- Body size: 14-20pt (never below 13pt)

**Layout rules:**
- No more than 7 words per line of body text
- One idea per slide
- Dark backgrounds (primary dark) for section dividers, title, close
- Light backgrounds (white) for content slides
- Accent color for emphasis bars, numbers, highlights

### Step 4: Generate the Presentation

Create a Node.js script that uses pptxgenjs to generate the .pptx file. Read `references/slide-patterns.md` for the reusable slide pattern library.

**Slide categories and their patterns:**

1. **Title slide** — dark bg, large title, subtitle, author, accent bar
2. **Section divider** — dark bg, large text, subtitle, accent bar
3. **Big number** — dark bg, one massive stat (80-120pt), context below
4. **Before/After comparison** — two columns, red accent (before) vs green (after)
5. **Framework visual** — shapes/diagrams illustrating a model (pyramid, stages, pillars)
6. **Evidence stack** — 3 cards with accent bars showing research findings
7. **Interactive beat** — light bg, challenge prompt in a card, instructions
8. **Quote** — dark bg, large italic text, attribution
9. **Action items** — numbered circles with titles and descriptions
10. **Resource/CTA** — textbook link, QR code placeholder, stats

### Step 5: Write Speaker Notes

Every slide gets detailed speaker notes. These are the real script — the slides are just visual anchors. Notes include:

- **TIMING**: Cumulative minutes (e.g., "TIMING: 15:00")
- **SAY**: The exact narrative to deliver (2-4 sentences, conversational)
- **META-MOMENT**: Where the speaker reveals the framework AFTER demonstrating it (e.g., "Notice what I just did? That was Klein's Dilemma stage.")
- **TRANSITION**: The bridge sentence to the next slide
- **AUDIENCE PULSE**: When to pause, ask a question, or let silence work

### Step 6: Generate and Verify

1. Run the Node.js script to generate the .pptx
2. Verify slide count matches the design
3. Extract text with `python -m markitdown output.pptx` to confirm content
4. Report the result to the user with slide count and timing estimate

## Output

The presentation file should be saved to:
```
{project-root}/presentation/{kebab-case-title}.pptx
```

Along with the generation script:
```
{project-root}/presentation/generate.js
```

## Adapting for Different Subjects

This skill works for ANY intelligent textbook, not just communication. The key adaptations:

- **Subject-specific stories**: Open with a story from the textbook's domain (engineering, science, business)
- **Framework names**: Use whatever frameworks the textbook teaches (not just Minto, Klein, etc.)
- **Color palette**: Derive from the textbook's CLAUDE.md
- **Audience**: Match the course-description.md target audience
- **Interactive beats**: Design exercises relevant to the subject matter

The 4-act structure and McLuhan principle remain constant regardless of subject.

## References

- `references/slide-patterns.md` — Reusable pptxgenjs code patterns for each slide type
- `references/speaker-notes-guide.md` — How to write effective speaker notes

## Best Practices

1. **Cut aggressively**: If a slide doesn't change understanding, delete it. The Dilution Effect applies to slide decks too.
2. **Story first, framework second**: Always demonstrate a principle through a story or example before naming the framework.
3. **One idea per slide**: If you need two sentences to explain what a slide is about, split it into two slides.
4. **Speaker notes ARE the presentation**: The slides are visual anchors. The speaker's narrative, pauses, and meta-moments are where learning happens.
5. **Test the McLuhan principle**: For every slide, ask "Is this slide itself an example of what it teaches?" If not, redesign it.
