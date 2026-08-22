# Glossary of Terms

This glossary defines every concept in the
[learning graph](./learning-graph/concept-list.md) for this course. Definitions
follow the ISO 11179 metadata registry criteria: each one is precise, concise,
distinct from related terms, non-circular, and free of procedural rules.

Terms are listed in alphabetical order.

#### About Page

A page describing a book's purpose, its author, and how to cite it.

#### Accessible Color Schemes

Color selections that remain distinguishable to readers with color vision differences and maintain sufficient contrast.

**Example:** A diagram distinguishes categories by shape as well as color, so it stays readable to someone with red-green color blindness.

#### Action Verbs for Outcomes

The observable verbs that make an outcome measurable, chosen to match the intended cognitive category.

**Example:** "Compare two routing strategies" is testable; "appreciate routing" is not.

#### add-iframes-to-chapter.py

The program that inserts embedding markup for generated simulations into the chapter that requested them.

**Example:** One run inserts twelve embedding blocks that would otherwise be pasted by hand.

#### add-taxonomy.py Script

The program that assigns category abbreviations to rows of a dependency file.

**Example:** It assigns the graph category to every row whose label concerns dependency structure.

#### Admonition Blocks

Set-apart callout boxes that highlight notes, warnings, tips, or questions distinctly from body text.

**Example:** A warning box draws attention to a mistake readers commonly make at that point.

#### Agent Skill

A packaged set of instructions and supporting files that teaches an AI agent to perform a specific task consistently.

**Example:** A skill that generates glossaries carries the definition standards, the output format, and the assembly script it needs.

#### Agent Skills Open Standard

The published specification defining what a skill folder must contain and which metadata fields conforming clients recognize.

**Example:** A folder written against the standard loads unchanged in Codex and Cursor.

#### Agentic Workflow

A sequence of model-driven steps in which each step's output informs the next, with the model choosing actions rather than following a fixed script.

**Example:** The agent reads a validator's error output and decides which file to open next.

#### AGENTS.md Convention

The practice of placing project instructions in a commonly recognized filename so multiple agent platforms read the same guidance.

**Example:** Copying the project rules to a second recognized filename lets another platform read them.

#### AI Coding Agent

A program that combines a language model with the ability to read files, run commands, and edit a project, so it can carry out multi-step development tasks.

**Example:** Claude Code reads a chapter file, writes a simulation, runs a validator, and fixes what the validator reports.

#### Allowed Tools Field

An optional list of pre-approved actions a skill may take without further prompting. Its behavior varies between agent platforms.

**Example:** A read-only reporting skill may list only file reading and searching.

#### Ambiguous Term Clarification

Resolving request words that could indicate several visualization types before generation begins.

**Example:** "Map" may mean a geographic display or a relationship diagram, and the difference must be settled first.

#### Analyze Level

The cognitive category covering breaking material into parts and determining how they relate, expressed by actions such as differentiating and comparing.

**Example:** "Compare two routing strategies and explain when each fails."

#### analyze-graph.py Script

The program that examines a dependency file and reports structural measurements including loops, entry points, endpoints, and connectivity.

**Example:** It reports that a structure has 570 ideas, six entry points, and no closed paths.

#### analyze-reading-levels.py

The program that measures textual difficulty per chapter and reports variation across a book.

**Example:** It flags one chapter written three grade levels above the rest.

#### analyze-skills.py Script

The program that processes recorded usage events and reports duration and consumption per skill.

**Example:** It shows that simulation generation consumed more than all other skills combined.

#### Animated Current Flow

A moving visual indication of charge travelling through a circuit, making an invisible process observable.

**Example:** Moving dots along a wire stop when a switch opens, showing directly why a lamp goes dark.

#### Annotation-Free Illustration

A generated picture produced deliberately without text, arrows, or labels, so an interactive layer can supply them.

**Example:** A cell diagram is produced with no printed labels so markers can be placed afterward.

#### Announcement Preview Image

The picture accompanying a shared announcement, cropped to the proportions a platform displays.

**Example:** A cover picture cropped to a wide ratio so it displays fully in a feed.

#### Answer Distribution Balance

Spreading correct answers evenly across the available positions so position alone gives no advantage.

**Example:** If every correct answer were the third option, readers could score well without reading the questions.

#### AP Style Writing

A journalistic convention governing capitalization, numbers, titles, and attribution in press material.

**Example:** Numbers below ten are spelled out, and titles are capitalized only before a name.

#### Apply Level

The cognitive category covering use of a procedure in a given situation, expressed by actions such as implementing, solving, and using.

**Example:** "Use the dependency file to produce a viewer-ready graph."

#### Archived Skill

An original standalone skill retained for reference after its content was folded into a meta-skill. Archived skills are not loaded.

**Example:** The original timeline generator stays readable after its content moved into the simulation router.

#### Artificial Intelligence

The field of building computer systems that perform tasks normally requiring human cognition, such as recognizing language, generating text, or making decisions under uncertainty.

**Example:** An agent that reads a course description and proposes a list of concepts to teach is applying artificial intelligence to instructional design.

#### Assessing Student Understanding

Determining what a learner has actually grasped, through questions and activities aligned to stated outcomes.

**Example:** A question asking a reader to predict an outcome reveals more than one asking for a definition.

#### Assets Directory

The folder holding templates, schemas, and images that a skill copies or reads when producing output.

**Example:** A starter configuration copied into every new book lives here.

#### Asymmetric Content Handling

Allowing a comparison layout to show unequal amounts of material on each side, so missing evidence is displayed honestly rather than filled with invention.

**Example:** If only one side has published measurements, the other side is left empty rather than given plausible numbers.

#### Atomic Concept

A teachable idea that cannot be usefully divided further without losing meaning, making it a suitable single node.

**Example:** "Cycle Detection" is atomic; "Graph Theory" is not.

#### Audio Streaming Playback

Delivering generated sound so it begins playing before the whole file has downloaded.

**Example:** A long narration begins within a second instead of after a full download.

#### Audit Trail Preservation

Retaining the evidence chain behind published material so any figure can be traced back to where it came from.

**Example:** A reader questioning a figure can follow it to the quoted sentence in the cited study.

#### Auto-Commit Hook

A configured callback that records a turn's file changes automatically using a message left for it, so work is never left uncommitted.

**Example:** The agent leaves a message file during its turn, and the hook commits and pushes when the turn ends.

#### Automated Work Item Filing

Recording each identified shortfall as a tracked task at the moment it is found, rather than relying on memory.

**Example:** A lab missing a parts list generates a tracked task naming the skill that can supply one.

#### Average Dependencies

The mean number of prerequisites per idea, used as a health measure. Values that are too low suggest missing relationships.

**Example:** A value near one suggests a chain rather than a network.

#### Baked-In Text Problem

The condition in which wording is permanently fixed into pixels, so any error requires regenerating the whole picture and cannot be audited by a reader.

**Example:** Correcting a single misspelled label requires regenerating the entire picture.

#### Balancing Loop

A closed path of influence that counteracts change, driving a system toward a stable value.

**Example:** Rising prices reduce demand, which lowers prices again.

#### Batch Screenshot Capture

Generating preview images for many simulations in one automated pass.

**Example:** Twelve preview images are produced in one run instead of twelve manual captures.

#### Batch Script Substitution

Replacing repetitive generated output with a program that produces the same result, so the model performs only the creative portion.

**Example:** A script scaffolds directories, stub files, and metadata for twelve simulations, leaving only the logic file to be written.

#### Batch Sim Generation

Producing all simulations requested by a chapter in one coordinated pass rather than individually.

**Example:** Every simulation a chapter requests is scaffolded, written, and validated together.

#### Batch Utility Token Savings

The reduction in consumption achieved by having programs perform the repetitive parts of simulation production instead of the model.

**Example:** Automating parsing, scaffolding, embedding, and validation saves roughly four hundred thousand tokens across one chapter's simulations.

#### bk Command Family

The set of installed command-line utilities, each prefixed for recognition, that perform book maintenance tasks such as capturing screenshots or generating metrics.

**Example:** One command captures a simulation screenshot; another regenerates the metrics file the publishing routes depend on.

#### bk-install-skills Script

The utility that creates the links from the skill repository into the agent's skills directory and removes links whose targets no longer exist.

**Example:** Running it after adding a skill makes that skill available in every project.

#### Blank Line Before Lists

A markdown authoring rule requiring an empty line between a paragraph and a following list so the list renders correctly.

**Example:** Without the blank line, the list renders as one run-on paragraph.

#### Bloom Level to Interaction

The principle of matching interaction style to intended cognitive demand, so an activity exercises the level it claims to.

**Example:** Understanding is served by stepping through a worked example; creating is served by a builder tool.

#### Bloom's 1956 Original

The initial version of the cognitive objective classification, whose top categories were synthesis and evaluation.

**Example:** Its categories were nouns, where the revision uses verbs.

#### Bloom's 2001 Revision

The updated classification that restates categories as verbs and places creation at the highest level. This revision is the one used throughout this workflow.

**Example:** Creating replaced synthesis as the most demanding category.

#### Bloom's Taxonomy

A classification of educational objectives arranged by cognitive demand, used to ensure material addresses more than factual recall.

**Example:** A chapter that only asks readers to define terms addresses one level and neglects the rest.

#### Body Loading Budget

The cost of reading a skill's full instruction file once that skill is triggered.

**Example:** A one-page router costs far less to load than a thirty-page guide.

#### Book Chapter Generator

The skill that designs a chapter outline from a dependency structure, assigning ideas to chapters in an order that respects prerequisites.

**Example:** It groups related ideas into a chapter and places prerequisite chapters first.

#### Book Completion Workflow

The coordinated final pass that generates all remaining supporting material and reports before a book is released.

**Example:** One run produces the glossary, questions, assessments, references, and metrics together.

#### Book Installer Skill

The meta-skill that scaffolds a new book and installs individual site features on request.

**Example:** A request for math support routes to the guide that configures equation rendering.

#### Book Launch Checklist

The list of confirmations completed before announcing a book, covering build, deployment, metrics, and links.

**Example:** Confirming the site builds, deploys, and shows current statistics before posting an announcement.

#### Book Metrics

Quantitative measurements describing a finished book, such as its word count, illustration count, and equivalent page count.

**Example:** A book reports 120,000 words across 40 chapters, roughly 480 printed pages.

#### Book Publisher Skill

The meta-skill that produces repository summaries, announcement posts, slideshows, and press releases from a book's recorded measurements.

**Example:** The same recorded figures feed the repository summary and the public announcement.

#### Book Status Report

A generated overview of how complete a book is and which stages of its production remain.

**Example:** It reports that chapters exist but assessments do not.

#### book-metrics.json Hub

The generated file holding a book's measurements in structured form, serving as the single source every publishing route reads.

**Example:** A repository summary and a press release both read this file, so their figures always agree.

#### book-metrics.py Script

The program that measures a book's content and writes the structured measurement file.

**Example:** It counts words, illustrations, and formulas across every chapter in one pass.

#### Breadboard Tie Points

The individual holes on a prototyping board, internally connected in rows and columns that determine which parts share a connection.

**Example:** Five holes in a row share one connection, so two parts placed in that row are joined.

#### Bubble Chart Matrix

A plot positioning items on two axes with size encoding a third value, used for priority and trade-off comparisons.

**Example:** Features plotted by effort and impact, sized by estimated cost.

