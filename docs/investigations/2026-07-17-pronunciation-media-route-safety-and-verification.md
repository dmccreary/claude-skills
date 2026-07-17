# Pronunciation Media Route Safety and Verification Investigation

## Status

CURRENT

## Symptom

The active `book-media-generator` pronunciation route is not safe or
verifiable as a publication workflow:

- `--output pareto.mp3` calls `os.makedirs("")` and raises
  `FileNotFoundError` before making the API request.
- `slugify("../escape")` returns `../escape`, and `slugify("A/B Test")`
  returns `a/b-test`, so generated names can escape or create unintended
  directories.
- API response bytes are written directly to the final `.mp3` path without
  atomic staging, media validation, artifact provenance, or failure cleanup.
- The guide publishes inline `onclick` JavaScript, which is blocked by a
  strict Content Security Policy and does not define an accessible playback
  status or error state.
- The guide hard-codes model, voice, and SSML capability claims and points at
  a private machine path instead of current primary documentation.

## Impact

An agent following the active skill can fail on a valid basename output,
write outside the intended audio directory, publish truncated or non-audio
bytes under an `.mp3` extension, or produce a playback control that does not
work under a strict Content Security Policy. The resulting artifact cannot be
traced to the term, model, voice, request parameters, or source response that
created it.

Severity is **high** for the generator contract because user-controlled output
names can cross path boundaries and failed or malformed network responses can
be mistaken for completed publication assets. The browser-control defect is
**medium** because it blocks playback and obscures failure without corrupting
other files.

## Phase 0: Tools

The investigation uses a clean worktree based on `origin/main`, Git history,
GitHub CLI access, `rg`, Python standard-library tests, browser tests where
applicable, the full codebase-memory index for this worktree, primary vendor
documentation, repository release validators, and live audio/browser playback
verification. All required tools were exercised before evidence collection.

## Established Timeline

| Time / marker | Event | Confidence | Source | Timezone |
| --- | --- | --- | --- | --- |
| 2026-07-10 05:37:21 CDT, commit `1e3206a2` | The archived pronunciation route, including the generator and guide, entered the fork during the Fable 5 refactor. | High | `git log --follow` | Commit offset `-05:00` |
| 2026-07-10 05:56:57 CDT, commit `d133ef8b` | The same route was promoted into the active `book-media-generator` skill. | High | `git log --follow` and current paths | Commit offset `-05:00` |
| 2026-07-17, source commit `4d27c014` | The unsafe path handling, direct final-path write, inline handler, and stale capability guidance remain on current `origin/main`. | High | Fresh worktree source read | Date only; no time claim |

## Preserved Source Evidence

| Location | Observed behavior |
| --- | --- |
| `skills/book-media-generator/scripts/audio/generate-pronunciation.py:25-27` | Slug construction removes only spaces and quotes; separators and traversal segments survive. |
| `skills/book-media-generator/scripts/audio/generate-pronunciation.py:77-83` | The script creates an empty parent for basename outputs and streams response bytes directly into the final file. |
| `skills/book-media-generator/references/pronounce-button-guide.md:18-23` | Prerequisites cite a private developer-machine path. |
| `skills/book-media-generator/references/pronounce-button-guide.md:40-54` | Model and SSML behavior are asserted as fixed facts without a current primary-source check. |
| `skills/book-media-generator/references/pronounce-button-guide.md:110-147` | Published examples use inline `onclick` handlers and define no playback status or error contract. |

## Hypotheses

### Generative-prior calibration

A repository search finds 20 `CONFIRMED` mentions and 11 `REFUTED` mentions
across 15 investigation files. Those labels are sparse, repeated within some
documents, and not consistently one-per-hypothesis, so the apparent 65% ratio
is not a measured first-pass hit rate. This investigation therefore uses the
methodology's conservative 20% prior: most hypotheses listed in Phase 2 will
be wrong, and the true cause is probably absent from the initial list.

No source-reading narrative becomes root cause without an executable
experiment. The Phase 2 table will reserve substantial probability for "the
true cause is not yet listed," and at least one experiment will exercise the
unmodified route in a way that can reveal a cause not named in advance.

### Assumptions

