---
title: Iframe Tester Requires Playwright to Display Help
date: 2026-07-16
status: resolved
severity: medium
component: skills/microsim-utils/scripts/test-iframe-heights.py
trello: https://trello.com/c/4o9PtgT5/205-investigation-iframe-tester-imports-playwright-before-help
---

# Iframe Tester Requires Playwright to Display Help

## Symptom

The standard discovery command fails before displaying any options:

```bash
python3 skills/microsim-utils/scripts/test-iframe-heights.py --help
```

On a machine without the optional browser dependency, it exits 1 with
`ModuleNotFoundError: No module named 'playwright'` and a traceback.

## Root cause

`playwright.sync_api` was imported at module scope. Python therefore resolved
the optional dependency before `main()` created the argument parser. Argparse
never received `--help`, even though the help text is where a new operator
should discover the dependency and command shape.

## Remediation

1. Keep standard-library imports and parser construction dependency-free.
2. Parse arguments first, allowing argparse to own the help exit.
3. Load `sync_playwright` only when a browser test will run.
4. Convert an absent Playwright package into a concise parser error that names
   both required installation commands.
5. Return an integer from `main()` and keep process exit at the module boundary.
6. Test help under `python -S`, missing-dependency execution, and an installed
   Playwright-compatible execution path.

## Verification

- Focused regression suite covers all three CLI boundaries.
- Help exits zero and contains `--sims-dir` and `--report` without site packages.
- A real run without Playwright exits 2, names both installation commands, and
  emits no traceback.
- A fake installed Playwright contract completes the zero-simulation browser
  lifecycle and exits zero.

## Closure criteria

- Focused and repository tests pass.
- User-facing prerequisite documentation matches the CLI behavior.
- The fix is merged and independently read from the default branch.
- The optional-dependency command-boundary lesson is compounded and linked.

## Resolution evidence

- Fix PR: [#14](https://github.com/yaniv256/dmccreary-claude-skills/pull/14)
- Merge commit: `aad007744899bef2614f4c6e0e29123f8aa96814`
- Merged at: 2026-07-16T05:48:37Z
- Focused iframe-tester CLI regressions: 3/3 passed.
- Combined MicroSim utility tests: 8/8 passed.
- Repository Python tests: 31/31 passed.
- Durable learning:
  [Parse Help Before Loading Optional Dependencies](../solutions/logic-errors/parse-help-before-loading-optional-dependencies.md)

All closure criteria are satisfied. An independent read from `origin/main`
confirmed the lazy import, parser-owned dependency error, dependency-free help,
and all three subprocess regressions at the merge commit.
