# README Route License Authority Investigation

## Status

CURRENT

## Symptom

The active `book-publisher` README guide instructs an agent to publish a
Creative Commons BY-NC-SA 4.0 badge when it cannot find repository license
evidence:

> Default to Creative Commons BY-NC-SA 4.0 if not specified.

That instruction converts missing evidence into an affirmative legal grant.
The same route later requires a License section, so a generated README can
state licensing terms that the repository owner never selected.

## Impact

An agent following the active guide can misrepresent an unlicensed repository
as licensed, obscure conflicting or split code/content licenses, and produce a
README whose badge and prose disagree with the repository's actual legal
files. The defect affects every user of the active README route and can grant
apparent permissions that do not exist.

Severity is **high** because the generated publication artifact makes a legal
claim. GitHub's licensing guidance states that default copyright applies when
a repository has no license and no permission to reproduce, distribute, or
create derivative works is granted.

## Phase 0: Tools

The investigation uses a clean worktree based on `origin/main`, Git history,
the full codebase-memory index for the worktree, repository tests and release
validators, primary GitHub licensing documentation, and installed-skill parity
checks. The index includes active and archived scripts, the target source is
readable, the worktree is clean, and the existing focused test module loads.

## Established Timeline

| Time / marker | Event | Confidence | Source | Timezone |
| --- | --- | --- | --- | --- |
| 2025-11-11 13:11:06 CST, commit `6403c8e6` | The standalone README skill introduced the no-evidence CC BY-NC-SA 4.0 default. | High | `git blame` and `git log --follow` | Commit offset `-06:00` |
| 2026-07-10 05:52:45 CDT, commit `ac26066d` | The standalone README route was promoted into active `book-publisher` guidance without changing the license default. | High | `git log --follow` and current path history | Commit offset `-05:00` |
| 2026-07-17, source commit `e2dd7a0f` | The invented-license default remains in current `origin/main`. | High | Fresh worktree source read | Date only; no time claim |

## Preserved Source Evidence

| Location | Observed behavior |
| --- | --- |
| `skills/book-publisher/references/readme-guide.md:77-88` | The active route checks three weakly defined sources and defaults to a specific Creative Commons license when none is found. |
| `skills/book-publisher/references/readme-guide.md` | The guide later requires a License section but defines no fail-closed behavior for absent, conflicting, split, or nonstandard evidence. |
| `skills/book-publisher/scripts/validate-readme.py` | Required-section validation accepts the word `license` anywhere in the README and does not compare claims with repository evidence. |
| `skills/book-publisher/tests/test_validate_readme.py` | Existing tests cover Markdown fence parsing only; no licensing contract is executable. |

## Primary External Evidence

