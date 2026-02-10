# Session Log: Refactor MicroSim Generator for Token Efficiency

**Date**: February 10, 2026
**Session Focus**: Create batch processing utilities to eliminate ~430K tokens of waste per MicroSim generation run
**Skills Used**: microsim-generator, chapter-content-generator
**Primary Tools**: Python script development, SKILL.md updates

---

## Table of Contents

1. [Session Overview](#session-overview)
2. [Problem Analysis](#problem-analysis)
3. [Files Created](#files-created)
4. [Files Modified](#files-modified)
5. [Verification Results](#verification-results)
6. [sim-status.json Schema](#sim-status-json-schema)
7. [Batch Workflow](#batch-workflow)
8. [Summary and Results](#summary-and-results)

---

## Session Overview

The batch generation of 31 MicroSims for geometry chapters 1-3 consumed ~1.6M tokens. Analysis showed ~55% of tokens were wasted on repetitive tasks: redundant skill guide reads (25%), boilerplate file generation (15%), mkdocs.yml nav editing (10%), and spec parsing from chapters (5%). This session created five Python utilities to eliminate that waste, plus a `sim-status.json` tracking file for resuming work across context windows.

**Key Achievement**: Created a complete pipeline of 5 Python scripts (standard library only) that eliminates ~430K tokens per batch run and enables fast restart after context window fills.

---

## Problem Analysis

| Waste Category | % of Tokens | Solution |
|----------------|-------------|----------|
| Redundant skill guide reads | 25% | `extract-sim-specs.py` pre-parses specs |
| Boilerplate file generation | 15% | `generate-sim-scaffold.py` creates main.html, index.md, metadata.json |
| mkdocs.yml nav editing | 10% | `update-mkdocs-nav.py` regenerates nav section |
| Spec parsing from chapters | 5% | `extract-sim-specs.py` extracts all specs to JSON |
| Quality checking | ~5% | `validate-sims.py` automates 100-point rubric |

---

## Files Created

All new files in `/Users/dan/Documents/ws/claude-skills/src/microsim-utils/`:

### 1. shared.py — Common Utilities

Common module imported by all scripts. Contains:

- **ANSI color constants**: `GREEN`, `RED`, `YELLOW`, `BLUE`, `CYAN`, `BOLD`, `DIM`, `RESET`
- **Unicode symbols**: `CHECK` (✔), `CROSS` (✘), `WARN` (⚠), `ARROW` (→), `BULLET` (•)
- **`find_project_root(start_dir)`**: Walks up from start_dir to find the directory containing `mkdocs.yml`
- **`load_mkdocs_config(project_dir)`**: Parses `site_url`, `site_name`, `docs_dir` from mkdocs.yml using regex (no PyYAML dependency)
- **`kebab_case(title)`**: Converts title strings to kebab-case directory names (e.g., "Point Line and Plane" → "point-line-and-plane")
- **`parse_yaml_frontmatter(content)`**: Extracts flat key-value YAML frontmatter from markdown content
- **`detect_library(html_content)`**: Detects JavaScript library from `<script>` src attributes in main.html (p5.js, vis-network, Chart.js, Mermaid, Plotly, Leaflet, vis-timeline)
- **`LIBRARY_CDNS`**: CDN URL mapping for scaffold generation (p5.js 1.11.10, vis-network 9.1.9, Chart.js 4.4.4, Mermaid 10, Plotly 2.35.0, Leaflet 1.9.4)
- **`LIBRARY_CSS`**: CSS CDN URLs for libraries that need them (vis-timeline, Leaflet)

### 2. extract-sim-specs.py (Priority 1, ~80K token savings)

Parses all `#### Diagram:` / `#### Drawing:` headers from chapter markdown files. Handles both layout patterns found in the geometry course:

- **iframe-before-details** (chapters 01-10): iframe appears above the `<details>` block
- **details-before-iframe** (chapter 11): `<details>` block appears first, iframe below

Key features:
- Extracts `sim_id` from iframe src path, explicit `**sim-id:**` field, or kebab-case title fallback
- Extracts `library` from explicit `**Library:**` field or Implementation line hints
- Infers Bloom level from learning objective text when not explicitly stated
- `--status-file` flag generates `sim-status.json` combining spec extraction with filesystem scan

```bash
python3 extract-sim-specs.py --project-dir /path/to/project --output specs.json --verbose
python3 extract-sim-specs.py --project-dir /path/to/project --chapter 03-angles-and-relationships --output ch03.json
python3 extract-sim-specs.py --project-dir /path/to/project --status-file sim-status.json --verbose
```

Output fields per spec: `sim_id`, `title`, `summary`, `heading_type`, `chapter`, `element_type`, `bloom_level`, `library`, `iframe_src`, `iframe_height`, `spec_text`, `status`

### 3. generate-sim-scaffold.py (Priority 2, ~150K token savings)

Reads specs JSON from extract-sim-specs.py and generates three scaffold files per sim:

- **`main.html`**: Correct CDN for detected library, schema meta tag, `<main>` tag (no id attribute), link back to lesson plan
- **`index.md`**: YAML frontmatter (title, description, image paths, quality_score: 0), iframe embed, fullscreen button, placeholder sections for About, How to Use, Lesson Plan, References
- **`metadata.json`**: Dublin Core + educational + pedagogical fields with TODO placeholders

The agent then only needs to write the `.js` file — all boilerplate is pre-generated.

```bash
python3 generate-sim-scaffold.py --spec-file specs.json --project-dir /path/to/project --verbose
python3 generate-sim-scaffold.py --spec-file specs.json --sim-id angle-explorer --dry-run
python3 generate-sim-scaffold.py --spec-file specs.json --force  # overwrite existing
```

### 4. update-mkdocs-nav.py (Priority 3, ~100K token savings)

Scans `docs/sims/` for directories containing `index.md`, extracts display titles (from frontmatter > `# heading` > directory name), and replaces the MicroSims nav section in mkdocs.yml with an alphabetically sorted list.

- Keeps "List of MicroSims: sims/index.md" as first entry
- Idempotent — safe to run multiple times
- Finds section boundaries by detecting `- MicroSims:` start and next top-level nav entry

```bash
python3 update-mkdocs-nav.py --project-dir /path/to/project --dry-run --verbose
python3 update-mkdocs-nav.py --project-dir /path/to/project
```

### 5. add-iframes-to-chapter.py (Priority 4, ~50K token savings)

Finds `#### Diagram:` / `#### Drawing:` entries in chapter markdown that are missing iframe embeds and inserts them before the `<details>` block.

Additional features:
- `--fix-heights`: Parses JS files for `createCanvas()` calls and updates iframe heights to match
- `--fix-paths`: Normalizes absolute paths (`/sims/`) to relative (`../../sims/`), fixes `500xp` typos to `500px`

```bash
python3 add-iframes-to-chapter.py --chapter 11-circles --project-dir /path/to/project --dry-run --verbose
python3 add-iframes-to-chapter.py --all --project-dir /path/to/project --fix-heights --fix-paths
```

### 6. validate-sims.py (Priority 5, ~50K token savings)

100-point quality rubric aligned with the existing `calculate-quality-score.py` in the microsim-utils skill:

| Category | Points | Checks |
|----------|--------|--------|
| main.html | 10 | exists (5), schema meta tag (3), `<main>` tag (2) |
| metadata.json | 30 | present (10), required fields (10), educational section (5), pedagogical section (5) |
| index.md structure | 35 | title (2), YAML basic (3), YAML images (5), iframe (10), fullscreen (5), iframe example (5), description (5) |
| image | 5 | screenshot PNG present |
| lesson plan | 10 | Lesson Plan section exists |
| references | 5 | References section exists |
| p5.js conventions | 5 | updateCanvasSize (2), no DOM buttons (2), querySelector parenting (1) |

Non-p5.js sims get full marks on the p5.js conventions category.

```bash
python3 validate-sims.py --project-dir /path/to/project --sim angle-builder --verbose
python3 validate-sims.py --project-dir /path/to/project --min-score 0 --format table
python3 validate-sims.py --project-dir /path/to/project --output scores.json
```

### 7. README.md

Full documentation with:
- Overview table of all 5 scripts with token savings
- ASCII workflow diagram showing script chaining
- Per-script documentation with usage examples
- sim-status.json schema documentation
- Design constraints (standard library only, Python 3.7+, idempotent operations)
- Complete batch generation workflow with 6-step CLI commands

---

## Files Modified

### 8. skills/microsim-generator/SKILL.md

**Section added**: "Batch Generation Utilities" after the existing "mkdocs.yml Integration" section (around line 325).

Changes:
- Updated "mkdocs.yml Integration" section to reference `update-mkdocs-nav.py` for batch operations
- Added table of 5 utilities with purpose and token savings
- Added 6-step batch workflow with exact CLI commands
- Added `sim-status.json` integration documentation explaining the lifecycle states

### 9. skills/chapter-content-generator/SKILL.md

**Updated**: The `<details markdown="1">` template (around line 315) to include three machine-readable fields:

```markdown
**sim-id:** [kebab-case-directory-name]<br/>
**Library:** [p5.js | vis-network | Chart.js | Mermaid | Plotly | Leaflet | vis-timeline]<br/>
**Status:** Specified
```

Added explanatory text describing how these fields enable machine-readable extraction by batch utilities.

### 10. skills/chapter-content-generator/references/content-element-types.md

Three changes made:

1. **Fixed `height="500xp"` typo** → `height="500px"` — 8 occurrences across all example specifications (Diagrams, Infographics, MicroSims, Charts, Timelines, Maps, Workflows, Graph Models, Details Block Template)

2. **Replaced `{MICROSIM_NAME}`** → `{sim-id}` — all occurrences, with updated note about kebab-case naming

3. **Updated Details Block Template** (end of file) to include `sim-id`, `Library`, `Status` structured fields with explanatory text

4. **Updated CMDB Architecture Diagram example** to include the new structured fields as a concrete example

---

## Verification Results

All 5 verification tests passed against the geometry-course repository:

### Test 1: extract-sim-specs.py

```
Total specs found: 169
  01-foundations-of-geometry: 8 specs
  02-logic-and-proof: 11 specs
  03-angles-and-relationships: 17 specs
  04-geometric-constructions: 16 specs
  05-coordinate-geometry: 14 specs
  06-transformations-congruence: 13 specs
  07-triangle-congruence: 15 specs
  08-triangle-centers: 14 specs
  09-polygons-quadrilaterals: 13 specs
  10-similarity-trigonometry: 14 specs
  11-circles: 16 specs
  12-area-volume-applications: 18 specs
```

- Correctly detected both iframe-before-details and details-before-iframe patterns
- Green checkmarks (✔) for specs with existing iframes, yellow warnings (⚠) for missing iframes

### Test 2: generate-sim-scaffold.py --dry-run

```
[dry-run] Would create docs/sims/chords-in-a-circle/main.html
[dry-run] Would create docs/sims/chords-in-a-circle/index.md
[dry-run] Would create docs/sims/chords-in-a-circle/metadata.json
✔ [dry-run] Scaffolded: 1  Skipped: 0  Total: 1
```

### Test 3: update-mkdocs-nav.py --dry-run

```
Found 144 MicroSims with index.md
[dry-run] Would replace lines 41-169 (129 lines) with 146 lines
[dry-run] MicroSims nav entries: 144
```

### Test 4: validate-sims.py --sim angle-builder

```
MicroSim                                 Score  Grade
-----------------------------------------------------
✔ angle-builder                             85     A
      main.html: missing schema meta tag
      metadata.json: missing educational section
      screenshot PNG missing
      p5.js: uses DOM functions (createButton(, createSlider(, createSelect()
```

Score breakdown: 85/100 (loses 3 for missing schema tag, 5 for missing educational section, 5 for missing screenshot, 2 for DOM functions)

### Test 5: extract-sim-specs.py --status-file

```
sim-status.json summary:
  specified     83
  scaffolded    3
  implemented   30
  validated     51
  deployed      60
  total         227
```

227 total entries: 169 from chapter specs + 58 additional sims found in docs/sims/ not referenced in chapters.

---

## sim-status.json Schema

Generated by `extract-sim-specs.py --status-file`. Enables fast restart after context window fills.

### Status Lifecycle

```
specified → scaffolded → implemented → validated → deployed
```

| Status | Detection Logic |
|--------|----------------|
| `specified` | Has `<details>` spec in chapter but no sim directory |
| `scaffolded` | Directory with main.html/index.md but no substantive JS |
| `implemented` | JS file exists and >50 lines |
| `validated` | quality_score >= 70 in index.md frontmatter |
| `deployed` | iframe in chapter AND validated |

### Entry Schema

```json
{
  "sim_id": "angle-builder",
  "title": "Angle Builder",
  "chapter": "01-foundations-of-geometry",
  "bloom_level": "Apply",
  "library": "p5.js",
  "status": "deployed",
  "has_iframe": true,
  "quality_score": 85
}
```

---

## Batch Workflow

The complete workflow for generating MicroSims across multiple chapters:

```bash
PROJECT=/Users/dan/Documents/ws/geometry-course
UTILS=/Users/dan/Documents/ws/claude-skills/src/microsim-utils

# 1. Extract all specs from chapter markdown
python3 $UTILS/extract-sim-specs.py \
    --project-dir $PROJECT --output /tmp/specs.json \
    --status-file $PROJECT/docs/sims/sim-status.json --verbose

# 2. Scaffold unbuilt sims (main.html, index.md, metadata.json)
python3 $UTILS/generate-sim-scaffold.py \
    --spec-file /tmp/specs.json --project-dir $PROJECT --verbose

# 3. Agent implements .js files (this is where the creative work happens)
#    Read sim-status.json to find sims with status "scaffolded"

# 4. Insert iframes into chapter markdown for newly built sims
python3 $UTILS/add-iframes-to-chapter.py \
    --all --project-dir $PROJECT --fix-heights --fix-paths

# 5. Update mkdocs.yml navigation
python3 $UTILS/update-mkdocs-nav.py --project-dir $PROJECT

# 6. Validate quality scores
python3 $UTILS/validate-sims.py --project-dir $PROJECT --output /tmp/scores.json
```

---

## Summary and Results

### What Was Built

- **5 Python utility scripts** + 1 shared module + README.md in `src/microsim-utils/`
- **3 skill files updated** to support machine-readable spec extraction and batch workflows
- **8 typo fixes** (`500xp` → `500px`) in content-element-types.md
- **sim-status.json** lifecycle tracking with 5 status levels

### Design Constraints Met

- Standard library only (no pip dependencies)
- Python 3.7+ compatible
- All scripts support `--project-dir`, `--dry-run`, `--verbose`
- Idempotent operations
- `if __name__ == '__main__':` with argparse

### Geometry Course Stats

- **169 specs** extracted across 12 chapters
- **227 total sims** tracked in sim-status.json
- **83 sims** still in "specified" status (ready for scaffolding + implementation)
- **60 sims** fully deployed (validated + iframe in chapter)

### Token Impact

Estimated savings per batch generation run: **~430K tokens** (~27% of the 1.6M baseline), enabling generation of the remaining 83 unbuilt sims in approximately 2 context windows instead of 4-5.
