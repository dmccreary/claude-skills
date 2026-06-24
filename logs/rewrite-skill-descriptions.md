# Skill Description Rewrite Log

**Date:** 2026-06-23  
**Scope:** All 25 skills in `skills/*/SKILL.md`  
**Skills changed:** 22  
**Skills already compliant:** 7 (`causal-loop-diagram-generator`, `microsim-generator`, `text-to-speech`, `book-installer`, `moving-rainbow`, `microsim-utils`, `learning-graph-generator`)

## Best Practices Applied

1. **Short** — 1–3 sentences, 20–55 words (down from 55–200+)
2. **Verb-first opener** — starts with the action ("Generates", "Creates", "Validates") not "This skill..."
3. **"Use when..."** — one concrete trigger condition, not a list of quoted phrases
4. **Key constraint** — one differentiator or sequencing note where relevant (e.g. "Use before running learning-graph-generator")
5. **No trigger-phrase lists** — removed all `"make me a CLD"`, `"add photos"`, `"create slides"` enumeration
6. **No implementation details** — pipeline steps, file counts, agent configs belong in the skill body, not metadata

## Changes by Skill

| Skill | Old words | New words | Issues fixed |
|-------|-----------|-----------|--------------|
| `book-chapter-generator` | 65 | 29 | "This skill..." opener; redundant phrasing |
| `chapter-content-generator` | 71 | 34 | "This skill..." opener; stray parenthetical `(project, gitignored)` |
| `chapter-image-enhancer` | 75 | 28 | Multiline YAML `>`; trigger-phrase list |
| `concept-classifier` | 55 | 34 | Implementation detail (`data.json` editing); "Ideal for..." filler |
| `course-description-analyzer` | 55 | 32 | "This skill..." opener; hardcoded file path in description |
| `diagram-reports-generator` | 60 | 31 | "This skill..." opener; hardcoded "geometry course" (too specific) |
| `docx-to-web-publisher` | 105 | 27 | Multiline YAML `>`; full pipeline enumeration; trigger-phrase list |
| `faq-generator` | 60 | 30 | "This skill..." opener; chatbot-integration detail |
| `glossary-generator` | 52 | 27 | "This skill automatically..." opener |
| `init-textbook` | 130 | 32 | Trigger-phrase list; post-scaffolding routing instructions |
| `interactive-infographic-overlay` | 75 | 34 | "This skill..." opener; file list belongs in body |
| `linkedin-announcement-generator` | 55 | 29 | "This skill..." opener; "professional"/"engaging" filler |
| `microsim-iframe-tester` | 90 | 31 | Trigger-phrase list (`"check if my sims fit"`, etc.) |
| `microsim-layout-reviewer` | 100 | 33 | Single-quoted YAML; trigger labels; "Complements" reference |
| `press-release-generator` | 130 | 40 | Trigger-phrase list; variant synonyms; "even if they don't say..." |
| `quiz-generator` | 65 | 26 | "This skill..." opener; implementation note (`serial execution`) |
| `readme-generator` | 50 | 22 | "This skill..." opener; self-referential sentence structure |
| `reference-generator` | 52 | 26 | "This skill..." opener; "high-quality"/"curated" filler |
| `register-book-analytics` | 90 | 33 | Multiline YAML `>-`; trigger-phrase list |
| `story-generator` | 120 | 33 | "This skill..." opener; `--panels` arg detail; trigger-phrase list |
| `textbook-to-presentation-generator` | 110 | 28 | Multiline YAML `>`; McLuhan quote; trigger-phrase list |
| `verified-infographic-generator` | 130 | 30 | Trigger-phrase list; "Skip only for..." double-negative |

## Before / After Examples

### `press-release-generator` (most extreme)

**Before (130 words):**
> Generates a professional, AP-style press release announcing an intelligent textbook, course, or major content milestone — inverted-pyramid structure with a real news hook, dateline, headline, lead, attributed quotes, an "About" boilerplate, a media-contact block, and the ### end mark. Reuses the book-metrics extraction pattern (docs/learning-graph/book-metrics.json + mkdocs.yml + docs/course-description.md) but produces a formal release for newsrooms and advocacy press rather than a social-media post. Use this skill whenever the user asks for a press release, news release, media release, media advisory, press statement, or "announcement for the press/media," or says they want to pitch a textbook to journalists, local newspapers, education trade press, or an advocacy newsletter — even if they don't say the exact words "press release." Distinct from linkedin-announcement-generator (social post) and readme-generator (GitHub docs).

**After (40 words):**
> Generates an AP-style press release for an intelligent textbook or course milestone — headline, lead, attributed quotes, boilerplate, and media-contact block. Use when pitching to journalists or education trade press; distinct from linkedin-announcement-generator (social post) and readme-generator (GitHub docs).

### `init-textbook` (trigger-phrase bloat)

**Before (130 words):**
> Scaffolds a new intelligent textbook project from scratch — creates mkdocs.yml, the docs/ directory tree, contact.md, license.md (CC BY-NC-SA 4.0), license.png badge, and starter index/about/course-description pages. Use this skill at the very start of a new textbook project, before any chapters, learning graph, or MicroSims exist. Trigger on phrases like "init textbook", "initialize textbook", "new textbook project", "scaffold a textbook", "set up a new book", or when the user is in an empty directory and asks to start building an intelligent textbook. After scaffolding, route the user to the book-installer skill to layer on optional features...

**After (32 words):**
> Scaffolds a new intelligent textbook project from scratch — mkdocs.yml, docs/ directory tree, starter pages, and license files. Use at the very start of a new project, before chapters, learning graph, or MicroSims exist.
