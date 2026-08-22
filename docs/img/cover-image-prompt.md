# Cover Image Prompt

Please generate a professional-quality cover image for this textbook.
This image will be used in social media previews and must follow the
formatting guidelines for an Open Graph image preview.

**Required specifications:**

- Format: PNG
- Wide-landscape format
- Size: 1200x630 pixels (1.91:1 aspect ratio)
- This is the Open Graph standard for social media previews

The image has four layers, back to front: background montage, color
treatment, mascot, and title text.

## Subject & Tone

**Agent Skills for Intelligent Textbooks** is a textbook about using portable
AI agent skills — packaged, reusable instruction sets — to build interactive
educational textbooks with learning graphs, glossaries, quizzes, and embedded
simulations. The intended audience is teachers, instructional designers, and
technical authors at an undergraduate reading level.

The visual tone should be **modern, technical, and warm** — a builder's
toolkit rather than a research lab. The book's thesis is that authoring an
intelligent textbook is craft work with good tools, so the cover should feel
capable and inviting, not futuristic or corporate.

**This cover must be vendor-neutral.** The skills documented in this book run
on Claude, OpenAI Codex, Google Antigravity, Gemini, and Cursor alike. The
cover must not favor or reference any one AI company. See the Avoid section —
this is the single most important constraint on this image.

## Title

Place **Agent Skills for Intelligent Textbooks** in the center of the image,
in a clean, highly legible sans-serif font. Use a white font color with a
subtle dark scrim behind it so it stays readable against the montage.

Set "Agent Skills" on the first line at the largest size, and "for Intelligent
Textbooks" on a second line at roughly 60% of that size. Keep generous
negative space immediately behind both lines — simplify or blur the montage
directly behind the text rather than shrinking the type.

## Background Montage

Arrange a montage of the following 8 elements around the title, each rendered
in a consistent flat-vector illustration style (see Style below) so the
composition reads as one image rather than a collage. Each element is a real
artifact from this book — reference screenshots are listed for accuracy.

1. **Learning graph** — a dense cloud of 60+ small colored ellipse nodes
   connected by thin directed arrows, colored in coral, teal, yellow, pink,
   purple and orange, on a pale field. This is the book's signature visual and
   should be the largest montage element.
   *Reference: `docs/sims/graph-viewer/graph-viewer.png` — use only the graph
   itself, not the surrounding sidebar or its category labels.*
2. **Five levels of textbook intelligence** — an ascending staircase of five
   rounded rectangular blocks stepping up left to right, in orange, yellow,
   green and purple.
   *Reference: `docs/sims/five-levels-of-textbook-intelligence-visual-model/five-levels-of-textbook-intelligence-visual-model.png`*
3. **Bloom's taxonomy** — a six-tier pyramid in red, orange, yellow, green,
   blue and purple bands, from Remember at the base to Create at the apex.
   *Reference: `docs/sims/bloom-s-taxonomy-1956-vs-2001-comparison/bloom-s-taxonomy-1956-vs-2001-comparison.png`*
4. **DAG vs. cycle** — two small side-by-side node graphs: the left one flowing
   cleanly downward with arrows, the right one containing a closed loop marked
   in red to show a forbidden circular dependency.
   *Reference: `docs/sims/dag-vs-cyclic-graph-comparison/dag-vs-cyclic-graph-comparison.png`*
5. **Taxonomy distribution** — a multicolored donut chart of roughly a dozen
   segments.
   *Reference: `docs/sims/taxonomy-distribution-pie/taxonomy-distribution-pie.png`*
6. **Concept-length histogram** — a simple teal bar chart with a clean baseline
   axis, bars rising and falling in a rough bell shape.
   *Reference: `docs/sims/concept-length-histogram/concept-length-histogram.png`*
7. **Interactive simulation** — a smooth sine wave plotted on a light canvas
   with a small slider control beneath it, representing the book's MicroSims.
   *Reference: `docs/sims/sine-function-plot/sine-function-plot.png`*
8. **Skill file** — a single document card showing a small delimited metadata
   block at the top above a few lines of body text, representing a skill
   definition. Keep the text as abstract line-work, not readable characters.
   *Reference: `docs/sims/skill-file-anatomy-diagram/skill-file-anatomy-diagram.png`*

## Mascot

Place the book's mascot, **Kit the Otter**, in the **lower-left corner** of the
image, sized so it does not overlap the title text or run off the canvas edge.
Use the waving welcome pose.

Kit is a small, round sea otter with warm brown fur (`#8d6e63`) and a cream
belly (`#efebe9`), wearing a deep teal (`#00695c`) canvas tool satchel slung
bandolier-style across the chest with three small tool loops and a slate
(`#37474f`) buckle. A smooth grey-blue river stone sits in the satchel's front
pouch. Kit has large round dark eyes, short whiskers, and a warm smile, and is
waving cheerfully with one front paw.

**Reference image:** `docs/img/mascot/welcome.png` — attach this file to the
generation request and match it closely. The canonical description is
`docs/img/mascot/character-sheet.md`.

Kit should read as the friendly guide inviting the reader in, so keep the pose
facing the viewer and the scale large enough that the satchel and stone are
legible at 1200px wide — roughly 25–30% of the image height.

## Style & Composition

- **Illustration style:** flat vector with solid color fills, bold clean
  outlines, and no gradients — matching the mascot's own style so Kit does not
  look pasted onto a different illustration.
- **Color palette:** deep teal and mid-blue as the dominant colors, with amber
  and warm coral as accents. This carries over the existing site palette and
  matches Kit's teal satchel.
- **Lighting/mood:** bright, flat, and optimistic; no dramatic shadows or
  cinematic lighting.
- **Composition:** title centered with clear negative space behind it, the
  eight montage elements arranged in a loose ring around it at varied scales,
  Kit in the lower-left corner, and the busiest montage element (the learning
  graph) placed upper-right to balance Kit's visual weight diagonally.

## Avoid

**Vendor neutrality — the hard constraints:**

- Do not include the word "Claude", "Anthropic", "OpenAI", "GPT", "Gemini",
  "Copilot", "Cursor", or any other AI product or company name anywhere in the
  image. The previous cover of this book read "Anthropic Claude" and is being
  replaced specifically to remove it.
- Do not include any AI company's logo, wordmark, or signature glyph — no
  spark or asterisk marks, no hexagon or swirl emblems, no brand-colored
  gradients standing in for a logo.
- Do not depict humanoid robots or android figures. The previous cover used
  two of them; they read as generic "AI product" imagery and work against this
  book's message that skills are portable authoring tools, not a product.

**General:**

- Do not render dense paragraphs of illegible text anywhere in the image.
- Avoid generic stock-photo cliches — handshakes, isolated lightbulbs, glowing
  brains, circuit-board brains, people pointing at whiteboards.
- Avoid photorealistic human faces.
- Do not let montage elements visually compete with or overlap the title, and
  do not let any element overlap Kit in the lower-left corner.
