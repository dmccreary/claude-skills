---
name: microsim-utils
description: Utility tools for MicroSim management including quality validation, screenshot capture, icon management, and index page generation. Routes to the appropriate utility based on the task needed.
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

## Step 1: Identify Utility Type

Match the user's request to the appropriate utility guide:

### Routing Table

| Trigger Keywords | Guide File | Purpose |
|------------------|------------|---------|
| standardize, quality, validate, score, check, audit | `references/standardization.md` | Quality validation and scoring |
| screenshot, capture, preview, image, thumbnail | `references/screen-capture.md` | Automated screenshot generation |
| icons, add icons, favicon, logo | `references/add-icons.md` | Icon management for MicroSims |
| index page, microsim list, grid, directory, catalog, update the microsim listings, update the list of microsims, create a grid view, generate a listing | `references/index-generator.md` | Generate index page with grid cards |

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
```

## Step 2: Load the Matched Guide

Read the corresponding guide file from `references/` and follow its workflow.

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
