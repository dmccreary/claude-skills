# Session Log — Learning Graph Regeneration

**Skill:** learning-graph-generator v0.06
**Date:** 2026-08-22
**Trigger:** Regenerate the learning graph after the course description was rewritten.

## Context

The previous learning graph held 200 concepts and 227 edges, derived from the
original course description written when the repository contained only a handful
of skills. That description was rewritten in the preceding turn to cover the
current library: 14 active skills, 5 meta-skills, 99 reference guides, 80 Python
programs, token-optimization practice, verified image generation, and
domain-specific extension. The graph no longer matched its source.

## Steps Executed

| Step | Action | Result |
|------|--------|--------|
| 1 | Course description quality assessment | **Skipped.** Frontmatter carried `quality_score: 95`, above the 85 threshold. Skipping is the documented token saving. |
| 2 | Concept enumeration | 570 concepts |
| 3 + 6 | Dependency mapping with taxonomy | Written as a single taxonomy-enriched CSV rather than two passes |
| 4 | Quality validation | Valid DAG, 0 cycles, 0 orphans, 1 connected component |
| 5 | Concept taxonomy | 14 categories |
| 5b | taxonomy-names.json | 14 human-readable names |
| 7 | metadata.json | Title, creator, date, version 2.0, license |
| 8 | color-config.json | 14 colors from the recommended distinct palette |
| 9 | learning-graph.json | 570 nodes, 1137 edges, 14 groups; schema validation passed |
| 10 | Taxonomy distribution | Largest category 11.6%, well under the 30% ceiling |
| 11 | index.md | Stale counts corrected |

## Deviation From the Skill Workflow

**Steps 3 and 6 were combined.** The skill writes the dependency CSV first and
adds the taxonomy column in a later pass. Writing both at once avoided emitting
570 concept labels twice. `concept-list.md` was then derived from the CSV by
script rather than authored separately, so the labels were written exactly once.

## Defect Found and Fixed

`docs/learning-graph/analyze-graph.py` was a stale copy that reported
**"Valid DAG Structure: No"** while simultaneously reporting **0 cycles**.

Cause: its `verify_dag()` seeded Kahn's algorithm from nodes whose in-degree
counted *dependents* (terminal nodes), then relaxed edges in the
*prerequisite → dependent* direction. The two orientations are inconsistent, so
any concept with dependents but no prerequisites — every foundational concept —
could never be dequeued. `len(processed) < len(concepts)` then reported a false
negative on any well-formed graph.

The copy in `skills/learning-graph-generator/` was already correct and also
carried `find_orphaned_nodes()` plus a corrected terminal-node definition. The
stale project copies were replaced from the skill:

- `analyze-graph.py` (fixes the false DAG failure, adds orphan detection)
- `csv-to-json.py`
- `taxonomy-distribution.py`
- `validate-learning-graph.py`

The graph was independently confirmed acyclic before the fix: all 570 nodes
topologically sort, and every dependency points to a strictly lower ConceptID,
which is a structural proof of acyclicity.

## Quality Adjustment

The first dependency pass produced an average of **1.69** prerequisites per
concept, below the 2–4 band in the project quality standards. A second
prerequisite was added to 184 under-connected concepts, all pointing to lower
identifiers so acyclicity was preserved by construction. Final average: **2.02**.

## Final Metrics

| Metric | Value |
|--------|-------|
| Concepts | 570 |
| Edges | 1137 |
| Average dependencies | 2.02 |
| Foundational concepts | 6 |
| Terminal nodes | 219 (38.4%) |
| Orphaned nodes | 0 |
| Connected components | 1 |
| Cycles | 0 |
| Taxonomy categories | 14 |
| Largest category | Interactive Simulations, 11.6% |
| Longest dependency chain | 26 |

## Script Versions Used

- `analyze-graph.py` — synced from skill, includes orphaned-node detection
- `csv-to-json.py` — v0.04+ (auto font-color selection, 24-color palette)
- `taxonomy-distribution.py` — invoked with `taxonomy-names.json` as third
  argument so the report shows category names rather than raw identifiers
- `validate-learning-graph.py` — requires both a data file and a schema file

## Downstream Impact

Artifacts generated from the previous 200-concept graph are now inconsistent
with it and were **not** regenerated in this session: chapter structure, chapter
content, quizzes, FAQ, diagram reports, and book metrics.
