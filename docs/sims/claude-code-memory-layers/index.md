---
title: Claude Code Memory Layers
description: An interactive infographic showing the five memory layers in Claude Code, how they load, and how higher-priority rules override lower-priority ones.
image: /sims/claude-code-memory-layers/claude-code-memory-layers.png
og:image: /sims/claude-code-memory-layers/claude-code-memory-layers.png
twitter:image: /sims/claude-code-memory-layers/claude-code-memory-layers.png
social:
   cards: false
---

# Claude Code Memory Layers

<iframe src="main.html" height="602px" width="100%" scrolling="no"></iframe>

[Run the Claude Code Memory Layers MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## About This Infographic

This interactive visualization demonstrates how Claude Code manages its memory hierarchy through five distinct layers. Each layer serves a specific purpose and has different sharing scopes.

## How to Use

1. **Click "Play Animation"** to watch how Claude Code loads rules from each layer sequentially
2. **Hover over any layer** to see detailed information including:
   - File locations for different operating systems
   - Purpose and use case examples
   - Who the rules are shared with
   - Example rules for that layer
3. **Watch the override example** that appears after the animation completes

## The Five Memory Layers

| Priority | Layer | Location | Shared With |
|----------|-------|----------|-------------|
| 1 (Highest) | Enterprise Policy | System directories | All org users |
| 2 | Project Memory | `./CLAUDE.md` | Team (via git) |
| 3 | Project Rules | `./.claude/rules/*.md` | Team (via git) |
| 4 (Lowest) | User Memory | `~/.claude/CLAUDE.md` | Just you |
| N/A | Project Local | `./CLAUDE.local.md` | Just you (gitignored) |

## Key Concepts

### Rule Override Behavior

Higher priority rules **override** lower priority rules when there's a conflict. For example:

- Your **User Memory** might specify: `"Use 2-space indentation"`
- But the **Project Memory** specifies: `"Use 4-space indentation"`
- **Result**: Claude uses 4-space indentation because Project Memory has higher priority

### Loading Order

Claude Code reads memory files in priority order:

1. Enterprise Policy loads first (if present)
2. Project Memory loads next
3. Project Rules are loaded
4. User Memory preferences are applied
5. Project Local settings are applied last

Despite loading last, lower-priority files have lower precedence - they fill in gaps but don't override higher-priority settings.

## Embed This MicroSim

You can include this MicroSim on your website using the following `iframe`:

```html
<iframe src="https://dmccreary.github.io/claude-skills/sims/claude-code-memory-layers/main.html"
        height="602px"
        width="100%"
        scrolling="no"></iframe>
```

## References

- [Claude Code Memory Documentation](https://code.claude.com/docs/en/memory)
- [Claude Code Official Documentation](https://docs.anthropic.com/claude-code)

## Lesson Plan

### Learning Objectives

By using this MicroSim, students will be able to:

1. **Remember** the five memory layers and their priority order
2. **Understand** how rule override works between layers
3. **Apply** knowledge to configure their own Claude Code environment
4. **Analyze** which layer is appropriate for different types of rules

### Discussion Questions

1. Why might an organization want to use Enterprise Policy rules?
2. When should you use Project Rules vs. Project Memory?
3. What types of preferences belong in User Memory vs. Project Local?
4. How does the gitignore behavior of `CLAUDE.local.md` affect team collaboration?

### Hands-On Activity

1. Create a `~/.claude/CLAUDE.md` file with a personal preference
2. Create a project `./CLAUDE.md` that overrides that preference
3. Observe which rule Claude follows

---

*Remember to create a screenshot image (`claude-code-memory-layers.png`) for social media previews.*
