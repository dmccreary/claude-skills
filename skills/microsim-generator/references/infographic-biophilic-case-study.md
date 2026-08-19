# Case Study: Biophilic vs. Brutalist Spaces Poster

This worked example shows how the verified-infographic workflow
would have prevented the 10 fact errors found in a real one-shot-generated
poster.

## The Original One-Shot Poster

A side-by-side infographic titled **"THE EVIDENCE: PEOPLE ARE HAPPIER &
HEALTHIER IN BIOPHILIC SPACES"** was generated from a single text-to-image
prompt. It contained the following claims:

**Biophilic side:** +15% happiness, -23% stress cortisol, +12% cognitive
performance, +26% health/recovery, +8–15% productivity.

**Brutalist side:** -10% happiness, +15% stress, -9% cognition, -20%
health, -7–12% productivity.

**Cited sources:** Browning et al. (2014); Human Spaces / Terrapin
(2015–2023); University of Exeter; Singapore NUS; Finnish studies.

## Fact-Check Results

**80% of numeric claims were unsupported.** Specifically:

| # | Claim | Problem |
|---|---|---|
| 1 | -23% cortisol | No primary source; round-trip marketing stat |
| 2 | +12% cognitive | Misattributed — 12% is a greenery *dose*, not a cognitive uplift |
| 3 | +26% recovery | No study produces this number; Ulrich 1984 showed ~8.5% |
| 4 | -10% happiness (brutalist) | Fabricated mirror-statistic |
| 5 | +15% stress (brutalist) | Fabricated mirror-statistic |
| 6 | -9% cognition (brutalist) | Fabricated mirror-statistic |
| 7 | -20% health (brutalist) | Fabricated mirror-statistic |
| 8 | -7–12% productivity (brutalist) | Fabricated mirror-statistic |
| 9 | "Finnish studies" | Misattributed — research is Japanese |
| 10 | Browning 2014 as empirical source | Category error — it's a meta-synthesis |

Only **+15% well-being** and **+8–15% productivity** were supportable.

## How the Skill Would Have Prevented Each Error

### Phase 1 (Claim Planning) catches symmetry bias

The "versus brutalist" structure triggers the symmetry_warning flag. Claude
would tell the user up front: *"The brutalist side may end up with almost
no verified data. We will not invent mirror-statistics. Are you OK with an
asymmetric layout, or would you like to reshape this as a single-subject
biophilic-benefits poster?"*

This one question alone would have prevented errors #4–#8.

### Phase 2 (Source Discovery) catches round-trip marketing stats

For the "-23% cortisol" claim, Claude runs multiple searches and finds:

- Antonelli et al. (2019) meta-analysis: *significant* cortisol reduction
  but no clean -23%
- "Human Spaces" marketing pages cite the number with no primary source
- No peer-reviewed paper produces this exact figure for indoor biophilic
  design

Claim is classified as **QUALITATIVE-ONLY** — descriptor "Significant" is
used instead of a fake percentage. Error #1 prevented.

Same process catches error #2: Claude notices that "12%" in the literature
refers to an optimal greenery coverage ratio (Lei et al. 2021), not a
cognitive uplift. The actual effect is 14% short-term memory improvement
(Yin et al. 2019) — the number gets corrected, with a proper citation.

### Phase 3 (Verification) catches the Browning meta-source error

When Claude attempts to verify a specific percentage against the Browning
2014 paper, it finds the paper is a synthesis of 500+ other studies, not
an originator of the percentage. The citation is demoted — Browning can
appear in a general reading list but cannot be cited as the source of a
specific number. Error #10 prevented.

### Phase 3 (Verification) catches geographic misattribution

Claude searches for "Finnish biophilic cortisol studies" and finds the
cortisol-reduction literature is overwhelmingly Japanese (Shinrin-yoku,
Miyazaki, Park, Li). The citation is corrected. Error #9 prevented.

### Phase 4 (User Checkpoint) catches anything the automated phases missed

The Verification Report would show the user:

- Biophilic side: 3 VERIFIED / DIRECTIONAL claims, 2 QUALITATIVE
- Brutalist side: 1 VERIFIED claim (sick days), 1 QUALITATIVE (attention
  restoration), 3 REJECTED

The **rejection rate on the brutalist side is 60%**, far above the 20%
abort threshold. Claude halts and proposes reshaping the poster.

The user has three good options:

1. Drop the comparison, make it a single-subject poster.
2. Keep the comparison but render asymmetric (3 vs. 2 rows).
3. Substitute a different comparison subject that actually has data
   (e.g., "windowless offices" instead of "brutalist spaces").

All three produce honest posters. None require fabrication.

### Phase 8 (Post-Render Audit) catches image-model drift

Even with a locked prompt, image models sometimes render "+15%" as "+51%"
or misspell author names. The Phase 8 audit reads the rendered image
multimodally and flags any mismatch between pixels and spec. Up to 3
regeneration attempts are allowed; beyond that, the user is alerted.

## Final Poster Content (What Gets Published)

Based on the verified evidence, the final poster would contain:

**Title:** "Biophilic Spaces Improve Well-Being at Work"

**Verified claims (left column, 5 rows):**

1. Well-being: +15% (Human Spaces, 2015)
2. Stress reduction: "Significant" (Antonelli et al., 2019 meta-analysis)
3. Short-term memory: +14% (Yin et al., 2019)
4. Surgical recovery: -8.5% days (Ulrich, 1984)
5. Creativity & productivity: +6% to +15% (Human Spaces, 2015; Exeter, 2014)

**Conventional-space claims (right column, 2 rows — asymmetric):**

1. Sick leave: +18% days with limited daylight (UK GBC, 2016)
2. Attention restoration: "Reduced" (Kaplan, 1995)

**Sidecar source file `sources.md`** contains full citations with URLs
and quoted passages, so any reader can verify every number.

## Error Count: Before vs. After

| Approach | Numeric claims | Fabricated / misattributed | Error rate |
|---|---|---|---|
| One-shot text-to-image | 10 | 8 | 80% |
| verified-infographic-generator | 7 | 0 | 0% |

The verified-infographic skill produces a slightly smaller poster (fewer
rows, because empty rows are not invented to fill space) but every claim
is defensible, every citation is real, and the poster has a reader-facing
sidecar so any fact can be checked in seconds.
