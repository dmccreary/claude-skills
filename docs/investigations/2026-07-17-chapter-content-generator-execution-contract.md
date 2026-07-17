# Chapter Content Generator Execution Contract Investigation

## Status

MITIGATED LOCALLY - PENDING PR AND DEFAULT-BRANCH VERIFICATION

## Symptom

The canonical `chapter-content-generator` skill publishes mutually exclusive
execution policies in the same file. Its overview and execution-mode sections
make sequential generation the default and permit parallel generation only
after an explicit user request and token-cost warning. Later sections require
parallel generation for four or more chapters, label parallel execution the
default, and prescribe a six-agent run for an ordinary all-chapters request.

## Impact

- An executing agent can choose opposite workflows depending on which section
  it follows.
- The stale parallel path can multiply repeated context and system-prompt work,
  increasing token usage and the chance of cross-chapter inconsistency.
- The user-request boundary is ineffective because later mandatory language
  overrides it.
- There is no executable contract test to stop either policy from drifting back
  into the skill after remediation.

Severity is **medium**: this is a deterministic operating-contract defect in an
active skill, but it does not corrupt an already-running production service.

## Phase 0: Tools

The investigation uses a clean isolated Git worktree, Git history and blame,
`rg`, Python `unittest`, the indexed code graph, official vendor documentation,
and repository validation. The source contradiction is directly reproducible
on `origin/main` at `2a66630c`. No production mutation is required.

## Established Timeline

| Time / marker | Event | Confidence | Source | Timezone |
| --- | --- | --- | --- | --- |
| 2026-02-03 15:14 CST, commit `ef578888` | Parallel generation became the default; the commit message says testing was limited. | High | Git history and blame | Commit offset `-06:00` |
| 2026-02-13 19:01 CST, commit `5617cfa2` | Sequential generation became the default and parallel generation became request-only, but the older parallel example and workflow remained. | High | Git blame and file comparison | Commit offset `-06:00` |
| 2026-03-29 09:45 CDT, commit `5b2e83c6` | The feature summary documented sequential generation and a 38% parallel token penalty. | High | Git blame | Commit offset `-05:00` |
| 2026-04-02 08:46 CDT, commit `2413b35f` | The scaffolding edit preserved and renumbered the already-stale rule to always use parallel mode for four or more chapters; it did not introduce that rule. | High | Commit patch; blame alone was misleading | Commit offset `-05:00` |
| 2026-07-16, source commit `43507a05` | The quiz-generator contract class search detected and recorded the independent chapter-content defect. | High | Prior investigation and Trello card | Date only; no time claim |
| 2026-07-17, `origin/main` `2a66630c` | The contradiction remains present on the current fork default branch. | High | Fresh fetch and source read | Date only; no time claim |

## Preserved Source Evidence

| Location | Current claim |
| --- | --- |
| `SKILL.md:21` | Sequential generation is the default; parallel generation requires an explicit request and costs 38% more tokens. |
| `SKILL.md:41-50` | Sequential mode is the default for all use cases; parallel mode is request-only. |
| `SKILL.md:732` | Four or more chapters must always use parallel mode. |
| `SKILL.md:800-817` | Parallel mode is labeled the default and the ordinary all-chapters example spawns six agents. |

## Hypotheses

### Generative-prior calibration

A repository search finds only fourteen explicit hypothesis outcome labels
(eight `CONFIRMED`, six `REFUTED`). That sample is sparse, inconsistently
recorded, and biased toward investigations that wrote an explicit outcome, so
its apparent 57% hit rate is not a reliable calibration set. This investigation
uses the methodology's conservative 20% first-pass hit-rate prior: most named
hypotheses will be wrong, and the cause may be absent from the initial list.
No explanation becomes root cause from source reading alone. The hypothesis
table will reserve real probability mass for an unlisted cause, and at least
one executable regression will test the original source rather than merely
restating the preferred policy.

### Assumptions

