---
title: CLI Introspection Must Not Cross the Write Boundary
date: 2026-07-16
category: logic-errors
module: microsim-utils
problem_type: logic_error
component: tooling
symptoms:
  - "Running a script with --help rewrites tracked project files"
  - "An exploratory command mutates whichever repository is the current directory"
root_cause: missing_validation
resolution_type: code_fix
severity: high
tags: [cli, argparse, dry-run, side-effects, project-root, regression-testing]
---

# CLI Introspection Must Not Cross the Write Boundary

## Problem

A content generator performed filesystem work at module scope. The familiar
`--help` probe therefore ignored the flag and rewrote the current project's
catalog, TODO, and frontmatter before the operator had chosen to run anything.

## Symptoms

- `python3 generator.py --help` prints a completion summary instead of usage.
- Running the command from a different repository changes that repository.
- There is no safe way to inspect planned work before applying it.
- Importing the module for tests would execute the same mutations.

## What Didn't Work

Documenting that operators should run the command from a particular directory
does not make discovery safe. People and agents use `--help` precisely before
they understand a command's assumptions.

Adding only an `if __name__ == "__main__"` guard is also insufficient. It makes
imports safe, but a normal invocation still writes before the caller can review
the target or the planned changes.

## Solution

Give the command an explicit, layered boundary:

```python
def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-dir")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    root = resolve_project_root(args.project_dir)
    plan = discover_and_render(root)
    if not args.dry_run:
        apply(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

The MicroSim implementation parses arguments before resolving any project
path, validates both `mkdocs.yml` and `docs/sims`, and defers writes until after
discovery. See
`skills/microsim-utils/scripts/generate-microsim-index.py:21-208`.

Test the safety contract at the process boundary, including all files rather
than only the expected outputs:

```python
before = digest_tree(project)
result = subprocess.run([sys.executable, str(script), "--help"])
assert result.returncode == 0
assert digest_tree(project) == before
```

The corresponding regressions are in
`skills/microsim-utils/tests/test_generate_microsim_index.py`.

## Why This Works

`argparse` handles `--help` by exiting before project resolution. Discovery is
pure with respect to the project tree, so `--dry-run` can execute the same
selection and reporting path used by a real run without entering the write
phase. Explicit root validation prevents a relative path from silently binding
to an unrelated repository.

The subprocess tests verify the contract users actually experience. Hashing
the whole fixture catches unexpected side effects, including a new file that a
test author did not know to assert individually.

## Prevention

- Put executable behavior behind `main()`; never mutate at import time.
- Parse `--help` before environment or project validation.
- Give every generator a non-mutating preview path.
- Validate identity-bearing project files before reading or writing outputs.
- Make write intent visible in the command and documentation.
- Test `--help`, preview, invalid input, and apply modes as subprocesses.
- Compare whole-tree digests for commands whose contract is "writes nothing."

## Related Issues

- [Investigation record](../../investigations/2026-07-16-microsim-index-generator-help-mutation.md)
