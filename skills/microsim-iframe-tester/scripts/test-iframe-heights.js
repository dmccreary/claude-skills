#!/usr/bin/env node
/**
 * MicroSim Iframe Height Tester
 *
 * Uses Playwright to load each MicroSim's main.html inside a viewport
 * constrained to the iframe height declared in index.md, then checks
 * whether all interactive controls (buttons, sliders, selects, etc.)
 * are fully visible without clipping.
 *
 * Usage:
 *   node test-iframe-heights.js --sims-dir docs/sims [--sim name] [--height N] [--report file.md]
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// CLI argument parsing
// ---------------------------------------------------------------------------
const args = process.argv.slice(2);
function getArg(name) {
  const idx = args.indexOf(name);
  return idx !== -1 && idx + 1 < args.length ? args[idx + 1] : null;
}

const simsDir = getArg('--sims-dir') || 'docs/sims';
const singleSim = getArg('--sim');          // optional: test only one sim
const heightOverride = getArg('--height');  // optional: override all heights
const reportPath = getArg('--report');      // optional: write markdown report
const TOLERANCE = 5;   // px — controls within this margin still count as visible
const SAFETY_MARGIN = 10; // px — added to suggested height
const VIEWPORT_WIDTH = 800; // standard test width

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

/** Extract the iframe height from an index.md file. */
function extractIframeHeight(indexMdPath) {
  const content = fs.readFileSync(indexMdPath, 'utf-8');
  // Match: <iframe src="main.html" height="532" ...> or height="532px"
  const match = content.match(/<iframe[^>]*\bheight="(\d+)(px)?"/i);
  return match ? parseInt(match[1], 10) : null;
}

/** Collect MicroSim directories that contain both main.html and index.md. */
function discoverSims(baseDir) {
  if (!fs.existsSync(baseDir)) {
    console.error(`Sims directory not found: ${baseDir}`);
    process.exit(1);
  }
  const entries = fs.readdirSync(baseDir, { withFileTypes: true });
  const sims = [];
  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const dir = path.join(baseDir, entry.name);
    const hasHtml = fs.existsSync(path.join(dir, 'main.html'));
    const hasIndex = fs.existsSync(path.join(dir, 'index.md'));
    if (hasHtml && hasIndex) {
      sims.push({ name: entry.name, dir });
    }
  }
  return sims.sort((a, b) => a.name.localeCompare(b.name));
}

/** Round up to the nearest multiple of `step`. */
function roundUp(value, step) {
  return Math.ceil(value / step) * step;
}

// ---------------------------------------------------------------------------
// Main test logic
// ---------------------------------------------------------------------------
async function testSim(page, sim, iframeHeight) {
  const htmlPath = path.join(sim.dir, 'main.html');
  const fileUrl = `file://${path.resolve(htmlPath)}`;

  // Set viewport to the iframe dimensions
  await page.setViewportSize({ width: VIEWPORT_WIDTH, height: iframeHeight });

  // Navigate and wait for network idle (libraries load from CDN)
  try {
    await page.goto(fileUrl, { waitUntil: 'networkidle', timeout: 15000 });
  } catch (e) {
    return {
      sim: sim.name,
      iframeHeight,
      contentHeight: null,
      status: 'ERROR',
      suggestedHeight: null,
      clippedElements: [],
      error: `Failed to load: ${e.message}`
    };
  }

  // Give p5.js / vis-network / Chart.js a moment to render controls
  await page.waitForTimeout(2000);

  // Find all interactive controls — both p5.js-created and regular DOM
  const controlSelectors = [
    'button',
    'input[type="range"]',   // sliders
    'input[type="checkbox"]',
    'input[type="text"]',
    'input[type="number"]',
    'select',
    'textarea',
    '.p5Canvas',             // the p5.js canvas itself
    'canvas',                // any canvas element
  ];
  const selector = controlSelectors.join(', ');

  // Measure each control's position relative to the viewport
  const measurements = await page.evaluate(({ sel, viewportHeight, tolerance }) => {
    const elements = document.querySelectorAll(sel);
    const results = [];
    for (const el of elements) {
      const rect = el.getBoundingClientRect();
      // Skip invisible or zero-size elements
      if (rect.width === 0 && rect.height === 0) continue;
      if (rect.height === 0) continue;

      const bottomEdge = rect.bottom;
      const isVisible = bottomEdge <= viewportHeight + tolerance;
      const tag = el.tagName.toLowerCase();
      const type = el.getAttribute('type') || '';
      const label = el.textContent?.trim().slice(0, 30) || '';

      results.push({
        tag,
        type,
        label,
        top: Math.round(rect.top),
        bottom: Math.round(rect.bottom),
        isVisible,
      });
    }
    return results;
  }, { sel: selector, viewportHeight: iframeHeight, tolerance: TOLERANCE });

  // Find the actual content height — the bottom edge of the lowest element
  const allElements = await page.evaluate(() => {
    const body = document.body;
    const main = document.querySelector('main');
    const target = main || body;

    // Get bounding rect of the main content area
    const mainRect = target.getBoundingClientRect();

    // Also check all children for anything that extends further
    let maxBottom = mainRect.bottom;
    const allEls = target.querySelectorAll('*');
    for (const el of allEls) {
      const rect = el.getBoundingClientRect();
      if (rect.height > 0 && rect.bottom > maxBottom) {
        maxBottom = rect.bottom;
      }
    }
    return Math.round(maxBottom);
  });

  const clipped = measurements.filter(m => !m.isVisible && m.tag !== 'canvas');
  const contentHeight = allElements;
  const suggestedHeight = roundUp(contentHeight + SAFETY_MARGIN, 10);

  const status = clipped.length === 0 ? 'PASS' : 'FAIL';

  return {
    sim: sim.name,
    iframeHeight,
    contentHeight,
    status,
    suggestedHeight: status === 'FAIL' ? suggestedHeight : iframeHeight,
    clippedElements: clipped.map(c => `${c.tag}${c.type ? '[' + c.type + ']' : ''} "${c.label}" bottom=${c.bottom}px`),
    error: null,
  };
}

