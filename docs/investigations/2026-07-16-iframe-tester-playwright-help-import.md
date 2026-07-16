---
title: Iframe Tester Requires Playwright to Display Help
date: 2026-07-16
status: active
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

Pending pull request and merge verification.
