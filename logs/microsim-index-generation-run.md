# MicroSim Index Generation Run Log

**Date:** 2026-01-28
**Skill Used:** `/microsim-utils` → `index-generator`
**Operator:** Claude Opus 4.5

## Summary

Successfully updated the MicroSim index page (`/docs/sims/index.md`) and mkdocs.yml navigation to use mkdocs-material grid cards format with 36 MicroSims.

## Files Updated

1. **`/docs/sims/index.md`** - Completely rewritten with grid cards format
2. **`mkdocs.yml`** - MicroSims navigation section updated and sorted alphabetically
3. **`/docs/sims/TODO.md`** - Created with exact shell commands for missing screenshots
4. **`~/.claude/skills/microsim-utils/references/index-generator.md`** - Updated skill to require TODO.md logging

## Statistics

- **Total MicroSims:** 36
- **MicroSims with screenshots:** 30
- **MicroSims missing screenshots:** 6

## MicroSims Missing Screenshots

The following MicroSims do not have matching PNG screenshot files in their directories:

| MicroSim | Expected Screenshot | Status |
|----------|---------------------|--------|
| book-build-workflow | `book-build-workflow.png` | Missing |
| certificate-generator | `certificate-generator.png` | Missing (only has `dan-mccreary-signature.png`) |
| claude-code-memory-layers | `claude-code-memory-layers.png` | Missing |
| claude-code-tshirt-design | `claude-code-tshirt-design.png` | Missing |
| graph-color-test | `graph-color-test.png` | Missing |
| three-color-dfs | `three-color-dfs.png` | Missing |

## Bug Fixed in Skill

The `microsim-utils/references/index-generator.md` workflow originally did not enforce logging missing screenshots to TODO.md.

**Issue:** The workflow mentioned TODO.md logging but only as an afterthought for failed captures, not as a required step before generating the index.

**Fix Applied:** Updated the skill to:
1. Made Step 5 "Log Missing Screenshots to TODO.md (REQUIRED)" - a mandatory step before index generation
2. Added clear instructions to create TODO.md with exact shell commands for each missing screenshot
3. Made screenshot capture (Step 6) optional, while TODO.md logging is required
4. Renumbered subsequent steps (Step 6 → Step 7, etc.)

**Result:** `/docs/sims/TODO.md` now contains copy-paste ready commands:
```bash
~/.local/bin/bk-capture-screenshot docs/sims/<microsim-name>
```

## Changes Made

### Index Page Updates

- Converted from simple markdown list to mkdocs-material `<div class="grid cards">` format
- Added YAML frontmatter with title, description, and image metadata
- Added `hide: - toc` to reduce clutter on the index page
- Each card includes: linked title, screenshot image, and description
- All entries sorted alphabetically by display title

### Navigation Updates

- Sorted all MicroSim entries alphabetically
- Fixed typos:
  - "Enviroment" → "Environment"
- Renamed entries for consistency:
  - "Graph Viewer" → "Learning Graph Viewer"
  - "Map Test World Cities" → "Major World Cities Map"
  - "Skill Impact Chart" → "Skill Development Priority Matrix"
- Added missing entry: "Book Levels"

## Verification Steps Needed

1. Run `mkdocs serve` to verify the grid cards render correctly
2. Check that all image paths resolve (6 will show broken images)
3. Capture missing screenshots using the screenshot tool
4. Verify navigation links work in the sidebar

## Next Steps

1. Run the commands in `/docs/sims/TODO.md` to capture the 6 missing screenshots
2. Verify screenshots render correctly in the grid cards
3. Remove entries from TODO.md as screenshots are captured
