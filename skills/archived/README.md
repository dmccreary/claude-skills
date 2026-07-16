# Archived Skills

These directories are the verbatim originals of standalone skills that were
consolidated into meta-skills. They are **never loaded** by Claude Code: skill
discovery only scans one level below `~/.claude/skills/`, and
`scripts/bk-install-skills` explicitly skips this directory. They are kept for
reference and rollback — to restore one, `git mv` it back to `skills/` and
rerun the installer.

## Alias map: old skill → where it lives now

| Old skill | New home | Trigger keywords |
|-----------|----------|------------------|
| `causal-loop-diagram-generator` | `microsim-generator` → `references/causal-loop-guide.md` | causal loop, CLD, feedback loop, reinforcing, balancing, systems archetype |
| `concept-classifier` | `microsim-generator` → `references/concept-classifier-guide.md` | classify, categorize, sort scenarios, identify types |
| `interactive-infographic-overlay` | `microsim-generator` → `references/infographic-overlay-guide.md` | diagram overlay, callout labels, anatomy, labeled illustration |
| `docker-python-lab` | `microsim-generator` → `references/docker-python-lab-guide.md` | python lab, code runner, runnable code block, docker |
| `diagram-reports-generator` | `microsim-utils` → `references/diagram-reports.md` | legacy diagram specification report, planned visual inventory |
| `init-textbook` | `book-installer` → `references/init-textbook.md` (feature 0) | init textbook, scaffold textbook, brand new book, empty directory |
| `register-book-analytics` | `book-installer` → `references/google-analytics.md` (feature 25) | google analytics, GA4, measurement id, G-* |
| `readme-generator` | `book-publisher` → `references/readme-guide.md` | readme, github readme, badges |
| `linkedin-announcement-generator` | `book-publisher` → `references/linkedin-post-guide.md` | linkedin post, announcement, milestone |
| `linkedin-carousel-generator` | `book-publisher` → `references/linkedin-carousel-guide.md` | linkedin carousel, document post, slideshow post |
| `press-release-generator` | `book-publisher` → `references/press-release-guide.md` | press release, media pitch, journalists, AP style |
| `marp-generator` | `book-media-generator` → `references/marp-deck-guide.md` | slide deck, presentation, web slides, MARP |
| `textbook-to-presentation-generator` | `book-media-generator` → `references/pptx-lecture-guide.md` | powerpoint, pptx, lecture deck, classroom slides |
| `story-generator` | `book-media-generator` → `references/story-guide.md` | story, graphic novel, historical figure |
| `verified-infographic-generator` | `book-media-generator` → `references/verified-infographic-guide.md` | infographic, poster, fact-checked statistics |
| `chapter-image-enhancer` | `book-media-generator` → `references/chapter-images-guide.md` | chapter images, photos, maps, Wikimedia |
| `text-to-speech` | `book-media-generator` → `references/text-to-speech-guide.md` | text to speech, voiceover, ElevenLabs |
| `pronounce-button` | `book-media-generator` → `references/pronounce-button-guide.md` | pronounce, pronunciation, glossary audio |
