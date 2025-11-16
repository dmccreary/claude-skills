# Chapter Content Generator

This skill is run on each chapter after the book-chapter-generator has been run.

This skill generates a structured chapter outline for intelligent textbooks by analyzing course descriptions, learning graphs, and concept dependencies. Use this skill after the learning graph has been created and before generating chapter content, to design an optimal chapter structure that respects concept dependencies and distributes content evenly across 6-20 chapters.

## When to Use This Skill

Use this skill when:
- A learning graph has been generated (learning-graph.json exists)
- The course description is finalized
- The concept taxonomy has been established
- Chapter content structure needs to be designed before writing begins

**Prerequisites:**
- `/docs/course-description.md` must exist
- `/docs/learning-graph/learning-graph.json` must exist with ~200 concepts
- `/docs/learning-graph/concept-taxonomy.md` should exist
- MkDocs chapter structure must be in place:

The table of contents must exist:

    '/docs/chapters/index.md`

There must be one index.md file for each chapter:

    '/docs/chapters/NN-CHAPTER_TITLE/index.md`

Withing the chapter index.md file there is a chapter title, summary and concept list.

**Do NOT use this skill if:**
- The learning graph hasn't been generated yet (use `learning-graph-generator` first)
- Chapter content already exists and just needs updating

For a full description of the steps see the main SKILL.md file in the skills folder:

[GitHub SKILL.md file for the Chapter Content Generator](https://github.com/dmccreary/claude-skills/blob/main/skills/chapter-content-generator/SKILL.md)
