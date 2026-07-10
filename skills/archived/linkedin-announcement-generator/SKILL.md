---
name: linkedin-announcement-generator
description: Generates a LinkedIn post announcing an intelligent textbook milestone by pulling book metrics, chapter count, and key statistics. Use when announcing textbook completion or major content milestones on social media.
license: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
model: sonnet
---

# LinkedIn Announcement Generator

## Overview

This skill automates the creation of professional LinkedIn announcements for intelligent textbooks. It analyzes book metrics from the `docs/learning-graph/` directory, gathers statistics about chapters, concepts, and educational resources, and generates engaging announcement text with relevant hashtags and links to the published site.

The announcements are designed to highlight the scope and completeness of the textbook, showcase its educational features, and attract educators, students, and learning professionals to the content.

## When to Use This Skill

Use this skill when:

- Publishing a completed intelligent textbook to GitHub Pages
- Announcing major milestones (e.g., "First 10 chapters complete!")
- Promoting updated or newly added content
- Sharing the textbook with the educational technology community
- Preparing social media posts for course launches
- Creating announcements for conference presentations or workshops
- Building awareness for open educational resources

## Prerequisites

The intelligent textbook project should have:

- A `docs/learning-graph/book-metrics.json` file containing the canonical
  textbook statistics (produced by the book-metrics tool). If it is missing,
  generate it first with `bk-generate-book-metrics` (or the
  `python3 "$BK_HOME/src/book-metrics/book-metrics.py" docs` fallback).
- A `mkdocs.yml` file with site_name, site_url, and site_description
- Deployed site on GitHub Pages (or another hosting platform)
- Optional: `docs/learning-graph/chapter-metrics.md` for chapter-level details
- Optional: `docs/course-description.md` for audience and topic information

## Workflow

### Step 1: Gather Book Metadata

Extract key information from the project configuration:

1. Read `mkdocs.yml` to get:
   - `site_name` - Title of the textbook
   - `site_url` - Live site URL (typically GitHub Pages)
   - `site_description` - Brief description of the textbook
   - `repo_url` - GitHub repository URL

2. Read `docs/course-description.md` (if it exists) to get:
   - Target audience (grade level, prerequisites)
   - Subject matter/topic
   - Learning objectives
   - Course context

**Example extraction:**

```yaml
site_name: 'Geometry for High School Students'
site_url: 'https://username.github.io/geometry-course/'
site_description: 'An interactive geometry textbook with MicroSims and quizzes'
```

### Step 2: Analyze Book Metrics

Read the canonical metrics file `docs/learning-graph/book-metrics.json` — do
**not** parse the human-readable `book-metrics.md` table (brittle) or recount
content yourself. This is the same source the README and case-study skills use,
so the numbers stay consistent across every artifact.

```bash
python3 - <<'PY'
import json, pathlib, sys
p = pathlib.Path("docs/learning-graph/book-metrics.json")
if not p.exists():
    sys.exit("book-metrics.json missing — run bk-generate-book-metrics first")
m = json.loads(p.read_text())["metrics"]
print(json.dumps(m, indent=2))
PY
```

**Core Metrics (keys in the `metrics` object):**

- `chapters` — Number of chapters
- `concepts` — Number of concepts in the learning graph
- `glossaryTerms` — Number of glossary terms
- `faqs` — Number of FAQ questions
- `quizQuestions` — Number of quiz questions
- `diagrams` — Number of diagrams
- `equations` — Number of equations
- `microsims` — Number of MicroSims (interactive simulations)
- `words` — Total word count
- `links` — Number of hyperlinks
- `equivalentPages` — Equivalent printed pages
- `developmentStage` — Author-declared publication stage

If `book-metrics.json` does not exist, regenerate it with
`bk-generate-book-metrics` before reading. The format is defined by
`src/book-metrics/book-metrics.schema.json`.

**Handle missing metrics gracefully:**

