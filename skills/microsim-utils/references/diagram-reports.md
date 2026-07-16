# Diagram Specification Reports

> Formerly the standalone skill `diagram-reports-generator`.

## Scope

This route inventories **planned diagram and MicroSim specification blocks** in
an intelligent textbook. It recognizes a numbered chapter containing a
`#### Diagram: Title` heading followed by a `<details>...</details>` block.

It does not discover rendered `<figure>` elements, Markdown images, iframes, or
MicroSim implementation directories. It also does not establish instructional
quality, accessibility, browser behavior, or implementation completeness. For a
mature book, use the repository's native visual and MicroSim audits instead.

## Use This Route When

- chapter authors use the legacy diagram-specification schema;
- a planning inventory of proposed visuals is needed;
- implementation status or stated Bloom levels must be summarized; or
- a CSV or HTML planning export is useful.

Do not use it as a publication-quality gate or as evidence that a completed book
has no visuals.

## Prerequisites

1. Run from the textbook repository root.
2. Confirm `docs/chapters/` uses one or both supported layouts:
   - flat: `docs/chapters/01-name.md`
   - nested: `docs/chapters/01-name/index.md`
3. Confirm the target content uses the recognized schema:

   ```markdown
   #### Diagram: Example title

   <details>
   <summary>Specification</summary>

   **Type:** MicroSim
   **Status:** Planned
   **Learning Objective:** Compare two outcomes.
   **Bloom's Taxonomy:** Analyzing
   </details>
   ```

4. Identify the canonical script inside the installed `microsim-utils` skill.
   Run that script directly. Do not copy it into the textbook; copied utilities
   drift from their source and make later fixes ambiguous.

## Run Non-Destructively First

Write the representative report to a temporary directory:

```bash
python3 /path/to/microsim-utils/scripts/diagram-report.py \
  --chapters-dir docs/chapters \
  --output-dir /tmp/diagram-report \
  --verbose
```

The command fails closed when:

- no supported chapter files exist;
- any chapter cannot be read or analyzed; or
- no recognized specification blocks exist.

An empty result usually means the schema does not fit the book, not that the
book has no visuals. Use `--allow-empty` only when an empty *specification*
report is explicitly intended.

## Review the Evidence Boundary

For each extracted specification, the report records:

- source chapter and title;
- stated status and type;
- stated Bloom levels and learning objective;
- the number of UI-keyword mentions; and
- a coarse planning heuristic labelled Easy, Medium, Hard, or Very Hard.

The UI count is a text-occurrence count, not a count of implemented controls.
The difficulty value is a heuristic derived from those mentions and feature
words. Neither value is a quality score or a measured engineering estimate.

Before publishing any report, compare its rows with the source blocks and keep
the textbook's local validators, rendered browser checks, accessibility checks,
and instructional review authoritative.

## Generate a Repository Report

After the temporary output is reviewed:

```bash
python3 /path/to/microsim-utils/scripts/diagram-report.py \
  --chapters-dir docs/chapters \
  --output-dir docs/learning-graph
```

Markdown output creates:

- `diagram-table.md`
- `diagram-details.md`

Alternative formats:

```bash
python3 /path/to/microsim-utils/scripts/diagram-report.py --format csv
python3 /path/to/microsim-utils/scripts/diagram-report.py --format html
```

Only add generated files to `mkdocs.yml` after verifying that their source links
resolve for the book's chapter layout. Generated planning reports should not be
silently presented as learner-facing content.

## Failure Modes

| Symptom | Interpretation | Response |
| --- | --- | --- |
| No numbered chapters | Unsupported or wrong project path | Correct `--chapters-dir`; do not create an empty report |
| Numbered chapters, zero specs | The book does not use the legacy schema | Use a native rendered-visual inventory or explicitly allow an empty spec report |
| Missing fields | Source spec omits optional metadata | Correct the source if the metadata matters; do not infer authority |
| Broken source links | Report and chapter layout disagree | Treat as a defect and fix the canonical script |
| Plausible but surprising difficulty | Keyword heuristic is too coarse | Review manually; never use it as a quality gate |

## Bundled Resource

`scripts/diagram-report.py` is the canonical implementation for this route. The
legacy `bk-diagram-reports` command delegates to it so the command and skill do
not maintain separate copies.
