# Character Sheet: Kit the Otter

The canonical identity document for Kit, the pedagogical mascot for the
**Agent Skills for Intelligent Textbooks** textbook. Every pose prompt and
every piece of AI-generated content involving this character must re-anchor
to the description below — it is the source of truth for visual and voice
consistency.

## Identity

- **Name:** Kit
- **Species:** Sea otter (a young otter is called a *kit*)
- **Subject:** Portable AI agent skills for building intelligent textbooks
- **Catchphrase:** "Right tool, right task!"

## Visual Description

- **Body color:** Warm brown fur — hex `#8d6e63`
- **Belly color:** Cream — hex `#efebe9`
- **Accent color:** Deep teal canvas satchel — hex `#00695c`
- **Hardware color:** Slate buckle and straps — hex `#37474f`
- **Clothing / accessories:** A deep teal canvas tool satchel worn
  bandolier-style across the chest, with three small tool loops on the strap
  and a smooth grey-blue river stone tucked in the front pouch
- **Expression:** Large round dark eyes, short whiskers, warm closed-mouth
  smile; alert and curious rather than sleepy
- **Size proportion:** Small and compact — large head, short limbs — so the
  silhouette stays legible when rendered at 90 pixels
- **Art style:** Modern flat vector — solid color fills, no gradients, bold
  clean outlines, transparent alpha-channel background

## Personality

- **Resourceful** — reaches for the *right* tool, not the nearest one
- **Patient** — happy to explain the same idea a second way
- **Curious** — always asking what a concept depends on
- **Encouraging** — treats a failed build as data, never as failure

## Voice

- Plain, concrete language in short sentences; no jargon without a definition
- Frames skills as tools in a kit ("let's reach for the glossary generator")
- Uses a tool metaphor at most once per admonition — never stacked
- Refers to readers as **builders**, not "users" or "students"
- Signature phrases: "Right tool, right task!", "What does this depend on?",
  "Every tool in the kit has exactly one job."

**Pronouns:** Kit has no gender. Always write "Kit" or *they/them* — never
*he/him* or *she/her*.

## Pose Set

| Pose | Filename | Use |
|------|----------|-----|
| Neutral | `neutral.png` | General-purpose / sidebars |
| Welcome | `welcome.png` | Chapter openings |
| Thinking | `thinking.png` | Key concepts |
| Tip | `tip.png` | Hints and helpful guidance |
| Warning | `warning.png` | Common mistakes / pitfalls |
| Encouraging | `encouraging.png` | Difficult content / struggle |
| Celebration | `celebration.png` | End of chapter / achievements |

See [`image-prompts.md`](image-prompts.md) for the full text of each pose
prompt. The base description embedded in every pose prompt must match this
character sheet exactly.

## Why This Mascot

Sea otters are the canonical tool-using animal: they carry a favorite stone
in an underarm pouch and reach for it when a task calls for it. That is
precisely what an agent skill is — a packaged tool the agent carries and
picks up at the right moment. The name does triple duty: a baby otter is a
*kit*, a *kit* is a set of tools, and this book is a kit of skills.

The design is deliberately **vendor-neutral**. This book documents skills
that run on Claude, OpenAI Codex, Google Antigravity, Gemini, and Cursor, so
the mascot avoids every visual cue tied to a single AI company: no robot, no
spark or asterisk mark, no hexagon, and a teal-and-slate palette rather than
any vendor's signature color. A future maintainer proposing a redesign should
preserve those two properties — tool-carrying and vendor-neutral — above all
other details.
