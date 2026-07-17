# Supplementary Content Navigation Serialization Investigation

## Status

REMEDIATED LOCALLY - validation passed; merge and default-branch verification pending

## Incident

The `supplementary-content-generator` is a batch workflow, but its quiz step
instructs the operator to edit `mkdocs.yml` after every generated chapter quiz.
The repository's canonical navigation guide requires batch workflows to collect
all navigation changes and apply them in one serialized edit at the end. The
quiz example also uses the retired `Chapter N - Title` label instead of the
canonical `N. Title` form.

The same workflow already follows the canonical rule for generated references,
which makes two adjacent steps prescribe opposite mutation strategies for the
same file.

## Impact

- A multi-chapter run can repeatedly read and rewrite the same order-sensitive
  YAML list instead of performing one final mutation.
- A later step can write from stale navigation state and lose or misorder an
  earlier step's entry.
- Quiz labels can diverge from the narrow-sidebar convention used by the rest of
  the book.
- The workflow can claim Step 12 owns the final navigation update while earlier
  steps have already mutated the file.

## Phase 0: Tools and external contract

The investigation is reproducible from source commit `37c9db3a` using Git
history, text search, Python `unittest`, and the repository's strict MkDocs
build. No production state is involved.

MkDocs defines `nav` as the global navigation structure in `mkdocs.yml`. Its
official configuration guide describes the value as nested lists and notes that
navigation list items cannot be merged through configuration inheritance. This
supports treating the navigation as one ordered document that must be read and
written coherently rather than as independently appendable fragments:

- https://www.mkdocs.org/user-guide/configuration/#nav
- https://www.mkdocs.org/user-guide/writing-your-docs/#configure-pages-and-navigation

The stronger serialization and label rules are repository policy in
`skills/book-installer/references/mkdocs-nav-editing.md`.

## Phase 1: Timeline and preserved evidence

| Date | Evidence | Consequence |
| --- | --- | --- |
| 2026-06-03 | Commit `26d71c4b` introduces the supplementary workflow. Its quiz step edits navigation after each quiz and uses `Chapter N - Title`. Other artifact steps also mutate navigation inline. | Establishes the original incremental-edit contract. |
| 2026-07-10 | Commit `73fba782` introduces the canonical navigation guide. It requires batch quiz changes to be collected and applied in one final edit, and prohibits `Chapter` in chapter labels. | Supersedes the original mutation and label rules. |
| 2026-07-16 | Commit `5dac387f` migrates the adjacent reference step to defer navigation to Step 12, but does not update the quiz or other inline-navigation steps. | Leaves contradictory policies inside one active workflow. |

### Current contradiction

| Surface | Current instruction |
| --- | --- |
| Supplementary Step 5 | After each `quiz.md`, add a `Chapter N - Title` navigation entry. |
| Supplementary Step 6 | Collect reference entries and defer them to one serialized edit in Step 12. |
| Canonical guide | Batch workflows collect all quiz/navigation changes and apply one edit at the end; chapter labels use `N. Title`. |
| Supplementary Step 12 | Update navigation after all content is generated. |

## Phase 2: Initial hypotheses

| Hypothesis | Category | Initial probability | Assumptions |
| --- | --- | ---: | --- |
| H1: The July canonical-policy migration did not update the older direct integrator. | documentation migration | 82% | The canonical guide is authoritative and the integrator predates it. |
| H2: Step 5 intentionally owns incremental edits while Step 12 only verifies them. | workflow ownership | 7% | The canonical batch rule has an undocumented exception. |
| H3: "Add" means queue an entry rather than mutate `mkdocs.yml`. | wording ambiguity | 5% | Operators infer behavior opposite to the literal instruction. |
| H4: The reference step is the incorrect outlier. | source authority | 2% | The newer migration and canonical guide are both wrong. |
| H5: The true cause is not listed. | unlisted | 4% | Another execution surface controls the workflow. |

H1 is the maximum-pain hypothesis because it implicates migration and regression
coverage across the entire direct integrator. It is tested first.

## Phase 3: Evidence and revised hypotheses

### E1: Git ordering is unambiguous

Move-aware source history is not needed for the responsible lines: blame assigns
the quiz mutation and label directly to the original `26d71c4b` commit. The
canonical guide was added later in `73fba782` and explicitly names batch quizzes
as its motivating case.

### E2: The later reference fix demonstrates intended integration behavior

The Step 6 remediation in `5dac387f` tells the invoked skill to defer navigation,
collects its entries, and names Step 12 as the sole mutation point. This is an
implemented example of how a nested content skill participates in the batch
workflow without exercising its standalone navigation behavior.

### E3: Step 12 already exists as a final owner

