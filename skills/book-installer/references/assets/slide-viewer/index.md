# Slide Viewer

A lightweight slide viewer for Markdown slide decks authored as MkDocs pages. Pass the rendered page URL of a `slides.md` file via the `?src=` query parameter and the viewer fetches the built HTML, splits the content on horizontal rules (`---`), and renders one slide at a time.

## Open a Deck

<!-- DECK_LIST_START -->
<!-- Deck links are appended here by the slide-generator installer. -->
<!-- DECK_LIST_END -->

## How It Works

- Author slides as a normal `slides.md` file next to a chapter's `index.md`.
- MkDocs builds that file into a standard page at a directory-style URL (e.g. `chapters/01-foundations/slides/`).
- The viewer fetches **that built URL** (never a `.md` path — MkDocs doesn't serve raw `.md`), parses the page's article content, and splits it on `<hr>` elements.
- The first slide is styled as a title slide; the last slide is flagged so the mascot swaps to a celebration pose.

## Controls

| Action | Keys | Button |
|---|---|---|
| Next slide | `→`, `Space`, `PageDown` | `›` |
| Previous slide | `←`, `PageUp` | `‹` |
| First slide | `Home` | `⏮` |
| Last slide | `End` | `⏭` |
| Fullscreen | `f` | `⛶` |
| Table of contents | `t` | `☰` |
| Close overlay | `Esc` | — |

## URL Parameters

| Param | Purpose | Example |
|---|---|---|
| `src` | Rendered page URL of the slide deck (no `.md`) | `?src=../../chapters/01-foundations/slides/` |
| `slide` | 1-based starting slide number | `?src=...&slide=5` |

## Authoring a Deck

Create a `slides.md` file anywhere under `docs/`. Use `---` on its own line to separate slides:

    # Title of the Deck

    Subtitle or author line.

    ---

    ## First Content Slide

    - Point one
    - Point two

    ---

    ## Second Content Slide

    Paragraph text and **bold** work normally.

Then open the viewer at the deck's **rendered** page URL:

    docs/sims/slide-viewer/main.html?src=<rendered-page-url>/

For a file at `docs/chapters/01-foundations/slides.md`, the rendered URL is `chapters/01-foundations/slides/`.

## Mascot Integration

If the project has a learning mascot installed at `docs/img/mascot/`, the viewer shows `neutral.png` in the lower-left of every slide and swaps to `celebration.png` on the final slide. If the mascot images are absent, the `<img>` simply 404s silently and the rest of the viewer works unchanged.
