---
name: chapter-content-generator
description: Generates detailed chapter content for an intelligent textbook — text, diagrams, MicroSims, and exercises at the appropriate Bloom's level. Use when a chapter's index.md exists with title, summary, and concept list.
model: sonnet
license: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
---

# Chapter Content Generator

**Version:** 0.09

## Overview

This skill generates detailed educational content for individual textbook chapters, transforming chapter outlines (title, summary, concept list) into comprehensive learning material with appropriate reading level, rich visual elements, and interactive components. The skill is designed to run after the `book-chapter-generator` skill has created the chapter structure.

**Version 0.09 Features:**
- **Mascot self-introduction in Chapter 1** - When the project CONTENT-GENERATION-GUIDE.md defines a pedagogical mascot, the FIRST mascot admonition in Chapter 1 must be a self-introduction that names the mascot and enumerates each of the six pose-roles the mascot will play across the book. This sets reader expectations for every later chapter (see Step 2.4, principle 4)

**Version 0.07 Features:**
- **Instructional scaffolding** - Define-before-display rules ensure terms are explained before diagrams use them, code parameters are explained before code examples, and tables reinforce rather than introduce concepts (see Step 2.4, principle 3)
- **Sequential execution** - Generate content one chapter at a time to avoid excessive token usage. A user may override this with the phrase "use parallel execution" but the skill will warn them that a 38% additional tokens will be used
- **Edge direction validation** - Mandatory check to prevent inverted dependency bugs (see Step 1.3a)

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
- The user is almost out of tokens (over 95% of used in a 5-hour window)

## Execution Modes

### Sequential Mode (Default for all use-cases)

- Always only do one chapter at a time due to large overhead of parallel mode
- Wait for a chapter to totally finish and log the session before you begin the next chapter
- Clearly indicate to the user when each chapter is finished

### Parallel Mode (Only on request)

Parallel mode should ONLY be used when the user specifically request parallel execution.
Warn the user that there will be a substantial token penalty to pay for parallel execution.

### Single Chapter Mode

Use for:
- Updating one chapter after outline revision
- Testing content format before batch generation

## Workflow

### Phase 1: Setup (Sequential)

This phase runs once before any content generation, reading shared context that all agents will need.

#### Step 1.1: Capture Start Time for Logging

```bash
date "+%Y-%m-%d %H:%M:%S" >>logs/ch-{NN}-content-generation.md
```

Where {NN} is the two digit chapter number with zero padding.

Log the start time for the session report.

#### Step 1.2: Indicate Skill Running

Notify the user: "Chapter Content Generator Skill v0.09 running in [parallel/sequential] mode."

#### Step 1.3: Read Shared Context

Read and cache these files for all agents:

1. **Course Description** (`docs/course-description.md`)
   - Extract target audience and reading level
   - Note course objectives and tone guidelines in the project CONTENT-GENERATION-GUIDE.md
   - Identify any mascot or narrative elements (e.g., Delta in calculus) in the project CONTENT-GENERATION-GUIDE.md

2. **Learning Graph** (`docs/learning-graph/learning-graph.json` and/or `learning-graph.csv`)
   - Load concept list with dependencies
   - Understand concept relationships for pedagogical ordering

   !!! info "Learning Graph = Concept Dependency Graph (a DAG)"
       A learning graph is a **Concept Dependency Graph** -- a directed acyclic
       graph (DAG) where each edge represents a "depends on" relationship. We use
       the **dependency direction** (edges point FROM a concept TO the concepts it
       depends on) because this aligns with standard graph theory algorithms for
       topological sorting, cycle detection, and transitive reduction.

       Some learning management systems use an **enablement graph** where edges
       point the opposite way (FROM prerequisite TO enabled concept). That direction
       is more intuitive for some teachers but less natural for graph algorithms.
       This project uses the dependency direction exclusively.

   !!! danger "CRITICAL: Edge Direction in learning-graph.json"
       In the vis-network JSON format, edges point **FROM dependent TO prerequisite**
       (the dependency direction).

       - Edge `{from: 5, to: 1}` means "Biodiversity (5) depends on Ecology (1)"
       - It does NOT mean "Ecology leads to Biodiversity" (that would be the enablement direction)

       **To build a prerequisite map:**
       ```python
       # CORRECT: dependency direction -- from=dependent, to=prerequisite
       prereqs[edge['from']].add(edge['to'])
       ```

       **NEVER use:**
       ```python
       # WRONG: accidentally converts to enablement direction, inverting ALL dependencies
       prereqs[edge['to']].add(edge['from'])
       ```

       Getting this wrong produces hundreds of false violations and wastes
       significant tokens on invalid chapter designs. Always validate with
       Step 1.3a before proceeding.

