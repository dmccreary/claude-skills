---
title: Agent Skill Fundamentals
description: Defines what an Agent Skill is, unpacks the SKILL.md frontmatter contract field by field, and covers the skill directory structure and progressive disclosure.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 13:20:00
version: 0.09
---

# Agent Skill Fundamentals

## Summary

This chapter defines what an Agent Skill is and how it differs from a prompt, then unpacks the SKILL.md frontmatter contract field by field -- name, description, license, compatibility, and allowed tools. It also covers the skill directory structure, including the references, scripts, and assets folders. Students will be able to read a SKILL.md file and identify each required and optional field after this chapter.

## Concepts Covered

This chapter covers the following 23 concepts from the learning graph:

1. Agent Skill
2. Agent Skills Open Standard
3. SKILL.md File
4. Skill Execution Context
5. Skills Versus Prompts
6. YAML Frontmatter
7. Skill Directory Structure
8. Skill Versioning
9. Skill Workflow Instructions
10. Skill Name Field
11. Skill Description Field
12. Skill License Field
13. Compatibility Field
14. Skill Metadata Field
15. Allowed Tools Field
16. Vendor Extension Fields
17. References Directory
18. Scripts Directory
19. Assets Directory
20. Model Selection Per Skill
21. Skill Composition
22. Frontmatter Contract
23. Progressive Disclosure

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [4. Development Tools: Editor, Terminal, and Git Basics](../04-dev-tools-editor-git-basics/index.md)

---

!!! mascot-welcome "Now we get to the good part."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Everything so far has been setup. This chapter is where you finally open up the tool itself — the Agent Skill — and see exactly what's inside. Right tool, right task!

## What Is an Agent Skill?

An **Agent Skill** is a packaged set of instructions and supporting files that teaches an AI agent to perform a specific task consistently — not a one-off request, but a reusable capability you can invoke by name every time you need it. That's the heart of **skills versus prompts**: the distinction between a reusable packaged capability with supporting files and a single request typed into a session. A prompt disappears once you close the conversation; a skill lives in your project (or your global configuration) and works the same way every time it's triggered.

Because skills are meant to be shared across projects and even across different AI tools, they follow the **Agent Skills open standard**: the published specification defining what a skill folder must contain and which metadata fields conforming clients recognize. That shared standard is exactly what lets this book's library run on Claude Code, OpenAI Codex, and other agent platforms without a rewrite for each one.

## The SKILL.md File and Its Frontmatter

Every skill folder has one required file at its root: the **SKILL.md file**, containing metadata at the top and workflow instructions below. The metadata block at the top is written as **YAML frontmatter**: a block of key-value metadata at the start of a file, delimited by triple dashes, that carries structured information separate from the body.

```yaml
---
name: learning-graph-generator
description: Generates a 300-600 concept learning graph from a course description.
---
```

Before that example, notice the shape: everything between the two `---` lines is frontmatter, read by the agent before it ever looks at the instructions below. Not every field an agent platform might invent is safe to rely on everywhere, though — that's the **frontmatter contract**: the agreement that only a small set of metadata fields is portable across agent platforms, making those fields the safe surface for a shared library.

## The Required and Optional Frontmatter Fields

Two frontmatter fields are required by the open standard. The **skill name field** is the required identifier for a skill, restricted to lowercase letters, digits, and hyphens, and matching the folder that contains it. The **skill description field** is the required summary stating what a skill does and when it should be used — it's the text an agent actually matches your request against, so a vague description means a skill that never triggers when you need it.

Everything else is optional. The **skill license field** names the terms under which a skill may be used or redistributed. The **compatibility field** describes environment requirements such as needed packages or network access — advisory rather than enforced, so an agent won't stop you from running a skill even if your environment doesn't meet it. The **skill metadata field** is an optional map of string keys and values carrying client-specific or organization-specific information that the agent itself ignores. The **allowed tools field** is an optional list of pre-approved actions a skill may take without further prompting, though its exact behavior varies between agent platforms.

!!! mascot-warning "Not every field travels well."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    **Vendor extension fields** are metadata keys outside the published specification, added by a particular platform — some clients ignore them silently, and some reject the whole file outright. If you want a skill to run on more than one agent platform, keep to the frontmatter contract's safe fields and treat anything vendor-specific as an enhancement, never a requirement.

| Field | Required? | Purpose |
|-------|-----------|---------|
| `name` | Required | Identifier matching the skill's folder |
| `description` | Required | What triggers the skill and when |
| `license` | Optional | Reuse and redistribution terms |
| `compatibility` | Optional | Advisory environment requirements |
| `metadata` | Optional | Client-specific key-value data |
| `allowed-tools` | Optional | Pre-approved actions (platform-dependent) |

