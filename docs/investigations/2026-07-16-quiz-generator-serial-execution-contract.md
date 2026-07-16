# Quiz Generator Serial Execution Contract Investigation

## Status

OPEN

## Incident

The operating `quiz-generator` skill declares serial execution to be a hard
requirement, but its adjacent README advertises parallel execution as the
default for four or more chapters. The README also claims parallel execution
uses the same number of tokens, while the operating skill records a measured
13% token penalty and additional consistency failures.

One navigation instruction and two explicit-request caveats inside the
operating skill retained parallel-generation assumptions even after the
serial-only policy was adopted.

## Impact

- An agent or user can select opposite execution strategies depending on which
  checked-in entry point they read.
- Following the README repeats system-prompt and project-context overhead for
  every spawned agent.
- Concurrent agents can produce inconsistent quiz strategies and conflicting
  `mkdocs.yml` edits.
- The README misclassifies quiz metadata as required and offers an embedded
  quiz layout that the operating skill no longer supports.

## Phase 0: Tools

The defect is reproducible from source commit `43507a05` with text search and
file comparison. Remediation uses Python `unittest`, repository validation,
Git, and GitHub CI. No production mutation is required.

## Phase 1: Preserved evidence

| Surface | Preserved claim | Consequence |
| --- | --- | --- |
| `skills/quiz-generator/SKILL.md` | "Serial Execution Only" and "Always use a single serial agent" | Canonical operating contract is serial. |
| Same file | Parallel four-agent run adds about 48,000 tokens | Directly contradicts README's same-token claim. |
| `skills/quiz-generator/README.md` | "Parallel Mode (Default for 4+ chapters)" | Public guidance selects the prohibited path. |
| Same file | "Same token usage" | Contradicts measured evidence in the operating skill. |
| Same file | Metadata JSON is required and quizzes may be embedded | Contradicts the operating output summary. |
| `SKILL.md`, warning and pitfalls | Permit parallel execution after an explicit request | Contradicts the hard serial-only requirement. |
| `SKILL.md`, navigation step | Mentions quizzes generated in parallel | Residual migration wording inside the canonical contract. |

## Phase 2: Hypotheses

| Hypothesis | Initial probability | Assumptions |
| --- | ---: | --- |
| H1: `SKILL.md` moved to v0.4 serial execution while the v0.3 README was not migrated. | 90% | Version labels and policy changes identify the same transition. |
| H2: README describes a still-supported alternate mode. | 4% | The hard prohibition in the skill is overstated. |
| H3: Parallel execution became token-neutral after the skill measurement. | 2% | Unrecorded runtime changes superseded the canonical evidence. |
| H4: The contradiction is intentional audience-specific guidance. | 1% | Users and executing agents are expected to follow opposite contracts. |
| H5: The true cause is not listed. | 3% | Another source controls execution mode. |

## Phase 3: Evidence and final hypothesis

The README identifies itself as version 0.3 and describes the parallel rollout.
The operating skill identifies itself as version 0.4 and explicitly records why
parallel execution was retired. No implementation or third source selects an
execution mode. H1 therefore explains the complete defect with greater than
99% confidence: the README and one cross-reference sentence were missed during
the v0.4 policy migration.

## Phase 4: Blame assignment

### Responsible text

- `skills/quiz-generator/README.md`: stale version, execution mode, workflow,
  performance, and output-contract sections.
- `skills/quiz-generator/SKILL.md`: a stale navigation sentence and two stale
  explicit-request caveats.

### Anti-pattern

The same behavioral contract is narrated independently in an executable skill
and a user-facing README without a synchronization test.

### Development practice

The v0.4 migration changed the canonical skill but had no checklist or
regression gate covering adjacent documentation.

## Phase 5: Remediation plan

1. Preserve the contradiction in this investigation artifact.
2. Migrate the README to the v0.4 serial execution contract.
3. Reconcile required, recommended, and optional outputs with `SKILL.md`.
4. Remove the stale parallel assumption from the navigation instruction.
5. Add focused tests that compare version, execution, and output contracts.
6. Search all skill documentation for the same parallel/serial contradiction
   class and record separate defects outside this skill's ownership boundary.
7. Run focused and repository validation.
8. Merge through a reviewed pull request and verify the default branch.
9. Run CE Compound and restore the blocked parent skill-evaluation task.

## Phase 6: Class search

A repository-wide search for serial/parallel execution claims found one separate
defect outside the quiz-generator ownership boundary. The
`chapter-content-generator` skill first permits parallel execution only after
an explicit user request and a token-cost warning, but later requires parallel
execution for four or more chapters, labels it the default, and instructs the
operator to spawn six agents. That defect is preserved for independent
remediation on Trello:

- [Investigation: chapter-content-generator execution policy contradicts itself](https://trello.com/c/Yt6HWSYp/208-investigation-chapter-content-generator-execution-policy-contradicts-itself)

The remaining matches are historical v0.3 notes or explicit warnings against
parallel execution. They do not advertise a conflicting current quiz-generator
workflow.

## Closure criteria

- README and `SKILL.md` both publish version 0.4 and serial execution as default.
- No current workflow text makes parallel execution the default or token-neutral.
- Required and optional outputs agree across both surfaces.
- Focused regression tests detect the original defect and pass after remediation.
- Repository validation and CI pass.
- The fix is merged and independently read back from the default branch.
- The reusable prevention lesson is compounded or a verified existing solution
  is recorded as the owner.
- The blocked parent Trello card returns to Next after this investigation enters Done.

## Closure evidence

Pending remediation.
