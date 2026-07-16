# Reference Generator Contract Drift Investigation

## Status

CURRENT - remediation in progress

## Incident

The executable `reference-generator` skill requires exactly 10 references for
every chapter, stored in a separate `references.md` file with a fixed source
mix. The public skill description still publishes the retired 10/20/30/40
learner-level contract, offers book-level or inline chapter output, requires
publication dates, and prescribes a different source mix.

The repository also publishes old reference-generation transcripts without
consistently identifying them as historical, and a live book-installer
integration retained part of the retired contract. A reader or invoking agent
can therefore follow opposite contracts depending on which checked-in entry
point it opens.

## Impact

- Agents can generate four different quantities for the same chapter.
- References can land in `docs/references.md`, inline in a chapter, or in the
  canonical per-chapter `references.md` file.
- Source positions, date requirements, chapter links, and navigation edits vary
  by entry point.
- A generated textbook can satisfy one published contract while failing the
  executable skill and the current book pipeline.

## Phase 0: Tools

The source worktree is pinned to commit `a97a886c` on branch
`fix/reference-generator-contract`. Git history, repository text search,
codebase-memory indexing, Python `unittest`, MkDocs validation, and GitHub are
available. No production state or ephemeral evidence is involved.

The official Anthropic skills repository describes each skill as a folder whose
`SKILL.md` contains the instructions and metadata the agent uses. That confirms
the local `SKILL.md` is the executable contract, while the website description
is an explanatory surface that must agree with it:

- https://github.com/anthropics/skills

## Phase 1: Timeline and preserved evidence

| Date | Evidence | Consequence |
| --- | --- | --- |
| 2025-11 | The original skill and prompt transcripts introduced learner-level quantities, book-level output, inline chapter output, dates, and user choice. | Establishes the retired contract. |
| 2026-01-31 | Commit `977bcd77` is titled "updated the reference generator skill to focus on 10 high-quality stable links" and rewrites `SKILL.md`. | Intentional migration to the current contract. |
| 2026-06-23 | Commit `d2763452` shortens skill frontmatter descriptions but does not update the public reference-generator description. | The stale explanatory surface survives a later documentation pass. |
| 2026-07-10 | Commit `73fba782` updates the current skill's navigation guidance without restoring the old quantity or output modes. | Current maintenance continues from the ten-per-chapter contract. |

### Contract comparison

| Dimension | Executable `SKILL.md` | Stale description, transcript, or integrator |
| --- | --- | --- |
| Quantity | Exactly 10 per chapter | 10, 20, 30, or 40 by learner level |
| Placement | `docs/chapters/<slug>/references.md` | `docs/references.md` or appended inline |
| User choice | None | Ask book-level or chapter-level |
| Positions 1-3 | Wikipedia | Resource mix varies by learner level |
| Positions 4-5 | Textbooks without URLs | Links and dates expected for every reference |
| Positions 6-10 | Verified online resources | Academic/resource mix varies by learner level |
| Dates | Not required | Publication date required |
| Chapter integration | Replace inline section with one annotated-references link | Append an inline `## References` section |
| Navigation | Add serialized `Annotated References` child entry | No navigation edit |

The active pipeline was only partially migrated:

- `commands/ibook.md` assigns `reference-generator` to
  `docs/chapters/*/references.md`.
- `skills/book-installer/SKILL.md` identifies per-chapter reference files as the
  generator's output.
- `skills/book-installer/references/supplementary-content-generator.md` invokes
  the skill once for each chapter that lacks `references.md`, but then overrides
  it with 8-15 sources grouped by type and a `References` navigation label. It
  also invoked a whole-book skill separately for every missing chapter.

The root README's mention of `docs/references.md` containing 30 sources describes
this repository's own current content tree; it is not generator guidance and is
outside this defect.

## Phase 2: Initial hypotheses

| Hypothesis | Category | Initial probability | Assumptions |
| --- | --- | ---: | --- |
| H1: The January skill migration did not enumerate and update every public guidance surface. | documentation migration | 84% | `SKILL.md` is authoritative and the old pages predate it. |
| H2: The old contract remains a supported alternate mode. | specification ambiguity | 5% | The exact-ten and separate-file language is overstated. |
| H3: The public description superseded the executable skill later. | source authority | 3% | A later intentional change selected the old behavior again. |
| H4: Audience-specific quantities and fixed source positions can both be satisfied. | interpretation | 1% | The conflicting quantities and placements are composable. |
| H5: The true cause is not listed. | unlisted | 7% | Another source controls execution. |

The maximum-pain hypothesis is H1 because it implicates the repository's own
migration discipline, not reader interpretation. It was tested first.

## Phase 3: Evidence and revised hypotheses

### E1: The migration diff is explicit

Commit `977bcd77` removes the learner-level table, book-level output, inline
chapter output, publication-date requirement, and user-choice prompt from
`SKILL.md`. It adds exact-ten quantities, fixed positions, per-chapter files,
chapter links, and navigation edits in one coherent change.

### E2: Git ordering eliminates later-supersession

The stale public description and prompt text originate before the January
migration. Later edits to the current skill retain the new contract. No later
commit restores the old behavior to `SKILL.md`.

### E3: The active pipeline was only partially migrated

The current `ibook` command and book-installer guidance both route reference
generation to per-chapter `references.md` files. However, the direct
supplementary-content integrator still imposed 8-15 sources grouped by type and
the noncanonical `References` navigation label. The migration therefore reached
the output location but not every quantity, source-position, and navigation
contract at the invocation boundary.

