# Agent Skill Portability Strategy

## CLAUDE.md vs AGENTS.md

All systems use the AGENTS.md file except Claude Code.  Claude can be configured to look at the AGENTS.md file.

The home page of a project must have one of these two files and they are often read by other agents.
They are really two names for the same set of instructions for all agents.
There are many options with tradeoffs:

1. **Symbolic Links** - MicroSoft Windows must be configured to support these links
2. **Hard Links** - allows updates on one to automatically appear in the other
3. **Include instruction** - Claude can be instructed to automatically include the AGENTS.md

```markdown
@AGENTS.md
```

Note that the last option is both visible and easy to implement.

## Image Generation

Claude does not have any image generation capability other than generating SVG images.  These images are not appropriate for many application.  Claude Fable can generate better lineart but this
is VERY token expensive.

## Image Understanding

Claude 5.0 models currently have vastly superior ability to analyze what is in an image.
This is VERY critical for adjusting user interface layout.

See the layout reviewer feature in the microsim-uitls skill: skills/microsim-utils/references/visual-checklist.md