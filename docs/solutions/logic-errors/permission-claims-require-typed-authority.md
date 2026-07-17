---
title: Permission Claims Require Typed Publication Authority
date: 2026-07-17
category: logic-errors
module: book-publisher
problem_type: logic_error
component: tooling
symptoms:
  - A generated README can grant rights that no repository source grants
  - Missing or conflicting license evidence is converted into a convenient default
  - Presentation validation reports success while semantic authority is absent
root_cause: missing_validation
resolution_type: code_fix
severity: critical
tags: [license-authority, publication-contract, fail-closed, readme, validation]
---

# Permission Claims Require Typed Publication Authority

## Problem

A content generator can publish a polished but unauthorized permission claim
when it treats license text as ordinary copy. Repository absence, scoped terms,
conflicting files, custom terms, and explicit owner authorization are materially
different states; collapsing them into prose pressures the generator to choose
terms it has no authority to choose.

## Symptoms

- A missing root license becomes a default Creative Commons or software license.
- A documentation-only license is presented as repository-wide permission.
- Multiple or custom license files are reduced to one familiar label.
- A validator rewards the presence of a badge or heading without checking the
  evidence that authorizes the claim.
- Archived guidance or validators can restore the unsafe behavior after the
  active route is fixed.

The complete causal record is in
[the README license-authority investigation](../../investigations/2026-07-17-readme-route-license-authority.md).

## What Didn't Work

- **Using a convenient default.** A common license is still an affirmative grant
  and cannot be selected by a generator.
- **Treating metadata as authority.** Copyright display text, package metadata,
  public repository visibility, and an author's usual preference do not by
  themselves establish repository-wide permission.
- **Checking presentation instead of provenance.** A valid badge URL, a License
  heading, or a high README score says nothing about whether the claim is
  authorized.
- **Encoding failure states only in prose.** Agents cannot reliably fail closed
  when absence, ambiguity, scope, and authorization have no machine-readable
  representation.

## Solution

Put a deterministic authority boundary in front of generation and validation:

1. Inspect repository-root evidence without modifying it.
2. Represent the result as typed states such as `absent`, `scoped`,
   `single-evidence`, `nonstandard-or-unresolved`, `ambiguous`, and
   `explicitly-authorized`.
3. Permit a named claim only when one known source supports it or the owner
   explicitly authorizes that exact value for the repository.
4. For custom or unresolved terms, permit only neutral wording linked to the
   exact evidence file.
5. Reject badges, headings, and affirmative prose claims when authority is
   absent, scoped, ambiguous, or mismatched.
6. Keep the inspector offline and read-only. Unknown terms remain unresolved;
   the tool does not render a legal opinion or create license files.
7. Route archived executable validators through the active implementation so
   the authority contract has one source of truth.

The implementation is defined by:

- `skills/book-publisher/scripts/license_authority.py`
- `skills/book-publisher/scripts/validate-readme.py`
- `skills/book-publisher/tests/test_license_authority.py`
- `skills/book-publisher/references/readme-guide.md`

## Why This Works

The generator no longer receives “pick a license” as an implicit fallback. It
receives an evidence state with a bounded set of allowed outputs. The validator
then checks the semantic claim against that same state and fails the operation
when the claim exceeds its authority, independently of the README's style or
quality score.

Exact evidence links preserve provenance without pretending that arbitrary
custom text has been legally classified. Rejecting symlink evidence and keeping
inspection offline also prevents repository authority from silently depending
on content outside the reviewed tree or on mutable network responses.

## Prevention

- Treat legal, privacy, security, accessibility, and compliance statements as
  consequential publication claims, not template copy.
- Give each claim type a typed evidence and authorization contract before a
  generator can emit it.
- Include negative fixtures for absent, scoped, conflicting, compound, custom,
  and mismatched evidence, plus explicit-authorization tests.
- Make semantic authority failures hard failures; never hide them inside a
  weighted presentation score.
- Scan active guides, archived sources, prompts, packaged copies, and sibling
  publication routes after finding an invented default.
- Preserve complexity when evidence is unresolved. Reporting uncertainty is
  safer than manufacturing a simple answer.

## Related Issues

- [Keep Behavioral Documentation Synchronized with Executable Contracts](behavioral-documentation-needs-executable-contracts.md)
- [Active Media Routes Require Publication Contracts](active-media-routes-require-publication-contracts.md)
- [README license-authority investigation](../../investigations/2026-07-17-readme-route-license-authority.md)
