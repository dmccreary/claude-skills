# Image Prompt Template — Phase 6 Output

> Sibling template: for **interactive diagram overlays** (annotation-free scientific
> illustrations that get callout markers from diagram.js), use the microsim-generator
> skill's `$HOME/.claude/skills/microsim-generator/references/overlay-image-prompt.md` instead. Both share the core rule:
> **no text, labels, arrows, or annotation marks baked into the generated image.**

This is the **locked** prompt sent to the text-to-image model. Every text
element in this prompt was copied verbatim from the approved Layout Spec
(Phase 5). No numbers, author names, years, or institution names should
differ from what is in `03-layout-spec.yaml`.

## Prompt Structure

```
A clean, modern horizontal infographic poster, {DIMENSIONS}, with a
sophisticated editorial design style. {BACKGROUND_DESCRIPTION}.

CRITICAL RENDERING INSTRUCTIONS — READ BEFORE DRAWING:

Render the following exact text verbatim. Do not substitute any numbers,
paraphrase any labels, change any author names, invent any additional
statistics, rows, columns, or citations. All percentages, author names,
years, and institution names must appear EXACTLY as written below. If
you cannot render a text element legibly at the requested size, leave
it out rather than approximating — do not invent a shorter version.

Do not add decorative statistics, placeholder percentages, or "example"
numbers to fill empty space. Asymmetric column content is intentional
and correct.

HEADER:
{MAIN_TITLE}
{SUBTITLE}

LAYOUT:
{DESCRIBE TWO-COLUMN OR OTHER LAYOUT}

TOP IMAGES (if applicable):
- LEFT: {PHOTOREALISTIC DESCRIPTION A}
- RIGHT: {PHOTOREALISTIC DESCRIPTION B}

LEFT COLUMN METRIC ROWS:
{FOR EACH factual element with column: left — copy verbatim:}
Row N — {ICON} icon
  "{LABEL}"
  "{DESCRIPTOR}"
  Bar: {bar_fill_pct}% filled  |  "{VALUE}"

RIGHT COLUMN METRIC ROWS:
{FOR EACH factual element with column: right — copy verbatim:}
Row N — {ICON} icon
  "{LABEL}"
  "{DESCRIPTOR}"
  Bar: {bar_fill_pct}% filled  |  "{VALUE}"

FOOTER (small, centered, verbatim citation list):
{ASSEMBLED FROM sources_rendered_from — one citation per source,
 comma-separated, split across two lines if needed}

STYLE NOTES:
- Typography: {heading_font} / {body_font}
- Palette: {palette.primary}, {palette.accent}, {palette.neutral}, {palette.text}
- Icons: flat filled circles, consistent stroke weight
- Bar charts: rounded caps, 20px tall
- Ample white space, airy editorial feel
- No emojis, no decorative flourishes beyond what is specified
- All text must render as legible, properly-spelled characters — no
  garbled pseudo-text, no made-up Greek letters, no lorem-ipsum
```

## Worked Example

Below is an example prompt assembled from a Layout Spec. Notice every
number and author name traces directly to the `03-layout-spec.yaml`:

```
A clean, modern horizontal infographic poster, 1200x680 pixels, with a
sophisticated editorial design style. White background with a subtle
light-green border frame.

CRITICAL RENDERING INSTRUCTIONS — READ BEFORE DRAWING:

Render the following exact text verbatim. Do not substitute any numbers,
paraphrase any labels, change any author names, invent any additional
statistics, rows, columns, or citations. Asymmetric column content is
intentional — the right column has fewer rows than the left, by design.

HEADER (centered, forest-green bold, 32pt):
"THE EVIDENCE: BIOPHILIC SPACES IMPROVE WELL-BEING AT WORK"

SUBTITLE (muted gray italic, 14pt, centered):
"A review of peer-reviewed findings on nature-inclusive workplace design"

TWO-COLUMN COMPARISON:
- Left column labeled "BIOPHILIC SPACES" in a rounded green pill tab.
- Right column labeled "CONVENTIONAL INDOOR SPACES" in a rounded gray
  pill tab. A dark-green circle between reads "VS."

LEFT COLUMN (3 metric rows, mint-green rounded card):
Row 1 — smiley icon
  "Well-being"
  "Self-reported increase (Human Spaces, 2015)"
  Bar: 75% filled  |  "+15%"

Row 2 — leaf icon
  "Stress Reduction"
  "Cortisol reduction with nature exposure (Antonelli et al., 2019)"
  Bar: 60% filled  |  "Significant"

Row 3 — heart icon
  "Surgical Recovery"
  "Shorter hospital stay, fewer analgesics (Ulrich, 1984)"
  Bar: 55% filled  |  "-8.5% days"

RIGHT COLUMN (2 metric rows, light-gray rounded card — asymmetric
by design):
Row 1 — shield icon
  "Sick Leave"
  "More sick days with limited daylight access (UK GBC, 2016)"
  Bar: 40% filled  |  "+18% days"

Row 2 — brain icon
  "Attention Restoration"
  "Reduced without nature exposure (Kaplan, 1995)"
  Bar: 35% filled  |  "Reduced"

FOOTER (centered, small dark-green, two lines):
Line 1: "Sources: Cooper, C. et al. (2015), Human Spaces / Interface;
Antonelli, Barbieri & Donelli (2019), Int. J. Biometeorology;
Ulrich, R. (1984), Science 224."
Line 2: "UK Green Building Council (2016); Kaplan, S. (1995),
Attention Restoration Theory."

STYLE NOTES:
- Typography: Inter Bold / Inter Regular
- Palette: #2E5E3E (forest green), #E8F3EC (mint), #6B6B6B (warm gray)
- Icons: flat filled circles
- Bar charts: rounded caps, 20px tall
- Ample white space, airy editorial feel
- No emojis, no decorative flourishes
- All percentages and citations must render as legible, correctly spelled text
```

## After Rendering

Save the rendered image to `docs/posters/<slug>/poster.png` and proceed to
Phase 8 (post-render audit) to verify that every number, year, and author
name in the pixels matches this prompt.
