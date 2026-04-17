/**
 * TEMPLATE: Rich content component for a published document
 *
 * CUSTOMIZE: Replace all placeholder content with actual document content.
 * Keep the structural patterns (prose wrapper, not-prose tables, callout boxes).
 *
 * This is a React Server Component — no 'use client' needed.
 */

export default function DocumentContent() {
  return (
    <article className="prose prose-neutral dark:prose-invert max-w-none prose-headings:scroll-mt-20">
      {/* ── Hero Stats (optional — use for documents with key metrics) ── */}
      <div className="not-prose grid grid-cols-2 md:grid-cols-4 gap-4 mb-10 p-6 rounded-xl bg-neutral-50 dark:bg-neutral-800/50 border border-neutral-200 dark:border-neutral-700">
        <div className="text-center">
          <div className="text-3xl font-bold text-primary-700 dark:text-primary-400">42</div>
          <div className="text-xs text-neutral-500 mt-1">Metric Label</div>
          <div className="text-[10px] text-neutral-400">Supporting detail</div>
        </div>
        {/* Repeat for each key metric */}
      </div>

      {/* ── Section with heading ── */}
      <h2>Section Title</h2>
      <p>
        Paragraph text. Use <strong>bold</strong> for emphasis.
        Use &mdash; for em dashes, &ndash; for en dashes, &times; for
        multiplication, &apos; for apostrophes.
      </p>

      {/* ── Ordered list (for findings, recommendations) ── */}
      <h3>Key Findings</h3>
      <ol className="space-y-4">
        <li>
          <strong>Finding headline.</strong>{' '}
          Supporting detail paragraph that explains the finding.
        </li>
      </ol>

      {/* ── Data table ── */}
      {/*
        IMPORTANT: Tables must be wrapped in not-prose with explicit text colors.
        Without this, dark mode text is invisible.
      */}
      <div className="not-prose overflow-x-auto mb-8 text-neutral-700 dark:text-neutral-200">
        <table className="w-full text-sm border-collapse border border-neutral-200 dark:border-neutral-700">
          <thead>
            <tr className="bg-neutral-100 dark:bg-neutral-800">
              <th className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 text-left font-semibold text-neutral-900 dark:text-white">Column A</th>
              <th className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 text-left font-semibold text-neutral-900 dark:text-white">Column B</th>
              <th className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 text-left font-semibold text-neutral-900 dark:text-white">Column C</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 font-medium text-neutral-900 dark:text-white">Row Name</td>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2">Value</td>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2">Description</td>
            </tr>
            <tr className="bg-neutral-50 dark:bg-neutral-800/30">
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 font-medium text-neutral-900 dark:text-white">Alternating Row</td>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2">Value</td>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2">Description</td>
            </tr>
          </tbody>
        </table>
      </div>

      {/* ── Outcome metrics table (with colored result values) ── */}
      <h3>Outcome Metrics</h3>
      <div className="not-prose overflow-x-auto mb-8 text-neutral-700 dark:text-neutral-200">
        <table className="w-full text-sm border-collapse border border-neutral-200 dark:border-neutral-700">
          <thead>
            <tr className="bg-neutral-100 dark:bg-neutral-800">
              <th className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 text-left font-semibold text-neutral-900 dark:text-white">Metric</th>
              <th className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 text-left font-semibold text-neutral-900 dark:text-white">Result</th>
              <th className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 text-left font-semibold text-neutral-900 dark:text-white">vs. Baseline</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2">Metric Name</td>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2 font-medium text-emerald-700 dark:text-emerald-400">93%</td>
              <td className="border border-neutral-200 dark:border-neutral-700 px-3 py-2">+15pts vs. baseline</td>
            </tr>
          </tbody>
        </table>
      </div>

      {/* ── Callout box: Investor/Business implication ── */}
      <div className="not-prose my-6 p-5 rounded-lg bg-amber-50 dark:bg-amber-900/20 border border-amber-200 dark:border-amber-800">
        <div className="font-semibold text-amber-800 dark:text-amber-300 text-sm uppercase tracking-wide mb-2">Investor Implication</div>
        <p className="text-sm text-amber-900 dark:text-amber-200">
          Callout content for business/investor implications.
        </p>
      </div>

      {/* ── Callout box: Technical detail ── */}
      <div className="not-prose my-6 p-5 rounded-lg bg-blue-50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800">
        <div className="font-semibold text-blue-800 dark:text-blue-300 text-sm uppercase tracking-wide mb-2">Technical Detail</div>
        <p className="text-sm text-blue-900 dark:text-blue-200">
          Technical callout content with <code className="text-xs bg-blue-100 dark:bg-blue-800 px-1 rounded">inline code</code> if needed.
        </p>
      </div>

      {/* ── Callout box: Key insight / capital reallocation ── */}
      <div className="not-prose my-6 p-5 rounded-lg bg-emerald-50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800">
        <div className="font-semibold text-emerald-800 dark:text-emerald-300 text-sm uppercase tracking-wide mb-2">Key Insight</div>
        <p className="text-sm text-emerald-900 dark:text-emerald-200">
          Important insight or economic implication.
        </p>
      </div>

      {/* ── Block quote (for key questions, thesis statements) ── */}
      <p className="italic text-neutral-700 dark:text-neutral-300 border-l-4 border-primary-500 pl-4">
        A key question or thesis statement styled as a block quote.
      </p>

      {/* ── Closing section ── */}
      <div className="not-prose my-10 p-6 rounded-xl bg-neutral-100 dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 text-center">
        <p className="text-lg font-semibold text-neutral-900 dark:text-white mb-2">
          Closing statement headline.
        </p>
        <p className="text-sm text-neutral-600 dark:text-neutral-400">
          Supporting closing text.
        </p>
      </div>

      <p className="text-xs text-neutral-400 text-center mt-8">
        &copy; 2026 Organization Name. All rights reserved.
      </p>
    </article>
  )
}
