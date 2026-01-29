# MicroSim Index Generator Skill Updates Log

## 2026-01-28 - Initial Feature Addition

### Summary

Enhanced the `microsim-utils` meta-skill with improved index-generator functionality based on the mkdocs-material grid card format used in the intro-to-physics-course project.

### Changes Made

#### 1. Updated SKILL.md Routing Table

Added additional trigger phrases to the routing table:
- "update the microsim listings"
- "update the list of microsims"
- "create a grid view"
- "generate a listing"

**File:** `skills/microsim-utils/SKILL.md`

#### 2. Enhanced index-generator.md Reference Guide

Comprehensive update to `skills/microsim-utils/references/index-generator.md`:

**New Features:**
- Added "Trigger Phrases" section with common user requests
- Enhanced workflow to add missing descriptions to MicroSim index.md files
- Updated screenshot capture to use `~/.local/bin/bk-capture-screenshot`
- Added TODO.md logging for failed screenshot captures
- Improved grid card format documentation based on physics course example
- Added quality checklist for verification

**Workflow Improvements:**
- Step 3 now handles adding missing `description:` fields to index.md YAML frontmatter
- Step 5 includes verification of screenshot capture success
- Failed screenshots are logged to `/docs/sims/TODO.md` rather than stopping execution
- Better documentation of the exact card format (title/link, image, description order)

**Format Clarification:**
The grid card format follows the physics course pattern:
```markdown
-   **[Title](./name/index.md)**

    ![Title](./name/name.png)

    Description from index.md YAML frontmatter.
```

### Reference Materials Used

- Example format from: `https://github.com/dmccreary/intro-to-physics-course/blob/main/docs/sims/index.md`
- Screenshot tool: `~/.local/bin/bk-capture-screenshot` (symlink to `scripts/bk-capture-screenshot`)
- Existing MicroSim examples in this project (`docs/sims/`)

### Files Modified

1. `skills/microsim-utils/SKILL.md` - Updated routing table with new trigger keywords
2. `skills/microsim-utils/references/index-generator.md` - Complete rewrite with enhanced workflow

### Files Created

1. `logs/generate-microsim-index-skill.md` - This log file

### Testing Notes

The skill should now be triggered when users say:
- "Update the microsim listings"
- "Update the list of microsims"
- "Create a grid view of all the microsims"
- "Generate a listing of all the microsims"
- "Update the MicroSim index page"
- "Regenerate the sims index"

### Next Steps

- Test the skill on the current project's `/docs/sims/` directory
- Verify grid cards render correctly with mkdocs serve
- Add any missing descriptions to existing MicroSims
- Capture missing screenshots for MicroSims without preview images
