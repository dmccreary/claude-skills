---
name: story-generator
description: This skill generates graphic novel narratives about scientists, mathematicians, engineers, inventors, and other historical figures in science and technology, designed for intelligent textbooks. It creates compelling, historically accurate 12-panel stories with embedded image prompts and can also generate the panel images automatically via the Google Gemini API. Use this skill when the user wants to add a new historical-figure story to a textbook's Stories section, or when creating educational graphic novel content.
---

# Story Generator

This skill generates complete graphic novel narratives about key contributors to science, mathematics, and technology, for intelligent textbooks built with MkDocs Material. Each story is a 12-panel graphic novel plus cover, designed to be inspirational, engaging, and historically accurate. Each panel includes a narrative paragraph below it and a detailed image-generation prompt in a collapsible `<details>` block.

As of the 2026-04 skill update, the skill can also **automatically generate all 13 panel images** (1 cover + 12 panels) natively at 16:9 (1344×768) via Google Gemini 2.5 Flash Image. See "Step 3.5: Generate Images" below.

## When to Use This Skill

Use this skill when:

- The user requests a new graphic novel story about a scientist, mathematician, engineer, or other historical figure
- Adding a story to a Stories / History section of any intelligent textbook
- Creating educational narrative content with embedded image prompts
- The user mentions "story", "graphic novel", or "narrative" about a historical figure

## Story Structure

Each story follows a consistent structure designed to engage teenage and young-adult readers:

### Required Components

1. **YAML Frontmatter** — Title, description, Open Graph image paths
2. **Cover Image** — With detailed generation prompt in a `<details>` block
3. **Narrative Prompt** — Background context for the whole story
4. **Prologue** — Hook introducing the subject's significance
5. **12 Panels** — Each with narrative text, image placeholder, and image prompt
6. **Epilogue** — Lessons table (Challenge / Response / Lesson for Today)
7. **Call to Action** — Inspiring message connecting to readers
8. **Quotes** — 2-3 memorable quotes from the subject
9. **References** — 5 real working URLs (first 3 Wikipedia, then secondary sources). **Never use `(PLACEHOLDER)`.**

A template for the complete structure is at `references/index-template.md`.

### YAML Frontmatter

Use the Open Graph protocol for social media sharing:

```yaml
---
title: <Catchy Title> - <Subject Name>'s <Theme>
description: A graphic-novel story of how <brief description>...
image: /stories/{story-dir-name}/cover.png
og:image: /stories/{story-dir-name}/cover.png
twitter:image: /stories/{story-dir-name}/cover.png
social:
   cards: false
---
```

Where `{story-dir-name}` is the kebab-case directory name.

**Length guidance:**
- Title: 60-70 characters max (longer titles get truncated on social media)
- Description: 155-200 characters (1-2 punchy sentences)

### Image Prompt Requirements

Every image prompt must specify:

- Wide-landscape **16:9 format** (the `generate-images.py` script passes this via API config — the text in the prompt is redundant but harmless)
- Period-appropriate art style (see the Art Style Reference table below)
- Specific characters with physical features and clothing
- Specific setting including year and location
- Color palette guidance
- Emotional tone and mood
- At least 6 specific visual details
- End with: `Generate the image immediately without asking clarifying questions.`

The `generate-images.py` script parses `<details><summary>Image Prompt</summary>...</details>` blocks directly from the story's `index.md`, so the block structure is load-bearing — do not change the HTML shape.

## Workflow

### Step 1: Gather Information and Plan the Story

Before writing, identify:

- The subject's full name and birth/death years
- Country and historical period
- Key discoveries, contributions, or life events
- Central theme (e.g., "persistence through failure", "seeing what others could not")
- Appropriate art style for the era
- 3-5 key life events that will anchor the 12 panels

### Step 2: Create the Story Directory

```bash
mkdir -p docs/stories/{story-dir-name-in-kebab-case}
```

