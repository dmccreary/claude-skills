# Installing the Glossary Generator Skill

## Quick Start

To use this skill with Claude:

### Option 1: Claude.ai Web Interface

1. Go to [claude.ai](https://claude.ai)
2. Start a new conversation
3. Upload or reference this skill directory
4. Ask Claude to use the glossary-generator skill

### Option 2: Claude Code CLI

If using Claude Code CLI with skills support:

```bash
# Copy skill to Claude's skills directory
cp -r /skills/glossary-generator ~/.claude/skills/

# Or use it directly from this location
claude --skill /skills/glossary-generator "Generate a glossary"
```

### Option 3: Direct Reference

Simply tell Claude:

> "Please use the glossary-generator skill located at /skills/glossary-generator to create a glossary from my concept list"

## Verification

To verify the skill is properly structured:

```bash
cd /skills/glossary-generator
ls -la
```

You should see:

```
SKILL.md                    # Main skill instructions (required)
README.md                   # Documentation
INSTALL.md                  # This file
references/                 # Reference materials
  └── iso-11179-standards.md
```

## Testing the Skill

### Test with Example Data

1. Ensure you have a concept list file:
   - Location: `docs/learning-graph/02-concept-list-v1.md`
   - Format: Numbered list of concepts

2. Ensure you have a course description:
   - Location: `docs/course-description.md`
   - Contains: Audience, objectives, prerequisites

3. Ask Claude:
   ```
   Use the glossary-generator skill to create a glossary from
   docs/learning-graph/02-concept-list-v1.md
   ```

4. Expected outputs:
   - `docs/glossary.md` (main glossary file)
   - `docs/learning-graph/glossary-quality-report.md` (quality metrics)

### Validate Output

Check that:

- [ ] All concepts from input list appear in glossary
- [ ] Terms are alphabetically sorted
- [ ] Definitions follow ISO 11179 standards
- [ ] 60-80% of terms have examples
- [ ] Quality score > 85/100
- [ ] No circular definitions
- [ ] Markdown renders correctly

## Skill Structure Explained

```
glossary-generator/
│
├── SKILL.md                 # Core instructions for Claude
│   ├── YAML frontmatter     # name, description, license
│   └── Markdown content     # Step-by-step workflow
│
├── README.md                # Human-readable documentation
├── INSTALL.md              # This installation guide
│
└── references/             # Loaded as needed by Claude
    └── iso-11179-standards.md  # Detailed ISO standards
```

### How Claude Uses This Skill

1. **Skill Detection:** Claude reads YAML frontmatter to know when to use skill
2. **Workflow Execution:** Claude follows SKILL.md instructions step-by-step
3. **Reference Lookup:** Claude loads `iso-11179-standards.md` when needed
4. **Quality Assurance:** Claude uses scoring rubrics to validate output

## Requirements

### Input Files Required

- Concept list (markdown file with numbered list)
- Course description (markdown file)

### Input Files Optional

- Existing glossary (for updates)
- Previous quality reports (for comparison)

### Output Directory Structure

Skill expects this directory structure:

```
docs/
├── glossary.md                  # Created by skill
├── course-description.md        # Required input
└── learning-graph/
    ├── 02-concept-list-v1.md   # Required input
    └── glossary-quality-report.md  # Created by skill
```

## Troubleshooting

### Skill Not Triggering

**Problem:** Claude doesn't recognize the skill

**Solutions:**
- Verify SKILL.md has proper YAML frontmatter
- Check that name and description are descriptive
- Explicitly tell Claude to use the skill by name

### Missing Reference Files

**Problem:** Claude can't find ISO standards reference

**Solutions:**
- Verify `references/iso-11179-standards.md` exists
- Check file permissions (should be readable)
- Path should be relative to SKILL.md

### Output Files Not Created

**Problem:** Glossary or quality report not generated

**Solutions:**
- Verify output directories exist (`docs/`, `docs/learning-graph/`)
- Check write permissions
- Ensure input files are valid (concept list, course description)

### Quality Score Too Low

**Problem:** Glossary quality score < 85

**Solutions:**
- Review input concept list for quality issues
- Ensure concepts are clear, unique, properly formatted
- Check that course description provides good context
- Review quality report recommendations

## Advanced Configuration

### Customizing Output Locations

Tell Claude explicitly where to put outputs:

```
Use the glossary-generator skill to create a glossary.
Place the glossary at docs/reference/glossary.md
Place the quality report at reports/glossary-quality.md
```

### Adjusting Quality Thresholds

Tell Claude to use different thresholds:

```
Use the glossary-generator skill with these requirements:
- Minimum quality score: 90/100
- Example coverage: 80% (instead of default 60%)
- Maximum definition length: 40 words (instead of 50)
```

### Focusing on Specific Concepts

Generate glossary for subset of concepts:

```
Use the glossary-generator skill to create definitions
only for concepts in the "Educational Technology" category
```

## Next Steps

After installing the skill:

1. **Test it:** Generate a glossary from your concept list
2. **Review output:** Check quality report and scores
3. **Iterate:** Refine based on recommendations
4. **Integrate:** Use glossary in your textbook content

## Related Documentation

- **Full Specification:** `/docs/skills/glossary-generator.md`
- **Skill Index:** `/docs/skills/index.md`
- **ISO Standards Reference:** `references/iso-11179-standards.md`
- **Example Workflow:** See README.md

## Support

If you encounter issues:

1. Check this installation guide
2. Review SKILL.md for workflow details
3. Consult ISO standards reference
4. Check quality report for specific guidance

## Version

- **Skill Version:** 1.0
- **Last Updated:** 2025-01-31
- **Compatibility:** Claude Code, Claude.ai
