# Glossary of Terms

This glossary contains definitions of key concepts used throughout the course "Using Claude Skills to Create Intelligent Textbooks." Each definition follows ISO 11179 metadata registry standards: precise, concise, distinct, non-circular, and free of business rules.

## A

#### Action Verbs for Learning Outcomes

Specific action words that describe observable behaviors students can demonstrate at each level of Bloom's Taxonomy.

**Example:** The verb "define" indicates Remember level, while "design" indicates Create level in learning outcomes.

#### add-taxonomy.py Script

A Python program that adds a taxonomy categorization column to a learning graph CSV file.

**Example:** Running this script on `learning-graph.csv` adds a TaxonomyID field to categorize each concept.

#### Advanced Concepts

High-level ideas that require multiple prerequisite concepts to be understood before they can be mastered.

**Example:** "Capstone: Complete Textbook Project" depends on understanding all 199 prior concepts in the learning graph.

#### Admonitions in MkDocs

Specially formatted callout boxes in Material for MkDocs that highlight notes, warnings, tips, or important information.

**Example:** Using `!!! note` creates a blue box with "Note" header to draw attention to key information.

#### Allowed Tools in Skills

Specification in skill YAML frontmatter defining which Claude Code tools the skill is permitted to use.

**Example:** A skill might specify `allowed-tools: [Read, Write, Bash]` to limit file operations.

#### Analyze (Cognitive Level 4)

The fourth level of Bloom's Taxonomy where learners break material into parts and determine relationships between components.

**Example:** Students analyze why a skill fails by examining error logs, file permissions, and workflow dependencies.

#### analyze-graph.py Script

A Python program that validates learning graph structure, detects circular dependencies, and generates quality metrics reports.

**Example:** This script checks if your 200-concept graph is a valid DAG and reports statistics like average dependencies per concept.

#### Anthropic Claude Pro Account

A paid subscription to Claude AI that provides extended usage limits, longer conversation context, and access to Claude Code.

**Example:** A Claude Pro account allows 4-hour usage windows with higher token limits for generating textbook content.

#### Apply (Cognitive Level 3)

The third level of Bloom's Taxonomy where learners carry out procedures or use knowledge in specific situations.

**Example:** Students apply prompt engineering principles to create a new skill for generating chapter quizzes.

#### Artificial Intelligence

Computer systems designed to perform tasks that typically require human intelligence, such as learning, reasoning, and problem-solving.

**Example:** Claude AI uses artificial intelligence to understand course descriptions and generate structured learning content.

#### Assessing Course Descriptions

The process of evaluating a course description for completeness, clarity, and alignment with educational standards.

**Example:** The course-description-analyzer skill scores descriptions on presence of prerequisites, Bloom's outcomes, and target audience.

#### Assessing Student Understanding

Methods for evaluating whether learners have mastered concepts through quizzes, exercises, and interactive activities.

**Example:** Multiple-choice quizzes aligned to Bloom's Taxonomy levels assess student understanding across cognitive domains.

#### Assessing Student Understanding Through Quiz Analytics

Evaluation of learner comprehension by analyzing quiz performance patterns across cognitive levels and concept areas to identify knowledge gaps.

**Example:** Analyzing quiz results shows students score well on Remember questions but struggle with Analyze questions, indicating need for more worked examples.

#### Atomic Concepts

Single, indivisible ideas that cannot be meaningfully broken into smaller learning components.

**Example:** "Variable" is atomic, while "Variable Declaration and Assignment" could be split into two atomic concepts.

#### Average Dependencies Per Concept

The mean number of prerequisite relationships each concept has in a learning graph.

**Example:** A well-structured graph typically has 2-4 average dependencies per concept, avoiding both isolation and over-complexity.

#### Avoiding Over-Representation

The practice of ensuring no single taxonomy category contains too many concepts, maintaining balanced distribution.

**Example:** If 60% of concepts are in the BASIC category, the graph may need rebalancing across foundational and advanced levels.

## B

#### Bash

A Unix shell and command language used for executing system commands, running scripts, and automating tasks.

**Example:** Running `./install-claude-skills.sh` in Bash creates symlinks to make skills available globally.

#### Bloom's 2001 Revision

An updated framework of cognitive learning objectives that replaced "Knowledge" with "Remember" and "Synthesis" with "Create."

**Example:** The 2001 revision emphasizes active learning verbs and clearer distinctions between cognitive levels.

#### Bloom's Taxonomy

A hierarchical framework of six cognitive levels used to classify educational learning objectives from simple recall to complex creation.

**Example:** Learning outcomes progress from Remember (defining terms) through Create (designing complete textbooks).

#### Bloom's Taxonomy in Quizzes

The practice of distributing quiz questions across all six cognitive levels to assess comprehensive understanding.

**Example:** A quiz includes 20% Remember questions, 20% Understand, 15% Apply, 20% Analyze, 15% Evaluate, and 10% Create.

## C

#### Capstone: Complete Textbook Project

A culminating project where learners design and implement an entire intelligent textbook from course description through deployment.

**Example:** The capstone requires creating a learning graph, generating content, building MicroSims, and publishing to GitHub Pages.

#### Category Distribution

The spread of concepts across different taxonomy categories in a learning graph.

**Example:** A balanced distribution might be 15% foundational, 35% basic, 30% intermediate, 15% advanced, and 5% integration concepts.

#### Chapter Concept Lists

Enumerated sets of specific concepts that will be covered within a particular chapter of a textbook.

**Example:** Chapter 3's concept list includes concepts 45-67 from the learning graph, respecting dependency order.

