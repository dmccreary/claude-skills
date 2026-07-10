---
name: marp-generator
description: Generates slide decks in the MARP (Markdown Presentation Ecosystem) format and publishes them as live, embeddable presentations on an MkDocs Material site. Use this skill whenever the user wants to turn a topic, description, or existing chapter/document into a presentation, slide deck, or set of slides — trigger on phrases like "make a slide deck", "turn this chapter into a presentation", "create slides for X", "I need to present this", "build a deck about Y", or "add a presentation to the site", even if the user never says "MARP" by name. Produces a self-contained docs/slides/<deck-name>/ directory (MARP source, exported HTML, thumbnail, documentation page), adds the deck to the docs/slides/index.md gallery, and updates mkdocs.yml nav.
model: sonnet
license: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC-SA 4.0)
---

# MARP Generator

This skill turns a topic description or an existing document into a [MARP](https://marp.app/) slide deck, exports it to a self-contained HTML file, and wires it into an MkDocs Material site the same way this repo already publishes MicroSims — a dedicated directory under `docs/`, an `index.md` documentation page with an embedded iframe, an entry in a gallery page, and a nav entry in `mkdocs.yml`.

## What the user gets

For a deck about, say, "the history of Unix," the skill produces:

```
docs/slides/history-of-unix/
├── slides.md        # MARP source — the only file you hand-edit
├── slides.html       # Self-contained rendered export (generated — never hand-edit)
├── slides.pdf         # Optional PDF export for download (generated on request)
├── thumbnail.png     # First-slide image, used as the gallery card image + og:image
├── metadata.json      # Deck metadata (title, theme, slide count, source doc, etc.)
└── index.md           # MkDocs page: intro + embedded iframe + fullscreen/download buttons
```

Plus:
- A new card in `docs/slides/index.md` (created if it doesn't exist yet) using the site's standard `grid cards` gallery pattern.
- A new nav entry under a `Slides:` top-level section in `mkdocs.yml` (created if it doesn't exist yet), mirroring the existing `MicroSims:` section.

## Why HTML export + iframe, not a live-rendering plugin

There are three ways to get MARP content onto a published site: (1) an MkDocs plugin that renders MARP server-side at build time, (2) client-side rendering via the `@marp-team/marp-core` JS bundle loaded from a CDN, or (3) pre-rendering each deck to a single self-contained HTML file with `marp-cli` and embedding it via iframe.

This skill uses **option 3**. `marp-cli --html` produces one HTML file per deck with all CSS and navigation JS inlined — no CDN dependency at page-load, no server-side build step beyond a one-time `npx` call, and it degrades gracefully on GitHub Pages' static hosting. It's the exact same pattern this repo already uses for MicroSims (`main.html` embedded via iframe), so it fits the existing publishing model instead of introducing a second one. See [references/mkdocs-integration.md](references/mkdocs-integration.md) for the alternatives considered and the exact export commands.

## High-level workflow

### 1. Figure out the input and clarify scope

The user gives you one of two things:
- **A topic/description** ("make me a deck on X") — you'll draft the outline yourself.
- **An existing document** (a chapter, README, or other markdown/text file) — read it and condense it; don't invent content that isn't there.

Before writing any slides, ask (briefly — don't interrogate over things you can reasonably assume):
- Roughly how many slides / how long is the talk? Default to ~12–15 slides for a topic overview, or roughly one slide per major heading/section when condensing an existing document.
- Any preferred MARP theme? Default to `default` if they have no opinion; `gaia` and `uncover` are the other two built-in options (see [references/authoring-guide.md](references/authoring-guide.md)).
- Should this land in a specific chapter/section of the site, or just in the general `docs/slides/` gallery?

### 2. Draft an outline and confirm before writing full slides

List the proposed slide titles (title slide, agenda, one line per content slide, summary/closing slide) and show them to the user before generating the full deck. It's much cheaper to reshuffle a 15-line outline than to rewrite 15 fully-written slides. Skip this confirmation step only for very short decks (under ~6 slides) or if the user has clearly already told you the exact structure they want.

### 3. Write `docs/slides/<deck-slug>/slides.md`

Use [assets/template.md](assets/template.md) as the starting skeleton for frontmatter and slide separators. Follow the content rules in [references/authoring-guide.md](references/authoring-guide.md) — one idea per slide, a hard cap on bullets, speaker notes for detail that doesn't belong on the slide itself. When condensing an existing document, put the material that got cut from the visible slide into a speaker-note HTML comment rather than dropping it silently — that way nothing is lost, it's just deferred to presenter notes.

`<deck-slug>` is a kebab-case slug derived from the deck title (e.g. "History of Unix" → `history-of-unix`), matching the naming convention already used under `docs/sims/`.

### 4. Export the deck

Run these from the project root (the directory containing `mkdocs.yml`). The first invocation downloads `@marp-team/marp-cli` and can take a minute or two; subsequent runs are fast since npx caches it.

```bash
DECK=docs/slides/<deck-slug>

# Self-contained HTML export — this is what index.md embeds
npx --yes @marp-team/marp-cli@latest "$DECK/slides.md" --html -o "$DECK/slides.html"

# Thumbnail from the title slide — used as the gallery card image
npx --yes @marp-team/marp-cli@latest "$DECK/slides.md" --image png -o "$DECK/thumbnail.png"
```

If the user wants a downloadable PDF too (nice-to-have, not required):

```bash
npx --yes @marp-team/marp-cli@latest "$DECK/slides.md" --pdf -o "$DECK/slides.pdf"
```

If `slides.md` references local image files, add `--allow-local-files` to all three commands. Re-run all exports any time `slides.md` changes — `slides.html`, `thumbnail.png`, and `slides.pdf` are build artifacts, not source.

### 5. Write `index.md`

Follow the exact iframe + fullscreen-button pattern this repo uses for MicroSims:

```markdown
---
title: <Deck Title>
description: <one-line description>
image: /slides/<deck-slug>/thumbnail.png
og:image: /slides/<deck-slug>/thumbnail.png
hide:
    - toc
---

# <Deck Title>

<One or two sentence description of what the deck covers and who it's for.>

<iframe src="./slides.html" width="100%" height="600px" scrolling="no"></iframe>

[View Fullscreen](./slides.html){ .md-button .md-button--primary }
[Download PDF](./slides.pdf){ .md-button }

## About This Deck

<Brief overview: topic, slide count, theme, and — if condensed from an existing
document — a link back to the source page.>
```

Drop the "Download PDF" button/line entirely if no PDF was exported. The 600px iframe height suits the default 16:9 Marp layout; the global `iframe { border: solid 2px blue; }` rule in `docs/css/extra.css` applies automatically — don't override it.

**Always hide the table of contents.** A deck's `index.md` has one heading and an iframe — there's nothing for a TOC to usefully outline, so always include `hide:` / `    - toc` in its frontmatter (as in the template above). This is the same `hide: [toc]` mechanism already used on the `docs/slides/index.md` gallery page in step 7.

**YAML frontmatter and colons.** A colon followed by a space (`: `) inside a frontmatter value breaks YAML parsing, because YAML reads it as a new key. `title: Claude Skills for Intelligent Textbooks: Overview` parses as key `title` with value `Claude Skills for Intelligent Textbooks`, then errors on the stray `Overview`. Prefer rewording the title/description to avoid a colon in the first place — e.g. an em dash or "—" reads just as well as a colon and never needs quoting (`Claude Skills for Intelligent Textbooks — Overview`). If a colon is unavoidable (a deck title quoting a colon-bearing phrase, for instance), wrap the whole value in double quotes: `title: "Claude Skills for Intelligent Textbooks: Overview"`. This applies to every frontmatter value you write in this skill — `index.md`, `docs/slides/index.md`, and the `title`/`label` values in `mkdocs.yml` nav entries alike.

### 6. Write `metadata.json`

```json
{
  "title": "<Deck Title>",
  "description": "<one-line description>",
  "creator": "<site author from mkdocs.yml>",
  "date": "<today, YYYY-MM-DD>",
  "type": "Slide Deck",
  "format": "text/html",
  "language": "en-US",
  "rights": "CC BY-NC-SA 4.0",
  "publisher": "Claude Skills Repository",
  "framework": "MARP (Markdown Presentation Ecosystem)",
  "theme": "default",
  "slideCount": 14,
  "sourceDocument": "<path to source doc, or null if drafted from scratch>",
  "tags": ["<a few keywords for search/filtering>"]
}
```

### 7. Add the deck to the gallery: `docs/slides/index.md`

Create this file if it's the first deck in the project, modeled on `docs/sims/index.md`:

```markdown
---
title: List of Slide Decks
description: A list of all the MARP presentations for this site
hide:
    - toc
---

# List of Slide Decks

Slide decks built with MARP (Markdown Presentation Ecosystem).

<div class="grid cards" markdown>

-   **[<Deck Title>](./<deck-slug>/index.md)**

    ![<Deck Title>](./<deck-slug>/thumbnail.png)

    <One-line description.>

</div>
```

If `docs/slides/index.md` already exists, insert the new card alphabetically among the existing ones inside the same `<div class="grid cards" markdown>` block — don't create a second grid block.

### 8. Update `mkdocs.yml` nav

If there's no `Slides:` top-level nav section yet, add one right after the `MicroSims:` section (or near the end of `nav:` if there's no MicroSims section), matching its structure:

```yaml
  - Slides:
    - List of Slide Decks: slides/index.md
    - <Deck Title>: slides/<deck-slug>/index.md
```

If the section already exists, just add one line for the new deck (alphabetically, matching the existing convention for the MicroSims list).

### 9. Report back

Tell the user the deck's file paths, that they can preview it with `mkdocs serve` (never start/stop this yourself — the user runs it in their own terminal), and remind them that editing the deck means changing `slides.md` and re-running the export commands from step 4.

## What NOT to do

- **Don't hand-edit `slides.html` or `thumbnail.png`.** They're generated artifacts. Edit `slides.md` and re-export.
- **Don't cram content.** MARP slides are a fixed 16:9 canvas with no scrolling — more than ~6 bullets or a few sentences will overflow or shrink unreadably. Split into more slides instead of packing them.
- **Don't silently drop content when condensing an existing document.** Put what doesn't fit on the visible slide into an HTML-comment speaker note instead.
- **Don't use client-side MARP JS rendering (`marp-it`/CDN bundle) instead of the pre-rendered HTML export.** It adds a runtime CDN dependency for no benefit here — see [references/mkdocs-integration.md](references/mkdocs-integration.md) for why the self-contained export is more robust for a statically-hosted MkDocs site.
- **Don't skip the outline-confirmation step (§2) for anything beyond a handful of slides.** Reshuffling an outline is cheap; reshuffling a finished deck is not.
- **Don't write an unquoted colon into a YAML frontmatter value.** `title: Some Thing: A Subtitle` silently breaks parsing. Prefer a colon-free phrasing (em dash instead of colon) in titles/descriptions; if a colon is truly unavoidable, quote the whole value.

## Reference docs

- **[references/mkdocs-integration.md](references/mkdocs-integration.md)** — why HTML-export-plus-iframe was chosen over an MkDocs plugin or client-side rendering, plus the full `marp-cli` flag reference (PDF, PPTX, images, themes, `--allow-local-files`).
- **[references/authoring-guide.md](references/authoring-guide.md)** — MARP frontmatter options, built-in themes, per-slide content rules, speaker notes, and how to condense an existing document into slides.
- **[assets/template.md](assets/template.md)** — starter MARP skeleton (frontmatter + title slide + agenda + content slide + closing slide) to copy into a new `slides.md`.
