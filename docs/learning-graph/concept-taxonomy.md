# Concept Taxonomy

The 570 concepts in the [learning graph](./learning-graph.json) are organized into
14 categories. Each category has a short `TaxonomyID` used in the
`TaxonomyID` column of [learning-graph.csv](./learning-graph.csv) and as the
group key in the graph viewer legend.

Categories were chosen so that no single category dominates the graph. The
largest category holds under 12% of all concepts, well below the 30% ceiling
used as a quality threshold for this project.

## Categories

### Foundations of AI and Intelligent Books

**TaxonomyID:** `FOUND`

Core ideas a reader needs before anything else: what a large language model is,
what tokens and context windows are, how an AI coding agent differs from a chat
interface, and what makes a textbook "intelligent" across the five levels of
textbook intelligence.

### Agent Skill Architecture

**TaxonomyID:** `SKARCH`

The structure of a skill itself — the `SKILL.md` file, the frontmatter contract,
the directory layout, progressive disclosure and its three loading budgets, and
the meta-skill routing pattern that keeps a large library under the loading limit.

### Skill Development and Portability

**TaxonomyID:** `SKDEV`

Building, testing, installing, and distributing skills, plus everything involved
in making one skill library run across Claude Code, Codex, Gemini, Cursor, and
Copilot without forking it.

### Token Optimization and Measurement

**TaxonomyID:** `TOKEN`

Treating tokens as an engineering budget: plan limits and usage windows, the cost
of serial versus parallel sub-agents, file layout as a token strategy, and the
hooks and logs used to measure what each skill actually consumes.

### Python Tooling and Automation

**TaxonomyID:** `PYTOOL`

The scripts that do the deterministic work — parsing, validating, scaffolding,
counting, and converting — together with the general Python practices that make
those scripts safe to run repeatedly.

### Course Design and Pedagogy

**TaxonomyID:** `CDESIGN`

Course descriptions, Bloom's Taxonomy and its six cognitive levels, learning
outcomes, reading level, instructional scaffolding, and the pedagogical mascot
conventions used to guide readers.

### Learning Graphs

**TaxonomyID:** `LGRAPH`

Concepts, learning dependencies, and the directed acyclic graph they form:
enumeration, dependency mapping, quality metrics, taxonomy assignment, and the
JSON format that drives the interactive graph viewer.

### Chapter and Content Generation

**TaxonomyID:** `CONTENT`

Turning a learning graph into chapters — structure design, concept assignment,
section organization, admonitions, math support, and the specification blocks
that later drive diagram and simulation generation.

### Supporting Content

**TaxonomyID:** `SUPPORT`

The material that surrounds the chapters: ISO 11179-compliant glossaries, FAQs
and their chatbot exports, quizzes and distractor quality, and curated reference
lists that credit the authors behind influential explanations.

### Interactive Simulations

**TaxonomyID:** `MSIM`

MicroSims end to end — directory structure and file separation, metadata schemas,
the visualization libraries the generator routes between, iframe embedding and
height management, and the quality and screenshot utilities that maintain them.

### Images, Infographics, and Media

**TaxonomyID:** `MEDIA`

Everything generated as pixels or audio: text-to-image models and their
fabrication risks, the verified infographic pipeline, interactive overlay
engines, freely-licensed image sourcing, slide decks, and text-to-speech.

### Domain-Specific Skill Extension

**TaxonomyID:** `DOMAIN`

Extending a subject-neutral library into a specific field, using the
beginning-electronics case study: circuit schematic generation, breadboard
simulations, and rubric-driven hands-on lab evaluation.

### Platform, Tooling, and Deployment

**TaxonomyID:** `PLATFORM`

MkDocs and the Material theme, site features, the editor and terminal, Git and
GitHub, deployment to GitHub Pages, and analytics registration.

### Publishing, Metrics, and Promotion

**TaxonomyID:** `PUBLISH`

Measuring a finished book and announcing it: the canonical book metrics hub,
README generation, LinkedIn posts and carousels, press releases, and the session
logs that record how the book was built.
