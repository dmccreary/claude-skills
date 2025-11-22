# MicroSim Utility Scripts

This directory contains utility scripts for batch processing and standardizing MicroSims in the repository.

## Scripts

### 1. batch-standardize.py

Batch standardizes all MicroSims in the repository by adding missing structural elements.

**What it does:**
- Detects JavaScript library used (p5.js, Chart.js, Mermaid, etc.)
- Creates metadata.json files with Dublin Core metadata
- Adds YAML frontmatter to index.md files
- Adds iframe embeds, fullscreen buttons, and copy-paste examples
- Adds Overview sections
- Calculates quality scores based on standardization rubric

**Usage:**
```bash
# From repository root
python3 src/utilities/batch-standardize.py

# Or from docs/sims directory
cd docs/sims
python3 ../../src/utilities/batch-standardize.py
```

**Skip threshold:** Skips MicroSims with quality_score ≥ 85

**Output:** Updated index.md and metadata.json files for each MicroSim

---

### 2. batch-capture-screenshots.sh

Batch captures PNG screenshots for all MicroSims that don't have images.

**What it does:**
- Identifies MicroSims missing PNG screenshot files
- Uses Chrome headless mode to capture screenshots
- Saves screenshots as `{microsim-name}.png` in each directory
- Waits 5 seconds for JavaScript to render

**Prerequisites:**
- Google Chrome installed
- `microsim-screen-capture` skill script available

**Usage:**
```bash
# From docs/sims directory
cd docs/sims
bash ../../src/utilities/batch-capture-screenshots.sh
```

**Output:** PNG files (typically 40KB-200KB) in each MicroSim directory

---

### 3. update-image-metadata.py

Updates index.md YAML frontmatter with image metadata paths.

**What it does:**
- Checks which MicroSims have PNG files
- Adds `image:` and `og:image:` fields to YAML frontmatter
- Recalculates quality scores (+10 points for images)
- Updates quality_score field

**Usage:**
```bash
# From docs/sims directory
cd docs/sims
python3 ../../src/utilities/update-image-metadata.py
```

**Requirements:**
- MicroSim must have a PNG file
- index.md must have YAML frontmatter

**Output:** Updated index.md files with image metadata

---

### 4. batch-add-lesson-plans.py

Adds comprehensive lesson plans to specified MicroSims.

