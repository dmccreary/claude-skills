---
name: learning-mascot
description: Guides users through designing a pedagogical agent (learning mascot) for their intelligent textbook, generating AI image prompts, and implementing the mascot using custom CSS admonitions with body-floated images.
---

# Learning Mascot (Pedagogical Agent)

This skill helps users design and implement a pedagogical agent — a visual mascot character that guides students through their intelligent textbook. Research on the "persona effect" shows that characters improve learner engagement and perception of learning.

## What This Skill Creates

1. **Character Design** - A fully defined mascot persona (name, species, appearance, voice, catchphrase)
2. **AI Image Prompts** - Ready-to-use prompts for generating mascot images in consistent poses
3. **Implementation** - Custom CSS admonitions with mascot images floated left in the admonition body
4. **CLAUDE.md Section** - Character guidelines for consistent AI-generated content

## Benefits of a Learning Mascot

- **Engagement** - Gives the textbook personality that students connect with emotionally
- **Wayfinding** - Signals special content types (tips, challenges, reflections) visually
- **Encouragement** - Character dialogue normalizes struggle and celebrates progress
- **Branding** - Distinctive mascots make courses memorable and build community identity

## Prerequisites

- Existing MkDocs Material project (use `mkdocs-template.md` first if needed)
- Access to an AI image generator (ChatGPT/DALL-E, Midjourney, Stable Diffusion, or similar)
- Course description or learning graph to inform mascot theme

## Performance Guidelines

This skill involves interactive Q&A (Steps 1-2) followed by file generation (Steps 3-7).

**During Q&A (Steps 1-2):** Ask all design questions in as few turns as possible. Present all questions together with default suggestions so the user can answer multiple at once.

**During file generation (Steps 3-7):** Do NOT use TaskCreate/TaskUpdate — the overhead of loading deferred tools and making 12+ task calls turns a <1 minute job into 10+ minutes. Instead:

1. Run `mkdir -p docs/img/mascot docs/css` first
2. Then execute ALL file operations in a single parallel batch:
   - Write `docs/css/mascot.css`
   - Write `docs/img/mascot/image-prompts.md`
   - Write `docs/learning-graph/mascot-test.md`
   - Write or update `CLAUDE.md`
   - Edit `mkdocs.yml` (theme palette, extra_css, nav entry)
3. Target: all file generation completes in one tool-call round

**During trim step (Step 4b):** The trim script path is `$PROJECT_HOME/../claude-skills/src/image-utils/trim-padding-from-image.py`. Do NOT search for it — just run it directly on all 7 images. Use the known filenames: neutral.png, welcome.png, thinking.png, tip.png, warning.png, encouraging.png, celebration.png.

## Workflow

### Step 1: Gather Course Context

Before designing the mascot, collect information about the book:

1. **Book Title** - What is the textbook about?
2. **Subject Area** - The academic domain (math, science, history, programming, etc.)
3. **Target Audience** - Age range and level (K-5, middle school, high school, college, professional)
4. **Tone** - Serious/academic, friendly/approachable, playful/fun, inspiring/motivational
5. **Existing Color Palette** - Primary and accent colors from the book's theme

### Step 2: Design the Mascot Character

Ask the user these questions to define their mascot. Provide suggestions for each.

**Question 1: What type of character?**

Suggest options based on the subject area:

| Subject Area | Suggested Characters | Reasoning |
|-------------|---------------------|-----------|
| Mathematics | Owl, Fox, Raccoon | Wisdom, cleverness, curiosity |
| Science | Squirrel, Cat, Robot | Experimentation, curiosity, precision |
| History | Tortoise, Elephant, Raven | Longevity, memory, storytelling |
| Programming | Robot, Cat, Octopus | Logic, independence, multitasking |
| Language Arts | Parrot, Bookworm, Fox | Communication, reading, storytelling |
| Music/Art | Peacock, Songbird, Chameleon | Expression, creativity, adaptation |
| Environmental Science | Tree Frog, Bee, Dolphin | Ecology, community, intelligence |
| Engineering | Beaver, Ant, Spider | Building, teamwork, design |
| Business | Lion, Eagle, Dolphin | Leadership, vision, collaboration |
| Health/PE | Cheetah, Bear, Hawk | Speed, strength, focus |

Also offer: abstract characters (geometric shapes with faces), human characters (student, professor, explorer), or mythological creatures (phoenix, dragon, unicorn).

