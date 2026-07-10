# MicroSim Standardization Skill

## Overview

The microsim-standardization skill performs comprehensive audits and quality upgrades of MicroSim directories to ensure they meet documentation and structural standards. It validates structure, YAML metadata, Dublin Core metadata, iframe embeds, documentation completeness, and generates quality scores (0-100) based on a detailed rubric. The skill works with all MicroSim types regardless of the JavaScript library used (p5.js, vis-network, Chart.js, Plotly.js, Leaflet, Mermaid, etc.).

## Purpose

This skill automates the process of bringing existing MicroSims up to standardized quality levels, ensuring consistent documentation, proper metadata for social sharing and SEO, complete lesson plans, and comprehensive educational content. It systematically identifies gaps in documentation and structure, then optionally implements all necessary improvements to achieve quality scores of 85 or higher.

## Key Features

- **Quality Score Calculation**: Evaluates MicroSims against a 14-point rubric (0-100 scale)
- **Pre-Audit Check**: Skips standardization if quality_score ≥ 85 to conserve tokens
- **Comprehensive Checklist**: Validates 12 critical structural and documentation elements
- **Dublin Core Validation**: Ensures metadata.json conforms to JSON schema with 9 required fields
- **TODO Generation**: Creates actionable TODO.txt file with all needed improvements
- **Automated Implementation**: Optionally applies all standardization changes with user approval
- **Library Detection**: Automatically identifies JavaScript library (p5.js, Chart.js, etc.)
- **Template-Based**: Uses standardized templates for index.md and metadata.json
- **YAML Metadata**: Validates frontmatter for social preview images and quality scores
- **Educational Content**: Ensures lesson plans, learning objectives, and references are present

## When to Use

Use this skill when:

- Auditing existing MicroSims for quality and completeness
- Upgrading older MicroSims to current documentation standards
- Preparing MicroSims for publication or sharing
- Ensuring consistent documentation across multiple MicroSims
- Adding missing metadata for SEO and social media previews
- Validating MicroSim structure before adding to textbook navigation
- Implementing lesson plans and educational content for existing simulations
- Achieving quality scores of 85+ for production-ready MicroSims

## Common Trigger Phrases

- "Standardize this MicroSim"
- "Audit the MicroSim at docs/sims/..."
- "Check if this MicroSim meets quality standards"
- "Upgrade this MicroSim to production quality"
- "Validate MicroSim documentation"
- "Add missing metadata to this simulation"
- "Ensure this MicroSim has a lesson plan"
- "Calculate the quality score for this MicroSim"
- "Bring this MicroSim up to standards"

## Workflow Steps

### Step 1: Receive MicroSim Directory Path

Accept the path to the MicroSim directory from the user:
- **Location**: `docs/sims/[microsim-name]/`
- **Naming convention**: kebab-case (lowercase letters and dashes only)
- **Minimum requirement**: Directory must contain `main.html` file

**Example paths:**
- `docs/sims/sine-function/`
- `docs/sims/learning-graph-viewer/`
- `docs/sims/bubble-chart-priority-matrix/`

Verify the directory exists and contains at minimum the core `main.html` simulation file.

### Step 2: Check for Existing Quality Score

Read the `index.md` file and check for existing quality_score in YAML frontmatter:

```yaml
---
quality_score: 86
---
```

**Decision logic:**
- **If score ≥ 85**: Suggest to the user that standardization may not be needed. Inform them that tokens could be better spent creating new MicroSims rather than upgrading an already high-quality one.
- **If score < 85 or missing**: Proceed with comprehensive standardization audit.

This pre-check prevents unnecessary work on already-standardized MicroSims.

### Step 3: Run Standardization Checklist

Systematically evaluate the MicroSim against all 12 standardization criteria. Use the TodoWrite tool to create a comprehensive TODO list documenting all items that need attention. Save the TODO list to `TODO.txt` in the MicroSim directory.

#### Standardization Checklist (12 Items)

**1. Index.md File Existence**
- Check if `index.md` file exists in the MicroSim directory
- If missing: Add TODO to create `index.md` file from template

