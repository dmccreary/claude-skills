#!/usr/bin/env node
// Scaffold a multi-brand sticker agent in a shilpiworks-style codebase.
//
// Generates the 9 brand-specific files needed (data, anchors dir, steps,
// workflow, agent runner, route, trigger script, batch script, storefront
// page) with placeholder content + TODO markers. Customize each per the
// brand kit. Read references/visual-prompt-design.md, references/quote-
// generation-design.md, and references/threading.md before customizing.
//
// Usage:
//   node scaffold-brand-agent.mjs \
//     --brand <kebab-name> \
//     --watermark-url <brand>.com \
//     --tagline "<short tagline>" \
//     --primary-color "#XXYYZZ" \
//     --type-color "#XXYYZZ" \
//     --accent-color "#XXYYZZ" \
//     --repo-root <path/to/shilpiworks-repo>
//
// PREREQUISITES (in the target repo, see references/threading.md):
//   - agent-runner.js accepts brand, watermarkText, qaResult config
//   - publish.js threads those through to features.brand + isActive
//   - watermark.js takes watermarkText as a param
// If those aren't already in place, do them once first.
//
// AFTER RUNNING:
//   1. Drop seed quotes into data/<brand>-quotes.js
//   2. Drop anchor image(s) into anchors/<brand>/
//   3. Customize the structured-block image prompt in <brand>-steps.js
//   4. Customize the brand voice in generate<Brand>Quote
//   5. Add the registration line to agents.js (the script prints the line)
//   6. Optionally run stochastic-image-qa-gate's scaffolder to add a QA step
//   7. Test: node scripts/trigger-<brand>.js

import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

function parseArgs(argv) {
  const args = {
    brand: null,
    watermarkUrl: null,
    tagline: '',
    primaryColor: '#121B31',
    typeColor: '#F7F7F7',
    accentColor: '#D0E156',
    repoRoot: null,
    help: false,
  };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--help' || a === '-h') args.help = true;
    else if (a === '--brand' && argv[i + 1]) args.brand = argv[++i];
    else if (a === '--watermark-url' && argv[i + 1]) args.watermarkUrl = argv[++i];
    else if (a === '--tagline' && argv[i + 1]) args.tagline = argv[++i];
    else if (a === '--primary-color' && argv[i + 1]) args.primaryColor = argv[++i];
    else if (a === '--type-color' && argv[i + 1]) args.typeColor = argv[++i];
    else if (a === '--accent-color' && argv[i + 1]) args.accentColor = argv[++i];
    else if (a === '--repo-root' && argv[i + 1]) args.repoRoot = argv[++i];
    else { console.error(`Unknown arg: ${a}`); args.help = true; }
  }
  return args;
}

function printHelp() {
  console.log(`scaffold-brand-agent.mjs — generate boilerplate for a brand sticker agent

USAGE
  node scaffold-brand-agent.mjs --brand <name> --watermark-url <domain> [--repo-root <path>] [other opts]

REQUIRED FLAGS
  --brand              Brand name in kebab-case (e.g. "ourbrand", "acme-cards")
  --watermark-url      Domain for the edge watermark (e.g. "ourbrand.com")
  --repo-root          Path to the shilpiworks-style repo root

OPTIONAL FLAGS
  --tagline            Brand tagline (used in storefront hero)
  --primary-color      Sticker fill hex (default: #121B31 navy)
  --type-color         Primary type hex (default: #F7F7F7 soft white)
  --accent-color       Accent / focal-script hex (default: #D0E156 lime)

GENERATES (under <repo-root>/frontend/...):
  lib/mastra/data/<brand>-quotes.js          — empty seed pool, customize
  lib/mastra/anchors/<brand>/                — empty dir, drop refs
  lib/mastra/<brand>-steps.js                — Mastra steps + helpers
  lib/mastra/<brand>-workflow.js             — workflow chain
  lib/mastra/<brand>.js                      — createAgentRunner config
  app/api/agent/<brand>/route.js             — HTTP endpoint
  scripts/trigger-<brand>.js                 — manual trigger
  scripts/batch-<brand>.mjs                  — batch runner
  app/<brand>/page.js                        — collection storefront

PRINTS one line to add manually to:
  app/api/telegram/run-agent/agents.js       — registry entry
`);
}

