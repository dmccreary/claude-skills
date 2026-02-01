# Feature Checklist Generator

## Purpose

Generates a comprehensive feature checklist for an intelligent textbook by scanning the project's `mkdocs.yml` configuration and `docs/` directory to automatically detect which features are implemented.

## When to Use

Use this feature when:

- Starting a new textbook project to establish a baseline
- Reviewing project status before a release
- Comparing your textbook's features against others
- Identifying gaps and prioritizing next steps
- Creating documentation for stakeholders

## Trigger Keywords

- `feature checklist`
- `generate feature checklist`
- `feature status`
- `what features do I have`

## Workflow

### Step 1: Verify Prerequisites

Check that the project has:

1. A valid `mkdocs.yml` file in the project root
2. A `docs/` directory with content

If missing, inform the user and exit.

### Step 2: Run the Generator Script

Execute the feature checklist generator Python script:

```bash
# From the project directory
python ~/.claude/skills/book-installer/scripts/generate-feature-checklist.py .

# Or specify paths explicitly
python ~/.claude/skills/book-installer/scripts/generate-feature-checklist.py /path/to/project --output docs/feature-checklist.md
```

**Options:**
- `--dry-run` or `-n`: Print to stdout instead of writing file
- `--output` or `-o`: Specify output path (default: docs/feature-checklist.md)
- `--save-json` or `-j`: Also save detection results as JSON for debugging

**Example with all options:**
```bash
python ~/.claude/skills/book-installer/scripts/generate-feature-checklist.py . \
    --output docs/feature-checklist.md \
    --save-json logs/feature-detection.json
```

### Step 3: Review Generated Checklist

The script automatically:
- Scans mkdocs.yml for configuration-based features
- Checks docs/ directory for file-based features
- Counts chapters, MicroSims, glossary terms, FAQ questions, and quizzes
- Generates the markdown file with status icons:
  - `:white_check_mark:` for detected features
  - `:x:` for missing features

### Step 4: Customize for Project

Replace placeholders in the template:

- `{BOOK_TITLE}` - From `site_name` in mkdocs.yml
- `{CHAPTER_COUNT}` - Count of chapter directories
- `{MICROSIM_COUNT}` - Count of sims directories
- `{GLOSSARY_TERM_COUNT}` - Count of terms in glossary.md
- `{FAQ_COUNT}` - Count of questions in faq.md
- `{QUIZ_COUNT}` - Count of quiz.md files

### Step 5: Update Navigation

Add to `mkdocs.yml` navigation if not present:

```yaml
nav:
  # ... existing nav ...
  - Feature Checklist: feature-checklist.md
```

## Feature Detection Logic

The Python script checks for features using these patterns:

### Basic Features (from mkdocs.yml)

| Feature | Detection Method |
|---------|-----------------|
| Navigation sidebar | Always present with MkDocs Material |
| Search functionality | `plugins: - search` or default |
| Site title | `site_name:` present |
| Site author | `site_author:` present |
| GitHub repository | `repo_url:` present |
| Custom logo | `theme.logo:` present |
| Custom favicon | `theme.favicon:` present |
| Color theme | `theme.palette:` present |
| Footer navigation | `navigation.footer` in features |
| Navigation expand | `navigation.expand` in features |
| Back to top | `navigation.top` in features |
| Breadcrumbs | `navigation.path` in features |
| Section index | `navigation.indexes` in features |

### Content Enhancement Features

| Feature | Detection Method |
|---------|-----------------|
| GLightbox | `- glightbox` in plugins |
| KaTeX | `pymdownx.arithmatex` in extensions AND `katex` in extra_javascript |
| MathJax | `pymdownx.arithmatex` in extensions AND `mathjax` in extra_javascript |
| Admonitions | `- admonition` in extensions |
| Code copy button | `content.code.copy` in features |
| Syntax highlighting | `pymdownx.highlight` in extensions |
| Tabbed content | `pymdownx.tabbed` in extensions |
| Task lists | `pymdownx.tasklist` in extensions |
| Mark/highlight | `pymdownx.mark` in extensions |
| Strikethrough | `pymdownx.tilde` in extensions |
| Magic links | `pymdownx.magiclink` in extensions |
| Snippets | `pymdownx.snippets` in extensions |
| Emoji | `pymdownx.emoji` in extensions |
| Collapsible details | `pymdownx.details` in extensions |

### Site-Wide Resources (from docs/)

| Feature | Detection Method |
|---------|-----------------|
| Glossary | `docs/glossary.md` exists |
| FAQ | `docs/faq.md` exists |
| References | `docs/references.md` exists |
| Custom CSS | `docs/css/*.css` exists OR `extra_css` in mkdocs.yml |
| Custom JavaScript | `docs/js/*.js` exists OR `extra_javascript` in mkdocs.yml |
| Google Analytics | `analytics.property` in extra |

### Publishing Features

| Feature | Detection Method |
|---------|-----------------|
| Social media cards | `- social` in plugins |
| Edit page button | `edit_uri:` present |

### Advanced Features (from docs/)

| Feature | Detection Method |
|---------|-----------------|
| MicroSims | `docs/sims/` directory with subdirectories |
| MicroSim index | `docs/sims/index.md` exists |
| Per-chapter quizzes | `quiz.md` files in chapter directories |
| Course description | `docs/course-description.md` exists |
| Learning graph CSV | `docs/learning-graph/*.csv` exists |
| Learning graph JSON | `docs/learning-graph/*.json` exists |
| Graph viewer | `docs/sims/graph-viewer/` exists |
| Concept taxonomy | `docs/learning-graph/concept-taxonomy.md` exists |
| Book metrics | `docs/learning-graph/book-metrics.md` exists |
| Chapter metrics | `docs/learning-graph/chapter-metrics.md` exists |

### Content Generation (from docs/)

| Feature | Detection Method |
|---------|-----------------|
| Chapters | Count directories in `docs/chapters/` |
| License page | `docs/license.md` exists |
| Contact page | `docs/contact.md` exists |
| About page | `docs/about.md` exists |

## Output Files

1. **`docs/feature-checklist.md`** - The generated checklist with detected statuses
2. **`logs/feature-detection-{date}.json`** - Raw detection results for debugging

## Example Output

After running, the feature-checklist.md will show:

```markdown
| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| Navigation sidebar | :white_check_mark: | Trivial | Left-side menu showing all chapters |
| Custom logo | :white_check_mark: | Trivial | Found: img/logo.png |
| Glossary | :x: | Medium | Not found - run glossary-generator skill |
| MicroSims | :white_check_mark: | High | 12 simulations found in docs/sims/ |
```

## Customization

After generation, you should:

1. Review auto-detected statuses for accuracy
2. Add project-specific notes to the Notes column
3. Update the "Comparison with Other Books" section
4. Add any custom features unique to your project

## Troubleshooting

### False Negatives

If a feature shows as `:x:` but is actually implemented:
- Check file paths match expected locations
- Verify mkdocs.yml syntax is valid YAML
- Ensure feature uses standard naming conventions

### False Positives

If a feature shows as `:white_check_mark:` but isn't working:
- The detection only checks configuration, not functionality
- Test the feature manually after detection
- Check browser console for JavaScript errors

## Integration with Other Skills

This feature works well with:

- **book-metrics-generator** - For detailed content statistics
- **glossary-generator** - To implement missing glossary
- **faq-generator** - To implement missing FAQ
- **quiz-generator** - To implement missing quizzes
