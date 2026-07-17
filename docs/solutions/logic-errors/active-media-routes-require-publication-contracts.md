---
title: Active Media Routes Require Publication Contracts
date: 2026-07-17
category: logic-errors
module: book-media-generator
problem_type: logic_error
component: tooling
symptoms:
  - A valid basename output crashes before the API request
  - User-derived names can escape or create unintended output directories
  - Interrupted or malformed responses can replace a verified media artifact
  - Published controls fail under strict Content Security Policy
root_cause: missing_validation
resolution_type: code_fix
severity: high
tags: [media-publication, atomic-write, provenance, csp, skill-promotion]
---

# Active Media Routes Require Publication Contracts

## Problem

An archived pronunciation demo became an active `book-media-generator` route
without changing its engineering contract. The route looked complete because
it could call the vendor and emit an MP3, but it did not constrain the output
path, validate the received representation, preserve an existing artifact on
failure, record provenance, or verify the browser control it taught agents to
publish.

## Symptoms

- `--output pareto.mp3` passed an empty parent string to directory creation and
  failed before making a request.
- Separators and traversal syntax survived filename construction.
- The final MP3 was opened in write mode before the response was read, so an
  interrupted read truncated a previous artifact.
- A successful JSON error body could be published under an `.mp3` suffix.
- Audio and provenance had no paired rollback contract.
- Inline playback handlers were blocked by strict CSP and exposed no accessible
  status or failure state.

The complete reproduction and causal record is in
[the pronunciation media investigation](../../investigations/2026-07-17-pronunciation-media-route-safety-and-verification.md).

## What Didn't Work

- **Treating an archived route as vetted because it already existed.** Moving a
  script into an active skill changes its authority, not its safety.
- **Treating HTTP success as content validation.** Transport status does not
  prove MIME type, media structure, completeness, or intended output format.
- **Writing directly to the final pathname.** This combines generation and
  publication, so an interrupted operation destroys prior verified state.
- **Testing only the Python happy path.** The route also publishes browser
  behavior; a valid MP3 does not make an inline-handler control usable under
  the deployment CSP.

## Solution

The pending remediation in
[PR #36](https://github.com/yaniv256/dmccreary-claude-skills/pull/36)
turns generation into a bounded publication transaction:

1. Resolve one `.mp3` destination beneath an explicitly approved root.
2. Set a network timeout and response-size ceiling.
3. Require an expected media type and recognizable MP3 signature before any
   final-path mutation.
4. Stage audio and JSON provenance in private same-directory temporary files,
   flush them, and publish with `os.replace`.
5. Back up an existing audio/provenance pair and restore it when either final
   replacement fails. If rollback cannot be proved, retain recovery files and
   fail closed.
6. Record the request fingerprint, audio digest, model, voice, output format,
   byte count, and non-secret request/trace identifiers.
7. Reuse only a byte-matching artifact; require explicit `--force` for a
   different request.
8. Publish native audio controls with an external controller, accessible name,
   live status, fallback link, and strict-CSP browser tests.

The implementation and deterministic contracts live in:

- `skills/book-media-generator/scripts/audio/generate-pronunciation.py`
- `skills/book-media-generator/tests/test_pronunciation_media_contract.py`
- `skills/book-media-generator/tests/test_pronunciation_controls_browser.spec.js`
- `skills/book-media-generator/references/pronounce-button-guide.md`

## Why This Works

Validation now occurs before publication, and publication is separated from
network generation. A failed read cannot touch the destination. A failed
two-file replacement restores the old pair, so an audio digest and provenance
record cannot silently drift apart during a handled error. Confinement turns a
caller-provided pathname into a location within a declared authority boundary
rather than treating the string itself as permission.

The browser test protects the other half of the operating contract. It proves
that generated markup remains interactive at desktop and mobile widths under
the same strict CSP that rejects the former inline handler.

## Prevention

- Treat promotion from archived material to an active skill as a release. Run
  a boundary audit even when the files are copied byte-for-byte.
- Require every active script-backed media guide to test adversarial paths,
  malformed and oversized successful responses, interruption, preservation of
  previous output, provenance, idempotency, and explicit replacement.
- Validate media with a format-specific hook before publishing. Do not infer
  validity from status code, suffix, or content type alone.
- Keep staging on the destination filesystem and separate generation from the
  final replacement step.
- Test failures between each publication step, not only before the first write.
- Discover mutable vendor models and voices from primary APIs; do not canonize
  account-specific inventory in an operating guide.
- Pair source-level contracts with strict-CSP, accessibility, error-state, and
  responsive browser coverage whenever a route emits UI.
- Search sibling active routes after confirming the root cause, then record
  separate investigations rather than widening one fix without evidence.

## Related Issues

- [Keep Behavioral Documentation Synchronized with Executable Contracts](behavioral-documentation-needs-executable-contracts.md)
- [Validated Filesystem Objects Must Stay Pinned Through Publication](validated-filesystem-objects-must-stay-pinned.md)
- [Pronunciation media investigation](../../investigations/2026-07-17-pronunciation-media-route-safety-and-verification.md)
- [Remediation PR #36](https://github.com/yaniv256/dmccreary-claude-skills/pull/36)
