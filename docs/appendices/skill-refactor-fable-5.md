# Skill Refactor with Fable 5

*A case study in how an agent skill library evolves — and why it needs to be periodically re-architected.*

## Context: Nine Months of Claude Skills

Anthropic introduced Claude Skills — self-contained `SKILL.md` bundles that Claude Code discovers, matches by description, and loads on demand — in October 2025. The `ibook-skills` repository adopted the pattern almost immediately: each capability needed to build an intelligent textbook (learning graph generation, chapter writing, MicroSim creation, glossary generation, and dozens more) became its own skill directory.

That worked well at first. It worked less well nine months later.

By July 2026 the repository held **36+ individual skills**. Two structural limits, invisible to a casual contributor adding "just one more skill," had both been quietly breached:

1. **Claude Code caps loaded skills at 30.** This is a hard, silent limit — when a project exceeds it, extra skills are dropped with no error message, and *which* ones get dropped is non-deterministic across restarts.
2. **Every skill's `name:` and `description:` frontmatter is injected into every session's context, unconditionally.** This is the "always-on tax": tokens spent before the user has typed a single word, on every turn, whether or not that skill is ever invoked.

This is the story of the second time this repository hit that wall, and how it was fixed.

## Round One: The Meta-Skill Pattern (Spring 2026)

The first consolidation, documented in [`docs/consolidation-plan/`](../consolidation-plan/index.md), took 36 skills down to 19 by inventing a pattern that has held up well: the **meta-skill router**.

Instead of one skill per capability, a meta-skill is a thin dispatcher:

- A compact `SKILL.md` with a keyword **routing table** (`| Trigger Keywords | Guide File | Purpose |`) and a redundant prose decision tree.
- A `references/` folder holding one **guide file per consolidated capability** — the actual multi-hundred-line workflow that used to be its own `SKILL.md`.
- Optional `scripts/` and `assets/` subfolders for the Python tooling and templates each capability needs.

The router's frontmatter is the only part that's *always* loaded. The guide inside `references/` is read only when Claude actually matches a request to it. This is the key mechanical trick that makes consolidation a token-budget win rather than just a filing exercise: **fourteen capabilities behind one router cost roughly the token price of one skill description, not fourteen.**

Three meta-skills emerged from round one — `book-installer` (project setup and infrastructure), `microsim-generator` (interactive simulation generators), and `microsim-utils` (MicroSim QA and maintenance) — and the repository settled at 19 skills.

## The Regrowth Problem

Nineteen skills didn't stay nineteen. Over the following months, new capabilities were added the easy way: as fresh top-level skill directories, not as new routes inside an existing meta-skill. By July 2026 the count had crept back to **29 loaded skills**, plus two stray, non-skill directories that had accumulated in `skills/` (a committed eval-output folder and, separately, an unversioned skill that only ever existed as a real directory in `~/.claude/skills`, never checked into git).

This is a completely ordinary failure mode for any organizing system — a taxonomy, a folder structure, a component library — and it's worth naming explicitly: **consolidation is not a one-time event, it's a maintenance cadence.** The meta-skill pattern from round one solved the problem that existed in round one; it didn't prevent a *new* generation of ungrouped skills from accumulating around it. Nothing in the tooling stopped a contributor from creating skill #30, #31, #32 as flat top-level directories, because nothing was watching the count or the token budget as new skills were added.

By the time this was noticed, the numbers were stark:

| Metric | State in July 2026 |
|---|---|
| Skills in the repository | 29 (+ 2 non-skill stray directories) |
| Loaded in `~/.claude/skills` | 30 / 30 — at the hard cap |
| Skills silently dropped | 2 (`docker-python-lab`, `linkedin-carousel-generator` — never even got a symlink) |
| Always-on description tokens | ~2,053 tokens |

## The Token-Budget Question, and Why "1M Context Windows" Doesn't Make It Go Away