#### Budget-Constrained Authoring

Planning a book's production to fit a fixed monthly allowance, choosing techniques by cost as well as quality.

**Example:** Choosing one-agent generation so a full book fits inside a monthly allowance.

#### Button Control

A clickable interface element that triggers a discrete action such as resetting or starting a simulation.

**Example:** A reset control returns a simulation to its starting state.

#### Cached Quality Score

A previously computed assessment stored with a document so later runs can read it instead of recomputing it.

**Example:** A score of 95 stored in a page's metadata lets a later run skip re-scoring.

#### calculate-quality-score.py

The program that computes a numeric rating for a simulation from measurable properties.

**Example:** It rates a simulation on file separation, metadata completeness, and control conventions.

#### Callout Marker Coordinates

The stored positions identifying where each marker sits on an illustration, kept in data so they can be adjusted without editing code.

**Example:** Moving a marker two pixels is a data edit, not an image regeneration.

#### Callout Overlay Engine

The code layer that draws numbered point markers on specific features of an illustration and connects them to descriptive labels.

**Example:** Numbered circles appear over specific structures in an anatomical illustration.

#### Canonical Metrics Principle

The rule that all published figures derive from one generated measurement file, so different announcements never disagree.

**Example:** A repository summary and a public announcement quote the same page count because both read the same file.

#### Canvas Container Sizing

Measuring the available width of a surrounding element and sizing the drawing surface to match, so a simulation fits its frame.

**Example:** A simulation measures its frame width at startup so it fills the space available.

#### CANVAS_HEIGHT Directive

A recorded height value inside a simulation's source that serves as the single authority for how tall its embedding frame should be.

**Example:** A recorded value of 695 tells every embedding frame how tall to be.

#### Capstone Project

A culminating assignment requiring learners to combine most of a course's material into one substantial piece of work.

**Example:** Building a complete textbook from a course description, end to end.

#### Capstone Textbook Project

A culminating exercise in which a learner produces a complete intelligent textbook, applying the entire pipeline end to end.

**Example:** A learner produces a structure, chapters, simulations, and a deployed site for a subject of their choice.

#### Carousel Slide Patterns

The recurring panel layouts used in a slideshow post, such as a title panel, a statistics panel, and a closing call to action.

**Example:** An opening title panel, three statistic panels, and a closing link panel.

#### Category Over-Representation

The condition in which one category holds a disproportionate share of all ideas, suggesting it should be subdivided.

**Example:** A category holding more than thirty percent of ideas is treated as too broad.

#### Causal Loop Diagram

A systems-thinking illustration showing how variables influence one another around closed paths of cause and effect.

**Example:** Arrows show how workload, fatigue, and error rate influence one another.

#### Celebration Animation

A brief visual effect acknowledging completion of an activity, used to mark progress.

**Example:** A brief effect appears when a reader finishes a sorting activity.

#### Chapter Concept Assignment

Allocating each teachable idea to the single chapter responsible for introducing it.

**Example:** "Cycle Detection" is assigned to the graph quality chapter, not the introduction.

#### Chapter Concept List

The enumerated ideas a specific chapter is responsible for introducing.

#### Chapter Content Generator

The skill that expands a chapter outline into full instructional text with examples, diagrams, and exercises at appropriate cognitive levels.

**Example:** It expands a title, summary, and idea list into full prose with examples and exercises.

#### Chapter Image Placement

Deciding where illustrations appear within a chapter so they support the surrounding explanation.

**Example:** An illustration appears immediately after the paragraph describing it.

#### Chapter Index File

The main markdown file for a chapter, holding its title, summary, assigned ideas, and eventually its full text.

**Example:** The file holding a chapter's title, summary, assigned ideas, and body text.

#### Chapter Metrics

Per-chapter measurements such as word count, illustration count, and equation count, used to detect uneven coverage.

**Example:** One chapter has 800 words while its neighbors have 3,000, revealing uneven depth.

#### Chapter Metrics Report

A generated table of measurements per chapter, used to identify uneven depth across a book.

**Example:** A table showing word count and illustration count for each of forty chapters.

#### Chapter Navigation Entry

The site menu item pointing to a chapter, which must be declared explicitly for the page to be reachable.

**Example:** A page absent from the menu is unreachable even though it built successfully.

#### Chapter Reading Level Audit

Measuring textual difficulty across chapters and flagging those that diverge from the declared target.

**Example:** A chapter measuring four grades above target is flagged for simplification.

#### Chapter Review Workflow

The author-led inspection of generated chapter material before dependent artifacts such as quizzes and simulations are produced.

**Example:** An author corrects a chapter before its assessments are generated from it.

#### Chapter Structure Design

Determining how many chapters a book needs and which material belongs in each, guided by the ordering relationships between ideas.

**Example:** Forty ideas become five chapters, ordered so nothing precedes its prerequisites.

#### Chapter Summary

A brief statement of what a chapter covers, used for navigation, previews, and generation context.

#### Chapter Token Budgeting

Allocating a per-chapter allowance for generation so a long book completes without exhausting a period's capacity.

**Example:** Allocating a fixed allowance per chapter so a long book completes across sessions.

#### Chart.js Library

A JavaScript charting library producing bar, line, pie, radar, and related plots from structured values.

**Example:** A bar chart comparing consumption across four generation strategies.

#### Chat Versus Agent Interfaces

The distinction between a conversational interface that only returns text and an agent interface that can also act on files and run commands.

**Example:** A chat window can describe how to fix an iframe height; an agent can open the file and fix it.

#### Chatbot Training JSON

A structured export of question-and-answer pairs formatted for consumption by a conversational retrieval system.

**Example:** An exported question set lets a course assistant answer from the book itself.

#### check-loops.py Script

The program that searches a dependency file specifically for closed paths and reports the identifiers involved in each.

**Example:** It reports that ideas 12, 40, and 55 form a closed path.

#### Checkbox Control

An interface element toggling a setting between two states, used for optional display features.

**Example:** A toggle that shows or hides velocity arrows in a physics simulation.

#### Circuit Schematic Generation

Producing a standard electrical diagram from a description, as a maintainable program plus a rendered picture.

**Example:** A description of a resistor and lamp in series becomes a standard diagram.

#### Claim Planning Phase

The initial stage listing every factual assertion a planned poster will make, before any source is consulted.

**Example:** Listing eight intended figures before searching for any source.

#### Claim Verification Report

The record showing each planned assertion, its supporting quotation, and whether it passed, was softened, or was removed.

**Example:** Two claims pass with quotations, one is softened to qualitative wording, and one is dropped.

#### Claude Code Interface

The command-line environment in which Claude reads a project, runs tools, and applies edits under the user's permission settings.

**Example:** An author asks for a chapter's simulations and watches the files appear in the project.

#### Claude Command

A named, reusable instruction file invoked directly by the user, typically to run a fixed procedure rather than an open-ended task.

**Example:** Typing a command name runs a fixed procedure rather than describing a task.

#### Claude Max Plan Limits

The larger usage allowance of a higher-cost subscription tier.

#### Claude Pro Plan Limits

The usage allowance of the lower-cost subscription tier, which constrains how much generation can occur within a given period.

**Example:** An author on this tier plans generation to fit a smaller periodic allowance.

#### CLAUDE.md Project Memory

A project file holding standing instructions an agent reads at the start of every session, encoding conventions specific to that repository.

**Example:** A rule about where generated simulations must be placed applies without needing to be restated.

#### Clickable Matrix Table

A grid whose cells expand to reveal detailed explanation, used for framework comparisons too dense for a static table.

**Example:** Selecting a cell reveals a paragraph explaining that combination.

#### Code Syntax Highlighting

Coloring code samples by language structure so they are easier to read, usually with a copy control.

**Example:** Keywords, strings, and comments appear in distinct colors with a copy control.

#### Cognitive Level Distribution

The spread of material across the six cognitive categories, used to check that a course is not concentrated in recall alone.

**Example:** A course with thirty recall outcomes and two creation outcomes is unbalanced.

#### collect-site-metrics.py

The program that gathers statistics from a built site for use in summaries and announcements.

**Example:** It counts published pages and simulations from the built site.

#### color-config.json File

The stored assignment of a display color to each category, ensuring the same category keeps the same color across regenerations.

**Example:** Saving the assignment keeps one category the same color across every regeneration.

#### Command Definition File

The markdown file that declares a command's name and description and contains the steps it performs.

**Example:** The file declaring a runbook command's name, description, and steps.

#### Command-Line Arguments

Values supplied to a program when it is invoked, allowing one script to operate on different inputs.

**Example:** One validation script checks any dependency file named when it is run.

#### Comment System

An embedded discussion feature letting readers leave remarks on a page.

#### Comparison Table Sim

An interactive table presenting side-by-side attributes with rated values across several options.

**Example:** Four visualization libraries rated across five attributes side by side.

#### Compatibility Field

An optional metadata entry describing environment requirements such as needed packages or network access. It is advisory rather than enforced.

**Example:** A note that a skill needs network access to verify citations.

#### Component Placement

Positioning parts into specific holes so their connections match the intended circuit.

**Example:** A resistor spans the center channel so its two ends sit in separate rows.

#### compress-images.py Script

The program that reduces picture file sizes across a project to improve page load speed.

**Example:** It reduces a folder of cover art from twelve megabytes to two.

#### Concept

A single teachable idea in a course, small enough to be explained on its own and named with a short label.

**Example:** "Cycle Detection" is one teachable idea and occupies one node.

#### Concept Classifier Sim

An interactive sorting activity in which a reader assigns scenarios to categories and receives immediate feedback.

**Example:** A reader sorts described situations into reinforcing and balancing categories.

#### Concept Coverage Exactly Once

The rule that every enumerated idea is introduced in one chapter and only one, preventing both gaps and duplication.

**Example:** An idea introduced in two chapters wastes space and creates conflicting explanations.

#### Concept Enumeration

The process of deriving the full set of teachable ideas from a course description, before any ordering is assigned.

**Example:** A course description yielding 570 distinct teachable ideas.

#### Concept Granularity

The chosen level of detail at which ideas are separated, balancing a graph that is too coarse to guide sequencing against one too fine to read.

**Example:** Splitting "Git" into forty separate ideas would overwhelm a diagram.

#### Concept Label

The short name identifying a teachable idea, written in title case and constrained in length so it displays legibly in a network diagram.

**Example:** "Directed Acyclic Graph" fits a node box; a full sentence would not.

#### Concept List File

The numbered document listing every teachable idea with its identifier, produced for author review before dependencies are mapped.

**Example:** A numbered document an author edits before any dependency is assigned.

#### Concept List Review

Examining and editing the enumerated ideas before dependencies are assigned, since later changes propagate through every downstream artifact.

**Example:** Removing an unwanted idea at this stage costs nothing; removing it after chapters are written requires rewriting them.

#### Concept Search in Viewer

A control that locates a named idea within a rendered diagram and brings it into view.

#### Concept Taxonomy

A set of categories used to group teachable ideas by subject area, providing color coding and distribution analysis.

**Example:** Ideas about tokens, plans, and measurement group into one category.

#### ConceptID Field

The unique integer identifying each teachable idea, used to reference it from dependency lists and graph files.

**Example:** Idea 244 is referenced from every row that depends on it.

#### Concise Definition

A definition expressed in the fewest words that still convey the full meaning, typically twenty to fifty.

