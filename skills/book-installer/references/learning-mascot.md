---
name: learning-mascot
description: Guides users through designing a pedagogical agent (learning mascot) for their intelligent textbook, generating AI image prompts, and implementing the mascot using inline images, custom CSS admonitions, or JavaScript auto-detection.
---

# Learning Mascot (Pedagogical Agent)

This skill helps users design and implement a pedagogical agent — a visual mascot character that guides students through their intelligent textbook. Research on the "persona effect" shows that characters improve learner engagement and perception of learning.

## What This Skill Creates

1. **Character Design** - A fully defined mascot persona (name, species, appearance, voice, catchphrase)
2. **AI Image Prompts** - Ready-to-use prompts for generating mascot images in consistent poses
3. **Implementation** - One of three methods for embedding the mascot in the textbook:
   - **Option 1**: Inline markdown images (simplest)
   - **Option 2**: Custom CSS admonitions with mascot icons (recommended)
   - **Option 3**: JavaScript auto-detection of character name/catchphrase (most advanced)
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

The catchphrase serves double duty — it's personality AND a trigger for CSS/JS styling. Suggest options:

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

| Context | Purpose | Frequency |
|---------|---------|-----------|
| Chapter openings | Welcome and preview | Every chapter |
| Key concept introductions | Signal important content | 2-3 per chapter |
| Tips and hints | Offer helpful guidance | As needed |
| Warnings and pitfalls | Alert to common mistakes | As needed |
| Practice exercises | Encourage practice | After each section |
| Chapter summaries | Review and celebrate | Every chapter |
| Difficult concepts | Provide encouragement | Where students struggle |

**IMPORTANT: Restraint Guidelines**

The mascot should NOT appear:

- More than 5-6 times per chapter
- In every single admonition or callout
- In ways that interrupt reading flow
- With excessive dialogue that adds no value

### Step 3: Generate AI Image Prompts

Create a set of prompts for generating consistent mascot images. Generate prompts for these standard poses:

#### Base Character Prompt

This is the core description reused across all poses:

```
A [ART_STYLE] illustration of [NAME] the [SPECIES], a friendly pedagogical mascot
for a [SUBJECT] textbook. [NAME] is [COLOR_DESCRIPTION], wearing [ACCESSORIES].
[NAME] has [EXPRESSION]. The character is [SIZE_DESCRIPTION].
Style: [ART_STYLE], clean lines, transparent or white background,
suitable for embedding in educational content. No text in image.
```

#### Pose Variants

Generate prompts for each of these poses:

**0. Neutral/Default Pose** (general sidebars, introductions, inline use)
```
[BASE_PROMPT] [NAME] stands upright in a relaxed, neutral pose facing the
viewer directly, with a calm and friendly closed-mouth smile. Arms/paws/wings
rest naturally at their sides with no specific gesture. The pose is balanced
and unassuming — suitable as a general-purpose or default illustration.
```

**1. Welcome/Introduction Pose** (chapter openings)
```
[BASE_PROMPT] [NAME] is waving cheerfully with one hand/paw/wing,
facing the viewer with a warm, welcoming expression.
The pose suggests "welcome" and "let's get started."
```

**2. Thinking/Teaching Pose** (key concepts)
```
[BASE_PROMPT] [NAME] has one hand/paw on chin in a thoughtful pose,
with a small lightbulb or thought bubble above their head.
The pose suggests deep thinking and discovery.
```

**3. Pointing/Tip Pose** (tips and hints)
```
[BASE_PROMPT] [NAME] is pointing upward with one finger/paw
as if sharing an important tip. Expression is helpful and knowing.
A small star or sparkle near the pointing gesture.
```

**4. Warning/Caution Pose** (warnings and pitfalls)
```
[BASE_PROMPT] [NAME] holds up both hands/paws in a gentle "stop"
or "be careful" gesture. Expression is concerned but caring.
A small exclamation mark or caution symbol nearby.
```

**5. Celebration Pose** (achievements, chapter completion)
```
[BASE_PROMPT] [NAME] is jumping or raising both arms/paws/wings
in celebration. Expression is joyful and proud.
Small confetti or stars around the character.
```

