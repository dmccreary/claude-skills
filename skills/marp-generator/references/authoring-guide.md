# MARP Authoring Guide

## Frontmatter

Every MARP deck starts with YAML frontmatter. The essentials:

```yaml
---
marp: true
theme: default
paginate: true
size: 16:9
---
```

- `theme`: one of the three built-in themes — `default` (clean, neutral, safe default), `gaia` (bolder, gradient-friendly, good for high-contrast talks), `uncover` (minimal, large type, best for very sparse/visual decks). Ask the user if they have a preference; otherwise use `default`.
- `paginate: true` shows page numbers — turn on unless the user explicitly wants a cleaner look.
- `size: 16:9` is the modern default; `4:3` exists but rarely wanted.
- Optional: `backgroundColor`, `color`, `header`, `footer` — set these if the user wants consistent branding across slides (e.g. a footer with the site name).

## Slide separators and per-slide directives

Slides are separated by a line containing only `---`, with a blank line on each side:

```markdown
# Slide One

Content here.

---

# Slide Two

More content.
```

Per-slide HTML comment directives change that one slide's rendering:

```markdown
<!-- _class: lead -->
# Big Title Slide

Centered, larger type — use this for the title slide and section dividers.
```

`_class: lead` (in `default`/`gaia`) centers content vertically and is the standard choice for a title slide and any section-break slides in a longer deck.

## Content rules — why they matter

A MARP slide is a fixed 16:9 canvas with **no scrolling**. Content that would be fine in a document overflows or gets auto-shrunk into unreadable tiny text on a slide. Concretely:

- **One idea per slide.** If a slide needs "and" in its title to describe what's on it, it's probably two slides.
- **Cap bullets at ~5–6 per slide**, each a short phrase, not a sentence. If condensing prose, cut it down to the core claim, not the full explanation.
- **Prefer a strong header + short list over a wall of text.** The header carries the idea; the audience reads the slide in 3 seconds while listening to the speaker.
- **Images/diagrams should be the point of the slide when used, not decoration alongside a full paragraph.** `![width:600px](image.png)` sizing syntax controls image size inline.

## Speaker notes

Anything after an HTML comment at the end of a slide's content, using MARP's presenter-note syntax, doesn't render on the slide itself but is preserved for the presenter:

```markdown
# The Point

- Short bullet
- Another short bullet

<!--
Presenter note: this is where the fuller explanation goes — the caveats,
the data source, the anecdote you'd say out loud but that would clutter
the slide itself.
-->
```

This is exactly where to put content that got cut when condensing an existing document into slides — don't just delete detail, defer it to a speaker note. Export speaker notes to a plain-text file with `marp-cli --notes` if the user wants a printable presenter script.

## Condensing an existing document into slides

When the input is an existing markdown file/chapter rather than a from-scratch topic:

1. Read the whole document first — don't start converting until you understand its overall arc.
2. Each major heading (`##` or `###`) typically becomes one slide, sometimes two if the section is dense. Don't force a 1:1 mapping if a section is trivial (fold it into an adjacent slide) or unusually rich (split it).
2. The slide gets the section's core claim or takeaway, stated as a short header + a few bullets. The section's full prose becomes the speaker note (see above) — don't lose it, defer it.
3. Add a title slide (document title + author/date if known) and, for longer documents, an agenda slide listing the major sections as an outline.
4. Close with a summary or "key takeaways" slide — restating the document's conclusion in slide form, not just stopping after the last section.
