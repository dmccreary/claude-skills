# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a curated collection of Claude AI skills for creating intelligent, interactive educational textbooks. Each skill is an autonomous agent that automates specific aspects of educational content creation - from learning graph generation to interactive p5.js simulations (MicroSims).

The skills are designed for building **Level 2+ intelligent textbooks** using MkDocs with Material theme, following educational frameworks like Bloom's Taxonomy (2001), ISO 11179 metadata standards, and concept dependency graphs.

## Repository Structure

```
claude-skills/
├── skills/                          # Skill definitions (main directory)
│   ├── course-description-analyzer/ # Validates course descriptions
│   ├── faq-generator/              # Generates FAQs from course content
│   ├── glossary-generator/         # Creates ISO 11179-compliant glossaries
│   ├── intelligent-textbook/       # Complete textbook generation workflow
│   ├── intelligent-textbook-creator/# MkDocs Material textbook creator
│   ├── learning-graph-generator/   # Generates 200-concept learning graphs
│   │   ├── SKILL.md               # Skill definition and workflow
│   │   ├── analyze-graph.py       # Validates DAG structure and quality
│   │   ├── csv-to-json.py         # Converts CSV to vis-network JSON
│   │   ├── add-taxonomy.py        # Adds taxonomy column to CSV
│   │   └── taxonomy-distribution.py # Generates taxonomy reports
│   ├── microsim-p5/               # Creates p5.js educational simulations
│   ├── moving-rainbow/            # MicroPython for Raspberry Pi Pico
│   └── quiz-generator/            # Generates Bloom's Taxonomy-aligned quizzes
├── docs/                          # MkDocs documentation site
├── scripts/                       # Utility scripts
│   ├── install-claude-skills.sh  # Creates symlinks to ~/.claude/skills/
│   ├── list-skills.sh            # Lists available skills
│   └── list-skills-format.sh     # Outputs skills in various formats
├── commands/                      # Slash commands
│   └── skills.md                 # /skills command definition
└── mkdocs.yml                    # MkDocs configuration
```

**Key Directories:**
- **`skills/`**: Each subdirectory contains a SKILL.md file defining the skill's behavior, plus supporting files (Python scripts, templates, reference docs)
- **`docs/`**: Documentation site built with MkDocs Material theme, deployed to GitHub Pages

## Architecture Patterns

### Skill System

Skills are autonomous agents loaded by Claude Code. Each skill:
1. Is defined by a `SKILL.md` file with YAML frontmatter containing `name:`, `description:`, `license:`, and optional `allowed-tools:`
2. Contains workflow instructions that Claude executes step-by-step
3. May include supporting assets (Python scripts, templates, reference documents)
4. Is designed to be invoked with `/skill [skill-name]` or through the Skill tool

### Learning Graph Architecture

The learning graph generator follows this data flow:

```
course-description.md
  → concept enumeration (200 concepts)
  → dependency mapping (CSV with DAG structure)
  → quality validation (Python: analyze-graph.py)
  → taxonomy categorization (12 categories)
  → JSON conversion (vis-network format for visualization)
```

**Critical constraint**: Dependency graphs must be **Directed Acyclic Graphs (DAGs)** - no circular dependencies allowed.

### MicroSim Pattern

MicroSims are interactive p5.js simulations stored in `docs/sims/[sim-name]/`:
- `main.html` - Standalone p5.js simulation
- `index.md` - Documentation page with iframe embed
- Each simulation focuses on one educational concept
- Uses seeded randomness for reproducibility
- Includes interactive controls (sliders, buttons)

### Intelligent Textbook Workflow

The `intelligent-textbook` skill orchestrates a 12-step process:
1. Course Description Development → 2. Bloom's Taxonomy Integration → 3. Concept Enumeration (250 concepts) → 4. Concept Dependencies (DAG) → 5. Concept Taxonomy → 6. Learning Graph Visualization → 7. Chapters/Sections Structure → 8. Content Generation → 9. MicroSim Creation → 10. Site Assembly → 11. Quality Assurance → 12. Deployment

This workflow is documented in detail in `skills/intelligent-textbook/SKILL.md`.

## Common Development Tasks

### Working with Skills

**List available skills:**
```bash
./scripts/list-skills.sh
# or
./scripts/list-skills-format.sh json  # outputs JSON
```

**Install skills globally (for all projects):**
```bash
cd scripts
./install-claude-skills.sh
```
This creates symlinks from `./skills/*` to `~/.claude/skills/`

**Install skills for a single project:**
Edit `install-claude-skills.sh` and change:
```bash
$HOME  # from ~/.claude/skills
# to:
/path/to/project/.claude/skills
```

### Working with Documentation

**Build and serve the documentation site:**
```bash
mkdocs serve
# Opens at http://localhost:8000
```

