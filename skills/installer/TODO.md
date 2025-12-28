# Installer Skill TODO

## Add MathJax Support to MkDocs Template

**Priority:** Medium
**Added:** 2025-12-28

### Description

Update the mkdocs-template.md to include MathJax configuration for LaTeX formula rendering.

### Changes Required

1. **Add to `markdown_extensions` in mkdocs.yml template:**
```yaml
  - pymdownx.arithmatex:
      generic: true
```

2. **Add to `extra_javascript` in mkdocs.yml template:**
```yaml
extra_javascript:
   - js/mathjax.js
   - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js
```

3. **Create `docs/js/mathjax.js` asset file:**
```javascript
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
```

### Usage in Markdown

- Display math: `$$F = k \frac{|q_1 q_2|}{r^2}$$`
- Inline math: `$F$`, `$k = 8.99 \times 10^9$`

### Reference

Configuration added to `intro-to-physics-course` project on 2025-12-28.
