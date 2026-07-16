# Glossary Generator Scoring Contract Investigation

## Status

RESOLVED

## Incident

The `glossary-generator` skill describes its glossary-definition quality score
as a 1-100 measure, but the documented scoring instructions can produce 125
points. Step 3 begins with four criteria worth 25 points each. Step 7 adds a
fifth criterion, still at 25 points, while continuing to refer to definitions
that meet "all 4 criteria." The ISO reference repeats the five-criterion,
25-point shape without reconciling the denominator.

## Impact

- Two agents can follow the skill exactly and report incomparable scores.
- A definition can exceed the published 100-point maximum.
- The `85-100` success band has no stable meaning.
- Generated quality reports can claim ISO compliance using an unrepeatable
  local scoring convention.

## Phase 0: Tools

The investigation requires only the checked-in source, focused text searches,
Python `unittest`, Git, and the official ISO catalogue. Each was verified before
editing. No production state or ephemeral evidence is involved.

## Phase 1: Timeline and preserved evidence

The defect is present at source commit `0538f277`.

| Location | Preserved wording | Consequence |
| --- | --- | --- |
| `skills/glossary-generator/SKILL.md`, Step 3 | Four named criteria, each worth 25 points | Coherent 100-point subtotal, but omits the later business-rule criterion. |
| `skills/glossary-generator/SKILL.md`, Step 7 | Five criteria, each worth 25 points | Maximum becomes 125. |
| `skills/glossary-generator/SKILL.md`, Step 7 | "Definitions meeting all 4 criteria" | Criterion count contradicts the list immediately above it. |
| `skills/glossary-generator/references/iso-11179-standards.md` | Four core criteria plus an additional fifth principle | The conceptual structure is five-part, but the heading obscures that. |
| Same reference, scoring rubric | Each criterion worth 25 points | Five documented criteria again yield 125 points. |

The official ISO catalogue describes ISO/IEC 11179-4 as requirements and
recommendations for the semantic formulation of definitions. It does not make
this repository's 100-point weighting an ISO-prescribed score. The weights are
therefore a local evaluation contract and must be named and normalized as such.

## Phase 2: Initial hypotheses

| Hypothesis | Category | Initial probability | Assumptions |
| --- | --- | ---: | --- |
| H1: A fifth criterion was added after the original four-part rubric without renormalizing the score. | documentation drift | 72% | The five sections were intended to participate in one score. |
| H2: "Unencumbered by business rules" was intended as an unscored advisory principle. | specification ambiguity | 12% | Step 7's explicit five-criterion instruction is accidental. |
| H3: Scores were intended to be normalized from 125 to 100 downstream. | missing mechanism | 6% | A normalization rule exists elsewhere. |
| H4: The source is correct and only the wording is misleading. | interpretation | 2% | Independent readers converge on one computation despite the text. |
| H5: The true cause is not yet listed. | unlisted | 8% | Another generator or inherited template controls the denominator. |

The maximum-pain hypothesis is H1 because it implicates the skill's own quality
contract rather than an operator interpretation. It was tested first.

## Phase 3: Evidence

### E1: Arithmetic reproduction

Five criteria multiplied by 25 points produce 125. No normalization instruction
appears in the skill or its bundled reference.

### E2: Structural reproduction

Text search finds both "5 criteria (25 points each)" and "all 4 criteria" in the
same quality-report step. This is an internal contradiction independent of any
glossary input.

### E3: Reference reproduction

The bundled ISO guide documents precision, conciseness, distinctiveness,
non-circularity, and freedom from business rules, then assigns 25 points to each.
The reference therefore reproduces rather than resolves the denominator drift.

### E4: External standard boundary

The official ISO/IEC 11179-4 catalogue page says the standard addresses semantic
requirements and recommendations for definitions. The repository's numeric
weights are a local assessment device, so the remediation may normalize the
weights without claiming to change ISO.

## Phase 4: Revised hypotheses