| # | Type | Assumption | Initial P | Inverse | Verification |
| --- | --- | --- | ---: | ---: | --- |
| A1 | source | `SKILL.md` is the active operating contract for this skill. | 95% | 5% | Inspect repository surfaces and package layout. |
| A2 | ordering | Parallel-by-default text predates sequential-by-default text. | 95% | 5% | Compare Git history and blame. |
| A3 | provenance | No generator overwrites `SKILL.md` from another canonical source. | 85% | 15% | Search build scripts and repository references. |
| A4 | intent | The March sequential feature note records an intentional policy decision. | 75% | 25% | Inspect the introducing commits and adjacent changes. |
| A5 | behavior | Current agent tooling can execute concurrent subagents when instructed. | 80% | 20% | Check official vendor documentation; runtime capability does not decide the preferred policy. |
| A6 | scope | There is no audience-specific dispatcher that selects different sections of the file. | 95% | 5% | Inspect the skill packaging and invocation model. |
| A7 | prevention | A source-level contract test can detect all current default-policy contradictions. | 90% | 10% | Write the test and prove it fails on the original source. |

### Initial hypothesis table

| # | Hypothesis | Category | Initial P | Assumptions | Ceiling |
| --- | --- | --- | ---: | --- | ---: |
| H1 | The sequential migration was incomplete: new default-policy text was added, but the older parallel workflow/example survived and a later edit copied its assumption. | migration | 28% | A1, A2, A4 | 68% |
| H2 | Parallel execution is actually the intended current default; the top sequential sections are the stale half. | product intent | 12% | A1, A5 | 76% |
| H3 | The contradiction is intentional: sequential text governs user communication while lower parallel text governs internal optimization. | architecture | 5% | A1, A6 false | 5% |
| H4 | Independent additive edits created two policy authorities because the skill has no canonical invariant or executable contract test. | development process | 15% | A1, A7 | 86% |
| H5 | `SKILL.md` is generated from another source, so editing it directly would be overwritten and the real defect is in the generator. | build/provenance | 5% | A3 false | 15% |
| H6 | The true cause is not yet listed. | unknown | 35% | none | 100% |

The probabilities sum to 100%. The maximum-pain hypothesis is H2 because it
would invalidate the investigation's assumed remediation direction despite the
clear sequential language near the top. It will be tested before treating H1
or H4 as established. H5 is the highest-value provenance check because a false
assumption there would make a direct patch non-durable.

## Evidence and Experiments

### Phase 3: Evidence collection

| ID | Evidence | Result | Effect |
| --- | --- | --- | --- |
| E1 | Commit `ef578888` introduced parallel-by-default execution on 2026-02-03 and explicitly described the change as only lightly tested. | Confirmed from the commit subject and patch. | Establishes the provenance of the lower parallel workflow and example. |
| E2 | Commit `5617cfa2` intentionally changed the execution contract to sequential-by-default and request-only parallel execution on 2026-02-13, but left the lower mandatory parallel principle and default-parallel example in place. | Confirmed from the patch, not inferred from current wording. | Strongly supports H1 and weakens H2. |
| E3 | Commit `5b2e83c6` later reinforced sequential-by-default execution and the 38% parallel token penalty in the feature summary. | Confirmed from the patch. | Shows that the sequential policy remained intentional after the incomplete migration. |
| E4 | Repository search found no generator or alternate canonical source that writes `skills/chapter-content-generator/SKILL.md`; packaging and invocation consume this file directly. | Confirmed with `rg`, package layout inspection, and code-graph search. | Confirms A1 and A3; refutes H5. |
| E5 | Official Anthropic tool-use documentation describes parallel tool use and the `disable_parallel_tool_use` control. It establishes capability only; it does not choose this skill's execution policy. | Confirmed from official vendor documentation. | Confirms A5 in its narrow capability sense without supporting H2. |
| E6 | Code-graph and text search found one `Parallel Mode (Default)` heading and one 38% token-penalty claim, both in the same active skill. There is no audience dispatcher or separate operating surface selecting between them. | Confirmed. | Confirms A6 and refutes H3. |
| E7 | `git blame` attributed the stale four-chapter rule to `2413b35f`, but that commit's patch only moved and renumbered text that already existed. | Surprise: blame attribution was insufficient. | Corrects the timeline and requires patch-level provenance for moved documentation. |