**Example:** "A repository that stores learner activity statements" says enough in nine words.

#### Content Element Types

The catalog of components a chapter may contain, such as prose, worked examples, diagrams, exercises, and callouts.

**Example:** A chapter may combine prose, a worked example, a diagram request, and five exercises.

#### Content Generation Guide

A project document defining voice, character conventions, and placement rules that generated text must follow.

**Example:** A project document specifying that the recurring character appears at most twice per chapter.

#### Content Quality Standards

The criteria generated text must meet, covering prerequisite respect, cognitive coverage, example count, and formatting.

**Example:** Every section must include two worked examples and five practice problems.

#### Context Compaction

Summarizing earlier parts of a long session so work can continue after the accumulated material would otherwise exceed capacity.

**Example:** A long session summarizes its earlier work so generation can continue.

#### Context Window

The maximum amount of text, measured in tokens, that a language model can consider at one time. Content beyond this limit is unavailable to the model.

**Example:** A book with 40 chapters cannot be placed in a single context window, so skills read only the chapter currently being generated.

#### Context Window Management

Deliberately controlling what enters a model's working memory so the relevant material fits and nothing is wasted.

**Example:** Reading one chapter rather than the whole book before generating that chapter's simulations.

#### Continuous Book Improvement

Using measurements, reader feedback, and usage data to revise a book and the skills that produced it after release.

**Example:** Feedback showing a chapter confuses readers prompts both a rewrite and a skill revision.

#### Core Versus Domain Skills

The distinction between subject-neutral skills usable by any book and specialized skills meaningful only within one field.

**Example:** A glossary generator serves any book; a breadboard generator serves one.

#### Cost Per Book Estimate

A projection of total consumption for a complete textbook, derived from measured per-stage costs.

**Example:** Measured stage costs project the total consumption of a forty-chapter book.

#### Course Description

A structured document stating what a course covers, who it is for, what is excluded, and what learners will be able to do afterward. It is the source input for concept enumeration.

**Example:** A document naming the audience, prerequisites, topics, exclusions, and outcomes of a course.

#### Course Description Analyzer

The skill that scores an existing course description against the rubric or drafts one that satisfies it.

**Example:** It scores a draft at 62 and lists which elements are missing.

#### Course Description Rubric

The point-allocated scoring guide that assesses whether a course description contains every element needed for downstream generation.

**Example:** Points are allocated to the title, audience, prerequisites, topics, exclusions, and each cognitive level.

#### Course Description Score

The numeric result of applying the rubric, used as a gate before concept enumeration begins.

**Example:** A score above the threshold allows the pipeline to proceed and lets later runs skip re-scoring.

#### Course Prerequisites

The knowledge and access a learner is assumed to have before starting, stated explicitly rather than implied.

**Example:** Stating that readers need basic programming and a hosting account.

#### Course Title

The name identifying a course, used as the book title and in generated metadata.

**Example:** "Using Agent Skills to Create Intelligent Textbooks."

#### Cover Image Generation

Producing the principal illustration representing a book, derived from the book's own subject matter.

**Example:** A picture derived from the book's own subject rather than a stock illustration.

#### Create Level

The cognitive category covering assembly of elements into a new coherent whole, expressed by actions such as designing and constructing.

**Example:** "Design and build a complete intelligent textbook for a subject of your choice."

#### Creative Commons Licensing

A family of standardized licenses that grant specified reuse rights while retaining copyright, commonly used for educational material and images.

**Example:** A CC BY-NC license permits classroom reuse with attribution but forbids commercial resale.

#### Crediting Pedagogical Authors

Naming the specific writers responsible for an influential explanation, analogy, or derivation, rather than citing only encyclopedic sources.

**Example:** A citation credits the author who introduced a now-standard teaching analogy for a difficult idea.

#### crop-screenshot.py Script

The program that trims a captured image to a required aspect ratio for use in posts and previews.

**Example:** It trims a captured page to the proportions a sharing platform displays.

#### Cross-Platform Skill Testing

Running the same skill on several agent platforms and comparing results to find behavior that depends on one vendor.

**Example:** A skill that works in one agent silently skips its image step in another.

#### CSV Parsing in Python

Reading delimited tabular text into structured records for processing.

**Example:** Reading a dependency file into records so each row can be validated.

#### csv-to-json.py Script

The program that converts a tabular dependency file into the viewer-ready format, generating the legend from category definitions.

**Example:** It turns a dependency spreadsheet into the file an interactive viewer renders.

#### Curated Reference List

A deliberately selected set of sources chosen for quality and relevance rather than assembled by bulk search.

**Example:** Ten sources chosen for a chapter rather than fifty returned by a search.

#### Cursor IDE

An editor with a built-in AI agent that can load and run skills alongside normal editing.

**Example:** An author edits chapters while an embedded agent generates their simulations.

#### Custom 404 Page

A replacement for the default missing-page message, offering navigation back into a book.

**Example:** A missing page offers links back to the table of contents.

#### Cycle Detection

Checking a directed structure for any closed loop, which would make a consistent teaching order impossible.

**Example:** If a closed path is reported, no valid teaching order exists.

#### data.json File

A file holding a simulation's underlying values separately from its code, so figures can be updated without touching logic.

**Example:** Updating a chart's figures without touching the code that draws it.

#### Define Before Display Rule

The authoring rule that a term must be explained before any diagram, table, or code sample relies on it.

**Example:** A parameter appearing in a code listing is described in prose before the listing appears.

#### Definitions Without Rules

A definition that describes what something is rather than prescribing how it must be used or who may use it.

**Example:** "A structure showing prerequisite relationships" rather than "learners must finish prerequisites first."

#### Dependency Chain Length

The number of steps in the longest path from an entry point to a final idea, indicating how deep the material runs.

**Example:** A longest path of twenty-six steps indicates substantial depth.

#### Dependency Edge

The arrow in a graph that represents a single ordering relationship between two ideas.

**Example:** An arrow from "Directed Acyclic Graph" to "Cycle Detection."

#### Dependency-Ordered Chapters

Sequencing chapters so no chapter relies on material introduced only in a later chapter.

**Example:** A chapter using dependency structure appears after the chapter introducing it.

#### Deployment Verification

Confirming that a published site renders correctly and that its links and assets resolve after release.

**Example:** Confirming that pictures load and internal links resolve on the published site.

#### Description Trigger Testing

Checking a skill description against sample requests to confirm it activates when it should and stays silent when it should not.

**Example:** Ten sample requests confirm the intended skill activates for each.

#### Descriptive Context

Supporting narrative in a course description explaining why the subject matters and how the material will be used.

**Example:** A paragraph explaining why an author would want to build a textbook this way.

#### Design Decision Record

A written account of why a particular approach was chosen over alternatives, preserved so the reasoning survives.

**Example:** Noting why serial generation was chosen over concurrent generation prevents the question being reopened later.

#### Details Disclosure Block

A collapsible region that hides supporting material until a reader expands it, keeping a page readable while retaining depth.

**Example:** A simulation's full specification is stored collapsed inside the chapter that requests it.

#### detect_features.py Script

The program that inspects a project and reports which site capabilities are installed.

**Example:** It reports that equation rendering is installed but the comment system is not.

#### Deterministic Computation

An operation that returns the same result for the same input every time, making it suitable for automated validation.

**Example:** Counting words in a chapter returns the same number every time.

#### Deterministic Work Offloading

Assigning every step with a single correct answer to a program, reserving the model for judgment and composition.

**Example:** Sorting a glossary is arithmetic, not judgment, so a program does it.

#### Diagram Coverage Report

A generated summary showing which requested visuals exist, which are missing, and which chapters lack illustration.

**Example:** One chapter requested five visuals and has three.

#### Diagram Specification Block

A structured description of a required visual placed inside a chapter, later read by a generator to produce the actual simulation.

**Example:** A block naming the visualization type, data, and interaction is parsed automatically rather than read by hand.

#### diagram-report.py Script

The program that compares requested visuals against existing ones and reports coverage per chapter.

**Example:** It lists which requested visuals are still missing per chapter.

#### Digital Circuit Simulation

Modeling a circuit whose signals take discrete states, so a reader can observe switching behavior without building hardware.

**Example:** A lamp turns on only while a modeled button is held closed.

#### Directed Acyclic Graph

A structure of nodes and one-way arrows containing no path that returns to its starting node, guaranteeing a valid ordering exists.

**Example:** If A precedes B and B precedes C, no arrow may run from C back to A.

#### Directory Navigation

Moving between folders in a filesystem and referring to files by absolute or relative path.

**Example:** Referring to a chapter by its path from the project root.

#### Disconnected Subgraph

A cluster of ideas linked to one another but not reachable from the main body of the structure.

**Example:** Three ideas reference each other but nothing links them to the main body.

#### Distinct Definition

A definition that clearly separates its term from related terms rather than blurring into them.

**Example:** A terminal node and an orphaned node differ, and their definitions must show it.

#### Distractor Design

The construction of incorrect alternatives that represent genuine misunderstandings rather than obvious filler.

**Example:** An alternative reflecting a common confusion between two similar terms tests understanding; a nonsensical option does not.

#### Distractor Plausibility

The degree to which an incorrect alternative could reasonably be selected by a reader holding a specific misconception.

**Example:** An option reflecting confusion between terminal and orphaned nodes tests real understanding.

#### Docker Python Lab

An interactive exercise in which a reader edits and runs code inside a contained environment directly from a textbook page.

**Example:** A reader edits a loop, runs it, and sees output without installing anything.

#### Document Status Indicator

A visual marker in site navigation showing where a page stands in its review lifecycle.

**Example:** A colored dot marks a page as draft, in review, or complete.

#### Domain Skill Case Study

A worked example showing how a general library was extended for one subject, used as a pattern for other fields.

**Example:** An electronics book extending the shared library with three specialized skills.

#### Domain Skill Standards

The requirement that a specialized skill follow the same structure, description quality, and validation practices as the shared library.

**Example:** A specialized skill carries the same description quality and validation as a shared one.

#### Domain Vocabulary Gap

The shortfall that appears when a general skill lacks the terms, conventions, and correctness rules a specific subject requires.

**Example:** A general simulation generator has no notion of a tie-point row.

#### Domain-Specific Skill

A skill encoding knowledge particular to one subject area, used where general-purpose skills lack the necessary vocabulary or conventions.

**Example:** A skill that understands components and wiring is needed for electronics and useless elsewhere.

#### Drawing Specification Block

A structured description of a required static illustration placed inside a chapter for later generation.

**Example:** A description of a required static illustration placed inside a chapter.

#### Dropdown Select Control

An interface element presenting a list of options from which one is chosen, used for selecting modes or datasets.

**Example:** Choosing which dataset a chart displays.

#### Dry Run Mode

An option that reports what a program would change without changing anything, used to preview destructive operations.

**Example:** A script reports that it would rewrite forty files, without changing any.

#### Dublin Core Metadata

A standard set of descriptive fields such as title, creator, date, and rights, used to make a resource identifiable and citable.

**Example:** Recording a book's title, creator, date, and license so it can be cited.

#### Edges Section

The part of a graph file listing every ordering relationship as a pair of identifiers.

**Example:** A pair recording that one idea precedes another.

#### Editable Marker Positions

The ability to reposition annotation markers through stored data, allowing correction without regenerating anything.

**Example:** A misplaced label is corrected by editing two numbers in a data file.

#### Educational Metadata Section

