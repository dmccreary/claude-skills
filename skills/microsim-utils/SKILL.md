---
name: microsim-utils
description: Utility tools for MicroSim management including quality validation, screenshot capture, icon management, index page generation, and iframe height synchronization. Routes to the appropriate utility based on the task needed.
---

# MicroSim Utilities

## Overview

This meta-skill provides utility functions for managing and maintaining MicroSims in intelligent textbook projects. It consolidates four utility skills into a single entry point with on-demand loading of specific utility guides.

## When to Use This Skill

Use this skill when users request:

- Validating MicroSim quality and standards
- Capturing screenshots for preview images
- Adding or managing icons for MicroSims
- Generating index pages for MicroSim directories
- Quality scoring and standardization checks
- Synchronizing iframe heights from JS source files

## Step 1: Identify Utility Type

Match the user's request to the appropriate utility guide:

### Routing Table

| Trigger Keywords | Guide File | Purpose |
|------------------|------------|---------|
| standardize, quality, validate, score, check, audit | `references/standardization.md` | Quality validation and scoring |
| screenshot, capture, preview, image, thumbnail | `references/screen-capture.md` | Automated screenshot generation |
| icons, add icons, favicon, logo | `references/add-icons.md` | Icon management for MicroSims |
| index page, microsim list, grid, directory, catalog, update the microsim listings, update the list of microsims, create a grid view, generate a listing | `references/index-generator.md` | Generate index page with grid cards |
| TODO, todo json, extract specs, diagram specs, unimplemented, create microsim todo, todo files, extract diagrams, unimplemented microsims | `scripts/create-microsim-todo-json-files.py` | Extract unimplemented diagram specs into TODO JSON files |
| fix iframe heights, sync iframe heights, correct iframe heights, iframe height, canvas height, sync heights, update iframe heights | `scripts/sync-iframe-heights.py` | Synchronize iframe heights from CANVAS_HEIGHT in JS files to sim and chapter index.md files |

### Decision Tree

```
Need to check MicroSim quality/standards?
  → YES: standardization.md

Need to capture screenshots for previews?
  → YES: screen-capture.md

Need to add or manage icons?
  → YES: add-icons.md

Need to generate/update the MicroSim index page?
  → YES: index-generator.md

Need to extract unimplemented diagram specs into TODO files?
  → YES: Run scripts/create-microsim-todo-json-files.py

Need to fix, sync, or correct iframe heights?
  → YES: Run scripts/sync-iframe-heights.py
```

## Step 2: Load the Matched Guide or Run the Script

For reference-based utilities, read the corresponding guide file from `references/` and follow its workflow.

For Python script utilities, run the script directly:

**TODO JSON extractor:**
```bash
python /path/to/skills/microsim-utils/scripts/create-microsim-todo-json-files.py --project-dir /path/to/project
```
Report the summary output to the user (chapters scanned, total specs found, already implemented, TODO files written, output directory).

**Iframe height sync:**
```bash
python /path/to/skills/microsim-utils/scripts/sync-iframe-heights.py --project-dir /path/to/project --verbose
```
Report the summary output to the user (sims synced, CANVAS_HEIGHT comments inserted, iframe heights updated).

## Step 3: Execute Utility

Each guide contains:
1. Purpose and use cases
2. Prerequisites
3. Step-by-step workflow
4. Output format
5. Best practices

## Available Utilities

### standardization.md

**Purpose:** Validate MicroSim quality against standards

**Checks:**
- Required file presence (main.html, index.md)
- Code structure and patterns
- Accessibility features
- Documentation completeness
- Responsive design implementation

**Output:** Quality score (0-100) with recommendations

### screen-capture.md

**Purpose:** Capture high-quality screenshots for social media previews

**Script:** `~/.local/bin/bk-capture-screenshot <microsim-directory-path>`

**Features:**
- Uses Chrome headless mode with localhost server
- Handles JavaScript-heavy visualizations (p5.js, vis-network, Chart.js)
- Waits 3 seconds for proper rendering
- Creates consistent 1200x800 image sizes

**Output:** PNG screenshot named `{microsim-name}.png` in MicroSim directory

### add-icons.md

**Purpose:** Add favicon and icons to MicroSim directories

**Creates:**
- favicon.ico
- apple-touch-icon.png
- Other platform-specific icons

### index-generator.md

**Purpose:** Generate comprehensive MicroSim index page

**Creates:**
- Grid-based card layout
- Screenshots for each MicroSim
- Alphabetically sorted entries
- MkDocs Material card format
- Updates mkdocs.yml navigation

### create-microsim-todo-json-files.py

