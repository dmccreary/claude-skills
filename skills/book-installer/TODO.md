# Installer Skill TODO

Create a .gitignore

```
site
.cache
.DS_Store
~$*
```

The `site` is never checked into the main branch.  It is pushed to the gh-deploy branch by the
`mkdocs gh-deploy` command.

The `.cache` is for the social medial images and should not be in the main branch.
.DS_Store is for the MacOS

The ~$* is for MicroSoft PowerPoint backup files


Create a VSCode workspace

**IMPORTANT:** Do NOT include `processHtmlClass: "arithmatex"` - this restricts MathJax to only process arithmatex-wrapped content and breaks `$`/`$$` delimiter support. Without this restriction, MathJax scans the entire page for all configured delimiters.

### Usage in Markdown

- Display math: `$$F = k \frac{|q_1 q_2|}{r^2}$$`
- Inline math: `$F$`, `$k = 8.99 \times 10^9$`
- Alternative display: `\[...\]`
- Alternative inline: `\(...\)`

### Reference

- Configuration added to `intro-to-physics-course` project on 2025-12-28.
- Configuration corrected based on `search-microsims` project on 2026-01-25. Key fix: removed `processHtmlClass` restriction to enable `$`/`$$` support.