The part of a simulation's descriptive record holding grade level, subject, objectives, and targeted cognitive levels.

**Example:** A simulation records that it targets the analyze level for secondary students.

#### Elapsed Time Measurement

Recording how long a skill takes from start to finish, separate from what it costs.

**Example:** A skill taking six minutes may still be the cheapest option available.

#### ElevenLabs Voice Settings

The parameters controlling a synthesized voice's identity, pacing, and expressiveness in generated audio.

**Example:** Adjusting pacing so narration matches a comfortable listening speed.

#### Encouraging Tone

A writing register that remains supportive and accessible, reducing the chance a reader abandons difficult material.

**Example:** Framing a difficult step as common rather than as a failure of the reader.

#### Equation Count

The number of mathematical expressions in a book, indicating how quantitative the material is.

**Example:** A book containing 240 formulas is clearly quantitative.

#### Equation Numbering

Assigning identifiers to displayed formulas so they can be referenced from surrounding text.

**Example:** Referring back to "Equation 3" later in a chapter.

#### Equivalent Page Count

An estimate of how many printed pages a book's content would occupy, giving readers a familiar sense of size.

**Example:** A word count presented as roughly 480 printed pages.

#### Error Analysis in Skills

Examining failed runs to determine whether the fault lies in the description, the instructions, a script, or the environment.

**Example:** A failure traced to a description that never matched the request.

#### Evaluate Level

The cognitive category covering judgment against criteria, expressed by actions such as critiquing, assessing, and justifying.

**Example:** "Judge whether a quality check is worth its cost."

#### Experience API

A specification for recording statements about learner activity in a consistent structure so that interactions can be collected and analyzed.

**Example:** A statement records that a reader completed a specific simulation at a specific time.

#### extract-sim-specs.py Script

The program that reads a chapter and produces a structured list of every simulation it requests, replacing manual parsing.

**Example:** It finds every visual request in a chapter and returns them as structured records.

#### Fact Fabrication Rate

The measured proportion of generated factual claims that no cited source supports.

**Example:** In one observed poster, eight of ten figures were unsupported and two of five citations did not exist.

#### False Trigger Misfire

A routing error in which a skill activates for a request it does not handle, usually caused by an overly broad description.

**Example:** A description mentioning "diagram" activates for every chart request.

#### FAQ

A collection of common questions with answers, organized to address the difficulties readers most often encounter.

**Example:** A collection answering the questions readers most often raise.

#### FAQ Categorization

Grouping questions by subject and difficulty so a reader can locate the relevant area quickly.

**Example:** Questions grouped into setup, workflow, and troubleshooting.

#### FAQ Coverage Gaps

Areas of a course for which no question exists, identified by comparing questions against the enumerated ideas.

**Example:** No question addresses a chapter's most difficult idea.

#### FAQ Generator

The skill that derives questions and answers from course material, the idea structure, and defined vocabulary.

**Example:** It derives questions from chapters, the idea structure, and defined vocabulary.

#### Feature Auto-Detection

Examining a project to determine which capabilities are already installed, so a report reflects reality rather than assumption.

**Example:** A scan reports which site capabilities a book already has.

#### Feature Checklist

A generated document listing available site capabilities and marking which are present in a given book.

**Example:** A generated table marking twenty capabilities present and twenty absent.

#### Feature Installation Routing

Matching a request for a site capability to the specific guide describing how to install it.

**Example:** A request mentioning "favicon" routes to the icon generation guide.

#### File Access Permissions

The rules governing which files an agent may read or modify during a session.

**Example:** An agent permitted to read a directory but not to delete from it.

#### File Globbing

Selecting files by wildcard pattern rather than naming each one, used to process every chapter or simulation at once.

**Example:** Selecting every chapter file with one pattern rather than naming forty.

#### File Layout as Token Strategy

Organizing content into separate files so a routine update reads only a small file instead of a large one.

**Example:** Keeping references in their own file lets an update read two hundred tokens rather than six thousand.

#### File Separation Principle

The rule that structure, presentation, behavior, and data each live in their own file, improving maintainability and caching.

**Example:** Styling changes touch one file and never risk breaking behavior.

#### Five Levels of Intelligence

A scale describing how responsive an educational resource is to its reader, progressing from static pages through interactive, adaptive, chatbot-integrated, and fully autonomous material.

**Example:** A book with embedded MicroSims and quizzes but no personalization sits at the second level.

#### Five-Hour Usage Window

A rolling measurement period used on some plans to meter consumption before capacity refreshes.

**Example:** Work paused near a limit resumes once the period refreshes.

#### Flesch-Kincaid Grade Level

A readability measure derived from sentence and word length, used to compare chapters against a declared target.

**Example:** A chapter measuring several grades above target needs simplification.

#### Font Size for Readability

Text sizing within a simulation chosen so labels remain legible when the simulation is displayed in a reduced frame.

**Example:** Labels legible at full size may be unreadable in a reduced frame.

#### Foundational Concept

A teachable idea with no prerequisites, serving as an entry point where a learner can begin.

**Example:** "Artificial Intelligence" has no prerequisites and is where a reader may begin.

#### Four-Hour Usage Window

A rolling period over which consumption is measured against a plan allowance, after which capacity replenishes.

**Example:** Consumption is measured against the allowance for this rolling period.

#### Freely-Licensed Images

Pictures whose terms permit reuse in educational material, typically with attribution.

**Example:** A photograph reusable in a textbook provided its creator is credited.

#### Frontmatter Contract

The agreement that only a small set of metadata fields is portable across agent platforms, making those fields the safe surface for a shared library.

**Example:** Only the name and description are guaranteed portable, so a shared library relies on those.

#### Frontmatter Quality Score

An assessment value written into a page's metadata block so its standing is visible to both tooling and authors.

**Example:** A lab page carrying a score of 78 in its metadata block.

#### Fullscreen Sim Button

A link that opens a simulation in its own tab at full size for closer inspection.

**Example:** A link opening a dense network diagram at full window size.

#### generate-favicon.py Script

The program that produces browser tab icons at required sizes from a source picture.

**Example:** It produces tab icons at several sizes from one source picture.

#### generate-images.py Script

The program that requests illustrations for a narrative and stores them with their descriptions.

**Example:** It requests illustrations for each scene of a narrative and stores them with descriptions.

#### generate-sim-scaffold.py

The program that creates the standard directory and placeholder files for a simulation from its specification.

**Example:** It creates the directory, markup, styling, metadata, and documentation stubs.

#### generate-sims-index.py

The program that builds the catalog page listing every simulation with its preview image.

**Example:** It rebuilds the catalog page after new simulations are added.

#### Getting Started Section

The part of a repository summary telling a newcomer how to install dependencies and run the site locally.

**Example:** Instructions to install dependencies and serve the site locally.

#### gh-deploy Command

The instruction that builds a site and publishes it to its hosting branch in one step.

**Example:** One instruction builds the site and publishes it.

#### Git

A distributed version control system that records snapshots of a project over time and allows changes to be reviewed, reverted, and merged.

#### Git Add Command

The instruction that marks changed files for inclusion in the next recorded snapshot.

#### Git Branching

Maintaining parallel lines of development so work in progress does not disturb the published state.

**Example:** Drafting a chapter without disturbing the published version.

#### Git Commit

The instruction that records marked changes as a permanent snapshot with an explanatory message.

**Example:** A message explaining why a change was made is what makes a later investigation possible.

#### Git Push

The instruction that sends locally recorded snapshots to the shared hosted copy.

#### Git Repository Structure

The layout of a project tracked by Git, including the working files, the history database, and the ignore rules that exclude generated artifacts.

**Example:** Working files, recorded history, and rules excluding generated output.

#### Git Status

The instruction that reports which files have changed and which are marked for the next snapshot.

#### GitHub Copilot

An AI assistant integrated with editors and GitHub that can consume portable skill definitions.

**Example:** An assistant embedded in an editor that can consume portable skill definitions.

#### GitHub Integration

Connecting a local repository to a hosted service that stores the shared copy and provides issues, reviews, and site hosting.

**Example:** Connecting a local book to its hosted copy so it can be published.

#### GitHub Pages Deployment

Publishing a built site through a hosting service attached to its repository.

**Example:** A built site served directly from its repository.

#### GitHub Projects Kanban

A board tracking outstanding work in columns representing stages of progress.

**Example:** Chapters move from drafted to reviewed to published.

#### Global Skill Installation

Placing skills where every project on a machine can use them, rather than inside a single project.

**Example:** One skill collection serving every book on a machine.

#### Glossary

An alphabetical collection of terms with definitions, serving as the reference layer for vocabulary used across a book.

**Example:** The reference layer readers consult when a chapter uses unfamiliar vocabulary.

#### Glossary Anchor Links

Direct links from body text to a specific definition, letting readers resolve unfamiliar vocabulary without losing their place.

**Example:** A term used in a chapter links directly to its definition.

#### Glossary Generator

The skill that converts an enumerated idea list into formatted definitions meeting a defined quality standard.

**Example:** It converts an idea list into formatted definitions meeting a defined standard.

#### Glossary Quality Report

A generated assessment scoring definitions against the metadata criteria and listing entries that need revision.

**Example:** It reports mean definition length and which entries need revision.

#### Glossary Term Ordering

Arranging entries alphabetically without regard to case, category, or topic, so any term can be located directly.

**Example:** "About Page" precedes "Accessible Color Schemes" regardless of subject.

#### Glossary Token Benchmark

A measured reference point showing that a three-hundred-fifty-term glossary can be produced by a single agent for roughly thirty-one thousand tokens.

**Example:** A measured figure used to estimate the cost of a glossary of any size.

#### Google Analytics GA4

A measurement service that records how readers reach and move through a published site.

**Example:** A report showing which chapters readers actually reach.

#### Google Antigravity

A Google AI development environment that can execute agent skills within a supported project.

**Example:** A development environment that can run skills within a supported project.

#### Government Archive Images

Pictures from public agency collections, often free of copyright restriction and suitable for educational reuse.

**Example:** A public agency photograph usable without a licensing fee.

#### Graceful Capability Degradation

Designing a skill so that when a platform lacks a capability, the skill produces a reduced but still useful result rather than failing.

**Example:** A layout review that cannot analyze a screenshot falls back to checking measurable properties in the source files.

#### Graph Legend and Colors

The key mapping each displayed color to its category, letting a reader interpret a diagram at a glance.

**Example:** A colored node is immediately recognizable as belonging to one category.

#### Graph Remediation

Correcting structural defects a quality report identifies, such as removing a loop or connecting an isolated idea.

**Example:** Adding a missing link so an isolated idea joins the main structure.

#### Graph Review Workflow

The author-led inspection of a generated structure before content generation begins, when corrections are still inexpensive.

**Example:** An author corrects two mislabeled ideas before chapters are generated.

#### Graphic Novel Format

A sequential illustrated narrative with panels and dialogue, used for extended storytelling within a book.

**Example:** A sequence of panels dramatizing how an idea was discovered.

#### Grep Before Read

Searching for a pattern to locate relevant lines before opening a file, so only the necessary region is loaded.

**Example:** Searching for a heading to locate the relevant section before opening a large file.

#### Grid Overlay Engine

The code layer that draws rectangular interactive regions over columns or sections of a poster-style image.

**Example:** Hovering over a poster column reveals an explanation of that column.

#### Grounding and Verification

