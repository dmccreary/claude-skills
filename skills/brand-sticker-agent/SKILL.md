---
name: brand-sticker-agent
description: Scaffolds a complete multi-brand sticker agent in a shilpiworks-style codebase (Next.js + Mastra + Prisma + Vercel Blob + Gemini Nano Banana 2). Use this skill whenever the user wants to add a new sticker brand to a sticker shop, scaffold a brand sticker pipeline, create a Lorignite-style agent for someone, white-label a sticker line for a friend or partner brand, build a brand-isolated sticker agent with its own collection page, add another agent to the createAgentRunner factory pattern, set up a brand kit-driven sticker generator, or wire up a categorized seed-quote-pool plus LLM-fresh-quote pipeline with structured-block image prompts. Also triggers on phrases like "add a sticker agent for <name>", "lorignite-style agent", "new brand collection", "scaffold a sticker brand", "white-label sticker pipeline". Generates the brand-quotes data file, anchors directory, Mastra workflow + steps, agent-runner registration, route, trigger script, batch script, and the /<brand> storefront collection page — wired with brand-isolated watermarks (© <brand>.com), features.brand persistence for storefront filtering, and the visual-QA gate from the stochastic-image-qa-gate skill. Originally extracted from the Lorignite agent built for Lori Ryan in shilpiworks.
---

# Brand Sticker Agent

