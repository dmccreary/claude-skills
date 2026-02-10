---
name: microsim-generator
description: Creates interactive educational MicroSims using the best-matched JavaScript library (p5.js, Chart.js, Plotly, Mermaid, vis-network, vis-timeline, Leaflet, Venn.js). Analyzes user requirements to route to the appropriate visualization type and generates complete MicroSim packages with HTML, JavaScript, CSS, documentation, and metadata.
---

# MicroSim Generator

## Overview

This meta-skill routes MicroSim creation requests to the appropriate specialized generator based on visualization requirements. It consolidates 14 individual MicroSim generator skills into a single entry point with on-demand loading of specific implementation guides.

Five Python batch utilities in `src/microsim-utils/` automate the repetitive parts of MicroSim generation (parsing specs, scaffolding files, inserting iframes, validating quality, updating navigation), saving ~430K tokens per batch run. The agent's creative work is focused on writing the `.js` file.

## When to Use This Skill

Use this skill when users request:

- Interactive educational visualizations
- Data visualizations (charts, graphs, plots)
- Timelines or chronological displays
- Geographic/map visualizations
- Network diagrams or concept maps
- Flowcharts or workflow diagrams
- Mathematical function plots
- Set diagrams (Venn)
- Priority matrices or bubble charts
- Custom simulations or animations
- Comparison tables with ratings
- Matrix comparisons with expandable cell details
- Batch generation of MicroSims for a chapter

---

## Step 0: Environment Setup

Before any generation work, establish paths and determine scope.

### 0.1 Set Paths

```bash
# Python utilities live in the claude-skills repo
UTILS="$HOME/Documents/ws/claude-skills/src/microsim-utils"

# Detect project root (directory containing mkdocs.yml)
PROJECT=$(python3 -c "
import os, sys
d = os.path.abspath('.')
while d != os.path.dirname(d):
    if os.path.isfile(os.path.join(d, 'mkdocs.yml')): print(d); sys.exit()
    d = os.path.dirname(d)
print('ERROR: mkdocs.yml not found', file=sys.stderr); sys.exit(1)
")
```

If the scripts are not found at `$UTILS`, check for them in the project's own `src/microsim-utils/` directory.

### 0.2 Determine Scope

| User Request | Route |
|-------------|-------|
| "Generate MicroSims for chapter 11" | **Chapter batch** → Step 1 |
| "Create a MicroSim for inscribed angles" | **Single sim** → Step 1B |
| "Build a timeline of Unix history" | **Single sim** → Step 1B |

---

## Step 1: Extract Specs from Chapter (Batch Route)

**MANDATORY for chapter-level generation.** Do NOT manually parse chapter markdown.

```bash
python3 $UTILS/extract-sim-specs.py \
    --project-dir $PROJECT \
    --chapter <chapter-dir-name> \
    --output /tmp/ch-specs.json \
    --status-file /tmp/sim-status.json \
    --verbose
```

**What this does:**

- Parses all `#### Diagram:` and `#### Drawing:` headers from the chapter's `index.md`
- Extracts `<details>` block content, iframe paths, sim IDs, Bloom levels, and library hints
- Produces a JSON array of spec objects (one per sim)
- Generates a `sim-status.json` with lifecycle states: `specified → scaffolded → implemented → validated → deployed`

**Read the output:**

```bash
cat /tmp/ch-specs.json | python3 -m json.tool | head -60
```

Check the status file to see which sims need work:

```bash
python3 -c "
import json
with open('/tmp/sim-status.json') as f:
    for e in json.load(f):
        if e['status'] != 'deployed':
            print(f\"  {e['status']:12s}  {e['sim_id']}\")
"
```

After extracting, proceed to **Step 2**.

---

## Step 1B: Single-Sim Shortcut

For a single MicroSim request (not a full chapter batch):

1. **Write a 1-entry spec JSON** manually:

```bash
cat > /tmp/ch-specs.json << 'EOF'
[{
    "sim_id": "inscribed-angle-theorem",
    "title": "Central vs Inscribed Angles Interactive",
    "summary": "Demonstrates the inscribed angle theorem",
    "heading_type": "Diagram",
    "chapter": "",
    "element_type": "microsim",
    "bloom_level": "Analyze",
    "library": "p5.js",
    "iframe_src": "",
    "iframe_height": "",
    "spec_text": "",
    "status": ""
}]
EOF
```

2. **Run scaffold** for just that sim:

