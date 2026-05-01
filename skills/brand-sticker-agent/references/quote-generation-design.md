# Quote Generation Design

How the agent decides which phrase goes on each sticker. Two paths feed the workflow's `<brand>-quote` step: the seed pool (curated by the brand owner) and the LLM-fresh path (generated in-voice by Gemini Flash). 50/50 coin flip by default.

## The seed pool

Lori provided 50 quotes for Lorignite, organized into 5 tone categories. That structure scales:

```js
// frontend/lib/mastra/data/<brand>-quotes.js
export const BRAND_CATEGORIES = {
  'Category A': {
    tone: '<one-sentence description of how phrases in this category sound>',
    quotes: ['Phrase 1', 'Phrase 2', ...],
  },
  // ...
};

export const BRAND_ALL_QUOTES = Object.entries(BRAND_CATEGORIES)
  .flatMap(([category, { quotes }]) => quotes.map(quote => ({ quote, category })));
```

Categories are TONE buckets, not topic buckets. The right number is 3–7 (Lorignite uses 5). Each category needs at least 5–10 quotes; under that, the seed-pool path runs out fast and the agent falls through to LLM-fresh.

The categories' `tone` field gets injected into the LLM-fresh generator's system prompt — so good tone descriptions matter even for quotes you never generate.

## The LLM-fresh generator

Same workflow step (`<brand>-quote`) — when the coin flips to `mode: 'llm'`, it calls a Gemini Flash JSON function that writes a fresh phrase in the brand voice for the chosen category.

```js
export async function generateBrandQuote(category, recentQuotes = [], pillarKey = null) {
  // ... Gemini Flash JSON call ...
}
```

Three inputs shape the system prompt:

1. **Brand core**: belief, voice, audience, what to avoid (1 paragraph)
2. **Category-specific tone**: from `BRAND_CATEGORIES[category].tone`
3. **Thematic pillar** (optional but recommended for variety): see below

## Thematic pillars (variety multiplier)

Lorignite's catalog initially over-indexed on the literal word "curiosity" because:
- 74% of seed quotes contained it
- The LLM-fresh generator's system prompt emphasized it ("AI rewards curiosity")
- The image prompt said "pick the most curiosity-charged word" as focal

The fix: thematic pillars. The brand has 5–6 thematic anchors beyond its top-of-mind concept. Each generation rolls a pillar dice and conditions the LLM on that pillar's brief + example phrasings.

Lorignite's 6 pillars:
- Curiosity (down-weighted to 1/12 since seed pool already over-indexes)
- Experimentation / play
- Everyday superpowers
- Thinking partner (AI in dialogue, not query)
- Community learning (share what you tried)
- Reinvention (late-bloomer energy)

Result: 5 categories × 6 pillars = 30 distinct system-prompt configurations producing on-brand variety. The LLM stops repeating itself on a single dominant concept.

For a new brand, work with the brand owner to identify 4–7 pillars. They're typically not on the brand's tagline — the tagline is one pillar, and the others are adjacent ideas the brand also stands for.

## The brand test

Every generated phrase passes a deterministic test before being returned. For Lorignite:

> THE LORIGNITE TEST (the phrase must pass all of these):
>   - Does it make AI feel less intimidating?
>   - Does it spark curiosity?
>   - Does it encourage someone to try something new?
>   - Does it sound human and conversational?
>   - Would someone want to share this with a friend?

This goes in the system prompt as a checklist. The model produces phrases that pass the test naturally because the test sits in front of every generation.

For a new brand, the test should:
- Have 3–6 items (over 6 = the model averages, doesn't follow)
- Be specific to the brand's purpose, not generic ("is it well-written?" doesn't help)
- Each item testable from the phrase alone

## Recent-quote dedup

The `<brand>-quote` step receives `recentQuotes: string[]` from the agent-runner factory (the factory queries `AgentRun.findMany(...)` for the last 30 successful runs of this agent type). Pass these to the LLM-fresh generator so it doesn't repeat — and use them to filter the seed pool so the agent doesn't pick a quote that just shipped.

```js
// In <brand>-quote step:
const recent = new Set((inputData.recentQuotes || []).map(q => q.toLowerCase().trim()));

if (wantsSeed) {
  const pool = BRAND_CATEGORIES[category].quotes.filter(
    q => !recent.has(q.toLowerCase().trim())
  );
  if (pool.length > 0) {
    return { quote: pickRandom(pool), category, mode: 'seed', tone };
  }
  // Pool exhausted — fall through to LLM
}
const fresh = await generateBrandQuote(category, inputData.recentQuotes || [], pillar);
return { quote: fresh, category, mode: 'llm', tone };
```

Seed pool exhaustion is automatic: when all of a category's quotes are in the recent list, the agent falls through to LLM-fresh. With 30 recents and a 50-quote seed pool spanning 5 categories, exhaustion happens for a category after ~6+ recent runs from that category — natural rotation.

## Coin-flip ratio

Default 50/50 seed-vs-LLM. The seed path produces brand-verified copy (Lori's own words for Lorignite). The LLM path explores beyond. Both stay on-brand.

If the brand owner has more than 100 quotes and wants stricter brand-voice fidelity: shift to 70/30 seed-heavy. If the brand owner wants the LLM to do more discovery: shift to 30/70 LLM-heavy. Make this an env var if needed; don't hard-code per agent.

## Don't pre-categorize what you generate

When the LLM-fresh path generates a phrase, don't have it also output the category — the category was an INPUT. Outputting and re-inputting it adds noise. Also don't have the LLM output the focal word for the image prompt — that's the decomposer mistake (see [visual-prompt-design.md](visual-prompt-design.md)). The image model picks the focal word.

The LLM-fresh function returns just `{ quote, reasoning }` and trusts the rest of the pipeline.
