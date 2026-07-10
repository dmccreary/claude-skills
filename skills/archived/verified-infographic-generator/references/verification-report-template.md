# Verification Report — `<slug>`

**Date:** YYYY-MM-DD
**Poster topic:** <one-line description>
**Claim Plan:** [01-claim-plan.yaml](01-claim-plan.yaml)

This report is the user checkpoint artifact. It shows every claim from the
Claim Plan, what the web search turned up, and how each claim was classified.
**No layout or image generation happens until the user approves this report.**

## Summary

| Metric | Count |
|---|---|
| Claims planned | N |
| VERIFIED (exact number supported) | N |
| DIRECTIONAL (range or best-available study) | N |
| QUALITATIVE-ONLY (descriptor word, no fake %) | N |
| REJECTED (removed or replaced) | N |

**Abort threshold check:** If rejected claims > 20% of planned claims, halt
and reshape the poster with the user.

## Claim-by-Claim Results

### claim_id: `example_claim_1`

- **Subject:** well-being in biophilic offices
- **Classification:** VERIFIED
- **Final value:** +15%
- **Final phrasing:** "Self-reported well-being increase"
- **Source:** Human Spaces / Interface (2015)
- **Authors:** Cooper, C. et al.
- **URL:** https://www.interface.com/...
- **Quoted passage:** "employees who work in environments with natural elements report a 15% higher level of well-being"
- **Search queries used:**
  - `"Human Spaces Global Report 2015 biophilic design productivity well-being"`
  - `"Interface 2015 biophilic office survey 7600 workers"`

### claim_id: `example_claim_2`

- **Subject:** cortisol response in natural environments
- **Classification:** QUALITATIVE-ONLY
- **Final value:** "Significant reduction" (no percentage)
- **Final phrasing:** "Nature exposure reduces cortisol (Antonelli et al., 2019 meta-analysis)"
- **Source:** Antonelli, Barbieri & Donelli (2019). *International Journal of Biometeorology.*
- **URL:** https://pubmed.ncbi.nlm.nih.gov/31001682/
- **Quoted passage:** "Forest bathing can significantly influence cortisol levels on a short term in such a way as to reduce stress."
- **Why not quantified:** Meta-analysis reports significant effect sizes but no single clean percentage appropriate for a hero number.

### claim_id: `example_claim_3`

- **Subject:** hypothetical symmetry-bias claim for the comparison side
- **Classification:** REJECTED
- **Reason:** No peer-reviewed source locates this specific number. Appears only in marketing pages with no traceable primary paper.
- **Action:** Remove from layout, or replace with a QUALITATIVE-ONLY descriptor drawn from a related verified study.

## Fabrication Risks Detected

List any patterns that suggested numbers were being invented, e.g.:

- **Symmetry bias.** The right-hand side of the versus comparison has only 2
  VERIFIED claims to the left's 5. Planned layout will be asymmetric; no
  filler statistics will be invented.
- **Meta-source attribution.** User-suggested citation to Browning et al.
  (2014) demoted — it is a review, not the primary source for any specific
  percentage.
- **Geographic misattribution.** User suggested "Finnish studies" for
  cortisol research; replaced with correctly attributed Japanese
  Shinrin-yoku literature.

## Recommended Final Claim Set

A cleaned list, in the order they should appear on the poster, ready to
hand off to the Layout Spec (Phase 5):

1. `claim_id: example_claim_1` — VERIFIED — +15%
2. `claim_id: example_claim_2` — QUALITATIVE-ONLY — "Significant reduction"
3. *(example_claim_3 dropped)*

## User Checkpoint

**Approval required before proceeding to layout and rendering.**

User options:

- [ ] Approve this claim set as-is
- [ ] Request additional sources for: `<claim_id>`
- [ ] Reshape poster: `<describe>`
- [ ] Accept qualitative language in place of missing percentages
