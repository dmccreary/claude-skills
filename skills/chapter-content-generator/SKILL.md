---
name: chapter-content-generator
description: This skill generates comprehensive chapter content for intelligent textbooks after the book-chapter-generator skill has created the chapter structure. Use this skill when a chapter index.md file exists with title, summary, and concept list, and detailed educational content needs to be generated at the appropriate reading level with rich non-text elements including diagrams, infographics, and MicroSims. (project, gitignored)
---

# Chapter Content Generator

**Version:** 0.04

## Overview

This skill generates detailed educational content for individual textbook chapters, transforming chapter outlines (title, summary, concept list) into comprehensive learning material with appropriate reading level, rich visual elements, and interactive components. The skill is designed to run after the `book-chapter-generator` skill has created the chapter structure.

**Version 0.04 Features:**
- **Parallel execution** - Generate content for multiple chapters simultaneously
- **3-4x faster** - 23 chapters in ~15-20 minutes instead of ~60+ minutes
- **Same token usage** - Parallel doesn't increase total tokens, only reduces wall-clock time

## When to Use This Skill

Use this skill when:
- The `book-chapter-generator` skill has created chapter directories with index.md files
- A chapter index.md contains: title, summary, and concepts covered list
- Detailed chapter content needs to be generated
- Content should be adapted to a specific reading level (junior high, senior high, college, graduate)
- Rich non-text elements (diagrams, MicroSims, infographics) are desired

Do NOT use this skill when:
- Chapter structure hasn't been created yet (use `book-chapter-generator` first)
- Content already exists and just needs editing (use Edit tool directly)
- Generating other types of content (prompts, glossaries, etc.)

## Execution Modes

### Parallel Mode (Default for 4+ chapters)

When generating content for 4 or more chapters, use parallel execution:

| Aspect | Sequential | Parallel |
|--------|------------|----------|
| Agents | 1 | 4-6 concurrent |
| Wall-clock time | ~60+ minutes (23 chapters) | ~15-20 minutes |
| Total tokens | Same | Same |

### Sequential Mode

Use for:
- Fewer than 4 chapters
- Debugging or troubleshooting
- When explicit sequential processing is requested

### Single Chapter Mode

Use for:
- Updating one chapter after outline revision
- Testing content format before batch generation

## Workflow

### Phase 1: Setup (Sequential)

This phase runs once before any content generation, reading shared context that all agents will need.

#### Step 1.1: Capture Start Time

```bash
date "+%Y-%m-%d %H:%M:%S"
```

Log the start time for the session report.

#### Step 1.2: Indicate Skill Running

Notify the user: "Chapter Content Generator Skill v0.04 running in [parallel/sequential] mode."

#### Step 1.3: Read Shared Context

Read and cache these files for all agents:

1. **Course Description** (`docs/course-description.md`)
   - Extract target audience and reading level
   - Note course objectives and tone guidelines
   - Identify any mascot or narrative elements (e.g., Delta in calculus)

2. **Learning Graph** (`docs/learning-graph/learning-graph.csv` or similar)
   - Load concept list with dependencies
   - Understand concept relationships for pedagogical ordering

3. **Glossary** (`docs/glossary.md`)
   - Load term definitions for consistent terminology
   - Note which concepts have glossary entries

4. **Project CLAUDE.md** (if exists)
   - Load project-specific guidelines
   - Note any mascot specifications, tone requirements, or special formatting

5. **Chapter List** (scan `docs/chapters/` directory)
   - Enumerate all chapter directories
   - Identify which chapters need content generation (have outline but no content)

#### Step 1.4: Determine Reading Level

Extract the grade reading level from the course description:

**Reading level indicators:**
- "junior-high", "junior high", "grades 7-9", "middle school" → Junior High
- "senior-high", "senior high", "grades 10-12", "high school" → Senior High
- "college", "undergraduate", "bachelor" → College
- "graduate", "master", "masters", "master's", "PhD", "doctoral" → Graduate

