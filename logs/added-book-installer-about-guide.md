# Add About Page Generator Guide to Book-Installer

**Date:** April 20, 2026
**Project:** claude-skills/skills/book-installer
**Commit:** 8716790a

## Summary

Added a dedicated reference guide (`references/about-page.md`) to the book-installer meta-skill that generates professional `docs/about.md` pages for intelligent textbooks. The guide is designed to produce about pages that establish credibility with curriculum staff, school administrators, and educators evaluating textbooks for adoption.

## Motivation

The existing about.md template was a minimal placeholder with generic sections. After reviewing 10 recently published intelligent textbooks, a clear pattern emerged: the best about pages (digital-citizenship, Dementia, genetics, ecology, functions, theory-of-knowledge, unicorns) all share a motivational "Why This Book" section backed by cited statistics, a professional author bio, and formal citation formats. Curriculum staff evaluating textbooks for school adoption need these credibility signals before recommending a textbook. The new guide codifies this pattern so every future textbook gets a high-quality about page by default.

## Research: About Page Patterns Across 10 Textbooks

Analyzed the 10 most recently modified `docs/about.md` files across the workspace:

| Textbook | Mascot Welcome | Why Section | Statistics | Author Bio | Citations | License |
|----------|:-:|:-:|:-:|:-:|:-:|:-:|
| digital-citizenship | Yes (Maka) | Yes (Purpose) | No | Brief | No | Yes |
| Dementia | Yes (Tokie) | Yes (strong) | Yes (8 US, 5 global) | Yes (Rick Tanler) | Yes (4 formats) | No |
| functions | Yes (Rick) | Yes (strong) | Yes (3 stats) | Yes (Dan) | No | No |
| theory-of-knowledge | Yes (Sofia) | Yes | Yes (3 stats) | Yes (Dan) | Yes (APA + BibTeX) | No |
| genetics | Yes (Dottie) | Yes (strong) | Yes (5 stats) | Yes (Dan) | No | No |
| unicorns | Yes (Sparkle) | Yes (satirical) | No | Yes (Dan, humorous) | Yes (4 formats) | No |
| ecology | Yes (Bailey) | Yes | No | Yes (Dan) | Yes (4 formats) | No |
| ckg-benchmark | No | Yes (Why Does This Matter) | No | No | No | Yes |
| learning-sciences | No (placeholder) | No | No | No | No | No |
| pre-calc | Empty | No | No | No | No | No |

**Key findings:**
- Best pages have a "Why" section with real cited statistics (Dementia, genetics, functions)
- Dementia about page is the gold standard — 8 US statistics + 5 global, all footnoted
- Four citation formats (APA, Chicago, MLA, BibTeX) appear in the strongest pages
- Mascot welcome adds personality but must be in-character and concise
- Author bio with credentials list is essential for curriculum staff credibility

## Changes Made

### 1. Created `skills/book-installer/references/about-page.md` (351 lines)

New comprehensive guide with 8 template sections:

| Section | Purpose | Required |
|---------|---------|:--------:|
| Title + Frontmatter | SEO-friendly metadata | Yes |
| Mascot Welcome | In-character greeting | Only if mascot exists |
| Why This Intelligent Textbook | Motivational section with cited statistics | Yes |
| How to Use This Book | Feature inventory with counts | Yes |
| About the Author | Professional bio + credentials | Yes |
| How to Cite This Book | APA, Chicago, MLA, BibTeX formats | Yes |
| License | CC BY-NC-SA 4.0 or project license | Yes |
| Footnote References | Sources for statistics | Yes |

**"Why This Intelligent Textbook" section structure:**
1. Opening hook — ties subject to current urgency (1-2 sentences)
2. Evidence block — 4-8 cited statistics split into national and global groups
3. Emotional bridge — connects stats to the reader's students (1-2 sentences)
4. What makes this book different — concrete differentiators (learning graph, MicroSims, open source, prerequisite ordering)

**Author bio includes:**
- Dan McCreary's standard bio as default (with instructions for alternate authors)
- Selected credentials bulleted list
- Headshot image alignment

**Citation formats include:**
- APA 7th edition
- Chicago 17th edition
- MLA 9th edition
- BibTeX with proper key generation (`{author_last}{year}{subject_slug}`)
- Per-chapter citation example

### 2. Updated `skills/book-installer/SKILL.md`

- Added item **36** to the help list: "About page - professional about.md with motivation, author bio, and citations"
- Added routing table entry for keywords: `about page, about, about.md, about this book, author bio, cite this book, citation, 36`
- Added decision tree branch for about page generation
- Added Example 13: Generate About Page

### 3. Updated `skills/book-installer/references/assets/templates/docs/about.md`

Replaced the minimal 28-line placeholder template with a structured template matching all 8 sections from the guide. Template uses `{{VARIABLE}}` placeholders consistent with other book-installer templates.

## Design Decisions

1. **Statistics must be real and cited** — the guide explicitly forbids fabricated statistics. If a real stat isn't available, use qualified language ("estimated", "approximately") with the best available source. This prevents the footgun of AI-generated plausible-but-wrong statistics undermining credibility with curriculum reviewers.

2. **Four citation formats, not one** — curriculum staff work in different academic traditions. Providing APA, Chicago, MLA, and BibTeX covers education (APA), humanities (Chicago/MLA), and technical (BibTeX) without the user needing to convert.

3. **Dan McCreary bio as default with override path** — since Dan is the author of 70+ textbooks, his bio is the default. The guide includes explicit instructions for gathering bio information from alternate authors rather than always prompting.

4. **"Why" section is marked as the most important** — the guide explicitly calls this out. A curriculum director deciding whether to adopt a textbook will scan this section first. Generic motivational language is specifically prohibited.

## Files Changed

| File | Action | Lines |
|------|--------|------:|
| `skills/book-installer/references/about-page.md` | Created | 351 |
| `skills/book-installer/SKILL.md` | Modified | +15 |
| `skills/book-installer/references/assets/templates/docs/about.md` | Rewritten | 68 |

## Session Metrics

- Files created: 1
- Files modified: 2
- Research files read: 10 (about.md pages across workspace) + 2 (SKILL.md, home-page-template.md for pattern reference)
- Total lines of guide content: 351
