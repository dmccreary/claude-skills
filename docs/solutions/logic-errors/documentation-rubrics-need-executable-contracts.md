---
title: Keep Documentation Rubrics as Executable Contracts
date: 2026-07-15
category: logic-errors
module: glossary-generator
problem_type: logic_error
component: documentation
symptoms:
  - A documented score can exceed its published maximum
  - Different sections disagree about criterion count or weights
  - A local scoring convention is presented as if the external standard assigned it
root_cause: missing_validation
resolution_type: documentation_update
severity: medium
tags: [rubric, documentation-contract, denominator, regression-test, iso-11179]
---

# Keep Documentation Rubrics as Executable Contracts

## Problem

A numeric rubric can look internally plausible while becoming arithmetically
impossible after incremental edits. In the glossary generator, four criteria at
25 points grew into five criteria at 25 points, allowing a score of 125 on a
published 100-point scale.

## Symptoms

- The instructions named five scored criteria but retained the old
  four-criterion denominator.
- One section still referred to definitions meeting "all 4 criteria."
- The bundled reference reproduced the conflicting weights instead of resolving
  them.
- The report language risked presenting a repository-local weighting as an ISO
  score.

## What Didn't Work

- **Relying on prose review.** Every individual sentence was readable, but no
  mechanism checked the arithmetic across sections.
- **Repeating the rubric in several forms.** Headings, numbered lists, score
  bands, and a reference file drifted independently.
- **Treating standards language as the score contract.** ISO/IEC 11179 informs
  the definition qualities, but it does not assign this repository's numeric
  weights. Calling local score bands "ISO criteria" obscured ownership of the
  denominator.

## Solution

Define one explicit, delimited table for the local score contract and make every
consumer agree with it. The glossary skill now declares five named criteria at
20 points each and states that the weighting is local
(`skills/glossary-generator/SKILL.md:149-163`). The bundled reference carries the
same contract and attribution boundary
(`skills/glossary-generator/references/iso-11179-standards.md:5-21`).

```markdown
<!-- glossary-quality-rubric:start -->
| Criterion | Weight |
| --- | ---: |
| Precision | 20 |
| Conciseness | 20 |
| Distinctiveness | 20 |
| Non-circularity | 20 |
| Unencumbered by business rules | 20 |
<!-- glossary-quality-rubric:end -->
```

Add a focused contract test that parses both copies, compares exact criterion
identity, and calculates the total rather than checking only for preferred
phrasing (`skills/glossary-generator/tests/test_scoring_contract.py:13-44`). The
same test also rejects stale four-criterion wording and accidental attribution
of the local score to ISO (`skills/glossary-generator/tests/test_scoring_contract.py:46-63`).

## Why This Works

The table makes the denominator visible to people and parseable by a test. Exact
dictionary equality catches renamed, missing, duplicated, or reweighted
criteria, while summing the values proves the advertised maximum. Testing both
the operating skill and its reference turns synchronization from a review habit
into an executable invariant.

Separating the external standard's conceptual guidance from the local numeric
rubric also establishes the correct authority boundary. The project owns and
may change its weights; it must not imply that ISO prescribed them.

## Prevention

- Put every numeric rubric behind one explicit marker-delimited table.
- Test criterion names, individual weights, and the total denominator.
- Test every checked-in consumer or reference that repeats the contract.
- Reject known stale phrases when a migration changes criterion count or score
  ownership.
- Label repository-defined scoring as local, even when its qualitative criteria
  are informed by an external standard.
- Run the contract test against the pre-fix source once; an expected failure
  proves the test detects the original defect rather than only blessing the new
  wording.

## Related Issues

- [Glossary generator scoring contract investigation](../../investigations/2026-07-15-glossary-generator-scoring-contract.md)