**Question 2: What personality traits?**

Suggest 3-4 traits that match the tone:

- **Friendly/Approachable**: Warm, patient, encouraging, slightly goofy
- **Academic/Scholarly**: Wise, precise, thoughtful, curious
- **Adventurous/Exciting**: Bold, enthusiastic, energetic, brave
- **Calm/Supportive**: Gentle, reassuring, steady, kind

**Question 3: What is the character's name?**

Suggest names that:

- Are easy to remember and pronounce
- Relate to the subject (e.g., "Ada" for programming, "Archie" for architecture)
- Have alliteration with the species (e.g., "Sylvia the Squirrel", "Otto the Owl")
- Are culturally neutral and inclusive

Provide 3-5 name suggestions based on the species and subject.

**Question 4: What is the character's catchphrase?**

The catchphrase adds personality. Suggest options:

- **Math**: "Let's figure this out!", "Numbers never lie!", "Time to calculate!"
- **Science**: "Let's experiment!", "Hypothesis time!", "Let's crack this nut!"
- **Programming**: "Let's debug this!", "Time to code!", "Compile and conquer!"
- **History**: "Let's travel back in time!", "History has a lesson!", "What happened next?"
- **General**: "Great question!", "Let's explore!", "You've got this!", "Think about it!"

**Question 5: What does the character look like?**

Collect specific visual details:

- **Species/Type**: (from Question 1)
- **Colors**: Primary body color, accent colors (hat, scarf, glasses, etc.)
- **Clothing/Accessories**: Glasses, lab coat, backpack, tool belt, scarf, hat
- **Expression**: Friendly smile, curious look, thoughtful pose
- **Size Proportion**: Small (icon-sized) to medium (quarter-page)
- **Art Style**: Cartoon/flat, watercolor, pixel art, 3D rendered, hand-drawn sketch

**Question 6: Where should the mascot appear?**

Suggest placement contexts:

| Context | Purpose | Frequency | Filename |
|---------|---------|-----------|----------|
| Neutral Pose | General pose | As needed | neutral.png |
| Chapter Welcome | Welcome and preview | Start of every chapter | welcome.png |
| Key insight | Signal important insights | As needed | thinking.png |
| Tips and hints | Offer helpful guidance | As needed | tip.png |
| Warnings and pitfalls | Alert to common mistakes | As needed | warning.png |
| Difficult concepts | Provide encouragement | As needed | encouraging.png |
| Chapter summaries | Review and celebrate | End of every chapter | celebration.png |

**IMPORTANT: Restraint Guidelines**

The mascot should NOT appear:

- More than 5-6 times per chapter
- In every single admonition or callout
- In ways that interrupt reading flow
- With excessive dialogue that adds no value

### Step 3: Generate AI Image Prompts

Create a set of prompts for generating consistent mascot images. **Each prompt must be fully self-contained** — include the complete base character description in every prompt so they can be used independently without copying a separate base block.

#### Base Character Prompt

This is the core description to include in every pose prompt:

```
Please generate a new pose for [NAME] the [SPECIES].
A [ART_STYLE] illustration of [NAME] the [SPECIES], a friendly pedagogical mascot
for a [SUBJECT] textbook. [NAME] is [COLOR_DESCRIPTION], wearing [ACCESSORIES].
[NAME] has [EXPRESSION]. The character is [SIZE_DESCRIPTION].
Style: [ART_STYLE], clean lines, transparent background,
suitable for embedding in educational content. No text in image.

Please generate a new png image now with a fully transparent background now.

```

#### Pose Variants

Generate prompts for each of these poses. **Always include the full base description in each prompt** — never use `[BASE]` shorthand:

**1. Neutral/Default Pose** (general sidebars, introductions, inline use)

[FULL BASE DESCRIPTION] [NAME] stands upright in a relaxed, neutral pose facing the
viewer directly, with a calm and friendly closed-mouth smile. Arms/paws/wings
rest naturally at their sides with no specific gesture. The pose is balanced
and unassuming — suitable as a general-purpose or default illustration.
Filename: neutral.png

Please generate a new png image now with a fully transparent background now.
The background MUST be fully transparent.  DO NOT use a white, black or a checkered background.


**2. Welcome/Introduction Pose** (chapter openings)