3. **Glossary** (`docs/glossary.md`)
   - Load term definitions for consistent terminology if they exist
   - In most cases the glossary is created after the content is generated
   - Note which concepts have glossary entries

4. **Project CONTENT-GENERATION-GUIDE.md** (if exists)
   - Load project-specific guidelines
   - Note any reading level, mascot specifications, tone requirements, or special formatting

5. **Chapter List** (scan `docs/chapters/` directory)
   - Enumerate all chapter directories
   - Identify which chapters need content generation (have outline but no content)

#### Step 1.3a: Validate Edge Direction (MANDATORY)

Before using any dependency data, verify the edge direction is correct. This step prevents the most common and expensive bug in chapter generation -- an inverted dependency map that silently produces invalid chapter orderings.

**Validation procedure:**

1. Identify foundational concepts -- those with empty Dependencies in the CSV, or with zero prerequisites in the JSON
2. Build the prerequisite map using `prereqs[edge['from']].add(edge['to'])`
3. Check that foundational concepts have ZERO entries in the prereqs map

```python
import json
from collections import defaultdict

with open('docs/learning-graph/learning-graph.json') as f:
    data = json.load(f)

# Build prereqs: from=dependent, to=prerequisite
prereqs = defaultdict(set)
for e in data['edges']:
    prereqs[e['from']].add(e['to'])

# Find concepts with zero prerequisites (foundational)
all_ids = {n['id'] for n in data['nodes']}
foundational = all_ids - set(prereqs.keys())

print(f"Foundational concepts (no prerequisites): {len(foundational)}")
for fid in sorted(foundational):
    node = next(n for n in data['nodes'] if n['id'] == fid)
    print(f"  {fid}: {node['label']}")

# SANITY CHECK: foundational concepts should be simple/introductory
# If you see advanced concepts here, the edge direction is WRONG
```

**Pass criteria:**

- Foundational concepts should be simple, introductory terms (e.g., "Ecology", "Energy", "System")
- If advanced concepts appear as foundational (e.g., "Sustainability", "Climate Change", "Tipping Points"), the edge direction is inverted -- STOP and fix before proceeding
- The number of foundational concepts should be small (typically 3-10 for a 200-400 concept graph)
- If you see 50+ "foundational" concepts, the direction is likely inverted

**If validation fails:** Do NOT proceed with content generation. Report the issue to the user and suggest re-running with the correct edge direction.

#### Step 1.3b: Verify Chapter Dependency Order (MANDATORY)

After validating edge direction, verify that every chapter's concept prerequisites have already been covered in earlier chapters. This ensures content can reference prior material without forward references.

```python
# Build chapter_map: concept_id -> chapter_index
chapter_map = {}
for i, (title, cids) in enumerate(chapters):
    for cid in cids:
        chapter_map[cid] = i

# Check: for every concept, all prerequisites must be in same or earlier chapter
violations = []
for i, (title, cids) in enumerate(chapters):
    for cid in cids:
        for dep in prereqs.get(cid, set()):
            if dep in chapter_map and chapter_map[dep] > i:
                violations.append(
                    f"  {nodes[cid]['label']}(ch{i+1}) needs "
                    f"{nodes[dep]['label']}(ch{chapter_map[dep]+1})"
                )

if violations:
    print(f"DEPENDENCY VIOLATIONS: {len(violations)}")
    for v in violations:
        print(v)
    print("\nDo NOT generate content until all violations are resolved.")
else:
    print("All dependencies respected. Safe to generate content.")
```

**Pass criteria:** Zero violations. If any exist, the chapter structure must be fixed before content generation begins.

#### Step 1.4: Determine Reading Level

Extract the grade reading level from the course description:

**Reading level indicators:**
- "grade-school", "grade school", "grades 1-6", "elementary school" → Elementary School
- "junior-high", "junior high", "grades 7-9", "middle school" → Junior High
- "senior-high", "senior high", "grades 10-12", "high school" → Senior High
- "college", "undergraduate", "bachelor" → College
- "graduate", "master", "masters", "master's", "PhD", "doctoral" → Graduate

**Reading level characteristics:**
- **Grade School (Grades 1-6):** Very sentences (10-14 words), common vocabulary, concrete examples, frequent visual aids
- **Junior High (Grades 7-9):** Simple sentences (12-18 words), common vocabulary, concrete examples, frequent visual aids
- **Senior High (Grades 10-12):** Mixed sentence complexity (15-22 words), technical vocabulary with definitions, balance of concrete and abstract
- **College:** Academic style (18-25 words), technical terminology, case studies, research context
- **Graduate:** Sophisticated prose (20-30+ words), full jargon, theoretical depth, research literature