function pascal(kebab) {
  return kebab.split('-').map(p => p[0].toUpperCase() + p.slice(1)).join('');
}

function camel(kebab) {
  return kebab.split('-').map((p, i) => i === 0 ? p : p[0].toUpperCase() + p.slice(1)).join('');
}

function envName(kebab) {
  return kebab.toUpperCase().replace(/-/g, '_');
}

function ensureDir(p) {
  fs.mkdirSync(p, { recursive: true });
}

function writeIfMissing(filePath, content) {
  if (fs.existsSync(filePath)) {
    console.log(`  · skipped (exists): ${path.relative(process.cwd(), filePath)}`);
    return false;
  }
  ensureDir(path.dirname(filePath));
  fs.writeFileSync(filePath, content);
  console.log(`  ✓ wrote: ${path.relative(process.cwd(), filePath)}`);
  return true;
}

function templates({ brand, watermarkUrl, tagline, primaryColor, typeColor, accentColor }) {
  const Pascal = pascal(brand);   // e.g. "Ourbrand"
  const cam = camel(brand);       // e.g. "ourbrand"
  const envP = envName(brand);    // e.g. "OURBRAND"

  return {
    quotesData: `// ${brand} seed-quote pool — customize with the brand owner's phrases.
// Categorize by TONE (not topic). 3-7 categories of 5-15 quotes each is the
// sweet spot. The agent picks a random category per run, then 50/50 between
// pulling a seed quote vs LLM-fresh generation.
//
// CUSTOMIZE: tone strings get injected into the LLM-fresh generator's
// system prompt — write them carefully even if you don't expect to use the
// LLM path heavily.

export const ${envP}_CATEGORIES = {
  'Category A': {
    tone: 'TODO: describe how phrases in this category sound',
    quotes: [
      // 'Phrase 1',
      // 'Phrase 2',
    ],
  },
  // 'Category B': { ... },
};

export const ${envP}_ALL_QUOTES = Object.entries(${envP}_CATEGORIES).flatMap(
  ([category, { quotes }]) => quotes.map(quote => ({ quote, category }))
);
`,

    stepsFile: `// ${brand} agent — workflow steps.
//
// CUSTOMIZE:
//   1. The brand-voice generateBrandQuote system prompt below
//   2. The structured-block image prompt in build${Pascal}ImagePrompt
//   3. (Optional) Wire in a visual-QA step from stochastic-image-qa-gate skill
//
// See ~/.claude/skills/brand-sticker-agent/references/visual-prompt-design.md
// for the structured-block prompt format.

import { createStep } from '@mastra/core/workflows';
import { z } from 'zod';
import { ${envP}_CATEGORIES } from './data/${brand}-quotes.js';

const CATEGORY_KEYS = Object.keys(${envP}_CATEGORIES);

// ─── LLM-fresh quote generator ───────────────────────────────────────────────
// CUSTOMIZE the systemPrompt for the brand voice + brand test.
// See references/quote-generation-design.md for the brand-test pattern.

export async function generate${Pascal}Quote(category, recentQuotes = []) {
  const apiKey = process.env.GOOGLE_API_KEY;
  if (!apiKey) throw new Error('GOOGLE_API_KEY not set');

  const cat = ${envP}_CATEGORIES[category];
  if (!cat) throw new Error(\`generate${Pascal}Quote: unknown category "\${category}"\`);

  const seedExamples = cat.quotes.slice(0, 6).map(q => \`"\${q}"\`).join(', ');
  const recentList = recentQuotes.length > 0
    ? \`\\n\\nDO NOT use any of these recently produced phrases:\\n\${recentQuotes.map(q => \`  - "\${q}"\`).join('\\n')}\`
    : '';

  const systemPrompt = \`You are the in-house copywriter for ${brand}.

[TODO: BRAND CORE — belief, voice, audience, what to avoid]

THE ${envP} TEST (the phrase must pass all of these):
  - [TODO: test item 1]
  - [TODO: test item 2]
  - [TODO: test item 3]

CATEGORY: \${category}
CATEGORY TONE: \${cat.tone}
EXAMPLES IN THIS CATEGORY (for register, do NOT copy): \${seedExamples}

CONSTRAINTS:
  - 2-6 words ideal; never more than 8.
  - No emojis. No hashtags. No URLs.
  - The phrase should feel like something the brand owner would actually say.\${recentList}

Return JSON with the phrase and a one-line reasoning.\`;

  const userPrompt = \`Generate one fresh sticker phrase for the "\${category}" category.\`;

  const schema = {
    type: 'OBJECT',
    properties: {
      quote: { type: 'STRING' },
      reasoning: { type: 'STRING' },
    },
    required: ['quote'],
  };

  const data = await callGeminiFlashJson({ systemPrompt, userPrompt, schema, temperature: 0.85 });
  return data.quote.trim();
}

// ─── Structured-block image prompt ───────────────────────────────────────────
// CUSTOMIZE: this is where the brand visual identity gets encoded.
// See references/visual-prompt-design.md for the canonical Lorignite example
// and the design framework.

export function build${Pascal}ImagePrompt({ quote }) {
  return \`STICKER (the sticker IS this object — read this first):
[TODO: one-paragraph description of the brand's signature look]

ERA: [TODO: visual era / register]

TEXT TO RENDER (letter-perfect, every letter spelled correctly):
The phrase: "\${quote}"
The brandmark: "${brand}"
Nothing else. No URLs, no hashtags, no extra words.

TYPOGRAPHY — YOU DECIDE THE FOCAL WORD:
Render the phrase as TWO COMPLEMENTARY STYLES, balanced together:
  • Choose EXACTLY ONE word from the phrase to be the FOCAL element. Pick the most emotionally resonant or compositionally interesting word — typically the punch noun, the vivid verb, or the surprise/action word.
  • The FOCAL word is rendered in [TODO: focal treatment, e.g. "HANDWRITTEN FLOWING SCRIPT in ${accentColor}"].
  • EVERY OTHER word is rendered in [TODO: other treatment, e.g. "BOLD SANS-SERIF ALL-CAPS in ${typeColor}"].
  • CRITICAL: the focal word is rendered EXACTLY ONCE — never as both caps AND script.
  • The brandmark "${brand}" sits in a clearly bounded bottom-right inset zone.

PALETTE (strict — no other colors except those listed):
  • Sticker fill: ${primaryColor}
  • Primary type: ${typeColor}
  • Accent / focal: ${accentColor}
  • Background OUTSIDE the sticker: pure white RGB(255,255,255)

ICONS:
[TODO: icon vocabulary + placement rules]

COMPOSITION:
Centered. [TODO: die-cut shape spec — blob, circle, irregular silhouette].

TONE: [TODO: 1-2 sentences on emotional register]

NEGATIVES (specific failure modes to avoid — every one matters):
  • The focal word appearing TWICE — once in caps and once in script
  • Any word from the phrase rendered more than once
  • [TODO: brand-specific failure modes seen in production]
  • More than one sticker in the image
  • URLs, watermarks, or copyright text (added downstream)\`;
}

// ─── Internal: shared Gemini Flash JSON caller with retry/backoff ────────────

async function callGeminiFlashJson({ systemPrompt, userPrompt, schema, temperature = 0.4 }) {
  const apiKey = process.env.GOOGLE_API_KEY;
  const MAX_ATTEMPTS = 5;
  let res;
  let lastBody = '';
  for (let attempt = 1; attempt <= MAX_ATTEMPTS; attempt++) {
    res = await fetch(
      \`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=\${apiKey}\`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          systemInstruction: { parts: [{ text: systemPrompt }] },
          contents: [{ parts: [{ text: userPrompt }] }],
          generationConfig: {
            responseMimeType: 'application/json',
            responseSchema: schema,
            temperature,
          },
        }),
      },
    );
    if (res.ok) break;
    lastBody = await res.text();
    const retriable = res.status === 429 || res.status === 503;
    if (!retriable || attempt === MAX_ATTEMPTS) {
      throw new Error(\`Gemini Flash error \${res.status}: \${lastBody}\`);
    }
    await new Promise(r => setTimeout(r, Math.min(1000 * 2 ** (attempt - 1), 16000)));
  }
  const data = await res.json();
  const text = data.candidates?.[0]?.content?.parts?.[0]?.text || '';
  return JSON.parse(text.replace(/\`\`\`json\\n?|\`\`\`/g, '').trim());
}

// ─── Mastra step: ${brand}-quote ─────────────────────────────────────────────

export const ${cam}QuoteStep = createStep({
  id: '${brand}-quote',
  inputSchema: z.object({
    recentQuotes: z.array(z.string()).default([]),
    quoteOverride: z.string().optional(),
    categoryOverride: z.string().optional(),
    modeOverride: z.enum(['seed', 'llm']).optional(),
  }),
  outputSchema: z.object({
    quote: z.string(),
    category: z.string(),
    mode: z.enum(['seed', 'llm', 'override']),
    tone: z.string(),
  }),
  execute: async ({ inputData }) => {
    const recent = new Set((inputData.recentQuotes || []).map(q => q.toLowerCase().trim()));

    if (inputData.quoteOverride) {
      const category = (inputData.categoryOverride && CATEGORY_KEYS.includes(inputData.categoryOverride))
        ? inputData.categoryOverride
        : pickRandom(CATEGORY_KEYS);
      return {
        quote: inputData.quoteOverride,
        category,
        mode: 'override',
        tone: ${envP}_CATEGORIES[category].tone,
      };
    }

    const category = (inputData.categoryOverride && CATEGORY_KEYS.includes(inputData.categoryOverride))
      ? inputData.categoryOverride
      : pickRandom(CATEGORY_KEYS);

    const wantsSeed = inputData.modeOverride === 'seed'
      || (inputData.modeOverride !== 'llm' && Math.random() < 0.5);

    if (wantsSeed) {
      const pool = ${envP}_CATEGORIES[category].quotes.filter(
        q => !recent.has(q.toLowerCase().trim())
      );
      if (pool.length > 0) {
        return {
          quote: pickRandom(pool),
          category,
          mode: 'seed',
          tone: ${envP}_CATEGORIES[category].tone,
        };
      }
      console.log(\`Agent (${brand}): seed pool for "\${category}" exhausted — falling through to LLM\`);
    }

    const fresh = await generate${Pascal}Quote(category, inputData.recentQuotes || []);
    return {
      quote: fresh,
      category,
      mode: 'llm',
      tone: ${envP}_CATEGORIES[category].tone,
    };
  },
});

// ─── Mastra step: build-prompt ───────────────────────────────────────────────
// id MUST be exactly 'build-prompt' for the agent-runner factory to extract it

export const build${Pascal}ImagePromptStep = createStep({
  id: 'build-prompt',
  inputSchema: z.object({
    quote: z.string(),
    category: z.string(),
    mode: z.enum(['seed', 'llm', 'override']),
    tone: z.string(),
  }),
  outputSchema: z.object({
    designPrompt: z.string(),
    context: z.string(),
  }),
  execute: async ({ inputData }) => {
    const designPrompt = build${Pascal}ImagePrompt({ quote: inputData.quote });
    const context = \`${brand} sticker (\${inputData.category}, \${inputData.mode}-sourced quote): "\${inputData.quote}".\`;
    return { designPrompt, context };
  },
});

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}
`,

    workflowFile: `// ${brand} — Mastra workflow.
//
// Pipeline: ${brand}-quote → build-prompt → generate-image-gemini
//
// To add a visual-QA gate, run the stochastic-image-qa-gate skill's
// scaffolder and splice the generated step in after generate-image-gemini.
// See its references/threading.md.

import { createWorkflow } from '@mastra/core/workflows';
import { z } from 'zod';
import { ${cam}QuoteStep, build${Pascal}ImagePromptStep } from './${brand}-steps.js';
import { generateImageStepGemini } from './steps.js';

export const ${cam}Workflow = createWorkflow({
  id: '${brand}-sticker',
  inputSchema: z.object({
    recentQuotes: z.array(z.string()).default([]),
    quoteOverride: z.string().optional(),
    categoryOverride: z.string().optional(),
    modeOverride: z.enum(['seed', 'llm']).optional(),
  }),
  outputSchema: z.object({
    base64: z.string(),
    analysis: z.any(),
  }),
})
  .then(${cam}QuoteStep)
  .then(build${Pascal}ImagePromptStep)
  .map(async ({ inputData, getStepResult }) => {
    const quoteOut = getStepResult('${brand}-quote');
    return {
      designPrompt: inputData.designPrompt,
      context: inputData.context,
      anchorSet: '${brand}',
      thinkingLevel: 'high',
      fallbackMetadata: {
        theme: '${Pascal}',
        visualConcept: '${brand}-typographic-poster',
        keyword: quoteOut?.quote || '',
        agentType: '${brand}',
      },
    };
  })
  .then(generateImageStepGemini)
  .commit();
`,

    runnerFile: `// ${brand} sticker agent.

import { createAgentRunner } from './agent-runner.js';
import { ${cam}Workflow } from './${brand}-workflow.js';

export const run${Pascal}Agent = createAgentRunner({
  type: '${brand}',
  theme: '${Pascal}',
  defaultStyle: '${brand}-typographic-poster',
  workflowName: '${cam}Workflow',
  workflow: ${cam}Workflow,
  quoteStepId: '${brand}-quote',
  brand: '${brand}',
  watermarkText: '© ${watermarkUrl}',
  requiredTags: ['${Pascal}'],
  buildExtraResult: (quoteResult) => ({
    category: quoteResult?.category,
    mode: quoteResult?.mode,
    tone: quoteResult?.tone,
  }),
});
`,

    routeFile: `import { NextResponse } from 'next/server';
import { run${Pascal}Agent } from '../../../../lib/mastra/${brand}.js';
import { gateGetToCronOnly, readOptionalJsonBody, validateAgentRequestAuth } from '../route-utils.js';

export const maxDuration = 600;
export const dynamic = 'force-dynamic';

export async function POST(request) {
  const authError = await validateAgentRequestAuth(request);
  if (authError) return authError;

  const body = await readOptionalJsonBody(request);

  try {
    const result = await run${Pascal}Agent({
      quoteOverride: body.quoteOverride,
      categoryOverride: body.categoryOverride,
      modeOverride: body.modeOverride,
    });
    return NextResponse.json(result);
  } catch (err) {
    console.error('${brand} agent error:', err);
    return NextResponse.json({ error: err.message }, { status: 500 });
  }
}

export async function GET(request) {
  const denied = gateGetToCronOnly(request);
  if (denied) return denied;
  return POST(request);
}
`,

    triggerFile: `import { run${Pascal}Agent } from '../lib/mastra/${brand}.js';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: path.resolve(__dirname, '../.env.local') });
dotenv.config({ path: path.resolve(__dirname, '../../backend/.env'), override: false });

function parseArgs(argv) {
  const out = {};
  for (let i = 2; i < argv.length; i++) {
    const flag = argv[i];
    const val = argv[i + 1];
    if (flag === '--quote' && val) { out.quoteOverride = val; i++; }
    else if (flag === '--category' && val) { out.categoryOverride = val; i++; }
    else if (flag === '--mode' && (val === 'seed' || val === 'llm')) { out.modeOverride = val; i++; }
  }
  return out;
}

async function main() {
  const opts = parseArgs(process.argv);
  console.log('🚀 Triggering ${brand} agent...');
  if (Object.keys(opts).length > 0) console.log('   overrides:', opts);
  try {
    const result = await run${Pascal}Agent(opts);
    console.log('✅ ${brand} agent run successful');
    console.log(JSON.stringify(result, null, 2));
  } catch (err) {
    console.error('❌ ${brand} agent run failed');
    console.error(err);
    process.exit(1);
  }
}

main();
`,

    batchFile: `// ${brand} starter-batch runner.
//
// Usage: node scripts/batch-${brand}.mjs [count] [--pause-ms <ms>]

import { run${Pascal}Agent } from '../lib/mastra/${brand}.js';
import dotenv from 'dotenv';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
dotenv.config({ path: path.resolve(__dirname, '../.env.local') });
dotenv.config({ path: path.resolve(__dirname, '../../backend/.env'), override: false });

function parseArgs(argv) {
  let count = 10;
  let pauseMs = 4000;
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (/^\\d+$/.test(a)) count = parseInt(a, 10);
    else if (a === '--pause-ms' && argv[i + 1]) { pauseMs = parseInt(argv[++i], 10); }
  }
  return { count, pauseMs };
}

async function main() {
  const { count, pauseMs } = parseArgs(process.argv);
  console.log(\`🚀 ${brand} batch — \${count} runs, \${pauseMs}ms inter-run pause\`);

  for (let i = 1; i <= count; i++) {
    const tStart = Date.now();
    console.log(\`[\${i}/\${count}] starting…\`);
    try {
      const r = await run${Pascal}Agent({});
      const elapsed = ((Date.now() - tStart) / 1000).toFixed(1);
      console.log(\`[\${i}/\${count}] ✓ \${r.title} (\${elapsed}s) — \${r.imageUrl}\`);
    } catch (err) {
      console.warn(\`[\${i}/\${count}] ✗ failed: \${err.message}\`);
    }
    if (i < count && pauseMs > 0) {
      await new Promise(r => setTimeout(r, pauseMs));
    }
  }
}

main().catch(err => { console.error('Fatal:', err); process.exit(1); });
`,

    storefrontFile: `import Link from 'next/link';
import prisma from '@/lib/prisma';
import ProductCard from '@/components/ProductCard';
import { absoluteUrl } from '@/lib/site';
import { safeJsonLd } from '@/lib/safe-jsonld';

export const revalidate = 60;

const ${envP}_PRIMARY = '${primaryColor}';
const ${envP}_TYPE = '${typeColor}';
const ${envP}_ACCENT = '${accentColor}';

async function get${Pascal}Products() {
  try {
    const products = await prisma.product.findMany({
      where: { isActive: true },  // QA-killed products are inactive — preserved but hidden
      orderBy: { createdAt: 'desc' },
    });
    return products
      .map(p => {
        let parsed = null;
        try { parsed = p.features ? JSON.parse(p.features) : null; } catch {}
        return { ...p, features: parsed, image_url: p.imageUrl };
      })
      .filter(p => p.features?.brand === '${brand}');
  } catch (err) {
    console.error('${brand} collection: fetch failed', err);
    return [];
  }
}

export default async function ${Pascal}Page() {
  const products = await get${Pascal}Products();

  const collectionPageJsonLd = {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    name: '${Pascal} — Stickers',
    description: '${tagline || `Stickers from ${Pascal}`}',
    url: absoluteUrl('/${brand}'),
    mainEntity: {
      '@type': 'ItemList',
      numberOfItems: products.length,
      itemListElement: products.slice(0, 20).map((product, index) => ({
        '@type': 'ListItem',
        position: index + 1,
        url: absoluteUrl(\`/products/\${product.slug || product.id}\`),
        name: product.name,
      })),
    },
  };

  return (
    <div style={{ background: ${envP}_PRIMARY, minHeight: '100vh' }}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: safeJsonLd(collectionPageJsonLd) }}
      />

      <header className="container mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-12 text-center">
        <p
          className="text-sm font-bold uppercase tracking-[0.25em] mb-6"
          style={{ color: ${envP}_ACCENT }}
        >
          ${Pascal}
        </p>
        <h1 className="text-5xl sm:text-6xl font-black tracking-tight" style={{ color: ${envP}_TYPE }}>
          ${tagline || `${Pascal} Stickers`}
        </h1>
        <p className="mt-3 text-sm" style={{ color: ${envP}_TYPE, opacity: 0.6 }}>
          Visit{' '}
          <a href="https://${watermarkUrl}" target="_blank" rel="noopener noreferrer" style={{ color: ${envP}_ACCENT, textDecoration: 'underline' }}>
            ${watermarkUrl}
          </a>
        </p>
      </header>

      <section className="container mx-auto px-4 sm:px-6 lg:px-8 pb-20">
        {products.length > 0 ? (
          <div
            className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 rounded-xl p-6"
            style={{ background: ${envP}_TYPE }}
          >
            {products.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        ) : (
          <div className="text-center py-16 rounded-xl" style={{ background: 'rgba(255,255,255,0.05)' }}>
            <p style={{ color: ${envP}_TYPE, opacity: 0.85 }} className="text-lg">
              The first batch is being printed. Check back soon.
            </p>
          </div>
        )}
      </section>

      <footer className="border-t border-white/10">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-8 flex items-center justify-between">
          <Link href="/" className="text-sm" style={{ color: ${envP}_TYPE, opacity: 0.6 }}>← Home</Link>
        </div>
      </footer>
    </div>
  );
}

export async function generateMetadata() {
  const title = '${Pascal} — Stickers';
  const description = '${tagline || `Stickers from ${Pascal}`}';
  return {
    title,
    description,
    alternates: { canonical: absoluteUrl('/${brand}') },
    openGraph: { title, description, url: absoluteUrl('/${brand}'), type: 'website' },
    twitter: { card: 'summary', title, description },
  };
}
`,

    registryLine: `  '${brand}': () => import('@/lib/mastra/${brand}.js').then(m => m.run${Pascal}Agent),`,
  };
}

