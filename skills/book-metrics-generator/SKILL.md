---
name: book-metrics-generator
description: This skill generates comprehensive metrics reports for intelligent textbooks built with MkDocs Material, analyzing chapters, concepts, glossary terms, FAQs, quiz questions, diagrams, equations, MicroSims, word counts, and links. Use this skill when working with an intelligent textbook project that needs quantitative analysis of its content, typically after significant content development or for project status reporting. The skill creates two markdown files - book-metrics.md with overall statistics and chapter-metrics.md with per-chapter breakdowns - in the docs/learning-graph/ directory.
---

# Book Metrics Generator

## Overview

This skill automates the generation of comprehensive metrics for intelligent textbooks. It analyzes the entire textbook structure and content to produce three outputs:

1. **book-metrics.md** - Overall book statistics with links to relevant sections
2. **chapter-metrics.md** - Chapter-by-chapter breakdown in tabular format
3. **book-metadata.json** - Machine-readable book-wide totals (created or updated in place, preserving any author-supplied fields) for use in the intelligent-textbooks case-studies index

The metrics provide quantitative insights into content volume, educational components, and interactive elements, helping authors track progress and identify areas needing attention.

## Running the Shell Script Directly

Tell the user the following:

We setup this skill mostly to automate the process of installing the shell script.
The shell script calls a Python program that does the work of building the metrics files.
If you want to save a few tokens, after the skill is installed (a symbolic link really)
you can run the following from your terminal:

```sh
~/.claude/skills/book-metrics-generator/scripts/book-metrics-generator.sh
```

Just make sure that you do a git pull on the claude-skills repo to get the latest version.

## When to Use This Skill

Use this skill when:

- Tracking progress on intelligent textbook development
- Preparing status reports for stakeholders or collaborators
- Assessing content completeness before publication
- Analyzing the distribution of educational elements across chapters
- Estimating the physical page equivalent of the digital textbook
- Auditing content after major updates or additions
- Comparing metrics over time to track growth

The skill is designed for MkDocs Material-based intelligent textbooks following the structure defined in the intelligent-textbook skill.

## Prerequisites

The intelligent textbook project should have:

- A `docs/` directory containing the textbook content
- A `docs/chapters/` directory with chapter subdirectories (e.g., `01-chapter-name/`, `02-chapter-name/`)
- Each chapter directory containing an `index.md` file
- A `docs/learning-graph/` directory (will be created if it doesn't exist)

Optional components that enhance metrics:

- `docs/learning-graph/learning-graph.csv` - For concept counting
- `docs/glossary.md` - For glossary term counting
- `docs/faq.md` - For FAQ counting
- `docs/sims/` - For MicroSim counting
- `docs/stories/` - For story counting (story subdirectories with index.md)
- `docs/img/mascot/` - For mascot pose counting
- `docs/appendices/` (or `appendicies/`) - For appendix page counting
- Chapter-level `quiz.md` files - For quiz and quiz-question counting
- Chapter-level `references.md` files - For reference counting
- `mkdocs.yml` `extra.development_stage` (or course-description.md) - For development stage

## Usage

### Basic Workflow

To generate metrics for an intelligent textbook:

1. Navigate to the textbook project root directory
2. Execute the shell script:

```bash
./scripts/book-metrics-generator.sh
```

Or if the skill scripts are available:

```bash
bash /path/to/skill/scripts/book-metrics-generator.sh
```

3. Review the generated files:
   - `docs/learning-graph/book-metrics.md`
   - `docs/learning-graph/chapter-metrics.md`
   - `docs/learning-graph/book-metadata.json` (created or updated in place)

4. Update `mkdocs.yml` navigation to include the new metrics files:

```yaml
nav:
  - Learning Graph:
    - Book Metrics: learning-graph/book-metrics.md
    - Chapter Metrics: learning-graph/chapter-metrics.md
```

### Custom Docs Directory

To analyze a textbook in a non-standard location:

```bash
./scripts/book-metrics-generator.sh path/to/custom/docs
```

### Running the Python Script Directly

For more control or integration into custom workflows:

```bash
python3 scripts/book-metrics.py docs
```

## Book Metrics Collected

The **book-metrics.md** file opens with a **Book Composition** table covering the
twelve tracked elements of an intelligent textbook, each labeled *Required*,
*Recommended*, or *Optional* (a required element that is still missing is flagged
with ⚠️):

| # | Element | Status | Source |
|---|---------|--------|--------|
| 1 | Concepts | Required | Rows in learning-graph.csv |
| 2 | Chapters | Required | Chapter directories with index.md |
| 3 | MicroSims | Recommended | Directories in docs/sims/ with index.md |
| 4 | Stories | Optional | Story directories in docs/stories/ with index.md |
| 5 | Chapter Quizzes | Recommended | Chapters with a quiz.md (plus total questions) |
| 6 | Chapter References | Recommended | Chapters with references.md (plus total references) |
| 7 | Glossary Terms | Recommended | H4 headers in glossary.md |
| 8 | FAQs | Recommended | H3 headers in faq.md |
| 9 | Words | Required | Words across student-facing markdown |
| 10 | Mascot | Optional | Image poses in docs/img/mascot/ |
| 11 | Appendices | Optional | Pages in appendices/ (excluding index.md) |
| 12 | Development Stage | Required | mkdocs.yml `extra.development_stage` or course-description.md |

A second **Student-Facing Content Metrics** table provides the deeper content
counts:

| Category | Metric | Description |
|----------|--------|-------------|
| Visual | Diagrams | Count of H4 headers starting with "#### Diagram:" |
| Technical | Equations | LaTeX expressions using $ and $$ delimiters |
| Content | Total Words | All words in markdown files (excluding code and URLs) |
| Content | Links | Markdown-formatted hyperlinks [text](url) |
| Estimation | Equivalent Pages | Calculated pages based on words + visuals |

### Page Calculation Formula

Equivalent pages are estimated using:

```
Pages = (Total Words ÷ 250) + (Diagrams × 0.25) + (MicroSims × 0.5)
```

Assumptions:
- 250 words per printed page
- Each diagram occupies 0.25 page
- Each MicroSim occupies 0.5 page

## Book Metadata JSON

In addition to the two markdown reports, the script creates or updates
`docs/learning-graph/book-metadata.json`. This is the same file that is
created when the learning graph is generated; it holds descriptive fields for
the book (title, description, creator, cover image, repository, license, etc.).

Each time the metrics script runs it **merges** a single `metrics` object into
that file and stamps two provenance fields, **without disturbing any of the
author-supplied fields**:

```json
{
  "title": "My Intelligent Textbook",
  "description": "...",
  "creator": "Author Name",
  "metrics": {
    "concepts": 200,
    "chapters": 12,
    "microsims": 18,
    "stories": 2,
    "glossaryTerms": 200,
    "faqs": 40,
    "quizQuestions": 120,
    "chapterQuizzes": 12,
    "chapterReferences": 12,
    "references": 120,
    "diagrams": 30,
    "equations": 45,
    "words": 45000,
    "links": 300,
    "appendices": 3,
    "mascotImages": 7,
    "developmentStage": "Complete",
    "equivalentPages": 250
  },
  "metricsGeneratedBy": "Book Metrics Python Program v0.07",
  "metricsGeneratedOn": "June 03, 2026 at 10:13 AM"
}
```

These are the book-wide totals that feed the case-study cards in the
[intelligent-textbooks](https://github.com/dmccreary/intelligent-textbooks)
`docs/case-studies/index.md` page (e.g. "200 Concepts · 12 Chapters · 18
MicroSims · 45K Words · 200 Glossary Terms").

**Rules the script follows for `book-metadata.json`:**

- **Only book-wide totals** go in the `metrics` object. Per-chapter
  breakdowns are intentionally excluded — those live only in
  `chapter-metrics.md`.
- **Author fields are preserved.** Only the `metrics` block and the two
  `metricsGenerated*` provenance fields are written; everything else the
  author put in the file is left untouched.
- **Botany books** (those with a `docs/plants/` directory) additionally get
  `speciesCards`, `speciesCardsWithIllustration`, `speciesCardsWithPhotos`,
  and `speciesCardsWithQuickFacts` totals.
- **Safety:** if the existing `book-metadata.json` cannot be parsed as a JSON
  object, the script leaves it untouched and prints a warning rather than
  risk clobbering the author's metadata.

## Chapter Metrics Collected

The **chapter-metrics.md** file contains a table with these columns:

| Column | Description |
|--------|-------------|
| Chapter | Chapter number (leading zeros removed) |
| Name | Chapter title extracted from index.md H1 header |
| Sections | Count of H2 and H3 headers in chapter markdown files |
| Diagrams | Count of "#### Diagram:" headers in chapter |
| Equations | LaTeX expressions in the chapter |
| Words | Total word count for all markdown in the chapter |
| Links | Markdown-formatted hyperlinks in the chapter |
| Quiz | Number of quiz questions in the chapter's quiz.md (0 if none) |
| Refs | Number of references in the chapter's references.md (0 if none) |

This table enables quick identification of:
- Chapters with insufficient content
- Uneven content distribution
- Chapters lacking visual aids
- Outlier chapters requiring review

## Technical Details

### File Detection Patterns

The Python script uses these patterns to count elements:

- **Chapters**: Directories in `docs/chapters/` containing `index.md`
- **Concepts**: Rows in `docs/learning-graph/learning-graph.csv` (excluding header)
- **Glossary Terms**: `^####` headers in `glossary.md`
- **FAQs**: `^###` headers (not `####`) in `faq.md`
- **Quiz Questions**: `^####\s+\d+\.` and legacy `^##` patterns in all `quiz.md` files
- **Chapter Quizzes**: Chapter directories containing a `quiz.md` file
- **Chapter References**: Chapter directories containing a `references.md` file; references counted via `^\s*\d+\.\s+` numbered list items
- **Stories**: Subdirectories in `docs/stories/` with `index.md`
- **Mascot**: Image files (png/jpg/jpeg/gif/svg/webp) in `docs/img/mascot/`
- **Appendices**: Markdown pages (and subdirs with `index.md`) in `docs/appendices/` or `docs/appendicies/`, excluding `index.md`
- **Development Stage**: `development[-_]stage:` value in `mkdocs.yml`, then `course-description.md`; "Not specified" if absent
- **Diagrams**: `^####\s+Diagram:` pattern (multiline flag)
- **Equations**: `\$[^$]+\$` (inline) and `\$\$[^$]+\$\$` (display)
- **MicroSims**: Subdirectories in `docs/sims/` with `index.md`
- **Links**: `\[([^\]]+)\]\(([^)]+)\)` pattern

### Word Counting Methodology

To ensure accurate word counts, the script:

1. Removes code blocks (triple backticks)
2. Removes inline code (single backticks)
3. Removes URLs (http/https links)
4. Counts word boundaries using `\b\w+\b` pattern

### Error Handling

The script gracefully handles:

- Missing directories (returns 0 for counts)
- Missing files (returns 0 for counts)
- Malformed CSV files (prints warning, returns 0)
- Encoding issues (UTF-8 with fallback)
- Permission errors (prints warning, continues)

## Extending the Metrics

### Adding New Book-Level Metrics

To add a new book-level metric:

1. Add a counting method to the `BookMetricsGenerator` class:

```python
def count_new_metric(self) -> int:
    """Count the new metric.

    Returns:
        Number of items
    """
    # Implementation here
    pass
```

2. Update `generate_book_metrics_md()` to call the new method:

```python
new_metric = self.count_new_metric()
```

3. Add a row to the markdown table:

```python
md += f"| New Metric | {new_metric} | [Link](path) | Description |\n"
```

4. Add explanation in the "Metrics Explanation" section

### Adding New Chapter-Level Metrics

To add a new chapter-level metric:

1. Update `get_chapter_metrics()` to compute the new metric:

```python
def get_chapter_metrics(self, chapter: Dict[str, Any]) -> Dict[str, Any]:
    # Existing code...

    # Add new metric
    new_metric = self.count_new_metric_for_chapter(chapter)

    return {
        # Existing fields...
        'new_metric': new_metric
    }
```

2. Update `generate_chapter_metrics_md()` to include the new column:

```python
md += "| Chapter | Name | ... | New Metric |\n"
# In the row loop:
md += f"| {metrics['number']} | ... | {metrics['new_metric']} |\n"
```

3. Add explanation in the "Metrics Explanation" section

## Integration with Workflows

### After Content Generation

Run metrics generation after completing chapters:

```bash
# Generate chapter content
/skill intelligent-textbook

# Generate metrics
/skill book-metrics-generator

# Review progress
cat docs/learning-graph/book-metrics.md
```

### Continuous Integration

Add to `.github/workflows/metrics.yml`:

```yaml
name: Generate Metrics

on:
  push:
    paths:
      - 'docs/**/*.md'

jobs:
  metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate metrics
        run: python3 scripts/book-metrics.py docs
      - name: Commit metrics
        run: |
          git config user.name "GitHub Actions"
          git add docs/learning-graph/book-metrics.md
          git add docs/learning-graph/chapter-metrics.md
          git commit -m "Update metrics" || exit 0
          git push
```

### Pre-Deployment Checklist

Before deploying the textbook:

1. Run metrics generation
2. Verify all chapters have reasonable word counts (>1000 words)
3. Check that quiz questions exist for most chapters
4. Ensure MicroSims cover key concepts
5. Review total page count for scope appropriateness

## Troubleshooting

### No Chapters Found

**Symptom**: "No chapters found" in chapter-metrics.md

**Solution**: Ensure chapter directories:
- Are located in `docs/chapters/`
- Contain an `index.md` file
- Follow naming pattern: `NN-chapter-name/` (where NN is a number)

### Concept Count is Zero

**Symptom**: Concepts metric shows 0

**Solution**: Verify that:
- `docs/learning-graph/learning-graph.csv` exists
- CSV file has correct format (header row + data rows)
- CSV file is UTF-8 encoded

### Missing Metrics Files

**Symptom**: Metrics files not created

**Solution**: Check that:
- `docs/learning-graph/` directory exists (script creates it if missing)
- User has write permissions to the directory
- Python 3 is installed and accessible via `python3` command

### Incorrect Word Counts

**Symptom**: Word counts seem too high or too low

**Solution**: The script excludes code blocks and URLs. To verify:
- Check for large code blocks that should be excluded
- Review markdown files for formatting issues
- Ensure no binary or non-text files with .md extension

## Resources

### scripts/

This skill includes two executable scripts:

#### book-metrics-generator.sh

Bash wrapper script that:
- Validates the docs directory exists
- Checks for Python 3 installation
- Executes the Python metrics generator
- Provides user-friendly output

Default usage assumes `docs/` directory in current working directory.

#### book-metrics.py

Python 3 script that:
- Implements modular `BookMetricsGenerator` class
- Provides separate methods for each metric type
- Generates markdown-formatted output
- Handles errors gracefully with warnings
- Supports custom docs directory path

The Python script is designed for extensibility - new metrics can be added by implementing new counting methods and updating the markdown generation functions.

## Example Output

### Book Composition Table Sample

```markdown
| # | Element | Value | Status | Notes |
|---|---------|-------|--------|-------|
| 1 | Concepts | 200 | Required | Concepts from learning graph |
| 2 | Chapters | 12 | Required | Chapter directories with index.md |
| 3 | MicroSims | 18 | Recommended | Interactive simulations in docs/sims/ |
| 4 | Stories | 2 | Optional | Graphic-novel narratives in docs/stories/ |
| 5 | Chapter Quizzes | 12 / 12 | Recommended | Chapters with a quiz.md (120 questions total) |
| 6 | Chapter References | 12 / 12 | Recommended | Chapters with references.md (120 references total) |
| 7 | Glossary Terms | 200 | Recommended | Defined terms in glossary.md |
| 8 | FAQs | 40 | Recommended | Questions in faq.md |
| 9 | Words | 45,000 | Required | Words across student-facing markdown |
| 10 | Mascot | 7 | Optional | Mascot image poses in docs/img/mascot/ |
| 11 | Appendices | 3 | Optional | Appendix pages |
| 12 | Development Stage | Not specified | Required ⚠️ | From mkdocs.yml or course-description.md |
```

### Chapter Metrics Table Sample

```markdown
| Chapter | Name | Sections | Diagrams | Words |
|---------|------|----------|----------|-------|
| 1 | Introduction to Geometry | 8 | 3 | 3,200 |
| 2 | Points and Lines | 12 | 7 | 4,100 |
| 3 | Angles and Triangles | 15 | 12 | 5,500 |
```

## Related Skills

- **intelligent-textbook** - Complete textbook generation workflow (runs before metrics)
- **learning-graph-generator** - Creates the concept graph (provides concept count)
- **glossary-generator** - Generates glossary (provides glossary term count)
- **faq-generator** - Creates FAQ section (provides FAQ count)
- **quiz-generator** - Generates quizzes (provides quiz question count)
- **chapter-content-generator** - Creates chapter content (provides word count)
