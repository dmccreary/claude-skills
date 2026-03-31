---
name: interactive-infographic-overlay
description: This skill generates a complete interactive diagram MicroSim directory with a text-to-image prompt, data.json overlay file, main.html, index.md, and mkdocs.yml integration. Use this skill when an intelligent textbook chapter specifies a diagram overlay MicroSim that needs a scientific illustration with interactive callout labels, explore/quiz modes, and an edit mode for calibrating marker positions. The skill produces annotation-free image prompts and data.json files compatible with the shared diagram.js library.
---
# Interactive Infographic Overlay Generator

**Version:** 1.0

## Overview

This skill generates a complete MicroSim directory for interactive diagram overlays used in intelligent textbooks. It produces all files needed for a diagram where:

1. A text-to-image LLM generates an annotation-free scientific illustration
2. The `diagram.js` shared library renders interactive numbered markers, leader lines, and labels over the image
3. Students can explore (hover for info), take quizzes (identify structures), and instructors can edit marker positions

## When to Use This Skill

Use this skill when:

- A chapter content spec includes a `#### Diagram:` details block with type "Interactive Infographic" or "Diagram" that requires a scientific illustration with labeled callouts
- The textbook needs a labeled anatomy diagram, structural diagram, process diagram, or any image with identified regions
- The specification calls for explore mode (hover to learn), quiz mode (identify structures), or both

Do NOT use this skill when:

- The diagram is better served by Mermaid, Chart.js, or p5.js drawing (no background image needed)
- The content is a pure simulation with dynamic elements (use microsim-generator instead)
- The diagram needs only simple inline markdown images with no interactivity

## Prerequisites

The project must have the shared diagram library installed:

```
docs/sims/shared-libs/
├── diagram.js    (interactive overlay engine)
└── style.css     (shared styles for all diagram MicroSims)
```

If `shared-libs/` does not exist, install it from this skill's bundled assets:

```bash
mkdir -p docs/sims/shared-libs
cp ~/.claude/skills/interactive-infographic-overlay/assets/shared-libs/diagram.js docs/sims/shared-libs/
cp ~/.claude/skills/interactive-infographic-overlay/assets/shared-libs/style.css docs/sims/shared-libs/
```

Always check that the project's copy is up to date with the skill's bundled version before creating new diagram MicroSims.

## Workflow

### Step 1: Gather Diagram Requirements

Extract from the chapter content specification or user request:

1. **Subject** — What the diagram depicts (e.g., "animal cell cross-section," "moss sporophyte anatomy," "mossarium layers")
2. **Structures to label** — List of 5-15 structures/regions with:
   - Name/label
   - Brief description (1-2 sentences)
   - Approximate position in the image
   - Suggested color for the marker
3. **Image style** — Scientific illustration style (flat, watercolor, realistic, etc.)
4. **Image dimensions** — Typically 1200×900 (landscape 4:3) or 900×1200 (portrait 3:4)
5. **Layout** — `side-panel` (default, labels on right), `top-bottom`, or `dual-panel`
6. **Context tips** — Optional exam tips, hints, or additional info per structure

### Step 2: Create the MicroSim Directory

Create the directory under `docs/sims/`:

```bash
mkdir -p docs/sims/{sim-id}
```

Where `{sim-id}` is a kebab-case name (e.g., `moss-sporophyte`, `mossarium-layers`, `animal-cell`).

### Step 3: Generate image-prompt.md

Create `docs/sims/{sim-id}/image-prompt.md` with a detailed prompt for the text-to-image LLM. Use the template in `references/image-prompt-template.md`.

**Critical rules for all image prompts:**

1. **NO TEXT IN THE IMAGE** — The image must contain absolutely no text, labels, arrows, callout lines, numbers, or annotation marks of any kind. All labeling is handled by diagram.js.
2. Specify exact dimensions, background color, and art style
3. Describe each structure with precise position, color, shape, and size
4. Use percentage-based positioning (e.g., "centered at 40% from left, 30% from top")
5. Specify the viewing angle (cross-section, top-down, side view, etc.)

### Step 4: Generate data.json

Create `docs/sims/{sim-id}/data.json` with the overlay data. See `references/data-json-schema.md` for the complete schema and field definitions.

**Position guidelines:**

- `x` and `y` are percentages of the image dimensions (0 = left/top, 100 = right/bottom)
- Place markers at the visual center of each structure
- Space markers at least 5-8% apart to avoid overlap
- Use the `?edit=true` URL parameter to calibrate positions after image generation

### Step 5: Generate main.html

Create `docs/sims/{sim-id}/main.html` using the template in `assets/main-template.html`. Replace `{TITLE}`, `{IMAGE_FILENAME}`, and `{ALT_TEXT}` with the actual values.

### Step 6: Generate index.md

Create `docs/sims/{sim-id}/index.md` with documentation and an embedded iframe. Include:

- Title with `hide: toc` frontmatter
- Embedded iframe (`height="640px" width="100%"`)
- Fullscreen link
- Usage instructions for explore, quiz, and edit modes
- Numbered list of all labeled structures

### Step 7: Update mkdocs.yml

Add two entries to `mkdocs.yml`:

1. **Navigation** — Add the MicroSim to the nav section under MicroSims
2. **Exclude image prompt from build** — Add `sims/{sim-id}/image-prompt.md` to the `exclude_docs:` block to prevent mkdocs from rendering it as a page. Create the `exclude_docs:` block if it doesn't exist yet.

### Step 8: Inform the User

Report all files created and provide next steps:

1. Copy image prompt into text-to-image tool
2. Save generated image to the MicroSim directory
3. View at `http://127.0.0.1:8000/{repo}/sims/{sim-id}/main.html`
4. Calibrate positions with `?edit=true`
5. Copy calibrated JSON back into data.json

## Calibration Workflow

After the image is generated and saved, marker positions will likely need adjustment:

1. Open `main.html?edit=true` in the browser
2. Drag each numbered marker to the correct position on the image
3. Click "Copy JSON" to get the calibrated coordinates
4. Replace the `callouts` array in `data.json` with the copied data
5. Reload the page to verify positions

This edit mode is built into diagram.js and requires no additional code.

## Layout Options

| Layout | Description | Best For |
|--------|-------------|----------|
| `side-panel` | Image left (65%), labels right (35%) | Most diagrams — default choice |
| `top-bottom` | Labels above and below image | Wide panoramic images |
| `dual-panel` | Labels left (22%), image center (56%), labels right (22%) | Diagrams with many callouts (12+) |

## Color Palette for Markers

```
#8E44AD  purple    — nucleus, central structures
#E74C3C  red       — energy-related structures
#3498DB  blue      — membrane structures
#2ECC71  green     — photosynthetic structures
#E67E22  orange    — transport structures
#1ABC9C  teal      — storage structures
#F39C12  gold      — signaling structures
#9B59B6  violet    — genetic structures
#34495E  dark gray — structural elements
#16A085  sea green — fluid/matrix regions
```

## Iframe Auto-Resize via postMessage

Diagram overlay MicroSims have responsive content heights that change with
viewport width. Rather than guessing a fixed `height` for the `<iframe>`,
`diagram.js` automatically reports its actual content height to the parent
page via `postMessage`. The parent page's `extra.js` listens for these
messages and adjusts the iframe height dynamically.

### How It Works

1. **Sender (diagram.js)** — After init and on every resize, the
   `reportHeight()` method temporarily populates the infobox with the
   **longest** callout's description + AP tip, measures
   `document.body.scrollHeight + 30px`, then restores the default infobox
   state. This ensures the iframe is sized for the worst-case content height
   from the start — no clipping when users hover over long descriptions.

2. **Receiver (extra.js on parent page)** — A `message` event listener
   matches `event.source` to the correct iframe's `contentWindow` and sets
   `iframe.style.height` to the reported height.

3. **Fallback** — The static `height="NNN"` attribute in the iframe HTML
   remains as a fallback shown while the sim loads. Once the sim renders
   and reports its height, the static value is overridden.

### Requirements

The parent page must include this listener in its JavaScript (already present
in the standard `docs/js/extra.js`):

```javascript
window.addEventListener('message', function (event) {
    if (!event.data || event.data.type !== 'microsim-resize') return;
    var iframes = document.querySelectorAll('iframe');
    for (var i = 0; i < iframes.length; i++) {
        if (iframes[i].contentWindow === event.source) {
            iframes[i].style.height = event.data.height + 'px';
            break;
        }
    }
});
```

If the project's `extra.js` does not have this listener, add it. The
diagram MicroSims will still work without it — they'll just use the static
iframe height as before.

## Controls Placement

The Explore/Quiz `#controls` div must be placed **below** `#layout` and
**above** `#infobox` in `main.html`. This gives the diagram image maximum
vertical space and places mode buttons where users expect them after
viewing the diagram. The `main-template.html` asset already follows this
order.

## Common Pitfalls

- **Text in generated images** — Always verify the image has NO text, labels, or arrows. Regenerate if the LLM adds annotations.
- **Marker overlap** — Keep callout positions at least 5-8% apart. Use edit mode to fine-tune.
- **Missing shared-libs** — Verify `docs/sims/shared-libs/diagram.js` and `style.css` exist before testing.
- **Forgetting exclude_docs** — The `image-prompt.md` file will cause mkdocs build warnings if not excluded.
- **Wrong image path** — The `image` field in data.json must match the exact filename (case-sensitive).

## Resources

### references/

- `data-json-schema.md` — Complete data.json schema with field definitions and examples
- `image-prompt-template.md` — Template for generating image prompts

### assets/

- `main-template.html` — HTML template for main.html with placeholder variables
- `shared-libs/diagram.js` — Interactive diagram overlay engine (explore, quiz, edit modes)
- `shared-libs/style.css` — Shared styles for all diagram MicroSims
