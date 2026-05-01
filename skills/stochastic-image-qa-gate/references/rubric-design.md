# Rubric Design

How to choose what the gate evaluates, how to bucket items by severity, and how to defend against false positives. Read this when designing a new gate's rubric for an agent.

## The two-bucket model

Every rubric item is either KILL-class or SOFT-class.

**KILL-class** — failure makes the output unshippable. Cost of shipping it is high (broken brand, customer confusion, refund). Cost of false positive is moderate (one wasted generation, recoverable via admin override). Bucket in only when both:
- The failure mode is unambiguous from the image alone
- A SOFT outcome would still embarrass the brand

**SOFT-class** — failure degrades but doesn't break the output. Reads as "ship-with-flag-for-review" rather than "discard". Soft items also serve as data: tracking soft-rate over time tells you which dimensions of the brand spec are drifting.

A typical gate has 2–3 KILL items and 1–3 SOFT items. More than 6 total and the rubric becomes hard for the model to evaluate consistently.

## Item catalog

These are the rubric items that have proven useful. Pick from this menu, don't invent new ones unless you have a clear reason — the more standardized the rubric, the easier it is for the model to evaluate.

### Text correctness (almost always KILL)

| Item | What it checks | Severity |
|---|---|---|
| `letterPerfect` | Rendered text matches expected text letter-for-letter | KILL (with Levenshtein softening — see below) |
| `noDuplicates` | No word from the source appears more than once on the sticker | KILL |
| `noExtraText` | No additional words/text beyond the brief + brandmark | SOFT |

### Color / palette (mix)

| Item | What it checks | Severity |
|---|---|---|
| `paletteCore<Color>` | Required brand color appears in the right element (e.g. focal word is lime green) | KILL |
| `paletteClean` | No off-brand colors leaked into the design | SOFT |
| `backgroundCorrect` | Background is the specified color | SOFT |

### Brand presence (mostly SOFT)

| Item | What it checks | Severity |
|---|---|---|
| `brandmarkPresent` | The brand wordmark/logo is visible | SOFT |
| `brandmarkPosition` | Brandmark in the specified corner/zone | SOFT |
| `brandmarkLegible` | Brandmark text is readable, not blurred | SOFT |

### Composition (almost always SOFT)

| Item | What it checks | Severity |
|---|---|---|
| `singleSubject` | Only one sticker/subject in the image | KILL |
| `subjectCentered` | Composition is balanced, not cramped to one edge | SOFT |
| `dieCutShape` | Shape matches spec (blob, circle, rectangle, etc.) | SOFT |

### Domain-specific (varies)

| Item | What it checks | Severity |
|---|---|---|
| `noHumanFigures` | If the brief forbids human figures | KILL |
| `noPhotoRealism` | If the brief specifies vector/illustrated style | SOFT |
| `periodAccurate` | (For period-artifact agents) Visual register matches the named era | SOFT |

## False-positive defenses

The biggest risk with a QA gate is killing perfectly good output because the model misjudges. Three defenses:

### 1. Levenshtein softening on text

Cursive script with thin upstrokes and ligatures fools OCR. The model genuinely cannot reliably read its own rendering — it might say "Curiosity" was rendered as "Curiosify" because the script 't' threw it off. The sticker is fine; the OCR isn't.

Defense: when `letterPerfect.passes === false`, compute Levenshtein distance between `renderedText` (model's OCR output) and `expectedText`. Normalize first (lowercase, strip punctuation, collapse whitespace).

| Distance | Action |
|---|---|
| 0 | Pass (shouldn't happen if model said fail, but guard anyway) |
| 1–2 | Downgrade to SOFT (likely OCR confusion, sticker probably fine) |
| 3+ | KILL (real text rendering miss like "leariyned" vs "learned") |

The threshold of 2 was chosen because:
- "Curiosify" vs "Curiosity" = 1 (one letter swap, OCR error)
- "We're" vs "Were" = 2 (apostrophe difference, normalize handles this so distance = 0 actually)
- "Leariyned" vs "Learned" = 3 (two extra letters, real model error)

### 2. Hue tolerance for palette checks

A single rendered word's color isn't always pure #D0E156. Anti-aliasing pixels at letter edges, JPEG-style compression artifacts, or the model's slight palette drift can make even a correct lime green read as "almost lime, leans yellow". The model might call this fail.

Defense: phrase palette items in the rubric prompt with explicit tolerance: "lime green close to #D0E156 — accept any clearly green-yellow color, only fail if the word is white/blue/teal/red/etc."

If palette miss-rate is high after going live, look at the rejected images. If they're all "actually fine, just slightly off-hue", soften further or downgrade the item to SOFT.

### 3. Composition tolerance

Pixel-level "is this centered" checks are brittle. The model can disagree about what "centered" means. Avoid composition items as KILL-class unless the failure mode is dramatic (sticker cropped off-canvas, second subject in frame). Prefer "looks reasonable" framings over "is geometrically perfect".

## Severity computation rule

Compute severity in code from the rubric JSON. Never let the model return `severity` directly — models are inconsistent at "is this a kill or soft?" because the question requires holding multiple rubric items in mind at once. Models are good at per-item booleans; rollup logic is your code's job.

```js
let severity = 'pass';
const failures = [];

// Apply KILL items first
if (!rubric.letterPerfect?.passes) {
  // ... with Levenshtein softening
}
if (!rubric.noDuplicates?.passes) { failures.push(...); severity = 'kill'; }
if (!rubric.paletteCoreLime?.passes) { failures.push(...); severity = 'kill'; }

// Apply SOFT items (only escalate from pass to soft, never override kill)
if (!rubric.brandmarkPresent?.passes) {
  failures.push(...);
  if (severity === 'pass') severity = 'soft';
}
if (!rubric.paletteClean?.passes) {
  failures.push(...);
  if (severity === 'pass') severity = 'soft';
}

return { passes: severity === 'pass', severity, failures, raw: rubric };
```

## Tuning after deployment

After 10–20 production runs with the gate live:

**If KILL rate is ≥ 30%:** the gate is too strict OR the underlying model is too unreliable. Look at the inactive products. If most are real misses, the model's the problem (consider better prompting upstream). If most are false positives, soften the rubric.

**If KILL rate is 0%:** the gate may be too lenient. Manually inspect random successes. If you find quality issues that the gate let through, sharpen the rubric.

**If SOFT rate is ≥ 50%:** brand spec drift, or item is too sensitive. Check whether the SOFT items are pulling their weight or just generating noise. Drop items that always fire SOFT regardless of actual quality.

A healthy gate after tuning:
- KILL: 5–15% (real misses)
- SOFT: 10–30% (degraded but readable, flagged for review)
- PASS: 60–80% (ship-as-active)

## Don't over-engineer the rubric

The temptation is to add more items to catch more failure modes. Resist past 6 items — the model's per-item accuracy drops when the rubric gets long. Better to have 4 sharp items the model evaluates well than 10 mushy items it averages out.

If a new failure mode appears in production, first ask: is it caught by an existing item if I sharpen the prompt? Only add a new item when no existing one covers it.