- If diagrams = 0, mention "includes equations and visual elements" instead
- If quiz questions = 0, omit quiz mention
- If MicroSims = 0, mention "comprehensive content" instead

### Step 3: Determine Textbook Completeness

Calculate the completion status based on metrics:

**Indicators of completeness:**

- Chapters ≥ 8: Substantial textbook
- Total words > 30,000: Comprehensive content
- Quiz questions ≥ 50: Well-assessed
- MicroSims ≥ 5: Interactive elements present
- Equivalent pages > 100: Book-length work

**Status categories:**

- **Complete** (100%): All major components present, ready for use
- **Nearly Complete** (90-99%): Most content done, minor additions pending
- **In Progress** (70-89%): Substantial content, ongoing development
- **Early Release** (< 70%): Initial chapters available, more coming

Choose appropriate language for the announcement based on status.

### Step 4: Craft the Announcement Structure

Create a LinkedIn post with the following components:

**1. Opening Hook (1-2 sentences)**

Start with an attention-grabbing statement that:
- Announces the textbook completion/release
- Mentions the topic and audience
- Highlights what makes it special

**Examples:**

- "Excited to share a new open educational resource for [AUDIENCE]!"
- "Just published: An AI-generated interactive textbook on [TOPIC]!"
- "Thrilled to announce the completion of [TEXTBOOK NAME]!"

**2. Content Description (2-3 sentences)**