```bash
python3 $UTILS/generate-sim-scaffold.py \
    --spec-file /tmp/ch-specs.json \
    --sim-id inscribed-angle-theorem \
    --project-dir $PROJECT \
    --verbose
```

3. **Jump to Step 3** (Instructional Design Checkpoint), then **Step 4** (Implement .js).

---

## Step 2: Scaffold Sim Directories

**MANDATORY for batch generation.** Do NOT manually create main.html, index.md, or metadata.json.

```bash
python3 $UTILS/generate-sim-scaffold.py \
    --spec-file /tmp/ch-specs.json \
    --project-dir $PROJECT \
    --verbose
```

**What this does:**

- Creates `docs/sims/<sim-id>/` directory for each spec
- Generates `main.html` with correct CDN links, `<main>` tag, and schema meta tag
- Generates `index.md` with frontmatter, iframe embed, fullscreen link, lesson plan skeleton
- Generates `metadata.json` with Dublin Core fields and educational metadata
- **Skips** directories that already exist (unless `--force` is used)

**Using `--force` for partially-built sims:**

When sim directories exist (with main.html + .js) but lack index.md or metadata.json, the scaffold script skips the entire directory by default. Use `--force` to regenerate all scaffold files. This is safe because the creative work lives in the `.js` file, which the scaffold never overwrites.

```bash
python3 $UTILS/generate-sim-scaffold.py \
    --spec-file /tmp/ch-specs.json \
    --project-dir $PROJECT \
    --force \
    --verbose
```

**After scaffolding, the agent ONLY writes .js files from here on.**

---

## Step 3: Instructional Design Checkpoint (MANDATORY)

**Before writing any .js file, you MUST complete this checkpoint.**

### 3.1 Identify Learning Objective Details

Extract from the specification:
- **Bloom Level**: Remember, Understand, Apply, Analyze, Evaluate, or Create
- **Bloom Verb**: The action verb (explain, demonstrate, calculate, etc.)
- **Learning Objective**: The full statement of what learners will be able to do

### 3.2 Match Interaction Pattern to Bloom Level

| Bloom Level | Appropriate Patterns | Inappropriate Patterns |
|-------------|---------------------|------------------------|
| Remember (L1) | Flashcards, matching, labeling | Complex simulations |
| **Understand (L2)** | **Step-through worked examples, concrete data visibility** | **Continuous animation, particle effects** |
| Apply (L3) | Parameter sliders, calculators, practice problems | Passive viewing only |
| Analyze (L4) | Network explorers, comparison tools, pattern finders | Pre-computed results |
| Evaluate (L5) | Sorting/ranking activities, rubric tools | No feedback mechanisms |
| Create (L6) | Builders, editors, canvas tools | Rigid templates |

### 3.3 Answer These Questions

Before proceeding, answer these questions:

1. **What specific data must the learner SEE?**
   - Not "animated particles" but "the tokenized array ['physics', 'ball']"

2. **Does the learner need to PREDICT before observing?**
   - If YES → Use step-through with Next/Previous buttons
   - If YES → Do NOT use continuous animation

3. **What does animation add that static arrows don't?**
   - If you can't answer this clearly → Don't use animation

4. **Is continuous animation appropriate for this Bloom level?**
   - For Understand (L2) with verb "explain" → Almost always NO
   - For Apply (L3) with real-time feedback → Often YES

### 3.4 Modify Specification If Needed

If the specification requests animation/effects for an UNDERSTAND level objective:
- **Flag this as a potential instructional design issue**
- **Recommend step-through pattern instead**
- **Ask user**: "The specification requests animation, but for an 'explain' objective, a step-through approach with concrete data visibility typically supports learning better. Should I proceed with step-through instead?"

### 3.5 Document Your Decision

Add to your response:
```
Instructional Design Check:
- Bloom Level: [level]
- Bloom Verb: [verb]
- Recommended Pattern: [pattern]
- Specification Alignment: [aligned/modified]
- Rationale: [why this pattern supports the learning objective]
```

---

## Step 4: Implement .js Files

This is where the agent's creative work happens. For each sim that needs implementation:

### 4.1 Analyze Request and Match Generator

Scan the spec for trigger keywords and match to the appropriate generator guide.

#### Quick Reference Routing Table

