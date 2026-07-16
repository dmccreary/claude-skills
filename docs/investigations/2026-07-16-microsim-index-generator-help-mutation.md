---
title: MicroSim Index Generator Mutates the Working Tree on Help
date: 2026-07-16
status: resolved
severity: high
component: skills/microsim-utils/scripts/generate-microsim-index.py
trello: https://trello.com/b/1otItvDs/tomas
---

# MicroSim Index Generator Mutates the Working Tree on Help

## Symptom

Running the generator with the conventional discovery command below did not
show usage information:

```bash
python3 skills/microsim-utils/scripts/generate-microsim-index.py --help
```

Instead, the script immediately scanned `docs/sims`, added missing frontmatter
descriptions, replaced the MicroSim catalog, and replaced the screenshot TODO.
The first observed run changed three tracked files in the caller's repository.

## Preserved evidence

- The pre-fix command printed `Processed 90 MicroSims` and
  `Missing screenshots logged: 1` instead of help.
- Its generated patch changed `docs/sims/index.md`, `docs/sims/TODO.md`, and
  `docs/sims/grid-overlay-test/index.md`.
- The patch was frozen before the three accidental changes were reversed.
- The original script had no argument parser, `main()` boundary, project-root
  validation, or preview mode. Its filesystem reads and writes executed at
  module import time.

## Initial hypotheses

| Hypothesis | Prior | Evidence | Status |
| --- | ---: | --- | --- |
| Top-level execution ignores every CLI argument | 85% | The source contains no argument parser and reaches writes unconditionally | Confirmed |
| The command selected the wrong generator through PATH | 5% | It used an explicit repository path | Refuted |
| A generated-project hook rewrote the files after exit | 5% | The writes occur directly in the script | Refuted |
| None of the listed causes | 5% | Reserved for an unobserved execution path | Refuted by source trace |

## Root cause

The script was written as an executable sequence rather than a command-line
program. Importing or invoking it immediately used the caller's current
directory as the project root and performed writes. Because no parser owned the
command boundary, `--help` was merely an unused string in `sys.argv`.

The relative `docs/sims` path compounded the problem: an exploratory command
could mutate whichever repository happened to be the current working
directory, provided it exposed a compatible-looking path.

## Remediation

1. Move all behavior behind `main()` and `if __name__ == "__main__"`.
2. Add `argparse`, including `--project-dir`, `--course-name`, and `--dry-run`.
3. Resolve and validate the project root before accessing catalog files.
4. Separate discovery and rendering from the write phase.
5. Derive the course name from `mkdocs.yml` instead of hard-coding a title.
6. Require both `main.html` and `index.md` when cataloging runnable MicroSims,
   thereby excluding support-only directories.
7. Add subprocess tests that hash the entire fixture before and after `--help`,
   `--dry-run`, and invalid-root calls.

## Verification

- Focused regression suite: 5/5 tests pass.
- `--help` returns exit code 0, displays both `--project-dir` and `--dry-run`,
  and leaves the source worktree unchanged.
- A dry run against X Marketing with actions.json reports 14 MicroSims, 14
  missing screenshots, and five missing descriptions.
- The SHA-256 aggregate for every file under the real book's `docs/sims`
  directory is identical before and after that dry run.
- An explicit fixture run still generates an alphabetized catalog, a
  screenshot TODO, and missing frontmatter descriptions.
- A runnable page without YAML frontmatter remains catalogable but is not
  rewritten merely to inject generated metadata.

## Closure criteria

- Help and dry-run paths are mechanically proven non-mutating.
- Invalid project roots fail before writes.
- Generation requires an explicit validated project boundary.
- Existing catalog-generation behavior remains covered by tests.
- The fix is merged, independently read back from the target branch, and linked
  from this record.
- The durable command-boundary lesson is captured under `docs/solutions/`.

## Resolution evidence

- Fix PR: [#12](https://github.com/yaniv256/dmccreary-claude-skills/pull/12)
- Focused CLI regressions: 5/5 passed.
- Repository Python tests: 28/28 passed.
- Real-book dry run: 14 candidates, 14 missing screenshots, five missing
  descriptions, and no file changes.
- Durable learning:
  [CLI Introspection Must Not Cross the Write Boundary](../solutions/logic-errors/cli-introspection-must-not-cross-the-write-boundary.md)

Merge commit and independent default-branch verification remain pending.