Please generate a new welcome pose for [NAME].
[FULL BASE DESCRIPTION] [NAME] is waving cheerfully with one hand/paw/wing,
facing the viewer with a warm, welcoming expression.
The pose suggests "welcome" and "let's get started."
Filename: welcome.png

Please generate a new png image now with a fully transparent background now.
The background MUST be fully transparent.  
DO NOT use a white, black or a checkered background.


**3. Thinking/Teaching Pose** (key concepts)


Please generate a new thinking pose for [NAME].
[FULL BASE DESCRIPTION] [NAME] has one hand/paw on chin in a thoughtful pose,
with a small lightbulb or thought bubble above their head.
The pose suggests deep thinking and discovery.
Filename: thinking.png

Please generate a new png image now with a fully transparent background now.
The background MUST be fully transparent.  DO NOT use a white, black or a checkered background.


**4. Pointing/Tip Pose** (tips and hints)


Please generate a new tip pose for [NAME].
[FULL BASE DESCRIPTION] [NAME] is pointing upward with one finger/paw
as if sharing an important tip. Expression is helpful and knowing.
A small star or sparkle near the pointing gesture.
Filename: tip.png

Please generate a new png image now with a fully transparent background now.
The background MUST be fully transparent.  DO NOT use a white, black or a checkered background.


**5. Warning/Caution Pose** (warnings and pitfalls)


Please generate a new friendly warning pose for [NAME].
[FULL BASE DESCRIPTION] [NAME] holds up both hands/paws in a gentle "stop"
or "be careful" gesture. Expression is concerned but caring.
A small exclamation mark or caution symbol nearby.
Filename: warning.png

Please generate a new png image now with a fully transparent background now.
The background MUST be fully transparent.  DO NOT use a white, black or a checkered background.


**6. Encouraging Pose** (difficult sections)


Please generate a new encouraging pose for [NAME].
[FULL BASE DESCRIPTION] [NAME] gives a thumbs up (or equivalent gesture)
with a reassuring, supportive smile. The pose radiates confidence
and "you can do it" energy.
Filename: encouraging.png

Please generate a new png image now with a fully transparent background now.
The background MUST be fully transparent.  DO NOT use a white, black or a checkered background.


**7. Celebration Pose** (achievements, chapter completion)


Please generate a new celebration pose for [NAME].
[FULL BASE DESCRIPTION] [NAME] is jumping or raising both arms/paws/wings
in celebration. Expression is joyful and proud.
Small confetti or stars around the character.
Filename: celebration.png

Please generate a new png image now with a fully transparent background now.
The background MUST be fully transparent.  DO NOT use a white, black or a checkered background.


#### Example: Complete Prompt Set for "Otto the Owl"


```
Base: A flat cartoon illustration of Otto the Owl, a friendly pedagogical
mascot for a mathematics textbook. Otto is a round barn owl with warm
brown and cream feathers, wearing small round glasses and a blue
graduation cap. Otto has large, kind eyes with a gentle smile.
The character is small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, transparent background,
suitable for embedding in educational content. No text in image.

Neutral: [Base] Otto stands upright in a relaxed, neutral pose facing
the viewer with a calm, friendly closed-mouth smile. Both wings rest
naturally at his sides. No specific gesture.

Welcome: [Base] Otto is waving one wing cheerfully, facing the viewer
with a warm, welcoming expression.

Thinking: [Base] Otto has one wing on his chin, looking upward
thoughtfully. A small lightbulb glows above his head.

Tip: [Base] Otto points upward with one wing feather, looking helpful
and knowing. A small star sparkles near the gesture.

Warning: [Base] Otto holds up both wings in a gentle "be careful"
gesture, looking concerned but caring.

Encouraging: [Base] Otto gives a wing thumbs-up with a warm,
reassuring smile.

Celebration: [Base] Otto spreads both wings wide with joy, eyes
squinted in a big smile. Small confetti falls around him.
```

Present the generated prompts to the user and ask them to generate images using their preferred AI image tool. Recommend generating at 512x512 or 1024x1024 pixels, then resizing down for use
and also running the python script that will remove extra padding around the edges with
the scripts/trim-padding-from-image.py program.  Place the trim padding command in
the screen for the user to run.

### Step 4: Save Mascot Images

After the user generates their images, instruct them to save them:

```
docs/img/mascot/
├── neutral.png       # General purpose / default
├── welcome.png       # Chapter openings
├── thinking.png      # Key concepts
├── tip.png           # Tips and hints
├── warning.png       # Warnings
├── celebration.png   # Achievements
└── encouraging.png   # Difficult sections
```

```bash
mkdir -p docs/img/mascot
```

Required specifications:

- Format: PNG with transparent background
- Dimensions: 200x200 to 400x400 pixels for display
- File size: Under 100KB per image for web performance

#### Step 4b: Trim Excess Padding from Mascot Images

AI image generators frequently add excessive transparent padding around mascot images, which makes the mascot appear too small when displayed at the target CSS size (e.g., 90px). After saving the images, recommend running the padding trimmer on each file:

```bash
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/neutral.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/welcome.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/thinking.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/tip.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/warning.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/celebration.png
python $BK_HOME/src/image-utils/trim-padding-from-image.py docs/img/mascot/encouraging.png
```

This script trims transparent padding to the bounding box of the visible content. It is critical to run this step because untrimmed images display much smaller than intended inside the admonition boxes.

### Step 5: Create the Custom CSS

Create or append to `docs/css/mascot.css`:

```css
/* ============================================
   Learning Mascot: {{CHARACTER_NAME}} the {{SPECIES}}
   Pedagogical agent for {{SUBJECT}}
   ============================================ */

:root {
  --mascot-primary:   {{PRIMARY_COLOR}};   /* e.g., #2e7d32 forest green  */
  --mascot-secondary: {{SECONDARY_COLOR}}; /* e.g., #795548 warm brown    */
  --mascot-bg:        {{BG_COLOR}};        /* e.g., #e8f5e9 light green   */
  --mascot-border:    {{BORDER_COLOR}};    /* e.g., #43a047 medium green  */
  --mascot-size: 90px;
}

/* ---- Shared base for all mascot admonitions ---- */
/* Override MkDocs Material's default smaller admonition font size
   so mascot admonition text matches the body text exactly. */
.md-typeset .admonition.mascot-welcome,
.md-typeset .admonition.mascot-thinking,
.md-typeset .admonition.mascot-tip,
.md-typeset .admonition.mascot-warning,
.md-typeset .admonition.mascot-celebration,
.md-typeset .admonition.mascot-encourage,
.md-typeset .admonition.mascot-neutral,
.md-typeset details.mascot-welcome,
.md-typeset details.mascot-thinking,
.md-typeset details.mascot-tip,
.md-typeset details.mascot-warning,
.md-typeset details.mascot-celebration,
.md-typeset details.mascot-encourage,
.md-typeset details.mascot-neutral {
  font-size: inherit;
}

/* ---- Welcome (chapter openings) — primary color ---- */
.md-typeset .admonition.mascot-welcome,
.md-typeset details.mascot-welcome {
  border-color: var(--mascot-primary);
  background-color: var(--mascot-bg);
}
.md-typeset .mascot-welcome > .admonition-title,
.md-typeset .mascot-welcome > summary {
  background-color: var(--mascot-primary);
  color: white;
}

/* ---- Thinking (key concepts) — secondary color ---- */
.md-typeset .admonition.mascot-thinking,
.md-typeset details.mascot-thinking {
  border-color: var(--mascot-secondary);
  background-color: #efebe9;
}
.md-typeset .mascot-thinking > .admonition-title,
.md-typeset .mascot-thinking > summary {
  background-color: var(--mascot-secondary);
  color: white;
}

/* ---- Tip (hints) — teal ---- */
.md-typeset .admonition.mascot-tip,
.md-typeset details.mascot-tip {
  border-color: #00897b;
  background-color: #e0f2f1;
}
.md-typeset .mascot-tip > .admonition-title,
.md-typeset .mascot-tip > summary {
  background-color: #00897b;
  color: white;
}

/* ---- Warning (common mistakes) — red ---- */
.md-typeset .admonition.mascot-warning,
.md-typeset details.mascot-warning {
  border-color: #c62828;
  background-color: #ffebee;
}
.md-typeset .mascot-warning > .admonition-title,
.md-typeset .mascot-warning > summary {
  background-color: #c62828;
  color: white;
}

/* ---- Celebration (achievements) — deep purple so pale confetti sparkles pop ---- */
/* NOTE: celebration poses typically contain pale gold/white confetti that
   vanishes against light backgrounds. Keep the body dark and flip text
   color to light. See "Contrast-check each pose image" below. */
.md-typeset .admonition.mascot-celebration,
.md-typeset details.mascot-celebration {
  border-color: #4a148c;
  background-color: #311b4f;
  color: #f3e5f5;
}
.md-typeset .mascot-celebration > .admonition-title,
.md-typeset .mascot-celebration > summary {
  background-color: #4a148c;
  color: white;
}

/* ---- Encourage (difficult content) — blue ---- */
.md-typeset .admonition.mascot-encourage,
.md-typeset details.mascot-encourage {
  border-color: #0277bd;
  background-color: #e1f5fe;
}
.md-typeset .mascot-encourage > .admonition-title,
.md-typeset .mascot-encourage > summary {
  background-color: #0277bd;
  color: white;
}

/* ---- Neutral (general purpose) — slate gray ---- */
.md-typeset .admonition.mascot-neutral,
.md-typeset details.mascot-neutral {
  border-color: #546e7a;
  background-color: #eceff1;
}
.md-typeset .mascot-neutral > .admonition-title,
.md-typeset .mascot-neutral > summary {
  background-color: #546e7a;
  color: white;
}

/* ---- Title: left-align text, remove default MkDocs icon completely ---- */
.md-typeset [class*="mascot-"] > .admonition-title,
.md-typeset [class*="mascot-"] > summary {
  text-align: left;
  padding-left: 0.8rem;
}
.md-typeset [class*="mascot-"] > .admonition-title::before,
.md-typeset [class*="mascot-"] > summary::before {
  display: none;
}

/* ---- Mascot image floated LEFT of admonition body text ---- */
.mascot-admonition-img {
  float: left;
  width: var(--mascot-size);
  height: var(--mascot-size);
  /* margin: top right bottom left */
  margin: 0 .5em 0 0;
  object-fit: contain;
}
```

