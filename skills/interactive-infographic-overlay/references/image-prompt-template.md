# Image Prompt Template

Use this template when generating the `image-prompt.md` file for a diagram overlay MicroSim.

## Template

```markdown
# {Diagram Title} — Image Generation Prompt

Please generate a new image.

## Critical Rule

**This image must contain absolutely no text, labels, arrows, callout lines, or
annotation marks of any kind.** All labeling will be added as an interactive HTML
overlay from a separate data file. Any embedded text will conflict with the overlay
system and must not appear.

---

## Image Specifications

- **Format**: PNG
- **Dimensions**: {width} × {height} px ({orientation}, {ratio} ratio)
- **Background**: {background color, e.g., clean white (#FFFFFF) or transparent}
- **Style**: {art style}; suitable for a {audience level} textbook

---

## What to Draw

{Overall description: what the diagram shows, viewing angle, framing, scale}

{For each structure, create a level-3 heading:}

### {N}. {Structure Name}

**Position**: {precise position — e.g., "slightly left of center, upper third of frame"}
**Visual**: {color, shape, size, distinctive features, texture}

{Repeat for each structure...}

---

## Layout Notes

{Instructions about spacing, proportions, margins, or composition details
that ensure overlay markers will fit cleanly over the image}
```

## Guidelines

1. **Be extremely specific** about colors — use hex codes or named colors
2. **Describe position** using both relative terms ("upper-left quadrant") and percentages ("centered at 35% from left, 25% from top")
3. **Specify dimensions** — the standard is 1200×900 for landscape, 900×1200 for portrait
4. **Describe each structure independently** so the image generator can render them without ambiguity
5. **Include a Layout Notes section** with spacing guidance to ensure markers have room
6. **Repeat the "no text" rule** — LLMs frequently add labels despite being told not to. Emphasize this at the top AND in layout notes.