**What it does:**
- Inserts pre-written lesson plans before References sections
- Each lesson plan includes:
  - Learning Objectives (Bloom's Taxonomy aligned)
  - Target Audience
  - 4 hands-on activities
  - Formative and summative assessments
  - Extension activities
- Updates quality scores (+10 points)

**Usage:**
```bash
# From docs/sims directory
cd docs/sims
python3 ../../src/utilities/batch-add-lesson-plans.py
```

**Note:** Currently contains lesson plans for 5 specific MicroSims:
- microsim-file-relationship-diagram
- mkdocs-github-pages-deployment
- orphaned-nodes-identification
- taxonomy-distribution-pie
- test-world-cities

To add more lesson plans, edit the `LESSON_PLANS` dictionary in the script.

---

### 5. iframe-border-cleanup.py

Automatically cleans up CSS files to create borderless designs optimized for iframe embedding.

**What it does:**
- Sets `background: aliceblue` for body, container, and diagram-container
- Removes all `padding` and `margin` (sets to 0px)
- Removes decorative `border-radius` and `box-shadow` properties
- Maintains other styling (fonts, colors, responsive design)

**Usage:**
```bash
# Process a single CSS file
python src/utilities/iframe-border-cleanup.py docs/sims/my-sim/style.css

# Process all MicroSim CSS files
python src/utilities/iframe-border-cleanup.py --all

# Preview changes without modifying files
python src/utilities/iframe-border-cleanup.py --dry-run docs/sims/my-sim/style.css
```

**Modified CSS Selectors:**
- **body**: `background: aliceblue`, `padding: 0px`
- **.container**: `background: aliceblue`, `padding: 0px`, `margin: 0 auto`, removes `border-radius` and `box-shadow`
- **.diagram-container**: `background: aliceblue`, `padding: 0px`, `margin: 0px`, removes `border-radius` and `box-shadow`

**When to Use:**
- Creating new MicroSims that need clean iframe embedding
- Converting existing MicroSims to borderless design
- Standardizing CSS across multiple MicroSims
- Removing decorative elements for embedded content

**Output Example:**
```
Processing: docs/sims/terminal-workflow-textbook/style.css
  ✓ Successfully cleaned up docs/sims/terminal-workflow-textbook/style.css

Processing: docs/sims/adding-taxonomy-workflow/style.css
  No changes needed - file already clean
```

**Note:** The script is idempotent - safe to run multiple times on the same file.

---

## Typical Workflow

### Initial Standardization (for new MicroSims)

```bash
cd docs/sims

# 1. Add structural elements
python3 ../../src/utilities/batch-standardize.py

# 2. Capture screenshots
bash ../../src/utilities/batch-capture-screenshots.sh

# 3. Update image metadata
python3 ../../src/utilities/update-image-metadata.py
```

After these steps, MicroSims typically achieve 80-85/100 quality scores.

### Adding Educational Content

```bash
cd docs/sims

# 4. Add lesson plans (edit script first to add your lesson plans)
python3 ../../src/utilities/batch-add-lesson-plans.py
```

After adding lesson plans, MicroSims typically achieve 90-95/100 quality scores.

### Reaching Perfect Scores

To achieve 100/100:
- Manually add comprehensive References sections (5 points)
- Add library-specific documentation (5 points)
  - p5.js: Link to p5.js editor sketch
  - Other libraries: Configuration examples, tips

---

## Quality Score Rubric

| Element | Points | Script that Adds It |
|---------|--------|---------------------|
| Title | 2 | batch-standardize.py |
| main.html | 10 | (manual) |
| YAML metadata | 3 | batch-standardize.py |
| Image metadata | 5 | update-image-metadata.py |
| metadata.json | 10 | batch-standardize.py |
| metadata.json valid | 20 | batch-standardize.py |
| iframe | 10 | batch-standardize.py |
| Fullscreen button | 5 | batch-standardize.py |
| iframe example | 5 | batch-standardize.py |
| Image file | 5 | batch-capture-screenshots.sh |
| Overview | 5 | batch-standardize.py |
| Lesson plan | 10 | batch-add-lesson-plans.py |
| References | 5 | (manual) |
| Type-specific | 5 | (manual) |
| **Total** | **100** | |

---

## Path Configuration

All scripts are designed to work from the repository root or from `docs/sims/`:

```python
# Path resolution in Python scripts
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent.parent
SIMS_DIR = REPO_ROOT / 'docs' / 'sims'
```

This ensures scripts work regardless of where they're called from.

---

## Site Configuration

The `SITE_URL` in batch-standardize.py should match your GitHub Pages URL:

```python
SITE_URL = "https://dmccreary.github.io/claude-skills"
```

Update this if deploying to a different domain.

---

## Error Handling

All scripts include:
- Try-catch blocks for individual MicroSim failures
- Continuation on error (one failure doesn't stop batch processing)
- Summary reports showing successes and failures

Example output:
```
✓ Successful: 28
✗ Failed: 1
```

---

## Dependencies

**Python Scripts:**
- Python 3.7+
- Standard library only (no external packages)

**Shell Scripts:**
- Bash
- Google Chrome (for screenshots)

---

## Related Documentation

- [MicroSim Standardization Skill](../../skills/microsim-standardization/)
- [MicroSim Screen Capture Skill](../../skills/microsim-screen-capture/)
- [Quality Report Generator](../book-metrics/microsim-quality-report.py)

---

## License

All scripts are part of the claude-skills repository and follow the same license.