**IMPORTANT design rules:**

- **Never** put mascot icons in the admonition title bar (no `::before` pseudo-elements with mascot images)
- **Always** place mascot images in the admonition body using `<img class="mascot-admonition-img">`
- The title bar is clean text only — the default MkDocs icon is hidden via `display: none`
- **Contrast-check each pose image against its admonition background before finalizing colors.** Open the PNG and look for fine pale details — confetti sparkles, glow, LED highlights, thin white outlines. If the pose has pale elements (the celebration pose almost always does), the admonition background must be dark enough that those details remain visible; flip the body text color to a light shade to compensate. If the pose is mostly dark or saturated, a light pastel background is fine. The celebration CSS block above is the canonical example of the dark-background treatment.

#### Step 5b: Register the CSS in mkdocs.yml

Add the stylesheet to `mkdocs.yml`:

```yaml
extra_css:
  - css/mascot.css
```

Also ensure the custom admonition types are registered:

```yaml
markdown_extensions:
  - admonition
  - md_in_html
  - pymdownx.details
  - pymdownx.superfences
  - attr_list
```

### Step 6: Usage in Chapter Markdown

Authors use standard admonition syntax with the custom types. The mascot image is placed as an `<img>` tag floated left inside the admonition body (requires `md_in_html` extension):

**IMPORTANT: Image paths** — The `<img>` `src` path is relative to the rendered page URL, not the markdown file. Because MkDocs uses directory URLs (e.g., `chapters/01-intro/` renders as `chapters/01-intro/index.html`), you must count directories from the page to `docs/img/mascot/`. For a chapter page at `chapters/01-intro/index.md`, use `../../img/mascot/`. For a page at `learning-graph/mascot-test.md`, use `../../img/mascot/`.

