---
title: Keep Behavioral Documentation Synchronized with Executable Contracts
date: 2026-07-16
category: logic-errors
module: quiz-generator
problem_type: logic_error
component: documentation
symptoms:
  - User-facing guidance and operating instructions prescribe opposite workflows
  - Adjacent documents publish different versions of the same skill
  - Required and optional artifacts change depending on which entry point is read
  - A direct integrator overrides the contract while appearing to invoke the canonical skill
root_cause: missing_validation
resolution_type: documentation_update
severity: medium
tags: [documentation-contract, skill, readme, behavioral-drift, regression-test]
---

# Keep Behavioral Documentation Synchronized with Executable Contracts

## Problem

A README and an operating skill can each be coherent while prescribing opposite
behavior. The quiz generator's README still promoted its v0.3 parallel workflow
after the operating skill moved to a v0.4 serial-only contract. Both files were
plausible in isolation, so prose review alone did not expose the migration gap.

## Symptoms

- The README made parallel execution the default for larger books while the
  operating skill prohibited parallel agents.
- The README called parallel execution token-neutral while the operating skill
  recorded about 13% additional token use.
- The README classified metadata as required and allowed embedded quizzes while
  the operating skill required only a separate `quiz.md` file.
- Residual phrases inside the operating skill still implied an explicit-request
  exception and parallel navigation workflow.

## What Didn't Work

- **Updating only the canonical instruction file.** Agents may execute the
  operating skill, but people often enter through the README. Leaving either
  surface stale keeps two effective contracts alive.
- **Checking for one preferred phrase.** A version match would not detect a
  stale workflow or output classification; a serial-mode heading would not
  detect parallel instructions elsewhere.
- **Treating historical notes as current guidance.** Version history may retain
  superseded behavior, but execution sections must not advertise it as active.

## Solution

First identify the authoritative behavioral dimensions rather than comparing
documents byte-for-byte. For this skill they are version, execution mode,
workflow shape, and output classification. The operating skill now declares
one serial agent and one serialized navigation edit
(`skills/quiz-generator/SKILL.md:36-62`,
`skills/quiz-generator/SKILL.md:691-705`). The README exposes the same policy
and Required/Recommended/Optional hierarchy
(`skills/quiz-generator/README.md:9-60`,
`skills/quiz-generator/README.md:94-168`).

Then encode those dimensions as a focused test. The quiz contract suite checks
the published version, rejects known stale parallel-default phrases, isolates
the three output sections, and verifies that required artifacts do not leak
into optional guidance
(`skills/quiz-generator/tests/test_documentation_contract.py:13-56`).

The test was also run against the pre-fix source through `QUIZ_SKILL_DIR`; all
five tests failed there and pass against the remediated tree. That negative
control proves the suite detects the original drift instead of merely blessing
the new wording.

The same rule applies to direct integrators, not only prose. The
reference-generator investigation found that the book installer invoked the
canonical skill while overriding its quantity, source positions, and navigation
behavior. Its contract suite therefore includes the direct integrator and the
upstream command and installer surfaces that define invocation ownership. The CI
workflow watches those authorities as well as the skill and public description;
otherwise a correct test can silently stop running when the integration changes.

## Why This Works

The test compares meaning-bearing invariants while still allowing each document
to serve its audience. The README can remain explanatory and the skill can
remain operational, but neither can silently change the version, default mode,
or artifact contract. Explicit stale-phrase assertions also make a migration's
retired policy visible to future maintainers.

This complements the narrower numeric-rubric pattern in
[Keep Documentation Rubrics as Executable Contracts](documentation-rubrics-need-executable-contracts.md).
That pattern parses arithmetic structure; this one protects behavioral agreement
between independently written entry points.

## Prevention

- List every checked-in surface that communicates a skill's behavior before a
  version or policy migration.
- Include direct callers and integrators in that inventory. An invocation can
  publish a competing contract through arguments and follow-up instructions even
  when it names the canonical skill correctly.
- Define the small set of behavioral dimensions that must agree: version,
  defaults, workflow, safety rules, and artifact ownership.
- Test semantic sections independently so headings cannot bleed into adjacent
  Required/Recommended/Optional regions.
- Preserve historical behavior only under clearly superseded version history,
  never in current execution instructions.
- Run the contract suite against the pre-migration source once; an expected
  failure is evidence that the test covers the defect.
- Search the repository for the retired policy and record separate defects
  rather than widening one module's remediation boundary silently.
- Make workflow path filters cover every authority the test reads. A semantic
  test is not a release gate when changes to an asserted input do not trigger it.

## Related Issues

- [Quiz generator serial execution investigation](../../investigations/2026-07-16-quiz-generator-serial-execution-contract.md)
- [Source remediation PR #16](https://github.com/yaniv256/dmccreary-claude-skills/pull/16)
- [Reference generator contract investigation](../../investigations/2026-07-16-reference-generator-contract-drift.md)
- [Reference generator remediation PR #18](https://github.com/yaniv256/dmccreary-claude-skills/pull/18)