**Build for production:**
```bash
mkdocs build --strict
```

**Deploy to GitHub Pages:**
```bash
mkdocs gh-deploy
```

### Working with Learning Graphs

When the learning-graph-generator skill creates files in `/docs/learning-graph/`, you must:

1. **Run Python scripts in the learning-graph directory:**
```bash
cd docs/learning-graph
python analyze-graph.py learning-graph.csv quality-metrics.md
python csv-to-json.py learning-graph.csv learning-graph.json
python taxonomy-distribution.py learning-graph.csv taxonomy-distribution.md
```

2. **Update mkdocs.yml navigation** to include new files:
```yaml
nav:
  - Learning Graph:
    - Introduction: learning-graph/index.md
    - Course Description Assessment: learning-graph/course-description-assessment.md
    - Concept Enumeration: learning-graph/list-concepts.md
    - Graph Quality Analysis: learning-graph/quality-metrics.md
```

3. **Always verify** `learning-graph.json` is valid JSON before using in visualizations

## Educational Frameworks

### Bloom's Taxonomy (2001 Revision)

All content generation follows the six cognitive levels:
1. **Remember** (Red) - Define, list, recall, identify
2. **Understand** (Orange) - Summarize, explain, classify
3. **Apply** (Yellow) - Implement, solve, use
4. **Analyze** (Green) - Differentiate, compare, organize
5. **Evaluate** (Blue) - Judge, critique, assess
6. **Create** (Purple) - Design, construct, develop

### ISO 11179 Standards (Glossary Definitions)

Glossary terms must be:
- **Precise** - Exact meaning without ambiguity
- **Concise** - Minimal words needed
- **Distinct** - Unique from related terms
- **Non-circular** - Don't define terms using themselves
- **Free of business rules** - No implementation details

### Five Levels of Textbook Intelligence

- **Level 1**: Static text and images
- **Level 2**: Hyperlinked content with navigation (MkDocs default)
- **Level 3**: Interactive elements and quizzes
- **Level 4**: Adaptive content based on learner progress
- **Level 5**: AI-powered personalization

This repository targets Level 2 by default, with support for Level 3 through MicroSims and quizzes.

## Data Format Specifications

### Learning Graph CSV Format

```csv
ConceptID,ConceptLabel,Dependencies,TaxonomyID
1,Introduction to Programming,,FOUND
2,Variables and Data Types,1,BASIC
3,Control Flow,1|2,BASIC
```

- **ConceptID**: Integer (1-200)
- **ConceptLabel**: Title Case, max 32 characters
- **Dependencies**: Pipe-delimited list of ConceptIDs (empty for foundational concepts)
- **TaxonomyID**: 3-5 letter abbreviation for category

### vis-network JSON Format

The `csv-to-json.py` script converts learning graphs to vis-network format:
```json
{
  "nodes": [
    {"id": 1, "label": "Concept Name", "group": "TAXID"}
  ],
  "edges": [
    {"from": 1, "to": 2}
  ]
}
```

## Important Conventions

### Markdown Generation

**Always place a blank line before markdown lists** - required by MkDocs:
```markdown
Here is a list:

- Item 1
- Item 2
```

### Concept Labels

- Use **Title Case**
- Maximum **32 characters**
- Avoid acronyms unless necessary for brevity
- Each concept should be atomic (single, clear idea)

### File Naming

- Skills use kebab-case: `learning-graph-generator`
- Markdown files use kebab-case: `course-description.md`
- Python scripts use snake_case but are typically: `analyze-graph.py`

### Navigation Updates

After adding any `.md` file to `docs/`, update the `nav:` section in `mkdocs.yml` so it appears in the site navigation.

## Quality Standards

### Learning Graph Quality Metrics

A high-quality learning graph should have:
- Quality score ≥ 70/100
- Zero circular dependencies (must be a DAG)
- Foundational concepts with zero dependencies
- No orphaned nodes (concepts nothing depends on)
- Average 2-4 dependencies per concept
- No single taxonomy category exceeding 30% of concepts
- All concepts connected to the main graph

### Content Quality Standards

Generated content should:
- Respect concept dependencies (prerequisites taught first)
- Address multiple Bloom's levels
- Include worked examples (2-3 per section)
- Provide practice exercises (5-8 per section)
- Use clear markdown formatting with admonitions
- Maintain encouraging, accessible tone

## Website

**Documentation**: https://dmccreary.github.io/claude-skills/
**Repository**: https://github.com/dmccreary/claude-skills

## Technology Stack

- **MkDocs** with **Material for MkDocs** theme - static site generation
- **p5.js** - interactive simulations (MicroSims)
- **vis-network.js** - learning graph visualization
- **Python** - data processing scripts
- **GitHub Pages** - hosting
- **Bash** - utility scripts