```markdown
!!! mascot-neutral "A Note from {{CHARACTER_NAME}}"
    <img src="../../img/mascot/neutral.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} neutral pose">
    Use this for general sidebars, introductions, or any content
    that doesn't call for a specific emotional tone.

!!! mascot-welcome "Welcome!"
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} waving welcome">
    In this chapter, we'll discover how to solve equations
    of the form ax² + bx + c = 0. Get ready for some
    powerful mathematical tools!

!!! mascot-thinking "Key Insight"
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} thinking">
    Notice that every quadratic equation has at most two
    solutions. This connects directly to the degree of the
    polynomial!

!!! mascot-tip "{{CHARACTER_NAME}}'s Tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} giving a tip">
    Always check your answers by substituting back into
    the original equation. It only takes a moment and
    catches most errors!

!!! mascot-warning "Common Mistake"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} warning">
    Don't forget to account for the negative sign when
    using the quadratic formula. The ± means you need
    to solve BOTH cases!

!!! mascot-encourage "You Can Do This!"
    <img src="../../img/mascot/encouraging.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} encouraging">
    Factoring can feel tricky at first. That's completely
    normal! With practice, you'll start seeing patterns
    everywhere.

!!! mascot-celebration "Great Progress!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} celebrating">
    You've now mastered the quadratic formula! This is
    one of the most important tools in all of algebra.
```

### Step 7: Add Character Guidelines to CLAUDE.md

To ensure consistent mascot usage across AI-generated content, add a section to the project's `CLAUDE.md`:

```markdown
## Learning Mascot: {{CHARACTER_NAME}} the {{SPECIES}}

### Character Overview

- **Name**: {{CHARACTER_NAME}}
- **Species**: {{SPECIES}}
- **Personality**: {{TRAIT_1}}, {{TRAIT_2}}, {{TRAIT_3}}, {{TRAIT_4}}
- **Catchphrase**: "{{CATCHPHRASE}}"
- **Visual**: {{BRIEF_APPEARANCE_DESCRIPTION}}

### Voice Characteristics

- {{VOICE_TRAIT_1}} (e.g., "Uses simple, encouraging language")
- {{VOICE_TRAIT_2}} (e.g., "Occasionally uses subject-specific puns")
- {{VOICE_TRAIT_3}} (e.g., "Refers to students as 'explorers' or 'investigators'")
- Signature phrases: "{{PHRASE_1}}", "{{PHRASE_2}}", "{{PHRASE_3}}"

### Mascot Admonition Format

Always place mascot images in the admonition body, never in the title bar:

    !!! mascot-welcome "Title Here"
        <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} waving welcome">
        Admonition text goes here after the img tag.

### Placement Rules

| Context | Admonition Type | Frequency |
|---------|----------------|-----------|
| General note / sidebar | mascot-neutral | As needed |
| Chapter opening | mascot-welcome | Every chapter |
| Key concept | mascot-thinking | 2-3 per chapter |
| Helpful tip | mascot-tip | As needed |
| Common mistake | mascot-warning | As needed |
| Difficult content | mascot-encourage | Where students may struggle |
| Section completion | mascot-celebration | End of major sections |

### Do's and Don'ts

**Do:**

- Use {{CHARACTER_NAME}} to introduce new topics warmly
- Include the catchphrase in welcome admonitions
- Keep dialogue brief (1-3 sentences)
- Match the pose/image to the content type

**Don't:**

- Use {{CHARACTER_NAME}} more than 5-6 times per chapter
- Put mascot admonitions back-to-back
- Use the mascot for purely decorative purposes
- Change {{CHARACTER_NAME}}'s personality or speech patterns
```

### Step 8: Verify the Implementation

After setup, verify the mascot works correctly:

```bash
mkdocs serve
```

Check the following:

1. Mascot images load correctly (no broken images)
2. Admonition styling appears as expected
3. Colors match the book's theme
4. Images are appropriately sized (not too large or small)
5. Text wrapping around images looks clean
6. Mobile/responsive layout works

### Step 9: Create a Mascot Rendering Test Page

Create `docs/learning-graph/mascot-test.md` to preview all mascot variants
by running unix shell script:

```sh
../scripts/render-mascot-test.sh {MASCOT_NAME}
```

**IMPORTANT:** Adjust the `src` path based on the page's depth. For a page at `learning-graph/mascot-test.md` (which renders at `learning-graph/mascot-test/index.html`), use `../../img/mascot/`.

This program will copy the mascot-test.md file from the template here:

[Mascot Render Test Template](./assets/templates/docs/learning-graph/mascot-render-test.md)

Remind the user that if there is excessive padding around the images that we can
run the following `Trim Padding From Image` python program:

```sh
../scripts/trim-padding-from-image.py docs/img/mascot/FILENAME.png
```

Note that the exact path to the image must be given to the script as the first parameter.

Here is what is a example of what is in this test file:

```markdown
# Mascot Style Guide

This page shows all mascot admonition styles for reference.

!!! mascot-neutral "General Note"
    <img src="../../img/mascot/neutral.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} neutral pose">
    This is the neutral style, used for general sidebars or introductions.

!!! mascot-welcome "Welcome!"
    <img src="../../img/mascot/welcome.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} waving welcome">
    This is the welcome style, used at chapter openings.

!!! mascot-thinking "Key Insight"
    <img src="../../img/mascot/thinking.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} thinking">
    This is the thinking style, used for key concepts.

!!! mascot-tip "Helpful Tip"
    <img src="../../img/mascot/tip.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} giving a tip">
    This is the tip style, used for hints and advice.

!!! mascot-warning "Watch Out!"
    <img src="../../img/mascot/warning.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} warning">
    This is the warning style, used for common mistakes.

!!! mascot-celebration "Well Done!"
    <img src="../../img/mascot/celebration.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} celebrating">
    This is the celebration style, used for achievements.

!!! mascot-encourage "Keep Going!"
    <img src="../../img/mascot/encouraging.png" class="mascot-admonition-img" alt="{{CHARACTER_NAME}} encouraging">
    This is the encouraging style, used for difficult content.
```

There is also additional code to view the border of the images.

**Note:** Place the test file in the `docs/learning-graph/` directory alongside the other learning graph assets. Include this page in the navigation unless the user requests that it is not
displayed.  If they do not want it display then add it to the exclude_docs section in the mkdocs.yml

```yml
exclude_docs: |
  docs/learning-graph/mascot-test.md
```

## Quick Reference

### File Structure

```
docs/
├── img/
│   └── mascot/
│       ├── image-prompts.md
│       ├── neutral.png
│       ├── welcome.png
│       ├── thinking.png
│       ├── tip.png
│       ├── warning.png
│       ├── encouraging.png
│       └── celebration.png
├── css/
│   └── mascot.css
└── learning-graph/
    └── mascot-test.md          # Mascot rendering test page
```

### Admonition Types

| Type | Usage | Title Bar Color |
|------|-------|-----------------|
| `mascot-neutral` | General sidebars / default | Slate gray |
| `mascot-welcome` | Chapter openings | Primary color |
| `mascot-thinking` | Key concepts | Secondary color |
| `mascot-tip` | Tips and hints | Teal |
| `mascot-warning` | Warnings | Red |
| `mascot-encourage` | Difficult content | Blue |
| `mascot-celebration` | Achievements | Purple |

### Mascot Image Placement Pattern

**Always** use this pattern — image in the body, never put the image in the title:

```markdown
!!! mascot-TYPE "Title Text"
    <img src="PATH/TO/mascot/POSE.png" class="mascot-admonition-img" alt="Description">
    Body text goes here after the img tag.
```

## Troubleshooting

### Images Not Loading

1. Verify images exist in `docs/img/mascot/`
2. Check file names match exactly (case-sensitive)
3. Verify `src` path depth — count directories from the rendered page URL to `docs/img/mascot/`
4. For a page at `chapters/01-intro/index.md`, use `../../img/mascot/`
5. For a page at `learning-graph/mascot-test.md`, use `../../img/mascot/`

### Admonition Styles Not Appearing

1. Verify `css/mascot.css` is listed in `extra_css` in mkdocs.yml
2. Check browser dev tools for CSS loading errors
3. Ensure admonition type matches exactly (e.g., `mascot-welcome`, not `mascot_welcome`)
4. Verify `md_in_html` is in `markdown_extensions` (required for `<img>` tags inside admonitions)
5. Clear browser cache and rebuild: `mkdocs build --clean`

### Mascot Images Too Large/Small

- Adjust `--mascot-size` CSS variable in the `:root` section of `mascot.css`
- Default is 90px, which works well for most layouts

### Colors Don't Match Book Theme

1. Update CSS variables in `:root` section of `mascot.css`
2. Use your book's primary/secondary colors from mkdocs.yml palette
3. Use a color contrast checker to ensure text readability

### Too Much Padding Around Image

If the users says that there is too much padding around the icons, then run the `Trim Padding From Image` python program:

```sh
../scripts/trim-padding-from-image.py docs/img/mascot/FILENAME.png
```

## Related Skills

- `home-page-template.md` - Create home page with cover image
- `mkdocs-features.md` - Add admonitions and other features
- `cover-image-generator.md` - Generate AI images for book cover