Scaffolds a brand-isolated sticker agent in a shilpiworks-style codebase. The pattern was developed for Lorignite (Lori Ryan's AI-literacy brand) and generalizes to any new brand that wants its own sticker line on the same Next.js + Mastra + Prisma + Vercel Blob infrastructure.

## When this applies

You're working in a codebase with the shilpiworks pattern:
- `frontend/lib/mastra/` — Mastra workflows, steps, anchors, factory (`agent-runner.js`)
- `frontend/lib/mastra/publish.js` — shared `publishProduct` that handles edge watermark, Blob upload, Prisma write
- `frontend/lib/mastra/agent-runner.js` — `createAgentRunner` factory accepting `brand`, `watermarkText`, `qaResult` config
- `frontend/app/api/agent/<agent>/route.js` — HTTP entry per agent
- `frontend/app/<brand>/page.js` — brand-themed collection storefront
- `Product` table with `features` JSON column persisting `brand`, `agent_type`, `qa_verdict`, etc.

If the codebase doesn't have these pieces, this skill assumes too much. Build the foundation first or adapt the patches.

## What you need before scaffolding

The user must provide a brand kit. Minimum:
- **Brand name** (kebab-case, lowercase, no spaces — e.g. `lorignite`, `acme-cards`)
- **Brand palette** — at minimum a primary background color, a primary type color, and an accent/focal color (hex codes)
- **Brand voice** — 2–3 sentences on tone, audience, what to avoid
- **Seed quotes** — 20–80 phrases the brand wants on stickers, optionally categorized by tone/use-case
- **One or more anchor images** — sample stickers in the brand's visual register (mockups, existing prints, brand guide pages); these feed NB2 as reference images
- **Brandmark spec** — wordmark text + small icon hint + corner placement
- **Watermark URL** — the brand's domain for edge watermarks (e.g. `lorignite.com`)

If anything is missing, **ask the user before scaffolding** — don't guess. Skip this only when you have a complete brand guide PDF / kit on disk that you can extract from.

## The eight pieces

A complete brand agent has these files. The scaffolder generates all eight; you customize each.

| File | What it contains |
|---|---|
| `brands/<brand>/` | Optional folder for raw brand-kit PDFs/xlsx/etc. — archival reference |
| `frontend/lib/mastra/data/<brand>-quotes.js` | Categorized seed quote pool — exports `BRAND_CATEGORIES` (tone buckets + quotes) |
| `frontend/lib/mastra/anchors/<brand>/` | Reference image(s) for NB2 anchored mode |
| `frontend/lib/mastra/<brand>-steps.js` | Mastra `<brand>-quote` step (seed-or-LLM coin flip), `build-prompt` step, `generateBrandQuote` LLM-fresh quote function, structured-block image prompt builder, optional QA step |
| `frontend/lib/mastra/<brand>-workflow.js` | Mastra workflow chaining the steps + image gen + QA |
| `frontend/lib/mastra/<brand>.js` | `createAgentRunner` config — sets `type`, `brand`, `watermarkText`, `requiredTags`, hooks |
| `frontend/app/api/agent/<brand>/route.js` | HTTP POST endpoint with auth gating |
| `frontend/scripts/trigger-<brand>.js` + `batch-<brand>.mjs` | Local manual-trigger and batch-runner |
| `frontend/app/<brand>/page.js` | Brand-themed collection storefront filtering on `features.brand === '<brand>'` |
| Registration line in `frontend/app/api/telegram/run-agent/agents.js` | One line in the factory map |

## Implementation guide

The scaffold script generates the boilerplate:

```bash
node ~/.claude/skills/brand-sticker-agent/scripts/scaffold-brand-agent.mjs \
  --brand <brand-name> \
  --watermark-url <brand>.com \
  --tagline "<brand tagline>" \
  --primary-color "#XXYYZZ" \
  --type-color "#XXYYZZ" \
  --accent-color "#XXYYZZ" \
  --repo-root <path/to/shilpiworks-repo>
```

It writes ALL eight pieces with sensible defaults plus TODO markers where customization is required (rubric items for QA, signature visual prompt details, brand-voice strings).

After running the scaffold:

1. **Drop seed quotes into `data/<brand>-quotes.js`.** Categorize them — 5 categories of 10 each is a sweet spot. Empty categories work too; the agent handles small pools gracefully.

2. **Drop anchor images into `anchors/<brand>/`.** One composite mosaic of brand mockups works as a starting point; per the experience with Lorignite, multiple individually-cropped tiles (3–6) tend to produce more reliable visual register than one mosaic.

3. **Customize the structured-block image prompt.** The scaffold writes a placeholder template; replace `[BRAND_VISUAL_DESCRIPTION]` with the brand's actual typographic recipe — what's the focal-word treatment, what colors go where, what shape is the die-cut. See [references/visual-prompt-design.md](references/visual-prompt-design.md).

4. **Customize the `generateBrandQuote` system prompt.** Write the brand voice, the test the phrase must pass (the brand's "passes test"), the constraints (length, vocabulary).

5. **Wire the visual-QA gate** from the `stochastic-image-qa-gate` skill if you want post-generation validation. Run that skill's scaffolder to generate the QA step file, then splice into the workflow.

6. **Customize the storefront page** — palette, hero copy, founder bio.

7. **Test locally.** Run `node frontend/scripts/trigger-<brand>.js` to generate one sticker. Verify it lands in DB + Blob, renders on `/<brand>`. Iterate.

## Architecture decisions baked in

These decisions are encoded in the scaffold and should NOT be revisited per-brand without good reason:

- **`createAgentRunner` factory pattern.** Don't hand-roll the agent invocation lifecycle. The factory handles AgentRun create/update, recent-quotes dedup, decision trace, prompt-payload extraction, error handling.
- **Brand isolation via `features.brand` JSON field, not a Postgres column.** Adding a column is a migration risk in production-critical agent infra. Use the existing JSON `features` field; storefront filters on `features.brand === '<brand>'`. Can tighten to a column later if perf demands.
- **Watermark via `watermarkText` parameter, not a brand-specific watermark function.** The shared `applyWatermark` accepts a text param; pass `'© <brand>.com'`. Don't fork the watermark logic.
- **Seed-or-LLM coin flip, default 50/50.** Both paths produce on-brand output; the LLM path explores beyond the seed pool while staying in the brand voice. Tunable via `LORIGNITE_LLM_RATIO`-style env var if desired (the scaffold doesn't add this — start simple).
- **Categories are tone buckets; pillars are thematic anchors.** If the brand has 5 tone buckets and 5 thematic pillars, that's 25 LLM-prompt configurations producing variety without complexity. See [references/quote-generation-design.md](references/quote-generation-design.md).
- **The image prompt instructs NB2 to pick the focal word itself.** Do NOT add a separate Gemini Flash decomposer step that pre-decides the typographic split — that pattern was tried and rejected for Lorignite (introduced a fragility surface that produced duplicated words). Trust NB2 with the whole quote.

## Common mistakes

- **Adding a `Product.brand` column instead of using `features.brand`.** Tempting but adds a migration to a fragile production DB. Use the JSON path.
- **Hand-rolling the workflow without the factory.** You'll re-implement AgentRun lifecycle, recent-quote dedup, error handling, decision trace, and miss the brand/watermark threading. Use `createAgentRunner`.
- **Forgetting to register in `agents.js`.** Without that one line, the Telegram bot factory can't reach the agent. The scaffold adds it; verify after running.
- **Making the agent throw on bad output.** Use the soft-kill pattern from the QA gate skill — failed output lands as inactive Product, preserving evidence for review.
- **Putting a decomposer in the pipeline.** This was the Lorignite mistake. The image model has visual judgment a text-only decomposer doesn't. Let NB2 decide the focal word.
- **Categorical over-specificity in seed quotes.** If 5 categories each have 50 quotes that all sound the same, the LLM-fresh path can't add variety. Make categories meaningfully different in tone, not just topic.

## Scaling: when to add another brand

The factory pattern is genuinely multi-brand-ready. Adding brand #3 should be:

1. New brand kit dropped in
2. Run scaffolder
3. Customize 6 files (data, anchor, prompts, voice, palette, storefront)
4. Test, ship

Total time: ~2–4 hours per brand once the first one is working. The scaffolder won't make brand #3 better than brand #1 — it just makes the boilerplate identical so the per-brand work is concentrated on the parts that actually matter (quote curation, visual register, voice).

## Reference depth

This SKILL.md is the orientation. Three deeper references for specific decisions:

- [references/visual-prompt-design.md](references/visual-prompt-design.md) — structured-block prompt format, lead-with-non-negotiable, positive-not-negation, specific NEGATIVES; per-brand TYPOGRAPHY/PALETTE/COMPOSITION blocks
- [references/quote-generation-design.md](references/quote-generation-design.md) — categorized seed pools, LLM-fresh in-voice generation, thematic-pillar dice for variety, the brand-test rubric
- [references/threading.md](references/threading.md) — shared infrastructure changes (factory, publish.js) needed once before any new brand can be added; what to share vs. what to fork