The practice of tying generated claims to identifiable sources and confirming them before the claims are published.

**Example:** Every percentage in a poster is traced to a quoted passage from a cited URL before the poster is rendered.

#### Groups Section

The part of a graph file defining each category's display name, color, and font, which together form the legend.

**Example:** A category's display name, color, and font, which together form the legend.

#### Hallucination

Model output that is fluent and confident but factually wrong or unsupported by any source.

**Example:** An image model invents a plausible-looking citation for a statistic that no study actually reports.

#### Hands-On Lab Design

Constructing a practical activity a learner can complete independently with a defined set of parts.

**Example:** A wiring activity a learner completes alone with a specified parts kit.

#### Home Page Template

The starting page presenting a book's cover, summary, and entry points into its material.

**Example:** A landing page showing the cover, a summary, and links into the chapters.

#### Human in the Loop

A working pattern in which a person reviews and approves agent output at defined checkpoints instead of accepting results unexamined.

**Example:** An author reviews the concept list before chapter generation begins, because correcting concepts later is far more expensive.

#### ibook Runbook

The command that inspects a textbook project and reports how far the build pipeline has progressed and which skill to run next.

**Example:** It reports that the structure exists and chapters do not, so chapter design is next.

#### IDE Agent Integration

Running an AI coding agent inside an editor so file context, terminal, and generated changes share one workspace.

**Example:** Generated changes appear in the same window where the author is editing.

#### Idempotent Script Design

Writing a program so that running it repeatedly produces the same end state as running it once.

**Example:** A script that inserts an iframe checks whether one is already present rather than adding a duplicate.

#### Iframe Control Visibility

Confirming that a simulation's interface elements remain reachable when displayed at the frame height a page assigns.

**Example:** A slider positioned below the visible region is unusable even though the simulation itself works.

#### Iframe Embedding

Placing a self-contained page inside a documentation page so a simulation runs inline without navigating away.

**Example:** A simulation runs inline on a chapter page without navigating away.

#### Iframe Height Synchronization

Propagating a simulation's recorded height into every place it is embedded, so frames neither clip content nor leave blank space.

**Example:** Changing one value and running a script updates the frame height wherever that simulation appears.

#### Illustrated Story Format

A narrative retelling of course material paired with generated pictures, used to introduce ideas through story.

**Example:** A narrative introducing dependency ordering through a character's journey.

#### Image Attribution

Crediting the creator and stating the license of a reused picture, as the license terms require.

**Example:** A caption naming the photographer and the license.

#### Image Compression

Reducing the file size of pictures so pages load quickly, while keeping quality acceptable for reading.

**Example:** A cover reduced from four megabytes to four hundred kilobytes.

#### Image Prompt Engineering

Composing the description supplied to an image generator so the resulting picture matches an intended composition and content.

**Example:** Specifying composition, style, and exact wording so a picture matches its plan.

#### Image Understanding Dependency

A skill's reliance on a model's ability to interpret pictures, which is the capability most likely to be missing on non-Claude platforms.

**Example:** A layout review requiring picture interpretation cannot run everywhere.

#### Image Zoom Lightbox

A feature enlarging a picture in an overlay when a reader selects it, useful for detailed diagrams.

**Example:** A dense diagram expands to full size when selected.

#### Improving Skill Quality

Revising a skill in response to measured defects, then re-running the benchmark to confirm the change helped.

**Example:** A description rewritten after it failed to trigger on three sample requests.

#### Indegree Analysis

Counting how many ideas depend on each idea, revealing which are most heavily relied upon and therefore most important to explain well.

**Example:** An idea depended on by twenty-seven others deserves careful explanation.

#### Inline Code Antipattern

Embedding styling or logic directly inside a markup file, which is acceptable for prototypes but obstructs later maintenance.

**Example:** Styling written inside markup is quick to prototype and hard to maintain.

#### Input Versus Output Tokens

The distinction between text supplied to a model and text produced by it, which are metered separately and priced differently.

**Example:** Reading a long chapter costs input; writing a new one costs output.

#### Instructional Scaffolding

Sequencing support so each new idea rests on material already presented, and removing that support as competence grows.

**Example:** A worked example precedes the exercise asking for the same procedure.

#### Instructor Guide

Teacher-facing material describing how to use a book in a classroom, including pacing and discussion prompts.

**Example:** Pacing suggestions and discussion prompts for a two-week unit.

#### Intelligent Textbook

An educational resource that combines written content with structured knowledge and interactive elements so it can adapt to and respond to a reader.

**Example:** A book whose concepts are linked to a dependency graph, whose diagrams are interactive, and whose quizzes are aligned to cognitive levels.

#### Interactive Infographic Overlay

A labeled illustration in which a picture carries no printed annotation and a code layer draws numbered markers, labels, and explanations on top.

**Example:** Marker positions and wording can be corrected or translated without regenerating the underlying picture.

#### Invoking a Skill

Causing a skill's instructions to load and run, either by describing the task or by naming the skill explicitly.

**Example:** Describing a task lets the agent select the matching skill automatically.

#### ISO 11179 Standards

A metadata registry specification whose definition criteria require entries to be precise, concise, distinct, non-circular, and free of procedural rules.

**Example:** Defining a term by restating its own name violates the non-circularity criterion.

#### Iterative Refinement

Improving generated output through successive review-and-revise cycles rather than expecting a single correct result.

**Example:** A first draft is generated, reviewed, and regenerated with corrections.

#### JSON Schema Validation

Checking a structured data file against a formal description of its required shape, catching missing or malformed fields automatically.

**Example:** A missing required field is caught before the file reaches a viewer.

#### JSON Serialization

Converting structured data to and from a text format that both programs and web pages can read.

**Example:** Writing measurements to a file both a script and a web page can read.

#### JSONL Usage Log

An append-only file with one structured record per line, used to accumulate usage events without rewriting earlier entries.

**Example:** Each completed skill run appends one line without rewriting the file.

#### Jumper Wire Routing

Choosing paths for connecting wires so a circuit is both correct and readable to someone rebuilding it.

**Example:** Wires kept short and flat so a learner can trace each connection.

#### Lab Rubric Scoring

Assessing a practical activity against explicit point-allocated criteria rather than general impression.

**Example:** A rubric checks whether every part is listed, every step is illustrated, and the expected result is stated.

#### Label Length Limit

The maximum character count for a node name, set so text fits inside a rendered box without truncation.

**Example:** Thirty-two characters keeps labels readable at normal zoom in a graph with hundreds of nodes.

#### Large Language Model

A statistical model trained on very large text collections that predicts the next unit of text given preceding text, enabling it to generate and transform natural language.

**Example:** Claude, the model behind Claude Code, reads a chapter outline and drafts explanatory prose that matches the requested reading level.

#### LaTeX Equation Syntax

The notation used to express mathematical expressions in plain text for later typesetting.

**Example:** A fraction written in plain text and typeset when the page renders.

#### Layout Specification Lock

Fixing the exact wording and arrangement of a planned poster before generation, so nothing can drift during rendering.

**Example:** Wording approved in text cannot change once rendering begins.

#### Leader Line Rendering

Drawing a connecting line from a marker to its label so the association is unambiguous when labels sit outside the illustration.

**Example:** A thin line connects a marker to its label in the margin.

#### Leaflet Map Library

A JavaScript library that renders interactive geographic maps with markers and layers.

**Example:** Markers showing where a technology was developed.

#### Learning Dependency

A relationship asserting that one idea should be understood before another can be taught effectively.

**Example:** Understanding acyclic structures before attempting to detect closed paths.

#### Learning Graph

A directed structure whose nodes are teachable ideas and whose arrows indicate which ideas should be understood before others.

**Example:** An arrow from "Directed Acyclic Graph" to "Cycle Detection" shows the first must be understood before the second.

#### Learning Graph as Roadmap

The use of a dependency structure as a navigational aid that shows a learner where they are and what must come next.

**Example:** A reader sees which ideas they have covered and which come next.

#### Learning Graph CSV Format

The tabular file holding one row per teachable idea with its identifier, label, prerequisite list, and category.

**Example:** One row per idea with its identifier, label, prerequisites, and category.

#### Learning Graph Generator

The skill that converts a course description into a validated graph with categories, quality reports, and a viewer-ready data file.

**Example:** It turns a course description into a validated structure with reports and a viewer file.

#### Learning Graph JSON Schema

The formal description of the required structure of a graph file, used to validate generated output automatically.

**Example:** It catches a missing legend entry before the diagram is rendered.

#### Learning Graph Quality Score

A composite rating derived from structural checks such as absence of loops, connectivity, and dependency density.

**Example:** A structure with no loops, no isolated ideas, and healthy density scores well.

#### Learning Graph Viewer

An interactive simulation that renders a graph file, allowing readers to pan, zoom, search, and inspect relationships.

**Example:** A reader searches for an idea and sees everything it depends on.

#### Learning Outcomes

Statements of what a learner will be able to do after completing a course, expressed as observable actions.

**Example:** "Analyze a dependency structure and diagnose its defects."

#### Learning Pathway

An ordered route through material that respects what must be understood first, leading a learner toward a stated goal.

**Example:** One valid route runs from foundations through skills to publishing.

#### Learning Record Store

A repository that receives and stores learner activity statements for later querying and analysis.

**Example:** A repository queried to find which simulations learners actually completed.

#### Lesson Plan

A structured teaching outline for a single session, listing objectives, activities, and timing.

**Example:** A fifty-minute session with objectives, an activity, and a closing discussion.

#### Level 1 Static Content

The lowest tier of textbook intelligence, consisting of fixed text and images with no navigation aids or interactivity.

**Example:** A printed page reproduced as an image with no links.

#### Level 2 Interactive Content

A tier of textbook intelligence in which readers engage beyond passive reading through hyperlinks, embedded videos, quizzes, MicroSims, and a searchable glossary.

**Example:** A slider that redraws a chart as a reader changes a value.

#### Level 3 Adaptive Content

A tier of textbook intelligence in which presented material changes based on a reader's demonstrated progress, using personalized pathways and concept-graph traversal.

**Example:** Additional practice appears for a reader who answered incorrectly.

#### Level 4 Chatbot Integration

A tier of textbook intelligence in which a large-language-model-powered conversational tutor, often built on GraphRAG, answers a reader's questions in real time.

**Example:** A reader asks the embedded chatbot to re-explain a concept using a different analogy.

#### Level 5 Autonomous AI

The highest, largely aspirational tier of textbook intelligence, in which a system deeply understands each reader's knowledge state and generates fully customized lessons in real time.

**Example:** A system regenerates an entire chapter's worked examples to match one reader's prior misconceptions.

#### Linear Chain Detection

Identifying long runs where each idea depends only on the one immediately before it, which suggests missing relationships and a single rigid route.

**Example:** Forty ideas in a single unbranching line suggest missing relationships.

#### LinkedIn Announcement Post

A short professional-network message announcing a book milestone, drawing its figures from the recorded measurements.

**Example:** A short post citing the book's page count and linking to the site.

#### LinkedIn Carousel Document

A multi-page slideshow posted to a professional network, in which readers swipe through successive panels.

**Example:** Eight panels a reader swipes through summarizing a book.

#### Listing Available Skills

Displaying the skills an agent can currently use, along with their summaries.

**Example:** A summary of every skill currently loaded and what it does.

#### Local Development Server

A process that serves a site on the authoring machine and refreshes it as files change, allowing immediate preview.