**Reading level characteristics:**
- **Junior High (Grades 7-9):** Simple sentences (12-18 words), common vocabulary, concrete examples, frequent visual aids
- **Senior High (Grades 10-12):** Mixed sentence complexity (15-22 words), technical vocabulary with definitions, balance of concrete and abstract
- **College:** Academic style (18-25 words), technical terminology, case studies, research context
- **Graduate:** Sophisticated prose (20-30+ words), full jargon, theoretical depth, research literature

Default to Grade 10 (Senior High) if not specified.

#### Step 1.5: Plan Chapter Batches (Parallel Mode)

Divide chapters into batches for parallel processing:

**Batch Size Guidelines:**
- 4-8 chapters: 2 agents (2-4 chapters each)
- 9-15 chapters: 3-4 agents (3-4 chapters each)
- 16-24 chapters: 4-6 agents (4-5 chapters each)
- 25+ chapters: 5-6 agents (5-6 chapters each)

**Example for 23 chapters:**
```
Agent 1: Chapters 1-4 (Foundations)
Agent 2: Chapters 5-8 (Core Concepts Part 1)
Agent 3: Chapters 9-12 (Core Concepts Part 2)
Agent 4: Chapters 13-16 (Applications Part 1)
Agent 5: Chapters 17-20 (Applications Part 2)
Agent 6: Chapters 21-23 (Advanced Topics)
```

### Phase 2: Content Generation (Parallel or Sequential)

#### Parallel Execution

Spawn multiple Task agents simultaneously using the Task tool. Each agent receives:

1. **Shared context** (course info, reading level, glossary terms, tone guidelines)
2. **Assigned chapters** (specific chapter directories)
3. **Content format template** (the standard format from this skill)
4. **Output instructions** (write content to each chapter's index.md)

**Agent Prompt Template:**

```
You are generating educational content for an intelligent textbook. Generate
detailed chapter content for the following chapters.

COURSE CONTEXT:
- Course: [course name]
- Target audience: [audience]
- Reading level: [level] - [characteristics]
- Tone: [tone guidelines from course description or CLAUDE.md]

CONTENT GUIDELINES:
- No more than 3 paragraphs of pure text without a non-text element
- Use diverse element types (lists, tables, diagrams, MicroSims)
- Present concepts in pedagogical order (simple to complex)
- Include LaTeX equations where appropriate (backslash delimiters: `\( \)` for inline, `\[ \]` for display)

NON-TEXT ELEMENTS:
- Markdown lists and tables: embed directly (blank line before)
- Diagrams, MicroSims, infographics: use <details markdown="1"> blocks with #### Diagram: header

CHAPTERS TO PROCESS:
[List specific chapter directories with full paths]

FOR EACH CHAPTER:
1. Read the chapter index.md file to get title, summary, concepts covered
2. Generate comprehensive content (3000-5000 words)
3. Include 4-6 non-text elements per chapter
4. Verify all concepts from "Concepts Covered" list are addressed
5. Write the content to docs/chapters/[chapter-dir]/index.md

METADATA FORMAT (add to top of each file):
---
title: [Chapter Title]
description: [Short description]
generated_by: claude skill chapter-content-generator
date: [YYYY-MM-DD HH:MM:SS]
version: 0.04
---

REPORT when done:
- Chapter name
- Word count
- Non-text elements (lists, tables, diagrams, MicroSims)
- Concepts covered (X of Y)
```

**Launching Parallel Agents:**

Use the Task tool with multiple invocations in a SINGLE message to run agents in parallel:

```markdown
[Call Task tool for Agent 1: Chapters 1-4]
[Call Task tool for Agent 2: Chapters 5-8]
[Call Task tool for Agent 3: Chapters 9-12]
[Call Task tool for Agent 4: Chapters 13-16]
[Call Task tool for Agent 5: Chapters 17-20]
[Call Task tool for Agent 6: Chapters 21-23]
```

**IMPORTANT:** All Task tool calls MUST be in a single message to execute in parallel. If sent in separate messages, they will run sequentially.

#### Sequential Execution

For sequential mode or fewer than 4 chapters, process each chapter one at a time following the per-chapter steps below.

### Phase 2 Steps (Per Chapter - used by agents or sequential mode)

#### Step 2.1: Verify Chapter File Exists

Verify that the chapter file exists and has required elements.

**Expected input format:**
- Chapter name: "01-intro-to-itil-and-config-mgmt" or "Chapter 1"
- Full path: "/docs/chapters/01-intro-to-itil-and-config-mgmt/index.md"
- Relative path: "chapters/01-intro-to-itil-and-config-mgmt/index.md"

**Chapter directory structure:**
```
/docs/chapters/NN-lowercase-name/index.md
```

Where:
- `NN` = Two-digit chapter number with leading zero (e.g., "01", "07", "12")
- `lowercase-name` = URL-friendly lowercase name with dashes, no spaces

#### Step 2.2: Verify Chapter Outline

Open the chapter file and check for required elements.

**Required elements:**

1. **Title** in header 1 (# Title)
2. **Summary** in level 2 header (## Summary)
3. **Concepts Covered** in level 2 header (## Concepts Covered) with numbered list

**Actions:**
1. Parse the chapter index.md file
2. Extract:
   - Chapter title
   - Summary text
   - List of concepts covered (numbered list)
3. If any element is missing, skip chapter or ask user to provide content
4. Store concepts list for verification in Step 2.5

#### Step 2.3: Add Metadata

Add metadata to the top of the index file:

```markdown
---
title: Chapter Title
description: Short description of title
generated_by: claude skill chapter-content-generator
date: YYYY-MM-DD HH-MM-SS
version: 0.04
---
```

#### Step 2.4: Generate Detailed Chapter Content

Generate comprehensive educational content based on the chapter outline, concept list, and reading level.

**Content generation principles:**

1. **Reading level adaptation:**
   - Apply appropriate sentence complexity, vocabulary, and explanation style
   - See `references/reading-levels.md` for specific guidelines

2. **Concept ordering:**
   - Present simple concepts first, complex concepts last
   - Follow natural pedagogical progression
   - Do NOT necessarily follow the order in "Concepts Covered" list
   - Build on previously explained concepts

3. **Non-text elements:**
   - Goal: No more than 3 paragraphs of pure text without a non-text element.
   - Use diverse element types (don't repeat the same type).
   - Place special focus on interactive elements (infographics, MicroSims).
   - When appropriate, render equations in LaTeX using backslash delimiters:
     - Inline math: `\( equation \)` for equations within sentences
     - Display math: `\[ equation \]` for standalone equations on their own line
   - Do NOT use dollar sign delimiters (`$` or `$$`)
   - See the math-equations.md file in the references for proper formatting of equations.

**Non-text element types:**

Elements embedded directly in markdown (no `<details markdown="1">` block):

1. **Markdown lists** (bullet or numbered) - ALWAYS put blank line before list
2. **Markdown tables** - ALWAYS put blank line before table

Elements requiring diagram header and `<details markdown="1">` specification blocks:

3. **Diagrams/drawings** - System architectures, relationships, data flows
4. **Interactive infographics** - Clickable concept maps, progressive disclosure, hovers with definitions appearing in tooltips consistent with the glossary
5. **MicroSims** - p5.js simulations with interactive controls
6. **Charts** - Bar, line, pie charts with quantitative data
7. **Timelines** - Historical progression, sequential events
8. **Maps** - Geographic distribution with movement arrows
9. **Workflow diagrams** - Business processes with hover text
10. **Graph data models** - Entity relationships using vis-network
11. **Causal Loop Diagrams** - used in systems thinking and explaining causality

For each `<details markdown="1">` block element, use this structure:

```markdown
#### Diagram: [Brief descriptive title]

<details markdown="1">
<summary>[Brief descriptive title]</summary>
Type: [element-type]
**sim-id:** [kebab-case-directory-name]<br/>
**Library:** [p5.js | vis-network | Chart.js | Mermaid | Plotly | Leaflet | vis-timeline]<br/>
**Status:** Specified

[Detailed specification following guidelines in references/content-element-types.md]

Implementation: [Technology/approach]
</details>
```

The three structured fields enable machine-readable extraction by batch utilities:
- **sim-id** — kebab-case directory name (e.g., `angle-type-explorer`), used by `extract-sim-specs.py`
- **Library** — JavaScript library for CDN selection by `generate-sim-scaffold.py`
- **Status** — initial lifecycle state (always `Specified` for new specs)

Do not indent any text within a `<details markdown="1">` block. Do not put any leading spaces or tabs on newlines within a `<details markdown="1">` block.

Make SURE to put the level 4 header with the prefix `#### Diagram:` before the details. This is REQUIRED!

**Specification requirements:**
- Detailed enough that another skill or developer can implement without additional context
- Include all visual elements, data, labels, colors, interactions
- Specify canvas sizes, layout, default parameters
- Specify that the visual elements must have a responsive design that must respond to window resize events
- For MicroSims: describe learning objective, controls, visual elements, behavior
- See `references/content-element-types.md` for complete specification guidelines for each element type

**Content structure:**

1. Start with introductory paragraphs connecting to chapter summary
2. Present concepts in pedagogical order (simple to complex)
3. Integrate non-text elements naturally throughout
4. Use markdown lists and tables frequently (with blank lines before them)
5. Include `<details markdown="1">` blocks for complex visual/interactive elements
6. Place a level 4 markdown header before each `details` block
   ```#### Diagram: [Diagram Name]```
7. End with summary or key takeaways section

**Interactive elements emphasis:**
- Prioritize MicroSims and infographics that enable:
  - Student interaction tracking
  - Progress gauging
  - Personalized content recommendations
- Each interactive element should have clear **Learning objectives:**
- Reference a section of the 2001 Bloom Taxonomy when you describe a learning objective:
   - **Remembering:** Recalling facts, terms, basic concepts, and answers without necessarily understanding their meaning.
   - **Understanding:** Explaining ideas or concepts, demonstrating comprehension by summarizing or rephrasing information.
   - **Applying:** Using acquired knowledge to solve problems in new or unfamiliar situations.
   - **Analyzing:** Breaking down information into parts to understand its structure and relationships, and drawing comparisons.
   - **Evaluating:** Making judgments about information based on set criteria or standards, requiring critical thinking and justification.
   - **Creating:** Producing new or original work by combining elements to form a novel whole or solution.

#### Step 2.5: Verify Completeness

After generating chapter content, verify all concepts have been covered.

**Verification process:**
1. Review the generated content
2. Check that each concept from "Concepts Covered" list appears in the content
3. Create a checklist showing which concepts were covered
4. If any concepts missing:
   - Add content covering those concepts
   - Integrate them naturally into existing structure
5. Update the chapter index.md file with the complete generated content
6. Make **Absolutely Sure** that the content has been written to the chapter index.md file. Do a word count to make sure that **ALL** the content is present and that the TODO has been removed.

**Actions:**
- Replace the "TODO: Generate Chapter Content" placeholder with generated content
- Keep the existing title, summary, concepts list, and prerequisites sections
- Add the new detailed content after the prerequisites section

### Phase 3: Aggregation (Sequential, after parallel agents complete)

After all parallel agents complete, aggregate results.

#### Step 3.1: Collect Agent Results

Wait for all Task agents to complete. Collect from each:
- List of chapter files created/updated
- Per-chapter statistics (word count, non-text elements, concepts covered)
- Any errors or issues encountered

#### Step 3.2: Generate Summary Report

Create a summary of all content generation:

```markdown
# Chapter Content Generation Report

Generated: YYYY-MM-DD
Execution Mode: Parallel (6 agents)
Wall-clock Time: X minutes Y seconds

## Overall Statistics

- **Total Chapters:** 23
- **Total Words:** ~100,000
- **Avg Words per Chapter:** ~4,350
- **Total Non-text Elements:** ~115

## Execution Summary (Parallel Mode)

| Agent | Chapters | Words | Elements | Time |
|-------|----------|-------|----------|------|
| Agent 1 | 1-4 | 17,200 | 20 | 3m 15s |
| Agent 2 | 5-8 | 18,100 | 22 | 3m 42s |
| Agent 3 | 9-12 | 17,800 | 19 | 3m 28s |
| Agent 4 | 13-16 | 18,500 | 21 | 3m 51s |
| Agent 5 | 17-20 | 17,900 | 18 | 3m 33s |
| Agent 6 | 21-23 | 13,200 | 15 | 2m 45s |

## Per-Chapter Summary

| Chapter | Words | Lists | Tables | Diagrams | MicroSims | Concepts |
|---------|-------|-------|--------|----------|-----------|----------|
| 1. Foundations | 4,200 | 6 | 3 | 2 | 1 | 15/15 ✓ |
| 2. Limits | 4,500 | 5 | 2 | 3 | 2 | 14/14 ✓ |
| ... | ... | ... | ... | ... | ... | ... |
```

#### Step 3.3: Capture End Time and Write Session Log

Capture the end time:

```bash
date "+%Y-%m-%d %H:%M:%S"
```

Export the session information to `logs/chapter-content-generator-YYYY-MM-DD.md`:

```markdown
# Chapter Content Generator Session Log

**Skill Version:** 0.04
**Date:** YYYY-MM-DD
**Execution Mode:** Parallel (6 agents)

## Timing

| Metric | Value |
|--------|-------|
| Start Time | YYYY-MM-DD HH:MM:SS |
| End Time | YYYY-MM-DD HH:MM:SS |
| Elapsed Time | X minutes Y seconds |

## Token Usage

| Phase | Estimated Tokens |
|-------|------------------|
| Setup (shared context) | ~20,000 |
| Agent 1 (Ch 1-4) | ~80,000 |
| Agent 2 (Ch 5-8) | ~80,000 |
| ... | ... |
| Aggregation | ~5,000 |
| **Total** | ~500,000 |

## Results

- Total chapters: N
- Total words: ~X
- All chapters written successfully: Yes/No

## Files Created/Updated

[List all chapter index.md files]
```

#### Step 3.4: Notify User

Notify the user:

"Chapter Content Generator v0.04 complete!

- **Mode:** Parallel (6 agents)
- **Elapsed time:** X minutes Y seconds
- **Chapters processed:** 23
- **Total words:** ~100,000
- **Non-text elements:** ~115

All chapter content has been written to their respective index.md files.

Session logged to `logs/chapter-content-generator-YYYY-MM-DD.md`"

## Resources

This skill includes reference files that provide detailed guidelines for content generation:

### references/content-element-types.md

Comprehensive specifications for all non-text element types (3-11 above). Includes:
- When to use each element type
- Required information for specifications
- Implementation approaches
- Example specifications in `<details markdown="1">` block format
- Place a level 4 Diagram header before each `details` element

```markdown
#### Diagram: [Diagram Name]
```

Load this reference when generating content to ensure proper specification of diagrams, MicroSims, infographics, charts, timelines, maps, workflows, and graph models.

### references/reading-levels.md

Detailed guidelines for adapting content to different reading levels. Includes:
- Sentence structure and length guidelines
- Vocabulary choices
- Explanation styles
- Example complexity
- Assumed background knowledge
- Example text at each level

Load this reference when determining how to write content at the appropriate reading level.

## Best Practices

1. **Always read references:** Load `references/content-element-types.md` and `references/reading-levels.md` before generating content

2. **Maintain blank lines:** Always place blank line before markdown lists and tables (MkDocs requirement)

3. **Pedagogical ordering:** Don't feel constrained by concept list order - teach concepts in the most effective sequence

4. **Visual variety:** Mix different types of non-text elements rather than using the same type repeatedly

5. **Interactive emphasis:** Prioritize MicroSims and infographics that enable student engagement tracking

6. **Detailed specifications:** Make `<details markdown="1">` blocks comprehensive enough for implementation without additional context

7. **Concept integration:** Weave concepts together naturally rather than treating them as isolated topics

8. **Appropriate depth:** Match explanation depth to reading level (more scaffolding for junior high, more theory for graduate)

9. **Verification:** Always check that all concepts from "Concepts Covered" list appear in generated content

10. **Consistent style:** Maintain consistent voice, terminology, and visual style throughout chapter

11. **Parallel execution:** When processing 4+ chapters, always use parallel mode for efficiency

12. **Real timestamps:** Always use actual system timestamps, never synthetic data

## Common Pitfalls to Avoid

**Content Quality:**
- ❌ More than 3 paragraphs without a non-text element
- ❌ Using the same element type repeatedly
- ❌ Missing concepts from the "Concepts Covered" list
- ❌ Content too advanced or too simple for reading level

**Formatting:**
- ❌ Missing blank line before lists or tables
- ❌ Indenting content inside `<details>` blocks
- ❌ Missing `#### Diagram:` header before details blocks
- ❌ Missing closing `</details>` tag

**Parallel Execution:**
- ❌ Sending Task calls in separate messages (runs sequentially)
- ❌ Not waiting for all agents before aggregation
- ❌ Forgetting to aggregate statistics from all agents
- ❌ Using synthetic timestamps instead of real ones

## Output Files Summary

**Required (Per Chapter):**
1. Chapter content: `docs/chapters/[chapter-name]/index.md`

**Recommended (Aggregate):**
2. `logs/chapter-content-generator-YYYY-MM-DD.md` - Session log with timing

**Optional:**
3. Summary report with per-chapter statistics

## Example Session

### Parallel Mode (Default)

**User:** "Generate content for all chapters"

**Claude (using this skill):**

1. Captures start time
2. Notifies: "Chapter Content Generator Skill v0.04 running in parallel mode."
3. Reads shared context (course description, learning graph, glossary, CLAUDE.md)
4. Determines reading level (e.g., Senior High)
5. Scans chapter directories, finds 23 chapters needing content
6. Plans batches: 6 agents, ~4 chapters each
7. Spawns 6 Task agents in a SINGLE message (parallel execution)
8. Waits for all agents to complete
9. Aggregates results from all agents
10. Captures end time
11. Writes session log
12. Reports: "Chapter Content Generator v0.04 complete! Mode: Parallel. Time: 18m 32s. Chapters: 23. Words: ~100,000."

### Sequential Mode

**User:** "Generate content for Chapter 3 only"

**Claude (using this skill):**

1. Reads shared context
2. Verifies Chapter 3 file exists with required elements
3. Determines reading level
4. Generates comprehensive content (~4,000 words)
5. Includes 4-6 non-text elements
6. Verifies all concepts covered
7. Writes content to chapter index.md
8. Reports: "Generated content for Chapter 3. Words: 4,200. Elements: 5. Concepts: 15/15."

## Example Report

```
✅ Chapter content generated successfully!

Chapter: 01-intro-to-itil-and-config-mgmt
Reading level: Graduate
Content length: ~3,500 words

Non-text elements:
- 6 markdown lists
- 3 markdown tables
- 2 diagrams (CMDB architecture, ITIL process flow)
- 1 interactive timeline (ITIL evolution)
- 1 MicroSim (Configuration drift simulator)
- 1 workflow diagram (Change management process)

Interactive elements: 2 (timeline, MicroSim)
Skills required: 2 (microsim-p5 for MicroSim, infographic-generator for timeline)

All 20 concepts covered: ✓
```

!!! Note
   For admonitions to work, your mkdocs.yml must have admonition and pymdownx.details enabled.