Explain what the textbook covers and its unique features:
- Educational framework (Bloom's Taxonomy, concept dependencies)
- Interactive elements (MicroSims, quizzes)
- Technology stack (MkDocs, p5.js, AI-generated)
- Target audience and prerequisites

**Example:**

```
This intelligent textbook on [TOPIC] is designed for [AUDIENCE]. Built using MkDocs Material and AI-assisted content generation, it incorporates learning graphs, concept dependencies, and interactive MicroSims to make [TOPIC] accessible and engaging.
```

**3. Key Metrics (bulleted list)**

Present impressive statistics to demonstrate scope:

```
📊 By the numbers:
• [X] chapters covering [TOPIC AREAS]
• [Y] concepts in the learning graph
• [Z] interactive MicroSims (p5.js simulations)
• [Q] quiz questions for self-assessment
• [G] glossary terms with ISO 11179-compliant definitions
• [W] total words (~[P] equivalent printed pages)
```

**Formatting tips:**

- Use emoji bullets (📊, 📚, 🎓, ⚡, 🔬) for visual appeal
- Round large numbers (225,182 → 225,000)
- Group related metrics together
- Highlight the most impressive numbers

**4. Technology and AI Disclosure (1-2 sentences)**

Be transparent about AI involvement and technology:

```
Generated using Claude AI skills and the intelligent textbook framework, this open-source project demonstrates how AI can augment educational content creation while maintaining quality and pedagogical rigor.
```

**5. Call to Action (1 sentence)**

Direct readers to the site — but **never put the URL in the post body**.

**The "link in the first comment" rule:** research shows LinkedIn's algorithm
significantly reduces the reach of posts that contain external links in the
post body. Instead, tell readers the link is in the comments, and provide the
URL as a separate first-comment text the user pastes immediately after
publishing:

```
🔗 Link to the full textbook is in the first comment below! 👇
```

Always generate the first-comment text along with the post:

```
Explore the full textbook here: [SITE_URL]
```

This rule applies to ALL external links (site URL, GitHub repo, blog posts) —
none of them belong in the post body.

**6. Hashtags (8-15 tags)**

Include relevant hashtags for discoverability:

**Standard hashtags:**

- `#AI` / `#ArtificialIntelligence`
- `#GenAI` / `#GenerativeAI`
- `#Education` / `#EdTech` / `#EducationalTechnology`
- `#OpenEducation` / `#OER` (Open Educational Resources)
- `#ELearning` / `#OnlineLearning`

**Content-specific hashtags:**

- `#Textbook` / `#InteractiveTextbook`
- `#MicroSims` / `#Simulations`
- `#Visualizations` / `#DataViz`
- `#Diagrams` / `#Infographics`
- `#Quizzes` / `#Assessment`

**Technology-specific hashtags:**

- `#MkDocs` / `#MaterialDesign`
- `#p5js` / `#JavaScript`
- `#Python`
- `#ClaudeAI` / `#AnthropicClaude`

**Domain-specific hashtags:**

Add 2-4 hashtags specific to the subject matter:
- Math: `#Mathematics`, `#Geometry`, `#Calculus`, `#Algebra`
- Science: `#Physics`, `#Chemistry`, `#Biology`
- CS: `#Programming`, `#ComputerScience`, `#DataScience`
- History: `#History`, `#WorldHistory`, `#AmericanHistory`

**Professional/Academic hashtags:**

- `#LMS` / `#LearningManagementSystem`
- `#CurriculumDesign`
- `#InstructionalDesign`
- `#STEM` / `#STEMeducation`
- `#HigherEd` / `#K12Education`

**Total hashtag count:** Aim for 10-15 hashtags for optimal reach.

### Step 5: Apply Tone and Style Guidelines

**LinkedIn voice characteristics:**

- Professional but approachable
- Enthusiastic without being overly promotional
- Educational and informative
- Data-driven (cite specific metrics)
- Transparent about AI involvement
- Community-focused (sharing resources)

**Writing best practices:**

- Use first person ("I'm excited to share...")
- Keep paragraphs short (2-3 lines each)
- Use emoji sparingly (1-3 per post)
- Include line breaks for readability
- Front-load important information
- End with a clear call to action

**Avoid:**

- Overly academic language
- Excessive jargon
- Claims without evidence
- Overly promotional tone
- Clickbait-style hooks
- Too many emojis

### Step 6: Generate Multiple Variations

Create three variations of the announcement:

**Variation 1: Detailed (Full Length)**

- Complete description with all metrics
- 1500-2000 characters
- All hashtags included
- Best for: Initial launch announcement

**Variation 2: Medium (Standard Length)**

- Key metrics only (top 5-6)
- 800-1200 characters
- 10-12 hashtags
- Best for: Progress updates, milestone posts

**Variation 3: Concise (Short Form)**

- Essential info only
- 400-600 characters
- 6-8 hashtags
- Best for: Quick updates, cross-posting to other platforms

Provide all three variations so the user can choose based on their preference.

### Step 7: Add Optional Enhancements

**If available, include:**

**Screenshot or cover image suggestion:**

```
📸 Suggested visual: Screenshot of the learning graph visualization or the textbook home page
```

**Notable features callout:**

If the textbook has unique elements, highlight them:
- "Features interactive p5.js simulations you can run in your browser"
- "Includes concept dependency graphs showing learning pathways"
- "Contains ISO 11179-compliant glossary for precise terminology"

**Collaboration invitation:**

If seeking contributors:
- "Open for contributions! Check out the GitHub repo: [REPO_URL]"
- "Looking for educators to provide feedback. DM me if interested!"

**Related links:**

If applicable (all external links go in the first comment, never the post body):
- Link to GitHub repository (for developers)
- Link to related blog post or article
- Link to presentation slides

### Step 8: Format and Present Output

Present the LinkedIn announcement(s) in a clear, copy-paste ready format:

```markdown
## LinkedIn Announcement - Full Version

[Paste-ready text here]

---

## LinkedIn Announcement - Medium Version

[Paste-ready text here]

---

## LinkedIn Announcement - Concise Version

[Paste-ready text here]

---

## First Comment (paste immediately after publishing)

[Text containing the site URL — external links go here, never in the post body]

---

## Suggested Enhancements

**Visual:** [Description of recommended image/screenshot]

**Timing:** Best posted [weekday, time recommendation]

**Engagement Tips:**
- Tag relevant individuals or organizations if appropriate
- Respond to comments within first 2 hours for algorithm boost
- Consider posting during peak LinkedIn hours (Tuesday-Thursday, 8-10am or 12-2pm)
```

### Step 9: Validate Announcement Quality

Before finalizing, check that the announcement:

- [ ] Post body contains NO external links (LinkedIn cuts reach for posts with links)
- [ ] A separate first-comment text with the live site URL is provided
- [ ] Contains accurate metrics from book-metrics.json
- [ ] Has 10-15 relevant hashtags
- [ ] Mentions AI transparency
- [ ] Includes a clear call to action
- [ ] Is between 400-2000 characters (LinkedIn optimal range)
- [ ] Uses professional, enthusiastic tone
- [ ] Highlights unique or impressive features
- [ ] Is free of typos and grammatical errors
- [ ] Provides value to the educational community

### Step 10: Deliver the Announcement

Output the finalized announcement text(s) ready for the user to:

1. Copy and paste directly into LinkedIn
2. Customize with personal touches if desired
3. Add optional media (screenshots, videos)
4. Schedule or post immediately

Inform the user:

```
✅ LinkedIn announcement generated successfully!

Three variations provided (full, medium, concise) - choose the one that fits your style.

**Next steps:**
1. Copy your preferred version
2. Paste into LinkedIn post composer
3. Add a screenshot of your textbook (optional but recommended)
4. Review and post!
5. Immediately paste the provided first-comment text (with the link) as the first comment

Remember: keep the link OUT of the post body — LinkedIn reduces reach for posts with external links. The link goes in the first comment.

Pro tip: LinkedIn posts with images get 2x more engagement. Consider adding a screenshot of your learning graph or textbook homepage.
```

## Example Output

### Full-Length Announcement Example

```
🎓 Excited to share a new open educational resource: an interactive textbook on Geometry designed for high school students!

This intelligent textbook combines AI-assisted content generation with proven educational frameworks. Built using MkDocs Material, it incorporates learning graphs showing concept dependencies, interactive MicroSims using p5.js, and comprehensive assessment tools to make geometry accessible and engaging.

📊 By the numbers:
• 13 chapters covering points, lines, angles, triangles, polygons, circles, and 3D geometry
• 200 concepts organized in a dependency graph
• 5 interactive MicroSims (p5.js simulations)
• 10 quiz questions for self-assessment
• 22 glossary terms with precise definitions
• 225,000+ words (~900 equivalent printed pages)

Generated using Claude AI skills and the intelligent textbook framework, this open-source project demonstrates how AI can augment educational content creation while maintaining pedagogical quality and rigor.

All content follows Bloom's Taxonomy (2001) for learning outcomes and includes detailed explanations, worked examples, and practice exercises.

🔗 Link to the full textbook is in the first comment below! 👇

#AI #GenAI #GenerativeAI #Education #EdTech #OpenEducation #OER #ELearning #Textbook #InteractiveTextbook #MicroSims #Visualizations #Quizzes #Geometry #Mathematics #MkDocs #ClaudeAI #LMS #CurriculumDesign #STEMeducation
```

### Medium-Length Announcement Example

```
📚 Just published: An AI-generated interactive textbook on Geometry for high school students!

This intelligent textbook uses MkDocs Material, learning graphs, and interactive p5.js MicroSims to make geometry engaging and accessible.

Key features:
• 13 comprehensive chapters
• 200 concepts with dependency mapping
• 5 interactive simulations
• 225,000+ words of content
• Open source and freely available

Built using Claude AI and the intelligent textbook framework - demonstrating how AI can enhance educational content while maintaining quality.

Link in the first comment below! 👇

#AI #GenAI #Education #EdTech #OpenEducation #Textbook #MicroSims #Geometry #Mathematics #ClaudeAI #STEMeducation
```

### Concise Announcement Example

```
🎓 New open educational resource: Interactive Geometry textbook for high school!

✨ 13 chapters | 200 concepts | 5 MicroSims | 225K words

AI-generated using Claude and MkDocs Material. Free and open source.

📖 Link in the first comment!

#Education #EdTech #Geometry #AI #OpenEducation #Textbook
```

### First Comment Example

Paste immediately after publishing (external links live here, not in the post):

```
Explore the full textbook here: https://dmccreary.github.io/claude-skills/

GitHub repo: https://github.com/dmccreary/claude-skills
```

## Customization Options

The skill can be customized to:

**1. Adjust tone:**
- Academic (formal, research-focused)
- Casual (friendly, conversational)
- Promotional (marketing-focused)
- Technical (developer-focused)

**2. Target different audiences:**
- Educators and teachers
- Students and learners
- Instructional designers
- Software developers
- Educational technology leaders

**3. Emphasize different aspects:**
- AI/technology innovation
- Open source/open education
- Interactive elements
- Comprehensive coverage
- Pedagogical approach

**4. Include additional context:**
- Author background
- Development timeline
- Use cases and testimonials
- Research backing
- Awards or recognition

## Supporting Scripts

Metrics come straight from the canonical `book-metrics.json` — no markdown
parsing required. A small helper only needs to load the JSON and the site
config:

**`scripts/linkedin-metrics-extractor.py`**

```python
#!/usr/bin/env python3
"""Load canonical metrics + site config for LinkedIn announcements."""

import json
import yaml

def load_book_metrics(metrics_json="docs/learning-graph/book-metrics.json"):
    """Return the `metrics` dict from the canonical book-metrics.json."""
    with open(metrics_json, encoding="utf-8") as f:
        return json.load(f)["metrics"]

def extract_site_config(mkdocs_file):
    """Parse mkdocs.yml and return site metadata (name, url, description)."""
    # Implementation: Load YAML and extract site_name, site_url, etc.
    pass

def format_number(n):
    """Format numbers for readability (e.g., 225182 -> 225,000)."""
    # Implementation: Round and format large numbers
    pass

# Usage:
# python linkedin-metrics-extractor.py docs/learning-graph/book-metrics.json mkdocs.yml
```

## Quality Standards

A high-quality LinkedIn announcement should:

- Be accurate (all metrics verified)
- Be engaging (compelling hook and narrative)
- Be transparent (acknowledge AI involvement)
- Be professional (appropriate tone for LinkedIn)
- Be actionable (clear call to action)
- Be discoverable (relevant hashtags)
- Be concise (under 2000 characters)
- Be valuable (provides useful information to community)

## Troubleshooting

**Issue:** Metrics not found in book-metrics.json

**Solution:** Generate the metrics first — run `bk-generate-book-metrics` (or invoke `book-installer` and request the book-metrics guide) to create the metrics file

**Issue:** Site URL not available

**Solution:** Ask user for the deployed site URL or GitHub Pages link

**Issue:** Announcement too long (> 3000 characters)

**Solution:** Use the medium or concise variation instead

**Issue:** Not sure which hashtags to use

**Solution:** Focus on the subject domain (e.g., #Mathematics for math textbooks) and general education tags

## Related Skills

- **book-installer (book-metrics guide)** / `bk-generate-book-metrics` - Generates the metrics file used by this skill
- **readme-generator** - Creates GitHub README with similar content
- **intelligent-textbook** - The workflow that creates the textbook itself

## Resources

- [LinkedIn Best Practices for Posts](https://www.linkedin.com/help/linkedin/answer/a549970)
- [LinkedIn Character Limits](https://www.linkedin.com/help/linkedin/answer/a521928)
- [Hashtag Strategy Guide](https://www.linkedin.com/business/marketing/blog/content-marketing/hashtag-strategy-guide)
- [Open Educational Resources](https://www.oercommons.org/)