It's tempting to think the token-budget half of this problem has been solved by hardware, not architecture. Claude models today commonly ship **1M-token context windows**, dwarfing the 200K figure this project's internal budgeting convention (CLAUDE.md's "1% of context" rule) was written against. If the ceiling is 1M, doesn't 2,053 tokens of skill descriptions round to noise?

Two things keep this from being true in practice:

**First, the 30-skill cap is a *count* limit, not a token limit.** A 1M context window does nothing to relax Claude Code's hard ceiling of 30 loaded skills. Even if every skill description were free, thirty-one skills is still one too many, and the twenty-ninth and thirtieth silently-dropped skills in this project's case (`docker-python-lab`, `linkedin-carousel-generator`) prove the point — that failure had nothing to do with token math. **The count constraint, not the token constraint, was actually the more binding one**, and it's the one that motivated the hardest deadline in this refactor: nothing could be safely added until the roster shrank.

**Second, even where token budget is the live constraint, it doesn't disappear at 1M — it just becomes a smaller *percentage* of a larger number while staying the same *number* of wasted tokens.** A few things keep the absolute cost worth minimizing regardless of window size:

- **Portability.** Not every environment a skill library runs in has a 1M window. Claude Code sessions, third-party integrations, smaller models used for cheap routing tasks, and older or constrained deployments frequently still operate at 200K or less. A skill catalog engineered to be lean at 200K is lean everywhere; one engineered assuming 1M headroom breaks the moment it runs somewhere smaller.
- **It's a tax paid every single turn, not once.** In a long session, 2,000 wasted tokens of skill catalog overhead multiplies across every turn's cost and latency, compounding in a way a one-time "1% of 1M is nothing" framing misses.
- **Headroom is a resource, and it's finite regardless of the denominator.** A leaner catalog means more room to add the *next* ten skills without re-triggering this exact problem in another nine months. Token efficiency and skill-count efficiency are the same discipline pointed at two different limits, and both compound the same way.

So the refactor kept the original 1%-of-200K convention (~2,000 tokens) as its working budget — not because 200K is the true ceiling anymore, but because it's a conservative, portable target that stays correct as context windows keep growing, and because the *count* limit, not the token limit, was the deadline that actually mattered.

## The Process: An Agent-Authored Plan, Reviewed Phase by Phase

This round of consolidation was carried out by **Claude Fable 5** — Anthropic's newest and most capable generally-available model — operating inside Claude Code's plan mode. The process is worth documenting on its own terms, because it's a template for how a large, risky, multi-file refactor can be delegated to an agent without losing human control over the outcome.

### Exploration before opinion

Rather than proposing a plan from a skim of the directory listing, Fable 5 opened by measuring. It wrote a script to compute the exact character and token count of every skill's frontmatter, confirmed the 30-skill ceiling was actually being hit (not just theoretically close), and then dispatched **three parallel Explore subagents** — one over the existing meta-skill architecture, one over the book-generation pipeline skills, one over the media and miscellaneous skills — to build a complete map of the repository before writing a single sentence of recommendation. This surfaced the anomalies a surface read would have missed: a skill with a case-sensitive-filesystem-breaking lowercase filename, a guide file whose frontmatter still named a skill that had supposedly been retired months earlier, reference documents that no `SKILL.md` in the repository actually loaded by name, and a "feature" listed in a help menu that had never been given an implementation at all.

### Scoping through structured questions, not assumption

With the map in hand, Fable 5 didn't guess how aggressive the consolidation should be. It used the `AskUserQuestion` tool to put three concrete, mutually exclusive choices in front of the human collaborator:

1. **How aggressive should the consolidation be?** Full (~8 skills, folding even the content-generation pipeline into a meta-skill) vs. moderate (~14 skills, preserving the content pipeline as standalone skills) vs. cosmetic (trim descriptions only, no merging).
2. **What happens to the two skills unrelated to MkDocs textbooks** (a generic text-to-speech tool and a Word-to-web publisher)?
3. **How should the published documentation site handle the reorganization** — full rewrite, minimal patch, or defer entirely?

The answer to question 1 — **moderate, ~14 skills** — mattered architecturally: it preserved a decision from round one (that FAQ, quiz, glossary, and reference generation are complex enough workflows to deserve their own dedicated skills, not routes buried in a meta-skill) rather than silently overriding it in the name of a lower token count. A less careful process might have optimized purely for minimum footprint and thrown that earlier, deliberate decision away.

### A single, complete, reviewable plan

Only after those three answers came back did Fable 5 write the actual implementation plan — and it wrote the *whole* plan before touching a single file, using Claude Code's plan mode to guarantee no code could change until the human explicitly approved it. The plan specified:

- The exact final roster of 14 skills and what each one absorbed.
- File-by-file conversion mechanics for every merge (where each absorbed skill's body goes, how support files get renamed to avoid collisions, how routing-table rows get added).
- Where shared, duplicated content (mkdocs navigation-editing rules, Bloom's Taxonomy reference material) would be consolidated into single canonical files.
- A **nine-phase execution order**, each phase sized to land as exactly one git commit.
- A verification protocol to run after every phase.
- An explicit risk section, naming the specific things most likely to go wrong (trigger-keyword regressions from shortened descriptions, muscle-memory breakage from renamed skills, cross-skill path coupling) and the mitigation for each.

This plan was presented for approval before any implementation began, and the human reviewer edited it before accepting — the approved plan that actually drove the work differs from Fable 5's first draft in exactly the ways the three scoping answers dictated.

### Phase-by-phase execution, reviewed at every step

The nine phases were not run as one long unattended pass. Each phase corresponds to exactly one commit, and — because the repository's tooling only allows one automated commit per conversational turn — each phase was executed, verified, and reported back to the human, who then typed `continue` to authorize the next phase. This turned a single large, hard-to-review diff into **nine small, independently reviewable, independently revertible commits**, each with its own descriptive commit message explaining not just *what* changed but *why*.

That structure paid off directly: partway through, a large unrelated change from a prior session was discovered sitting uncommitted in the working tree. Rather than let the hygiene phase's auto-commit sweep it in as noise, it was committed separately first, under its own message, so the phase history stays a clean, honest record of *this* refactor and nothing else.

## What Actually Happened, Phase by Phase

| Phase | What it did | Skills after |
|---|---|---|
| Pre-phase | Rescued unrelated uncommitted work into its own commit | — |
| 0 — Hygiene | Removed a non-skill eval-output directory; adopted an unversioned skill into git; patched the installer to never load `skills/archived/`; salvaged a reference file that existed only in a stale local copy; fixed dangling documentation references | 30 loaded |
| 1 — MicroSim merge | Folded 4 stray MicroSim-generator skills into `microsim-generator`, including replacing a guide whose frontmatter still named a supposedly-retired skill | 27 loaded (freed slots let a previously-unloadable skill load for the first time ever) |
| 2 — Utils merge | Folded a diagram/coverage-report skill into `microsim-utils` | — |
| 3 — Installer merge | Folded project-scaffolding and Google Analytics registration into `book-installer` as new numbered features; discovered the Analytics feature had been listed in the help menu for months with no actual guide behind it | 25 loaded |
| 4 — New: `book-publisher` | Created a new meta-skill for README, LinkedIn, and press-release generation; discovered the "duplicated metrics collection" the plan expected to fix had already partly self-healed — most of these skills had already converged on reading one canonical metrics file | 22 loaded |
| 5 — New: `book-media-generator` | Created a new meta-skill for slide decks, illustrated stories, infographics, sourced images, and audio — the largest single merge (7 skills). Added an explicit disambiguation rule at the top of the router to resolve two skills that had been silently competing for the same "make me a presentation" trigger phrases | **14 loaded — target roster reached** |
| 6 — Content-skill dedup | Extracted navigation-editing rules and Bloom's Taxonomy guidance — duplicated across five separate skills — into two canonical shared reference files | 14 loaded |
| 7 — Docs sweep | Rewrote the internal architecture documentation, the build-order runbook, and the published documentation site to describe the new roster, while preserving every old inbound URL behind a "legacy snapshot" banner | 14 loaded |
| 8 — Verification | A repo-wide integrity sweep checking every file path referenced by every meta-skill actually exists, checking that all 31 distinctive trigger keywords from the 18 retired skills survived somewhere in the new descriptions, and cataloguing (without silently fixing, and without scope creep) a separate list of pre-existing broken references left over from round one | 14 loaded |
| Follow-up | A stale-but-unused "Option 2" installation guide, with assets that had never existed in the repository, was deleted entirely on explicit approval rather than patched around | 14 loaded |

The final numbers: **29 skills became 14. 2,053 tokens of always-on description text became 978 — 49% of the working budget, down from 103% over it.** The loaded-skill count went from 30-of-30 (at the hard ceiling, silently dropping capabilities) to 16-of-30, with fourteen free slots for whatever comes next.

## How Skills Compose Now

The point of the meta-skill pattern isn't just fewer entries in a list — it's that skills can now cooperate on a shared workflow without either re-deriving the same facts or stepping on each other's edits. Three concrete mechanisms make that possible after this refactor:

**On-demand loading keeps composition cheap.** Because a meta-skill's `references/` guides are only read when a specific route is actually matched, invoking three different routes across three different meta-skills in one session costs roughly the same as invoking one — the router frontmatter for all five meta-skills is already sitting in context regardless, and the guide content is the only thing that scales with what's actually used.

**A canonical metrics hub lets independent skills agree on facts.** `book-publisher`'s four routes (README, LinkedIn post, LinkedIn carousel, press release) all read the same `docs/learning-graph/book-metrics.json` file rather than each recomputing chapter counts, word counts, and MicroSim counts independently. Generate a README and a LinkedIn announcement in the same session and they will report identical numbers, because they're reading the same source rather than four independent recount passes that can drift out of sync.

**Canonical shared guides prevent divergent duplicate advice.** Five separate content-generation skills used to carry five separate, slowly-drifting copies of "how to safely edit `mkdocs.yml`'s navigation section." One of those copies had already, independently, grown a warning about concurrent-edit collisions that the other four didn't have. That warning is now promoted into the single canonical `mkdocs-nav-editing.md` guide that all five skills point at, so every skill that touches site navigation benefits from a lesson only one of them had actually learned.

**Cross-meta-skill references use one explicit convention.** Where a guide in one meta-skill needs a fact or a file that lives in another (the `microsim-generator` guide for MicroSim diagrams pointing at `microsim-utils` for QA, or `book-publisher` pointing at `book-installer`'s metrics-generation script), the reference is written as an absolute path — `$HOME/.claude/skills/<owner-skill>/references/<file>.md` — rather than a fragile relative path. This was an established pattern from round one; this refactor extended it as the standard way meta-skills talk to each other, rather than each pair inventing its own convention.

The `/ibook` slash command sits above all five meta-skills as a read-only orchestration layer: it detects which pipeline artifacts already exist in a given textbook project and recommends the single next skill (and route) to invoke, in `meta-skill → route` form. It never invokes anything automatically — every step still requires the human to explicitly run it — but it means a book author doesn't need to remember which of five meta-skills now owns "make me a press release" or "add a Python lab to this page." They ask `/ibook` where they are, and it tells them.

## What This Says About Running an Agent Skill Library at Scale

A few lessons generalize beyond this one repository:

- **Consolidation is maintenance, not a milestone.** The same forces that produced 36 skills the first time reproduced 29 the second time. Whatever solves this permanently will need to be a standing discipline — a token-budget check that runs automatically, not a periodic manual archaeology project — and that automated check is explicitly on the list of things this refactor did *not* attempt to build.
- **A hard count limit and a soft token budget are different constraints and need different fixes.** The 30-skill ceiling is the one that silently breaks things; the token budget is the one that degrades gracefully. Both were real, and treating them as the same problem would have under-solved the more dangerous one.
- **Archaeology finds real bugs, not just clutter.** A stale frontmatter still naming a retired skill, a documented feature with no implementation behind it, reference files no skill actually loaded — none of these were "consolidation opportunities" in the abstract; they were live defects that a careful read-before-merge process caught and fixed as a side effect of the reorganization.
- **Delegating a large refactor to an agent doesn't mean losing the ability to review it.** Structured scoping questions before planning, a complete written plan before any code changes, and a phase boundary at every commit turned what could have been one opaque mega-diff into a sequence anyone could stop, question, or revert at any point — and one point in that sequence *was* stopped and redirected, when the human explicitly approved deleting a broken guide the agent had originally only flagged rather than removed.

## Fable 5 Token Costs

This entire 8 phase refactor used only 23% of my Fable 5 tokens in my 5-hour window.
It is difficult to calculate exactly how many tokens were used since Anthropic
seems to scale token budgets based on supply and demand.

## Detailed Session Log

*Session log: [`logs/skill-refactor-by-fable-5.md`](https://github.com/dmccreary/ibook-skills/blob/main/logs/skill-refactor-by-fable-5.md) — the complete phase-by-phase engineering record, including the full approved plan document, every commit hash, and the outstanding follow-up items.*