**6. Encouraging Pose** (difficult sections)
```
[BASE_PROMPT] [NAME] gives a thumbs up (or equivalent gesture)
with a reassuring, supportive smile. The pose radiates confidence
and "you can do it" energy.
```

#### Example: Complete Prompt Set for "Otto the Owl"

```
Base: A flat cartoon illustration of Otto the Owl, a friendly pedagogical
mascot for a mathematics textbook. Otto is a round barn owl with warm
brown and cream feathers, wearing small round glasses and a blue
graduation cap. Otto has large, kind eyes with a gentle smile.
The character is small and compact, suitable for icon-sized display.
Style: modern flat vector, clean lines, white background,
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

Celebration: [Base] Otto spreads both wings wide with joy, eyes
squinted in a big smile. Small confetti falls around him.

Encouraging: [Base] Otto gives a wing thumbs-up with a warm,
reassuring smile.
```

Present the generated prompts to the user and ask them to generate images using their preferred AI image tool. Recommend generating at 512x512 or 1024x1024 pixels, then resizing down for use.

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

Recommended specifications:

- Format: PNG with transparent background (preferred) or WebP
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

### Step 5: Choose Implementation Method

Present the three implementation options to the user:

---

#### Option 1: Inline Markdown Images (Simplest)

**Best for:** Quick setup, minimal customization, few mascot appearances.

**How it works:** Place mascot images directly in markdown content using the `attr_list` extension.

**Prerequisites:** The `attr_list` extension must be enabled in mkdocs.yml:

```yaml
markdown_extensions:
  - attr_list
```

**Usage in chapter markdown:**

```markdown
## Welcome to Chapter 3

![Otto welcomes you](../img/mascot/welcome.png){ width="80" align="left" }

Welcome back! In this chapter, we'll explore the fascinating world of
quadratic equations. Let's dive in!

<div style="clear: both;"></div>

---

### Key Concept: The Quadratic Formula

![Otto is thinking](../img/mascot/thinking.png){ width="60" align="right" }

The quadratic formula is one of the most powerful tools in algebra...

<div style="clear: both;"></div>
```

**Pros:**

- Zero configuration beyond `attr_list`
- Works anywhere in markdown
- No CSS or JavaScript needed

**Cons:**

- Manual image placement every time
- No consistent styling wrapper
- Requires `clear: both` divs to prevent text wrapping issues
- Hard to maintain if mascot images change

---

#### Option 2: Custom CSS Admonitions (Recommended)

**Best for:** Consistent styling, branded callout boxes, moderate customization.

**How it works:** Creates custom admonition types that automatically display the mascot icon in a styled callout box. Authors use standard admonition syntax.

**Step 5a: Create the Custom CSS**

Create or append to `docs/css/mascot.css`:

```css
/* ============================================
   Learning Mascot: {{CHARACTER_NAME}} the {{SPECIES}}
   Custom admonition styles for pedagogical agent
   ============================================ */

/* --- Base mascot admonition --- */
:root {
  --mascot-primary: {{PRIMARY_COLOR}};      /* e.g., #5c6bc0 */
  --mascot-secondary: {{SECONDARY_COLOR}};  /* e.g., #ff7043 */
  --mascot-bg: {{BG_COLOR}};               /* e.g., #e8eaf6 */
  --mascot-border: {{BORDER_COLOR}};       /* e.g., #7986cb */
  --mascot-size: 60px;
}

/* Override MkDocs Material's default smaller admonition font size
   so mascot admonition text matches the body text exactly. */
.md-typeset .admonition.mascot-neutral,
.md-typeset .admonition.mascot-welcome,
.md-typeset .admonition.mascot-thinking,
.md-typeset .admonition.mascot-tip,
.md-typeset .admonition.mascot-warning,
.md-typeset .admonition.mascot-celebration,
.md-typeset .admonition.mascot-encourage,
.md-typeset details.mascot-neutral,
.md-typeset details.mascot-welcome,
.md-typeset details.mascot-thinking,
.md-typeset details.mascot-tip,
.md-typeset details.mascot-warning,
.md-typeset details.mascot-celebration,
.md-typeset details.mascot-encourage {
  font-size: inherit;
}

/* Neutral admonition (general purpose) */
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
.md-typeset .mascot-neutral > .admonition-title::before,
.md-typeset .mascot-neutral > summary::before {
  content: "";
  background: url('../img/mascot/neutral.png') center/contain no-repeat;
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.4em;
}

/* Welcome admonition */
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
.md-typeset .mascot-welcome > .admonition-title::before,
.md-typeset .mascot-welcome > summary::before {
  content: "";
  background: url('../img/mascot/welcome.png') center/contain no-repeat;
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.4em;
}

/* Thinking admonition */
.md-typeset .admonition.mascot-thinking,
.md-typeset details.mascot-thinking {
  border-color: var(--mascot-secondary);
  background-color: #fff3e0;
}
.md-typeset .mascot-thinking > .admonition-title,
.md-typeset .mascot-thinking > summary {
  background-color: var(--mascot-secondary);
  color: white;
}
.md-typeset .mascot-thinking > .admonition-title::before,
.md-typeset .mascot-thinking > summary::before {
  content: "";
  background: url('../img/mascot/thinking.png') center/contain no-repeat;
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.4em;
}

/* Tip admonition */
.md-typeset .admonition.mascot-tip,
.md-typeset details.mascot-tip {
  border-color: #66bb6a;
  background-color: #e8f5e9;
}
.md-typeset .mascot-tip > .admonition-title,
.md-typeset .mascot-tip > summary {
  background-color: #66bb6a;
  color: white;
}
.md-typeset .mascot-tip > .admonition-title::before,
.md-typeset .mascot-tip > summary::before {
  content: "";
  background: url('../img/mascot/tip.png') center/contain no-repeat;
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.4em;
}

/* Warning admonition */
.md-typeset .admonition.mascot-warning,
.md-typeset details.mascot-warning {
  border-color: #ef5350;
  background-color: #ffebee;
}
.md-typeset .mascot-warning > .admonition-title,
.md-typeset .mascot-warning > summary {
  background-color: #ef5350;
  color: white;
}
.md-typeset .mascot-warning > .admonition-title::before,
.md-typeset .mascot-warning > summary::before {
  content: "";
  background: url('../img/mascot/warning.png') center/contain no-repeat;
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.4em;
}

/* Celebration admonition */
.md-typeset .admonition.mascot-celebration,
.md-typeset details.mascot-celebration {
  border-color: #ab47bc;
  background-color: #f3e5f5;
}
.md-typeset .mascot-celebration > .admonition-title,
.md-typeset .mascot-celebration > summary {
  background-color: #ab47bc;
  color: white;
}
.md-typeset .mascot-celebration > .admonition-title::before,
.md-typeset .mascot-celebration > summary::before {
  content: "";
  background: url('../img/mascot/celebration.png') center/contain no-repeat;
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.4em;
}

/* Encouraging admonition */
.md-typeset .admonition.mascot-encourage,
.md-typeset details.mascot-encourage {
  border-color: #29b6f6;
  background-color: #e1f5fe;
}
.md-typeset .mascot-encourage > .admonition-title,
.md-typeset .mascot-encourage > summary {
  background-color: #29b6f6;
  color: white;
}
.md-typeset .mascot-encourage > .admonition-title::before,
.md-typeset .mascot-encourage > summary::before {
  content: "";
  background: url('../img/mascot/encouraging.png') center/contain no-repeat;
  width: 1.2em;
  height: 1.2em;
  display: inline-block;
  vertical-align: middle;
  margin-right: 0.4em;
}

/* --- Mascot image in admonition body (larger, decorative) --- */
.mascot-admonition-img {
  float: right;
  width: var(--mascot-size);
  height: var(--mascot-size);
  margin: 0 0 0.5em 1em;
  object-fit: contain;
}
```

**Step 5b: Register the CSS in mkdocs.yml**

Add the stylesheet to `mkdocs.yml`:

```yaml
extra_css:
  - css/mascot.css
```

Also ensure the custom admonition types are registered:

```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - attr_list
```

**Step 5c: Usage in Chapter Markdown**

Authors use standard admonition syntax with the custom types:

```markdown
!!! mascot-neutral "A Note from {{CHARACTER_NAME}}"

    Use this for general sidebars, introductions, or any content
    that doesn't call for a specific emotional tone.

!!! mascot-welcome "Welcome to Quadratic Equations!"

    In this chapter, we'll discover how to solve equations
    of the form ax² + bx + c = 0. Get ready for some
    powerful mathematical tools!

!!! mascot-thinking "Key Insight"

    Notice that every quadratic equation has at most two
    solutions. This connects directly to the degree of the
    polynomial!

!!! mascot-tip "{{CHARACTER_NAME}}'s Tip"

    Always check your answers by substituting back into
    the original equation. It only takes a moment and
    catches most errors!

!!! mascot-warning "Common Mistake"

    Don't forget to account for the negative sign when
    using the quadratic formula. The ± means you need
    to solve BOTH cases!

!!! mascot-celebration "Great Progress!"

    You've now mastered the quadratic formula! This is
    one of the most important tools in all of algebra.

!!! mascot-encourage "You Can Do This!"

    Factoring can feel tricky at first. That's completely
    normal! With practice, you'll start seeing patterns
    everywhere.
```

**Pros:**

- Consistent, branded appearance
- Authors use simple admonition syntax
- Easy to change styling globally via CSS
- Icons appear automatically in admonition titles

**Cons:**

- Requires CSS setup
- Custom admonition types need registration
- Authors must remember the correct type names

---

#### Option 3: JavaScript Auto-Detection (Most Advanced)

**Best for:** Large projects with many contributors, automatic styling without special syntax, maximum consistency.

**How it works:** A JavaScript file scans all admonitions on page load. When it finds the character's name or catchphrase in an admonition title, it automatically applies mascot styling and adds the character image.

**Step 5a: Create the JavaScript File**

Create `docs/js/mascot.js`:

```javascript
/* ============================================
   Learning Mascot: Auto-Detection Script
   Scans admonitions for character name/catchphrase
   and applies mascot styling automatically.
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {
  // --- Configuration ---
  const MASCOT_CONFIG = {
    name: '{{CHARACTER_NAME}}',
    catchphrases: [
      '{{CATCHPHRASE_1}}',
      '{{CATCHPHRASE_2}}',
      '{{CATCHPHRASE_3}}'
    ],
    images: {
      welcome:     '../img/mascot/welcome.png',
      thinking:    '../img/mascot/thinking.png',
      tip:         '../img/mascot/tip.png',
      warning:     '../img/mascot/warning.png',
      celebration: '../img/mascot/celebration.png',
      encouraging: '../img/mascot/encouraging.png',
      default:     '../img/mascot/welcome.png'
    },
    // Map keywords in title to image variant
    titleKeywords: {
      'welcome':       'welcome',
      'introduction':  'welcome',
      'let\\'s begin':  'welcome',
      'key':           'thinking',
      'insight':       'thinking',
      'think':         'thinking',
      'tip':           'tip',
      'hint':          'tip',
      'remember':      'tip',
      'warning':       'warning',
      'caution':       'warning',
      'mistake':       'warning',
      'careful':       'warning',
      'great':         'celebration',
      'congrat':       'celebration',
      'excellent':     'celebration',
      'well done':     'celebration',
      'you can':       'encouraging',
      'don\\'t give up': 'encouraging',
      'keep going':    'encouraging',
      'practice':      'encouraging'
    },
    cssClass: 'mascot-enhanced',
    borderColor: '{{PRIMARY_COLOR}}',
    bgColor: '{{BG_COLOR}}'
  };

  // --- Detection Logic ---
  function detectMascotAdmonitions() {
    const admonitions = document.querySelectorAll('.admonition, details');

    admonitions.forEach(function(admonition) {
      const titleEl = admonition.querySelector('.admonition-title, summary');
      if (!titleEl) return;

      const titleText = titleEl.textContent.toLowerCase();

      // Check if title contains character name or any catchphrase
      const nameMatch = titleText.includes(MASCOT_CONFIG.name.toLowerCase());
      const catchphraseMatch = MASCOT_CONFIG.catchphrases.some(function(phrase) {
        return titleText.includes(phrase.toLowerCase());
      });

      if (nameMatch || catchphraseMatch) {
        applyMascotStyling(admonition, titleText);
      }
    });
  }

  function applyMascotStyling(admonition, titleText) {
    // Prevent double-processing
    if (admonition.classList.contains(MASCOT_CONFIG.cssClass)) return;
    admonition.classList.add(MASCOT_CONFIG.cssClass);

    // Determine which image variant to use
    var imageVariant = 'default';
    var keywords = Object.keys(MASCOT_CONFIG.titleKeywords);
    for (var i = 0; i < keywords.length; i++) {
      if (titleText.includes(keywords[i])) {
        imageVariant = MASCOT_CONFIG.titleKeywords[keywords[i]];
        break;
      }
    }

    // Apply border and background styling
    admonition.style.borderLeftColor = MASCOT_CONFIG.borderColor;
    admonition.style.backgroundColor = MASCOT_CONFIG.bgColor;

    // Add mascot image to the admonition body
    var body = admonition.querySelector('.admonition-title ~ *, summary ~ *');
    if (body) {
      var imgPath = MASCOT_CONFIG.images[imageVariant];
      // Resolve path relative to site root
      var basePath = document.querySelector('meta[name="base_url"]');
      if (basePath) {
        imgPath = basePath.content + '/img/mascot/' + imageVariant + '.png';
      } else {
        // Fallback: use relative path from site root
        imgPath = '/img/mascot/' + imageVariant + '.png';
      }

      var img = document.createElement('img');
      img.src = imgPath;
      img.alt = MASCOT_CONFIG.name;
      img.className = 'mascot-auto-img';
      img.style.cssText = 'float:right;width:60px;height:60px;margin:0 0 0.5em 1em;object-fit:contain;';
      body.parentNode.insertBefore(img, body);
    }
  }

  // Run detection
  detectMascotAdmonitions();

  // Re-run on MkDocs instant navigation (Material theme)
  if (typeof document$ !== 'undefined') {
    document$.subscribe(function() {
      detectMascotAdmonitions();
    });
  }
});
```

**Step 5b: Register the JavaScript in mkdocs.yml**

```yaml
extra_javascript:
  - js/mascot.js
```

**Step 5c: Usage in Chapter Markdown**

Authors write standard admonitions — no special types needed. Just include the character's name or catchphrase in the title:

```markdown
!!! note "Otto Says: Let's Figure This Out!"

    The quadratic formula might look intimidating, but
    we'll break it down step by step.

!!! tip "Otto's Tip: Check Your Work"

    Always substitute your answers back into the original
    equation to verify they're correct.

!!! warning "Otto's Warning: Watch the Signs!"

    The most common mistake with the quadratic formula
    is mishandling the ± sign. Be careful!

!!! success "Otto Says: Great Progress!"

    You've mastered factoring! This skill will serve you
    well throughout algebra and beyond.
```

The JavaScript detects "Otto" in the titles and automatically adds the mascot image and styling.

**Pros:**

- Authors use standard admonition syntax
- No custom CSS types to remember
- Automatic — just mention the character name
- Works with existing content (add character name to titles)

**Cons:**

- Requires JavaScript (may not work in all environments)
- Slight page load overhead
- Harder to debug styling issues
- Relies on name/catchphrase matching (could have false positives)

---

### Step 6: Add Character Guidelines to CLAUDE.md

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

### Placement Rules

| Context | Admonition Type | Frequency |
|---------|----------------|-----------|
| General note / sidebar | mascot-neutral | As needed |
| Chapter opening | mascot-welcome | Every chapter |
| Key concept | mascot-thinking | 2-3 per chapter |
| Helpful tip | mascot-tip | As needed |
| Common mistake | mascot-warning | As needed |
| Section completion | mascot-celebration | End of major sections |
| Difficult content | mascot-encourage | Where students may struggle |

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

### Step 7: Verify the Implementation

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