**Example:** Saving a chapter refreshes the browser within a second.

#### Main Topics Covered

The enumerated subject areas a course addresses, providing the raw material from which individual teachable ideas are drawn.

**Example:** Ten grouped subject areas from which teachable ideas are drawn.

#### main.html File

The markup file defining a simulation's structure and loading its stylesheet, logic, and external libraries.

**Example:** It loads the styling, the behavior, and any external library a simulation needs.

#### Marginal Token Cost

The additional cost of one more unit of output after fixed overhead is excluded, used to predict how expense scales with size.

**Example:** Roughly fifty-four tokens per additional glossary entry once overhead is excluded.

#### Markdown Formatting

A lightweight plain-text syntax for headings, lists, links, and emphasis that converts cleanly to HTML.

**Example:** A chapter written as `## Section` and `- bullet` renders as a styled heading and list on the published site.

#### Markdown Parsing in Python

Extracting structure such as headings and fenced blocks from markdown source so content can be counted or transformed.

**Example:** Extracting every heading from a chapter to count its sections.

#### MARP Slide Deck

A presentation authored in markdown and rendered as a self-contained web deck that can be published alongside a book.

**Example:** A chapter summary published as a browsable web presentation.

#### Mascot Admonition Types

The distinct callout roles a recurring character occupies, such as warning, encouragement, or summary, each with its own visual treatment.

**Example:** One appearance warns, another encourages, and a third summarizes.

#### Mascot Self-Introduction

The first appearance of a recurring character, in which it names itself and previews the roles it will play later in the book.

**Example:** The character names itself and previews its roles in the first chapter.

#### Mascot Voice and Placement

The rules governing how a recurring character speaks and how often it appears, preventing overuse from diluting its effect.

**Example:** Two appearances per chapter keep a character noticeable rather than tiresome.

#### Math Equation Support

Site configuration that renders mathematical notation from source markup into properly typeset formulas.

**Example:** A formula written in plain text renders as typeset notation.

#### MathJax Configuration

The settings that enable and control mathematical typesetting on a generated site.

**Example:** Settings enabling equation rendering across every page.

#### Measurement ID

The identifier connecting a site to its analytics property, placed in the site configuration.

**Example:** A short identifier placed in the site configuration to enable reporting.

#### Mermaid Diagram Syntax

A text notation for describing flowcharts, sequence diagrams, and state machines that render as diagrams without manual drawing.

**Example:** A few lines of text produce a flowchart that stays editable in version control.

#### Meta-Skill

A skill whose primary job is to route a request to one of several detailed guides rather than to perform the task itself.

**Example:** A single simulation meta-skill replaces seventeen separate generators while loading only the guide the request needs.

#### Metadata Loading Budget

The cost of the always-resident summary for every installed skill. It is paid on every request, so descriptions must stay short.

**Example:** Fourteen skill summaries are read on every request, so each must stay short.

#### Metadata Section

The part of a graph file carrying descriptive information about the work, such as title, creator, date, and license.

**Example:** Title, creator, date, and license recorded inside a graph file.

#### MicroSim

A small self-contained interactive simulation embedded in a textbook page, focused on demonstrating one idea.

**Example:** A slider that changes a parameter and immediately redraws the result lets a reader discover a relationship directly.

#### MicroSim Directory Structure

The standard folder holding a simulation's markup, styling, logic, data, metadata, and documentation page as separate files.

**Example:** Six files per simulation, each with one responsibility.

#### MicroSim Generator

The meta-skill that routes a simulation request to the appropriate specialized guide and produces a complete package of files.

**Example:** A request for a chronology routes to the timeline guide automatically.

#### MicroSim Index Catalog

A generated listing of every simulation in a book with preview images and links.

**Example:** A grid of preview images linking to every simulation in a book.

#### MicroSim index.md File

The documentation page for a simulation, embedding it in a frame and providing a full-screen link and explanatory text.

**Example:** It embeds the simulation and offers a full-screen link.

#### MicroSim Metadata Schema

The formal description of required descriptive fields for a simulation, enabling automated cataloging and validation.

**Example:** It requires authorship, discovery, educational, and technical sections.

#### MicroSim metadata.json

The structured descriptive record for a simulation, covering authorship, discovery keywords, educational targeting, and technical requirements.

**Example:** It records that a simulation targets a cognitive level and needs one library.

#### MicroSim Quality Score

A computed rating of a simulation against structural and presentation standards.

**Example:** A simulation with inline styling and no metadata scores poorly.

#### MicroSim Screen Capture

Producing a still image of a running simulation for use as a catalog preview.

**Example:** A still image used as the catalog preview for a simulation.

#### MicroSim Standardization

Bringing existing simulations into conformance with the current file layout, control, and metadata conventions.

**Example:** An older simulation is split into separate files and given metadata.

#### MkDocs

A static site generator that builds a navigable website from a directory of markdown files and a configuration file.

**Example:** A folder of chapter files becomes a navigable website.

#### MkDocs Material Theme

A widely used presentation layer for MkDocs providing search, navigation, admonitions, code highlighting, and responsive layout.

**Example:** It supplies search, callouts, and responsive layout without custom styling.

#### MkDocs Plugins

Optional packages that add capabilities to a site generator, such as search enhancements or image handling.

**Example:** A plugin that generates social preview images at build time.

#### mkdocs.yml Configuration

The file that declares a site's title, theme, plugins, extensions, and navigation tree.

**Example:** It declares the site title, theme, and the full menu.

#### Model Selection Per Skill

Declaring which model tier a skill should run on, so demanding work gets a stronger model and routine work gets a cheaper one.

**Example:** Simulation generation is assigned a high-capability model while quiz formatting is assigned a lighter one.

#### Model Versus Script Division

The design rule separating work that requires judgment, which the model performs, from work with one correct answer, which a program performs.

**Example:** Prose is written by the model; word counts are produced by a script.

#### Multiple Learning Pathways

The property of a well-formed structure that several valid routes exist through the material, rather than one fixed sequence.

**Example:** A reader may reach publishing through either the simulation or the media route.

#### Multiple-Choice Question

An assessment item presenting one correct answer among several alternatives.

**Example:** One correct answer among four, each alternative reflecting a real misunderstanding.

#### Navigation Structure

The ordered hierarchy of pages presented to readers as a site's menu, declared explicitly rather than inferred from the filesystem.

**Example:** Every new markdown file must be added to this structure or it will not appear in the site menu.

#### Never Use Master Branch

The project convention that the principal line of development is always named `main`, including in configuration that generates edit links.

**Example:** A configuration generating edit links must point at the `main` branch.

#### Nodes Section

The part of a graph file listing every teachable idea with its identifier, label, and category assignment.

**Example:** Each idea with its identifier, label, and category.

#### Non-Circular Definition

A definition that does not rely on the term being defined, nor on another term whose own definition depends on it.

**Example:** "A learning graph is a graph that shows learning" explains nothing and is circular.

#### Nondeterminism in LLM Output

The property that a language model may produce different responses to identical input across runs, because output is sampled rather than computed deterministically.

**Example:** Running the same generation twice can yield two valid but differently worded definitions, which is why quality checks are scripted rather than eyeballed.

#### Note and Tip Admonitions

Callout variants used for supplementary information and practical advice respectively.

**Example:** A tip box offers a shortcut without interrupting the main explanation.

#### On-Demand Guide Loading

Reading a detailed instruction file only at the moment the matching task begins, rather than keeping every guide resident.

#### One-Shot Generation Risk

The hazard of asking an image generator to invent factual content and render it simultaneously, since neither step is verified.

#### Open Educational Resources

Teaching materials released under terms that permit free use, adaptation, and redistribution.

#### Open Graph Meta Tags

Markup in a page header supplying the title, description, and image that platforms use when rendering a shared link.

#### OpenAI Codex

An AI coding agent from OpenAI capable of running skills that adhere to the portable subset of the standard.

#### Optimizing Claude Usage

Arranging work to fit within plan allowances by sequencing, batching, and offloading deterministic steps.

#### Opus Versus Sonnet Routing

The specific choice between a high-capability model and a faster, cheaper one, traded off against task difficulty and cost.

#### Orphaned Node

A teachable idea with no incoming and no outgoing arrows, disconnected from the rest of the structure and indicating a defect.

**Example:** An idea added to the list but never linked to anything will appear isolated in the rendered diagram.

#### Outdegree Analysis

Counting how many prerequisites each idea declares, revealing ideas that may be too demanding to introduce at one point.

#### Overlay Explore Mode

An interaction style in which hovering or selecting a marker reveals explanatory information about that feature.

#### Overlay Quiz Mode

An interaction style in which a reader is asked to identify a named feature by selecting the correct marker.

#### p5.js Built-In Controls

The interface elements the drawing library supplies directly, used instead of hand-drawn substitutes so behavior stays consistent and accessible.

#### p5.js Draw Loop

The routine that runs repeatedly to render each frame, producing animation and responding to changing values.

#### p5.js Library

A JavaScript library for drawing and animation that provides a canvas, a render loop, and simple interface controls.

#### p5.js Setup Function

The routine that runs once at start to create the canvas and build interface controls.

#### Page Feedback Widget

A simple control asking whether a page was helpful, collecting signal about which material needs revision.

#### Parallel Agent Execution

Running several agents at the same time on portions of a task, paying startup overhead once per agent.

#### Parts Kit Buildability

The requirement that a practical activity be completable with an affordable, specified set of components.

#### Passage-Level Verification

Confirming an assertion by quoting the specific text in a source that supports it, rather than citing a document as a whole.

**Example:** A figure is accepted only when the sentence stating it can be quoted from the cited page.

#### Path Handling

Constructing and resolving file locations reliably so scripts work regardless of the directory they are run from.

#### Pedagogical Mascot

A recurring character that delivers guidance, warnings, and encouragement in a consistent voice, giving a book a familiar presence.

**Example:** A character who appears to flag a common mistake helps readers recognize a recurring hazard.

#### Permission Management

Controlling which actions an agent may take without asking, balancing convenience against the risk of unintended changes.

#### pip Package Management

The tool that installs and updates third-party Python packages.

#### Pipe-Delimited Dependencies

A storage convention listing several prerequisite identifiers in one spreadsheet cell separated by vertical bars.

**Example:** A cell containing `1|3|7` records three prerequisites for a single idea.

#### Plotly Library

A JavaScript plotting library well suited to mathematical functions and scientific charts with interactive axes.

#### PowerPoint Lecture Deck

A downloadable presentation file intended for classroom use, generated with structured narrative and presenter guidance.

#### Practice Exercises

Problems a learner attempts without a shown solution, used to consolidate a newly presented procedure.

#### Precise Definition

A definition that states exactly what a term means without ambiguity or unnecessary hedging.

#### Prerequisite Ordering in Text

Arranging explanations within a chapter so nothing is used before it has been introduced.

#### Prerequisite Relationship

The specific pairing in which one idea must precede another, forming the basis of a recommended teaching order.

#### Press Release

A formal announcement written for journalists, stating what was released, why it matters, and where to find it.

#### Progressive Disclosure

The loading strategy in which an agent sees only a skill's summary by default, reads its instructions when triggered, and opens detailed guides only when needed.

**Example:** A routing table of one page stays resident while a thirty-page implementation guide loads only for the matching request.

#### Project Instruction Files