Use kebab-case (lowercase with hyphens) for directory names: `ada-lovelace`, `rene-descartes`, `marie-curie`. Never use spaces or underscores.

### Step 3: Write the Story

Create `docs/stories/{story-dir-name}/index.md` following the template at `references/index-template.md`.

**Key conventions:**
- Exactly 12 numbered panels plus 1 cover = 13 images total
- All image references use `.png` extension
- Panel image prompts wrapped in `<details><summary>Image Prompt</summary>...</details>` blocks
- Cover image prompt wrapped in `<details><summary>Cover Image Prompt</summary>...</details>`
- Narrative paragraphs go *below* each panel's image (not inside the `<details>` block)
- References: 5 real URLs, never `(PLACEHOLDER)` — see the References Guidance section below

### Step 3.5: Generate Images (Optional but Recommended)

Once the markdown is written, generate the 13 panel images automatically with `scripts/generate-images.py`.

**Prerequisites:**

1. **Python package:**
   ```bash
   pip install google-genai
   ```

2. **API key** — Get a free one at https://aistudio.google.com/apikey, then:
   ```bash
   export GEMINI_API_KEY="your-key-here"
   ```
   For persistence, add it to `~/.zshrc` or `~/.bashrc`. The free tier requires no credit card and no billing account.

**First run — verify the cover image before burning credits on 12 more panels:**

```bash
python3 ~/.claude/skills/story-generator/scripts/generate-images.py \
    docs/stories/{story-dir-name} --first-only
```

This generates only the cover, verifies it is 16:9 via `sips`, and aborts automatically if the aspect ratio is wrong. Check the cover visually — does it match the art style and composition you want? If yes, proceed to the full run.

**Full run:**

```bash
python3 ~/.claude/skills/story-generator/scripts/generate-images.py \
    docs/stories/{story-dir-name}
```

This generates all 13 images (cover + 12 panels) at native 1344×768 (16:9). Expected wall-clock time: ~90 seconds at the 10 RPM rate limit. Each image is verified immediately after generation.

**Useful flags:**

| Flag | Purpose |
|---|---|
| `--first-only` | Generate only the cover image (aspect-ratio and style check) |
| `--skip-existing` | Skip any image whose PNG file already exists (safe for retries) |
| `--rpm N` | Override the default 10 RPM rate limit (use on paid tier with higher quota) |
| `--aspect-ratio W:H` | Override default `16:9`. Supported: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `9:16`, `3:4`, `2:3`, `5:4`, `4:5` |

**What the script produces:**

- PNG files at `docs/stories/{story-dir-name}/cover.png` and `panel-01.png` through `panel-12.png`
- A per-story markdown log at `logs/{story-dir-name}-{YYYY-MM-DD}.md` with run metadata, summary totals, per-image table, and prompt excerpts
- An appended JSONL audit line at `logs/image-generation-usage.jsonl` for each image (timestamp, tokens, computed cost)

**If an image generation fails:**

The script catches safety-filter failures and API exceptions, logs the reason (including `finish_reason` and safety ratings), and continues to the next image. Failed images are skipped, not fatal. After the run, rerun with `--skip-existing` to retry only the failures. See the "Safety Filter Patterns" section below for how to soften prompts that trip the safety filter.

### Step 4: Verify Images

After generation, run the verify script to confirm every image is present and at the right aspect ratio:

```bash
python3 ~/.claude/skills/story-generator/scripts/verify-images.py \
    docs/stories/{story-dir-name}
```

This is a read-only audit — it only checks, never modifies. Exit code 0 means clean, 1 means issues found. Especially useful for:
- Catching leftover square images from the old Antigravity workflow
- Verifying that all 13 panels exist after a partial run
- Pre-commit hooks

### Step 5: Add to Navigation

Edit `mkdocs.yml` to add the story in **chronological order by subject's birth year**:

```yaml
- Stories:
    - Overview: stories/index.md
    - <Subject Name> - <Title>: stories/<subject-name>/index.md
```

