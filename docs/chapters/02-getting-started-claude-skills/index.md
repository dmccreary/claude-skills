# Getting Started with Claude and Skills

## Summary

This chapter introduces the Claude Skills system, which is the foundation for automating intelligent textbook creation. You'll learn the structure of skill definition files, including YAML frontmatter, skill names, descriptions, licenses, and allowed tools. The chapter covers how to install skills, list available skills, and invoke them using slash commands. You'll also learn about Claude Commands and understand the important differences between skills and commands.

Additionally, this chapter explores practical considerations for working with Claude, including token limits, token management strategies, and iterative prompt refinement techniques that will help you work more effectively throughout the course.

## Concepts Covered

This chapter covers the following 18 concepts from the learning graph:

1. Claude Skill
2. Skill Definition File Structure
3. YAML Frontmatter in Skills
4. Skill Name and Description
5. Skill License Information
6. Allowed Tools in Skills
7. Skill Workflow Instructions
8. Installing a Claude Skill
9. Listing Available Skills
10. Invoking Skills with Slash Commands
11. Skill Execution Context
12. Claude Command
13. Command Definition Files
14. Installing Claude Commands
15. Difference Between Skills & Commands
16. Iterative Prompt Refinement
17. Claude Token Limits
18. Token Management Strategies

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction to AI and Intelligent Textbooks](../01-intro-ai-intelligent-textbooks/index.md)

---

## Understanding Claude Skills

Claude Skills represent autonomous agents—specialized AI assistants designed to execute complex, multi-step workflows without continuous human intervention. Unlike simple prompts that request a single output, skills encapsulate comprehensive procedures including context gathering, quality validation, iterative refinement, and structured deliverable generation.

In the context of intelligent textbook creation, skills automate domain-specific tasks such as generating learning graphs from course descriptions, creating glossaries aligned with ISO 11179 metadata standards, and producing interactive quizzes distributed across Bloom's Taxonomy cognitive levels. Each skill embodies best-practice workflows developed through iterative refinement, enabling consistent, high-quality outputs even for users new to educational content creation.

The skills framework addresses a fundamental challenge in AI-assisted content generation: translating high-level goals ("create an intelligent textbook") into executable sequences of specific operations. By packaging workflow expertise into reusable skills, the framework democratizes access to sophisticated educational content creation capabilities that would otherwise require extensive prompt engineering expertise.

!!! info "Historical Context: The Evolution to Claude Skills"
    Claude Skills emerged from decades of AI research and development. To understand the technological foundations that made skills possible, explore the **[Evolution of AI: From Neural Networks to Claude Code](../../sims/claude-code-timeline/index.md)** interactive timeline. This visualization traces 52 pivotal moments from the Perceptron (1957) through transformers, large language models, and Constitutional AI, culminating in Claude Code and the official Claude Skills announcement in October 2025.

    Key milestones enabling skills:

    - **1957-2011**: Neural network foundations (backpropagation, LSTM, deep learning revival)
    - **2012-2016**: Computer vision breakthroughs (AlexNet, ResNet demonstrating deep learning power)
    - **2017-2019**: Transformer architecture enabling language understanding at scale
    - **2020-2022**: Large language models (GPT-3, ChatGPT) bringing AI to mainstream users
    - **2021-2024**: Anthropic's Constitutional AI and Claude development focusing on safety
    - **2024-2025**: Claude Code and Skills formalizing AI-assisted development workflows

    [View Interactive Timeline](../../sims/claude-code-timeline/main.html){ .md-button }

Key distinctions between skills and general prompts:

- **Workflow automation:** Skills execute multi-step procedures autonomously
- **Quality assurance:** Built-in validation checkpoints ensure outputs meet standards
- **Context management:** Skills determine which files and resources to access
- **Error handling:** Skills adapt when expected files are missing or formats differ
- **Consistency:** Repeated executions produce structurally similar outputs

## Skill Definition File Structure

Every Claude Skill is defined by a `SKILL.md` file containing both metadata (YAML frontmatter) and workflow instructions (markdown content). This standardized structure enables Claude Code to discover, load, and execute skills consistently across projects.

The canonical skill file structure follows this pattern:

```markdown
---
name: skill-name-in-kebab-case
description: One-sentence summary of what the skill does
license: MIT
allowed-tools: [Tool1, Tool2, Tool3]
---

# Skill Display Name

## Overview

Brief description of the skill's purpose and when to use it.

## When to Use This Skill

Specific scenarios where this skill applies.

## Workflow

### Step 1: First Action

Detailed instructions for the first step.

### Step 2: Second Action

Detailed instructions for the second step.

## Resources

References to supporting files, templates, or documentation.
```