| Hypothesis | Revised probability | Evidence |
| --- | ---: | --- |
| H1: Fifth criterion added without renormalization | **97%** | E1-E4 explain every contradiction directly. |
| H2: Fifth criterion advisory only | 1% | Step 7 explicitly says to score all five. |
| H3: Missing downstream normalization | 1% | No mechanism or instruction exists. |
| H4: Wording-only issue | 0% | Literal execution yields 125 points. |
| H5: Unlisted cause | 1% | No inherited scoring source was found. |

Passive evidence is conclusive, so no state-changing production experiment is
required. The focused regression test is the controlled remediation experiment.

## Phase 5: Remediation experiment

### X1: Normalize and lock the rubric

- **Prediction before change:** a test requiring five named weights totaling
  100 will fail against the preserved source because each criterion is 25.
- **Intervention:** define the local rubric as five criteria worth 20 points
  each, reconcile every criterion-count reference, and test both files.
- **Expected success:** the test reads five unique criteria, calculates exactly
  100 total points, and finds no stale four-criterion or 25-point scoring text.

## Phase 6: Final hypothesis

H1 is confirmed above 99%: an incremental fifth criterion was added without a
single-source score contract or a regression check.

## Phase 7: Blame assignment

### Level 1: Responsible text

| Location | Fault | Severity |
| --- | --- | --- |
| `skills/glossary-generator/SKILL.md` Step 7 | Five 25-point criteria exceed the stated scale. | High |
| `skills/glossary-generator/SKILL.md` quality metrics | "all 4 criteria" conflicts with the five-item list. | Medium |
| `skills/glossary-generator/references/iso-11179-standards.md` | Five criteria reuse the old 25-point bands. | High |

### Level 2: Anti-pattern

The score contract is duplicated prose. Criterion count, weights, and score
bands are repeated independently instead of being anchored by one explicit
table and checked as a unit.

### Level 3: Development practice

The skill had no documentation contract test. Prose review could detect a typo,
but it could not prove the weights sum to the promised denominator or that the
skill and reference agree.

## Phase 8: Immediate remediation

1. Define one explicit five-by-20 local rubric in `SKILL.md`.
2. Use the same five criteria and scoring bands in the ISO reference.
3. State that the weighting is the skill's evaluation rubric, informed by ISO
   formulation principles rather than assigned by ISO.
4. Add a focused regression test for criterion identity, total weight, and stale
   contradictory phrases.

## Phase 9: Class search

Search the repository for glossary scoring references and the stale phrases
`25 points each`, `all 4 criteria`, and `Four Core Criteria`. Only the two owned
glossary-generator files are in this remediation boundary. Other skill rubrics
are separate contracts and are not mechanically rewritten.

## Phase 10: Remediation and closure plan

1. Preserve this investigation artifact before source edits.
2. Normalize the five glossary criteria to 20 points each.
3. Reconcile per-band scoring and every criterion-count statement.
4. Add and run focused regression tests.
5. Run adjacent repository validation and syntax checks.
6. Record the reusable single-source rubric lesson with CE Compound.
7. Merge the source PR and verify the merge commit.
8. Restore the blocked glossary learning task only after every closure criterion
   has direct evidence.

## Closure evidence

- Source remediation merged through
  [PR #5](https://github.com/yaniv256/dmccreary-claude-skills/pull/5)
  at merge commit `25c21067b5acd271fc567ff4c18378c1d3563c54`.
- The focused scoring-contract suite passed 4 of 4 tests. The adjacent
  `book-installer` and `book-publisher` suites passed 4 of 4 and 5 of 5 tests,
  respectively.
- The complete documentation site passed a strict MkDocs build with the
  repository's imaging and glightbox dependencies enabled.
- CE Compound captured the reusable prevention pattern in
  `docs/solutions/logic-errors/documentation-rubrics-need-executable-contracts.md`.
- The blocked `Learn glossary-generator from dmccreary-claude-skills` card was
  independently verified back in the Trello `Next` list while this
  investigation remained the sole `In Progress` card.

## Closure criteria

- Exactly five named criteria participate in the score.
- Their weights total exactly 100.
- No stale 25-point/four-criterion scoring statement remains in the owned files.
- Focused tests fail against the original contract and pass against the fix.
- Adjacent validation passes.
- CE Compound is recorded and the PR is merged.
- The blocked parent card is independently verified back in `Next`.
