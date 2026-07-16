---
title: Parse Help Before Loading Optional Dependencies
date: 2026-07-16
category: logic-errors
module: microsim-utils
problem_type: runtime_error
component: tooling
symptoms:
  - "A CLI --help request crashes because an optional package is not installed"
  - "Users cannot discover prerequisite instructions from the command itself"
root_cause: incomplete_setup
resolution_type: code_fix
severity: medium
tags: [cli, argparse, optional-dependencies, lazy-import, playwright, onboarding]
---

# Parse Help Before Loading Optional Dependencies

## Problem

An optional browser-testing dependency was imported before command-line
arguments were parsed. Users who most needed setup guidance could not display
the help that explained the command because they had not completed that setup.

## Symptoms

- `tool.py --help` exits non-zero with `ModuleNotFoundError`.
- The output is a traceback rather than usage and installation guidance.
- Every CLI operation appears to require an optional integration, including
  operations that should be dependency-free.

## What Didn't Work

Listing the prerequisite in a separate Markdown guide did not repair command
discovery. Operators and agents conventionally inspect `--help` before they
know which guide, package, or browser runtime is required.

Catching the import error at module scope would improve the wording but still
make help contingent on dependency handling. The parser must receive the help
flag before optional integration code runs.

## Solution

Keep parser construction dependency-free and load the integration only after
`parse_args` returns:

```python
def load_optional_browser():
    try:
        from browser_package import browser_factory
    except ModuleNotFoundError as error:
        if error.name == "browser_package":
            raise RuntimeError("Install with ...") from error
        raise
    return browser_factory


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        browser_factory = load_optional_browser()
    except RuntimeError as error:
        parser.error(str(error))
```

The name check matters: an import *inside* the optional package may fail for a
different missing dependency. Re-raising that error preserves the real defect
instead of falsely telling the user the top-level package is absent.

The defining implementation is in
`skills/microsim-utils/scripts/test-iframe-heights.py`; subprocess coverage is
in `skills/microsim-utils/tests/test_iframe_tester_cli.py`.

## Why This Works

Argparse implements help as an early successful exit, so no optional import is
attempted. Actual browser work still loads the same factory and follows the
same execution path. Missing setup becomes a concise usage error with direct
remediation rather than an implementation traceback.

Testing with `python -S` proves help does not accidentally succeed because a
developer already has the package installed. A tiny fake package proves the
normal import contract remains wired without requiring a browser download in
the unit suite.

## Prevention

- Treat `--help` and `--version` as standard-library-only command paths.
- Import optional integrations at the first operation that needs them.
- Distinguish a missing top-level package from a dependency failure inside it.
- Put installation commands in both the CLI error and the durable guide.
- Test help in an environment where site packages are unavailable.
- Test the installed integration boundary with a small contract fake.

## Related Issues

- [Investigation record](../../investigations/2026-07-16-iframe-tester-playwright-help-import.md)