**Purpose:** Extract unimplemented MicroSim diagram specifications from chapter content and create TODO JSON files

**Script:** `scripts/create-microsim-todo-json-files.py --project-dir /path/to/project`

**How it works:**
- Scans all `docs/chapters/*/index.md` files for `#### Diagram:` headers
- Extracts sim-id, library, Bloom level, learning objective, and full specification from `<details>` blocks
- Skips any sim-id that already has a directory with `main.html` under `docs/sims/`
- Writes one JSON file per unimplemented diagram to `docs/sims/TODO/`

**Output:** Individual JSON files in `docs/sims/TODO/{sim-id}.json` with fields:
- `sim_id`, `diagram_name`, `chapter_number`, `chapter_title`
- `library`, `bloom_level`, `bloom_verb`, `learning_objective`
- `completion_status: "specified"`, `extracted_date`, `specification`

**Important:** Always pass `--project-dir` pointing to the project root (the directory containing `mkdocs.yml`). If omitted, the script walks up from its own location to find `mkdocs.yml`, which may find the wrong project.

### sync-iframe-heights.py

**Purpose:** Synchronize iframe heights across MicroSim index.md files and chapter files using the `CANVAS_HEIGHT` comment in each sim's JavaScript file as the single source of truth.

**Script:** `scripts/sync-iframe-heights.py --project-dir /path/to/project`

**How it works:**
- Reads `// CANVAS_HEIGHT: <int>` from the first 15 lines of each sim's `.js` file
- If the comment is missing, computes CANVAS_HEIGHT from `drawHeight + controlHeight` (+ `graphHeight` if present) and **inserts** the comment on line 2 of the JS file
- Sets iframe height = `CANVAS_HEIGHT + 2` (2px for iframe border) in:
  - The sim's own `docs/sims/<sim-id>/index.md`
  - Any chapter file (`docs/chapters/*/index.md`) that embeds the sim
- Reports all changes with colored output

**Flags:**
- `--project-dir` — Project root containing `mkdocs.yml` (required or auto-detected)
- `--sim <sim-id>` — Sync a single sim instead of all
- `--dry-run` — Preview changes without writing files
- `--verbose` — Show status for all sims, not just changes

**Output:** Summary showing sims synced, CANVAS_HEIGHT comments inserted, and iframe heights updated.

**Important:** Always pass `--project-dir` pointing to the project root. The script auto-detects by walking up from cwd to find `mkdocs.yml` if omitted.

## Examples

### Example 1: Quality Check
**User:** "Check if my bouncing-ball MicroSim meets standards"
**Routing:** Keywords "check", "standards" → `references/standardization.md`
**Action:** Read standardization.md and follow its workflow

### Example 2: Capture Screenshot
**User:** "Create a preview image for the timeline MicroSim"
**Routing:** Keywords "preview", "image" → `references/screen-capture.md`
**Action:** Run `~/.local/bin/bk-capture-screenshot /path/to/docs/sims/timeline`

### Example 3: Update Index
**User:** "Update the MicroSim index page with all new sims"
**Routing:** Keywords "index", "update" → `references/index-generator.md`
**Action:** Read index-generator.md and follow its workflow

### Example 4: Create TODO JSON Files
**User:** "Create MicroSim TODO JSON files"
**Routing:** Keywords "TODO", "create microsim todo" → `scripts/create-microsim-todo-json-files.py`
**Action:** Run `python scripts/create-microsim-todo-json-files.py --project-dir /path/to/project` and report results (chapters scanned, specs found, already implemented, TODO files written)

### Example 5: Fix Iframe Heights
**User:** "fix the iframe heights" or "sync the iframe heights" or "correct the iframe heights"
**Routing:** Keywords "fix iframe heights", "sync iframe heights", "correct iframe heights" → `scripts/sync-iframe-heights.py`
**Action:** Run `python scripts/sync-iframe-heights.py --project-dir /path/to/project --verbose` and report results (sims synced, comments inserted, iframe heights updated)

## Common Workflows

### After Creating New MicroSim
1. Run `standardization.md` to validate quality
2. Run `~/.local/bin/bk-capture-screenshot <microsim-path>` to create preview image
3. Run `index-generator.md` to add to index page

### Bulk Quality Audit
Use `standardization.md` to audit all MicroSims in a project and generate a quality report.

## Integration Notes

These utilities work with the standard MicroSim directory structure:
```
docs/sims/<microsim-name>/
├── main.html       # Main visualization
├── index.md        # Documentation
├── *.js            # JavaScript code
├── style.css       # Styles (optional)
└── <name>.png      # Preview screenshot (created by screen-capture)
```