The workflow's execution summary assigns `mkdocs.yml` navigation to Step 12.
Inline edits in Steps 2-5, 8, and 9 therefore duplicate ownership rather than
filling a missing phase.

### Revised probabilities

| Hypothesis | Revised probability | Evidence |
| --- | ---: | --- |
| H1: Incomplete policy migration | 99% | Complete timeline, direct blame, adjacent migrated example, and existing final owner. |
| H2: Intentional incremental exception | 0% | Canonical rule explicitly names batch quiz generation. |
| H3: "Add" means queue | 0% | The instruction names `mkdocs.yml` and contrasts with explicit "collect" language in Step 6. |
| H4: Reference step is wrong | 0% | It agrees with both the later canonical guide and Step 12 ownership. |
| H5: Unlisted cause | 1% | No executable implementation selects a different workflow. |

## Phase 4: Blame assignment

### Level 1: Responsible text

- `skills/book-installer/references/supplementary-content-generator.md`, Step 5:
  performs one navigation edit per quiz and publishes the retired label.
- The same file's Steps 2-4, 8, and 9: retain inline navigation mutations inside
  the batch workflow.
- The same file's Step 12: does not explicitly collect every prior step's entries
  or assert sole ownership, allowing earlier instructions to survive beside it.

### Level 2: Anti-pattern

A standalone content skill's normal side effect is invoked from a batch
orchestrator without an integration boundary that suppresses the side effect and
returns a change request to the orchestrator.

### Level 3: Development practice

The canonical-policy migration deduplicated guidance but had no semantic test for
direct integrators. A later fix aligned one adjacent step without a same-file
class search, so the old behavior remained active elsewhere.

## Phase 5: Remediation experiment

### X1: Make Step 12 the single navigation writer

- **Prediction before change:** a focused test requiring all pre-Step-12 artifact
  steps to queue navigation will fail against `37c9db3a`; it will also detect the
  retired quiz label.
- **Intervention:** tell nested generators to return navigation entries without
  editing `mkdocs.yml`; collect all generated entries; apply them once in Step 12
  after a fresh read; use the canonical `N. Title` label.
- **Expected success:** no generation step before Step 12 directs a navigation
  mutation, Step 12 names itself as the sole writer, and strict MkDocs validation
  remains green.

The initial four-test contract failed three assertions against source commit
`37c9db3a`: the direct mutation phrases remained, Step 5 did not defer, and Step
12 did not claim sole ownership. After remediation, the expanded five-test suite
passes and separately verifies every navigation-producing step.

## Phase 6: Final hypothesis

H1 is confirmed above 99%: the July navigation-policy migration introduced the
correct canonical contract but did not propagate it into the June batch
integrator. The reference-generator remediation later fixed one branch of the
workflow without closing the same-file class.

## Phase 7: Class search

The same-file search found direct navigation mutations in the About, Glossary,
FAQ, quiz, metrics, and optional diagram-report steps. These are in the same
orchestrator ownership boundary and will be remediated together. Step 6 already
uses the intended deferred pattern.

A repository-wide search finds standalone skills that edit navigation as part of
their own workflow. Those are not defects: the problem is the batch integrator
allowing nested skills to exercise that side effect before its own final Step 12.

## Phase 8-10: Comprehensive remediation plan

1. Preserve this investigation before changing operating guidance.
2. Add a focused semantic contract test and run it against the preserved source.
3. Make every pre-Step-12 artifact step collect navigation entries without
   mutating `mkdocs.yml`.
4. Rewrite Step 12 as the sole writer: fresh read, one serialized edit, owned
   entries only, canonical labels, and file-existence checks.
5. Add a path-filtered CI gate for the integrator and canonical guide.
6. Run focused, adjacent, and strict MkDocs validation.
7. Merge through a reviewed pull request and independently verify `main`.
8. Update the existing behavioral-contract solution and close the investigation.

## Closure criteria

- Step 5 queues quiz entries and never directs an immediate `mkdocs.yml` edit.
- Every generated chapter label uses the canonical `N. Title` form.
- All pre-Step-12 generated navigation entries are deferred.
- Step 12 explicitly performs one fresh, serialized navigation mutation.
- Focused tests fail on the preserved source and pass after remediation.
- Adjacent tests and strict MkDocs validation pass.
- The fix is merged and independently read back from `main`.
- CE Compound updates the reusable owner before the investigation enters Done.

## Validation evidence

- Focused supplementary-navigation contract: 5 passed.
- Adjacent quiz and reference contracts: 15 passed.
- Complete discovered Python test set: 98 passed.
- `git diff --check` and Python compilation: passed.
- Strict MkDocs build: passed with pre-existing informational diagnostics only.