The separation of metadata (YAML frontmatter) from workflow instructions (markdown body) enables both machine parsing for skill discovery and human readability for understanding and customization. Claude Code processes the YAML to determine skill identity and tool permissions, then executes the markdown workflow instructions sequentially.

<details markdown="1">
    <summary>Skill File Anatomy Diagram</summary>
    Type: diagram

    Purpose: Illustrate the structure of a SKILL.md file with labeled components

    Components to show:
    - YAML Frontmatter section (top, enclosed in --- delimiters)
      - name field
      - description field
      - license field
      - allowed-tools field (shown as array)
    - Markdown Body section (below frontmatter)
      - ## Overview heading
      - ## When to Use heading
      - ## Workflow heading with numbered steps
      - ## Resources heading
    - Annotations showing what each section controls

    Layout: Vertical document structure with left sidebar annotations

    Labels:
    - "YAML Frontmatter: Machine-readable metadata"
    - "name: Identifies skill for invocation"
    - "description: Used in skill listings"
    - "allowed-tools: Permissions for tool access"
    - "Markdown Body: Human-readable workflow"
    - "Workflow section: Step-by-step execution instructions"

    Visual style: Document mockup with syntax highlighting

    Color scheme: Yellow background for YAML section, white for markdown body, blue annotations

    Implementation: SVG diagram with code-style formatting
</details>

### YAML Frontmatter in Skills

The YAML frontmatter section provides metadata that Claude Code uses for skill discovery, permission management, and user-facing documentation. All frontmatter fields use lowercase keys and follow YAML syntax conventions.

Required frontmatter fields:

**name:** The skill identifier in kebab-case (lowercase with hyphens). Must be unique within the skills directory. Examples: `learning-graph-generator`, `quiz-generator`, `microsim-p5`

**description:** A concise (typically 1-3 sentences) summary of the skill's function. This appears in skill listings when users run `/skills` or list-skills.sh. Should clearly communicate what the skill does and when to use it.

**license:** The software license under which the skill is distributed. Common choices: MIT, Apache-2.0, CC-BY-4.0. For educational skills in this repository, MIT is standard.

Optional frontmatter fields:

**allowed-tools:** An array of tool names the skill is permitted to use. When specified, this constrains the skill to only those tools, preventing unintended file modifications or external network access. Example: `[Read, Grep, Bash]` for a skill that only needs to analyze existing files.

When `allowed-tools` is omitted, the skill has access to all tools available to Claude Code. This is appropriate for skills that need full flexibility (like the intelligent-textbook-creator skill that orchestrates multiple sub-skills), but should be avoided when narrower permissions suffice.

### Skill Name and Description

Effective skill names and descriptions follow conventions that aid discoverability and communicate purpose clearly.

**Naming conventions:**

- Use verb-noun pattern: `generate-glossary`, `create-microsim`, `analyze-quality`
- Reflect the primary output: `learning-graph-generator` produces learning graphs
- Avoid abbreviations unless universally understood
- Keep length under 40 characters for usability in listings
- Use hyphens (kebab-case), never underscores or camelCase

**Description best practices:**

- Start with present-tense verb: "Generates", "Creates", "Analyzes"
- Specify primary input and output: "Generates a comprehensive glossary from learning graph concepts"
- Include key constraints or standards: "following ISO 11179 metadata registry standards"
- Mention when to use relative to other skills: "Use after learning graph has been finalized"
- Keep under 200 characters for display in skill listings

Example skill descriptions from this repository:

- `learning-graph-generator`: "Generates a comprehensive learning graph from a course description, including 200 concepts with dependencies, taxonomy categorization, and quality validation reports."
- `glossary-generator`: "Automatically generates a comprehensive glossary of terms from a learning graph's concept list, ensuring each definition follows ISO 11179 metadata registry standards."
- `quiz-generator`: "Generates interactive multiple-choice quizzes for each chapter with questions aligned to specific concepts and distributed across Bloom's Taxonomy cognitive levels."

Notice how each description answers: What does it make? From what input? Following what standards? This clarity enables users to select the appropriate skill for their current workflow stage.

### Skill License Information

Licensing determines how skills can be shared, modified, and redistributed. For educational skills in open-source repositories, permissive licenses like MIT enable maximum adoption and customization.

The MIT License provides:

- Permission to use, copy, modify, merge, publish, distribute, sublicense, and sell
- Requirement to include copyright notice and license text in redistributions
- No warranty or liability for the licensor

For skills in this repository, the MIT license supports the educational mission by allowing instructors to adapt skills for their specific courses, students to learn from and modify the code, and developers to build derivative works.

Alternative licenses you might encounter:

- **Apache 2.0:** Similar to MIT but with explicit patent grant protection
- **CC-BY-4.0:** Creative Commons Attribution license, appropriate for documentation-heavy skills
- **GPL-3.0:** Copyleft license requiring derivative works to use the same license

When creating your own skills, choose licenses that align with your sharing goals. For educational contexts, permissive licenses (MIT, Apache 2.0, CC-BY) generally maximize positive impact.

### Allowed Tools in Skills

The `allowed-tools` frontmatter field provides fine-grained permission control, limiting skills to specific Claude Code tools. This security and safety mechanism prevents skills from performing unintended operations.

Tool categories and common use cases:

**Read-only tools:**
- `Read`: Access file contents
- `Grep`: Search file contents with regex
- `Glob`: Find files matching patterns
- Appropriate for analysis and reporting skills

**Read-write tools:**
- `Write`: Create new files
- `Edit`: Modify existing files
- Appropriate for content generation skills

**Execution tools:**
- `Bash`: Execute shell commands
- Essential for running scripts, installing dependencies, executing builds

**Research tools:**
- `WebFetch`: Retrieve web page contents
- `WebSearch`: Search the web for information
- Appropriate for skills needing current documentation or examples

Example allowed-tools configurations:

```yaml
# Analysis skill: read-only access
allowed-tools: [Read, Grep, Glob]

# Content generator: read and write, no execution
allowed-tools: [Read, Write, Edit, Grep, Glob]

# Complete workflow: full access
# (allowed-tools omitted or set to all tools)
```

When developing skills, follow the principle of least privilege: grant only the tools necessary for the skill's function. This reduces risk of unintended modifications and makes skill behavior more predictable.

<details markdown="1">
    <summary>Skill Permission Matrix</summary>
    Type: markdown-table

    Purpose: Show which tools different skill types typically require

    | Skill Type | Read | Grep | Glob | Write | Edit | Bash | WebFetch |
    |---|---|---|---|---|---|---|---|
    | Quality Analyzer | ✓ | ✓ | ✓ | ✓ | | | |
    | Content Generator | ✓ | ✓ | ✓ | ✓ | ✓ | | |
    | MicroSim Creator | ✓ | ✓ | ✓ | ✓ | | | ✓ |
    | Workflow Orchestrator | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | |
    | Script Executor | ✓ | | | ✓ | | ✓ | |

    Note: ✓ indicates typically required tool
</details>

### Skill Workflow Instructions

The markdown body of a SKILL.md file contains detailed, step-by-step instructions that Claude Code executes autonomously. Well-designed workflow instructions exhibit several characteristics:

**Explicit sequencing:** Steps numbered clearly (Step 1, Step 2, etc.) with dependencies identified. Each step should be completable before proceeding to the next.

**Conditional logic:** Decision points where workflow branches based on file existence, quality metrics, or user input. Example: "If quality score < 70, prompt user to revise course description."

**Verification checkpoints:** Validation steps confirming expected files exist, contain required sections, and meet quality standards before proceeding.

**Error handling guidance:** Instructions for what to do when expected conditions aren't met. Example: "If learning-graph.csv not found, check for alternate filenames matching pattern learning-graph*.csv."

**Output specifications:** Detailed requirements for generated content including format, structure, naming conventions, and quality criteria.

Example workflow structure from the glossary-generator skill:

```markdown
## Workflow

### Step 1: Verify Learning Graph Exists

Check for learning-graph.csv in /docs/learning-graph/ directory.

Actions:
- Use Glob tool to search for learning-graph*.csv
- If not found, inform user and request path to learning graph
- Read the CSV file to extract ConceptLabel column

### Step 2: Generate Definitions

For each concept label, generate an ISO 11179-compliant definition.

Requirements:
- Precise: Exact meaning without ambiguity
- Concise: Minimal words needed
- Distinct: Differentiated from related concepts
- Non-circular: Doesn't define concept using itself
- Factual: No business rules or implementation details

### Step 3: Create Glossary File

Write glossary.md in /docs/glossary/ directory.

Format:
- Alphabetically sorted terms
- Each term as level 2 heading (##)
- Definition in paragraph below
- Back-to-top links after each entry
```