| # | Type | Assumption | Initial P | Inverse | Verification |
| --- | --- | --- | ---: | ---: | --- |
| A1 | ordering | The archived route existed before the active route. | 98% | 2% | Compare path history and introducing commits. |
| A2 | provenance | The active generator was copied from the archived generator. | 90% | 10% | Byte-compare the two versions and inspect the promotion patch. |
| A3 | architecture | No caller constrains `--output` to an approved root before this script receives it. | 80% | 20% | Search all callers and docs. |
| A4 | behavior | Agents execute this script directly from the active guide. | 90% | 10% | Inspect the guide, skill routing, and packaged install. |
| A5 | protocol | A successful HTTP status does not prove the response body is valid MPEG audio. | 95% | 5% | Check the vendor response contract and exercise mocked bodies. |
| A6 | browser | A strict Content Security Policy blocks inline event handlers. | 95% | 5% | Check the browser standard and run a strict-CSP fixture. |
| A7 | external | At least one hard-coded vendor capability claim can drift independently of this repository. | 80% | 20% | Compare current primary API documentation with the guide. |
| A8 | prevention | No executable test currently covers the active pronunciation generator or markup contract. | 90% | 10% | Search repository tests and CI commands. |
| A9 | scope | The active guide is an operating contract rather than historical commentary. | 95% | 5% | Inspect `book-media-generator/SKILL.md` routing and packaged paths. |

### Initial hypothesis table

| # | Hypothesis | Category | Initial P | Assumptions | Ceiling |
| --- | --- | --- | ---: | --- | ---: |
| H1 | The archived demo route was promoted into an active publication skill without hardening its path, network-response, provenance, or browser contracts. | migration | 20% | A1, A2, A4, A9 | 73% |
| H2 | The generator treats a final pathname as an ordinary string because the route has no artifact-transaction abstraction or approved output root. | architecture | 15% | A3, A4 | 72% |
| H3 | The implementation assumes a successful TTS response is valid audio and writes it directly, so protocol failures become publication artifacts. | network protocol | 8% | A5 | 95% |
| H4 | The browser example was copied from a permissive demo and never migrated to CSP-compatible, accessible playback state. | frontend migration | 8% | A6, A9 | 90% |
| H5 | Current vendor model, voice, and pronunciation-control behavior has drifted from the guide's hard-coded claims. | external drift | 6% | A7 | 80% |
| H6 | The repository's validation surface omits executable contracts for active scripts and operational guides, allowing every defect above to ship together. | quality system | 8% | A8, A9 | 86% |
| H7 | The true cause is not yet listed. | unknown | 35% | none | 100% |

The probabilities sum to 100%. The maximum-pain hypothesis is H1 because it
implicates the recent decision to promote an archived route into the active
meta-skill, rather than blaming ElevenLabs or browser policy. H6 is the painful
escape-mechanism candidate because it implicates the repository's own release
gate. Phase 5 will test H1 first and include a direct execution experiment that
can convert H7 into a named cause rather than merely selecting among H1-H6.

## Evidence and Experiments

### Phase 3: Non-destructive evidence collection

#### Revised assumptions

| # | Assumption | Initial P | Revised P | Evidence |
| --- | --- | ---: | ---: | --- |
| A1 | The archived route existed before the active route. | 98% | **99%** | Git history places the archived source in `1e3206a2` and active promotion in `d133ef8b`. |
| A2 | The active generator was copied from the archived generator. | 90% | **99%** | The two generator files are byte-identical and have the same code-graph fingerprint. |
| A3 | No caller constrains `--output` before the script receives it. | 80% | **98%** | The code graph finds only `main()` as an inbound caller; source search finds no wrapper. |
| A4 | Agents execute this script directly from the active guide. | 90% | **99%** | The active skill routes pronunciation requests to the guide, which invokes the script directly. |
| A5 | HTTP success does not prove valid MPEG audio. | 95% | **95%** | The API contract returns an audio body and selectable format; validity still requires checking the received representation. Executable proof remains pending. |
| A6 | Strict CSP blocks inline event handlers. | 95% | **99%** | MDN explicitly lists inline event handlers as disallowed and recommends `addEventListener()`. |
| A7 | Vendor capability claims can drift independently. | 80% | **99%** | Current API docs expose `GET /v1/models`, `GET /v2/voices`, output-format selection, and versioned pronunciation dictionaries. |
| A8 | No executable test covers this route. | 90% | **99%** | Repository-wide test search found only the source files, not pronunciation tests. |
| A9 | The guide is an active operating contract. | 95% | **99%** | `book-media-generator/SKILL.md` explicitly routes a user request to this guide and script. |

