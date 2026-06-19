---
name: press-release-generator
description: Generates a professional, AP-style press release announcing an intelligent textbook, course, or major content milestone — inverted-pyramid structure with a real news hook, dateline, headline, lead, attributed quotes, an "About" boilerplate, a media-contact block, and the ### end mark. Reuses the book-metrics extraction pattern (docs/learning-graph/book-metrics.json + mkdocs.yml + docs/course-description.md) but produces a formal release for newsrooms and advocacy press rather than a social-media post. Use this skill whenever the user asks for a press release, news release, media release, media advisory, press statement, or "announcement for the press/media," or says they want to pitch a textbook to journalists, local newspapers, education trade press, or an advocacy newsletter — even if they don't say the exact words "press release." Distinct from linkedin-announcement-generator (social post) and readme-generator (GitHub docs).
license: MIT
---

# Press Release Generator

## Overview

This skill writes a professional press release that announces an intelligent
textbook (or a major milestone, such as a new edition or a tie-in to current
events or legislation). It pulls the same canonical book statistics that the
README, LinkedIn, and case-study skills use, then reshapes them into the form
journalists actually expect: **Associated Press (AP) style, inverted-pyramid
structure, a genuine news hook, attributed quotes, and a boilerplate.**

A press release is not a LinkedIn post with a dateline glued on. The two
formats optimize for different readers, and that difference drives almost every
instruction below:

- A **LinkedIn post** sells scope to peers — metrics forward, emoji, hashtags,
  first person, enthusiastic.
- A **press release** gives a busy editor a story they can run with minimal
  rewriting — news value forward, human stakes, third person, neutral
  reported tone, verifiable facts, and a real person to call.

If you find yourself reaching for the LinkedIn voice (📊 bullet dumps,
"thrilled to announce," hashtags), stop — that is the wrong instrument.

## When to Use This Skill

- A textbook is being published or has reached a newsworthy milestone
- An advocacy group, school, library, or nonprofit wants media coverage
- The content ties to current events, a new law, a public-health need, or a
  local angle that a regional outlet would care about
- The user mentions a press release, news release, media advisory, press
  statement, embargo, or "getting picked up" by the press
- A conference, launch event, or grant announcement needs a written release

## Two operating modes (this matters — read before Step 1)

The skill must work in **both** of these situations, because the user often
wants a release for a book that is already deployed but not checked out locally:

1. **Inside the textbook repo** (ideal): `docs/learning-graph/book-metrics.json`
   and `mkdocs.yml` are on disk. Use the canonical metrics directly.
2. **Live site only**: you have a published URL but no repo. Derive a verified
   factual skeleton from the deployed site instead — see Step 2B. Do **not**
   invent numbers you cannot see; an editor will fact-check them.

Detect which mode you are in before gathering data, and tell the user which one
you used so they know how the figures were sourced.

## Workflow

### Step 1 — Gather book metadata

From `mkdocs.yml` (or, in live-site mode, the site `<head>` and footer):

- `site_name` — the textbook title
- `site_url` — the live URL (the single most important link in the release)
- `site_description` — one-line description
- `repo_url` — repository, for a "the project is open source" line if relevant

From `docs/course-description.md` (if present): audience, prerequisites,
subject scope, and learning goals. These shape the "who is this for" sentence.

### Step 2A — Metrics from the repo (preferred)

Read the canonical metrics file — never recount content by hand or scrape the
brittle `book-metrics.md` table. This is the same source the other book skills
use, so every artifact reports identical numbers.

```bash
python3 - <<'PY'
import json, pathlib, sys
p = pathlib.Path("docs/learning-graph/book-metrics.json")
if not p.exists():
    sys.exit("book-metrics.json missing — run bk-generate-book-metrics, or use Step 2B")
print(json.dumps(json.loads(p.read_text())["metrics"], indent=2))
PY
```

Useful keys: `chapters`, `concepts`, `glossaryTerms`, `quizQuestions`,
`microsims`, `words`, `equivalentPages`, `faqs`, `diagrams`, `developmentStage`.

### Step 2B — Facts from the live site (fallback)

When there is no repo, the deployed site still yields hard, checkable facts.
The sitemap is the fastest route to an accurate structural skeleton:

```bash
curl -s https://SITE/sitemap.xml | grep -o '<loc>[^<]*</loc>' | sed 's/<[^>]*>//g'
```