### Revised assumption table

| # | Assumption | Initial P | Revised P | Evidence |
| --- | --- | ---: | ---: | --- |
| A1 | `SKILL.md` is the active operating contract. | 95% | **99%** | Package layout and invocation surfaces consume it directly. |
| A2 | Parallel-by-default text predates sequential-by-default text. | 95% | **99%** | `ef578888` predates the policy change in `5617cfa2`. |
| A3 | No generator overwrites `SKILL.md` from another canonical source. | 85% | **98%** | Repository, build-path, and code-graph searches found no writer. |
| A4 | The sequential feature note records an intentional policy decision. | 75% | **98%** | Both `5617cfa2` and `5b2e83c6` intentionally state sequential-by-default policy. |
| A5 | Current agent tooling can execute concurrent tools when instructed. | 80% | **95%** | Official Anthropic documentation confirms the capability; repository policy remains separate. |
| A6 | No audience-specific dispatcher selects different policy sections. | 95% | **99%** | One undivided operating surface presents both claims to the same executor. |
| A7 | A source-level test can detect the current contradictions. | 90% | **90%** | Pending a red-first executable experiment. |

### Revised hypothesis table after source evidence

| # | Hypothesis | Initial P | Revised P | P ceiling | Key evidence |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | The sequential migration was incomplete. | 28% | **60%** | 96% | The `5617cfa2` patch changed the top policy but retained lower parallel mandates. |
| H2 | Parallel execution is the intended current default. | 12% | **3%** | 94% | Two later intentional edits state the opposite policy. |
| H3 | The contradiction is an intentional audience split. | 5% | **1%** | 1% | The skill has no dispatcher or separate operating surface. |
| H4 | Additive edits and no executable invariant allowed contradictory authorities to survive. | 15% | **30%** | 89% | Duplicated policy prose survived multiple edits and no test gates it. |
| H5 | Another source generates this file. | 5% | **1%** | 2% | No generator or alternate authority exists in the repository. |
| H6 | The true cause is not listed. | 35% | **5%** | 100% | Retained until the regression and adjacent-defect search complete. |

The probabilities still sum to 100%. H1 and H4 are compatible: the historical
cause can be an incomplete migration while the escape mechanism is duplicated
policy prose without an executable contract.

### Phase 5: Experiments

The three-strike count is zero for both the migration and documentation-contract
categories. No category pivot is required.

#### X1: Execute the sequential-default contract against current source

- **Tests:** H1, incomplete sequential migration.
- **Predicted outcome if H1 is true:** a contract that requires sequential
  execution for an ordinary multi-chapter request and request-gates every
  parallel workflow will fail on the current source, identifying surviving
  mandatory/default-parallel language.
- **Predicted outcome if H1 is false:** the current source will satisfy the
  sequential-default contract, or the only failures will be unrelated wording
  choices rather than executable-policy contradictions.
- **Procedure:** add a focused standard-library `unittest` contract for the
  active skill, run it unchanged against the unremediated `origin/main` source,
  and preserve the failing assertions before modifying `SKILL.md`.
- **Actual outcome:** All five contract tests failed on the untouched source.
  Failures independently identified the stale default-parallel heading, missing
  explicit gate on batch planning, automatic four-chapter threshold, ordinary
  all-chapters six-agent example, and stale active-version strings.
- **Conclusion:** Confirms H1 at 85%. The current file is a partially migrated
  operating contract, not merely ambiguous prose. It also demonstrates that a
  focused source contract can detect every observed contradiction, raising A7
  to 98% and establishing H4 as the contributing escape mechanism.

The post-experiment web checkpoint found the relevant behavior in the official
Git documentation: traditional `git blame` can attribute moved lines to the
moving commit, while `-M` adds movement detection. This matches E7 and further
supports using commit patches, rather than default blame output alone, for the
migration timeline.

### Phase 6: Final hypothesis revision