async function main() {
  // Discover sims
  let sims = discoverSims(simsDir);
  if (singleSim) {
    sims = sims.filter(s => s.name === singleSim);
    if (sims.length === 0) {
      console.error(`MicroSim "${singleSim}" not found in ${simsDir}`);
      process.exit(1);
    }
  }

  console.log(`Testing ${sims.length} MicroSim(s) in ${simsDir}\n`);

  // Launch browser
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const results = [];

  for (const sim of sims) {
    const iframeHeight = heightOverride
      ? parseInt(heightOverride, 10)
      : extractIframeHeight(path.join(sim.dir, 'index.md'));

    if (!iframeHeight) {
      console.log(`  SKIP  ${sim.name} — no iframe height found in index.md`);
      results.push({
        sim: sim.name,
        iframeHeight: null,
        contentHeight: null,
        status: 'SKIP',
        suggestedHeight: null,
        clippedElements: [],
        error: 'No iframe height in index.md',
      });
      continue;
    }

    process.stdout.write(`  Testing ${sim.name} (${iframeHeight}px)...`);
    const result = await testSim(page, sim, iframeHeight);
    results.push(result);

    if (result.status === 'PASS') {
      console.log(` PASS`);
    } else if (result.status === 'FAIL') {
      console.log(` FAIL — content ${result.contentHeight}px, suggest ${result.suggestedHeight}px`);
      for (const el of result.clippedElements) {
        console.log(`         Clipped: ${el}`);
      }
    } else {
      console.log(` ERROR — ${result.error}`);
    }
  }

  await browser.close();

  // Summary
  const passed = results.filter(r => r.status === 'PASS').length;
  const failed = results.filter(r => r.status === 'FAIL').length;
  const errors = results.filter(r => r.status === 'ERROR').length;
  const skipped = results.filter(r => r.status === 'SKIP').length;

  console.log(`\n--- Summary ---`);
  console.log(`  PASS: ${passed}  FAIL: ${failed}  ERROR: ${errors}  SKIP: ${skipped}  Total: ${results.length}`);

  // Generate markdown report if requested
  if (reportPath) {
    const lines = [
      '# MicroSim Iframe Height Test Report',
      '',
      `Tested: ${new Date().toISOString()}`,
      `Sims directory: \`${simsDir}\``,
      '',
      `| MicroSim | Iframe Height | Content Height | Status | Suggested Height |`,
      `|----------|---------------|----------------|--------|------------------|`,
    ];

    for (const r of results) {
      const ih = r.iframeHeight ?? '—';
      const ch = r.contentHeight ?? '—';
      const sh = r.suggestedHeight ?? '—';
      const statusEmoji = r.status === 'PASS' ? 'PASS' : r.status === 'FAIL' ? '**FAIL**' : r.status;
      lines.push(`| ${r.sim} | ${ih} | ${ch} | ${statusEmoji} | ${sh} |`);
    }

    if (failed > 0) {
      lines.push('');
      lines.push('## Failures Detail');
      lines.push('');
      for (const r of results.filter(r => r.status === 'FAIL')) {
        lines.push(`### ${r.sim}`);
        lines.push(`- Iframe height: ${r.iframeHeight}px`);
        lines.push(`- Content height: ${r.contentHeight}px`);
        lines.push(`- Suggested height: ${r.suggestedHeight}px`);
        lines.push(`- Clipped elements:`);
        for (const el of r.clippedElements) {
          lines.push(`  - ${el}`);
        }
        lines.push('');
      }
    }

    lines.push('');
    lines.push(`Summary: ${passed} pass, ${failed} fail, ${errors} error, ${skipped} skip out of ${results.length} total`);

    fs.writeFileSync(reportPath, lines.join('\n'));
    console.log(`\nReport written to ${reportPath}`);
  }

  // Exit with failure code if any tests failed
  if (failed > 0 || errors > 0) {
    process.exit(1);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(2);
});