#### Chapter Index Files

Markdown files named `index.md` that serve as the main content page for each chapter in a MkDocs textbook.

**Example:** `/docs/chapters/03/index.md` contains the title, summary, concept list, and full content for Chapter 3.

#### Chapter Structure

The organizational framework defining how textbook content is divided into major sections with logical progression.

**Example:** A 200-concept course might be organized into 12 chapters with 15-20 concepts per chapter.

#### Chapter Structure and Token Budgeting

The dual consideration of logical content organization and AI token limit management when designing textbook chapters.

**Example:** Balancing pedagogical needs (15-20 concepts per chapter) with practical constraints (staying under Claude's token limits per generation).

#### Circular Dependency Detection

The process of identifying invalid prerequisite loops where concept A depends on B, which depends on C, which depends on A.

**Example:** If "Variables" requires "Functions" which requires "Variables," the analyze-graph.py script reports a circular dependency error.

#### Claude AI

An artificial intelligence assistant created by Anthropic that uses large language models to understand and generate human-like text.

**Example:** Claude AI can read a course description and generate a complete 200-concept learning graph with dependencies.

#### Claude Code Interface

The command-line tool that enables users to interact with Claude AI for software development and content creation tasks.

**Example:** Running `claude` in the terminal launches an interactive session where you can invoke skills and execute commands.

#### Claude Command

A user-defined operation in Claude Code that expands a slash command into a full prompt for common workflows.

**Example:** The `/skills` command expands to list all available Claude skills in the current project.

#### Claude Pro Limitations

Usage restrictions on Claude Pro accounts including token limits per message and 4-hour usage windows.

**Example:** Claude Pro allows higher token limits than free accounts but still requires managing usage within 4-hour windows.

#### Claude Skill

An autonomous agent defined by a SKILL.md file that automates specific tasks in the Claude Code environment.

**Example:** The learning-graph-generator skill automates creating a 200-concept dependency graph from a course description.

#### Claude Token Limits

Maximum number of tokens (roughly word pieces) that can be processed in a single Claude conversation or message.

**Example:** Managing token limits requires breaking large content generation into multiple skill invocations.

#### Color Coding in Visualizations

Using distinct colors to represent different categories, groups, or properties in graphical displays.

**Example:** Learning graph visualizations use color to distinguish foundational concepts (orange) from advanced concepts (purple).

#### Command-Line Interface Basics

Fundamental concepts and operations for interacting with computers through text-based terminal commands.

**Example:** Basic CLI skills include navigating directories with `cd`, listing files with `ls`, and running scripts.

#### Command Definition Files

Markdown files that specify slash command behaviors, stored in the `.claude/commands/` directory.

**Example:** The file `.claude/commands/skills.md` defines what happens when you type `/skills`.

#### Common Student Questions

Frequently asked queries that learners typically have about course content, processes, or concepts.

**Example:** "How do I install a skill globally versus project-specific?" is a common question addressed in the FAQ.

#### Concept Categorization

The process of organizing concepts into groups based on difficulty level, subject area, or other distinguishing characteristics.

**Example:** Categorizing concepts as foundational, basic, intermediate, or advanced helps structure curriculum progression.

#### Concept Dependencies

Prerequisite relationships where understanding one concept requires prior mastery of other specific concepts.

**Example:** Understanding "Dependency Edges in Learning Graphs" depends on first understanding "Learning Graph."

#### Concept Enumeration Process

The systematic method of identifying and listing all atomic concepts that comprise a course or subject area.

**Example:** Reading the course description and generating exactly 200 distinct, atomic concepts covering all main topics.

#### Concept Granularity

The level of detail or specificity at which ideas are broken down into individual learning components.

**Example:** "Git Commands" has low granularity, while separate concepts for "Git Add Command," "Git Commit Command" has higher granularity.

#### Concept Label Requirements

Specifications that concept names must follow, including Title Case formatting and maximum character length constraints.

**Example:** Concept labels must be in Title Case and not exceed 32 characters to ensure readability in visualizations.

#### ConceptID Field

A unique numeric identifier assigned to each concept in a learning graph CSV file.

**Example:** The ConceptID field contains integers from 1 to 200, providing a stable reference for each concept.

#### ConceptLabel Field

The human-readable name of a concept in a learning graph CSV file, following Title Case and length conventions.

**Example:** The ConceptLabel field might contain "Learning Graph" or "Directed Acyclic Graph (DAG)."

#### Concept Nodes in Learning Graphs

Individual concepts represented as vertices in a directed graph structure showing learning relationships.

**Example:** In a visualization, each concept appears as a labeled circle (node) with arrows (edges) pointing to dependent concepts.

#### Concise Definitions

Brief explanations that convey essential meaning using minimal words, typically 20-50 words for glossary entries.

**Example:** "A directed graph of concepts" is more concise than "A specialized type of graph structure that shows relationships."

#### Content Generation Process

The systematic workflow for creating textbook chapters, sections, and supporting materials using AI assistance.

**Example:** The chapter-content-generator skill reads concept lists and generates comprehensive content with examples and exercises.

#### Course Description

A comprehensive document defining a course's title, audience, prerequisites, topics, exclusions, and Bloom's Taxonomy-aligned outcomes.

**Example:** A complete course description enables the learning-graph-generator skill to identify relevant concepts and dependencies.

#### Course Description Quality Score

A numeric assessment (1-100) evaluating how well a course description meets completeness and clarity standards.

**Example:** A score of 95 indicates all required sections are present with clear, measurable learning outcomes.

#### Course Prerequisites

Knowledge, skills, or experiences that learners must possess before beginning a course.

**Example:** Prerequisites for this course include basic programming understanding and access to Claude Pro.

#### Create (Cognitive Level 6)

The highest level of Bloom's Taxonomy where learners put elements together to form coherent, original works.

**Example:** Students create new Claude skills from scratch, designing workflows and writing skill definition files.

#### Creator Metadata Field

Dublin Core element identifying the person, organization, or entity responsible for creating a resource.

**Example:** The creator field in metadata.json might contain "Dan McCreary" or your organization name.

#### csv-to-json.py Script

A Python program that converts learning graph CSV files into vis-network JSON format for visualization.

**Example:** Running this script transforms `learning-graph.csv` into `learning-graph.json` with nodes and edges arrays.

#### CSV File Format for Graphs

A structured text format using comma-separated values to store learning graph data with headers and rows.

**Example:** Graph CSVs contain columns: ConceptID, ConceptLabel, Dependencies, TaxonomyID.

## D

#### DAG Validation

The process of verifying that a learning graph forms a valid directed acyclic graph with no circular dependencies.

**Example:** The analyze-graph.py script performs DAG validation and reports any cycles that would prevent topological sorting.

#### Date Metadata Field

Dublin Core element recording when a resource was created, modified, or published.

**Example:** The date field captures "2025-11-08" as the generation date for the learning graph.

#### Definitions Without Business Rules

ISO 11179 principle that glossary definitions should describe concepts without prescribing processes or requirements.

**Example:** Define "Prerequisites" as relationships between concepts, not "Students must complete prerequisites before advancing."

#### Dependency Edges in Learning Graphs

Directed arrows connecting prerequisite concepts to dependent concepts in a graph structure.

**Example:** An edge from "Variables" to "Functions" indicates that understanding variables is prerequisite for understanding functions.

#### Dependency Mapping Process

The systematic method of identifying and recording prerequisite relationships between all concepts in a learning graph.

**Example:** For each of 200 concepts, determine which prior concepts must be understood first and record them in the Dependencies field.

#### Dependencies Field

A CSV column containing pipe-delimited ConceptIDs representing prerequisite concepts that must be learned first.

**Example:** A Dependencies field of "1|5|12" means concepts 1, 5, and 12 are prerequisites for the current concept.

#### Description Metadata Field

Dublin Core element providing a textual explanation of a resource's content and purpose.

**Example:** The description field summarizes what the learning graph covers and its educational objectives.

#### Difference Between Skills & Commands

Skills are autonomous workflows defined in SKILL.md files, while commands are simple prompt expansions for common tasks.

**Example:** A skill generates entire chapters; a command might just list available skills or clear the conversation history.

#### Directed Acyclic Graph (DAG)

A graph structure with directed edges and no cycles, where you cannot traverse from any node back to itself.

**Example:** Learning graphs must be DAGs to ensure a valid learning sequence exists without circular prerequisites.

#### Directory Navigation

The process of moving between folders in a file system using command-line or graphical interfaces.

**Example:** Use `cd docs/chapters` to navigate into the chapters directory from the project root.

#### Disconnected Subgraphs

Separate groups of concepts in a learning graph that have no dependency connections between groups.

**Example:** If web development concepts and database concepts form separate clusters with no links, they are disconnected subgraphs.

#### Distinct Definitions

ISO 11179 principle ensuring each glossary entry is clearly distinguishable from related terms.

**Example:** "Learning Graph" and "Concept Dependency" have distinct definitions focusing on different aspects of concept relationships.

#### Dublin Core Metadata

A standardized set of 15 metadata elements for describing digital resources, including title, creator, date, and format.

**Example:** MicroSim metadata.json files use Dublin Core fields to document simulation properties.

## E

#### Edges Section in JSON

The array in vis-network JSON format containing objects that define directed connections between concept nodes.

**Example:** `{"from": 1, "to": 2}` in the edges array represents a dependency from concept 1 to concept 2.

#### Educational Content Prompts

Carefully designed instructions to AI systems specifying how to generate pedagogically sound learning materials.

**Example:** A prompt might request "Generate 5 worked examples demonstrating this concept at the Apply level of Bloom's Taxonomy."

#### Educational Simulation Design

The process of creating interactive visual models that demonstrate concepts through user manipulation and observation.

**Example:** A MicroSim showing bubble sort lets learners control array size and see step-by-step swaps in real-time.

#### Error Analysis in Skills

The systematic examination of skill execution failures to identify root causes and improvement opportunities.

**Example:** Analyzing error messages reveals that a skill failed because it expected a file in `/docs/learning-graph/` that didn't exist.

#### Evaluate (Cognitive Level 5)

The fifth level of Bloom's Taxonomy where learners make judgments based on criteria and standards.

**Example:** Students evaluate the quality of a generated glossary using ISO 11179 compliance as evaluation criteria.

## F

#### FAQ

A document containing Frequently Asked Questions and their answers to help learners find common information quickly.

**Example:** The FAQ addresses questions like "How do I install skills globally?" and "What's the difference between skills and commands?"

#### FAQ from Course Content

Questions and answers derived from analyzing course materials, learning graphs, and glossary terms.

**Example:** Generated FAQs explain technical terms from the glossary in simpler language with additional context.

#### FAQ Generation Process

The systematic workflow for creating comprehensive question-answer pairs from course content and anticipated learner needs.

**Example:** The faq-generator skill scans course content, identifies potential confusion points, and creates clear Q&A pairs.

#### File Access Permissions

Security settings that control which users and processes can read, write, or execute specific files.

**Example:** Script execution requires permission: `chmod +x install-claude-skills.sh` makes the file executable.

#### File Creation and Editing

The process of making new files or modifying existing files using text editors or command-line tools.

**Example:** Use `touch glossary.md` to create a new file, then edit it with VS Code or vim.

#### Five Levels of Textbook Intelligence

A framework categorizing educational materials from static text (Level 1) to AI-personalized learning (Level 5).

**Example:** Traditional PDFs are Level 1, while textbooks with adaptive quizzes and learning paths are Level 4.

#### Font Colors for Readability

Strategic color choices for text that ensure sufficient contrast and accessibility across different backgrounds.

**Example:** Light text on dark nodes requires careful color selection to maintain readability in graph visualizations.

#### Format Metadata Field

Dublin Core element specifying the file format or media type of a resource.

**Example:** The format field might indicate "text/html" for MicroSims or "application/json" for learning graphs.

#### Foundational Concepts

Fundamental ideas with no prerequisites that serve as building blocks for more advanced understanding.

**Example:** "Artificial Intelligence" and "Claude AI" are foundational concepts that don't depend on other course concepts.

#### 4-Hour Usage Windows

Time-based limits on Claude Pro usage where token allowances reset after four hours of activity.

**Example:** Planning to generate multiple chapters within a single 4-hour window maximizes efficiency.

## G

#### Generating 200 Concepts

The process of systematically enumerating exactly 200 atomic concepts that comprehensively cover a course's scope.

**Example:** The learning-graph-generator skill analyzes the course description and produces a numbered list of 200 concepts.

#### Git

A distributed version control system for tracking changes in source code and collaborating on software projects.

**Example:** Git commands like `git add`, `git commit`, and `git push` manage textbook content versions.

#### Git Add Command

A Git operation that stages modified or new files for inclusion in the next commit.

**Example:** `git add docs/glossary.md` stages the glossary file for committing to the repository.

#### Git Commit Command

A Git operation that saves staged changes to the local repository with a descriptive message.

**Example:** `git commit -m "Add glossary with 200 ISO 11179-compliant definitions"` records the glossary addition.

#### Git Push Command

A Git operation that uploads local commits to a remote repository like GitHub.

**Example:** `git push origin main` sends your latest commits to the main branch on GitHub.

#### Git Repository Structure

The organization of files, directories, and Git metadata within a version-controlled project.

**Example:** A textbook repo includes `/docs`, `/skills`, `.git` hidden folder, and configuration files like `mkdocs.yml`.

#### Git Status Command

A Git operation that displays the current state of the working directory and staging area.

**Example:** `git status` shows which files are modified, staged, or untracked.

#### GitHub Integration

The connection between local Git repositories and GitHub's cloud-based platform for hosting and collaboration.

**Example:** Linking a local textbook repository to GitHub enables deployment to GitHub Pages.

#### GitHub Pages Deployment

The process of publishing static website content to GitHub's free web hosting service.

**Example:** Running `mkdocs gh-deploy` builds the site and pushes it to the gh-pages branch for public access.

#### Glossary

An alphabetically organized collection of terms and their definitions specific to a subject area or course.

**Example:** This glossary defines 200 concepts related to creating intelligent textbooks with Claude Skills.

#### Glossary Generation Process

The systematic workflow for creating ISO 11179-compliant definitions from a concept list with quality validation.

**Example:** The glossary-generator skill reads concept lists, generates definitions, adds examples, and produces quality reports.

#### Groups Section in JSON

The array in vis-network JSON format defining visual properties for each taxonomy category.

**Example:** Groups specify colors like orange for foundational concepts and purple for advanced concepts.

## I

#### Iframe Embedding

The technique of inserting one HTML document inside another using the `<iframe>` tag.

**Example:** MicroSim documentation embeds `main.html` simulations in `index.md` pages using iframe tags.

#### Improving Skill Quality

The iterative process of refining skill workflows, error handling, and output quality through testing and feedback.

**Example:** Adding validation checks to skills ensures they fail gracefully when required input files are missing.

#### Indegree Analysis

Examining how many prerequisite concepts point to each concept in a learning graph.

**Example:** High indegree concepts require many prerequisites and are typically advanced topics.

#### index.md for MicroSim Docs

A markdown documentation file that describes a MicroSim's purpose, usage, and embeds the interactive simulation.

**Example:** `/docs/sims/bubble-sort/index.md` explains the simulation and embeds `main.html` in an iframe.

#### Installing a Claude Skill

The process of making a skill available for use in Claude Code by placing it in the `.claude/skills/` directory.

**Example:** Running `./scripts/install-claude-skills.sh` creates symlinks from project skills to global skills directory.

#### Installing Claude Commands

The process of placing command definition files in `.claude/commands/` to enable slash command usage.

**Example:** Copying `skills.md` to `.claude/commands/` enables the `/skills` command.

#### Installing Python Packages

The process of adding third-party Python libraries to your environment using package management tools.

**Example:** `pip install mkdocs-material` installs the Material theme for MkDocs documentation.

#### Installing Skills Globally

Placing skills in `~/.claude/skills/` to make them available across all Claude Code projects.

**Example:** Global skills can be invoked from any project directory without per-project installation.

#### Intelligent Textbook

An educational resource enhanced with interactive elements, adaptive content, or AI-powered features beyond static text.

**Example:** An intelligent textbook includes learning graphs, interactive MicroSims, and automatically generated quizzes.

#### Interactive Controls (Buttons)

User interface elements in MicroSims that trigger actions or state changes when clicked.

**Example:** A "Reset" button returns the simulation to initial conditions, while "Next Step" advances one iteration.

#### Interactive Controls (Sliders)

User interface elements in MicroSims that allow continuous value adjustment through dragging or clicking.

**Example:** A slider controls animation speed from 1 to 100, letting learners observe processes at different rates.

#### Interactive Elements

Components in educational materials that respond to user input and provide dynamic feedback.

**Example:** Interactive elements include clickable diagrams, adjustable parameters in simulations, and self-grading quizzes.

#### Interactive Simulations

Computer programs that model real-world or abstract processes, allowing learners to manipulate variables and observe outcomes.

**Example:** A physics simulation lets students adjust mass and velocity to see how momentum changes.

#### Invoking Skills with Slash Commands

The method of executing Claude skills by typing `/skill [skill-name]` in the Claude Code interface.

**Example:** Typing the skill name launches the skill to create a 200-concept dependency graph.

#### ISO 11179 Standards

International metadata registry standards defining principles for creating precise, concise, distinct, non-circular definitions.

**Example:** ISO 11179 requires glossary definitions avoid business rules like "must complete before advancing."

#### Iterative Prompt Refinement

The process of progressively improving AI prompts through testing, evaluation, and modification based on results.

**Example:** Refining a content generation prompt by adding "include 3 worked examples" after initial results lacked examples.

## J

#### JSON Schema for Learning Graphs

A formal specification defining the required structure and data types for learning graph JSON files.

**Example:** The schema requires "nodes" and "edges" arrays with specific properties like "id," "label," "from," and "to."

## L

#### Large Language Models Overview

An introduction to AI systems trained on vast text corpora to understand and generate human-like language.

**Example:** Claude, GPT, and other large language models can generate educational content from structured prompts.

#### Learning Graph

A directed graph of concepts showing prerequisite relationships that guide the optimal sequence for learning material.

**Example:** A learning graph for programming shows that "Variables" must be understood before "Functions," which precedes "Recursion."

#### Learning Graph Quality Score

A numeric assessment (1-100) evaluating graph structure quality based on connectivity, balance, and DAG validity.

**Example:** A score of 89 indicates excellent structure with balanced dependencies and no circular references.

#### Learning Outcomes

Specific, measurable statements describing what learners will be able to do after completing a course or module.

**Example:** "Students will be able to create a learning graph with 200 concepts and validate it has no circular dependencies."

#### Learning Pathways

Recommended sequences through course material that respect prerequisite dependencies and learner goals.

**Example:** A pathway for beginners starts with foundational concepts, while advanced learners might skip to intermediate concepts.

#### Level 1: Static Content

Textbooks containing only fixed text and images with no interactive or dynamic features.

**Example:** A PDF textbook or printed book represents Level 1 intelligence.

#### Level 2: Hyperlinked Navigation

Textbooks with clickable links enabling non-linear exploration and cross-referencing between sections.

**Example:** MkDocs-generated websites provide Level 2 intelligence with navigation menus and internal links.

#### Level 3: Interactive Elements

Textbooks incorporating user-controlled components like simulations, quizzes, and dynamic visualizations.

**Example:** Adding p5.js MicroSims and self-grading quizzes elevates a textbook to Level 3.

#### Level 4: Adaptive Content

Textbooks that adjust material presentation based on learner performance, preferences, or knowledge gaps.

**Example:** A Level 4 textbook recommends review material when quiz scores indicate weak understanding of prerequisites.

#### Level 5: AI Personalization

Textbooks using artificial intelligence to create customized learning experiences for individual learners.

**Example:** A Level 5 textbook generates practice problems tailored to each student's specific misconceptions.

#### License Metadata Field

Dublin Core element specifying usage rights, restrictions, and permissions for a resource.

**Example:** The license field might indicate "CC-BY-4.0" for Creative Commons Attribution license.

#### Linear Chain Detection

Identifying sequences in a learning graph where concepts form a single dependency line without branching.

**Example:** A linear chain like "A→B→C→D" lacks the richness of interconnected prerequisite relationships.

#### Listing Available Skills

The process of displaying all Claude skills accessible in the current project or globally.

**Example:** Running `/skills` or `./scripts/list-skills.sh` shows all skills with their descriptions.

## M

#### main.html in MicroSims

The standalone HTML file containing complete p5.js simulation code that can run independently in a browser.

**Example:** `/docs/sims/sorting/main.html` contains the full bubble sort visualization with embedded JavaScript.

#### Main Topics Covered

A comprehensive list of subject areas and themes included within a course's scope.

**Example:** Main topics include Claude Skills architecture, learning graphs, MkDocs, and Bloom's Taxonomy application.

#### Markdown Formatting Basics

Fundamental syntax for creating formatted text documents using plain text with special character conventions.

**Example:** Use `#` for headers, `**text**` for bold, `*text*` for italic, and `-` for bullet lists.

#### Maximum Character Length

The constraint that concept labels should not exceed 32 characters to ensure readability in visualizations and tables.

**Example:** "Directed Acyclic Graph (DAG)" is exactly 29 characters, fitting the maximum length requirement.

#### Maximum Dependency Chain Length

The longest path through prerequisite relationships from a foundational concept to a terminal concept.

**Example:** A chain length of 15 means some concepts require understanding 14 prerequisite concepts in sequence.

#### Metadata Section in JSON

The top-level object in vis-network JSON containing Dublin Core fields describing the learning graph resource.

**Example:** Metadata includes title, creator, description, date, version, format, and license information.

#### MicroSim

A focused, interactive p5.js simulation demonstrating a single educational concept through visual manipulation and observation.

**Example:** A binary search MicroSim shows how the algorithm eliminates half the search space with each comparison.

#### MicroSim Directory Structure

The standardized organization of files within a simulation folder: `main.html`, `index.md`, and `metadata.json`.

**Example:** `/docs/sims/bubble-sort/` contains these three files for the bubble sort visualization.

#### MicroSim Metadata

Dublin Core fields stored in `metadata.json` describing a simulation's title, creator, description, and educational purpose.

**Example:** Metadata records the concept being taught, target audience, and date created.

#### MicroSim Metadata Standards

The Dublin Core specification requirements for documenting simulations including required fields (title, creator, date) and recommended fields (description, version, license).

**Example:** MicroSim Metadata Standards ensure all simulations include consistent documentation for discovery, attribution, and educational context.

#### MkDocs

A static site generator that creates documentation websites from markdown files, designed for project documentation.

**Example:** Running `mkdocs build` converts markdown files in `/docs` into HTML pages with navigation.

#### MkDocs Configuration File

The `mkdocs.yml` file defining site settings, theme, navigation structure, and plugin configurations.

**Example:** The configuration file specifies the Material theme, navigation menu, and site name.

#### MkDocs Material Theme

A popular responsive theme for MkDocs providing modern design, search, and extensive customization options.

**Example:** Material theme enables features like tabs, admonitions, code highlighting, and dark mode.

#### Multiple-Choice Questions

Quiz items presenting a question with several answer options where learners select the correct response.

**Example:** "Which command stages files for commit? A) git push B) git add C) git status D) git clone"

## N

#### Navigation Structure in MkDocs

The hierarchical menu organization defined in `mkdocs.yml` that controls how pages appear in site navigation.

**Example:** The nav section defines chapters, subsections, and page ordering in the left sidebar menu.

#### Nodes Section in JSON

The array in vis-network JSON format containing objects representing individual concepts with id, label, and group properties.

**Example:** `{"id": 5, "label": "Claude Code Interface", "group": "FOUND"}` defines one concept node.

#### Non-Circular Definitions

ISO 11179 principle requiring definitions avoid referencing the term being defined or creating circular chains.

**Example:** Don't define "Learning Graph" using "graph for learning"; instead describe its structure and purpose.

## O

#### Optimizing Claude Usage

Strategies for maximizing productivity within Claude's token limits and usage windows through efficient prompting and batching.

**Example:** Generate multiple chapters in one session rather than invoking skills separately for each chapter.

#### Orphaned Nodes

Concepts in a learning graph that no other concepts depend on, suggesting they may be too specific or misplaced.

**Example:** If concept 150 has no concepts listing it as a prerequisite, it's orphaned and may need reevaluation.

#### Outdegree Analysis

Examining how many other concepts depend on each concept as a prerequisite in a learning graph.

**Example:** High outdegree indicates fundamental concepts that enable understanding of many subsequent topics.

## P

#### p5.js JavaScript Library

An open-source JavaScript library for creating interactive graphics and animations, especially suited for educational visualizations.

**Example:** p5.js provides simple functions like `circle()` and `line()` for drawing, plus `setup()` and `draw()` for animation loops.

#### Permission Management

The system for controlling access rights to files, directories, and commands in operating systems.

**Example:** Skills require read permissions on course files and write permissions on output directories.

#### pip Package Management

Python's standard tool for installing, upgrading, and managing third-party libraries and dependencies.

**Example:** `pip install mkdocs` downloads and installs MkDocs and its dependencies.

#### Pipe-Delimited Dependencies

A format for recording multiple prerequisite concept IDs separated by vertical bar characters in CSV files.

**Example:** The Dependencies field "1|5|12" indicates concepts 1, 5, and 12 are all prerequisites.

#### Practice Exercises

Learning activities where students apply concepts to solve problems, reinforcing understanding through active practice.

**Example:** After learning about skills, students practice creating a custom skill for their own use case.

#### Precise Definitions

ISO 11179 principle requiring glossary entries accurately capture specific meanings without ambiguity.

**Example:** Define "DAG" as "directed acyclic graph" with structural properties, not vaguely as "a type of graph."

#### Prerequisite Concepts

Ideas that must be understood before a learner can successfully grasp dependent advanced concepts.

**Example:** "Variables" is a prerequisite concept for understanding "Functions" in programming.

#### Prerequisite Relationships

Dependency connections indicating that understanding one concept requires prior mastery of other specific concepts.

**Example:** The relationship between "Git" and "Git Add Command" shows the general concept must precede the specific command.

#### Project-Specific Skills

Claude skills installed in a project's `.claude/skills/` directory, available only within that project.

**Example:** A custom textbook-generation skill stored locally serves project-specific needs without global installation.

#### Prompt Design Principles

Guidelines for creating effective AI instructions including clarity, specificity, context provision, and example usage.

**Example:** Good prompts specify output format, provide context, include examples, and define success criteria.

#### Prompt Engineering

The practice of crafting precise instructions to AI systems to elicit desired outputs and behaviors.

**Example:** Prompt engineering transforms "write about graphs" into "generate 200 atomic concepts with dependencies for graph theory."

#### Python

A high-level programming language widely used for scripting, data processing, and automation tasks.

**Example:** Python scripts like `analyze-graph.py` process learning graph data and generate quality reports.

#### Python Scripts for Processing

Automated programs written in Python to transform, analyze, or validate data in the textbook creation workflow.

**Example:** Scripts convert CSV to JSON, add taxonomy categories, and analyze graph structure.

#### Python Scripts in Skills

Supporting Python programs included in skill directories that perform specific data processing tasks.

**Example:** The learning-graph-generator skill includes four Python scripts for validation and transformation.

## Q

#### Quality Metrics for Graphs

Quantitative measures used to assess learning graph structure, including connectivity, balance, and DAG validity.

**Example:** Quality metrics include average dependencies, chain length, orphaned nodes, and category distribution percentages.

#### Quiz

A set of questions designed to assess learner understanding of concepts, typically with immediate feedback.

**Example:** Chapter quizzes contain 10-15 multiple-choice questions distributed across Bloom's Taxonomy levels.

#### Quiz Alignment with Concepts

The practice of ensuring each quiz question specifically tests understanding of identified learning graph concepts.

**Example:** Question 5 tests concept 42 ("Directed Acyclic Graph") by asking students to identify invalid graph structures.

#### Quiz Distribution Across Levels

Spreading quiz questions proportionally across all six Bloom's Taxonomy cognitive levels for comprehensive assessment.

**Example:** A balanced quiz has 15% Remember, 20% Understand, 20% Apply, 20% Analyze, 15% Evaluate, 10% Create questions.

## R

#### Reading Level Appropriateness

Ensuring textbook language complexity matches the target audience's comprehension abilities.

**Example:** Professional development content uses more technical vocabulary than high school materials.

#### Reading Level Categories

Standard classifications of target audiences based on educational development stage: junior-high, senior-high, college, and graduate levels.

**Example:** Reading Level Categories determine vocabulary complexity, sentence structure, and conceptual depth for generated textbook content.

#### Reference Documentation in Skills

Supporting files in skill directories providing examples, specifications, or guidance for skill execution.

**Example:** The learning-graph-generator includes sample CSVs and JSON schemas as reference documentation.

#### Remember (Cognitive Level 1)

The first level of Bloom's Taxonomy where learners retrieve, recognize, and recall relevant knowledge from memory.

**Example:** Students remember the six levels of Bloom's Taxonomy: Remember, Understand, Apply, Analyze, Evaluate, Create.

## S

#### Script Execution Permissions

File system settings that determine whether a script file can be run as a program.

**Example:** `chmod +x script.sh` grants execution permission, allowing `./script.sh` to run.

#### Section Organization

The structure of how content within chapters is divided into logical subsections with clear headings.

**Example:** Sections might include Introduction, Core Concepts, Examples, Practice Exercises, and Summary.

#### Scroll Hijacking

A usability problem where an embedded interactive element (such as an iframe, map, or canvas) captures mouse-wheel or touch-scroll input, preventing normal page scrolling.

**Example:** To prevent iframe scroll hijacking in chapter pages, set the iframe to non-scrolling and disable wheel zoom inside the MicroSim:
```html
<iframe src="../../sims/example/main.html" width="100%" height="500px" scrolling="no"></iframe>
```
```javascript
// Inside the MicroSim (e.g., Leaflet)
L.map('map', { scrollWheelZoom: false });
```

#### Security in Skill Execution

Safeguards ensuring skills only access authorized files and don't perform unintended or harmful operations.

**Example:** Skills should validate input file existence before processing to prevent unintended file creation.

#### Seeded Randomness

Using a fixed starting value for random number generation to produce reproducible results across simulation runs.

**Example:** `randomSeed(42)` in p5.js ensures the same "random" pattern appears each time for consistent demonstrations.

#### Self-Dependency Checking

Validation that no concept lists itself as its own prerequisite in a learning graph.

**Example:** The analyze-graph.py script reports an error if concept 25 includes 25 in its Dependencies field.

#### Shell Scripts

Text files containing sequences of command-line instructions that can be executed as automated programs.

**Example:** `install-claude-skills.sh` is a shell script that creates multiple symlinks with one command.

#### Skill Definition File Structure

The required format for SKILL.md files including YAML frontmatter followed by markdown workflow instructions.

**Example:** Frontmatter specifies name, description, and license; content describes step-by-step execution workflow.

#### Skill Directory Structure

The standardized organization of a skill folder containing SKILL.md, supporting scripts, templates, and reference files.

**Example:** `learning-graph-generator/` contains SKILL.md plus four Python scripts for graph processing.

#### Skill Distribution Methods

Approaches for sharing Claude skills including global installation, project-specific placement, or package repositories.

**Example:** Distribution methods include symlinks to global directory, copying to project folders, or Git repositories.

#### Skill Execution Context

The environment information available when a skill runs, including working directory, available files, and user permissions.

**Example:** Skills execute from the project root directory with access to files the user can read or write.

#### Skill License Information

The legal terms specifying how a skill can be used, modified, and distributed by others.

**Example:** Most skills use Apache-2.0 license allowing free use with attribution.

#### Skill Name and Description

The identifying label and brief summary in YAML frontmatter explaining what a skill does.

**Example:** `name: glossary-generator` and `description: Generate ISO 11179-compliant glossaries from concept lists`.

#### Skill Packaging Best Practices

Guidelines for organizing, documenting, and distributing skills to ensure usability and maintainability.

**Example:** Include README files, example inputs/outputs, clear dependencies, and comprehensive skill documentation.

#### Skill Testing and Debugging

The process of validating skill functionality, identifying errors, and iteratively improving skill reliability.

**Example:** Test skills with missing input files, malformed data, and edge cases to ensure robust error handling.

#### Skill Workflow Instructions

Detailed step-by-step procedures in SKILL.md that guide Claude through executing the skill's tasks.

**Example:** Workflow instructions specify "Step 1: Read concept list. Step 2: Validate quality. Step 3: Generate definitions."

#### Supporting Assets in Skills

Additional files in skill directories that assist execution, including scripts, templates, examples, and schemas.

**Example:** Supporting assets might include Python scripts, sample CSVs, JSON schemas, or reference documentation.

#### Symlink Creation

Making symbolic links that reference files in other locations, allowing access from multiple paths without duplication.

**Example:** `ln -s ~/claude-skills/skills ~/.claude/skills` creates a symlink for global skill access.

## T

#### Target Audience Definition

A clear specification of who the course is designed for, including their background and learning goals.

**Example:** "Professional development for educators with basic programming skills who want to create AI-assisted textbooks."

#### Taxonomy

A hierarchical classification system organizing concepts into categories based on shared characteristics or difficulty levels.

**Example:** Concepts are categorized as FOUND (foundational), BASIC, INTER (intermediate), ADVAN (advanced), or INTEG (integration).

#### Taxonomy Categories

Distinct groupings within a taxonomy system used to organize concepts by type, difficulty, or subject area.

**Example:** Common categories include foundational, basic, intermediate, advanced, and integration concepts.

#### taxonomy-distribution.py Script

A Python program that analyzes and reports the distribution of concepts across taxonomy categories.

**Example:** Running this script produces a report showing 15% foundational, 40% basic, 30% intermediate, 15% advanced concepts.

#### TaxonomyID Abbreviations

Short alphanumeric codes representing concept categories in learning graphs, typically 3-5 characters.

**Example:** FOUND for foundational, BASIC for basic concepts, ADVAN for advanced concepts.

#### TaxonomyID Field in CSV

A column in learning graph CSV files containing category abbreviations for each concept.

**Example:** The TaxonomyID field might contain "FOUND" for concept 1 and "ADVAN" for concept 200.

#### Template Files in Skills

Reusable file structures that skills populate with generated content to ensure consistent formatting.

**Example:** A chapter template defines standard sections: Introduction, Concepts, Examples, Exercises, Summary.

#### Terminal Commands

Text-based instructions entered in a command-line interface to execute programs, manage files, or configure systems.

**Example:** Terminal commands include `cd`, `ls`, `mkdir`, `python`, and `git` for various operations.

#### Terminal in VS Code

An integrated command-line interface within Visual Studio Code for running commands without leaving the editor.

**Example:** Open the VS Code terminal with Ctrl+` to run `mkdocs serve` while editing content.

#### The Role of FAQs in Intelligent Textbooks

The function of Frequently Asked Questions as supplementary resources providing quick answers to common learner queries and clarifying potentially confusing concepts.

**Example:** FAQs bridge gaps between formal content and student questions, offering conversational explanations that complement technical definitions in the glossary.

#### Title Case Convention

Capitalization style where the first letter of each major word is uppercase, used for concept labels.

**Example:** "Learning Graph Generator" follows Title Case, while "learning graph generator" does not.

#### Title Metadata Field

Dublin Core element providing the formal name or title of a resource.

**Example:** The title field might contain "Learning Graph for Claude Skills Course."

#### Token Management Strategies

Techniques for working within Claude's token limits including content chunking, selective context, and multi-turn workflows.

**Example:** Generate one chapter at a time rather than requesting all chapters in a single prompt.

#### Topics Excluded from Course

Subjects explicitly identified as out of scope to clarify course boundaries and manage learner expectations.

**Example:** This course excludes advanced machine learning theory and general web development beyond MkDocs.

## U

#### Understand (Cognitive Level 2)

The second level of Bloom's Taxonomy where learners construct meaning from instructional messages and explanations.

**Example:** Students understand how learning graphs guide concept sequencing by explaining prerequisite relationships.

## V

#### Version Control Basics

Fundamental concepts of tracking changes to files over time, including commits, branches, and repositories.

**Example:** Version control lets you see who changed what, when, and why, plus revert to earlier versions if needed.

#### Version Metadata Field

Dublin Core element recording the iteration or release number of a resource.

**Example:** The version field tracks "1.0" for initial release or "2.3" after multiple revisions.

#### vis-network JSON Format

A specific JSON structure used by the vis-network visualization library containing nodes, edges, groups, and metadata.

**Example:** The format requires separate arrays for nodes (with id, label, group) and edges (with from, to).

#### Visual Studio Code

A popular open-source code editor with integrated terminal, Git support, and extensions for various development tasks.

**Example:** VS Code provides markdown preview, making it ideal for writing and editing textbook content.

#### VS Code for Content Development

Using Visual Studio Code's features specifically for creating and managing educational textbook content.

**Example:** VS Code extensions for markdown linting, spell-checking, and MkDocs preview enhance content development.

## W

#### Worked Examples in Content

Step-by-step demonstrations showing how to solve problems or apply concepts with detailed explanations.

**Example:** A worked example shows creating a 10-concept learning graph from scratch, explaining each dependency decision.

## Y

#### YAML Frontmatter in Skills

Metadata section at the beginning of SKILL.md files enclosed in `---` delimiters containing key-value pairs.

**Example:** Frontmatter includes `name: glossary-generator`, `description: Generate glossaries`, and `license: Apache-2.0`.