**2. YAML Metadata at Top of index.md**
- Verify `index.md` begins with YAML frontmatter between `---` delimiters
- Required YAML fields:
  - `title:` - MicroSim title (string)
  - `description:` - Brief description for SEO and social previews (1-2 sentences)
  - `quality_score:` - Integer 1-100 indicating completeness/quality
  - `image:` - Social media preview image path (optional but recommended)
  - `og:image` - Open Graph image for social sharing (optional but recommended)
- If missing or incomplete: Add TODO to add/fix YAML frontmatter

**3. Level 1 Header After Frontmatter**
- Verify a level 1 header (`# Title`) appears immediately after YAML metadata
- The title should match or complement the YAML `title` field
- If missing: Add TODO to add level 1 header

**4. Iframe Embed After Title**
- Check for iframe element after the level 1 title
- Iframe must reference `main.html`
- Standard format (without frameborder attribute):
  ```html
  <iframe src="main.html" width="100%" height="600px"></iframe>
  ```
- **Note**: Do NOT add frameborder attribute; site-wide CSS handles iframe styling
- If missing or incorrect: Add TODO to add/fix iframe embed

**5. Copy-Paste Iframe Example**
- Check for a second iframe in an HTML code block with label "Copy this iframe to your website:"
- This allows users to embed the MicroSim in their own sites
- Standard format:
  ````markdown
  ```html
  <iframe src="https://your-domain.github.io/path/to/sims/microsim-name/main.html" width="100%" height="600px"></iframe>
  ```
  ````
- If missing: Add TODO to add copy-paste iframe example

**6. Metadata.json File Existence**
- Check if `metadata.json` file exists in the MicroSim directory
- If missing: Add TODO to create `metadata.json` with Dublin Core metadata

**7. Metadata.json Schema Validation**
- Validate `metadata.json` against the Dublin Core schema in `assets/metadata-schema.json`
- **Required Dublin Core fields (9 total):**
  - `title` - MicroSim name (string, minLength: 1)
  - `description` - Purpose and functionality (string, minLength: 1)
  - `creator` - Author name or organization (string, minLength: 1)
  - `date` - Creation date in ISO 8601 format: YYYY-MM-DD (pattern validated)
  - `subject` - Keywords or topics (string or array of strings)
  - `type` - Resource type (e.g., "Interactive Simulation")
  - `format` - File format (e.g., "text/html")
  - `language` - Language code (e.g., "en" or "en-US", minLength: 2)
  - `rights` - License information (e.g., "CC BY 4.0", "MIT License")
- **Optional educational fields:**
  - `educationalLevel` - Target grade level
  - `learningResourceType` - Type of resource (e.g., "simulation")
  - `audience` - Intended audience
  - `bloomLevel` - Bloom's Taxonomy levels addressed (string or array)
  - `concepts` - Key concepts demonstrated (array)
  - `prerequisites` - Prerequisite knowledge (array)
  - `library` - JavaScript library used (e.g., "p5.js")
- If validation fails: Add TODO to fix metadata.json structure and content

**8. Fullscreen Link Button**
- Check for fullscreen link button after the iframe example
- Standard format using MkDocs Material button classes:
  ```markdown
  [Run MicroSim in Fullscreen](main.html){ .md-button .md-button--primary }
  ```
- If missing: Add TODO to add fullscreen link button

**9. P5.js Editor Link (P5.js MicroSims Only)**
- Determine if the MicroSim uses p5.js by checking:
  - Import statements in `main.html` for p5.js CDN (e.g., `https://cdnjs.cloudflare.com/ajax/libs/p5.js/`)
  - Use of p5.js functions like `setup()`, `draw()`, `createCanvas()`
- If p5.js is used, check for p5.js editor link:
  ```markdown
  [Edit in the p5.js Editor](https://editor.p5js.org/username/sketches/SKETCH_ID){ .md-button }
  ```
- If link is missing or contains placeholder text: Add TODO to prompt user for p5.js sketch URL
- If not a p5.js MicroSim: Skip this check

**10. Description Section (Level 2 Header)**
- Check for a level 2 header section after the frontmatter elements
- Common headers: `## Description`, `## How to Use`, `## About This MicroSim`
- This section should describe:
  - The MicroSim's purpose
  - How to use it (interactive controls)
  - What concepts it demonstrates
  - Key features (bulleted list)
- If missing: Add TODO to add description section

