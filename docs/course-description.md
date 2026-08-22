---
title: Course Description for Agent Skills to Create Intelligent Textbooks
description: A detailed course description for building intelligent textbooks with a portable, token-efficient library of Agent Skills
quality_score: 95
---
# Using Agent Skills to Create Intelligent Textbooks

**Title:** Using Agent Skills to Create Intelligent Textbooks
**Target Audience:** Professional development
**Reading Level:** undergrad college student

## Prerequisites:

- Basic understanding of programming and the ability to read, run, and modify a short Python script
- Basics of prompt engineering
- Comfort with a terminal shell, a text editor, and basic Git operations
- Access to at least one AI coding agent such as Claude Code, OpenAI Codex, Google Antigravity, or Cursor
- A GitHub account for hosting a published book
- Curiosity about using AI to build textbooks

## Course Overview

This course provides comprehensive training on leveraging [Agent Skill](./glossary.md#agent-skill) to create intelligent, interactive textbooks that enhance learning through AI-assisted content generation. Participants learn the complete workflow from writing a high-quality [Course Description](./glossary.md#course-description), through generating a [Learning Graph](./glossary.md#learning-graph) of 300–600 concepts, designing chapter structure, generating [Chapter Content Generator](./glossary.md#chapter-content-generator), building interactive simulations, producing [Glossary](./glossary.md#glossary), quizzes, FAQs and references, and finally publishing, measuring, and announcing a finished book.

The reference library that accompanies this course is no longer a handful of prompts. It is **14 production Agent Skills**, backed by **99 on-demand reference guides**, **80 Python programs**, and **19 `bk-*` command-line tools**. Five of those skills are **meta-skills** — routers that read a request, match it against a keyword table, and load only the one guide needed for that job. This architecture exists for two reasons: an agent may only load about 30 skills at once, and every byte loaded costs money. Students learn to design skills the same way: a small always-resident description, a compact router, and heavyweight detail that loads only when earned.

A central theme of the course is **token frugality**. Most teachers cannot justify a $100/month AI subscription and want to build their books on a $20/month plan. The course therefore treats tokens as a first-class engineering budget. Students learn measured techniques rather than folklore: that each additional parallel sub-agent costs roughly 12,000 tokens of startup overhead, so a 350-term glossary is cheaper to write with **one** serial agent (~31,000 tokens total, ~54 tokens per marginal term) than with many parallel ones; that storing chapter references in separate `references.md` files drops the cost of a full 15-chapter reference update from ~90,000 tokens to ~3,000; that a batch of MicroSims scaffolded by Python utilities instead of by the model saves roughly 430,000 tokens per chapter run; and that a quality gate which already scores above 85 should be skipped rather than re-run. Students install usage-tracking hooks, analyze the resulting JSONL logs with Python, and build dashboards showing elapsed time and token consumption per skill.

The second theme is **Python as the agent's hands**. Anything deterministic — parsing, counting, validating, scaffolding, renaming, resizing, measuring — belongs in a script, not in the model's output stream. Students read and extend the actual programs used by the skills: `analyze-graph.py` for graph quality metrics, `csv-to-json.py` for vis-network conversion, `validate-learning-graph.py` for [Directed Acyclic Graph](./glossary.md#directed-acyclic-graph) and schema checks, `extract-sim-specs.py` for parsing simulation specifications out of chapter markdown, `sync-iframe-heights.py` for keeping every embedded simulation the right height, `calculate-quality-score.py` for MicroSim scoring, `book-metrics.py` for the canonical statistics hub every publishing route reads, `analyze-reading-levels.py` for Flesch-Kincaid consistency across chapters, and image utilities that trim, compress, and generate favicons and social cards. The rule students internalize is simple: the model writes the creative artifact; Python does everything countable.

The third theme is **breadth of generated media**. The MicroSim generator now routes across sixteen visualization families — p5.js simulations, Chart.js and Plotly charts, vis-network concept maps, Mermaid diagrams, vis-timeline chronologies, Leaflet maps, Venn and bubble diagrams, comparison and clickable matrix tables, causal-loop diagrams for systems thinking, concept-classifier sorting quizzes, celebration animations, Docker-backed runnable Python labs, interactive infographic overlays, and fact-verified statistics posters. The media generator adds MARP web decks, downloadable PowerPoint lectures with speaker notes, illustrated stories, freely-licensed chapter images sourced from Wikimedia and government archives, and ElevenLabs text-to-speech narration and glossary pronunciation buttons.

The quality of text-to-image models has changed what is possible here, and the course treats that change carefully. Modern image models can place long, exact text precisely inside a large, complex composition — which makes beautiful infographic posters achievable and factual errors permanent. In one measured session, eight of ten numeric claims in a one-shot generated poster were unsupported by their cited sources and two of five citations were fictional. The library's answer is an eight-phase pipeline that **separates facts from pixels**: claims are planned, sourced, verified against quoted passages, and locked in a YAML layout specification before a single image call is made, and every rendered number remains traceable to a source URL in a sidecar audit file. The complementary technique is the **interactive infographic overlay**, where the image model produces a deliberately annotation-free illustration and a JavaScript layer draws the numbered callouts, leader lines, hover explanations, and quiz modes on top — so labels stay editable, translatable, and accessible instead of being baked into pixels.

Finally, the course covers **domain extension**. The core library is subject-neutral, but real books need vocabulary the core does not have. Students study a worked example from a beginning-electronics textbook, where three project-local skills extend the library: a breadboard simulation generator that places components in real tie-point holes and animates current along jumper wires, a Schemdraw skill that turns a plain-language circuit description into a maintainable Python program and a verified schematic image, and a hands-on lab evaluator that scores a lab against a 103-point rubric for reader age and parts-kit buildability, then writes the score into frontmatter and files each gap as a work item. Students learn when to route to a general skill, when a domain deserves its own, and how a project skill inherits the same standards as the shared library.

Because these skills follow the open **Agent Skills** standard — a folder with a `SKILL.md`, a two-field frontmatter contract, and progressive disclosure — they also run in OpenAI Codex, Gemini, Cursor, and GitHub Copilot. Students learn which frontmatter fields are portable, which are vendor extensions, and how to degrade gracefully when a platform lacks a capability such as image understanding.

Through this professional development opportunity, learners gain expertise in both the technical craft of building and maintaining an Agent Skill library and the educational design principles — [Bloom's Taxonomy](./glossary.md#blooms-taxonomy), [ISO 11179 Standards](./glossary.md#iso-11179-standards) definitions, dependency-ordered concept sequencing — that make an [intelligent textbook](./glossary.md#intelligent-textbook) an effective learning tool rather than merely a generated one.

## Main Topics Covered

### Foundations

- What Agent Skills are and how they differ from prompts, commands, and chat
- The Agent Skills open standard and the `SKILL.md` frontmatter contract
- Progressive disclosure and the three loading budgets
- Prompt engineering for educational content
- Large language model basics relevant to content generation
- The five levels of textbook intelligence
- Intelligent textbook workflows end to end

### Skill Architecture and Engineering

- Skill directory structure: `SKILL.md`, `references/`, `scripts/`, `assets/`
- Writing a description that triggers reliably and does not misfire
- Meta-skill architecture and keyword routing tables
- The 30-skill loading limit and how consolidation works around it
- On-demand reference guides and when to split a guide out
- Model selection per skill (`opus` vs `sonnet`) and its cost consequences
- Allowed tools, permissions, and security in skill execution
- Skill packaging, symlink installation, and distribution
- Project-local skills versus globally installed skills
- Testing, debugging, and versioning a skill
- Skill portability across Claude Code, Codex, Gemini, Cursor, and Copilot
- Graceful degradation when a platform lacks a capability
- Creating new Claude commands and runbooks such as `/ibook`

### Token Optimization and Resource Measurement

- Why token budget, not wall-clock time, is the binding constraint
- Serial versus parallel sub-agents and the ~12K-token startup overhead
- Measured case study: a 350-term glossary in ~31K tokens
- File layout as a token strategy: separate `references.md` and `quiz.md` files
- Batch Python utilities that replace model output (~430K tokens saved per chapter)
- Short-circuiting quality gates that already pass
- Context window management and chapter-level token budgeting
- Claude usage limits, 4-hour and 5-hour windows, and Pro plan constraints
- Installing usage-tracking hooks
- Analyzing skill usage JSONL logs with Python
- Building dashboards for elapsed time and token consumption per skill
- Cost estimation for a complete book

### Python Inside Skills

- The division of labor: model writes creative artifacts, Python does the countable work
- Reading and extending the library's Python programs
- Graph analysis and quality metrics (`analyze-graph.py`)
- CSV to vis-network JSON conversion (`csv-to-json.py`)
- Schema and DAG validation (`validate-learning-graph.py`)
- Taxonomy assignment and distribution reporting
- Parsing chapter markdown for simulation specifications
- Scaffolding MicroSim directories from a specification file
- Iframe height synchronization from a single `CANVAS_HEIGHT` value
- MicroSim quality scoring and validation
- Book metrics, equation counting, and equivalent page calculation
- Reading level analysis across chapters
- Image utilities: trimming, compression, favicon and social card generation
- Site metrics collection for READMEs and announcements
- The `bk-*` command-line tool family and shell script conventions
- pip package management and virtual environments

### Course Design and the Learning Graph

- Writing and scoring a course description
- 2001 Bloom's Taxonomy and action verbs for learning outcomes
- Defining target audience, reading level, and prerequisites
- Declaring topics explicitly excluded from scope
- Concept enumeration to 300–600 atomic concepts
- Concept label conventions and granularity
- Dependency mapping and pipe-delimited CSV format
- Directed acyclic graphs, cycle detection, and orphan nodes
- Foundational concepts, terminal nodes, and dependency chain length
- Taxonomy categorization and category distribution limits
- Learning graph quality scoring and remediation
- Interactive learning graph visualization with vis-network
- Using the learning graph as a student-facing roadmap

### Chapter Structure and Content Generation

- Designing chapter structure from concept dependencies
- Ensuring every concept is covered exactly once
- Chapter index files, concept lists, and summaries
- Generating chapter content at the right reading level
- Instructional scaffolding and define-before-display rules
- Worked examples, practice exercises, and admonitions
- Pedagogical mascots, voice, and placement rules
- Math equation support with MathJax
- Diagram and drawing specification blocks inside chapters
- Glossary generation with ISO 11179-compliant definitions
- FAQ generation and chatbot-ready JSON export
- Quiz generation with Bloom's distribution and distractor quality
- Curated reference generation that credits pedagogical innovators
- Instructor guides and supplementary content

### Interactive Simulations (MicroSims)

- MicroSim anatomy: `main.html`, `style.css`, `script.js`, `data.json`, `metadata.json`, `index.md`
- Why file separation matters for maintenance and caching
- MicroSim metadata schema and Dublin Core fields
- Routing a request to the right visualization library
- p5.js simulations and the built-in control conventions
- Chart.js and Plotly for data and function visualization
- vis-network concept maps and vis-timeline chronologies
- Leaflet maps, Venn diagrams, and bubble matrices
- Mermaid flowcharts and structural diagrams
- Causal loop diagrams and systems archetypes
- Comparison tables and clickable matrix tables
- Concept-classifier sorting activities
- Docker-backed runnable Python lab exercises
- Matching Bloom's level to interaction pattern
- Iframe embedding, canvas height, and responsive layout
- Screenshot capture and MicroSim index catalogs
- Quality validation, standardization, and layout review
- Diagram coverage reports across chapters

### Images, Infographics, and Media

- What ultra-high-quality text-to-image models changed
- Why one-shot factual infographics fabricate data
- The eight-phase verified poster pipeline
- Claim planning, source discovery, and passage-level verification
- Locking a layout specification before any image call
- Writing a verbatim-text image prompt that forbids substitution
- Auditing a rendered image against its claim set
- Preserving a source audit trail in sidecar files
- Interactive infographic overlays: callout and grid engines
- Annotation-free illustrations plus a JavaScript label layer
- Explore mode, quiz mode, and editable marker positions
- Sourcing freely-licensed images from Wikimedia and government archives
- Cover images, logos, favicons, and social media previews
- MARP web decks published to the site
- PowerPoint lecture decks with speaker notes
- Illustrated stories and graphic novel formats
- Text-to-speech narration and glossary pronunciation buttons

### Domain-Specific Skill Extension

- Deciding when a subject needs its own skill
- Case study: extending the library for beginning electronics
- Generating circuit schematics from prose with Python Schemdraw
- Breadboard simulations with tie-point placement and animated current
- Rubric-driven lab evaluation and automatic work-item filing
- Writing frontmatter quality scores that drive a TODO backlog
- Keeping a project skill aligned with shared library standards

### Platform, Publishing, and Operations

- MkDocs and the Material theme
- `mkdocs.yml` configuration and navigation maintenance
- Site features: search, code highlighting, admonitions, image zoom, comments, feedback
- Custom 404 pages, document status indicators, and about pages
- Visual Studio Code for content development
- Integrating an AI coding agent into your IDE
- Terminal commands and command-line interfaces
- Git and revision control for content management
- GitHub Pages deployment and `gh-deploy`
- Google Analytics GA4 registration and measurement IDs
- Book metrics as a single canonical statistics hub
- GitHub Projects Kanban boards for textbook development
- README generation with badges and site statistics
- LinkedIn announcement posts and carousel documents
- AP-style press releases
- Running the full pipeline as an ordered runbook

## Topics Not Covered

While this course provides comprehensive coverage of Agent Skills for intelligent textbook creation, the following topics are explicitly out of scope:

- Advanced machine learning theory, model training, or fine-tuning
- Training or hosting your own text-to-image model
- General web development beyond MkDocs and some simple CSS
- JavaScript framework development (React, Vue, Svelte)
- Database administration beyond graph concepts
- Advanced Git workflows for large development teams
- General Python programming (only the specific scripts used in the workflow)
- Graphic design theory and manual image editing
- Video production and multimedia post-production
- Learning management system (LMS) integration
- xAPI server administration and learning record store operations
- Accessibility compliance in depth (though best practices are mentioned)
- Copyright and intellectual property law
- Electronics as a subject (it appears only as a domain-extension example)

## Learning Outcomes

After completing this course, students will be able to:

### Remember
*Retrieving, recognizing, and recalling relevant knowledge from long-term memory.*

- Remember the ordered steps in creating an intelligent textbook
- Remember what a learning graph is and why it must be acyclic
- Remember what an Agent Skill is and the two required frontmatter fields
- Remember the difference between a skill, a meta-skill, and a command
- Remember the standard MicroSim directory structure and required files
- Remember the steps to install a skill, a command, and the `bk-*` scripts
- Remember how to list the skills currently available to an agent
- Remember that skill resource utilization can be monitored with hooks
- Remember the approximate token overhead of launching an additional sub-agent
- Remember which Python script performs each deterministic step in the pipeline

### Understand
*Constructing meaning from instructional messages, including oral, written, and graphic communication.*

- Understand how skills are loaded, triggered, and used
- Understand how progressive disclosure keeps a large library affordable
- Understand how a meta-skill routes a request to a single reference guide
- Understand why the 30-skill limit forces consolidation
- Understand how hooks measure elapsed time and token usage per skill
- Understand which skills an intelligent textbook needs and in what order
- Understand how a learning graph guides students along a learning journey
- Understand why deterministic work belongs in Python and not in model output
- Understand why one-shot factual infographics fabricate numbers
- Understand why an annotation-free image plus a label layer beats baked-in text
- Understand how the Agent Skills standard makes a library portable across vendors

### Apply
*Carrying out or using a procedure in a given situation.*

- Apply the course-description-analyzer to score and repair a course description
- Apply the learning-graph-generator to produce 300–600 dependency-ordered concepts
- Apply the Python validation scripts to check a graph for cycles and orphans
- Apply the chapter and content generators to draft a complete chapter
- Apply the MicroSim generator to build simulations across several libraries
- Apply the batch Python utilities to scaffold and validate a chapter of MicroSims
- Apply the verified-infographic pipeline to produce a poster with a source audit trail
- Apply the overlay technique to add interactive callouts to a generated illustration
- Apply prompt engineering and the skill-creator skill to build a new skill
- Apply the command creation steps to create new commands and runbooks
- Apply skill usage log analysis to measure time and token consumption
- Apply the publishing skills to generate a README, an announcement, and a press release

### Analyze
*Breaking material into constituent parts and determining how the parts relate to one another and to an overall structure or purpose.*

- Analyze the result of a skill execution against its stated contract
- Analyze the quality of content generated by a skill
- Analyze the completeness of a document such as a course description
- Analyze a learning graph's quality metrics and diagnose structural defects
- Analyze which parts of a workflow should be Python and which should be model output
- Analyze where the token budget is actually being spent in a build
- Analyze whether serial or parallel execution is cheaper for a given task
- Analyze whether a skill should be split, consolidated, or routed
- Analyze why skills fail to install, trigger, or load their reference guides
- Analyze whether quality reports and coverage reports are working correctly
- Analyze skill usage log files and dashboard reports
- Analyze reading level consistency across chapters
- Analyze a domain to decide whether it warrants a project-specific skill

### Evaluate
*Making judgments based on criteria and standards through checking and critiquing.*

- Evaluate the quality of a course description against required elements
- Evaluate the quality and trigger reliability of a skill description
- Evaluate whether a quality test is a good use of tokens
- Evaluate whether a skill should run on a larger or smaller model
- Evaluate the quality of a generated book using book metrics
- Evaluate glossary definitions against ISO 11179 criteria
- Evaluate quiz questions and the plausibility of their distractors
- Evaluate a MicroSim against the quality and layout standards
- Evaluate whether every numeric claim in an infographic is traceable to a source
- Evaluate the portability of a skill across non-Claude agent platforms
- Evaluate the quality of a book announcement and its preview images
- Evaluate the total cost of producing a book against a monthly plan budget

### Create
*Putting elements together to form a coherent or functional whole; reorganizing elements into a new pattern or structure.*

- Create new skills from scratch that follow the Agent Skills standard
- Create a meta-skill with a routing table and on-demand reference guides
- Create Python utilities that replace repetitive model output
- Create new `bk-*` command-line tools for your own workflows
- Create new commands and ordered runbooks for agent workflows
- Create dashboards for monitoring skill resource utilization
- Create domain-specific skills for a subject the core library does not cover
- Create fact-verified infographics and interactive labeled diagrams
- Create new intelligent textbooks for a variety of subjects
- Design and implement a complete intelligent textbook project (capstone)