Default to Grade 10 (Senior High) if not specified.

#### Step 1.5: Plan Parallel Chapter Batches (Only after an explicit request)

This workflow runs only after the user explicitly requests parallel execution.
Warn the user about the token cost before proceeding. Otherwise, skip this step
and process every chapter sequentially.

For an explicitly requested parallel run, divide chapters into batches:

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

### Phase 2: Content Generation (Sequential by default)

#### Parallel Execution (Only after an explicit request)

Do not enter this workflow unless the user explicitly requested parallel
execution. Warn the user about the token cost before proceeding. When that
condition is met, spawn multiple Task agents simultaneously using the Task
tool. Each agent receives:

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
- Tone: [tone guidelines from course description or CONTENT-GENERATION-GUIDE.md]

CONTENT GUIDELINES:
- No more than 4 paragraphs of pure text without a non-text element
- Use diverse element types (lists, tables, diagrams, MicroSims)
- Present concepts in pedagogical order (simple to complex)
- Include LaTeX equations where appropriate (backslash delimiters: `\( \)` for inline, `\[ \]` for display)

SCAFFOLDING (CRITICAL):
- Define every technical term in prose BEFORE it appears in a diagram, code block, or table
- Before code examples, explain what the code does and what key parameters mean in plain language
- Tables must summarize concepts already explained — never introduce new concepts via tables
- Add bridging sentences before complex elements ("Before we examine this diagram, let's define...")

MASCOT (if a mascot is defined in CONTENT-GENERATION-GUIDE.md):
- If you are processing CHAPTER 1, the FIRST mascot admonition must be a self-introduction: state the mascot's name, list every pose-role the mascot plays across the book, and end with a contract sentence that the mascot is a signal not decoration. See Step 2.4 principle 4 for the exact pattern.
- For chapters 2 and beyond, open with a normal mascot-welcome admonition that gets straight into chapter-specific content. Do NOT repeat the self-introduction.
- Respect the mascot frequency rules in the project CONTENT-GENERATION-GUIDE.md (typically 5–6 admonitions per chapter, never back-to-back, exactly one welcome at start and one celebration at end).

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
version: 0.09
---