The experiment showed that H1 and H4 describe different parts of one causal
chain rather than competing root causes. H7 combines the initiating defect and
the escape mechanism into a falsifiable root-cause statement.

| # | Hypothesis | Initial P | Post-Evidence P | Post-Experiment P | Key experiment |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | The sequential migration was incomplete. | 28% | 60% | 2% | Subsumed by the more complete H7 after X1 confirmed both stale sections and the missing gate. |
| H2 | Parallel execution is the intended current default. | 12% | 3% | 1% | X1 treats the two later sequential decisions as the contract and exposes only older parallel residues. |
| H3 | The contradiction is an intentional audience split. | 5% | 1% | 0% | X1 operates on the single active surface; no dispatcher exists. |
| H4 | Additive edits and no executable invariant allowed contradictory authorities to survive. | 15% | 30% | 1% | Subsumed by H7 after the new contract caught every surviving contradiction. |
| H5 | Another source generates this file. | 5% | 1% | 0% | Repository provenance refutes it. |
| H6 | The true cause is not listed. | 35% | 5% | 0% | The experiment produced no unexplained behavior. |
| H7 | **Root cause: the intentional sequential migration edited only part of a duplicated operating contract, and the repository had no executable execution-policy invariant to reject the surviving parallel defaults.** | N/A | 0% | **96%** | X1 fails all five policy-contract tests on the unremediated source, matching the exact residues in the `5617cfa2` patch. |

H7 exceeds the 90% decision gate. Blame can now be assigned to the confirmed
system and process failure without attributing fault to an individual.

## Blame Assignment

### Level 1: Responsible source lines

Line numbers refer to the unremediated source at `2a66630c`.

| Location | Source contract | Why it is wrong | Severity |
| --- | --- | --- | --- |
| `skills/chapter-content-generator/SKILL.md:236-260` | Batch planning and parallel execution appear as an unconditional workflow. | The sections omit the explicit-request precondition declared at the top of the skill. | Medium |
| `skills/chapter-content-generator/SKILL.md:329` | Sequential processing applies to "fewer than 4 chapters." | This silently reinstates the superseded four-chapter automatic parallel threshold. | High |
| `skills/chapter-content-generator/SKILL.md:565-675` | Aggregation, report, log, and notification examples assume parallel agents and stale versions. | A normal sequential run is routed into parallel-only reporting semantics and misleading version output. | Medium |
| `skills/chapter-content-generator/SKILL.md:732` | "When processing 4+ chapters, always use parallel mode." | This directly reverses the canonical sequential default and user-consent boundary. | High |
| `skills/chapter-content-generator/SKILL.md:800-817` | "Parallel Mode (Default)" for an ordinary all-chapters request. | The example is executable guidance and contradicts both the overview and execution-mode contract. | High |

### Level 2: Anti-patterns

The primary anti-pattern is **multiple sources of truth inside one operating
document**. The execution policy is repeated in the overview, mode selector,
workflow headings, thresholds, aggregation templates, best practices, and
examples. A local edit can therefore be correct while the complete skill stays
wrong. The related migration anti-pattern is **partial replacement**: the
sequential policy was added without searching for and removing every behaviorally
equivalent parallel-default statement.

### Level 3: Development practice

The repository treated behavioral documentation as untested prose. Review and
blame inspection were insufficient because moved text could appear newer than
its real origin, and no executable invariant asked the only question that
matters to an agent: does every active section route an ordinary request to the
same execution mode? The durable practice change is a focused contract test
that encodes the canonical default, request gate, forbidden threshold language,
ordinary example, and current version markers.

The blame belongs to the operating interface and its missing validation, not to
an agent that happened to follow one of the contradictory instructions.

## Immediate Fix

The active skill now uses sequential generation as the sole default at every
decision surface. Batch planning and Task-agent instructions are guarded by an
explicit parallel request and token-cost warning. Aggregation and report
templates are mode-aware, the ordinary all-chapters example is sequential, and
active examples report version 0.09.