## Skill Directory Structure

A skill is more than its SKILL.md file. The **skill directory structure** is the folder layout of a skill: the required instruction file plus optional folders for reference documents, executable scripts, and templates. The **references directory** holds detailed guides that are read only when a particular task requires them, keeping them out of the default load. The **scripts directory** holds executable programs a skill runs to perform deterministic work — exactly the kind of Python scripts you met in Chapter 3. The **assets directory** holds templates, schemas, and images that a skill copies or reads when producing output.

#### Diagram: Skill Directory Structure

<iframe src="../../sims/skill-directory-structure/main.html" width="100%" height="460px" scrolling="no"></iframe>

<details markdown="1">
<summary>Skill Directory Structure (reused MicroSim)</summary>
Type: workflow
**sim-id:** skill-directory-structure<br/>
**Library:** Mermaid<br/>
**Status:** Reused<br/>
**Source:** docs/sims/skill-directory-structure

Reused from this book's own MicroSim catalog. Learning objective: Identify the role of a skill's SKILL.md file, references directory, scripts directory, and assets directory.
</details>

## Progressive Disclosure: Loading Only What's Needed

A large skill library can't afford to load every file from every skill into an agent's context window at once — that would burn through the budget you learned about in Chapter 1 before you even asked a question. **Progressive disclosure** is the loading strategy in which an agent sees only a skill's summary by default, reads its full instructions when triggered, and opens detailed reference guides only when a specific task actually needs them.

!!! mascot-thinking "Three layers, loaded only as needed."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Picture it as three nested layers: the frontmatter (tiny, always loaded so the agent can decide whether to trigger the skill), the SKILL.md body (loaded once triggered), and the references/assets folders (loaded only if that specific task needs them). A 99-guide meta-skill can sit in your library costing almost nothing until the one guide you actually need gets pulled in.

#### Diagram: Skill Context Window

<iframe src="../../sims/skill-context-window/main.html" width="100%" height="525px" scrolling="no"></iframe>

<details markdown="1">
<summary>Skill Context Window (reused MicroSim)</summary>
Type: microsim
**sim-id:** skill-context-window<br/>
**Library:** p5.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/skill-context-window

Reused from this book's own MicroSim catalog. Learning objective: Analyze how the frontmatter, SKILL.md file, and assets/resources layers load at different times under progressive disclosure.
</details>

## Workflow Instructions, Versioning, and Execution Context

Below the frontmatter, **skill workflow instructions** are the step-by-step body of a skill file that an agent follows once the skill is triggered — this is the actual recipe, written in plain language the model can execute. As a skill's instructions change over time, **skill versioning** records a revision number inside the skill so behavior changes can be tracked and a defect traced back to the specific revision that introduced it.

None of this runs in a vacuum. **Skill execution context** is the environment in which a skill runs, including the working directory, available tools, and granted permissions — the same skill can behave differently depending on what it's allowed to touch in a given session.

## Model Selection and Skill Composition

Not every skill needs the same amount of reasoning power. **Model selection per skill** is declaring which model tier a skill should run on, so demanding work gets a stronger model and routine, well-specified work gets a cheaper one — a real cost lever you'll revisit in the token-optimization chapters ahead. Skills also don't have to work alone: **skill composition** is combining several skills in sequence so the output of one becomes the input of the next, exactly how this book's own pipeline chains `course-description-analyzer` into `learning-graph-generator` into `book-chapter-generator`.

!!! mascot-tip "Compose skills instead of building one giant one."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    If a skill's instructions are getting long and unfocused, that's usually a sign it's really two skills. Split it, and let one skill's output feed the next — smaller, single-purpose skills are easier to trigger correctly and easier to test.

## Key Takeaways

- An **Agent Skill** is a reusable packaged capability, distinct from a one-off **prompt**, following the **Agent Skills open standard**.
- The **SKILL.md file** starts with **YAML frontmatter** governed by the **frontmatter contract**; only `name` and `description` are required.
- Optional fields — **license**, **compatibility**, **metadata**, **allowed-tools**, and platform-specific **vendor extension fields** — add capability but shouldn't be relied on everywhere.
- The **skill directory structure** organizes a **references**, **scripts**, and **assets** directory around the SKILL.md file, loaded through **progressive disclosure**.
- **Workflow instructions**, **versioning**, and **execution context** shape how a skill actually runs; **model selection** and **skill composition** shape how efficiently and how far it reaches.

!!! mascot-celebration "You can read any skill in this library now."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Open any `SKILL.md` file in this project and you'll recognize every part — the frontmatter, the fields, the folder structure underneath. That's the whole shape of the tool. Right tool, right task!