REPORT when done:
- Chapter name
- Word count
- Non-text elements (lists, tables, admonitions, diagrams, MicroSims)
- Concepts covered (X of Y)
```


#### Sequential Execution

Unless the user explicitly requested parallel execution, process every chapter
one at a time following the per-chapter steps below, regardless of chapter count.

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

**Launching Parallel Agents:**
This is done ONLY if the user requests parallel execution. Warn them about the
token cost before proceeding.

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
version: 0.09
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

3. **Scaffolding — define before you display:**
   - **Vocabulary before visuals:** Every diagram, code example, or table must be preceded by prose that defines all technical terms it contains. If a diagram shows "vectors" and "embeddings," those terms must be explained in the paragraph(s) immediately before the diagram. A reader should never encounter a term for the first time inside a non-text element.
   - **Bridge sentences before code:** Before any code example, include a plain-language sentence explaining what the code does and what its key parameters mean. Never present code and defer the explanation to a later section — the explanation must come first. Example: "The `temperature` parameter controls randomness (0 = deterministic, 1 = creative). The `max_tokens` parameter sets the maximum response length."
   - **Prose first, tables reinforce:** Tables summarize or compare information the reader already understands. Never use a table to introduce new concepts. The pattern is: (1) explain concepts in prose, (2) then present a table that organizes or compares them. If a reader would need to reverse-engineer meaning from table cells, the table is premature.
   - **Signpost what's coming:** Before complex elements, add a navigation cue: "Before we examine this diagram, let's define two key terms." or "The following table summarizes the three approaches we just discussed." These one-sentence bridges transform content from a reference document into a guided learning experience.

4. **Mascot self-introduction in Chapter 1 (MANDATORY when a mascot is defined):**

   If the project CONTENT-GENERATION-GUIDE.md defines a pedagogical mascot, the **first mascot admonition in Chapter 1** is not a normal welcome — it is a **self-introduction** that orients the reader to the mascot's role for the rest of the book. This sets reader expectations once, so every later chapter can use the mascot without re-explaining what it is.

   The self-introduction admonition must:

   - Use the `mascot-welcome` admonition type (it doubles as the chapter-opening welcome).
   - Have the mascot **state its name, species/type, and one personality detail** in a warm first-person voice. Match the tone the project CONTENT-GENERATION-GUIDE.md prescribes (playful, formal, dry, etc.).
   - **Enumerate every pose-role** the mascot will use across the book as a numbered list, in the order they typically appear during a chapter (welcome → think → tip → warn → encourage → celebrate is the standard six-pose set). Each list item is one short sentence describing *what the mascot does in that pose*, not what the pose looks like.
   - **End with a contract sentence** — something like "If I'm not doing one of those six things, I'm not in the chapter." — so the reader understands the mascot is used with restraint and is a *signal*, not decoration.
   - Read the project CONTENT-GENERATION-GUIDE.md mascot-rules section (if present) to extract the exact pose names, filenames, and roles. Do not invent poses the project does not define.

   Do this **only in Chapter 1, only on the mascot's very first appearance**, and never again. Chapters 2+ open with a normal `mascot-welcome` admonition that gets straight into chapter-specific content.

   Example shape (substitute your project's mascot, voice, and pose set):

   ```markdown
   !!! mascot-welcome "Hi! I'm {Name}."
       <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="{Name} waves hello">
       Welcome to {Course}! I'm **{Name}**, {one-line character description with personality}. I'll be popping into the margins all the way through this book, but I do not show up randomly. I have exactly **{N} jobs**, and you'll learn to recognize me by which one I'm doing:

       1. **Welcome you** at the start of every chapter — that's what I'm doing right now.
       2. **Help you think things through** when an idea is the kind that {project-specific phrasing}.
       3. **Give you tips** — the moves a working {domain} pro would make that nobody writes down.
       4. **Warn you gently** about the places where smart students and smart projects get into trouble.
       5. **Encourage you** when a concept looks scary on first contact.
       6. **Celebrate with you** at the end of each chapter when you've earned it.

       That's it. If I'm not doing one of those six things, I'm not in the chapter. {Closing line in mascot voice.}
   ```

5. **Non-text elements:**
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

**CRITICAL: Every diagram, chart, infographic, MicroSim, timeline, map, workflow, and graph model MUST be interactive.** NEVER specify a static image that does not give the learner feedback. At minimum, every visual element must support at least one of: clickable nodes/regions/bars that open an infobox, hoverable elements that reveal tooltips, or controls that change the rendered output. Mermaid diagrams are acceptable ONLY when every node has a `click` directive that reveals a definition or explanation in an infobox — a plain Mermaid diagram with no click handlers is a static image and is forbidden. If a candidate diagram cannot meet this bar, redesign it as a MicroSim, an interactive infographic, or a clickable Mermaid diagram — or cut it. See `references/content-element-types.md` "CRITICAL RULE: Every Visual Element Must Be Interactive" for the full specification.

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
- For the per-level action-verb lists and detailed question-writing guidance, read the canonical reference `references/blooms-taxonomy.md` (also used by faq-generator and quiz-generator).

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

### Phase 3: Aggregation and Reporting (Sequential)

After content generation completes, aggregate results. In sequential mode,
collect the result after each chapter. In explicitly requested parallel mode,
wait for every Task agent before aggregating.

#### Step 3.1: Collect Agent Results

Collect for each completed chapter:
- List of chapter files created/updated
- Per-chapter statistics (word count, non-text elements, concepts covered)
- Any errors or issues encountered

#### Step 3.2: Generate Summary Report

Create a summary of all content generation:

```markdown
# Chapter Content Generation Report

Generated: YYYY-MM-DD
Execution Mode: [Sequential | Parallel (N agents, explicitly requested)]
Wall-clock Time: X minutes Y seconds

## Overall Statistics

- **Total Chapters:** 23
- **Total Words:** ~100,000
- **Avg Words per Chapter:** ~4,350
- **Total Non-text Elements:** ~115

## Execution Summary

| Chapter | Words | Elements | Time |
|---------|-------|----------|------|
| 1. Foundations | 4,200 | 20 | 3m 15s |
| 2. Limits | 4,500 | 22 | 3m 42s |
| ... | ... | ... | ... |

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

**Skill Version:** 0.09
**Date:** YYYY-MM-DD
**Execution Mode:** [Sequential | Parallel (N agents, explicitly requested)]

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
| Chapter generation | ~N |
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

"Chapter Content Generator v0.09 complete!

- **Mode:** [Sequential | Parallel (N agents, explicitly requested)]
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

9. **Scaffolding — the experience of reading:** Generate content that reads like a guided tutorial, not a reference document. Every non-text element (diagram, code block, table) should feel like a natural payoff of the prose that preceded it. Ask: "If a student reads linearly from top to bottom, will they have the vocabulary and context to understand each element when they reach it?" If not, add bridging prose before the element.

