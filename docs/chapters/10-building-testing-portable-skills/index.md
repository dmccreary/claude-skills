---
title: Building and Testing Portable Skills
description: Covers writing a trigger-reliable skill description, testing and benchmarking a skill, permissions and security, packaging, and portability across AI agent platforms.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 14:20:00
version: 0.09
---

# Building and Testing Portable Skills

## Summary

This chapter covers permission management and script execution permissions inside a skill, then writing a trigger-reliable skill description and testing it. It explains how the Agent Skills open standard and the AGENTS.md convention keep one skill library working across Claude Code, OpenAI Codex, Google Antigravity, Cursor, and GitHub Copilot. Students will be able to test whether a skill triggers reliably and degrades gracefully on a platform lacking a capability.

## Concepts Covered

This chapter covers the following 21 concepts from the learning graph:

1. Skill Portability
2. Skill Creator Skill
3. AGENTS.md Convention
4. OpenAI Codex
5. Google Antigravity
6. Cursor IDE
7. GitHub Copilot
8. Permission Management
9. Script Execution Permissions
10. File Access Permissions
11. analyze-skills.py Script
12. Writing a Skill Description
13. Security in Skill Execution
14. Description Trigger Testing
15. Skill Evaluation Harness
16. Skill Benchmarking
17. Skill Testing and Debugging
18. Skill Packaging
19. Skill Variance Analysis
20. Skill Failure Modes
21. Skill Distribution Methods

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [2. AI Coding Agents and the Five Levels of Textbook Intelligence](../02-ai-agents-textbook-intelligence/index.md)
- [4. Development Tools: Editor, Terminal, and Git Basics](../04-dev-tools-editor-git-basics/index.md)
- [6. Agent Skill Fundamentals](../06-agent-skill-fundamentals/index.md)
- [7. Progressive Disclosure and Meta-Skill Routing](../07-progressive-disclosure-meta-skills/index.md)
- [9. Measuring and Optimizing Token Usage](../09-measuring-optimizing-tokens/index.md)

---

!!! mascot-welcome "Let's make sure your skill actually works."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A skill you can't test is a skill you can't trust. This chapter is how you build one that triggers reliably, stays safe, and runs the same way on someone else's machine — or someone else's AI tool entirely. Right tool, right task!

## Writing a Description That Triggers Reliably

**Writing a skill description** means composing the summary that determines when a skill activates, stating both what it does and the situations that should invoke it — get this wrong and the whole skill is invisible or, worse, a false-trigger risk from Chapter 7. You confirm it worked with **description trigger testing**: checking a skill description against sample requests to confirm it activates when it should and stays silent when it should not.

## Testing, Benchmarking, and Debugging a Skill

The **Skill Creator Skill** is a skill used to author, revise, and evaluate other skills, including testing how reliably their descriptions trigger — it's the meta-tool this chapter is really about. Underneath it sits a **skill evaluation harness**: a repeatable test setup that runs a skill against known inputs and scores the output, making quality changes measurable rather than anecdotal. Running that harness across a fixed set of cases is **skill benchmarking**: measuring a skill's output quality, runtime, and token consumption against a fixed set of cases so revisions can be compared apples to apples.

!!! mascot-tip "Run it three times before you trust the number."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Because model output is nondeterministic (Chapter 1), one benchmark run can mislead you. **Skill variance analysis** — running the same case repeatedly to measure how much a skill's output changes between runs — is what tells real improvement apart from random fluctuation.

More broadly, **skill testing and debugging** means exercising a skill against representative requests and diagnosing the cause when its behavior differs from what its instructions specify. That diagnosis is easier when you know the shape of what usually goes wrong: **skill failure modes** are the recurring ways a skill breaks — failing to trigger, triggering wrongly, loading the wrong guide, or producing output that fails validation.

## Permissions and Security

A skill that can act needs boundaries on what it's allowed to act on. **Permission management** is controlling which actions an agent may take without asking, balancing convenience against the risk of unintended changes. Two specific slices of that are **script execution permissions** — the settings that determine whether an agent may run a program directly or must request approval first — and **file access permissions**: the rules governing which files an agent may read or modify during a session.

!!! mascot-warning "A skill that can run anything, will eventually run the wrong thing."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    **Security in skill execution** covers the practices that keep a skill from taking damaging or unauthorized actions, including restricting tools and reviewing what a script does before running it. Never grant broader permissions than a skill's actual job requires — a chapter-content skill doesn't need permission to delete files.

#### Diagram: Security Zones for Skill Execution

<iframe src="../../sims/security-zones-diagram/main.html" width="100%" height="480px" scrolling="no"></iframe>

<details markdown="1">
<summary>Security Zones for Skill Execution (reused MicroSim)</summary>
Type: workflow
**sim-id:** security-zones-diagram<br/>
**Library:** Mermaid<br/>
**Status:** Reused<br/>
**Source:** docs/sims/security-zones-diagram

Reused from this book's own MicroSim catalog. Learning objective: Differentiate the no-access, read-only, and full-access zones a skill execution session typically operates within.
</details>

## Packaging and Distribution

Once a skill works and is safely scoped, **skill packaging** means assembling its instruction file, scripts, references, and assets into a self-contained folder that can be copied or shared. From there, **skill distribution methods** are the ways a skill actually reaches other users: a shared repository, a copied folder, or a plugin registry.

## Measuring Usage: analyze-skills.py

To know whether a skill is actually worth its cost, this project ties testing back to the measurement tools from Chapter 9. The **analyze-skills.py script** is the program that processes recorded usage events and reports duration and consumption per skill — the same JSONL log data feeding directly into a concrete, per-skill number instead of a vague impression.

## Running Skills Everywhere: Portability and AGENTS.md

**Skill portability** is the degree to which a skill written for one agent platform runs correctly on others without modification — the entire reason Chapter 6's frontmatter contract restricted itself to a safe, portable field set. One convention makes cross-platform instructions work without duplication: the **AGENTS.md convention**, the practice of placing project instructions in a commonly recognized filename so multiple agent platforms read the same guidance.

!!! mascot-thinking "Portable means tested, not just written carefully."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A skill that only ever ran in Claude Code might *look* portable and still fail the first time it meets a platform with a different tool-calling convention. Portability is a claim you verify by actually running the skill somewhere else, not a property you get for free from following the standard.

| Platform | What It Is |
|----------|------------|
| Claude Code | This project's primary development environment |
| **OpenAI Codex** | An AI coding agent from OpenAI running the portable subset of the standard |
| **Google Antigravity** | A Google AI development environment executing agent skills in a supported project |
| **Cursor IDE** | An editor with a built-in AI agent that loads and runs skills alongside normal editing |
| **GitHub Copilot** | An AI assistant integrated with editors and GitHub that consumes portable skill definitions |

## Key Takeaways

- **Writing a skill description** well and confirming it with **description trigger testing** is the foundation of a discoverable skill.
- The **Skill Creator Skill**, backed by a **skill evaluation harness**, **benchmarking**, and **variance analysis**, turns skill quality into something measurable.
- **Permission management**, **script execution permissions**, **file access permissions**, and **security in skill execution** keep a skill's reach appropriately narrow.
- **Skill packaging** and **distribution methods** get a finished skill to other users; **analyze-skills.py** tells you what it actually costs once it's in use.
- **Skill portability**, backed by the **AGENTS.md convention**, is what lets one library run across **Codex**, **Antigravity**, **Cursor**, and **Copilot** — but only if you actually test it there.

!!! mascot-celebration "You can now ship a skill you'd trust."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Tested, permission-scoped, packaged, and portable — that's a skill ready for someone else's project, not just your own. Right tool, right task!