From the URL list you can count chapters, simulations (`/sims/`), quizzes, and
named tools, and confirm the presence of a glossary, FAQ, and resources page.
Fetch the home page for the title, tagline, publisher, and mission language.
Prefer **fewer, certain** numbers (e.g., "nine chapters and four interactive
simulations," both countable from the sitemap) over impressive-but-unverifiable
ones. Tell the user which figures came from the sitemap so they can confirm.

### Step 3 — Get the news hook and the things only a human can supply

This is the step that separates a real release from a glorified summary, and
it is the step the repo cannot answer for you. **Interview the user** for:

- **The angle — why is this news *now*?** A new resource alone is weak. Strong
  hooks: ties to a specific law or policy, a public-health statistic, a local
  "first," a season (back-to-school), a grant, an event, an unmet need the data
  exposes. Lead with this.
- **Dateline city and state** — usually the publishing organization's home city.
- **Release timing** — "FOR IMMEDIATE RELEASE" or an embargo
  ("EMBARGOED UNTIL ...").
- **Spokesperson quote(s)** — full name, title, organization, and an approved
  quote. One or two only (a principal/leader, plus optionally a partner,
  educator, parent, or subject expert).
- **Boilerplate** — the standing "About [Organization]" paragraph.
- **Media contact** — name, email, phone.

If the user does not have a quote or contact yet, do not stall and do not
invent them — see "Never fabricate sourced facts" below.

### Step 4 — Assemble in AP style

Use the structure and rules in the **AP Style Reference** section. Build the
body in inverted-pyramid order: the single most important fact first, then
decreasing importance, so an editor can cut from the bottom without losing the
story.

### Step 5 — Run the AP checklist

Before presenting, verify against the **Quality Checklist** below. AP-style
slips (a superlative in the headline, a wrong month abbreviation, a quote that
starts with "I") are exactly what signals "amateur" to an editor.

### Step 6 — Deliver with a short distribution note

Present the release as clean, copy-paste-ready text (plain paragraphs, no
markdown styling inside the release body — newsrooms want plain text). Follow
it with 2–4 lines of practical distribution advice tailored to the topic:
which kinds of outlets fit (local dailies, education trade press, the relevant
advocacy/professional newsletters, the city/regional desk), and a reminder to
send as pasted text plus a PDF, not only an attachment.

## AP Style Reference

Embed this format exactly; it is what newsrooms expect.

### Overall structure

```
FOR IMMEDIATE RELEASE
[or: EMBARGOED UNTIL 9 A.M. CT, MONTH DAY, YEAR]

Headline in Title Case, Present Tense, No Period
Optional Subhead Adding the Second-Most-Important Fact

CITY, State abbrev., Month Day, Year — The lead sentence states WHO did WHAT,
WHEN, WHERE, and WHY in roughly 25–35 words, leading with the news hook.

The second paragraph expands the lead with the most important supporting facts
and context — the scale of the problem, the need, or the data.

"A quote that adds perspective or a forward-looking statement rather than
repeating the facts above," said Full Name, title at Organization. "An optional
second sentence."

Body paragraphs in descending order of importance: what the resource contains,
who it is for, what makes it credible or distinctive, how it is funded or
governed. Weave in two or three verifiable figures — do not dump a metrics list.

"An optional supporting quote from a partner, educator, parent, or expert,"
said Full Name, title at Organization.

A closing paragraph with availability, price (note if free), and the call to
action — the URL.

About [Organization]
[Organization] is a [one-sentence description]. [One or two sentences of
mission/background.] Learn more at [URL].

Media Contact:
Full Name
Email
Phone

###
```

The closing `###` (centered) is the traditional "end of release" mark; editors
rely on it to know nothing was truncated.

### Headline rules

- Title case, present tense, active voice, **no period**, **no exclamation point**
- No superlatives ("revolutionary," "groundbreaking," "first-ever," "best")
- State the actual news element, not a slogan

```
❌ Amazing New Epilepsy Textbook Will Revolutionize School Safety!
❌ Press Release: A New Resource for Schools
✅ Student-Led Group Releases Free Guide to Help Minnesota Schools Prepare for Seizures
```

### Dateline

Format: `CITY, State abbrev., Month Day, Year —`

AP **abbreviates** these months: Jan., Feb., Aug., Sept., Oct., Nov., Dec.
March, April, May, June, and July are **spelled out**. The city is uppercase;
the state uses the AP abbreviation (e.g., Minn., Calif., Mass.). Large cities
that stand alone without a state in AP style include New York, Chicago, Los
Angeles, Boston, and Washington; most others take the state.

```
ST. PAUL, Minn., June 19, 2026 —
MINNEAPOLIS, Sept. 3, 2026 —
```

### Lead paragraph

Answer the five W's, hook first, in ~25–35 words. Lead with *why it matters*,
not with the existence of a document.

```
❌ A new website has been launched that contains educational materials about
   epilepsy for use in schools and other settings.
✅ With Minnesota law now requiring every school to be ready for student
   seizures, a student-led advocacy group today released a free, plain-language
   textbook that walks families and staff through seizure first aid, the law,
   and a child's rights.
```

### Quotes

- One or two quotes maximum; each must be **attributable to a real, named person**
- Never begin a quote with "I"
- Attribution format: `"Quote," said Full Name, title at Organization.`
- Quotes add perspective or look forward; they never restate the body facts

```
❌ "I think this is a really exciting and important new resource," said the team.
✅ "Most seizures at school are handled by teachers, not doctors, so the people
   on the front lines deserve materials they can actually use," said Jane Doe,
   founder of the Epilepsy Data & Advocacy Network.
```

## Never fabricate sourced facts

A press release goes on the public record and editors verify it. A quote
attributed to a named person, a contact phone number, a partner organization,
or a statistic that turns out to be invented does lasting damage to the
author's credibility and cannot be un-published once it is on the wire. So:

- **Never invent a quotation** and attribute it to a real person. If the user
  has no approved quote yet, insert a clearly bracketed placeholder such as
  `[DRAFT QUOTE — replace with approved language from Jane Doe, EDAN founder]`
  and tell the user it must be filled before distribution.
- **Never invent contact details, partners, dollar figures, dates, or stats.**
  Use the journalist's `[TK]` ("to come") marker — e.g., `[TK: media contact
  email]` — for anything the user must supply. Bracketed gaps in a draft are
  normal and expected; fabricated specifics are not.
- **Prefer verified, modest numbers** over impressive guesses. "Nine chapters
  and four interactive simulations" that you counted beats a word count you
  cannot confirm.

This is about protecting the user, not bureaucratic caution — frame any gaps to
them plainly so they know exactly what to approve before sending.

## Quality Checklist

- [ ] Headline: title case, present tense, no period, no superlatives, real news
- [ ] Dateline present with correct AP month style
- [ ] Lead answers the five W's in ~25–35 words and leads with the hook
- [ ] Inverted pyramid: most important first, cuttable from the bottom
- [ ] Two or three verified figures woven in — not a metrics dump
- [ ] Every quote attributed to a named, real person (or clearly marked draft)
- [ ] No quote begins with "I"
- [ ] "About [Organization]" boilerplate present
- [ ] Media-contact block present (or `[TK]` placeholders flagged)
- [ ] The live URL appears and is correct
- [ ] Neutral reported tone — no hashtags, no emoji, no first person
- [ ] Closes with `###`
- [ ] Every `[TK]`/`[DRAFT ...]` placeholder called out to the user

