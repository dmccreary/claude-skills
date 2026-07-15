---
title: Book metrics must discover equivalent source layouts before publishing totals
date: 2026-07-15
category: logic-errors
module: book-metrics
problem_type: logic_error
component: tooling
symptoms:
  - "The generator exited successfully while reporting zero chapters and zero concepts for a mature textbook."
  - "The canonical JSON passed schema validation even though its totals contradicted the source tree."
root_cause: logic_error
resolution_type: code_fix
severity: high
tags:
  - book-metrics
  - source-discovery
  - intelligent-textbooks
  - semantic-validation
---

# Book metrics must discover equivalent source layouts before publishing totals

## Problem

The book-metrics generator treated one historical filesystem convention as the
definition of a chapter and concept inventory. A mature textbook using
equivalent flat-file conventions therefore produced canonical, schema-valid
metrics that falsely claimed it contained no chapters or concepts.

## Symptoms

- A book with 12 numbered chapter files generated `chapters: 0`.
- A book with 158 rows in `concepts.csv` generated `concepts: 0`.
- `chapter-metrics.md` said `No chapters found.`
- The command exited zero and the JSON schema validator passed because zero is
  structurally valid for both fields.

## What Didn't Work

Treating command success as proof did not detect the defect. The generator wrote
all four expected artifacts without error. Schema validation did not detect it
either: a schema can prove that a value is a non-negative integer, but it cannot
prove that the value agrees with the source tree.

A first implementation keyed every discovered chapter by chapter number. That
would have prevented a flat-file duplicate from being counted during migration,
but it would also have silently collapsed multiple legacy directory chapters
sharing a numeric prefix. The final implementation preserves all directory
sources and suppresses only flat files whose number is already represented by a
directory source.

## Solution

Discovery now models both supported chapter representations explicitly:

```text
docs/chapters/01-foundations/index.md
docs/chapters/01-foundations.md
```

`count_chapters()` records each chapter's canonical content files, optional
resource directory, report link, and layout. Directory chapters are discovered
first; flat files are added only when no directory chapter has the same number
(`src/book-metrics/book-metrics.py:78-144`). Downstream chapter aggregation uses
the declared content files rather than assuming that every chapter path is a
directory (`src/book-metrics/book-metrics.py:737-792`).

Concept discovery preserves `learning-graph.csv` as the first choice and falls
back to `concepts.csv` when the combined graph file is absent
(`src/book-metrics/book-metrics.py:166-197`).

Regression coverage exercises:

- historical directory chapters and `learning-graph.csv`;
- flat chapter files and `concepts.csv`;
- mixed migrations where the directory source takes precedence;
- multiple legacy directories sharing a numeric prefix;
- precedence when both concept inventory files exist.

## Why This Works

The generator now separates semantic identity from physical representation. A
chapter is a numbered learner-facing source, not necessarily a directory. A
concept inventory is a CSV of concept records, not necessarily the historical
combined graph filename.

The fix remains backward compatible because the original directory and combined
graph formats retain precedence. The production-boundary check also proves both
sides of the contract:

- the mature flat-layout book yields 12 chapters, 158 concepts, 12 existing
  chapter links, and schema-valid JSON;
- a copied legacy directory-layout textbook yields 17 chapters, 200 concepts,
  17 existing chapter links, and its historical quiz counts.

## Prevention

- Test every supported source representation as a first-class fixture.
- When two layouts can coexist during migration, define precedence and test that
  it avoids double counting without deleting valid historical records.
- Validate canonical metrics semantically against known source counts in at
  least one mature downstream book; schema validation alone is insufficient.
- Treat suspicious required-element zeros as a discovery signal during
  publication review, even when the generator exits successfully.
- Keep generated report links in the acceptance test so discovery and
  publication navigation cannot drift independently.

## Related Issues

- Investigation record:
  `docs/investigations/2026-07-15-book-metrics-layout-discovery.md`

