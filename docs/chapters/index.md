# Chapters

This textbook is organized into 31 chapters covering all 570 concepts in the
[learning graph](../learning-graph/index.md), plus four practical appendices.

## Chapter Overview

1. [Foundations of AI, Language Models, and Prompting](01-foundations-ai-language-models/index.md) — Introduces artificial intelligence, large language models, tokens, and context windows, then covers prompting and prompt engineering as the interface between a person and a model.
2. [AI Coding Agents and the Five Levels of Textbook Intelligence](02-ai-agents-textbook-intelligence/index.md) — Covers AI coding agents, agentic workflows, tool use, and the human-in-the-loop pattern that keeps a person in control of an agent's actions.
3. [Python Fundamentals for Skill Automation](03-python-fundamentals-automation/index.md) — Introduces the Python building blocks used across the skill library: the standard library, pip and virtual environments, JSON and CSV parsing, regular expressions, and command-line arguments.
4. [Development Tools: Editor, Terminal, and Git Basics](04-dev-tools-editor-git-basics/index.md) — Sets up the core development environment: Visual Studio Code and its integrated terminal, Git repository structure, and the first commands used to track changes.
5. [MkDocs Site Features, Deployment, and Analytics](05-mkdocs-deployment-analytics/index.md) — Expands the MkDocs Material feature set and walks through the Git commit, push, and branch workflow to a deployed site.
6. [Agent Skill Fundamentals](06-agent-skill-fundamentals/index.md) — Defines what an Agent Skill is and how it differs from a prompt, then unpacks the SKILL.md frontmatter contract field by field.
7. [Progressive Disclosure and Meta-Skill Routing](07-progressive-disclosure-meta-skills/index.md) — Explains progressive disclosure and its three loading budgets, along with how trigger matching and meta-skills keep a library under the loading limit.
8. [Token Budgets and Usage Limits](08-token-budgets-usage-limits/index.md) — Treats tokens as an engineering budget: the token cost model, plan limits and usage windows, and serial versus parallel execution.
9. [Measuring and Optimizing Token Usage](09-measuring-optimizing-tokens/index.md) — Covers file-layout token strategies, usage-tracking hooks, JSONL logs, and dashboards for token consumption.
10. [Building and Testing Portable Skills](10-building-testing-portable-skills/index.md) — Covers permission management, writing a trigger-reliable skill description, and testing skill portability across AI platforms.
11. [Distributing Skills and Building Commands](11-distributing-skills-commands/index.md) — Covers packaging and installing skills, plus creating Claude commands and ordered runbooks.
12. [Writing a Course Description](12-writing-course-description/index.md) — Walks through every required element of a course description and introduces Bloom's Taxonomy as the outcomes framework.
13. [Bloom's Taxonomy and Instructional Design](13-blooms-taxonomy-instructional-design/index.md) — Details all six Bloom's cognitive levels and the instructional-design conventions used to write chapter content.
14. [Learning Graphs and Concept Enumeration](14-learning-graphs-concept-enumeration/index.md) — Defines what a learning graph is and covers concept enumeration and dependency mapping.
15. [Learning Graph Data Formats and Taxonomy](15-learning-graph-formats-taxonomy/index.md) — Covers the CSV and vis-network JSON formats that encode a learning graph, and taxonomy categorization.
16. [Learning Graph Quality Validation](16-learning-graph-quality-validation/index.md) — Covers the quality checks a learning graph must pass and the interactive graph viewer.
17. [Chapter Structure and Content Elements](17-chapter-structure-content-elements/index.md) — Introduces the book-chapter-generator workflow and the markdown content elements available inside a chapter.
18. [Chapter Content Quality and Review](18-chapter-content-quality-review/index.md) — Covers section organization, diagram specification blocks, and the chapter review workflow.
19. [FAQs and Curated References](19-faqs-curated-references/index.md) — Covers generating a FAQ set and building a curated reference list that credits pedagogical authors.
20. [Glossaries and Quizzes](20-glossaries-and-quizzes/index.md) — Covers writing ISO 11179-compliant glossary definitions and generating Bloom's-aligned quizzes.
21. [MicroSim Anatomy and p5.js Basics](21-microsim-anatomy-p5js-basics/index.md) — Introduces the standard MicroSim directory structure and builds a first interactive simulation with p5.js.
22. [p5.js Controls and MicroSim Quality](22-p5js-controls-microsim-quality/index.md) — Covers the built-in p5.js control widgets and the standardization and quality-scoring checks every MicroSim must pass.
23. [The MicroSim Generator and Metadata Schema](23-microsim-generator-metadata-schema/index.md) — Explains how the MicroSim generator routes a request to a visualization library and documents it in metadata.
24. [Visualization Libraries and Systems Diagrams](24-visualization-libraries-systems-diagrams/index.md) — Surveys the MicroSim generator's other visualization families, including causal loop diagrams and batch scripts.
25. [Text-to-Image Models and the Verified Infographic Pipeline](25-verified-infographic-pipeline/index.md) — Explains why one-shot infographic generation fabricates facts and introduces the eight-phase verified pipeline.
26. [Interactive Infographic Overlays](26-interactive-infographic-overlays/index.md) — Covers the annotation-free illustration technique paired with a JavaScript overlay layer and its audit trail.
27. [Slide Decks, Stories, and Audio Media](27-slide-decks-stories-audio-media/index.md) — Covers MARP decks, PowerPoint lectures, illustrated stories, freely-licensed image sourcing, and text-to-speech narration.
28. [Domain-Specific Skill Extension: Electronics Case Study](28-domain-specific-skill-extension/index.md) — Walks through extending the skill library into a new domain using a beginning-electronics case study.
29. [Book Installer Features](29-book-installer-features/index.md) — Covers the book-installer meta-skill's feature system, from scaffolding a new textbook to installable extras.
30. [Session Logs and Book Metrics](30-session-logs-book-metrics/index.md) — Covers writing session logs and design decision records, and the canonical `book-metrics.json` hub.
31. [Publishing and Announcing a Finished Book](31-publishing-announcing-book/index.md) — Covers generating a README, LinkedIn posts, and a press release, closing with the book's capstone launch checklist.

## Appendices

Practical setup and workflow guides that stand outside the concept-dependency
sequence above:

- [Appendix A: Running Claude on the Raspberry Pi](appendix-a-claude-on-pi/index.md)
- [Appendix B: Installing Claude on Windows Subsystem for Linux (WSL)](appendix-b-claude-on-wsl/index.md)
- [Appendix C: User Global Claude Configuration](appendix-c-user-global-claude/index.md)
- [Appendix D: Parallel Execution of Tasks](appendix-d-parallel-execution/index.md)

## How to Use This Textbook

Work through the chapters in order — each one lists the earlier chapters its
concepts depend on, so prerequisites are always covered before they are
needed. The appendices can be read at any time; they support specific
platforms and workflows rather than building on the concept graph.

---

**Note:** Each chapter includes a list of concepts covered. Make sure to complete prerequisites before moving to advanced chapters.
