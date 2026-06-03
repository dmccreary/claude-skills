# Book Metrics

Generate comprehensive quantitative metrics for an intelligent textbook:
content volume, educational components, and interactive elements. Use this to
track progress, prepare status reports, assess completeness before publication,
or estimate the printed-page equivalent of the digital book.

## What It Produces

Running the metrics tool writes/updates three files in `docs/learning-graph/`:

1. **`book-metrics.md`** — overall book statistics (Book Composition table +
   Student-Facing Content Metrics table).
2. **`chapter-metrics.md`** — per-chapter breakdown (sections, diagrams,
   equations, words, links, quiz questions, references).
3. **`book-metadata.json`** — the machine-readable `metrics` block of book-wide
   totals (see [Book Metadata JSON](#book-metadata-json) below). Created during
   learning-graph generation and **merged in place** here; author fields are
   preserved.

## Prerequisites

- A `docs/` directory with the textbook content.
- `docs/chapters/NN-*/index.md` chapter directories (numbered, each with an `index.md`).
- `$BK_HOME` exported (the user's profile sets it to the `claude-skills`
  checkout) and `bk-generate-book-metrics` on `$PATH` — the same convention used
  by `bk-diagram-reports`.

Optional inputs that enrich the metrics (each is counted only if present):

- `docs/learning-graph/learning-graph.csv` (concepts)
- `docs/glossary.md` (glossary terms), `docs/faq.md` (FAQs)
- `docs/sims/` (MicroSims), `docs/stories/` (stories)
- `docs/img/mascot/` (mascot poses), `docs/appendices/` (appendix pages)
- per-chapter `quiz.md` and `references.md`
- `mkdocs.yml` `extra.development_stage` (development stage)

## How to Run

```bash
# Primary — the wrapper resolves $BK_HOME/src/book-metrics/book-metrics.py
# Run from the project root (the directory containing docs/).
bk-generate-book-metrics

# Fallback if bk-generate-book-metrics is not on $PATH:
python3 "$BK_HOME/src/book-metrics/book-metrics.py" docs
```

The Python script is the single source of truth at
`src/book-metrics/book-metrics.py` in the `claude-skills` repo — do not copy it
elsewhere. If `bk-generate-book-metrics` reports "command not found", make sure
`~/.local/bin` is on `$PATH` (it symlinks the wrapper in
`claude-skills/scripts/`).

## Book Composition

`book-metrics.md` opens with a **Book Composition** table covering the twelve
tracked elements of an intelligent textbook, each labeled *Required*,
*Recommended*, or *Optional* (a required element that is still missing is
flagged with ⚠️):

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

## Student-Facing Content Metrics

A second table provides the deeper content counts, excluding administrative
directories (`prompts/`, `learning-graph/`):

| Metric | Description |
|--------|-------------|
| Diagrams | H4 headers starting with `#### Diagram:` |
| Equations | LaTeX expressions using `$` and `$$` delimiters |
| Total Words | All words in markdown (excluding code blocks and URLs) |
| Links | Markdown-formatted hyperlinks `[text](url)` |
| Equivalent Pages | Estimated pages from words + visuals |

**Page calculation formula:**

```
Pages = (Total Words ÷ 250) + (Diagrams × 0.25) + (MicroSims × 0.5)
```

Assumptions: 250 words per printed page, each diagram 0.25 page, each MicroSim
0.5 page.

## Book Metadata JSON

The script also creates or updates `docs/learning-graph/book-metadata.json`,
the same file created when the learning graph is generated (it holds
descriptive fields: title, description, creator, cover image, repository,
license, etc.). Each run **merges** a single `metrics` object plus two
provenance fields without disturbing any author-supplied fields:

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

- **Only book-wide totals** go in the `metrics` object. Per-chapter breakdowns
  are intentionally excluded — those live only in `chapter-metrics.md`.
- **Author fields are preserved.** Only the `metrics` block and the two
  `metricsGenerated*` fields are written; everything else is left untouched.
- **Botany books** (those with a `docs/plants/` directory) additionally get
  `speciesCards`, `speciesCardsWithIllustration`, `speciesCardsWithPhotos`,
  and `speciesCardsWithQuickFacts` totals.
- **Safety:** if the existing `book-metadata.json` cannot be parsed as a JSON
  object, the script leaves it untouched and prints a warning rather than risk
  clobbering the author's metadata.

## Add to Navigation

After generating, add the reports to `mkdocs.yml`:

```yaml
nav:
  - Learning Graph:
    - Book Metrics: learning-graph/book-metrics.md
    - Chapter Metrics: learning-graph/chapter-metrics.md
```

## Troubleshooting

- **No chapters found** — ensure chapter directories live in `docs/chapters/`,
  are named `NN-chapter-name/`, and each contains an `index.md`.
- **Concept count is zero** — verify `docs/learning-graph/learning-graph.csv`
  exists, is UTF-8, and has a header row plus data rows.
- **`bk-generate-book-metrics: command not found`** — confirm `~/.local/bin` is
  on `$PATH`; use the `python3 "$BK_HOME/src/book-metrics/book-metrics.py" docs`
  fallback otherwise.
- **`$BK_HOME` errors** — the wrapper requires `$BK_HOME` to point at the
  `claude-skills` checkout (e.g. `export BK_HOME=$HOME/Documents/ws/claude-skills`).
- **Word counts look off** — the script excludes code blocks and URLs; check for
  large code blocks or malformed markdown if numbers seem wrong.