- [GitHub's repository licensing guide](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
  says that without a license default copyright applies and the repository
  grants no general permission to reproduce, distribute, or create derivative
  works.
- The same guide says license detection can fail when a repository has
  multiple licenses or other complexity and recommends documenting that
  complexity rather than simplifying it into a false single-license claim.
- [GitHub's licenses API documentation](https://docs.github.com/en/rest/licenses/licenses)
  states that GitHub's detector compares the repository license file with
  known licenses and does not infer licensing from arbitrary documentation.

## Hypotheses

### Generative-prior calibration

Repository investigations contain only two `CONFIRMED` and two `REFUTED`
labels. That 50% apparent ratio is four sparse mentions rather than a
measured one-row-per-hypothesis track record, so it is not a defensible
first-pass hit rate. This investigation uses the methodology's conservative
20% prior: most hypotheses listed next will be wrong, and the true cause is
probably absent from the initial list.

No source-reading narrative becomes root cause without an executable
experiment. The Phase 2 table will reserve plurality probability for "the
true cause is not yet listed," and the experiment matrix will exercise real
repository states so it can reveal a mechanism that the initial list failed
to name.

### Assumptions

| # | Type | Assumption | Initial P | Inverse | Verification |
| --- | --- | --- | ---: | ---: | --- |
| A1 | route | The active guide is an operative agent contract. | 95% | 5% | Trace routing from `book-publisher/SKILL.md`. |
| A2 | architecture | No wrapper supplies a verified license decision before the guide runs. | 75% | 25% | Trace active callers and commands. |
| A3 | authority | Repository-wide policy does not authorize this route to license arbitrary target repositories. | 85% | 15% | Inspect repository license and route scope. |
| A4 | validation | README validation does not compare license claims with target-repository evidence. | 85% | 15% | Trace validator data flow and run fixtures. |
| A5 | semantics | `docs/license.md` can describe content scope rather than the whole repository. | 70% | 30% | Check documented conventions and repository examples. |
| A6 | complexity | A target repository can contain multiple applicable license files. | 95% | 5% | Check GitHub/SPDX documentation and fixtures. |
| A7 | behavior | An agent following the guide will publish its fallback badge and section. | 85% | 15% | Run the route instructions in a fixture repository. |
| A8 | prevention | No executable test currently covers license authority for the active route. | 80% | 20% | Search test graph and release commands. |

All assumptions are primitive binary claims and each inversion sums to 100%.
A2 and A4 are the initial bottlenecks because they determine whether another
boundary already prevents the guide's unsafe instruction from reaching a
publication artifact.

### Initial hypothesis table

| # | Hypothesis | Category | Initial P | Assumptions | Ceiling |
| --- | --- | --- | ---: | --- | ---: |
| H1 | A textbook-specific Creative Commons convention was promoted into a generic active README route without preserving the distinction between a project convention and target-repository authority. | migration | 18% | A1, A3, A7 | 69% |
| H2 | The validator certifies a README from prose mentions alone, so it creates false confidence without checking the repository evidence that authorizes the legal claim. | quality system | 10% | A4, A8 | 68% |
| H3 | The guide treats copyright metadata as license evidence and therefore collapses identity/attribution into permission. | data semantics | 7% | A5, A7 | 60% |
| H4 | Active and archived templates perpetuate the same default, so later promotion and packaging preserve it mechanically. | duplication | 8% | A1, A8 | 76% |
| H5 | The route has no typed license state such as absent, single, ambiguous, split, or explicitly authorized; prose generation therefore cannot fail closed. | architecture | 10% | A2, A4, A6 | 61% |
| H6 | The route silently selects or invents one license when source files conflict because its discovery order is treated as precedence. | evidence handling | 7% | A5, A6, A7 | 57% |
| H7 | The true cause is not yet listed. | unknown | 40% | none | 100% |

The probabilities sum to 100%. The maximum-pain candidates are H1 and H2:
they implicate the recent promotion decision and the repository's own
validation surface rather than a user's repository layout. H1 will be tested
first, while the fixture matrix will deliberately attempt to convert H7 into
a named mechanism.

## Evidence and Experiments

### Phase 3: Non-destructive evidence collection

#### Revised assumptions

| # | Assumption | Initial P | Revised P | Evidence |
| --- | --- | ---: | ---: | --- |
| A1 | The active guide is an operative agent contract. | 95% | **99%** | `book-publisher/SKILL.md` routes every README request directly to `references/readme-guide.md`. |
| A2 | No wrapper supplies a verified license decision first. | 75% | **99%** | The code graph and route text expose no caller, command, or typed discovery step before the guide writes README content. |
| A3 | Repository policy does not authorize arbitrary targets. | 85% | **99%** | The guide explicitly targets any repository; this repository's own content terms cannot license a caller's separate repository. |
| A4 | Validation ignores target-repository license evidence. | 85% | **99%** | `validate_readme()` receives only one README path; required-section logic searches lowercase prose for the substring `license`. |
| A5 | `docs/license.md` can have narrower scope than the repository. | 70% | **99%** | The current repository has `docs/license.md` describing “content” but no root `LICENSE*`; MkDocs defines `copyright` as theme display information, not a license grant. |
| A6 | A target can contain multiple applicable licenses. | 95% | **99%** | GitHub documents multiple-license complexity; SPDX defines `AND`, `OR`, `WITH`, and `LicenseRef` rather than collapsing it. |
| A7 | An agent following the guide publishes the fallback claim. | 85% | **85%** | Source makes the instruction explicit, but executable fixture proof remains Phase 5 work. |
| A8 | No test covers license authority. | 80% | **99%** | The only active validator tests cover Markdown fence parsing; no fixture passes repository evidence. |

#### E1: Active guidance is a near-verbatim archived promotion

- `git log --follow` identifies the standalone README route before the
  `book-publisher` promotion.
- A direct diff shows that the active guide differs mainly in frontmatter,
  title, wording from “skill” to “guide,” and an updated script path. The
  license fallback and full CC BY-NC-SA example survived unchanged.
- Confidence: high. Supports H1 and H4; confirms A1.

#### E2: No authority boundary precedes README generation

- `book-publisher/SKILL.md` routes the user request straight to the guide.
- The guide discovers strings from `LICENSE`, `docs/license.md`, and the
  MkDocs `copyright` field, but defines no typed result, scope, conflict state,
  or authorized human selection.
- No wrapper, CLI, or function accepts a verified license decision.
- Confidence: high. Supports H1 and H5; confirms A2-A3.

#### E3: Two independent instructions invent the same legal claim

- Step 3 publishes a CC BY-NC-SA 4.0 badge when no evidence is found.
- Step 10 unconditionally emits a full CC BY-NC-SA 4.0 License section and
  links `docs/license.md`, even when that file is absent or says something
  else.
- Step 15 requires License as a fixed section rather than deriving its
  presence from an evidence state.
- Confidence: high. Supports H1, H3, and H5.

#### E4: Validation certifies prose, not authority

- `validate_readme()` reads only the README file. It has no repository-root,
  license-file, metadata, or authorized-selection input.
- `check_required_sections()` marks License present when `license` appears
  anywhere in lowercase content, including prose, badges, acknowledgements,
  or unrelated dependency text.
- The code graph shows no licensing checker in the validator call tree.
- Confidence: high. Supports H2 and confirms A4 and A8.

#### E5: The repository itself demonstrates scope ambiguity

- This repository contains `docs/license.md`, whose prose governs “content,”
  but does not contain a root `LICENSE`, `LICENSE.md`, `COPYING`, or `NOTICE`.
- The active skill frontmatter identifies CC BY-NC 4.0 while the docs page
  identifies CC BY-NC-SA 4.0. Those are different terms and scopes.
- The guide's ordered list provides no rule for reconciling this conflict and
  would select a claim without establishing what files it covers.
- Confidence: high. Supports H3, H5, and H6; confirms A5-A6.

#### E6: The unsafe contract remains duplicated

- `skills/archived/readme-generator/SKILL.md` preserves the same default and
  unconditional License section.
- `docs/prompts/readme-generator-skill.md` also says the default is always CC
  BY-NC-SA 4.0.
- A fix limited to the active sentence would leave sources that can reintroduce
  the defect during a later promotion or regeneration.
- Confidence: high. Supports H4.

#### E7: Primary documentation requires fail-closed evidence handling

- GitHub states that default copyright applies when no license exists and
  documents detection failures for multiple-license complexity.
- GitHub's API documentation says Licensee identifies known repository license
  files and does not infer a project license from arbitrary documentation.
- MkDocs defines `copyright` as display information included by the theme.
- SPDX provides explicit compound expressions and custom `LicenseRef` values
  for states that cannot be represented by one common badge.
- Confidence: high. Confirms A3, A5, and A6.

### Phase 4: Revised hypotheses after evidence

| # | Hypothesis | Initial P | Revised P | Ceiling | Key evidence |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | Textbook convention was promoted into a generic route without an authority boundary. | 18% | **5%** | 83% | Subsumed by H8 after E1-E4 connected promotion and prevention failure. |
| H2 | Prose-only validation creates false confidence. | 10% | **5%** | 98% | E4 confirms the mechanism, but it is one part of the full chain. |
| H3 | Copyright metadata is collapsed into permission. | 7% | **2%** | 84% | E5 and E7 confirm the semantic error, subsumed by H8. |
| H4 | Duplicated sources perpetuate the default. | 8% | **4%** | 98% | E1 and E6 confirm duplication, subsumed by H8. |
| H5 | The route has no typed license state and cannot fail closed. | 10% | **6%** | 96% | E2-E5 confirm the missing model, subsumed by H8. |
| H6 | Discovery order is mistaken for legal precedence. | 7% | **3%** | 83% | E3 and E5 show silent selection without scope/conflict rules. |
| H7 | The true cause is not yet listed. | 40% | **5%** | 100% | Retained until the fixture matrix directly executes the contract. |
| H8 | **The active incident is a promoted prose-only generator contract that has no license-authority state model, while a presentation-only validator and duplicated historical sources allow invented or ambiguous legal claims to be published as valid README content.** | N/A | **70%** | 78% | E1-E7 connect entry, mechanism, escape, and recurrence paths. |

The probabilities sum to 100%. H8 is between 50% and 80%, so Phase 5 must
exercise the current route and validator against real repository-state
fixtures before blame assignment. Primary GitHub, SPDX, REUSE, MkDocs, and
Creative Commons documentation all support the required distinction between
copyright display text, license evidence, authority to grant permissions, and
compound or file-scoped licensing.

### Phase 5: Experiments

No earlier experiment targets this architecture/quality-system category, so
the three-strike pivot is not active.

#### X1: No-license repository with invented CC README

- **Tests:** H8, including the entry and validator escape paths.
- **Predicted if H8 is true:** Following the guide in a repository with no
  license evidence yields the CC BY-NC-SA badge and section, and the validator
  reports no license-authority error.
- **Predicted if H8 is false:** The route declines to make a claim, asks for an
  authorized selection, or validation rejects the unsupported claim.
- **Procedure:** Create an isolated temporary repository containing no license
  file, write the guide's exact CC badge and section into its README, and run
  the unmodified active validator.
- **Actual outcome:** The unmodified validator reported all four required
  sections present, returned 80/100 with status `GOOD`, and emitted no
  license-authority error. The fixture contained no license file.
- **Conclusion:** Supports H8. The active quality gate treats an unsupported
  affirmative license grant as valid presentation content.

#### X2: Conflicting-license repository with one invented claim

- **Tests:** H5, H6, and the ambiguity branch of H8.
- **Predicted if H8 is true:** Adding distinct MIT and Apache license files does
  not change validator behavior; a README that claims only CC BY-NC-SA still
  passes the license section check.
- **Predicted if H8 is false:** Discovery reports ambiguity or validation
  rejects a single unsupported badge/section.
- **Procedure:** Create a separate fixture with `LICENSE-MIT` and
  `LICENSE-APACHE`, then validate the same README.
- **Actual outcome:** The unmodified validator produced the same 80/100
  `GOOD` result as X1. The presence of both `LICENSE-MIT` and
  `LICENSE-APACHE` caused no ambiguity signal and did not affect validation.
- **Conclusion:** Supports H5, H6, and H8. Repository evidence is outside the
  validator's data model, so contradictory source evidence cannot fail the
  generated single-license claim.

#### X3: Nonstandard license text

- **Tests:** H5 and the unknown-cause slot H7.
- **Predicted if H8 is true:** The route has no honest representation such as
  `LicenseRef`; validation ignores the nonstandard source and accepts the
  unrelated common-license claim.
- **Predicted if H8 is false:** The route preserves the source text or reports
  it as nonstandard without substituting a common badge.
- **Procedure:** Create a fixture with a custom root `LICENSE` and validate a
  README carrying the guide's CC claim.
- **Actual outcome:** The unmodified validator again returned 80/100 and
  `GOOD`. It ignored the root `LICENSE`, whose custom terms prohibit general
  redistribution, and accepted the unrelated CC BY-NC-SA claim.
- **Conclusion:** Supports H5 and H8 and reduces H7. The defect is not limited
  to GitHub-detectable common licenses; arbitrary source terms are invisible
  to the current route contract and quality gate.

#### X4: Prose mention masquerading as a License section

- **Tests:** H2 and the unknown-cause slot H7.
- **Predicted if H8 is true:** A README with no License heading can satisfy the
  required section merely by mentioning “license” in unrelated prose.
- **Predicted if H8 is false:** The validator requires a structural License
  heading and reports the section missing.
- **Procedure:** Validate a README whose acknowledgements say only that a
  dependency has a license, with no repository license badge or heading.
- **Actual outcome:** The validator credited all four required sections and
  returned 70/100 with status `ADEQUATE`, even though the README had no
  License heading or repository-license statement. The only occurrence was
  “A dependency's license is documented upstream.”
- **Conclusion:** Strongly supports H2 and H8. This was the most diagnostic
  surprise: the required-section check is not structural and can certify an
  unrelated prose mention as a repository License section.

#### Phase 5 result

The experiment matrix reproduced the unsafe entry, missing evidence model,
and validation escape independently. X1-X3 were presentation-identical to the
validator despite materially different legal states, while X4 proved the
validator does not even establish that the claimed required section exists.
H8 therefore explains the observed behavior without relying on an untested
agent interpretation or a repository-specific convention.

The post-experiment web checkpoint found matching primary-source semantics,
not an exceptional platform quirk: GitHub documents default copyright when
license evidence is absent and warns that multiple licenses create detection
complexity; SPDX explicitly models compound expressions, custom
`LicenseRef` values, `NoneLicense`, and `NoAssertionLicense`. The experiment's
four repository states are therefore states the route must preserve rather
than normalize into one Creative Commons claim.

### Phase 6: Final hypothesis revision

| # | Hypothesis | Initial P | Post-evidence P | Post-experiment P | Key experiment |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | Textbook convention was promoted into a generic route without an authority boundary. | 18% | 5% | **0%** | X1 confirms the entry but H8 explains the complete chain. |
| H2 | Prose-only validation creates false confidence. | 10% | 5% | **1%** | X4 confirms it as one escape mechanism within H8. |
| H3 | Copyright metadata is collapsed into permission. | 7% | 2% | **0%** | No additional explanatory power beyond H8. |
| H4 | Duplicated sources perpetuate the default. | 8% | 4% | **1%** | Source search confirms recurrence risk, not the complete incident. |
| H5 | The route has no typed license state and cannot fail closed. | 10% | 6% | **1%** | X1-X3 confirm state blindness as one mechanism within H8. |
| H6 | Discovery order is mistaken for legal precedence. | 7% | 3% | **0%** | X2 confirms ambiguity is ignored, subsumed by H8. |
| H7 | The true cause is not yet listed. | 40% | 5% | **1%** | All four outcomes match H8 without an unexplained residual mechanism. |
| H8 | **A promoted prose-only generator contract has no license-authority state model, while presentation-only validation and duplicated historical sources let invented or ambiguous legal claims publish as valid README content.** | N/A | 70% | **96%** | X1-X3 reproduce evidence blindness; X4 reproduces false structural certification. |

The probabilities sum to 100%. H8 exceeds the 90% gate because it predicts
both invariances demonstrated by the fixture matrix: materially different
repository evidence cannot affect validation, and unrelated prose can satisfy
the supposed License-section requirement.

### Phase 7: Blame assignment

#### Level 1: Responsible lines

| Location | Behavior | Why it is wrong | Severity |
| --- | --- | --- | --- |
| `skills/book-publisher/references/readme-guide.md:79-88` | Treats `LICENSE`, a docs page, and MkDocs copyright display text as interchangeable, then invents CC BY-NC-SA when none is found. | Discovery order is not authority or scope, copyright display text is not permission, and missing evidence means default copyright rather than an affirmative grant. | Critical |
| `skills/book-publisher/references/readme-guide.md:346-364` | Unconditionally emits a complete CC BY-NC-SA license grant. | It can contradict, broaden, or replace the repository owner's actual terms. | Critical |
| `skills/book-publisher/references/readme-guide.md:499-514` | Requires a License section in every generated README. | The route has no representation for absent, ambiguous, split, custom, or unresolved evidence, so the required output pressures the agent to fabricate one. | High |
| `skills/book-publisher/scripts/validate-readme.py:25-61` | Detects required sections by substring search over all prose. | X4 proves an unrelated dependency-license mention is accepted as a repository License section. | High |
| `skills/book-publisher/scripts/validate-readme.py:189-224` | Accepts only a README path and initializes the report as valid. | Repository evidence and explicit authorization cannot affect the verdict, making unsupported legal claims indistinguishable from grounded ones. | High |
| `skills/archived/readme-generator/SKILL.md:81-99,350-357` and `docs/prompts/readme-generator-skill.md:25-31` | Preserve the same invented default in reusable historical sources. | A narrow active-guide fix can be mechanically reverted by later promotion or reuse. | Medium |

#### Level 2: Anti-patterns

1. **Configuration Without Constraints (AP8):** a security- and
   permission-sensitive default is treated as benign content configuration.
   No evidence, scope, or explicit-authority constraint protects it.
2. **Silent Failure Escalation (AP6):** the validator reports `GOOD` or
   `ADEQUATE` while the legal claim is unsupported or structurally absent.
   Its apparent health signal conceals the failed authority check.
3. **Untyped evidence collapse:** absent, one-file, multiple-file, custom,
   split-scope, and explicitly authorized states all collapse into prose. The
   generator cannot fail closed because it receives no typed state.
4. **Presentation validation standing in for semantic validation:** badges,
   links, substrings, and formatting are scored while the claim's source and
   scope are not part of the contract.
5. **Duplicated normative sources:** active guidance, archived guidance, and
   a historical prompt all restate the policy instead of deriving from one
   tested authority contract.

#### Level 3: Development practice

- A legal/permission decision was shipped as natural-language guidance rather
  than an executable evidence boundary with explicit inputs and outputs.
- Promotion from an archived standalone skill to an active route copied prose
  without a migration review of assumptions, target scope, or failure modes.
- Validation tests cover parser mechanics but omit adversarial repository
  states: absent evidence, conflicting files, custom terms, prose-only false
  positives, and explicitly authorized selections.
- The quality score starts from presentation completeness and has no
  fail-closed semantic gate for unsupported consequential claims.
- Repository-wide anti-pattern scans do not prevent unsafe legal defaults from
  being reintroduced through archived or generated teaching material.

The immediate fix must change the responsible lines. The systemic fix must
introduce a typed license-authority boundary and structural validation. The
durable practice change is to require negative fixtures and a repository-wide
contract scan whenever an agent route can publish permission, privacy,
security, or compliance claims.

### Phase 8: Immediate fix

- Removed the invented Creative Commons default and unconditional grant from
  the active README guide, archived source, and historical generation prompt.
- Made badges and License sections conditional on unambiguous repository
  evidence or an explicit owner-authorized selection for that repository.
- Defined absent, conflicting, compound, scoped, and nonstandard evidence as
  fail-closed states: omit a single-license claim and report the evidence
  state outside the generated README.
- Replaced substring section detection with ATX/Setext Markdown heading
  extraction and made License optional rather than a required section.
- Added regression tests proving that unrelated prose cannot satisfy a License
  section and that reusable guidance cannot restore the invented default.

Focused verification: 9/9 `book-publisher` tests pass, changed Python files
compile, `git diff --check` passes, and the targeted repository-wide unsafe
phrase scan has zero hits outside the repository's own licensed README and the
investigation evidence.

### Phase 9: Anti-pattern audit

**Date:** 2026-07-17

**Triggered by:** README route publishing an invented license

**Scope:** Full `dmccreary-claude-skills` graph plus prose/template fallback
search

**Method:** Primary investigator only because this session prohibits
subagents. The codebase-memory graph identified the active and archived
validator topology first; graph-augmented text search then covered Markdown
guidance and templates that have no call edges.

#### Executive summary

Seven findings span AP6 Silent Failure Escalation and AP8 Configuration
Without Constraints.

| Severity | Count | Action |
| --- | ---: | --- |
| Critical | 2 | Remove or condition the hardcoded grant immediately. |
| High | 3 | Add an authority state and make publication routes consume it. |
| Medium | 2 | Mark archived copies non-authoritative or keep them byte-equivalent to the safe contract. |

#### Findings

| ID | Anti-pattern | Severity | Location | Finding |
| --- | --- | --- | --- | --- |
| AP8-1 | Configuration Without Constraints | **Critical** | `skills/book-installer/references/about-page.md:289-301` | The generated About page grants CC BY-NC-SA permissions by default and only checks for a different license afterward. |
| AP8-2 | Configuration Without Constraints | **Critical** | `skills/book-installer/references/instructors-guide.md:188-197` | The template unconditionally calls every textbook free, open source, and Creative Commons licensed. |
| AP8-3 | Configuration Without Constraints | **High** | `skills/book-publisher/references/linkedin-carousel-guide.md:39,62,65-66,92` | The active carousel route treats `docs/license.md` as sufficient authority and hardcodes “free & open source” into summary and CTA slides. |
| AP8-4 | Configuration Without Constraints | **High** | `skills/book-publisher/references/carousel-content-sourcing.md:18` | The active sourcing table turns one docs page into a rights summary without preserving scope or ambiguity. |
| AP6-1 | Silent Failure Escalation | **High** | `skills/book-publisher/scripts/validate-readme.py:188-304` | After the immediate structural fix, the validator still has no repository-root or authority input, so a manually introduced unsupported claim can still receive a positive score. |
| AP6-2 | Silent Failure Escalation | **Medium** | `skills/archived/readme-generator/scripts/validate-readme.py:25-61,144-179` | A directly executable archived validator retains the original substring check and mandatory License section, creating a reintroduction path. The graph reached this copy as a distinct `validate_readme` call tree. |
| AP8-5 | Configuration Without Constraints | **Medium** | `skills/archived/linkedin-carousel-generator/` | Archived guide and sourcing copies preserve AP8-3/AP8-4 and can reintroduce them during promotion. |

#### Positive finding

`skills/book-media-generator/scripts/images/commons_metadata.py:71-104`
demonstrates the pattern to replicate: known terms are allowlisted, creator and
source evidence are required, official license URLs are checked, and unknown
or missing licenses raise `ManualRightsReviewRequired` instead of receiving a
convenient default.

#### Priority order

1. Immediate: condition AP8-1 and AP8-2 on grounded evidence.
2. Immediate: remove hardcoded “free & open source” claims from AP8-3 and make
   slide 9 optional when no grounded license state exists.
3. Structural: add one typed license-authority inspector and require both the
   README validator and publication guides to consume its JSON result.
4. Recurrence: synchronize or explicitly disable archived executable copies
   and add a repository-wide contract test for invented permission claims.

The cross-cutting issue is not Creative Commons itself. It is publishing a
permission claim from a presentation template without a typed evidence and
authorization boundary.

### Phase 10: Comprehensive remediation plan

#### Phase 1: Stop the bleeding (today)

| Fix | Findings | Status |
| --- | --- | --- |
| Remove invented README defaults and unconditional CC grant from all three reusable README guidance sources. | Incident L1, AP8 recurrence | Complete in `39622877`. |
| Make License optional and structurally detect headings. | Incident L1, AP6 escape | Complete in `39622877`. |
| Add failure-path tests for absent evidence and prose-only false positives. | Level 3 test deficiency | Complete in `39622877`. |
| Record AP8-1 and AP8-2 as separate investigations before modifying book-installer templates. | Critical adjacent findings | Required; these routes have independent ownership and acceptance tests. |

#### Phase 2: Structural hardening (this week)

1. Add a deterministic `inspect-license-authority.py` helper under
   `book-publisher` that accepts a repository root and emits JSON. It must
   distinguish at least: `absent`, `single-evidence`, `ambiguous`, `scoped`,
   `nonstandard-or-unresolved`, and `explicitly-authorized`.
2. Make the README validator derive the repository root from the README path
   by default, with an explicit override for tests and unusual layouts.
3. When a README has a License heading or license badge, require grounded
   repository evidence or an explicit owner-authorized value. Absent and
   ambiguous states are errors, not score deductions.
4. Require grounded sections to link the exact evidence path. The validator
   may attest evidence linkage; it must not pretend to render a legal opinion
   about arbitrary custom text.
5. Add fixtures for absent evidence, one root file, multiple files, docs-only
   scoped terms, custom text, and explicit authorization. Assert that no
   validation path creates or changes a license file.
6. Make the archived executable validator delegate to or stay byte-equivalent
   with the active authority contract, or mark it non-executable and
   non-authoritative.

#### Phase 3: Architectural hardening (next sprint)

1. Move license state into one shared publication-evidence contract consumed
   by README, About page, instructors guide, carousel, LinkedIn, and future
   publication routes.
2. Replace each route's direct `docs/license.md` read with that contract,
   preserving repository, content, file, and compound scopes.
3. Add a release gate that scans active, archived, prompt, and packaged
   guidance for invented permission defaults and compares packaged copies with
   their source contracts.
4. Adopt the media generator's established pattern: allowlisted known states,
   verified source evidence, typed unresolved/manual-review outcomes, and no
   convenience default.
5. Require adversarial evidence fixtures whenever a route publishes legal,
   security, privacy, accessibility, or compliance claims.

#### Accepted debt

- The helper will not identify every legal text or decide whether terms are
  enforceable. Unknown/custom text remains unresolved and fail-closed.
- Compound SPDX semantics and file-level REUSE data can initially be reported
  as scoped/ambiguous evidence rather than fully evaluated. Preserving the
  complexity is safer than collapsing it.
- Archived narrative incident evidence may quote unsafe wording; contract
  scans should exclude clearly marked investigation evidence, not erase it.

#### What not to do

1. Do not replace one invented default with another common license.
2. Do not treat `mkdocs.yml` copyright text, an author's usual preference, a
   public GitHub repository, or `docs/license.md` existence as repository-wide
   authority.
3. Do not silently create, rewrite, rename, or copy a license file while
   generating or validating a README.
4. Do not make license identification depend on a network call; offline and CI
   behavior must be deterministic.
5. Do not claim that one detected file proves one repository-wide license when
   file headers, package metadata, or scoped documentation conflict.
6. Do not hide adjacent route fixes in this incident PR; give each independent
   publication defect its own investigation and tests while sharing the same
   authority contract.

### Structural remediation evidence

The systemic implementation now adds one offline, read-only authority
inspector and makes both active and archived README validation consume the
same contract:

- `skills/book-publisher/scripts/license_authority.py` discovers only regular
  repository-contained root evidence and distinguishes `absent`, `scoped`,
  `single-evidence`, `nonstandard-or-unresolved`, `ambiguous`, and
  `explicitly-authorized` states.
- `skills/book-publisher/scripts/validate-readme.py` treats unsupported or
  mismatched headings, badges, and affirmative prose claims as hard failures.
  One-file claims must link the exact evidence path. Custom terms permit only
  neutral wording tied to that path.
- `skills/archived/readme-generator/scripts/validate-readme.py` is now a
  compatibility wrapper over the active validator, eliminating the executable
  duplicate contract.
- The active guide requires the inspector and validator before publication and
  states that neither tool may create or modify license files.

The pre-PR code review found and closed five additional boundary defects:

1. Compound or unknown SPDX expressions could be truncated into one apparent
   identifier. They now remain unresolved and require manual review.
2. Affirmative license prose outside a License heading could avoid authority
   validation. It is now detected without treating a neutral tooling reference
   as a repository claim.
3. Bare repository-relative Markdown links such as `LICENSE` were incorrectly
   scored as invalid. Safe relative destinations are now accepted.
4. Bare identifiers in ATX or Setext License sections could be presented as
   custom neutral terms. Section bodies now receive stricter identifier
   detection.
5. Symlinked files or `LICENSES/` directories could make evidence depend on
   content outside the repository. Discovery now rejects those paths.

Verification on the final reviewed tree:

- 34/34 focused `book-publisher` tests pass.
- 160/160 tests across all eleven repository test directories pass.
- The three changed Python entry points compile.
- Strict MkDocs publication succeeds.
- `git diff --check` succeeds.
- CE Compound produced
  `docs/solutions/logic-errors/permission-claims-require-typed-authority.md`;
  its frontmatter and mechanical source/link claims validate with zero flags.
- `CONCEPTS.md` is absent, so lightweight vocabulary capture correctly made no
  glossary mutation. `CLAUDE.md` does not currently surface `docs/solutions/`;
  that discoverability gap is recorded rather than widened into this incident.

## Execution Checklist

- [x] Open the investigation and preserve the initial reproduction.
- [x] Calibrate the generative prior and record initial hypotheses.
- [x] Collect non-destructive source, history, route, and validation evidence.
- [x] Run targeted experiments against absent, conflicting, nonstandard, and
  prose-only license states.
- [x] Assign three-level blame after one hypothesis exceeds 90%.
- [x] Implement the immediate and systemic remediation.
- [x] Search the entire repository for the anti-pattern.
- [ ] Run focused, full, release, and installed-skill validation.
- [ ] Commit, open a PR, babysit it to merge, and verify `origin/main`.
- [x] Run CE Compound.
- [ ] Replace `CURRENT` with merged, installed, and closure evidence.