A new five-test documentation contract covers the failure path, including
forbidden automatic thresholds and stale default-parallel examples. It failed
5/5 before remediation and passes 5/5 afterward. All existing Python test
suites pass, `git diff --check` and Python compilation pass, the workflow YAML
parses, and a CI-equivalent `mkdocs build --strict` succeeds in a temporary
environment.

## Anti-Pattern Audit

The repository's indexed code graph was searched first for three structural
shapes: parallel-default operating policy, sequential/parallel policy gates,
and batch/Task-agent execution guidance. The graph reached the existing
`quiz-generator` documentation contract as the closest same-class finding and
the `reference-generator` contract as a second example of multiple published
surfaces requiring one executable invariant. Those findings are already
remediated and their tests pass. No additional active defect was found.

| Finding | Graph evidence | Severity | Disposition |
| --- | --- | --- | --- |
| `quiz-generator` previously published parallel and serial defaults on separate surfaces. | Graph search reached `test_readme_rejects_the_superseded_parallel_default`, `test_both_surfaces_define_serial_execution_as_the_default`, and `test_skill_does_not_describe_parallel_generation_as_current_workflow`. | Low, already fixed | Existing five-test contract passes. |
| `reference-generator` publishes a behavior across several integration authorities. | Graph search reached `test_current_surfaces_follow_canonical_serial_navigation` and related cross-surface contract methods. | Low, already guarded | Existing ten-test contract passes. |
| Other Markdown surfaces might retain default-parallel variants. | Text fallback searched default-parallel, automatic-parallel, Task-agent, and batch-planning variants after the graph pass. | None found | No follow-up defect. |

Subagent dispatch was intentionally omitted because this session did not have
authorization to create subagents. The anti-pattern categories were instead
queried independently through the code graph and merged here. Every repository
Python contract suite passes after the search.

## Remediation Plan

### Phase 1: Stop the bleeding (today, complete locally)

1. Make sequential generation the sole default across every active policy,
   workflow, reporting, best-practice, pitfall, and example section.
2. Retain parallel generation as an explicit-request option with a token-cost
   warning; do not add an automatic chapter-count threshold.
3. Update active examples to skill version 0.09.
4. Prove the original failure and the fix with the focused contract test.

### Phase 2: Structural hardening (this week, implementation complete)

1. Run the contract in GitHub Actions whenever the skill or workflow changes.
2. Keep the policy invariant behavioral: canonical default, request gate,
   forbidden threshold, ordinary all-chapters example, and active version.
3. Search the indexed repository for the same multiple-authority pattern and
   confirm existing quiz/reference contracts remain green.
4. Merge through a reviewed PR and independently rerun the focused contract on
   the updated default branch.

### Phase 3: Architectural prevention (next sprint, conditional)

If another execution-policy drift incident appears, inventory every skill that
publishes behavioral policy on more than one active surface and add focused
contracts to those skills. Do not build a generalized documentation parser or
central policy schema before recurrence demonstrates that the focused-test
pattern is insufficient.

### Accepted debt

- Parallel execution remains documented in several places because each place
  serves a distinct operational need: mode selection, batching, invocation,
  reporting, and an explicit-request example. The CI contract guards their
  shared precondition.
- Historical logs and prompts are evidence, not active operating authorities;
  they are not rewritten as part of this incident.

### What not to do

- Do not delete parallel mode; it remains a supported user-selected option.
- Do not infer consent from chapter count, latency goals, or an "all chapters"
  request.
- Do not rely on `git blame` alone for moved documentation; inspect the patch.
- Do not broaden this incident into unrelated prose cleanup or version-history
  rewriting.
- Do not mark the investigation closed before PR merge and default-branch proof.

## Closure Criteria

1. The source contains exactly one default execution policy: sequential for all
   ordinary requests.
2. Every parallel workflow is explicitly request-gated and includes the
   token-cost warning.
3. The five-test contract passes in CI and on the updated default branch.
4. All repository Python suites and strict documentation build pass.
5. The anti-pattern audit records no unguarded active sibling defect.
6. The source PR is merged and its merge commit is recorded here.
7. CE Compound records or reuses the durable learning before the Trello card is
   moved to Done.