### E4: Historical examples are still presented as current

Three prompt transcripts remain in the live MkDocs navigation. Together they
show the old learner-level quantities, book-level choice, and inline chapter
writes without consistent historical or superseded labels.

| Hypothesis | Revised probability | Evidence |
| --- | ---: | --- |
| H1: Incomplete migration across guidance surfaces | **99%** | E1-E4 explain every contradiction and the timeline. |
| H2: Supported alternate mode | 0% | Current skill explicitly replaces inline sections and fixes quantity. |
| H3: Description superseded skill | 0% | Git ordering is the reverse. |
| H4: Contracts are composable | 0% | Quantity and placement instructions are mutually exclusive. |
| H5: Unlisted cause | 1% | No other executable selector was found. |

Passive evidence is conclusive. The regression suite is the controlled
remediation experiment; no production experiment is required.

## Phase 4: Blame assignment

### Level 1: Responsible text

| Location | Fault | Severity |
| --- | --- | --- |
| `docs/skill-descriptions/book/reference-generator.md` | Publishes the complete retired quantity, placement, format, and workflow contract. | High |
| `docs/skill-descriptions/book/index.md` | Summarizes the retired 10/20/30/40 quantity. | Medium |
| `docs/prompts/generate-references.md` and its MkDocs label | Publishes an old execution transcript without a superseded warning. | Medium |
| `docs/prompts/references-generator-skill.md` | Preserves the old creation transcript without a superseded warning. | Low |
| `docs/prompts/update-skill-descriptions.md` | Preserves and republishes the retired description contract without a superseded warning. | Low |
| `skills/book-installer/references/supplementary-content-generator.md` | Invokes a whole-book skill once per missing chapter while overriding it with 8-15 sources and a conflicting navigation workflow and label. | High |

### Level 2: Anti-pattern

One behavioral contract is narrated independently across an executable skill,
a public description, an index summary, and example transcripts. The migration
updated only the executable source and had no semantic synchronization test.

### Level 3: Development practice

Skill migrations do not begin with an inventory of every surface that teaches
the behavior. Historical transcripts are published beside current guidance
without explicit provenance labels, making preservation look like instruction.

## Phase 5: Remediation experiment

### X1: Align and lock the current contract

- **Prediction before change:** tests requiring exact-ten per-chapter output and
  explicit superseded labels fail against commit `a97a886c`.
- **Intervention:** align the public description, index, and direct integrator
  to `SKILL.md`; label all three prompt transcripts as historical in their pages
  and navigation; and add a semantic contract suite enforced in CI.
- **Expected success:** current guidance agrees on every contract dimension,
  historical evidence remains readable but cannot be mistaken for current
  instruction, and the suite fails against the preserved source but passes on
  the remediated tree.

## Phase 6: Final hypothesis

H1 is confirmed above 99%: the January 2026 contract migration updated the
executable skill but did not inventory or validate its public explanatory and
historical surfaces.

## Phase 7: Class search

A repository-wide search found four classes of match:

1. **Owned current guidance:** the public description and its book index entry;
   these must be aligned in this remediation.
2. **Direct integration:** the supplementary-content generator invokes the
   skill but overrides its quantity, source mix, and navigation label; this must
   be aligned and covered by the same regression suite.
3. **Owned historical evidence:** three prompt transcripts; preserve their text
   and label them explicitly as superseded.
4. **Compatible or unrelated uses:** the root README describes this
   repository's own 30-source file rather than generator behavior.

No separate defect outside the reference-generator and direct-integration
ownership boundary was identified by the final search.

## Phase 8-10: Comprehensive remediation plan

1. Preserve this investigation artifact before changing guidance.
2. Rewrite the public skill description around the exact-ten, fixed-position,
   per-chapter output contract.
3. Align the public skill index summary.
4. Align the supplementary-content direct integrator to one scoped invocation,
   the exact-ten source positions, and the serialized `Annotated References`
   navigation contract.
5. Mark all three historical prompt transcripts and their published navigation
   labels as superseded without rewriting their evidence.
6. Add focused tests for quantity, placement, source positions, date policy,
   chapter linking, serialized navigation, direct integrators, stale phrases,
   deferred-navigation composition, current integration authorities, and
   historical labeling, plus a GitHub Actions gate that runs both the contract
   suite and the strict documentation build.
7. Run the suite against the pre-fix source as a negative control.
8. Run focused, adjacent, and strict documentation validation.
9. Merge through a reviewed pull request and independently read back `main`.
10. Run CE Compound, close the investigation, and restore the blocked parent
   evaluation to `Next` only after every closure criterion is verified.

## Closure criteria

- Every current guidance surface says exactly 10 references per chapter.
- Current guidance agrees on positions 1-3, 4-5, and 6-10.
- Current guidance requires a separate chapter `references.md`, one chapter
  link, and one serialized navigation entry.
- The direct book-installer integration does not override the current skill's
  invocation scope, quantity, source positions, annotations, or serialized
  navigation contract.
- Current guidance does not require publication dates or offer book-level and
  inline output modes.
- Historical transcripts remain available but are unmistakably labeled as
  superseded and non-authoritative.
- Focused tests fail against the pre-fix source and pass after remediation.
- A focused GitHub Actions workflow runs the semantic contract suite on changes
  to the skill, its direct integrator, or its published guidance.
- Adjacent tests and strict documentation validation pass.
- The remediation is merged and independently verified from `main`.
- CE Compound records the reusable lesson or verifies an existing solution as
  the owner before the investigation enters Done.

## Closure evidence

Pending remediation.
