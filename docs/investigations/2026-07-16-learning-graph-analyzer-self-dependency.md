---
title: Learning Graph Analyzer Crashes on Self-Dependencies
date: 2026-07-16
status: resolved
severity: high
component: skills/learning-graph-generator/analyze-graph.py
trello: https://trello.com/c/0HQv29lF/202-investigation-learning-graph-analyzer-crashes-on-self-dependency
---

# Learning Graph Analyzer Crashes on Self-Dependencies

## Symptom

A learning-graph CSV containing a concept that lists itself as a prerequisite
causes `analyze-graph.py` to raise `RecursionError` in `find_longest_chain`.
No quality report is written.

This contradicts both the skill contract, which says the analyzer checks
self-dependencies, and the report implementation, which previously printed
`Self-Dependencies: None detected` unconditionally.

## Minimal reproduction

```csv
ConceptID,ConceptLabel,Dependencies,TaxonomyID
1,Self Edge,1,TEST
```

```bash
python3 skills/learning-graph-generator/analyze-graph.py \
  /tmp/self.csv /tmp/report.md
```

Observed before remediation:

```text
RecursionError: maximum recursion depth exceeded
```

## Root cause

`generate_report` computed DAG validity and cycles, but called
`find_longest_chain` regardless of that result. The longest-path DFS memoized
only completed nodes and had no active-recursion guard, so a self-edge or any
larger cycle recursed indefinitely.

The same function then wrote a successful self-dependency line from a constant
string. No code actually collected or reported self-edges.

## Impact

- The analyzer fails on the invalid input it promises to diagnose.
- The user receives a Python stack trace instead of actionable concept IDs.
- Any cyclic graph can crash during longest-path analysis.
- The hardcoded status can falsely certify self-dependency safety if execution
  reaches report generation through a future control-flow change.

## Remediation plan

1. Add an explicit self-dependency detector that returns exact concept IDs.
2. Compute longest paths only after DAG validation succeeds.
3. For cyclic graphs, explain that longest-path analysis was skipped.
4. Report each self-dependent concept by ID and label.
5. Add regression fixtures for a self-edge, a multi-node cycle, and a valid
   three-node DAG.
6. Run focused tests, the analyzer against the existing sample graph, and the
   repository's existing Python test suites.
7. Merge the fix and update this record with immutable evidence.
8. Compound the validation-order lesson before closing the Trello
   investigation.

## Closure criteria

- A self-edge produces a complete report and no exception.
- The report says exactly how many self-dependencies were found and names them.
- A larger cycle also produces a complete report without attempting a longest
  path.
- A valid DAG retains its prior longest-path behavior.
- Focused and repository validation pass.
- The remediation is merged and the durable solution record is linked here.

## Resolution evidence

- Fix PR: [#7](https://github.com/yaniv256/dmccreary-claude-skills/pull/7)
- Merge commit: `e543355423c68b4f171465b92045734a527ba1ea`
- Merged at: 2026-07-16T04:29:07Z
- Focused analyzer tests: 3/3 passed.
- Existing sample graph: valid DAG, no self-dependencies, longest path 5.
- Repository Python tests: 22/22 passed across book installer, README
  validation, glossary scoring, learning-graph analysis, and book metrics.
- Closure and durable-learning PR:
  [#8](https://github.com/yaniv256/dmccreary-claude-skills/pull/8)
- Closure merge commit: `3f22411a36ae462cbd3fd3e03e49a87c87e98aea`
- Closure merged at: 2026-07-16T04:32:59Z
- Durable learning:
  [Validate Graph Preconditions Before Path Analysis](../solutions/logic-errors/validate-graph-preconditions-before-path-analysis.md)

All closure criteria are satisfied. Self-edges and larger cycles now produce a
complete diagnostic report without running longest-path analysis; valid DAGs
retain their prior path behavior.
