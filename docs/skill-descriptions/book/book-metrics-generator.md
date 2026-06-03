# Book Metrics Generator

The book-metrics-generator skill automates the generation of comprehensive metrics
for intelligent textbooks. It analyzes the entire textbook structure and content
to produce detailed quantitative reports for tracking progress and identifying
areas needing attention.

## Key Capabilities

This skill generates two report files in the `docs/learning-graph/` directory:

1. **book-metrics.md** - Overall book statistics with links to relevant sections
2. **chapter-metrics.md** - Chapter-by-chapter breakdown in tabular format

## Metrics Analyzed

The skill analyzes and reports on:

- **Content Volume**: Word counts, page equivalents, chapter counts
- **Educational Components**: Concepts covered, glossary terms, FAQ entries
- **Assessment Elements**: Quiz questions by chapter and Bloom's level
- **Interactive Elements**: MicroSims, diagrams, equations
- **Navigation**: Internal links, external references

## When to Use

Use this skill when:

- Tracking progress on intelligent textbook development
- Preparing status reports for stakeholders
- Assessing content completeness before publication
- Analyzing distribution of educational elements across chapters
- Estimating physical page equivalent of digital content
- Comparing metrics over time to track growth

## Prerequisites

The intelligent textbook project should have:

- A `docs/` directory containing the textbook content
- Chapters in `docs/chapters/` following numbered naming convention
- Standard MkDocs Material structure

## Output Example

The book-metrics.md file includes sections for:

- Summary statistics with links
- Content breakdown by type
- Chapter-by-chapter comparison table
- Visualization recommendations

## Shell Script Access

!!! note "Now part of book-installer"
    Book metrics is no longer a standalone skill — the capability now lives as
    the **book-metrics** guide inside the `book-installer` meta-skill. Invoke
    `book-installer` and ask for book metrics, or run the shell wrapper below.

For efficiency, you can run the metrics generator directly via the shell wrapper:

```bash
bk-generate-book-metrics
```

This wrapper runs `$BK_HOME/src/book-metrics/book-metrics.py` against the
project's `docs/` directory. If it is not on your `$PATH`, use the fallback
`python3 "$BK_HOME/src/book-metrics/book-metrics.py" docs`.

## Integration

Book metrics is typically generated after significant content development or as
part of regular project status reporting. It works with any MkDocs Material-based
intelligent textbook following the standard structure.