function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.brand || !args.watermarkUrl || !args.repoRoot) {
    printHelp();
    process.exit(args.help ? 0 : 1);
  }

  if (!/^[a-z][a-z0-9-]*$/.test(args.brand)) {
    console.error(`--brand must be kebab-case. Got: ${args.brand}`);
    process.exit(1);
  }

  if (!fs.existsSync(args.repoRoot)) {
    console.error(`--repo-root does not exist: ${args.repoRoot}`);
    process.exit(1);
  }

  const t = templates(args);
  const root = args.repoRoot;
  const fe = path.join(root, 'frontend');

  if (!fs.existsSync(fe)) {
    console.error(`Expected ${fe} to exist (shilpiworks-style repo with frontend/). Got: ${args.repoRoot}`);
    process.exit(1);
  }

  console.log(`Scaffolding ${args.brand} sticker agent into ${fe}/...`);
  console.log('');

  writeIfMissing(path.join(fe, 'lib/mastra/data', `${args.brand}-quotes.js`), t.quotesData);
  ensureDir(path.join(fe, 'lib/mastra/anchors', args.brand));
  console.log(`  ✓ created dir: lib/mastra/anchors/${args.brand}/`);
  writeIfMissing(path.join(fe, 'lib/mastra', `${args.brand}-steps.js`), t.stepsFile);
  writeIfMissing(path.join(fe, 'lib/mastra', `${args.brand}-workflow.js`), t.workflowFile);
  writeIfMissing(path.join(fe, 'lib/mastra', `${args.brand}.js`), t.runnerFile);
  writeIfMissing(path.join(fe, 'app/api/agent', args.brand, 'route.js'), t.routeFile);
  writeIfMissing(path.join(fe, 'scripts', `trigger-${args.brand}.js`), t.triggerFile);
  writeIfMissing(path.join(fe, 'scripts', `batch-${args.brand}.mjs`), t.batchFile);
  writeIfMissing(path.join(fe, 'app', args.brand, 'page.js'), t.storefrontFile);

  console.log('');
  console.log('NEXT STEPS:');
  console.log('  1. Add this line to frontend/app/api/telegram/run-agent/agents.js:');
  console.log('');
  console.log(t.registryLine);
  console.log('');
  console.log('  2. Drop seed quotes into frontend/lib/mastra/data/' + args.brand + '-quotes.js');
  console.log('  3. Drop anchor image(s) into frontend/lib/mastra/anchors/' + args.brand + '/');
  console.log('  4. Customize the structured-block image prompt in frontend/lib/mastra/' + args.brand + '-steps.js');
  console.log('     (search for [TODO] markers — there are several)');
  console.log('  5. Customize the brand voice in generate' + pascal(args.brand) + 'Quote');
  console.log('  6. (Optional) Add visual-QA gate via stochastic-image-qa-gate skill');
  console.log('  7. Test: cd frontend && node scripts/trigger-' + args.brand + '.js');
}

main();