The documents carrying persistent guidance for agents working in a repository, sometimes duplicated under a second filename for platform compatibility.

#### Project-Local Skill Directory

A folder inside a single book holding skills that apply only to that book.

#### Project-Specific Skills

Skills installed inside one project so they apply only to that book, typically because they encode subject-specific knowledge.

**Example:** A circuit-drawing skill lives in the electronics book and is invisible to unrelated projects.

#### Prompt

The text supplied to a language model to elicit a response. It carries the request, any supporting material, and constraints on the desired output.

#### Prompt Engineering

The practice of composing and revising prompts so a model produces accurate, well-formed output reliably rather than by chance.

**Example:** Specifying "return only a JSON array, no prose" removes the need to strip explanatory text from the result.

#### Pronounce Button

A small control beside a defined term that plays its spoken pronunciation, helping readers with unfamiliar vocabulary.

**Example:** A reader unsure how to say a technical term hears it rather than guessing.

#### Prose to Circuit Translation

Interpreting a plain-language description of a circuit and expressing it as an explicit component and connection list.

#### Python

A general-purpose programming language used throughout this workflow for parsing, validating, converting, and reporting on textbook data.

**Example:** A short Python script converts a dependency spreadsheet into the JSON format the graph viewer expects.

#### Python Scripts in Skills

Programs bundled with a skill that perform its deterministic steps, keeping that work out of the model's output.

**Example:** A script counts words and equations across every chapter and writes the totals to a metrics file.

#### Python Standard Library

The modules distributed with Python that handle common tasks such as file access, structured data, and pattern matching without additional installation.

#### Quality Gate

A defined check that output must pass before the next stage begins, preventing defects from propagating into expensive downstream work.

**Example:** A learning graph must contain no cycles before chapter generation starts.

#### Quality Gate Short-Circuit

Skipping a validation step whose result is already known to pass, avoiding cost without lowering standards.

**Example:** A course description already scored above the threshold is not re-scored during a later run.

#### Quality Metrics Report

The generated document presenting structural measurements of a graph together with recommendations for improvement.

#### Question Admonition

A callout variant used to pose a question to the reader, often with a concealed answer.

#### Quiz

A set of questions used to check whether a reader has grasped a chapter's material.

#### Quiz Analytics

Analysis of assessment results to identify material readers consistently struggle with.

#### Quiz Bank JSON

A structured export of all assessment items across a book, usable by external systems.

#### Quiz Bloom Distribution

The allocation of assessment items across cognitive categories, ensuring a quiz tests more than recall.

#### Quiz Explanation Text

The rationale accompanying each item that states why the correct answer is right and why each alternative is wrong.

#### Quiz Generator

The skill that produces chapter assessments aligned to assigned ideas and distributed across cognitive categories.

#### Rate Limit Handling

Responding to a throughput or allowance cap by pacing work rather than failing, so a long job completes across periods.

#### Read-Only State Detection

Inspecting a project to determine its progress without altering any file, so a status report can never cause damage.

#### Reading Level Consistency

Uniformity of textual difficulty across a book, so chapters written separately do not vary noticeably in complexity.

#### Reading Level Specification

A declared expectation of textual difficulty, used to keep prose consistent across chapters written at different times.

#### README Generation

Producing the repository's front page, including a summary, badges, statistics, and setup instructions.

#### Reference Docs in Skills

Detailed instructional documents stored alongside a skill and read selectively, allowing depth without a permanent loading cost.

#### Reference File Separation

Storing citations outside chapter prose so they can be reviewed and updated without loading the chapter body.

#### Reference Generator

The skill that produces curated citation lists for each chapter with short statements of each source's relevance.

#### Reference Loading Budget

The cost of opening a specific detailed guide, paid only for the one guide a task actually needs.

#### References Directory

The folder holding detailed guides that are read only when a particular task requires them, keeping them out of the default load.

#### Regular Expressions

A pattern language for matching and extracting text, used to locate structured fragments inside documents.

#### Reinforcing Loop

A closed path of influence in which a change is amplified as it travels around the loop, producing growth or collapse.

**Example:** More users attract more content, which attracts more users.

#### Remember Level

The cognitive category covering retrieval of stored knowledge, expressed by actions such as defining, listing, and identifying.

#### Rendered Image Audit

Checking a finished picture against its locked specification to confirm every element was reproduced correctly.

#### Repository Badges

Small status images displayed on a repository page showing license, build state, or site link.

#### Responsive Sim Layout

Designing a simulation so it adapts to the width available, remaining usable on narrow screens and inside frames.

#### Retrieval Augmented Generation

A technique in which relevant stored passages are retrieved and supplied to a model so its answers are grounded in specific source material.

**Example:** A course assistant answers from the book's own exported question set rather than from general knowledge.

#### Runbook Command

A command that reports the ordered steps of a process and identifies which step comes next, without performing the steps itself.

**Example:** A runbook reports that the learning graph exists and the chapter structure does not, so chapter design is next.

#### Runnable Code Block

A code sample a reader can execute in place and modify, rather than only read.

#### Schematic Verification

Confirming that a rendered electrical diagram matches the circuit that was described.

#### Schemdraw Library

A Python library that draws electrical schematics from code, so a diagram remains editable and version-controlled.

**Example:** A schematic is stored as a short program, letting a component value change without redrawing anything by hand.

#### Script Execution Permissions

The settings that determine whether an agent may run a program directly or must request approval first.

#### Script Exit Codes

Numeric values a program returns to indicate success or the kind of failure, allowing other scripts to react.

#### script.js File

The file holding all of a simulation's behavior, including event handling and rendering logic.

#### Scripts Directory

The folder holding executable programs a skill runs to perform deterministic work.

#### Search Configuration

The settings controlling how a site indexes its content and presents matches to a reader.

#### Search Metadata Section

The part of a simulation's descriptive record holding tags, visualization type, and keywords that support discovery.

#### Section Organization

Dividing a chapter into ordered subsections so material progresses from simpler to more demanding.

#### Security in Skill Execution

The practices that keep a skill from taking damaging or unauthorized actions, including restricting tools and reviewing what a script does before running it.

#### Seeded Randomness

Generating apparently random values from a fixed starting number so a simulation produces identical results each time it runs.

**Example:** A scattered arrangement looks arbitrary but appears the same for every reader, making it safe to describe in surrounding text.

#### Selective File Reading

Loading only the portion of a file relevant to the current task rather than its entire contents.

#### Self-Dependency Check

Verifying that no idea lists itself as its own prerequisite.

#### Separate Quiz Files

Storing each chapter's assessment in its own file so quizzes can be revised without reading the chapter body.

#### Separate References Files

Storing each chapter's citations in a dedicated file so reference maintenance does not require loading chapter prose.

#### Separating Facts From Pixels

The design rule that content is decided and verified in text before any picture is produced, so the image generator never chooses a figure.

#### Sequential Sim Execution

Generating simulations one after another by default, since concurrent generation multiplies fixed overhead without improving results.

#### Serial Agent Execution

Running one agent that completes an entire task, paying startup overhead only once.

#### Serial Versus Parallel Tradeoff

The decision between finishing sooner and spending less. Parallelism reduces elapsed time but multiplies fixed overhead, and is only justified when the work is genuinely large per agent.

**Example:** Four agents writing glossary definitions cost more than twice as much as one agent and produce no better result.

#### Session Log Format

The agreed structure of a working record, covering the request, the choices made, the revisions applied, and the result.

#### Session Logging

Recording what was produced during a working session and the decisions that shaped it.

#### Shebang Line

The first line of a script that names the interpreter to run it, allowing the file to be executed directly.

#### Shell Script Wrapper

A short shell program that supplies standard arguments and paths to a longer program, giving it a simple name users can remember.

#### Shell Scripting

Writing sequences of shell commands into an executable file so a multi-step task can be repeated identically.

**Example:** A script that starts a local server, waits for rendering, and captures a screenshot removes three manual steps.

#### Sim Lifecycle Status

The recorded stage of a simulation's production, progressing from specified through scaffolded, implemented, validated, and deployed.

#### Sim Scaffolding Workflow

Creating a simulation's directory and placeholder files automatically so only the behavior file requires authoring.

#### Site Build Command

The instruction that renders markdown sources into a complete static website.

#### Site Logo and Favicon

The small identifying marks shown in a site header and browser tab, typically derived from a book's cover or character artwork.

#### Site Metrics Collection

Gathering counts of published pages, simulations, and assets from a built site.

#### Skill Alias Map

A record of which former skill names now correspond to which routes inside a consolidated skill, so older references remain resolvable.

#### Skill Benchmarking

Measuring a skill's output quality, runtime, and token consumption against a fixed set of cases so revisions can be compared.

#### Skill Composition

Combining several skills in sequence so the output of one becomes the input of the next.

**Example:** The concept list produced by the graph skill becomes the term list consumed by the glossary skill.

#### Skill Consolidation

Merging several related skills into one router plus a set of guides, reducing the number of installed skills without losing capability.

#### Skill Creator Skill

A skill used to author, revise, and evaluate other skills, including testing how reliably their descriptions trigger.

#### Skill Description Field

The required summary stating what a skill does and when it should be used. It is the text an agent matches a request against.

**Example:** A description that lists concrete trigger phrases fires reliably; a vague one is skipped or misfires.

#### Skill Directory Structure

The folder layout of a skill: the required instruction file plus optional folders for reference documents, executable scripts, and templates.

#### Skill Discoverability

The degree to which an agent can determine that a relevant skill exists, governed almost entirely by description quality.

#### Skill Distribution Methods

The ways a skill reaches other users: a shared repository, a copied folder, or a plugin registry.

#### Skill Evaluation Harness

A repeatable test setup that runs a skill against known inputs and scores the output, making quality changes measurable rather than anecdotal.

#### Skill Execution Context

The environment in which a skill runs, including the working directory, available tools, and granted permissions.

#### Skill Failure Modes

The recurring ways a skill breaks: failing to trigger, triggering wrongly, loading the wrong guide, or producing output that fails validation.

#### Skill Library

The complete collection of skills available to an agent, together with the conventions that keep them consistent.

#### Skill Library Maintenance

The ongoing work of updating, testing, and pruning a collection of skills so they remain accurate as tools and standards change.

#### Skill License Field

An optional metadata entry naming the terms under which a skill may be used or redistributed.

#### Skill Metadata Field

An optional map of string keys and values carrying client-specific or organization-specific information that the agent itself ignores.

#### Skill Name Field

The required identifier for a skill, restricted to lowercase letters, digits, and hyphens, and matching the folder that contains it.

#### Skill Naming Conventions

The rules governing skill identifiers: lowercase, hyphen-separated, descriptive, and identical to the containing folder name.

#### Skill Packaging

Assembling a skill's instruction file, scripts, references, and assets into a self-contained folder that can be copied or shared.

#### Skill Portability

The degree to which a skill written for one agent platform runs correctly on others without modification.

#### Skill Routing Table

The decision table inside a meta-skill that maps trigger keywords to the guide file responsible for each variant of a task.

#### Skill Testing and Debugging

Exercising a skill against representative requests and diagnosing the cause when its behavior differs from what its instructions specify.

#### Skill Trigger Matching

The process by which an agent compares an incoming request against installed skill descriptions to decide which skill to load.

#### Skill Usage Analytics

Processing recorded usage events to reveal which skills run most often and what each consumes.

#### Skill Usage Hook