**11. Lesson Plan Section**
- Check if a `## Lesson Plan` level 2 header exists
- This section should include:
  - **Learning Objectives**: What students will be able to do (using Bloom's Taxonomy action verbs)
  - **Target Audience**: Grade level or educational level
  - **Prerequisites**: Required background knowledge
  - **Activities**: Structured exploration activities (3+ activities recommended)
  - **Assessment**: Discussion questions, reflection prompts, or demonstrations
- If missing: Add TODO to ask user whether to create a lesson plan section

**12. References Section**
- Check if a `## References` level 2 header exists at the end of the document
- This section should include:
  - Links to relevant academic papers or articles
  - Link format: `1. [Link Title](URL) - publication_date - publication_name - description and relevance`
  - Documentation for libraries used
  - Related educational resources
- If missing and appropriate for the content: Add TODO to add references section

### Step 4: Present TODO List to User

Present the comprehensive TODO list to the user, organized by priority:

1. **Critical structural issues** (missing index.md, invalid metadata.json)
2. **Required documentation elements** (frontmatter, headers, iframes)
3. **Enhanced documentation** (lesson plans, references)

**Example presentation:**
```
MicroSim Standardization Audit Complete

Found 8 items that need attention:

Critical (2):
- Create metadata.json with Dublin Core metadata
- Add YAML frontmatter to index.md

Required (4):
- Add iframe embed referencing main.html
- Add copy-paste iframe example
- Add fullscreen link button
- Add description section

Enhanced (2):
- Create lesson plan with learning objectives
- Add references section

Current estimated quality score: 45/100
Potential score after fixes: 90/100
```

Ask the user: **"Should I proceed with implementing these standardization changes? (y/n)"**

### Step 5: Implement Changes (If Approved)

If the user responds "y" or "yes":

1. Work through the TODO list systematically in priority order
2. Update the TodoWrite status as each item is completed
3. For items requiring user input (e.g., p5.js sketch URL, specific lesson plan content), use AskUserQuestion to gather necessary information
4. Validate all changes as they're made
5. Re-run metadata.json validation after modifications

#### Implementation Guidelines

**Preserve existing content**: Never remove or overwrite user content without explicit confirmation. Only add missing elements or fix formatting issues.

**Maintain formatting consistency**: Use the same markdown style as existing content. Match heading levels, list styles, and code block formatting.

**Add blank lines before lists**: MkDocs requires blank lines before markdown lists:
```markdown
Here are the features:

- Feature 1
- Feature 2
```

**Use Title Case for headers**: Follow MkDocs Material theme conventions for level 1 and level 2 headers.

**Validate JSON syntax**: Ensure metadata.json is valid JSON before saving. Use proper escaping for special characters.

**Test iframe paths**: Verify `main.html` path is correct relative to `index.md`.

**YAML vs Dublin Core separation**:
- **YAML frontmatter** (in index.md): Used for social preview images and quality_score only
- **Dublin Core metadata** (in metadata.json): All 9+ required metadata fields
- **Never mix these up**: Dublin Core fields belong ONLY in metadata.json

**Use templates**: Reference the template files for consistent structure:
- `assets/index-template.md` for index.md structure
- `assets/metadata-template.json` for metadata.json structure

### Step 6: Final Validation and Quality Report

After completing all changes:

1. **Run final validation** on metadata.json using the schema in `assets/metadata-schema.json`
2. **Check that all TODO items** are marked completed
3. **Calculate final quality score** using the rubric below
4. **Update quality_score** in index.md YAML frontmatter
5. **Provide a summary report** to the user

#### Quality Score Rubric

The quality score is calculated by summing points from the following 14 tests:

| Test Name | Description | Points |
|-----------|-------------|--------|
| Title | index.md file has a title in markdown level 1 | 2 |
| main.html | The file main.html is present | 10 |
| Metadata 1 | index.md has title and description metadata in YAML | 3 |
| Metadata 2 | index.md has image references for social preview | 5 |
| metadata.json present | A metadata.json file is present | 10 |
| metadata.json is valid | The MicroSim JSON schema validation passed with no errors | 20 |
| iframe | An iframe that uses src="main.html" is present | 10 |
| Fullscreen Link Button | A button to view the MicroSim in fullscreen is present | 5 |
| iframe example | An iframe example in an HTML source block is present | 5 |
| image | An image of the MicroSim is present in the directory and referenced by header metadata | 5 |
| Overview Documentation | A description of the MicroSim and how to use it is present | 5 |
| Lesson Plan | A detailed lesson plan is present | 10 |
| References | A list of references in markdown format | 5 |
| MicroSim Type Specific Format | Varies by type. Example: link to p5.js editor | 5 |

**Total possible score**: 100 points

**Quality score interpretation**:
- **90-100**: Excellent - All elements present, comprehensive documentation, lesson plan included
- **70-89**: Good - Most items present, solid documentation, may lack lesson plan or references
- **50-69**: Fair - Core items present, minimal documentation
- **Below 50**: Needs work - Missing critical components

After calculating the score, it MUST be written to the `quality_score` field in index.md YAML frontmatter.

**Example summary report**:
```
Standardization Complete!

Issues found and fixed: 8
- Created metadata.json with all 9 required Dublin Core fields
- Added YAML frontmatter with title, description, and image references
- Added iframe embed and copy-paste example
- Created comprehensive lesson plan with 4 activities
- Added 5 references to educational resources

Quality Score:
- Before: 45/100
- After: 92/100

The MicroSim now meets production quality standards and is ready for publication.
```

## Resources

### assets/metadata-schema.json

JSON Schema for validating MicroSim metadata.json files against Dublin Core standards. This schema defines:

- **Required fields**: 9 core Dublin Core elements (title, description, creator, date, subject, type, format, language, rights)
- **Optional fields**: Extended metadata for educational resources (educationalLevel, audience, bloomLevel, concepts, prerequisites, library)
- **Field types and validation patterns**: Date format validation (ISO 8601), language code validation, etc.
- **Educational extensions**: Bloom's levels, concepts, prerequisites specific to educational MicroSims

Use this schema to validate metadata.json files programmatically or to guide manual validation.

**Validation approach**: Compare the metadata.json structure against the schema, checking for:
- All required fields are present
- Field types match (string, array, etc.)
- String fields have minimum lengths
- Date field matches ISO 8601 pattern (YYYY-MM-DD)
- Arrays contain at least one item where required

### assets/index-template.md

Complete template showing the standard structure for a MicroSim index.md file, including:

- **YAML frontmatter** with all required fields (title, description, quality_score, image, og:image)
- **Level 1 header** matching the title
- **Iframe embeds** - both display iframe and copy-paste version with full URL
- **Fullscreen link button** using MkDocs Material button classes
- **P5.js editor link** (commented out for non-p5.js MicroSims)
- **Description section** with key features list and usage instructions
- **Lesson Plan section** with learning objectives, target audience, activities, and assessment
- **References section** with properly formatted links

Use this template when creating new index.md files or when a MicroSim is missing critical documentation sections. Replace all `{{PLACEHOLDERS}}` with actual values.

### assets/metadata-template.json

Complete template showing all Dublin Core metadata fields with example values, including:

- **All 9 required core fields**: title, description, creator, date, subject, type, format, language, rights
- **Optional Dublin Core fields**: contributor, identifier, publisher
- **Educational extensions**: educationalLevel, learningResourceType, audience, version, bloomLevel, concepts, prerequisites, library

Use this template when creating new metadata.json files or when existing metadata is incomplete. The template demonstrates:
- Proper JSON structure and formatting
- ISO 8601 date format (YYYY-MM-DD)
- Subject keywords as arrays
- Bloom's levels as arrays
- Proper license notation (CC BY 4.0)

## Best Practices

### Quality Standards

**Set clear thresholds**:
- Production-ready MicroSims should achieve scores of 85+
- MicroSims scoring 70-84 are acceptable but should be improved when time permits
- Scores below 70 indicate missing critical components requiring immediate attention

**Prioritize metadata completeness**:
- Valid metadata.json (20 points) is the highest-value improvement
- Social preview images (5 points) significantly improve discoverability
- Lesson plans (10 points) add substantial educational value

### Library Detection

Automatically detect JavaScript libraries by checking `main.html` for:

- **p5.js**: `p5.js` or `p5.min.js` in script tags or CDN URLs
- **vis-network**: `vis-network` in script tags or imports
- **Chart.js**: `chart.js` or `Chart.min.js` in script tags
- **Plotly.js**: `plotly` or `plotly.js` in script tags
- **Leaflet**: `leaflet` in script tags or imports
- **D3.js**: `d3.js` or `d3.min.js` in script tags
- **Mermaid**: `mermaid` in script tags

Store the detected library in the `library` field of metadata.json for proper categorization.

### Metadata Best Practices

**Use ISO 8601 dates**: Always format dates as YYYY-MM-DD (e.g., 2025-01-17)

**Include multiple subject keywords**: Add 3-5 specific keywords for discoverability:
- Good: ["trigonometry", "sine wave", "periodic functions", "calculus"]
- Avoid: ["math"] (too broad)

**Specify clear educational levels**: Use standard terminology:
- "Elementary School" (grades K-5)
- "Middle School" (grades 6-8)
- "High School" (grades 9-12)
- "Undergraduate"
- "Graduate"

**List all contributors**: Include everyone who contributed significantly, not just the primary creator

**Include version numbers**: Track iterations using semantic versioning (e.g., "1.0.0", "1.1.0")

**Choose appropriate licenses**: Common educational licenses:
- CC BY 4.0 (most permissive, allows derivatives and commercial use)
- CC BY-SA 4.0 (share-alike, derivatives must use same license)
- MIT License (permissive software license)
- Apache 2.0 (permissive with patent grant)

### Documentation Quality

**Write clear learning objectives**: Use Bloom's Taxonomy action verbs:
- Remember: Define, list, recall, identify
- Understand: Explain, summarize, classify, describe
- Apply: Implement, solve, use, demonstrate
- Analyze: Compare, differentiate, examine, organize
- Evaluate: Judge, critique, assess, justify
- Create: Design, construct, develop, formulate

**Design interactive activities**: Leverage the MicroSim's interactivity:
- "Use the slider to find where f(x) = 0"
- "Observe what happens when you increase the amplitude"
- "Compare the behavior at x = 0 versus x = π"

**Provide measurable assessments**: Include specific success criteria:
- "Student can identify at least 3 x-values where the function crosses zero"
- "Student can explain the relationship between period and frequency"

### Token Conservation

**Check quality scores first**: Always check for existing quality_score ≥ 85 before proceeding with full audit

**Batch similar MicroSims**: If standardizing multiple MicroSims, group by library type (all p5.js, then all Chart.js, etc.) for efficiency

**Use templates consistently**: Don't regenerate template structures; reference and reuse the templates in `assets/`

## Technical Details

- **YAML parser**: MkDocs uses PyYAML for frontmatter parsing
- **JSON validation**: Uses JSON Schema Draft 07 specification
- **Dublin Core version**: Follows DCMI Metadata Terms specification
- **ISO 8601 dates**: YYYY-MM-DD format with regex pattern `^\d{4}(-\d{2}(-\d{2})?)?$`
- **Markdown dialect**: CommonMark with GitHub Flavored Markdown extensions
- **MkDocs Material version**: Compatible with Material for MkDocs 9.x
- **Iframe security**: All iframes use same-origin or GitHub Pages hosting (no sandboxing needed)
- **Image formats**: PNG recommended for social preview images (1200x630px optimal)

## Example Use Cases

### Use Case 1: Upgrading Legacy MicroSim

**Scenario**: A p5.js MicroSim created in 2023 lacks metadata and lesson plan

**Process**:
1. Check quality score (score: 35/100 - missing metadata, no lesson plan)
2. Run standardization checklist
3. Generate TODO list: 10 items
4. Implement: Create metadata.json, add YAML frontmatter, write lesson plan, add references
5. Final score: 90/100

### Use Case 2: Pre-Publication Validation

**Scenario**: New Chart.js bubble chart needs validation before adding to textbook

**Process**:
1. Check quality score (missing - new MicroSim)
2. Run standardization checklist
3. Find 5 minor issues: missing social image, incomplete lesson plan
4. Implement fixes
5. Calculate score: 88/100 - ready for publication

### Use Case 3: Batch Standardization

**Scenario**: Standardizing 15 MicroSims across different library types

**Process**:
1. Check quality scores for all 15
2. Skip 4 MicroSims with scores ≥ 85
3. Prioritize remaining 11 by current score (lowest first)
4. Standardize in batches by library type
5. Achieve average score increase from 52 to 87

### Use Case 4: Educational Content Enhancement

**Scenario**: Existing MicroSim has good technical implementation but weak educational content

**Process**:
1. Quality score: 60/100 (good structure, weak lesson plan)
2. Focus standardization on educational elements
3. Enhance lesson plan with Bloom's Taxonomy alignment
4. Add 8 references to pedagogical resources
5. Final score: 85/100

## Troubleshooting

### Issue: Metadata.json validation fails

**Solution**: Check common JSON syntax errors:
- Missing commas between fields
- Unescaped quotation marks in strings
- Invalid date format (must be YYYY-MM-DD)
- Missing required fields (verify all 9 core fields present)

Use a JSON linter or validator before running schema validation.

### Issue: Quality score doesn't match expectations

**Solution**: Review the rubric carefully. Common missed points:
- Social preview images (5 points) - images must exist AND be referenced in YAML
- metadata.json validity (20 points) - must pass schema validation perfectly
- Lesson plan completeness (10 points) - must include objectives, activities, and assessment

### Issue: YAML frontmatter not parsing

**Solution**: Verify YAML syntax:
- Must start and end with `---` on separate lines
- Colons must have space after them (`title: Example` not `title:Example`)
- No tabs (use spaces only)
- Strings with colons must be quoted (`description: "This: Example"`)

### Issue: P5.js editor link placeholder remains

**Solution**: If p5.js is detected but no editor link provided:
- Prompt user for p5.js sketch URL
- If URL unavailable, comment out the link and note in TODO
- Reduce MicroSim Type Specific Format score (0/5 instead of 5/5)

### Issue: Reading level mismatch in lesson plan

**Solution**:
- Check `docs/course-description.md` for target reading level
- If not specified, assume high school level (grades 9-12)
- Adjust vocabulary and complexity accordingly
- Use simpler language for middle school, more technical for college

## References

- [Dublin Core Metadata Initiative](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) - Official DCMI Terms specification
- [JSON Schema Draft 07](https://json-schema.org/draft-07/schema) - JSON Schema specification
- [ISO 8601 Date Format](https://www.iso.org/iso-8601-date-and-time-format.html) - International date standard
- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/) - Theme documentation
- [Bloom's Taxonomy (2001 Revision)](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) - Educational framework
- [ISO 11179 Metadata Registry](https://www.iso.org/standard/50340.html) - Metadata naming standards
- [Creative Commons Licenses](https://creativecommons.org/licenses/) - Open content licenses
- [MicroSim Pattern Documentation](https://github.com/dmccreary/claude-skills/blob/main/README.md) - Repository-specific MicroSim guidelines

## Guide Location

`skills/microsim-utils/references/standardization.md`

This was formerly the standalone `microsim-standardization` skill; it is now a guide
inside the `microsim-utils` meta-skill.

## Notes

**Terminology Precision**: There are two types of metadata for MicroSims:

1. **YAML header metadata**: Inserted into the top of index.md file between `---` delimiters. Used for social image previews and quality_score. The mkdocs-material social plugin uses these fields.

2. **Dublin Core metadata**: Stored ONLY in the `metadata.json` file. Includes all 9 required Dublin Core elements plus optional educational extensions.

**Never mix these up!** Never put Dublin Core metadata into the YAML headers, and never put quality_score into metadata.json.

**Pre-Audit Efficiency**: The quality score pre-check (Step 2) is critical for token conservation. Always check for existing quality_score ≥ 85 before proceeding with the full audit. A high-quality MicroSim doesn't need re-standardization.

**Lesson Plan Value**: While lesson plans contribute only 10 points to the quality score, they provide substantial educational value and should be prioritized when standardizing MicroSims intended for classroom use.

**Library-Specific Elements**: Some libraries require specific documentation:
- **p5.js**: Link to p5.js editor sketch
- **vis-network**: Configuration options documentation
- **Chart.js**: Dataset structure examples
- **Plotly.js**: Trace configuration examples
- **Leaflet**: Map tile attribution requirements

Adjust the "MicroSim Type Specific Format" test (5 points) based on whether library-specific documentation is present and appropriate.
