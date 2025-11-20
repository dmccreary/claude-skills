---
title: Skill Context Window
description: A MicroSim demonstrating the progressive disclosure principle for Claude Skills, showing how different components are loaded into context at different times.
image: skill-context-window.png
og:image: skill-context-window.png
---

# Skill Context Window

<iframe src="main.html" height="502px" width="100%" scrolling="no"></iframe>

## How to Embed This MicroSim

You can include this MicroSim on your website using the following `iframe`:

```html
<iframe src="https://dmccreary.github.io/intro-to-graph/sims/skill-context-window/main.html" height="502px" width="100%" scrolling="no"></iframe>
```

[Run the Skill Context Window MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }

## Description

This MicroSim visualizes the **progressive disclosure** design principle used in Claude Skills. Skills use a three-level loading system to manage context efficiently and avoid overwhelming Claude's context window.

### The Three Layers

**Hover over each layer** to see detailed information about when and how it's loaded:

1. **SKILL.md Frontmatter** (Top - Always Loaded ~100 words)
   - Contains skill name and description
   - Always in context when Claude starts
   - Allows Claude to decide when to invoke the skill
   - Minimal token usage

2. **SKILL.md File** (Middle - When Triggered <5k words)
   - Complete skill instructions and workflows
   - Loaded when the skill is triggered/invoked
   - Contains procedural knowledge and examples
   - Moderate token usage

3. **Assets, References, Templates & Scripts** (Base - As Needed, Unlimited)
   - Scripts can be executed without loading into context
   - References loaded when Claude determines they're needed
   - Templates and assets used in output
   - Provides unlimited extensibility

### Progressive Disclosure Benefits

This layered approach provides several key advantages:

- **Efficiency**: Only loads what's needed, when it's needed
- **Scalability**: Skills can have unlimited resources without context bloat
- **Performance**: Minimal startup cost with full capability available
- **Flexibility**: Claude intelligently loads additional resources on demand

### Visual Design

The triangle shape represents the progressive expansion of context:
- **Narrow top**: Minimal frontmatter (always present)
- **Medium middle**: Full skill file (when active)
- **Wide base**: Extensive resources (loaded selectively)

The color coding indicates loading behavior:
- **Yellow**: Always in context (startup)
- **Blue**: Loaded when skill triggers (on-demand)
- **Green**: Loaded as needed (selective)

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
   - Discuss the size differences (~100 words vs <5k words vs unlimited)
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
1. Metadata (name + description) - Always in context (~100 words)
2. SKILL.md body - When skill triggers (<5k words)
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

1. [Claude Skills Documentation](https://code.claude.com/docs/) - Official documentation for Claude Code skills
2. [Skill Creator Skill](https://github.com/dmccreary/intro-to-graph) - The skill that creates other skills, demonstrates progressive disclosure
3. [Progressive Disclosure (Nielsen Norman Group)](https://www.nngroup.com/articles/progressive-disclosure/) - 2006 - UX design pattern for managing complexity
4. [Context Window Management in LLMs](https://www.anthropic.com/index/100k-context-windows) - 2023 - Anthropic - Technical background on context windows
5. [Modular Design Patterns](https://en.wikipedia.org/wiki/Modular_programming) - Wikipedia - Software architecture patterns for managing complexity