Example chronology (adapt to your project):
- Archimedes (287 BC)
- Galileo (1564)
- Descartes (1596)
- Newton (1643)
- Euler (1707)
- Fourier (1768)
- Faraday (1791)
- Lovelace (1815)
- Maxwell (1831)
- Tesla (1856)
- Marie Curie (1867)
- Einstein (1879)
- Noether (1882)
- Ramanujan (1887)
- Turing (1912)

### Step 6: Add a Grid Card to the Stories Index

Edit `docs/stories/index.md` to add a card using the MkDocs Material grid format:

```markdown
- **[<Story Title>](<subject-name>/index.md)**

    ![<Subject Name>](./<subject-name>/cover.png)
    <2-4 sentence compelling description emphasizing the story's theme>
```

## References Guidance

**Write real working URLs in the first draft. Do not use `(PLACEHOLDER)`.**

Follow the standard 5-reference pattern for every story:

| # | Source | Purpose |
|---|---|---|
| 1 | **Wikipedia: <Subject biography>** | Full biographical article |
| 2 | **Wikipedia: <Main contribution>** | The subject's signature discovery or work |
| 3 | **Wikipedia: <Related concept or work>** | A second topical link (e.g., an invention they're associated with, an equation named after them, a major paper) |
| 4 | **MacTutor** (mathematicians), **Nobel Prize** (laureates), **NASA** (mission scientists), or equivalent institutional bio | Stable academic history source |
| 5 | **Encyclopaedia Britannica** or **Stanford Encyclopedia of Philosophy** | Curated reference overview |

**Example — Ada Lovelace:**

```markdown
## References

1. [Wikipedia: Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace) - Biography of the English mathematician often called the first programmer
2. [Wikipedia: Analytical Engine](https://en.wikipedia.org/wiki/Analytical_Engine) - Babbage's proposed mechanical general-purpose computer
3. [Wikipedia: Note G](https://en.wikipedia.org/wiki/Note_G) - Lovelace's note describing the first published algorithm
4. [MacTutor: Augusta Ada King, Countess of Lovelace](https://mathshistory.st-andrews.ac.uk/Biographies/Lovelace/) - University of St Andrews history of mathematics archive
5. [Encyclopaedia Britannica: Ada Lovelace](https://www.britannica.com/biography/Ada-Lovelace) - Overview of Lovelace's life and contributions to computing
```

### Fixing Legacy Stories with PLACEHOLDER URLs

Some stories generated before the 2026-04 skill update still contain `(PLACEHOLDER)` reference URLs. To clean these up in bulk, copy `scripts/fix-references.py` to your project's `src/` directory, edit the `REFS` dict at the top to list the stories and their curated URLs, and run it:

```bash
cp ~/.claude/skills/story-generator/scripts/fix-references.py src/stories/
# Edit src/stories/fix-references.py to fill in the REFS dict
python3 src/stories/fix-references.py
```

The script rewrites everything from the `## References` heading to EOF in each listed story's `index.md`. Safe to re-run.

This script is intentionally NOT generic — curating good references is a judgment call, and each project wants slightly different sources. Maintaining a project-local customized copy is the right approach.

## Safety Filter Patterns

Gemini 2.5 Flash Image will refuse prompts that trip its safety classifier. The refusal shows up as `finish_reason=FinishReason.IMAGE_SAFETY` in the response, and the script logs it and continues to the next image without crashing.

**Known triggers:**

- Explicit Nazi imagery (swastikas, Nazi banners, SS uniforms)
- Graphic violence, wounds, or blood
- Nudity or sexual content
- Minors in explicitly distressing scenes
- Depictions of real people being killed or tortured

**Softening patterns** — rewrite the prompt to keep the emotional weight while removing the trigger:

| Original (triggers filter) | Softened (usually works) |
|---|---|
| "Nazi banners hanging on buildings" | "empty gray street with bare trees" |
| "swastika stamp on the letter" | "generic wax seal on the letter" |
| "forced out by Nazi laws" | "preparing to leave Germany" |
| "blood on the floor" | "a broken object on the floor" |
| "executed by firing squad" | "his empty desk and overturned chair" |

**Case study — Emmy Noether panel 10 (2026-04-05):** the original prompt explicitly mentioned "Nazi banners hang on a distant building" and "dismissal letter with a swastika stamp". Gemini refused with `IMAGE_SAFETY`. Softening to "empty gray street with bare trees" and "government dismissal letter with a generic wax seal" produced a clean generation on the next attempt. The historical meaning of forced exile survives; the explicit symbology is gone.

**Workflow when a prompt gets blocked:**

1. The script logs the failure and continues — no crash
2. Edit the offending prompt in the story's `index.md` to soften trigger words
3. Rerun: `python3 generate-images.py docs/stories/<name> --skip-existing`
4. Only the previously-failed panel regenerates; all other panels are skipped
5. Commit the softened prompt so future regenerations work on the first try

## Cost Analysis

**Gemini 2.5 Flash Image pricing (verified early 2026):**

- Input text tokens: $0.30 per 1M
- Output image tokens: $30.00 per 1M
- Fixed rate: **1,290 output tokens per image** = **$0.039 per image** on the paid tier

**Free tier:**

- 500 requests per day (RPD)
- 10 requests per minute (RPM)
- ~250,000 tokens per minute (TPM)
- **No credit card required**, no billing account

**Cost projections:**

| Scope | Images | Paid tier | Free tier |
|---|:---:|:---:|:---:|
| One story (1 cover + 12 panels) | 13 | $0.51 | **$0.00** |
| One 16-story textbook | 208 | $8.07 | **$0.00** |
| Daily free-tier ceiling | 500 | — | **$0.00** |

**Headline recommendation for low-budget users (teachers in developing countries, students, independent authors):** use the free tier. A single teacher producing one textbook per week uses roughly 6% of their monthly free quota. The paid tier is essentially never needed for realistic classroom workflows.

### Alternative Models (for high-volume production)

If you exceed 500 images/day per project on a sustained basis, cheaper options exist, though quality varies:

| Model | Provider | Approx cost/image | Notes |
|---|---|---|---|
| FLUX.1 [schnell] | Fal / Replicate | **$0.003** | 13× cheaper, decent quality, no native 16:9 config |
| FLUX.1 [dev] | Fal / Replicate | $0.025 | Middle tier, excellent quality |
| SD 3.5 Medium | Stability AI | ~$0.035 | Comparable to Gemini |
| gpt-image-1 (low) | OpenAI | $0.011 | 3× cheaper, lower quality, limited aspect ratios |
| Local SDXL / FLUX | Self-hosted GPU | ~free | Requires 16+ GB VRAM and setup time |

**Honest assessment:** Gemini 2.5 Flash Image remains the best quality per dollar at the scale this skill targets. The alternatives only become worthwhile above 500 images/day per project, which no realistic textbook workflow hits.

## Known Issues

### Antigravity `generate_image` tool does not expose `aspect_ratio`

Google Antigravity IDE ships an internal `generate_image` tool whose schema only accepts `Prompt`, `ImageName`, `ImagePaths`, and tool metadata. It does **not** expose `aspect_ratio` or `size`, so every image it generates defaults to 1:1 square. **Do not use Antigravity's `generate_image` for graphic novel panels.** Use `scripts/generate-images.py` (this skill) instead — it calls Gemini directly via `google-genai` and passes `ImageConfig(aspect_ratio="16:9")`.

Prompt-level workarounds like "16:9 landscape cinematic composition" do **not** work — Gemini obeys `ImageConfig.aspect_ratio` but treats aspect-ratio hints in the prompt as stylistic suggestions at best.

Worth reporting: the Antigravity team should expose all 10 aspect ratios Gemini supports (`21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `9:16`, `3:4`, `2:3`, `5:4`, `4:5`), plus ideally `response_modalities` and a transparent-PNG option.

### Character face consistency across panels

Gemini 2.5 Flash Image maintains **style continuity** (art style, color palette, mood) across multiple generations with similar prompts, but does **not** maintain exact facial features for the same character. Panel 3's Marie Curie will look stylistically similar to Panel 5's Marie Curie, but they won't be identical. For educational graphic novels where panels are read sequentially with narration below, this is usually acceptable. For professional-grade work requiring pixel-identical character faces, consider Flux Kontext, Imagen 4 with reference images, or a fine-tuned character LoRA. Out of scope for this skill.

### Only the first image part is used

If Gemini returns multiple image parts in a single response (rare but possible), the script saves only the first one. Multi-image responses are not supported.

## Art Style Reference by Era

| Era | Suggested Art Style |
|-----|---------------------|
| Ancient (before 500 AD) | Classical Mediterranean, mosaic-inspired |
| Renaissance (1400-1600) | Italian Renaissance, warm lighting |
| Enlightenment (1600-1800) | Baroque, Dutch Golden Age |
| Napoleonic Empire (1795-1815) | Empire-era French academic painting |
| Victorian (1800-1900) | Pre-Raphaelite, industrial |
| Gilded Age (1870-1900) | Art Nouveau, American industrial |
| Early Modern (1900-1950) | Art Deco, Modernist, Bauhaus (for Weimar-era Germany) |
| WWII era (1939-1945) | 1940s noir, muted olive/khaki |
| Mid-Century (1950-1980) | Atomic Age, clean lines, Bell Labs modernism |
| Space Age (1957-1975) | NASA technical illustration, cosmic blues |
| Contemporary (1980-present) | Photorealistic with period elements |

## Writing Guidelines

### Target Audience

- Secondary-school students (grades 9-12, ages 14-18) for most intelligent textbook projects
- Adjust reading level based on project — the skill supports younger or older audiences by changing the narrative voice, not the structure

### Narrative Style

- Use active voice and vivid descriptions
- Include dialogue when historically appropriate
- Balance drama with educational accuracy
- Emphasize the human story behind discoveries
- Show struggles, failures, and persistence
- Connect historical events to modern technology or contemporary relevance

### Theme Development

Choose a central theme that resonates with the target audience:

- Overcoming doubters and skeptics
- Persistence through failure
- Self-education and curiosity
- Fighting against discrimination
- Seeing what others couldn't see
- Staying humble despite success
- Making the invisible visible

### Historical Accuracy

- Research key dates, events, and relationships
- Use historically accurate details in image prompts (clothing, architecture, technology, typography)
- Note any creative liberties in the Narrative Prompt block
- Include verifiable quotes when possible

## Scripts

### generate-images.py (primary)

Generates all panel images via the Gemini API. See "Step 3.5: Generate Images" above.

### verify-images.py

Read-only audit tool — checks that all expected panels exist, are the right aspect ratio, and meet a minimum file size. Usage:

```bash
python3 ~/.claude/skills/story-generator/scripts/verify-images.py \
    docs/stories/{story-dir-name}
```

### fix-references.py (legacy-fix tool)

For retroactively replacing `(PLACEHOLDER)` reference URLs in older stories. **Not for new stories** — new stories should have real URLs in the first draft. See the "References Guidance" section above.

### uncomment-images.sh (fallback workflow)

For workflows that defer image generation: the markdown ships with image references wrapped in HTML comments (`<!-- ![](./panel-01.png) -->`) to prevent broken image icons, and this script uncomments them once the PNGs are produced by any means.

**Usage:**

```bash
~/.claude/skills/story-generator/scripts/uncomment-images.sh \
    docs/stories/{story-dir-name}/index.md
```

**When to use:**
- You want to ship markdown immediately and generate images later in a batch job
- You're using an image generation tool other than `generate-images.py`
- You're migrating from an older workflow

**When NOT to use:**
- You're using `generate-images.py` — it writes PNGs directly to the filenames referenced in `index.md`, so nothing needs uncommenting

## Checklist

After completing a story, verify:

**Content:**
- [ ] Story directory created: `docs/stories/<name>/`
- [ ] `index.md` has full narrative and all 13 image prompts (cover + 12 panels)
- [ ] All image references use `.png` extension (never `.jpg` or `.md`)
- [ ] YAML frontmatter has title, description, and og/twitter image paths
- [ ] 12 numbered panels with consistent structure (image + prompt + narrative)
- [ ] Epilogue includes the Challenge / Response / Lesson table
- [ ] 2-3 subject quotes present
- [ ] **References section has 5 real working URLs, first 3 on Wikipedia, no `(PLACEHOLDER)` strings**

**Image generation (if using generate-images.py):**
- [ ] `GEMINI_API_KEY` set in environment
- [ ] `pip install google-genai` completed
- [ ] `generate-images.py --first-only` run and cover verified as 16:9 natively (1344×768)
- [ ] Full `generate-images.py` run completed with no fatal errors
- [ ] All 13 PNG files present in the story directory
- [ ] `verify-images.py` exits with code 0
- [ ] Per-story log present at `logs/{story-name}-{YYYY-MM-DD}.md`
- [ ] JSONL usage log updated at `logs/image-generation-usage.jsonl`

**Integration:**
- [ ] Added to `mkdocs.yml` navigation in chronological order by birth year
- [ ] Grid card added to `docs/stories/index.md`
- [ ] Any safety-filter softenings are committed so future regenerations don't regress

## Appendix: Lessons Learned from the IB Functions Textbook (2026-04-05)

The 2026-04 skill update was driven by a real-world 16-story textbook project in `/Users/dan/Documents/ws/functions`. The definitive case study lives at `/Users/dan/Documents/ws/functions/logs/stories.md`. Key lessons captured here:

1. **The old workflow produced square images.** Stories were generated via the Antigravity IDE agent's `generate_image` tool, which does not expose `aspect_ratio` and defaults to 1:1. The workaround was to upscale the square to 1280×1280 and center-crop to 1280×720 — losing ~44% of the vertical content. The fix was to bypass Antigravity and call Gemini directly via `google-genai`, which is what `scripts/generate-images.py` now does.

2. **The free tier is genuinely free.** A full 16-story textbook (208 images) cost **$0.00** on the Gemini free tier and would have cost **$8.07** on the paid tier. For the teachers-in-developing-countries audience the skill targets, the free tier is the correct recommendation every time.

3. **Safety filters are rare but will bite you.** Out of 208 images generated, exactly 1 was blocked outright (Emmy Noether panel 10, because of explicit Nazi imagery) and 1 was blocked transiently (Mirzakhani panel 10, cleared on retry without any change). The script now handles both cases gracefully, and the softening pattern for Noether-style content is documented above.

4. **Placeholder references are a trap.** All 16 stories initially shipped with `(PLACEHOLDER)` URLs from an earlier version of this skill. Retroactively fixing them required writing a `fix-references.py` script. New stories should have real URLs in the first draft — this skill now teaches that explicitly.

5. **Per-run audit logs are worth the lines of code.** The JSONL audit log caught a subtle fact that would have been invisible otherwise: every single image, regardless of prompt complexity, bills for exactly 1,290 output tokens. This confirmed the published pricing model and gave the user confidence that cost projections would be accurate at scale.

6. **Character face consistency is not yet solved at this price point.** See "Known Issues" above. Users should not expect pixel-identical characters across 12 panels — the current state of the art at $0.039/image produces stylistically consistent but individually distinct characters. This is an acceptable tradeoff for educational graphic novels at scale; it is not acceptable for professional commercial publishing.

If you're updating this skill in the future, read `logs/stories.md` in the functions project for the full session transcript and all the decisions behind the current design.