## Example skeleton (generic — adapt, do not copy verbatim)

```
FOR IMMEDIATE RELEASE

Nonprofit Releases Free Interactive Textbook on [Topic] for [Audience]

CITY, State., Month Day, Year — [Lead: hook + five W's in 25–35 words.]

[Second paragraph: the need or the data behind the news.]

"[Perspective quote that does not restate the facts]," said Full Name, title
at Organization.

[Body: what the resource includes — chapters, interactive simulations,
glossary, quizzes — woven with two or three verified figures and who it serves.]

[Closing: free and open, where to find it, the URL.]

About [Organization]
[One-sentence description. Mission sentence.] Learn more at [URL].

Media Contact:
Full Name
Email
Phone

###
```

## Customization

- **Tone within AP bounds**: straight-news vs. feature/human-interest lead
- **Audience emphasis**: education desk, health desk, local/regional desk, or a
  trade/advocacy newsletter — adjust the angle and the supporting facts
- **Length**: a tight one-page release (default) or a longer version with an
  extra supporting quote and a "background" paragraph
- **Companion assets**: offer to generate a matching media advisory (shorter,
  event-style) or a tip sheet on request

## Related Skills

- **linkedin-announcement-generator** — social-post version of the same news
- **readme-generator** — GitHub project documentation
- **book-installer (book-metrics guide)** / `bk-generate-book-metrics` —
  produces the `book-metrics.json` this skill reads in repo mode

## Resources

- [AP Stylebook](https://www.apstylebook.com/)
- [Purdue OWL: Press Releases](https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/press_releases.html)
