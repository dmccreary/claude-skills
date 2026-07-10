# MARP + MkDocs Integration

## The three options

**1. An MkDocs plugin that renders MARP at build time.** No mature, actively-maintained `mkdocs-material`-compatible MARP plugin exists as a standard dependency the way `mkdocs-mermaid2-plugin` does for Mermaid. Adopting one would add a Python dependency of uncertain maintenance status to every project this skill touches, for a format that already has an excellent, official standalone renderer.

**2. Client-side rendering via `@marp-team/marp-core` loaded from a CDN.** This mirrors how Mermaid diagrams render client-side in this site. It's viable in principle, but it means every page view depends on a CDN being reachable, and it means shipping raw MARP markdown into the page and re-parsing it in the browser on every load — extra JS execution and a runtime dependency for content that doesn't need to be dynamic. A slide deck is finished content, not a live user-editable diagram (unlike, say, an interactive vis-network diagram) — there's no interactivity being lost by pre-rendering it.

**3. Pre-render with `marp-cli --html`, embed the resulting self-contained file via iframe.** This is what the skill does. `marp-cli` produces a single HTML file with all CSS and the Marp "bespoke" navigation JS (arrow-key/click slide advance, on-screen controller, fullscreen) inlined — no external requests at page-load. It's a one-time build step (`npx @marp-team/marp-cli`), not a standing dependency, and the output is a static file that GitHub Pages serves exactly like any other asset. It's also the same publishing shape this repo already uses for MicroSims (`main.html` embedded via iframe), so there's no new pattern for future maintainers to learn.

## Exact export commands

Run from the project root (the directory containing `mkdocs.yml`). `DECK` is the deck's directory, e.g. `docs/slides/history-of-unix`.

```bash
# HTML export (what index.md embeds)
npx --yes @marp-team/marp-cli@latest "$DECK/slides.md" --html -o "$DECK/slides.html"

# Thumbnail (first slide only) for the gallery card + og:image
npx --yes @marp-team/marp-cli@latest "$DECK/slides.md" --image png -o "$DECK/thumbnail.png"

# Optional: PDF for a download button
npx --yes @marp-team/marp-cli@latest "$DECK/slides.md" --pdf -o "$DECK/slides.pdf"
```

Notes:
- `--html` is required whenever the deck uses inline HTML (iframes, `<style>` blocks, HTML in slide content) — without it, MARP strips raw HTML from the output for safety.
- `--image` and `--pdf` launch a headless Chrome/Chromium under the hood (via Puppeteer) to rasterize the slide. This works out of the box wherever `npx` and a system Chrome/Chromium are available — no extra setup needed on a machine that already runs headless-Chrome screenshot tooling (e.g. the `bk-capture-screenshot` script used for MicroSim thumbnails).
- Add `--allow-local-files` to any of the above if `slides.md` references local image files by relative path (marked "NOT SECURE" by marp-cli because it lets the markdown read arbitrary local files during conversion — fine here since you control the source).
- The first `npx @marp-team/marp-cli@latest` call in a fresh environment downloads the package and can take a minute or two. Subsequent calls reuse npx's cache and are fast.
- Other available export formats if ever needed: `--pptx` (PowerPoint), `--notes` (speaker notes as a text file), `--images` (every slide as a separate image, vs. `--image` for just the first one).

## Full-width vs. embedded sizing

The exported HTML uses MARP's default 16:9 canvas and is responsive — it fills whatever container it's placed in. A `height="600px"` iframe (the value used in the `index.md` template) works well for a typical MkDocs Material content column width; adjust up or down if the deck's theme or the site's content width differs noticeably from the default.