This structure provides Claude Code with sufficient detail to execute the skill autonomously while maintaining flexibility for handling variations in project structure.

## Installing a Claude Skill

Skills can be installed globally (available across all projects) or locally (available only in a specific project). The installation process creates the `.claude/skills/` directory structure and copies skill files to the appropriate location.

### Global Installation

Global installation makes skills available in all Claude Code sessions regardless of current working directory. Skills are stored in `~/.claude/skills/` in the user's home directory.

Installation process:

1. **Create skills directory structure:**
```bash
mkdir -p ~/.claude/skills/skill-name
```

2. **Copy skill files:**
```bash
cp skill-name/SKILL.md ~/.claude/skills/skill-name/
cp -r skill-name/references ~/.claude/skills/skill-name/  # if present
```

3. **Verify installation:**
```bash
ls -la ~/.claude/skills/
```

For this course's skills, the provided `install-claude-skills.sh` script automates global installation:

```bash
cd scripts
./install-claude-skills.sh
```

This script iterates through all skill directories in `./skills/`, creating symlinks from `~/.claude/skills/` to the source files. Symlinks enable editing skills in the original repository while having them accessible globally—changes immediately propagate without reinstallation.

### Project-Local Installation

Project-local installation confines skills to a specific project, appropriate for specialized workflows unique to that textbook or for testing skills before global deployment.

Installation process:

1. **Create project skills directory:**
```bash
mkdir -p .claude/skills/skill-name
```

2. **Copy skill files to project:**
```bash
cp /path/to/skill-name/SKILL.md .claude/skills/skill-name/
```

3. **Verify in project context:**
```bash
ls -la .claude/skills/
```

Project-local skills take precedence over global skills with the same name, enabling project-specific customization of standard workflows.

<details markdown="1">
    <summary>Skill Installation Locations and Priority</summary>
    Type: diagram

    Purpose: Show where skills can be installed and which location takes precedence

    Components to show:
    - User Home Directory level
      - ~/.claude/skills/ (global skills)
    - Project Directory level
      - /project/.claude/skills/ (project-local skills)
    - Skill Loading Priority indicator (project-local overrides global)
    - Example: If both locations have "quiz-generator", project-local version used

    Layout: Hierarchical tree structure

    Labels:
    - "~/.claude/skills/: Global skills available in all projects"
    - ".claude/skills/: Project-specific skills or overrides"
    - "Priority: Project > Global"

    Visual style: Directory tree diagram with folder icons

    Color scheme: Blue for global location, green for project-local, orange for priority indicator

    Implementation: SVG diagram with tree structure
</details>

## Listing Available Skills

Discovering which skills are installed and available is essential for workflow planning. Multiple methods exist for listing skills, each providing different levels of detail.

### Using the /skills Slash Command

The `/skills` slash command provides the quickest way to list available skills from within a Claude Code session:

```
/skills
```

This command outputs a formatted list of all skills accessible from the current project, including both globally installed and project-local skills. Each entry shows the skill name and description from the SKILL.md frontmatter.

### Using list-skills.sh Script

The `scripts/list-skills.sh` bash script provides more detailed skill listings with various output formats:

**Basic listing:**
```bash
./scripts/list-skills.sh
```

Outputs skill names and descriptions in human-readable format.

**JSON format:**
```bash
./scripts/list-skills-format.sh json
```

Produces JSON array of skill objects with name, description, and file path—useful for programmatic processing or integration with other tools.

**Markdown format:**
```bash
./scripts/list-skills-format.sh markdown
```

Generates markdown-formatted list suitable for documentation or README files.

The listing scripts search both `~/.claude/skills/` and the current project's `.claude/skills/` directories, indicating which skills are globally versus locally installed.

### Programmatic Skill Discovery

For integration with custom workflows or tooling, skills can be discovered programmatically by searching for `SKILL.md` files and parsing their YAML frontmatter:

```bash
find ~/.claude/skills -name "SKILL.md" -type f
```

This approach enables building custom skill managers, automated testing frameworks, or skill catalog generation for documentation sites.

## Invoking Skills with Slash Commands

Skills are invoked using slash commands with the syntax `/skill skill-name` or through the Skill tool in direct tool use.

### Basic Invocation

To execute a skill, type the slash command followed by the skill name (without file extension):

```
/skill learning-graph-generator
```

Claude Code loads the corresponding SKILL.md file, processes the frontmatter to configure permissions, and begins executing the workflow instructions sequentially.

### Skill Execution Process

When a skill is invoked:

1. **Skill loading:** Claude Code locates SKILL.md in `.claude/skills/` or `~/.claude/skills/`
2. **Permission configuration:** `allowed-tools` frontmatter restricts available tools
3. **Context inheritance:** Skill receives full conversation history up to invocation point
4. **Workflow execution:** Claude Code processes markdown instructions as autonomous directives
5. **Output generation:** Skill produces specified files, reports, or artifacts
6. **Completion report:** Skill returns summary of actions taken and results achieved

Skills execute autonomously—once invoked, they make decisions about which files to read, what content to generate, and how to handle edge cases based on their workflow instructions. Users receive progress updates and final reports but don't need to make decisions at each step.

### Passing Context to Skills

Skills have access to the conversation history before their invocation, enabling contextual understanding. Users can provide additional context by preceding the skill invocation with instructions:

```
Generate chapter content for junior-high reading level with emphasis on concrete examples

/skill chapter-content-generator
```

The skill receives both the general instruction and executes its standard workflow, incorporating the contextual guidance where applicable.

<details markdown="1">
    <summary>Skill Invocation and Execution Lifecycle</summary>
    Type: workflow

    Purpose: Illustrate what happens when a skill is invoked from command to completion

    Visual style: Flowchart with swimlanes

    Swimlanes:
    - User
    - Claude Code System
    - Skill Executor
    - File System

    Steps:
    1. Start (User): "User types /skill skill-name"
       Hover text: "Example: /skill glossary-generator"

    2. Process (Claude Code): "Locate SKILL.md file"
       Hover text: "Search .claude/skills/ then ~/.claude/skills/ for matching skill"

    3. Decision (Claude Code): "Skill found?"
       Hover text: "Check if SKILL.md exists in either location"

    4a. End (User): "Error: Skill not found"
        Hover text: "Suggest running /skills to see available skills"

    4b. Process (Claude Code): "Parse YAML frontmatter"
        Hover text: "Extract name, description, allowed-tools"

    5. Process (Claude Code): "Configure tool permissions"
       Hover text: "Restrict to allowed-tools if specified"

    6. Process (Skill Executor): "Load workflow instructions"
       Hover text: "Read markdown body from SKILL.md"

    7. Process (Skill Executor): "Execute Step 1"
       Hover text: "Follow workflow instructions autonomously"

    8. Process (File System): "Read/write files as directed"
       Hover text: "Access course description, learning graphs, generate content"

    9. Decision (Skill Executor): "More steps?"
       Hover text: "Check if workflow complete"

    10. Loop: Execute next step (back to step 7)
        Hover text: "Continue through all workflow steps"

    11. Process (Skill Executor): "Generate completion report"
        Hover text: "Summarize actions taken, files created, quality metrics"

    12. End (User): "Display results and next steps"
        Hover text: "User sees summary and can proceed with next task"

    Color coding:
    - Blue: User interactions
    - Purple: System processing
    - Green: Skill execution
    - Orange: File operations

    Implementation: SVG flowchart with decision diamonds and process rectangles
</details>

### Skill Execution Context

Skills execute within a context that includes:

**Conversation history:** All messages and tool calls prior to skill invocation, enabling skills to understand project state and user objectives.

**Working directory:** The current directory where Claude Code was launched, typically the project root.

**File system access:** Ability to read and write files within project directory tree (subject to tool permissions).

**Isolated state:** Each skill invocation starts fresh—skills don't maintain state across invocations unless they write to files.

Understanding this context model helps in designing effective skills. For instance, the learning-graph-generator skill reads the course description file to understand course scope, generates concepts based on that description, and writes results to files that subsequent skills (like glossary-generator) will read.

## Understanding Claude Commands

Claude Commands provide a simpler alternative to skills for single-purpose prompt expansions. While skills execute multi-step workflows autonomously, commands simply expand to a predefined prompt, effectively providing reusable prompt templates.

Commands are defined in markdown files in the `.claude/commands/` directory. Unlike skills, commands don't have YAML frontmatter—they consist purely of the prompt text to be executed.

### Command Definition Files

A command file contains only the prompt that should be executed when the command is invoked. For example, `review-code.md` might contain:

```markdown
Review the code in this project for:
- Security vulnerabilities
- Performance issues
- Code style consistency
- Best practice violations

Provide a prioritized list of issues with specific file locations and suggested fixes.
```

When a user types `/review-code`, Claude Code replaces the command with this prompt and executes it in the current context.

### Installing Claude Commands

