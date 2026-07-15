# Book Metrics Layout Discovery Investigation

**Status:** Resolved upon merge of PR #2
**Observed:** 2026-07-15
**Affected component:** `src/book-metrics/book-metrics.py` v0.08

## Symptom

Running the generator against the mature `x-marketing-frontier-textbook`
repository completed successfully but published false canonical totals:

```json
{
  "concepts": 0,
  "chapters": 0,
  "microsims": 14,
  "words": 162054
}
```

The same source tree contains 12 numbered files under `docs/chapters/` and 158
concept records in `docs/learning-graph/concepts.csv`. The generated chapter
report consequently said `No chapters found.`

## Root Cause

The generator recognizes only one historical representation for each metric:

- chapters must be directories named with a numeric prefix and containing
  `index.md`;
- concepts must be rows in `docs/learning-graph/learning-graph.csv`.

The mature textbook uses equivalent, learner-facing representations:

- numbered chapter files such as `01-outcomes-before-content.md`;
- the normalized concept inventory `concepts.csv`, accompanied by separate
  dependency and taxonomy files.

Because missing discovery inputs are treated as zero rather than an error, the
layout mismatch crossed the canonical metrics boundary as plausible-looking
data. Every publishing route that consumes `book-metrics.json` could then repeat
those false totals.

## Remediation Plan

1. Preserve directory-based discovery as a supported legacy layout.
2. Recognize numbered flat Markdown chapter files without counting the chapter
   overview `index.md`.
3. Prefer directory chapters when both representations exist for the same
   chapter number, preventing double counting.
4. Read `learning-graph.csv` when present and otherwise fall back to
   `concepts.csv`.
5. Generate correct per-chapter metrics and links for both layouts.
6. Add isolated regression tests for legacy, flat, and mixed layouts.
7. Regenerate the affected textbook's canonical metrics and verify 12 chapters,
   158 concepts, valid schema, and working report links.
8. Update public documentation and compound the layout-discovery contract.

## Closure Criteria

- Regression tests fail on v0.08 and pass with the remediation.
- Existing directory-layout behavior remains covered and passing.
- The affected textbook produces 12 chapters and 158 concepts.
- `book-metrics.json` passes the schema validator.
- The source fix is merged and the downstream publisher task is restored.

## Verification Evidence

- Six layout-discovery regression tests pass, including legacy, flat, mixed,
  duplicate-prefix, title-fallback, and concept-precedence cases.
- The affected mature textbook generates 12 chapters and 158 concepts.
- All 12 generated chapter-report links resolve to existing source files.
- The generated `book-metrics.json` passes the Draft 2020-12 schema validator.
- A copied legacy textbook generates 17 chapters and 200 concepts, preserves 14
  chapter quizzes, and resolves all 17 generated chapter links.
- The reusable failure pattern is recorded in
  `docs/solutions/logic-errors/book-metrics-layout-discovery.md`.
- Review and merge record: https://github.com/yaniv256/dmccreary-claude-skills/pull/2