#### Evidence

### E1: Active generator is the archived implementation

- `cmp` reports the archived and active generator files are byte-identical.
- The code graph assigns both functions the same implementation fingerprint.
- The active guide differs from the archived skill only in frontmatter/title
  and its installed path.
- Confidence: high. Supports H1 and confirms A1-A2.

### E2: There is no protective caller boundary

- Code-graph inbound tracing finds only the module's own `main()` calling
  `generate_pronunciation()`.
- Repository search finds the active guide invoking the script directly and
  no wrapper that approves an output root or validates an artifact.
- Confidence: high. Supports H2 and confirms A3-A4.

### E3: The release surface has no pronunciation contract

- Repository-wide test search finds no test importing or invoking the active
  pronunciation generator and no browser fixture for the published markup.
- Confidence: high. Supports H6 and confirms A8.

### E4: Vendor capabilities are discoverable and versioned

- The official [Create speech API](https://elevenlabs.io/docs/api-reference/text-to-speech/convert)
  defines `output_format`, says model IDs should be queried through
  `GET /v1/models`, and returns generated audio.
- The official [pronunciation dictionary guide](https://elevenlabs.io/docs/eleven-api/guides/how-to/text-to-speech/pronunciation-dictionaries)
  currently documents phoneme support for `eleven_flash_v2` and `eleven_v3`,
  with versioned dictionary locators.
- The official [API introduction](https://elevenlabs.io/docs/api-reference/introduction/)
  exposes request and trace identifiers in response headers for debugging and
  provenance.
- Confidence: high. Supports H5 in its drift-risk form and confirms A7. It
  also shows that a durable client can record output format and request IDs.

### E5: Inline `onclick` is incompatible with strict CSP

- MDN's [Content Security Policy guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
  says inline event handlers are disallowed and should be refactored to
  `addEventListener()`.
- The current guide's exact pattern uses inline `onclick`.
- Confidence: high. Supports H4 and confirms A6.

### E6: Native audio controls already provide core user control

- MDN's [`audio` element reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)
  documents native controls for volume, seeking, pause, and resume.
- W3C's [audio-control guidance](https://www.w3.org/WAI/WCAG21/Understanding/audio-control.html)
  requires a mechanism to stop longer-playing audio and recognizes clearly
  labelled user-initiated controls.
- Confidence: high. Establishes a standards-backed baseline for the browser
  remediation without yet selecting the final UI.

### E7: Python provides a same-directory atomic publication primitive

- The Python [`tempfile` documentation](https://docs.python.org/3.11/library/tempfile.html)
  recommends creating a temporary file immediately rather than inventing a
  name and opening it later.
- The Python [`os.replace` documentation](https://docs.python.org/3.12/library/os.html#os.replace)
  states that a successful replacement is atomic on POSIX and notes that it
  can fail across filesystems. A temporary file in the destination directory
  therefore provides the appropriate publication boundary.
- Confidence: high. This does not prove the root cause; it establishes that
  the missing atomic-write contract has a standard-library remediation.

#### Phase 4: Revised hypothesis table after evidence

| # | Hypothesis | Initial P | Revised P | Ceiling | Key evidence |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | Archived demo route was promoted without publication hardening. | 20% | **5%** | 96% | Subsumed by H8 after E1 and E3 established both entry and escape mechanisms. |
| H2 | No artifact-transaction or approved-root abstraction exists. | 15% | **5%** | 97% | E2 confirms the missing boundary, but this is a mechanism rather than the complete causal chain. |
| H3 | HTTP-success assumptions turn malformed responses into assets. | 8% | **5%** | 95% | Source supports the mechanism; executable response-body proof remains pending. |
| H4 | Demo markup never migrated to CSP-compatible accessible playback. | 8% | **5%** | 98% | E1 and E5 establish copied inline-handler behavior. |
| H5 | Vendor capability drift invalidates hard-coded guidance. | 6% | **3%** | 99% | E4 proves drift risk and discoverability, but most guide claims remain plausible. |
| H6 | Missing executable contracts allowed the defects to ship together. | 8% | **7%** | 98% | Subsumed by H8 after E3 found no route tests. |
| H7 | The true cause is not yet listed. | 35% | **10%** | 100% | Retained until direct execution can reveal an unlisted failure. |
| H8 | **The active incident is an unmodified demo-to-production promotion whose path, response, provenance, and browser assumptions escaped because the promoted route had no executable contract.** | N/A | **60%** | 95% | E1-E5 connect the promotion, direct execution boundary, missing tests, and incompatible browser example. |

The probabilities sum to 100%. H8 is above 50% but below 80%, so Phase 5
must execute the untouched route before blame assignment. The required
experiment will test valid basename output, traversal-capable names, malformed
successful responses, partial reads, and strict-CSP markup. That matrix can
also convert H7 into a concrete new hypothesis if the implementation fails in
an unanticipated way.

#### Web checkpoint

Primary-source research found no vendor or browser defect that requires the
current implementation. ElevenLabs exposes output-format selection, model and
voice discovery, pronunciation dictionaries, and request/trace metadata. MDN
documents inline-handler rejection as expected strict-CSP behavior, and Python
documents same-directory temporary files plus atomic replacement. The leading
hypothesis therefore remains a local promotion and validation failure rather
than an upstream platform bug.

### Phase 5: Experiments

The migration/quality-system category has zero prior experiments, so the
three-strike pivot does not apply.

#### X1: Execute the untouched publication contract

- **Tests:** H8, unmodified demo-to-production promotion without an executable
  contract.
- **Predicted outcome if H8 is true:** focused tests against the untouched
  route will fail for basename output, separator/traversal slugs, malformed
  successful bodies, interrupted reads that target an existing final file,
  missing provenance, inline handlers, and missing playback state.
- **Predicted outcome if H8 is false:** the current route will already preserve
  the approved path and prior artifact, reject invalid audio, record
  provenance, and publish CSP-compatible accessible controls; or failures will
  reveal a materially different cause not named in H1-H6.
- **Procedure:** add a standard-library test module that imports the active
  script, replaces `urlopen` with deterministic response doubles, uses only a
  temporary directory, and statically validates the active guide. Run the
  tests before changing implementation or guide files and preserve every
  failing assertion.
- **Actual outcome:** Eight tests produced ten failed subtests and two errors
  on untouched source. Basename output raised `FileNotFoundError`; traversal
  and separators survived slugging; a JSON body with HTTP success was written
  as `.mp3`; an interrupted read truncated an existing artifact to zero bytes;
  no provenance sidecar was created; the private path and hard-coded
  capability omissions remained; and the guide still contained inline
  `onclick` with no controls, accessible name, status region, or event-based
  error contract.
- **Conclusion:** H8 rises from 60% to 93%. The experiment reproduces the
  exact promotion and escape mechanisms predicted from E1-E5 and reveals no
  competing external cause. H7 falls from 10% to 2%; its reserved experiment
  did not expose an unlisted failure category. The destructive truncation of
  an existing final artifact confirms that atomic staging is immediate
  remediation, not optional hardening.

### Phase 6: Final hypothesis revision

| # | Hypothesis | Initial P | Post-evidence P | Post-experiment P | Key experiment |
| --- | --- | ---: | ---: | ---: | --- |
| H1 | Archived demo route was promoted without publication hardening. | 20% | 5% | **1%** | Subsumed by H8 after X1 reproduces the complete route contract. |
| H2 | No artifact-transaction or approved-root abstraction exists. | 15% | 5% | **1%** | Confirmed mechanism, subsumed by H8. |
| H3 | HTTP-success assumptions turn malformed responses into assets. | 8% | 5% | **1%** | Confirmed mechanism, subsumed by H8. |
| H4 | Demo markup never migrated to CSP-compatible accessible playback. | 8% | 5% | **1%** | Confirmed mechanism, subsumed by H8. |
| H5 | Vendor capability drift invalidates hard-coded guidance. | 6% | 3% | **1%** | Contributing maintenance risk, not the incident's root cause. |
| H6 | Missing executable contracts allowed the defects to ship together. | 8% | 7% | **1%** | Confirmed escape mechanism, subsumed by H8. |
| H7 | The true cause is not yet listed. | 35% | 10% | **1%** | X1 revealed no unlisted failure category. |
| H8 | **Root cause: an archived demo was promoted unchanged into an active publication route, and no executable route contract rejected its path, response, provenance, and browser assumptions.** | N/A | 60% | **93%** | X1 fails across every predicted boundary on untouched source. |

The probabilities sum to 100%. H8 exceeds the 90% decision gate.

The post-experiment web checkpoint found the destructive read behavior in the
Python [`open()` contract](https://docs.python.org/3/library/functions.html#open):
write mode truncates an existing file before data is written. That exactly
matches X1's zero-byte artifact and confirms ordinary local file semantics,
not a network or interpreter bug. Official ElevenLabs voice and model pages
also reinforce that these resources are queryable and mutable, so the guide
should verify requested IDs rather than canonize an unverified static list.

## Blame Assignment

### Level 1: Responsible source lines

Line numbers refer to unremediated source at `4d27c014`.

| Location | Code or contract | Why it is wrong | Severity |
| --- | --- | --- | --- |
| `scripts/audio/generate-pronunciation.py:25-27` | `slugify()` removes only spaces and quotes. | Path separators and traversal components survive into generated file names. | High |
| `scripts/audio/generate-pronunciation.py:77-78` | `os.makedirs(os.path.dirname(output_path))` | A valid basename has an empty dirname and crashes before the request. | Medium |
| `scripts/audio/generate-pronunciation.py:81-83` | `open(output_path, "wb")` precedes `response.read()`. | Write mode truncates an existing final artifact before the replacement response is available. | Critical |
| `scripts/audio/generate-pronunciation.py:81-85` | Every successful body is written and announced as generated. | There is no MIME, MP3-signature, length, output-format, or response-metadata validation. | High |
| `references/pronounce-button-guide.md:20-23` | Prerequisites cite `/Users/dan/...`. | The active skill depends on a private, non-portable documentation path. | Medium |
| `references/pronounce-button-guide.md:40-54,186-197` | Model and voice choices are fixed prose. | Queryable external capabilities are presented as timeless inventory without verification. | Medium |
| `references/pronounce-button-guide.md:119-122,145-146` | The exact publication pattern uses inline `onclick`. | Strict CSP blocks the control, and the pattern defines no state or failure feedback. | High |

### Level 2: Anti-patterns

The initiating anti-pattern is **demo promotion without a boundary audit**.
The active route was copied byte-for-byte from an archived skill while its
status changed from historical material to executable publication guidance.
The promotion changed the route's authority but not its engineering contract.

The generator combines three related anti-patterns:

1. **Ambient path strings as authority.** A string supplied by the caller is
   treated as permission to create or replace any resolved path.
2. **In-place publication.** Network input is read only after the final file is
   opened and truncated; generation and publication are one irreversible step.
3. **Status-code-as-content-validation.** A transport success is treated as a
   valid media artifact without checking representation metadata or bytes.

The guide adds **external inventory as prose** and **inline behavior as
content**. Both can be locally readable while already wrong in the environment
where the skill executes.

### Level 3: Development practice

The repository assembled an active meta-skill by moving and copying files but
did not require each promoted route to pass an executable operating-contract
test. Documentation review checked that a route existed, not that it was safe
to execute, portable across installations, current against its vendor, or
usable under browser security and accessibility constraints.

The durable practice change is a route-level contract for every active
script-backed guide. At minimum it must exercise valid and adversarial paths,
network interruption, malformed successful responses, existing-artifact
preservation, provenance, external-capability discovery, and the browser
markup contract. Archived material may remain historical; promotion to an
active skill must make that contract mandatory.

## Phase 8: Immediate Fix

The immediate fix replaces the unsafe active route without changing unrelated
media workflows:

- `slugify()` now emits one non-empty filename component.
- `resolve_output_path()` confines `.mp3` publication beneath an explicit
  approved root and supports a basename destination.
- The API request pins `output_format` and asks for MPEG audio. A successful
  body is not publishable until both its media type and MP3 signature pass.
- Audio and provenance are written to same-directory temporary files, flushed
  with `fsync`, and moved into place with `os.replace` only after validation.
  A failed read therefore leaves the previous artifact untouched.
- A JSON sidecar records the request fingerprint, audio digest, model, voice,
  output format, byte count, request ID, trace ID, and generation time.
- Matching artifacts are idempotently reused. A mismatched existing output is
  retained unless the caller explicitly supplies `--force`.
- The active guide now links primary capability sources, requires current
  `GET /v1/models` and `GET /v2/voices` discovery, and removes the private
  machine prerequisite.
- Published markup uses native audio controls, an accessible label and
  fallback link, a live status region, and an external event controller with
  no inline JavaScript.

Focused standard-library verification passes 16/16 tests. It covers basename
output, path escape rejection, safe slugs, malformed successful responses,
oversized bodies, bounded network time, interrupted reads, paired-publication
rollback, provenance, request parameters, idempotent reuse, explicit
replacement, staging cleanup, current guide sources, and CSP/accessibility
contracts. The complete media-generator Python suite passes 27/27 tests.

The strict-CSP Playwright fixture passes 2/2 tests at 1280x900 and 390x844.
Chromium loads the external controller without a page error, exposes native
controls and the accessible name, reports play/pause/error state, and has no
horizontal overflow.

## Phase 9: Anti-Pattern Audit

The class-wide audit searched the code graph first for sibling publication
functions, callers, and tests, then used text search for markup and guidance
variants that are not represented as executable graph edges. The current
pronunciation fix remains intentionally scoped; each active sibling below is
tracked as a separate investigation rather than being silently expanded into
this patch.

| Severity | Route | Evidence | Required follow-up |
| --- | --- | --- | --- |
| **High** | `skills/book-media-generator/scripts/story/generate-images.py` | Graph tracing shows `main()` calling `generate_one()`, which writes Gemini `inline.data` directly to the final path. `verify_dimensions()` runs only after publication, and a decode result of `None` does not fail the record, so invalid bytes can remain and be recorded as successful. No route test was found. | Add output confinement, validated decoding before publication, same-directory atomic replacement, provenance, idempotency, and destructive-failure regressions. |
| **Medium** | `src/image-generation/generate-cover-openai.py` and `generate-logo-openai.py` | Graph tracing shows API bytes decoded through Pillow, then saved in place to caller-controlled final paths. Decoding validates the representation, but there is no approved root, atomic publication boundary, request provenance, or idempotency contract. | Harden the utilities or place them behind the repository's transactional media contract, with focused tests. |
| **High** | `skills/microsim-generator/references/docker-python-lab-guide.md` and `assets/templates/timeline/index.md` | Text audit found active routed examples with inline event handlers. These repeat the strict-CSP failure class fixed in the pronunciation guide. | Replace inline handlers with external controllers and add strict-CSP, keyboard, status, and error-state browser tests. |
| **Medium** | `skills/book-media-generator/references/story-guide.md` and `skills/microsim-utils/references/screen-capture.md` | Text audit found private `/Users/dan/...` paths in active operating guidance. The story guide also publishes mutable model, quota, and pricing claims as fixed prose. | Replace private paths with repository-relative or configurable locations and move mutable vendor facts behind primary-source discovery and dated verification. |

Two nearby routes provide useful positive patterns. The Commons metadata
client classifies 429 responses, bounds retries, clamps `Retry-After`, and
validates contact configuration. The book installer already has pinned,
transactional output behavior with executable tests. Those patterns should be
reused rather than creating another media-specific retry or transaction
framework.

This audit changes the organizational conclusion but not the root-cause
probability: the pronunciation incident is one instance of a broader absence
of mandatory publication contracts across promoted media routes. The current
fix establishes such a contract for pronunciation; the sibling investigations
must apply the same boundary independently and prove it against their own
media semantics.

## Remediation Plan

### Phase 1: Stop the bleeding (today, less than one day)

1. Ship the scoped pronunciation generator and guide changes already described
   in Phase 8. Keep the old final artifact intact on every failed request, and
   reject paths outside the caller-declared output root before network access.
2. Run the focused 16-test generator contract, the complete 27-test
   media-generator Python suite, the 2-viewport strict-CSP Playwright contract,
   Python compilation, JavaScript syntax, and whitespace gates in CI.
3. Generate one real MP3 with a currently discovered model and voice, inspect
   its sidecar and hashes, and play it through the strict-CSP control before
   calling the route released. If credentials are unavailable, keep this as an
   explicit human-required release gate rather than substituting fixture bytes.
4. Record the story-image, OpenAI cover/logo, and MicroSim CSP siblings as
   separate investigations with exact source evidence. They are not closure
   blockers for the scoped pronunciation patch, but they must not disappear
   into prose-only follow-up.

**Do not:** broaden the patch into unrelated media routes; accept an HTTP 200
or `.mp3` suffix as audio validation; publish directly to the final path; put a
credential in a test, guide, sidecar, shell history, or repository; or mark the
incident resolved from mocked tests alone.

### Phase 2: Structural hardening (this week, about three days)

1. Make the pronunciation contract workflow a required repository check for
   changes to the generator, guide, controller, fixture, or contract tests.
2. Add a promotion checklist for every script-backed route moved from archived
   material into an active skill. Require adversarial paths, interrupted input,
   malformed successful input, preservation of an existing artifact,
   provenance, idempotency, portability, current primary sources, and a browser
   contract when the route emits UI.
3. Complete the three sibling investigations. Fix each High finding with its
   own media semantics and deterministic red/green reproduction before sharing
   implementation code.
4. Add a published-guidance scan that rejects private home-directory examples
   and inline event handlers in active routes while allowing explicitly marked
   historical incident evidence and test fixtures.
5. Define a dated capability-verification record for mutable model, voice,
   quota, and pricing claims. Operational guides should point to discovery
   endpoints or primary documentation rather than copy an inventory into prose.

**Do not:** use a giant repository-wide regex rewrite; treat all binary files
as if they share MP3 validation; turn transient vendor inventory into a checked
in allowlist; or make browser examples depend on `unsafe-inline` CSP.

### Phase 3: Architectural hardening (next sprint, about one week)

1. After the sibling investigations define their needs, extract the common
   publication transaction: approved-root resolution, same-directory private
   staging, format-specific validation hook, digest/provenance generation,
   atomic replacement, idempotent reuse, and explicit replacement policy.
2. Keep representation validators pluggable. MP3, PNG/JPEG, SVG, video, and
   generated HTML require different structural and safety checks even when
   they share publication mechanics.
3. Make the active-skill release validator enumerate script-backed guide
   routes and require a declared executable contract for each. A route without
   a contract may remain archived but cannot be promoted as active guidance.
4. Add a small, versioned provenance schema with request fingerprints and
   non-secret debugging identifiers. Validate schema compatibility in tests so
   later tools can inspect artifacts without parsing guide-specific JSON.
5. Use one reusable strict-CSP, accessibility, and responsive browser harness
   for generated controls, while preserving route-specific interaction tests.

**Do not:** create a remote asset service, database, or job queue for local
book generation without measured need; centralize vendor clients merely to
share a few lines; or allow the shared transaction to bypass route-specific
validation and user authorization.

### Accepted debt

- Network generation remains synchronous because this CLI creates one short
  pronunciation asset at a time; a queue adds failure modes without current
  throughput evidence.
- MP3 validation uses declared media type plus MPEG/ID3 signature rather than
  full audio decoding. Real generation and browser playback are the release
  gate; a decoder dependency should be added only if malformed signed payloads
  are observed.
- Provenance records vendor request and trace IDs when returned but does not
  require them, because intermediaries or vendor changes may omit those
  headers. The request fingerprint and audio digest remain mandatory.
- The archived pronunciation copy is not rewritten by this incident. Active
  guidance is authoritative; archived material should be labeled historical
  and audited separately if it can still be invoked by an installer.

### Closure gates

The incident is resolved only after the scoped change is reviewed, merged,
and verified from the published repository; all automated tests pass; one real
audio artifact is generated, provenance-checked, and played; the active guide
and packaged skill are byte-consistent; sibling investigations are durably
tracked; and the repository receives a CE Compound learning that links this
investigation and its prevention contract.