| Trigger Keywords | Guide File | Library |
|------------------|------------|---------|
| timeline, dates, chronological, events, history, schedule, milestones | `references/timeline-guide.md` | vis-timeline |
| map, geographic, coordinates, latitude, longitude, locations, markers | `references/map-guide.md` | Leaflet.js |
| function, f(x), equation, plot, calculus, sine, cosine, polynomial | `references/plotly-guide.md` | Plotly.js |
| network, nodes, edges, graph, dependencies, concept map, knowledge graph | `references/vis-network-guide.md` | vis-network |
| flowchart, workflow, process, state machine, UML, sequence diagram | `references/mermaid-guide.md` | Mermaid.js |
| venn, sets, overlap, intersection, union, categories | `references/venn-guide.md` | Custom |
| chart, bar, line, pie, doughnut, radar, statistics, data | `references/chartjs-guide.md` | Chart.js |
| bubble, priority, matrix, quadrant, impact vs effort, risk vs value | `references/bubble-guide.md` | Chart.js |
| causal, feedback, loop, systems thinking, reinforcing, balancing | `references/causal-loop-guide.md` | vis-network |
| comparison, table, ratings, stars, side-by-side, features | `references/comparison-table-guide.md` | Custom |
| matrix, framework comparison, clickable cells, detail panel, expandable | `references/html-table.md` | Custom |
| animation, celebration, particles, confetti, effects | `references/celebration-guide.md` | p5.js |
| custom, simulation, physics, interactive, bouncing, movement, p5.js | `references/p5-guide.md` | p5.js |

#### Decision Tree

```
Has dates/timeline/chronological events?
  → YES: timeline-guide.md

Has geographic coordinates/locations?
  → YES: map-guide.md

Mathematical function f(x) or equation?
  → YES: plotly-guide.md

Nodes and edges/network relationships?
  → YES: vis-network-guide.md (or causal-loop-guide.md if systems thinking)

Flowchart/workflow/process diagram?
  → YES: mermaid-guide.md

Sets with overlaps (2-4 categories)?
  → YES: venn-guide.md

Priority matrix/2x2 quadrant/multi-dimensional?
  → YES: bubble-guide.md

Standard chart (bar/line/pie/radar)?
  → YES: chartjs-guide.md

Comparison table with ratings/stars?
  → YES: comparison-table-guide.md

Matrix comparison with clickable cells/detail panels?
  → YES: html-table.md

Celebration/particles/visual feedback?
  → YES: celebration-guide.md

Custom simulation/animation/physics?
  → YES: p5-guide.md
```

### 4.2 Load the Matched Guide

**Read the corresponding guide file** from the `references/` directory and follow its workflow for writing the `.js` file.

### 4.3 Write ONLY the .js File

The scaffold (Step 2) already created `main.html`, `index.md`, and `metadata.json`. You only need to write `docs/sims/<sim-id>/<sim-id>.js`.

Each guide contains:
1. Library-specific requirements
2. Code templates and patterns
3. Best practices for that visualization type

### 4.4 Handling Ambiguous Requests

If the request could match multiple generators:

1. **Read `references/routing-criteria.md`** for detailed scoring methodology
2. **Score top 3 candidates** using the 0-100 scale
3. **Present options to user** with reasoning:
   ```
   Based on your request, I recommend:
   1. [Generator A] (Score: 85) - Best for [reason]
   2. [Generator B] (Score: 70) - Alternative if you need [feature]
   3. [Generator C] (Score: 55) - Possible if [condition]

   Which would you prefer?
   ```
4. **Proceed with user's selection**

#### Common Ambiguities

| Ambiguous Term | Clarification Needed |
|----------------|---------------------|
| "graph" | Chart (ChartJS) or Network graph (vis-network)? |
| "diagram" | Structural (Mermaid), Network (vis-network), or Custom (p5)? |
| "map" | Geographic (Leaflet) or Concept map (vis-network)? |
| "table" | Star ratings (comparison-table) or Clickable cells with detail panels (html-table)? |
| "visualization" | What type of data? What interaction needed? |

---

## Step 5: Fix Chapter Iframes

**MANDATORY for batch generation.** Do NOT manually insert or edit iframes in chapter markdown.

```bash
python3 $UTILS/add-iframes-to-chapter.py \
    --chapter <chapter-dir-name> \
    --project-dir $PROJECT \
    --fix-heights \
    --fix-paths \
    --verbose
```

**What this does:**

