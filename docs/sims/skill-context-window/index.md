---
title: Skill Context Window
description: Interactive p5.js visualization of skill context window concept
image: /sims/skill-context-window/skill-context-window.png
og:image: /sims/skill-context-window/skill-context-window.png
quality_score: 100
---

# Skill Context Window

<iframe src="main.html" width="100%" height="527px" scrolling="no" style="overflow: hidden;"></iframe>

[Run the Skill Context Window MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

[Edit the Skill Context Window MicroSim using the p5.js Editor](https://editor.p5js.org/dmccreary/sketches/xg5bZmxLC)

## How to Embed This MicroSim

You can include this MicroSim on your website using the following `iframe`:

```html
<iframe src="https://dmccreary.github.io/claude-skills/sims/skill-context-window/main.html" width="100%" height="527px" scrolling="no" style="overflow: hidden;"></iframe>
```

## Description

This MicroSim visualizes the **progressive disclosure** design principle used in Claude Skills. Skills use a three-level loading system to manage context efficiently and avoid overwhelming Claude's context window.

As of Claude Code 2.0.20 skill were added.

### The Three Layers

**Hover over each layer** to see detailed information about when and how it's loaded:

### Skill Frontmatter

Top Layer of MicroSim - Always Loaded into the Context Window when Claude Code Starts
Length is about ~100 tokens (130 words)

!!! warning
   There is a 30-skill hard coded maximum in the 2.0.60 release of Claude Code.
   This hard-coded maximum is NOT configurable by the user.

- Contains skill name and description
- Always in context when Claude starts
- Allows Claude to decide when to invoke the skill
- Minimal token usage

### SKILL.md File

Middle Layer of MicroSim - When Triggered <5k tokens

- Complete skill instructions and workflows
- Loaded when the skill is triggered/invoked
- Contains procedural knowledge and examples
- Moderate token usage

### Assets, References, Templates & Scripts

 Base layer of MicroSim - As Needed, Unlimited

- **Scripts** are executed without loading into context - scripts are used by Claude but not loaded into the context window
- **References** loaded when Claude determines they're needed.  This is a good place to put your rules.
- **Templates** are sample code that is used as the first version
- **Assets** are used in output such as reports

Together, these types provides large extensibility within the context window.

### Progressive Disclosure Benefits

This layered approach provides several key advantages:

- **Efficiency**: Only loads what's needed, when it's needed
- **Scalability**: Skills can have unlimited resources without context bloat
- **Performance**: Minimal startup cost with full capability available
- **Flexibility**: Claude intelligently loads additional resources on demand

### Visual Design

The triangle shape represents the progressive expansion of context:

- **Narrow top**: Minimal frontmatter (always present in the context window)
- **Medium middle**: Full SKILL.md file - fully loaded into the context window when Claude determines a skill is needed.  Provides instructions on when to use scripts, references, templates and assets
- **Wide base**: Extensive resources of scripts, references, templates and assets (loaded selectively)

The color coding indicates loading behavior:

- **Yellow**: Always in context (startup)
- **Blue**: Loaded when skill triggers (on-demand)
- **Green**: Loaded as needed (selective)

## 30-Skill Hard Coded Limit

As of December of 2025, Claude Code 2.0.60 has a hard-coded maximum of 30 skills that can be loaded into a session.

- **Hard limit:** Maximum 30 skills total (combining personal ~/.claude/skills/, project .claude/skills/, and plugin skills)
- **Silent failure:** Skills beyond this limit are silently ignored with no error message
- **Non-deterministic:** Which skills get dropped is unpredictable!

**Solution/Workaround** - you must explicitly tell Claude exactly what skill to use and the path to the skill file!

Skills use progressive disclosure to minimize context usage:

1. Frontmatter only (~100 words / ~130 tokens per skill) - always in context so Claude knows what skills are available
2. Full SKILL.md (<5k words / ~6.5k tokens) - loaded only when the skill is invoked
3. Assets/references - loaded on-demand as needed

So even with 30 skills, only the frontmatter metadata is initially consuming context tokens. The full skill content loads when Claude actually uses that skill.

Claude has also shown the ability to refactor a large number of skills into a smaller set using
a process of `skill consolidation`.  For an example see the [Claude Code Skill Session Log](https://github.com/dmccreary/claude-skills/blob/main/logs/skill-consolidation.md).  In this example, Claude successfully consolidated 40+ skills down into 16 skills.

## Lesson Plan

**Target Audience**: Developers creating Claude Skills, AI prompt engineers, educational technologists

**Learning Objectives:**

By the end of this lesson, students will be able to:

1. Understand the three-level progressive disclosure system in Claude Skills
2. Explain when each layer is loaded into Claude's context window
3. Design efficient skills that minimize context usage
4. Apply progressive disclosure principles to their own skill development
5. Recognize the benefits of layered architecture for AI agent systems

**Prerequisites:**

- Basic understanding of Claude and AI language models
- Familiarity with context windows and token limits
- Knowledge of skills or similar modular systems

**Duration**: 15-20 minutes

**Activities:**

1. **Introduction (3 minutes)**
   - Explain the challenge of context window management
   - Introduce progressive disclosure as a solution
   - Show the MicroSim

2. **Exploration Activity (7 minutes)**
   - Students hover over each layer to read the details
   - Discuss the size differences (~100 words / ~130 tokens vs <5k words / ~6.5k tokens vs unlimited)
   - Compare loading strategies (always vs triggered vs as-needed)

3. **Analysis Exercise (5 minutes)**
   - Question: "Why is the frontmatter always loaded while assets are loaded as needed?"
   - Discuss trade-offs between context usage and capability
   - Analyze real skill examples

4. **Application Activity (5 minutes)**
   - Design a hypothetical skill using the three-layer model
   - Decide what goes in each layer
   - Justify the placement decisions

**Assessment:**

- **Formative**: Monitor discussions during exploration
- **Summative**: Have students design a skill architecture
- **Extended**: Create an actual skill following the progressive disclosure pattern

**Extensions:**

- Compare progressive disclosure to other architectural patterns (monolithic, microservices)
- Explore how other AI systems manage context windows
- Investigate token economics and context optimization strategies

## Skill Design Principles

This MicroSim illustrates key principles from the skill-creator documentation:

### Progressive Disclosure

**Definition**: A three-level loading system that manages what information is in Claude's context at different stages.

**Levels**:

1. Metadata (name + description) - Always in context (~100 words / ~130 tokens)
2. SKILL.md body - When skill triggers (<5k words / ~6.5k tokens)
3. Bundled resources - As needed by Claude (unlimited*)

*Unlimited because scripts can be executed without reading into context window.

### Context Efficiency

**Why it matters**: Claude's context window is finite. Loading everything upfront would:
- Waste tokens on unused information
- Slow down processing
- Reduce capacity for actual task work
- Limit skill complexity

**How progressive disclosure helps**:
- Minimal startup cost (just metadata)
- Full capability available when needed
- Selective resource loading
- Unlimited potential complexity

### Resource Organization

**Scripts** (`scripts/`):
- Executed without loading into context
- Provide deterministic operations
- Example: Screenshot capture, file manipulation

**References** (`references/`):
- Loaded into context when Claude needs them
- Provide detailed documentation
- Example: API specs, schemas, detailed guides

**Assets** (`assets/`):
- Used in output, not loaded into context
- Provide templates and resources
- Example: Templates, boilerplate, images

## Technical Implementation

**Architecture**: Based on the knowledge-triangle MicroSim pattern
- Responsive canvas design (width-responsive)
- Three-layer triangle visualization
- Interactive hover detection
- Informative popup boxes

**Key Features**:
- Clean, text-only layers (no background objects)
- Color-coded loading strategies
- Context-sensitive hover information
- Professional educational design

**p5.js Techniques**:
- Triangle geometry calculations
- Point-in-polygon detection
- Dynamic text wrapping
- Responsive canvas sizing

## References

1. [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills) - Official documentation for Claude Code skills
2. [GitHub Issue #13343: Skills truncated at 30 makes remaining skills undiscoverable](https://github.com/anthropics/claude-code/issues/13343) - Bug report documenting the 30-skill hard limit
3. [GitHub Issue #13344: Plugin enable/disable ignored - all skills loaded regardless of settings](https://github.com/anthropics/claude-code/issues/13344) - Related bug that can cause unexpected skill accumulation
4. [Skill Creator Skill](https://github.com/dmccreary/claude-skills) - The skill that creates other skills, demonstrates progressive disclosure
5. [Progressive Disclosure (Nielsen Norman Group)](https://www.nngroup.com/articles/progressive-disclosure/) - 2006 - UX design pattern for managing complexity
6. [Context Window Management in LLMs](https://www.anthropic.com/index/100k-context-windows) - 2023 - Anthropic - Technical background on context windows
7. [Modular Design Patterns](https://en.wikipedia.org/wiki/Modular_programming) - Wikipedia - Software architecture patterns for managing complexity