### Step 8: Create a Test Page (Optional)

Create `docs/learning-graph/mascot-test.md` to preview all mascot variants:

```markdown
# Mascot Style Guide

This page shows all mascot admonition styles for reference.

!!! mascot-neutral "General Note"
    This is the neutral style, used for general sidebars or introductions.

!!! mascot-welcome "Welcome!"
    This is the welcome style, used at chapter openings.

!!! mascot-thinking "Key Insight"
    This is the thinking style, used for key concepts.

!!! mascot-tip "Helpful Tip"
    This is the tip style, used for hints and advice.

!!! mascot-warning "Watch Out!"
    This is the warning style, used for common mistakes.

!!! mascot-celebration "Well Done!"
    This is the celebration style, used for achievements.

!!! mascot-encourage "Keep Going!"
    This is the encouraging style, used for difficult content.
```

**Note:** Place this file in the `docs/learning-graph/` directory alongside the other learning graph assets. You may want to exclude this page from the final navigation or keep it as a contributor reference.

## Quick Reference

### File Structure

```
docs/
├── img/
│   └── mascot/
│       ├── neutral.png
│       ├── welcome.png
│       ├── thinking.png
│       ├── tip.png
│       ├── warning.png
│       ├── celebration.png
│       └── encouraging.png
├── css/
│   └── mascot.css              # Option 2 only
├── js/
│   └── mascot.js               # Option 3 only
└── learning-graph/
    └── mascot-test.md          # Optional test page
```

### Implementation Comparison

| Feature | Option 1: Inline | Option 2: CSS Admonitions | Option 3: JS Detection |
|---------|------------------|---------------------------|------------------------|
| Setup complexity | None | Medium | Medium-High |
| Author effort | High (manual placement) | Low (use admonition type) | Lowest (just use name) |
| Consistency | Low | High | High |
| Customization | Per-instance | Global via CSS | Global via JS config |
| Works without JS | Yes | Yes | No |
| Maintenance | Hard | Easy | Easy |
| **Best for** | Small projects | Most projects | Large multi-author projects |

### Admonition Types (Option 2)

| Type | Usage | Color |
|------|-------|-------|
| `mascot-neutral` | General sidebars / default | Slate gray |
| `mascot-welcome` | Chapter openings | Primary color |
| `mascot-thinking` | Key concepts | Secondary color |
| `mascot-tip` | Tips and hints | Green |
| `mascot-warning` | Warnings | Red |
| `mascot-celebration` | Achievements | Purple |
| `mascot-encourage` | Difficult content | Blue |

## Troubleshooting

### Images Not Loading

1. Verify images exist in `docs/img/mascot/`
2. Check file names match exactly (case-sensitive)
3. Ensure image paths in CSS use correct relative paths (`../img/mascot/`)
4. For Option 3, check the JavaScript console for path errors

### Admonition Styles Not Appearing (Option 2)

1. Verify `css/mascot.css` is listed in `extra_css` in mkdocs.yml
2. Check browser dev tools for CSS loading errors
3. Ensure admonition type matches exactly (e.g., `mascot-welcome`, not `mascot_welcome`)
4. Clear browser cache and rebuild: `mkdocs build --clean`

### JavaScript Not Triggering (Option 3)

1. Verify `js/mascot.js` is listed in `extra_javascript` in mkdocs.yml
2. Check browser console for JavaScript errors
3. Ensure character name in config matches what's used in titles
4. Test with `document.querySelectorAll('.admonition')` in browser console

### Mascot Images Too Large/Small

- Adjust `--mascot-size` CSS variable (Option 2)
- Modify the `width` and `height` in inline styles (Option 1)
- Change the `style.cssText` dimensions in mascot.js (Option 3)

### Colors Don't Match Book Theme

1. Update CSS variables in `:root` section of `mascot.css`
2. Use your book's primary/secondary colors from mkdocs.yml palette
3. Use a color contrast checker to ensure text readability

## Related Skills

- `home-page-template.md` - Create home page with cover image
- `mkdocs-features.md` - Add admonitions and other features
- `cover-image-generator.md` - Generate AI images for book cover