- Finds `#### Diagram:` / `#### Drawing:` headers that are missing iframe embeds
- Inserts `<iframe>` tags before the `<details>` block with correct relative paths
- `--fix-heights`: Parses `.js` files to detect `createCanvas()` height and sets iframe height to canvas height + 2px
- `--fix-paths`: Converts absolute paths (`/sims/...`) to relative (`../../sims/...`)
- Fixes height typos (`500xp` → `500px`)

**For all chapters at once:**

```bash
python3 $UTILS/add-iframes-to-chapter.py \
    --all \
    --project-dir $PROJECT \
    --fix-heights \
    --fix-paths \
    --verbose
```

**Dry-run first** to preview changes:

```bash
python3 $UTILS/add-iframes-to-chapter.py \
    --chapter <chapter-dir-name> \
    --project-dir $PROJECT \
    --fix-heights --fix-paths \
    --dry-run --verbose
```

---

## Step 6: Validate Quality

**MANDATORY after implementing .js files.** Do NOT rely on a manual checklist.

```bash
python3 $UTILS/validate-sims.py \
    --project-dir $PROJECT \
    --format table \
    --verbose
```

**What this does:**

Scores each MicroSim on a 100-point rubric:

| Category | Points | Checks |
|----------|--------|--------|
| main.html | 10 | Exists (5), schema meta tag (3), `<main>` tag (2) |
| metadata.json | 30 | Present (10), required fields (10), educational (5), pedagogical (5) |
| index.md | 35 | Title (2), YAML (3), images (5), iframe (10), fullscreen (5), example (5), description (5) |
| Screenshot | 5 | PNG file exists |
| Lesson Plan | 10 | Section present in index.md |
| References | 5 | Section present in index.md |
| p5.js conventions | 5 | updateCanvasSize, no DOM buttons, querySelector parenting |

**Grade scale:** A (85+), B (70-84), C (50-69), D (<50)

**Validate a single sim:**

```bash
python3 $UTILS/validate-sims.py \
    --project-dir $PROJECT \
    --sim <sim-id> \
    --verbose
```

**Fix issues found, then re-validate** to confirm improvements:

```bash
# After fixing issues...
python3 $UTILS/validate-sims.py \
    --project-dir $PROJECT \
    --min-score 0 \
    --format table \
    --verbose
```

---

## Step 7: Update Navigation

**MANDATORY after creating new sims.** Do NOT manually edit the MicroSims section of mkdocs.yml.

```bash
python3 $UTILS/update-mkdocs-nav.py \
    --project-dir $PROJECT \
    --verbose
```

**What this does:**

- Scans `docs/sims/` for directories containing `index.md`
- Extracts display titles from frontmatter or `# Heading`
- Replaces the entire `- MicroSims:` section in `mkdocs.yml` with an alphabetically sorted list
- Idempotent and safe to run multiple times

**Dry-run first:**

```bash
python3 $UTILS/update-mkdocs-nav.py \
    --project-dir $PROJECT \
    --dry-run --verbose
```

---

## Workflow Summary

### Batch (Chapter-Level) Generation

```
Step 0: Set UTILS and PROJECT paths
  ↓
Step 1: extract-sim-specs.py → /tmp/ch-specs.json
  ↓
Step 2: generate-sim-scaffold.py → creates main.html, index.md, metadata.json
  ↓
Step 3: Instructional Design Checkpoint (per sim)
  ↓
Step 4: Write .js files (creative work — route to guide, implement)
  ↓
Step 5: add-iframes-to-chapter.py → inserts/fixes iframes
  ↓
Step 6: validate-sims.py → scores quality, fix issues
  ↓
Step 7: update-mkdocs-nav.py → regenerates nav
```

### Single Sim Generation

```
Step 0:  Set UTILS and PROJECT paths
  ↓
Step 1B: Write 1-entry spec JSON + scaffold
  ↓
Step 3:  Instructional Design Checkpoint
  ↓
Step 4:  Write .js file
  ↓
Step 6:  validate-sims.py --sim <name>
  ↓
Step 7:  update-mkdocs-nav.py
```

### Resuming After Context Window Fills

When a batch run fills the context window mid-chapter:

1. The new session reads `sim-status.json` to see what's done
2. Sims in `implemented` or later status are skipped
3. Sims in `specified` or `scaffolded` status still need .js files

```bash
# Check where we left off
python3 $UTILS/extract-sim-specs.py \
    --project-dir $PROJECT \
    --chapter <chapter-dir-name> \
    --status-file /tmp/sim-status.json \
    --verbose
```

---

## Available Generators

### Primary Generators