Commands are installed similarly to skills but in the `.claude/commands/` directory:

**Global installation:**
```bash
mkdir -p ~/.claude/commands/
cp command-name.md ~/.claude/commands/
```

**Project-local installation:**
```bash
mkdir -p .claude/commands/
cp command-name.md .claude/commands/
```

Like skills, project-local commands take precedence over global commands with the same name.

### Difference Between Skills & Commands

The fundamental distinction between skills and commands lies in autonomy and complexity:

| Aspect | Skills | Commands |
|--------|--------|----------|
| Definition | Multi-step autonomous workflows | Single prompt templates |
| File structure | SKILL.md with YAML frontmatter | Plain markdown file |
| Execution | Autonomous with decision-making | Simple prompt expansion |
| Tool control | allowed-tools permissions | Uses all available tools |
| Complexity | Multi-file operations, quality checks | Single request-response |
| State | Can read/write files, maintain project state | Stateless prompt execution |
| Examples | learning-graph-generator, quiz-generator | review-code, explain-concept |

**When to use skills:**
- Multi-step workflows requiring sequential operations
- Tasks needing file reading, analysis, and generation
- Processes with quality validation checkpoints
- Operations requiring consistency across projects

**When to use commands:**
- Simple prompt templates used frequently
- Single-request operations
- Project-specific prompt patterns
- Quick shortcuts for common questions

In this course, the intelligent textbook workflow relies primarily on skills due to the complexity and multi-step nature of content generation. Commands might be used for auxiliary tasks like "check-concept-coverage" or "validate-markdown-format."

<details markdown="1">
    <summary>Skills vs Commands Decision Tree</summary>
    Type: workflow

    Purpose: Help users decide whether to create a skill or command for their use case

    Visual style: Decision tree with yes/no branches

    Decision points:
    1. Start: "Do you need to perform multiple sequential steps?"
       Yes → Continue to 2
       No → "Consider using a Command"

    2. "Do you need to read from and write to multiple files?"
       Yes → Continue to 3
       No → "Consider using a Command"

    3. "Do you need quality validation or error handling?"
       Yes → Continue to 4
       No → "Simple Skill might work"

    4. "Will this workflow be reused across multiple projects?"
       Yes → "Create a Skill with full workflow"
       No → "Project-local Skill or Command"

    Terminal nodes:
    - "Create a Skill": For complex, reusable workflows
    - "Use a Command": For simple prompt templates
    - "Simple Skill might work": For straightforward multi-step tasks
    - "Project-local Skill or Command": For project-specific automation

    Color coding:
    - Green: Indicates skill is appropriate
    - Yellow: Indicates command might suffice
    - Orange: Indicates borderline case

    Implementation: SVG decision tree with diamond decision nodes
</details>

## Token Management Strategies

Effective use of Claude requires understanding and managing token consumption. Claude Pro accounts provide generous but finite token budgets within 4-hour usage windows, making token management essential for sustained productivity on textbook projects.

### Understanding Tokens

Tokens represent the fundamental units of text processing in large language models. A token typically corresponds to:

- One word (e.g., "textbook" = 1 token)
- Part of a long word (e.g., "educational" might be 2-3 tokens)
- Punctuation marks (e.g., "." = 1 token)
- Whitespace (spaces generally included with adjacent words)

On average, English text contains approximately 1 token per 4 characters or 1 token per 0.75 words. Technical content with specialized terminology may consume more tokens due to uncommon word fragments.

Both input (prompts, file contents, conversation history) and output (generated text) count toward token consumption. For intelligent textbook workflows, large inputs (entire learning graphs, multiple chapter files) combined with extensive outputs (comprehensive chapter content) can accumulate tokens quickly.

### Claude Token Limits

Claude Code uses the Sonnet or Opus models depending on task complexity. As of 2025, typical token windows are:

- **Context window:** 200,000 tokens (amount of text Claude can consider simultaneously)
- **Output limit:** ~4,000-8,000 tokens per response (model-dependent)

These generous limits enable Claude to process entire textbook chapters, comprehensive learning graphs, and extensive reference materials in a single context. However, the cumulative token consumption across an entire session must be managed within Claude Pro usage limits.

### 4-Hour Usage Windows

Claude Pro accounts operate on a rolling 4-hour usage window model. Rather than a daily reset, your available capacity regenerates continuously based on when tokens were consumed.

How it works:

1. You have a token budget (specific amount varies by subscription tier)
2. Each request consumes tokens from this budget
3. After 4 hours, those tokens return to your available pool
4. Usage resets continuously, not at a fixed daily time