10. **Verification:** Always check that all concepts from "Concepts Covered" list appear in generated content

11. **Consistent style:** Maintain consistent voice, terminology, and visual style throughout chapter

12. **Execution mode:** Process chapters sequentially by default, regardless of
chapter count. Use parallel mode only after the user explicitly requests it and
receives the token-cost warning.

13. **Real timestamps:** Always use actual system timestamps, never synthetic data

14. **Emoji discipline:** Use emoji only when they signal a metaphor the chapter teaches. Decorative emoji compete with the textbook's mascot and the bold-and-define vocabulary pattern — leave them out. Per Mayer's coherence principle, decorative visuals measurably reduce retention even when students find them friendly. Engagement is not the same as learning.

15. **Mascot self-introduction in Chapter 1:** When the project CONTENT-GENERATION-GUIDE.md defines a mascot, the very first mascot admonition in Chapter 1 must introduce the mascot by name and enumerate every pose-role the mascot will play across the book. This is a one-time orientation that sets reader expectations, so chapters 2+ never need to re-explain the mascot. Skip this if no mascot is defined. See Step 2.4 principle 4 for the canonical pattern.

## Common Pitfalls to Avoid

**Dependency Direction (HIGHEST PRIORITY):**
- ❌ Building prereqs map with `prereqs[edge['to']].add(edge['from'])` -- this INVERTS all dependencies
- ❌ Skipping edge direction validation (Step 1.3a) -- an inverted map silently produces invalid chapters
- ❌ Proceeding with chapter generation when dependency violations exist (Step 1.3b)
- ✅ Always use `prereqs[edge['from']].add(edge['to'])` -- from=dependent, to=prerequisite
- ✅ Always verify foundational concepts look correct before proceeding
- ✅ Always confirm 0 dependency violations before generating any content

**Scaffolding (CRITICAL — reader experience):**
- ❌ Diagram uses terms (e.g., "vectors", "embeddings") that haven't been defined in preceding prose
- ❌ Code example contains parameters (e.g., `temperature`, `max_tokens`) explained only in a later section
- ❌ Table introduces new concepts instead of summarizing concepts already explained in prose
- ❌ Complex element appears without a bridging sentence ("Before we look at this diagram...")
- ✅ Every technical term in a non-text element is defined in the prose immediately before it
- ✅ Code examples are preceded by plain-language explanations of what the code does and what its parameters mean
- ✅ Tables reinforce and organize — they never introduce
- ✅ Navigation cues ("Let's define two terms before examining this diagram") guide the reader through transitions

**Mascot Usage:**
- ❌ Chapter 1's first mascot admonition skips the self-introduction and goes straight into chapter content
- ❌ Chapters 2+ repeat the mascot self-introduction (it should appear exactly once, in Chapter 1)
- ❌ Inventing pose-roles the project CONTENT-GENERATION-GUIDE.md does not define
- ❌ Treating the mascot as decoration rather than a signal (5–6 admonitions per chapter is the documented ceiling)
- ✅ Chapter 1's first mascot admonition is a self-introduction listing every pose-role the mascot plays
- ✅ Chapters 2+ open with a normal mascot-welcome that gets straight into content
- ✅ Mascot admonitions are spaced apart (never back-to-back) and earned, not decorative

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

**Execution Modes:**
- ❌ Switching to parallel execution because the request contains many chapters
- ❌ Treating an ordinary "all chapters" request as permission to spawn agents
- ✅ Process every ordinary request sequentially, one chapter at a time
- ✅ Use parallel execution only after an explicit request and token-cost warning
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

### Sequential Mode (Default)

**User:** "Generate content for all chapters"

**Claude (using this skill):**

1. Captures start time
2. Notifies: "Chapter Content Generator Skill v0.09 running in sequential mode."
3. Reads shared context (course description, learning graph, glossary, CONTENT-GENERATION-GUIDE.md)
4. Determines reading level (e.g., Senior High)
5. Scans chapter directories, finds 23 chapters needing content
6. Processes each chapter one at a time, completing and logging one before starting the next
7. Aggregates the per-chapter results
8. Captures end time
9. Writes session log
10. Reports: "Chapter Content Generator v0.09 complete! Mode: Sequential. Chapters: 23. Words: ~100,000."

### Parallel Mode (Explicit request example)

**User:** "Generate content for all chapters. Use parallel execution."

**Claude (using this skill):**

1. Warns that parallel execution uses approximately 38% additional tokens
2. Plans six chapter batches
3. Spawns six Task agents in a single message
4. Waits for every agent, then aggregates and reports the results

### Single Chapter Mode

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