A configured callback that records information each time a skill runs, producing data for later analysis.

#### Skill Usage Report

A generated summary showing which skills ran, how long they took, and what they consumed.

#### Skill Variance Analysis

Running the same case repeatedly to measure how much a skill's output changes between runs, distinguishing real improvement from random fluctuation.

**Example:** A skill scoring 80 once and 60 the next time has a consistency problem, not a quality problem.

#### Skill Versioning

Recording a revision number inside a skill so behavior changes can be tracked and defects traced to a specific revision.

#### Skill Workflow Instructions

The step-by-step body of a skill file that an agent follows once the skill is triggered.

#### SKILL.md File

The required markdown file at the root of a skill folder, containing metadata at the top and workflow instructions below.

#### Skills Versus Commands

The distinction between a capability an agent selects automatically based on a request and a procedure the user invokes explicitly by name.

#### Skills Versus Prompts

The distinction between a reusable packaged capability with supporting files and a single request typed into a session.

#### Slash Command Invocation

Triggering a skill or command by typing its name after a forward slash rather than describing the task in prose.

#### Slide Deck Publishing

Adding a rendered presentation to a site so it can be viewed in a browser and linked directly.

#### Slider Control

A draggable interface element for selecting a value from a continuous range, used for parameters such as speed or size.

#### Social Media Preview Card

The image and text a platform displays when a link to a page is shared.

#### Solderless Breadboard

A reusable board with gridded holes that hold components and wires, allowing circuits to be assembled without permanent joins.

#### Source Discovery Phase

The stage locating authoritative material that could support each planned assertion.

#### Source Sidecar File

A companion file stored beside a finished image recording every claim, its source address, and its supporting quotation.

#### Speaker Notes

Presenter-facing text attached to a slide, describing what to say and which points to emphasize.

#### Stale Symlink Cleanup

Removing filesystem pointers that reference deleted or renamed skills, preventing load errors.

#### Stop Hook

A callback that fires when an agent finishes a turn, commonly used to record results or perform cleanup.

**Example:** A stop hook commits the turn's file changes using a message the agent left behind.

#### Strict Build Mode

A build setting that treats warnings such as broken links as failures, preventing defective sites from being published.

**Example:** A link to a page that was renamed fails the build instead of reaching readers.

#### style.css File

The file holding all of a simulation's presentation rules, kept separate from its structure and behavior.

#### Sub-Agent Startup Overhead

The fixed token cost of launching an additional agent, incurred before it performs any useful work, because it must receive its own instructions and tool definitions.

**Example:** Roughly twelve thousand tokens are consumed by each additional agent before it writes a single definition.

#### Substitution Prohibition

The explicit instruction forbidding an image generator from altering figures, names, or labels, or inventing additional ones.

#### Supplementary Content

Material surrounding the chapters, including glossary, questions, assessments, references, and reports.

#### Supporting Assets in Skills

Non-instruction files bundled with a skill, such as schemas, stylesheets, or starter templates, that its workflow copies or reads.

#### Symbolic Link Installation

Installing a skill by creating a filesystem pointer to its source folder, so edits to the source take effect immediately without copying.

**Example:** Linking a repository folder into the agent's skills directory means a fix committed once is live everywhere.

#### sync-iframe-heights.py

The program that reads each simulation's recorded height and updates every embedding frame to match.

#### System Prompt

Instructions supplied to a model separately from the user request that establish persistent role, constraints, and available tools for a session.

#### Systems Archetype

A recurring pattern of interacting loops that appears across many different domains and produces a characteristic behavior.

#### Target Audience Definition

An explicit statement of who a course is written for, which governs vocabulary, assumed background, and example complexity.

**Example:** Naming "professional development for educators" rather than "anyone interested" sets a usable writing standard.

#### Taxonomy Category Naming

Choosing descriptive category names that communicate their contents to a reader rather than only to the system.

#### Taxonomy Distribution

The count and percentage of ideas falling into each category, used to detect imbalance.

#### taxonomy-distribution.py

The program that counts ideas per category and writes a distribution report, flagging categories that exceed the share threshold.

#### taxonomy-names.json File

The mapping from short category abbreviations to human-readable names, required so reports and diagram legends display meaningful labels.

**Example:** Without it, a legend shows `LGRAPH` instead of "Learning Graphs".

#### TaxonomyID

A short uppercase abbreviation identifying a category, used in the data files and as the group key in a rendered diagram.

#### Technical Metadata Section

The part of a simulation's descriptive record holding framework, dimensions, dependencies, and accessibility information.

#### Template Files in Skills

Prewritten starter files a skill copies into a project and then customizes, avoiding regeneration of boilerplate.

#### Term Extraction

Identifying the vocabulary requiring definition, drawn from an enumerated idea list and from wording used across the written material.

#### Terminal Commands

Text instructions typed at a command-line shell to run programs, inspect files, and manage a project.

#### Terminal Node

A teachable idea that has prerequisites but that nothing else depends on, representing a natural endpoint of a route.

#### Text Input Control

An interface element accepting typed values, used where a reader supplies a number or short string.

#### Text Rendering in Images

The capability of an image generator to draw legible, exact wording inside a picture, which makes designed posters feasible and mistakes permanent.

#### Text-to-Image Model

A generative system that produces a picture from a written description, including modern systems able to place specified text accurately within a complex composition.

#### Text-to-Speech Narration

Generated spoken audio of written material, offering an alternative to reading.

#### Textbook Generation Pipeline

The ordered sequence of steps that turns a course description into a published book, passing through concepts, structure, content, media, and deployment.

#### Textbook Scaffold

The initial project structure created for a new book, including configuration, directory layout, and starter pages.

#### Thirty Skill Loading Limit

The practical ceiling on how many skills an agent can keep available at once, which forces related skills to be consolidated.

#### Title Case Convention

The capitalization rule applying initial capitals to principal words, used for consistency across labels and headings.

#### TODO Backlog Generation

Producing a consolidated list of outstanding work items across a project from automated assessments.

#### Token

The smallest unit of text a language model processes, roughly equivalent to a short word or word fragment. Model cost and capacity are measured in tokens rather than words.

**Example:** The phrase "learning graph" is typically three or four tokens, not two words.

#### Token Budget

A planned allowance of tokens for a task or a period, treated as a limited resource to be spent deliberately.

**Example:** Allocating most of a session's allowance to chapter prose and little to repeated validation runs.

#### Token Cost Estimation

Predicting the consumption of a planned task from measured rates, so an author knows the price before committing.

#### Token Cost Model

An understanding of what drives consumption — content read, content generated, and overhead paid per agent — used to predict expense before work begins.

#### Token Cost Per Term

The average consumption attributable to each glossary entry, useful for estimating the cost of a glossary of any size.

#### Token Frugality Principle

The design rule that a workflow should produce required quality at the lowest token cost, so authors on inexpensive plans can complete a book.

#### Token Management Strategies

The collected techniques for controlling consumption: file separation, script substitution, gate short-circuiting, and selective reading.

#### Token Usage Dashboard

A generated report that presents consumption and duration per skill so expensive steps can be identified.

#### Token Waste Antipatterns

Recurring practices that consume tokens without improving results, such as unnecessary parallel agents or manual assembly of sortable data.

**Example:** Emitting a sorted glossary through repeated edit calls instead of sorting it with three lines of code.

#### Tokenization

The process of splitting raw text into the discrete units a language model consumes. The chosen split determines how much of a document fits into a fixed budget.

#### Tokens Per Minute Limit

A cap on throughput, distinct from a total allowance, that governs how quickly work may proceed.

#### Tool Use by Agents

The mechanism by which a model requests actions in the outside world — reading a file, running a command, searching the web — and receives the results as new input.

#### Topics Excluded From Scope

An explicit list of subjects a course does not address, preventing generated material from drifting beyond its intended boundary.

**Example:** Declaring that model training is out of scope stops chapters from expanding into machine learning theory.

#### Trigger Keyword Table

An explicit mapping from request phrases to the action or guide that should handle them, making routing decisions predictable.

**Example:** The words "timeline" and "chronological" route a request to the timeline generator rather than the chart generator.

#### trim-padding-from-image.py

The program that removes surrounding blank space from a picture so it aligns correctly when placed.

#### Understand Level

The cognitive category covering construction of meaning, expressed by actions such as explaining, summarizing, and classifying.

#### update-mkdocs-nav.py Script

The program that inserts newly created pages into the site menu, ensuring generated content is reachable.

#### URL Verification

Confirming that a cited web address resolves and contains the material attributed to it.

#### validate-learning-graph.py

The program that checks a generated graph file against its formal schema and reports any structural violation.

#### validate-sims.py Script

The program that checks simulations against structural standards and reports violations.

#### Vendor Extension Fields

Metadata keys outside the published specification, added by a particular platform. Some clients ignore them and some reject them outright.

**Example:** A `model:` key is understood by one platform and may cause a hard error on another.

#### Venn Diagram Generator

The route that produces overlapping-set illustrations showing shared and exclusive membership between categories.

#### Verbatim Text Prompt

An image instruction requiring that supplied wording be reproduced exactly, with no paraphrase or substitution.

#### Verbose Output Mode

An option that makes a program report its intermediate steps, used for diagnosis.

#### Verified Infographic Pipeline

A staged process producing a factual poster in which claims are planned, sourced, verified, and locked before a single image is generated, and the result is audited afterward.

#### Version Control Basics

The practice of recording successive states of a project so any prior state can be recovered and any change can be attributed.

**Example:** A regenerated glossary can be compared against the previous version to confirm exactly which definitions changed.

#### Virtual Environment

An isolated Python installation for a single project, preventing its dependencies from conflicting with those of other projects.

#### vis-network JSON Format

The specific arrangement of nodes, edges, and groups expected by the JavaScript library that renders an interactive diagram.

#### vis-network Library

A JavaScript library that renders nodes and connecting arrows as an interactive diagram with physics-based layout.

#### vis-timeline Library

A JavaScript library that renders dated events along a navigable horizontal axis.

#### Visual Layout Review

Inspecting a rendered simulation for presentation defects such as overlapping elements, clipped labels, or controls positioned off-screen.

#### Visual Studio Code

A source code editor with integrated terminal, extension support, and file navigation, commonly used for authoring textbook content.

#### Visualization Library Routing

Selecting the rendering technology best matched to a request, based on the kind of data and interaction described.

**Example:** Chronological events route to a timeline library while node relationships route to a network library.

#### Voltage and Current Scope

A display panel plotting electrical quantities over time alongside a simulated circuit.

#### VS Code Terminal

A command-line shell embedded in the editor window, allowing commands to be run without leaving the authoring environment.

#### Wikimedia Commons Sourcing

Obtaining reusable illustrations and photographs from a large repository of openly licensed media.

#### Wikipedia as a Source

Use of an encyclopedic reference as a reliable starting point, placed before specialized sources in a citation list.

#### Word Count Metric

The total quantity of written text in a book, used as a basic measure of scale.

#### Worked Examples

Fully solved illustrations that show each step of a procedure, used to build competence before independent practice.

#### Writing a Skill Description

Composing the summary that determines when a skill activates, stating both what it does and the situations that should invoke it.

**Example:** Naming concrete trigger phrases such as "breadboard" and "wiring diagram" makes activation dependable.

#### YAML Frontmatter

A block of key-value metadata at the start of a file, delimited by triple dashes, that carries structured information separate from the body.