Example: If you consume 50,000 tokens at 9:00 AM, those tokens remain unavailable until 1:00 PM (4 hours later), when they're restored to your budget.

This model rewards distributed work patterns over concentrated bursts. For textbook creation workflows that may involve generating content for 13 chapters, spreading skill invocations across several sessions prevents exhausting your token budget.

<details markdown="1">
    <summary>4-Hour Token Window Visualization</summary>
    Type: timeline

    Purpose: Show how token usage and regeneration works over time

    Time period: 12-hour window

    Orientation: Horizontal timeline with token budget shown as vertical bar chart below

    Events:
    - 9:00 AM: Generate Chapter 1 content (consume 30,000 tokens)
    - 9:30 AM: Generate glossary (consume 15,000 tokens)
    - 11:00 AM: Generate Chapter 2 content (consume 30,000 tokens)
    - 1:00 PM: 9:00 AM tokens restored (+30,000 tokens)
    - 1:30 PM: 9:30 AM tokens restored (+15,000 tokens)
    - 3:00 PM: 11:00 AM tokens restored (+30,000 tokens)
    - 5:00 PM: Available budget fully replenished

    Visual elements:
    - Timeline showing activity times
    - Stacked bar chart below showing available vs consumed tokens at each time point
    - Rolling 4-hour window indicator
    - Annotations showing "Tokens consumed" and "Tokens restored"

    Color coding:
    - Blue: Available token budget
    - Orange: Consumed tokens
    - Green: Restored tokens
    - Gray: 4-hour restoration window

    Interactive features:
    - Hover over timeline events to see token amounts
    - Hover over bars to see total available vs used

    Implementation: HTML/CSS/JavaScript with Chart.js timeline
</details>

### Optimizing Claude Usage

Several strategies maximize productivity within token budgets:

**Strategy 1: Batch related operations**

Rather than generating one chapter at a time with full context reloading, batch similar operations together. Generate all quiz questions in one session, all MicroSim specifications in another.

**Strategy 2: Use focused contexts**

When invoking skills, provide only necessary context. Don't include the entire learning graph if the skill only needs concept labels. Use skill-specific context loading rather than maintaining everything in conversation history.

**Strategy 3: Leverage file-based state**

Skills that write intermediate results to files enable breaking workflows into smaller sessions. Generate chapter outlines in one session, detailed content in another—the outline file provides continuity without maintaining conversation history.

**Strategy 4: Progressive refinement over regeneration**

When chapter content needs adjustment, use targeted edits rather than regenerating entire chapters. Edit specific sections or add missing concepts rather than rewriting from scratch.

**Strategy 5: Monitor usage patterns**

Track which skills consume the most tokens (typically learning-graph-generator and chapter-content-generator for large textbooks). Plan sessions to stay within 4-hour windows for these heavy operations.

**Strategy 6: Use appropriate model variants**

For simpler tasks like validating markdown formatting or checking concept coverage, request that Claude use more efficient models. Reserve Opus for complex reasoning and content generation.

## Iterative Prompt Refinement

Effective prompt engineering for skills and educational content generation follows an iterative refinement cycle: draft, test, evaluate, refine, repeat. This section explores techniques for systematically improving prompts to achieve desired educational outcomes.

### Initial Prompt Drafting

The first iteration focuses on establishing basic structure and requirements:

1. **Define learning objectives:** What should learners understand or be able to do?
2. **Specify output format:** Markdown sections, details blocks, specific structures
3. **Identify constraints:** Reading level, word count, concept coverage
4. **Provide examples:** Reference materials demonstrating desired quality

For a chapter content generation prompt, an initial draft might specify:
- Target reading level (graduate)
- Concepts to cover (list from chapter outline)
- Required sections (introduction, concept explanations, summary)
- Interactive element frequency (every 3-5 paragraphs)

### Testing and Evaluation

Execute the prompt and evaluate outputs against quality criteria:

**Content coverage:** Are all required concepts addressed with adequate depth?

**Reading level appropriateness:** Does sentence complexity, vocabulary, and explanation style match target level?

**Structural compliance:** Does output follow specified markdown format with correct heading hierarchy?

**Interactive element integration:** Are details blocks properly formatted with sufficient specification detail?

**Pedagogical soundness:** Do explanations build logically? Are examples appropriate?

Document specific deficiencies: "Missing coverage of concepts 14-16," "Reading level too advanced for target audience," "Interactive elements lack implementation specifications."

### Refinement Strategies

