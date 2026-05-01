# Visual Prompt Design

How to write the structured-block image prompt that the agent sends to NB2 (or another image model). This is where the brand's visual identity gets encoded.

## Three NB2 prompting principles (load-bearing)

These are validated patterns from the shilpiworks codebase. Don't deviate without a reason.

### 1. Structured-block format beats paragraphs

NB2 follows named blocks (`STICKER`, `ERA`, `TEXT`, `TYPOGRAPHY`, `PALETTE`, `ICONS`, `COMPOSITION`, `TONE`, `NEGATIVES`) much more reliably than a single prose paragraph. The Stoic agent's redesign in shilpiworks used this format and produced 6-of-6 museum-quality artifacts on first try after a one-paragraph version had failed.

### 2. Lead with positive instructions, not negations

Models latch onto positive concepts (`HAND-WRITTEN PRINT`, `kindergarten-workbook style`, `print handwriting`) much more strongly than suppressed attractors (`no cursive, no script, no italic loops`). When a negation matters (no metallic gold, no neon, no chiseled-pillar shape), put it in a `NEGATIVES:` block at the END and call out the *specific* failure mode you've seen.

### 3. Move critical rules to the front

NB2 weighs leading instructions more heavily than trailing ones. If something must land — letter-perfect typography, "the artifact IS the silhouette", brand palette purity — make it the FIRST block, not buried mid-prompt.

## The canonical block order

```
STICKER       — the most non-negotiable concept (lead with this)
ERA / TONE    — the era / aesthetic register
TEXT          — what to render, letter-perfect
TYPOGRAPHY    — how the text is set (caps + script split, fonts, sizes)
PALETTE       — strict color spec
ICONS         — accent vocabulary + placement rules
COMPOSITION   — die-cut shape, balance, brandmark zone
NEGATIVES     — specific failure modes to avoid (last)
```

## Lorignite worked example (paraphrased)

Use this as a structural template, not a copy target.

```
STICKER (the sticker IS this object — read this first):
A modern typographic poster sticker. The shape is an irregular die-cut blob.
The sticker fill is deep navy, with bold sans-serif white capitals and one
flowing lime-green handwritten script word. A small "Lorignite" wordmark
with a tiny torch icon sits in a clear bottom-right inset zone.

ERA: Contemporary 2025 designer poster-sticker style. Vector-clean.
Optimistic, encouraging, smart-friend tone — never corporate, never
tech-bro, never childish.

TEXT TO RENDER (letter-perfect, every letter spelled correctly):
The phrase: "[QUOTE]"
The brandmark: "Lorignite"
Nothing else. No URLs, no hashtags, no extra words.

TYPOGRAPHY — YOU DECIDE THE FOCAL WORD:
  • Choose EXACTLY ONE word from the phrase to be the FOCAL element.
    Pick the most emotionally resonant or compositionally interesting word —
    typically the punch noun, the vivid verb, or the surprise/action word.
  • The FOCAL word is rendered in HANDWRITTEN FLOWING SCRIPT in lime green
    #D0E156 — elegant pointed cursive (Allura / Great Vibes / Magnolia
    Script style).
  • EVERY OTHER word is rendered in BOLD SANS-SERIF ALL-CAPS in soft white
    #F7F7F7.
  • CRITICAL: the focal word is rendered EXACTLY ONCE — never as both caps
    AND script.

PALETTE (strict — no other colors except those listed):
  • Sticker fill: navy #121B31
  • Sans-serif caps: soft white #F7F7F7
  • Handwritten script: lime green #D0E156
  • Sticker contour border: soft white #F7F7F7
  • Background OUTSIDE the sticker: pure white RGB(255,255,255)

ICONS:
[ICON_PLACEMENT description from icon vocabulary]
Icon style: flat vector, lime-green and white only — never blue glass,
never teal lens, never colored fills outside the brand palette. Small
(~10–15% of sticker area). Decorative accent, not focal.

COMPOSITION:
Centered overall. The die-cut blob silhouette traces snugly around the
text + icon. Brandmark in bounded inset zone bottom-right. ONE sticker
only on a pure white empty background.

TONE: A polished designer-made poster sticker handed out at an AI
workshop run by a warm, curious teacher.

NEGATIVES (specific failure modes seen in earlier attempts — avoid each):
  • The focal word appearing TWICE — once in caps and once in script
  • Any word from the phrase rendered more than once
  • Script word coming out white instead of lime green
  • Icons placed BETWEEN words or on top of letterforms
  • Brandmark overlapping or touching main body text
  • Rounded brush-script font (must be elegant pointed cursive)
  • More than one sticker in the image
  • Generic rectangular or oval sticker shape
  • Blue glass / teal lens on a magnifying-glass icon
```

## Per-brand customization checklist

When writing the prompt for a new brand, fill in:

- [ ] STICKER block: one-paragraph description of the brand's signature look
- [ ] ERA block: the visual era / register (modern poster, period artifact, retro, illustrated, etc.)
- [ ] TYPOGRAPHY: how to split text styles (single style? caps + script? all caps? mixed sizes?)
  - Specify fonts by name + style (e.g. "Work Sans Black", "Allura pointed cursive")
- [ ] PALETTE: hex codes with role assignments (which color goes where)
- [ ] ICONS: the brand's icon vocabulary + placement rules
- [ ] COMPOSITION: die-cut shape spec (blob, circle, rectangle, irregular silhouette of the subject)
- [ ] TONE: 1–2 sentences on the emotional register
- [ ] NEGATIVES: at least 3 specific failure modes (these get added to over time as production reveals new ones)

## Don't pre-decompose the text

This was the Lorignite mistake — early versions used a separate Gemini Flash decomposer step that decided which word in each quote became the focal script word, then passed `capsLines` and `scriptWord` arrays into the image prompt. NB2 dutifully rendered exactly what the decomposer said.

The decomposer occasionally put the same word in BOTH `capsLines` and `scriptWord`. NB2 then rendered the word twice. Catastrophic for a brand sticker.

The fix: tell NB2 to pick the focal word itself, with explicit "render exactly once" guards. NB2 has visual judgment the decomposer doesn't. The TYPOGRAPHY block above does this. Don't reintroduce a decomposer.

## Iterating on the prompt

When a batch produces consistently weird outputs:

1. Look at 5–10 failures, identify the pattern (e.g. icons keep crashing into letterforms)
2. Add the failure mode to NEGATIVES with specific language
3. If a positive pattern would help (e.g. icons go at OUTER EDGES of the text block), add that to TYPOGRAPHY or COMPOSITION
4. Run another batch
5. Repeat

Don't try to fix multiple failure modes at once — change one block, run, observe. Otherwise you can't tell which change helped.

The Lorignite prompt went through v1 → v2 → v3 → v4, each iteration tightening based on observed misses. The v4 (no decomposer, NB2 picks focal) is the current production form.