| Generator | Library | Best For |
|-----------|---------|----------|
| p5-guide | p5.js | Custom simulations, physics, animations |
| chartjs-guide | Chart.js | Bar, line, pie, doughnut, radar charts |
| timeline-guide | vis-timeline | Chronological events, history, schedules |
| map-guide | Leaflet.js | Geographic data, locations, routes |
| vis-network-guide | vis-network | Network graphs, dependencies, concept maps |
| mermaid-guide | Mermaid.js | Flowcharts, workflows, UML diagrams |
| plotly-guide | Plotly.js | Mathematical function plots |
| venn-guide | Custom | Set relationships (2-4 sets) |
| bubble-guide | Chart.js | Priority matrices, multi-dimensional data |
| causal-loop-guide | vis-network | Systems thinking, feedback loops |
| comparison-table-guide | Custom | Side-by-side comparisons with ratings |
| html-table | Custom | Matrix comparisons with clickable cells, detail panels |
| celebration-guide | p5.js | Particle effects, visual feedback |

### Shared Standards

All MicroSims follow these standards regardless of generator:

**Directory Structure:**
```
docs/sims/<microsim-name>/
├── main.html       # Main visualization file
├── index.md        # Documentation page
├── *.js or *.css   # Supporting files
└── metadata.json   # Dublin Core metadata (optional)
```

**URI Scheme for Discoverability:**

All MicroSim HTML files MUST include this schema meta tag for global discoverability:

```html
<meta name="schema" content="https://dmccreary.github.io/intelligent-textbooks/ns/microsim/v1">
```

This enables counting and discovery of MicroSims across GitHub using code search. See the [URI Scheme documentation](https://dmccreary.github.io/intelligent-textbooks/uri-scheme/) for details.

**Integration:**
- Embedded via iframe in MkDocs pages
- Width-responsive design
- Non-scrolling iframe container
- Standard height: drawHeight + controlHeight + 2px
- **Iframe paths MUST always be relative, NEVER absolute:**
  - From a sim's own `index.md`: `<iframe src="main.html" ...>`
  - From chapter files (`docs/chapters/*/index.md`): `<iframe src="../../sims/[sim-name]/main.html" ...>`
  - **NEVER use absolute paths** like `/sims/...` — they break on GitHub Pages where the site is served under a subdirectory (e.g., `/geometry-course/`)

**Quality Checklist:**
- [ ] Runs without errors in modern browsers
- [ ] Responsive to container width
- [ ] Controls respond immediately
- [ ] Educational purpose is clear
- [ ] Code is well-commented

## Examples

### Example 1: Timeline Request
**User:** "Create a timeline showing key events in computer history"
**Routing:** Keywords "timeline", "events", "history" → `references/timeline-guide.md`
**Action:** Read timeline-guide.md and follow its workflow

### Example 2: Chart Request
**User:** "Make a bar chart comparing programming language popularity"
**Routing:** Keywords "bar chart", "comparing" → `references/chartjs-guide.md`
**Action:** Read chartjs-guide.md and follow its workflow

### Example 3: Custom Simulation
**User:** "Build an interactive bouncing ball simulation"
**Routing:** Keywords "interactive", "bouncing", "simulation" → `references/p5-guide.md`
**Action:** Read p5-guide.md and follow its workflow

### Example 4: Ambiguous Request
**User:** "Create a graph of our project dependencies"
**Routing:** "graph" + "dependencies" suggests network → `references/vis-network-guide.md`
**Action:** Read vis-network-guide.md (but clarify if user meant a chart)

### Example 5: Chapter Batch
**User:** "Generate MicroSims for chapter 11"
**Action:** Step 0 → Step 1 → Step 2 → Step 3-4 (loop per sim) → Step 5 → Step 6 → Step 7

## Reference Files

For detailed information, consult:

- `references/routing-criteria.md` - Complete scoring methodology for all generators
- `references/<generator>-guide.md` - Specific implementation guide for each generator
- `assets/templates/` - Shared templates and patterns

## sim-status.json Lifecycle

The `extract-sim-specs.py --status-file` flag generates a lifecycle tracking file. States progress as:

| Status | Meaning |
|--------|---------|
| **specified** | Has spec in chapter but no sim directory yet |
| **scaffolded** | Directory with main.html/index.md but no substantive JS |
| **implemented** | JS file exists and >50 lines |
| **validated** | quality_score >= 70 |
| **deployed** | Validated + iframe present in chapter |