Based on evaluation results, refine prompts using these techniques:

**Add explicit constraints:** If output too verbose, add word count ranges. If examples too abstract, specify "concrete examples from daily professional experience."

**Provide negative examples:** Show what NOT to do alongside positive examples. "Avoid jargon like this [bad example]; instead use accessible language like this [good example]."

**Increase specificity:** Replace "add interactive elements" with "include 2 diagrams, 1 MicroSim, and 1 interactive infographic specified in details blocks."

**Incorporate rubrics:** Provide scoring criteria that Claude should self-evaluate against before finalizing output.

**Sequential generation:** Break complex generation into phases—outline first, then detailed content, then interactive elements—with validation checkpoints between phases.

### Convergence to Quality

Over 3-5 iterations, prompts typically converge to consistent, high-quality outputs. Indicators of convergence:

- Multiple consecutive executions produce similarly high-quality results
- Quality scores consistently exceed threshold (e.g., >85/100)
- Manual review finds few deficiencies requiring correction
- Generated content requires minimal post-processing

Converged prompts can be captured as skills or commands for reuse across projects, sharing expertise and accelerating future textbook development.

<details markdown="1">
    <summary>Iterative Prompt Refinement Metrics</summary>
    Type: chart

    Chart type: Line chart with annotations

    Purpose: Show how prompt quality improves across refinement iterations

    X-axis: Iteration number (1-5)
    Y-axis: Quality score (0-100)

    Data series:
    - Quality Score: [45, 62, 78, 88, 91]
    - Quality Threshold (horizontal line at 85)

    Title: "Prompt Quality Improvement Across Iterations"

    Data points:
    - Iteration 1 (45): "Initial draft - missing concepts, wrong reading level"
    - Iteration 2 (62): "Added concept coverage constraints - improved but verbose"
    - Iteration 3 (78): "Refined reading level parameters - closer to target"
    - Iteration 4 (88): "Added interactive element specifications - exceeds threshold"
    - Iteration 5 (91): "Minor refinements - consistent quality achieved"

    Visual elements:
    - Line showing quality progression
    - Threshold line at 85
    - Annotations for each data point explaining changes
    - Shaded region above 85 indicating "Acceptable Quality Zone"

    Color scheme: Blue line for quality score, green shaded region for acceptable zone, red dashed line for threshold

    Implementation: Chart.js line chart with annotations plugin
</details>

## Summary

This chapter introduced the Claude Skills system as the foundation for automating intelligent textbook creation workflows. You learned the anatomy of skill definition files, including YAML frontmatter for metadata and markdown workflow instructions for autonomous execution. We explored how skills differ from simpler command-based prompt expansions and when each approach is appropriate.

You learned practical techniques for installing skills globally or project-locally, listing available skills through slash commands and scripts, and invoking skills within Claude Code sessions. We examined the skill execution lifecycle and how skills access context, make autonomous decisions, and produce structured outputs.

Finally, we addressed token management strategies essential for sustained productivity within Claude Pro's 4-hour usage windows and explored iterative prompt refinement techniques for systematically improving educational content generation quality. These capabilities form the foundation for the educational framework and learning graph concepts introduced in subsequent chapters.

**Concepts covered:** Claude Skill ✓, Skill Definition File Structure ✓, YAML Frontmatter in Skills ✓, Skill Name and Description ✓, Skill License Information ✓, Allowed Tools in Skills ✓, Skill Workflow Instructions ✓, Installing a Claude Skill ✓, Listing Available Skills ✓, Invoking Skills with Slash Commands ✓, Skill Execution Context ✓, Claude Command ✓, Command Definition Files ✓, Installing Claude Commands ✓, Difference Between Skills & Commands ✓, Iterative Prompt Refinement ✓, Claude Token Limits ✓, Token Management Strategies ✓

## References

1. [Prompt Engineering in 2025: The Latest Best Practices](https://www.news.aakashg.com/p/prompt-engineering) - 2025 - Aakash Gupta - Comprehensive guide covering modern prompt engineering techniques including specificity, context provision, iterative refinement, and breaking down complex tasks, directly applicable to creating effective Claude Skills for educational content generation.

2. [10 Best Practices for Production-Grade LLM Prompt Engineering](https://latitude-blog.ghost.io/blog/10-best-practices-for-production-grade-llm-prompt-engineering/) - 2024 - Latitude - Professional guide to treating prompts like software artifacts with version control and systematic testing, essential for maintaining high-quality skill definitions in intelligent textbook workflows.
