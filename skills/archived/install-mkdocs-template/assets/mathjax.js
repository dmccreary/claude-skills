/**
 * MathJax configuration for MkDocs Material
 *
 * This file configures MathJax for rendering LaTeX math expressions.
 * Place this file in docs/javascripts/mathjax.js
 *
 * Usage in markdown:
 *   Inline math: $x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$
 *   Block math:
 *   $$
 *   E = mc^2
 *   $$
 */

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})
