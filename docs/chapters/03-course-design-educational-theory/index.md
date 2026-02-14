# Course Design and Educational Theory

## Summary

This chapter focuses on the educational foundations that underpin effective intelligent textbook creation. You'll learn how to develop comprehensive course descriptions that include target audience definitions, prerequisites, main topics, and explicitly excluded topics. The chapter provides in-depth coverage of Bloom's Taxonomy (2001 revision), exploring all six cognitive levels from Remember through Create.

You'll learn to write measurable learning outcomes using appropriate action verbs aligned with each cognitive level. The chapter also covers how to assess course description quality using scoring rubrics, ensuring your textbook projects start with a solid educational foundation.

## Concepts Covered

This chapter covers the following 17 concepts from the learning graph:

1. Course Description
2. Target Audience Definition
3. Course Prerequisites
4. Main Topics Covered
5. Topics Excluded from Course
6. Learning Outcomes
7. Bloom's Taxonomy
8. Bloom's 2001 Revision
9. Remember (Cognitive Level 1)
10. Understand (Cognitive Level 2)
11. Apply (Cognitive Level 3)
12. Analyze (Cognitive Level 4)
13. Evaluate (Cognitive Level 5)
14. Create (Cognitive Level 6)
15. Action Verbs for Learning Outcomes
16. Course Description Quality Score
17. Assessing Course Descriptions

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction to AI and Intelligent Textbooks](../01-intro-ai-intelligent-textbooks/index.md)

---

## Crafting Effective Course Descriptions

A course description serves as the foundational document for intelligent textbook development, defining scope, audience, learning outcomes, and conceptual boundaries. In the context of AI-assisted content generation, the course description provides the essential context that skills like learning-graph-generator use to enumerate concepts, map dependencies, and structure pedagogical sequencing.

Well-crafted course descriptions exhibit several key characteristics that enable effective automated content generation:

**Specificity:** Rather than vague statements like "students will learn about databases," effective descriptions enumerate specific topics: "students will learn graph database architectures, Cypher query language, and ACID transaction models."

**Completeness:** All required metadata elements present—target audience, prerequisites, main topics, excluded topics, and learning outcomes aligned with established taxonomies.

**Contextual clarity:** Sufficient background information for AI systems to understand domain conventions, terminology standards, and pedagogical approaches appropriate for the subject matter.

**Outcome focus:** Learning objectives stated as measurable, demonstrable competencies rather than aspirational goals.

For intelligent textbook projects, the course description quality directly impacts downstream artifacts. A comprehensive, well-structured course description enables the learning-graph-generator skill to produce 200+ relevant concepts with accurate dependencies, while an underspecified description yields generic or off-target concept graphs requiring extensive manual correction.

#### Diagram: Course Description Quality Impact on Workflow

<iframe src="../../sims/course-description-quality-workflow/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
    <summary>Course Description Quality Impact on Workflow</summary>
    Type: workflow

    Purpose: Show how course description quality affects subsequent skill outputs

    Visual style: Flowchart with quality branching

    Steps:
    1. Start: "Course Description Created"

    2. Decision: "Quality Score ≥ 70?"
       Hover text: "Assessed using course-description-analyzer skill"

    3a. High Quality Path (Score ≥ 70):
        - Process: "Learning graph generation"
          Hover text: "200 relevant concepts with accurate dependencies"
        - Process: "Glossary generation"
          Hover text: "Precise definitions aligned with concepts"
        - Process: "Chapter structure"
          Hover text: "Logical sequencing respecting prerequisites"
        - Result: "High-quality textbook with minimal manual correction"

    3b. Low Quality Path (Score < 70):
        - Process: "Learning graph generation"
          Hover text: "Generic or off-target concepts, unclear dependencies"
        - Process: "Manual correction required"
          Hover text: "Significant effort to refine concepts and relationships"
        - Process: "Regenerate downstream artifacts"
          Hover text: "Glossary, chapters must be redone with corrected graph"
        - Result: "Extended development time, inconsistent quality"

    Annotations:
    - "Investing time in course description quality pays exponential dividends"
    - "Quality threshold: 70+ for acceptable, 85+ for excellent"

    Color coding:
    - Green: High-quality path
    - Orange: Low-quality path requiring rework
    - Blue: Assessment and decision points

    Implementation: SVG flowchart with parallel quality paths

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (Score: 95/100) - Perfect for workflow/flowchart showing branching quality paths with decision points and parallel outcomes
2. microsim-p5 (Score: 65/100) - Could create custom flowchart with color-coded paths but Mermaid excels at this
3. vis-network (Score: 35/100) - Could show as network but flowchart structure is more appropriate
</details>

### Target Audience Definition

Defining the target audience establishes critical constraints for content generation including reading level, assumed background knowledge, professional context, and motivational framing.

Effective target audience definitions address:

**Educational level:** Junior high, senior high, college undergraduate, graduate (master's/PhD), professional development. This determines sentence complexity, vocabulary choices, and explanation depth as detailed in the reading level reference.

**Professional context:** Are learners students, working professionals, career changers, or hobbyists? Professional learners may need practical application emphasis, while academic contexts can explore theoretical depth.

**Prior knowledge baseline:** What concepts can be assumed as understood versus requiring explicit introduction? For a graph database course targeting software developers, relational database knowledge might be assumed; for data scientists, statistical concepts but not necessarily database administration.

**Learning motivation:** Are learners pursuing certification, solving specific problems, exploring new fields, or fulfilling requirements? Motivation affects example selection and application framing.

Example target audience definitions:

- **Generic (insufficient):** "Computer science students interested in databases"
- **Specific (effective):** "Graduate-level computer science students or working software engineers with 2+ years experience in relational databases, seeking to understand graph database architectures for dependency management, recommendation systems, or network analysis applications"

The specific definition enables AI to calibrate technical depth, select appropriate examples (enterprise contexts rather than academic exercises), and emphasize practical implementation alongside theoretical foundations.

### Course Prerequisites

Prerequisites define the boundary between what will be taught and what learners must already understand. For AI-assisted content generation, explicitly stated prerequisites prevent the learning graph from including foundational concepts that should be assumed.

Prerequisites should enumerate:

**Required knowledge domains:** Specific subject areas learners must have mastered, stated with sufficient granularity for AI to understand scope. "Basic programming" is vague; "variables, control flow, functions, and basic data structures (arrays, hashmaps)" is actionable.

**Skill-based requirements:** Practical abilities like "command-line interface navigation," "text editor proficiency," or "basic SQL queries."

**Tool access:** Required software, accounts, or hardware. For this course: "Anthropic Claude Pro account" is an explicit prerequisite.

**Assumed frameworks or standards:** If the course builds on specific methodologies, standards, or previous courses, state these explicitly.

Properly scoped prerequisites enable the learning-graph-generator to focus concept enumeration on course-specific topics rather than generating concepts for assumed knowledge, resulting in more relevant and appropriately scoped learning graphs.

### Main Topics Covered

The main topics section provides a structured inventory of subject matter domains the course addresses. This section directly informs concept enumeration, with each topic typically expanding into 10-20 concepts in the learning graph.

Effective topic listings exhibit:

**Hierarchical organization:** Group related topics and show relationships. Major topics (e.g., "Learning Graphs") contain subtopics (e.g., "Concept Nodes," "Dependency Edges," "DAG Validation").

**Appropriate granularity:** Topics sufficiently specific to guide concept generation but not so detailed that they become concept-level. "Graph databases" is too broad; "Neo4j administration and performance tuning" is too specific; "Graph database architectures and query patterns" strikes the right balance.

**Logical sequencing:** Present topics in a pedagogical order that respects dependencies, even though the learning graph will formalize these relationships. Early topics should be foundational, later topics build on them.

**Technical precision:** Use domain-standard terminology. In a graph database course, "Cypher query language" rather than "graph querying"; in this course, "Bloom's Taxonomy 2001 revision" rather than "learning objectives."

The course description for this intelligent textbooks course provides an exemplar with 25+ main topics ranging from foundational (Claude Skills architecture) through intermediate (learning graphs) to advanced (MicroSim development), demonstrating appropriate scope and progression.
#### Diagram: Topic-to-Concept Expansion Example

<iframe src="../../sims/topic-to-concept-expansion-example/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
    <summary>Topic-to-Concept Expansion Example</summary>
    Type: diagram

    Purpose: Illustrate how main topics expand into concept enumerations in learning graphs

    Components to show:
    - Main topic: "Learning Graphs" (top level)
    - Expanded concepts (second level, connected with arrows):
      1. Learning Graph
      2. Concept Nodes in Learning Graphs
      3. Dependency Edges in Learning Graphs
      4. Directed Acyclic Graph (DAG)
      5. Prerequisite Relationships
      6. Concept Dependencies
      7. Learning Pathways
      8. Graph Traversal Algorithms
      9. Topological Sorting
      10. Circular Dependency Detection
      11. Foundational vs Advanced Concepts
      12. Learning Graph Visualization
      13. Concept Granularity
      14. Atomic Concepts
      15. Concept Label Standards

    - Annotation showing "1 topic → 10-20 concepts typical expansion"
    - Visual indicators of concept dependencies (arrows between concepts)

    Layout: Mind map or tree structure

    Labels:
    - "Main Topic (from course description)"
    - "Concepts (generated by learning-graph-generator skill)"
    - "Dependencies shown as arrows"

    Visual style: Mind map with radial layout

    Color scheme: Purple for main topic, blue for foundational concepts, green for intermediate, gold for advanced

    Implementation: SVG mind map diagram

---
**MicroSim Generator Recommendations:**

1. vis-network (Score: 90/100) - Excellent for concept maps showing topic expansion into concepts with dependencies and hierarchical relationships
2. microsim-p5 (Score: 80/100) - Could create custom radial mind map with interactive expansion and color coding
3. mermaid-generator (Score: 65/100) - Could use graph diagram but less optimized for radial mind map layout
</details>

### Topics Excluded from Course

Explicitly stating what the course does NOT cover provides essential boundary-setting for concept generation, preventing scope creep and maintaining focus on defined learning objectives.

The exclusion section serves several purposes:

**Manages expectations:** Clarifies for learners what adjacent topics won't be addressed, helping them assess whether the course meets their needs.

**Constrains AI generation:** Instructs learning-graph-generator to avoid enumerating concepts in excluded domains. Without this guidance, a course on graph databases might generate concepts about relational database administration, OLAP systems, or distributed consensus algorithms that, while related, fall outside intended scope.

**Defines expertise boundaries:** Acknowledges related specializations requiring separate courses. This course excludes "advanced machine learning theory" and "general Python programming," recognizing these as distinct domains.

**Maintains depth over breadth:** By explicitly excluding tangential topics, courses can devote more depth to core topics rather than superficial survey coverage.

Example exclusion statement structure:

"While this course provides comprehensive coverage of [main topic], the following topics are explicitly out of scope: [excluded topic 1] (rationale), [excluded topic 2] (rationale), [excluded topic 3] (rationale)."

For AI interpretation, exclusions function as negative constraints: "do NOT generate concepts related to X." This prevents the 200-concept budget from being diluted with out-of-scope material.

## Understanding Learning Outcomes

Learning outcomes articulate specific, measurable competencies learners will demonstrate upon course completion. Unlike general objectives ("understand graph databases"), learning outcomes specify cognitive levels, action verbs, and assessment contexts following established educational frameworks.

For AI-assisted textbook development, learning outcomes serve multiple critical functions:

**Guide content generation:** Chapter content generation skills reference learning outcomes to ensure explanations, examples, and practice opportunities align with intended cognitive levels.

**Inform assessment design:** Quiz-generator skill uses learning outcomes to distribute questions across Bloom's Taxonomy levels, ensuring assessments measure intended competencies.

**Structure concept dependencies:** Learning graph concept labeling and sequencing respect the progression from lower-order (Remember, Understand) to higher-order (Analyze, Evaluate, Create) cognitive demands.

**Quality validation:** Course description analyzers assess whether learning outcomes cover multiple cognitive levels, use appropriate action verbs, and align with target audience sophistication.

Well-crafted learning outcomes exhibit the SMART criteria: Specific, Measurable, Achievable, Relevant, Time-bound. In educational contexts, "measurable" typically means "demonstrable through assessment"—learners can prove competency acquisition.

## Bloom's Taxonomy: Foundation for Learning Outcomes

Bloom's Taxonomy provides a hierarchical framework for categorizing cognitive learning objectives from basic recall through creative synthesis. Originally developed in 1956 and substantively revised in 2001, the taxonomy enables systematic design of learning experiences progressing from simple to complex cognitive demands.

The 2001 revision—which this course uses exclusively—reorganized the taxonomy from nouns to verbs, reflecting cognitive processes rather than knowledge categories. This verb-based framework aligns naturally with learning outcome statements and action-oriented skill development.

### The 2001 Revision: From Nouns to Verbs

The original 1956 Bloom's Taxonomy categorized learning into six noun-based levels: Knowledge, Comprehension, Application, Analysis, Synthesis, and Evaluation. The 2001 revision restructured these as cognitive process dimensions using verbs:

| Original (1956) | Revised (2001) | Shift in Emphasis |
|---|---|---|
| Knowledge | Remember | From passive possession to active retrieval |
| Comprehension | Understand | From static grasp to dynamic construction of meaning |
| Application | Apply | Unchanged - executing procedures |
| Analysis | Analyze | From breaking down to determining relationships |
| Synthesis | Create | Moved to top, emphasizing generative processes |
| Evaluation | Evaluate | From top to second-highest, clarifying as critical judgment |

The verb-based framework better aligns with outcome statements: "Students will analyze dependency graphs" (2001) versus "Students will demonstrate analysis of dependency graphs" (1956 phrasing). The active voice clarifies what learners do to demonstrate competency.

For AI-assisted content generation, the verb-based taxonomy enables more precise prompt engineering. Skills can be instructed to "generate examples requiring learners to evaluate trade-offs" rather than the less actionable "create evaluation content."
#### Diagram: Bloom's Taxonomy 1956 vs 2001 Comparison

<iframe src="../../sims/bloom-s-taxonomy-1956-vs-2001-comparison/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->

<details markdown="1">
    <summary>Bloom's Taxonomy 1956 vs 2001 Comparison</summary>
    Type: diagram

    Purpose: Show the structural differences between original and revised taxonomies

    Components to show (side-by-side pyramids):

    Left pyramid (1956 version):
    - Evaluation (top)
    - Synthesis
    - Analysis
    - Application
    - Comprehension
    - Knowledge (bottom)

    Right pyramid (2001 version):
    - Create (top)
    - Evaluate
    - Analyze
    - Apply
    - Understand
    - Remember (bottom)

    Arrows showing transformations:
    - Knowledge → Remember
    - Comprehension → Understand
    - Synthesis → Create (moved to top)
    - Evaluation → Evaluate (moved down one level)

    Labels:
    - "Original: Noun-based knowledge categories"
    - "Revised: Verb-based cognitive processes"
    - Annotation: "Create elevated to highest level, emphasizing generative thinking"

    Visual style: Two pyramids side-by-side with transformation arrows

    Color scheme: Red gradient for 1956, rainbow gradient (red to purple) for 2001

    Implementation: SVG diagram with pyramid shapes

---
**MicroSim Generator Recommendations:**

1. microsim-p5 (Score: 88/100) - Best for side-by-side pyramid comparison with transformation arrows and gradient coloring
2. chartjs-generator (Score: 50/100) - Could use stacked bar charts but pyramids better convey hierarchical metaphor
3. mermaid-generator (Score: 45/100) - Could show as diagrams but lacks pyramid-specific styling
</details>

## The Six Cognitive Levels

The 2001 Bloom's Taxonomy organizes cognitive processes into six hierarchical levels, each building on the capabilities of lower levels. Understanding these levels is essential for designing learning outcomes, structuring content progression, and creating assessments that measure intended competencies.

### Remember (Cognitive Level 1)

**Remember** encompasses retrieving relevant knowledge from long-term memory, including recognizing and recalling factual information, concepts, procedures, and principles.

**Cognitive processes:**
- **Recognizing:** Identifying information when presented (e.g., "Identify which of the following are valid Cypher queries")
- **Recalling:** Retrieving information from memory without prompts (e.g., "List the five levels of textbook intelligence")

**Characteristic action verbs:**
Define, list, recall, recognize, identify, name, state, describe, label, match, select

**Example learning outcomes:**
- "Remember the steps in creating an intelligent textbook"
- "Remember what a learning graph is"
- "Recall the required fields in SKILL.md frontmatter"
- "Identify components of the transformer architecture"

**Assessment approaches:**
- Multiple-choice questions with single correct answers
- Fill-in-the-blank factual recall
- Matching terms to definitions
- True/false statements about facts

**Content generation implications:**
Remember-level content includes definitions, lists of components, procedural steps stated explicitly, and terminology introduction. Examples should be straightforward instantiations of concepts without requiring inference or application.

### Understand (Cognitive Level 2)

**Understand** involves constructing meaning from instructional messages, including oral, written, and graphic communication. Learners demonstrate understanding by explaining concepts in their own words, classifying examples, summarizing key ideas, and making comparisons.

**Cognitive processes:**
- **Interpreting:** Converting information from one form to another (e.g., "Explain the transformer architecture in your own words")
- **Exemplifying:** Providing instances of concepts (e.g., "Give an example of a Level 3 intelligent textbook feature")
- **Classifying:** Determining category membership (e.g., "Categorize these concepts as foundational or advanced")
- **Summarizing:** Abstracting general themes (e.g., "Summarize the differences between skills and commands")
- **Inferring:** Drawing logical conclusions (e.g., "What would happen if a learning graph contained circular dependencies?")
- **Comparing:** Detecting correspondences (e.g., "Compare graph database and relational database approaches to relationship queries")
- **Explaining:** Constructing cause-and-effect models (e.g., "Explain how self-attention enables transformers to capture long-range dependencies")

**Characteristic action verbs:**
Explain, summarize, paraphrase, classify, categorize, compare, contrast, interpret, exemplify, illustrate, infer, predict

**Example learning outcomes:**
- "Understand how skills are used in textbook creation workflows"
- "Explain how a learning graph guides students on their learning journey"
- "Compare and contrast MicroSims and static diagrams"
- "Summarize the five levels of textbook intelligence"

**Assessment approaches:**
- Explanation questions requiring learners to describe concepts
- Classification tasks sorting items into categories
- Comparison questions identifying similarities and differences
- Prediction questions applying conceptual understanding to new scenarios

**Content generation implications:**
Understand-level content provides explanations with multiple representations (text, diagrams, examples), offers varied examples showing concept breadth, uses analogies connecting new concepts to familiar ones, and includes conceptual questions prompting learners to construct meaning.

### Apply (Cognitive Level 3)

**Apply** involves carrying out or using a procedure in a given situation. Application can be routine (using familiar procedures in standard contexts) or novel (adapting procedures to new situations).

**Cognitive processes:**
- **Executing:** Performing routine procedures (e.g., "Use the learning-graph-generator skill to create a concept graph")
- **Implementing:** Applying procedures to unfamiliar tasks (e.g., "Adapt the quiz-generator skill to create case study questions")

**Characteristic action verbs:**
Apply, execute, implement, use, carry out, solve, demonstrate, operate, employ, practice, construct (when following procedures)

**Example learning outcomes:**
- "Apply prompt engineering principles to create a new skill"
- "Use the course-description-analyzer to assess quality"
- "Implement MkDocs navigation for a new textbook"
- "Execute the complete intelligent textbook workflow"

**Assessment approaches:**
- Hands-on tasks requiring procedure execution
- Problem-solving requiring application of learned methods
- Case studies where learners apply concepts to realistic scenarios
- Implementation projects creating artifacts using taught techniques

**Content generation implications:**
Apply-level content includes worked examples with step-by-step execution, practice opportunities with varied scenarios, procedural guidance adaptable to contexts, and scaffolded problem-solving transitioning from guided to independent application.
#### Diagram: Lower-Order vs Higher-Order Thinking Skills

<iframe src="../../sims/lower-order-vs-higher-order-thinking-skills/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Lower-Order vs Higher-Order Thinking Skills</summary>
    Type: diagram

    Purpose: Show the division between lower-order (Remember, Understand, Apply) and higher-order (Analyze, Evaluate, Create) cognitive skills

    Components to show:
    - Pyramid divided horizontally at the middle
    - Lower half (shaded blue): Remember, Understand, Apply
    - Upper half (shaded gold): Analyze, Evaluate, Create
    - Label: "Lower-Order Thinking Skills (LOTS)"
    - Label: "Higher-Order Thinking Skills (HOTS)"
    - Annotations showing:
      - LOTS: Focus on knowledge acquisition and application
      - HOTS: Focus on critical thinking and creation

    Additional info boxes:
    - LOTS: "Essential foundation, but insufficient for mastery"
    - HOTS: "Demonstrate deeper learning, critical for professional competence"
    - Educational research note: "Well-designed courses include 60-70% HOTS outcomes"

    Visual style: Pyramid with horizontal division

    Color scheme: Blue for LOTS, gold for HOTS, gradient transition at boundary

    Implementation: SVG pyramid diagram with annotation boxes

---
**MicroSim Generator Recommendations:**

1. microsim-p5 (Score: 85/100) - Excellent for pyramid with horizontal division, gradient coloring, and annotation boxes for LOTS/HOTS
2. chartjs-generator (Score: 55/100) - Could use stacked bar but pyramid metaphor is more appropriate
3. mermaid-generator (Score: 40/100) - Could create diagram but lacks pyramid-specific layout
</details>

### Analyze (Cognitive Level 4)

**Analyze** involves breaking material into constituent parts and determining how parts relate to one another and to an overall structure or purpose. Analysis enables learners to distinguish relevant from irrelevant information, identify organizational principles, and recognize unstated assumptions.

**Cognitive processes:**
- **Differentiating:** Distinguishing relevant from irrelevant parts (e.g., "Identify which concepts in this list are foundational versus advanced")
- **Organizing:** Determining how elements fit within a structure (e.g., "Organize these concepts into a dependency graph showing prerequisite relationships")
- **Attributing:** Determining point of view or purpose (e.g., "Analyze why the learning-graph-generator produces 200 concepts rather than 50 or 500")

**Characteristic action verbs:**
Analyze, differentiate, distinguish, organize, integrate, structure, attribute, deconstruct, categorize (with reasoning), compare (with detailed structural analysis)

**Example learning outcomes:**
- "Analyze the result of a skill execution to identify quality issues"
- "Differentiate between situations requiring skills versus commands"
- "Organize course topics into logical chapter groupings"
- "Determine why a learning graph contains circular dependencies"

**Assessment approaches:**
- Case analysis identifying underlying patterns or principles
- Diagramming relationships among concepts
- Debugging tasks requiring identification of error sources
- Critical reading identifying assumptions or biases
- Dependency analysis tasks

**Content generation implications:**
Analyze-level content presents complex scenarios requiring decomposition, provides frameworks for systematic analysis, includes examples with hidden structure for learners to uncover, and offers guided analysis with scaffolding gradually removed.

### Evaluate (Cognitive Level 5)

**Evaluate** involves making judgments based on criteria and standards through checking and critiquing. Evaluation includes both judging internal consistency (checking) and judging based on external criteria (critiquing).

**Cognitive processes:**
- **Checking:** Testing for inconsistencies or fallacies (e.g., "Verify that all concepts in the learning graph follow title case convention")
- **Critiquing:** Judging based on external standards (e.g., "Assess whether this chapter content meets quality standards for graduate-level reading")

**Characteristic action verbs:**
Evaluate, judge, critique, assess, appraise, rate, verify, validate, test, measure, recommend, justify

**Example learning outcomes:**
- "Evaluate the quality of a course description against established criteria"
- "Assess whether a learning graph contains appropriate concept granularity"
- "Critique a chapter's interactive element integration"
- "Validate that quiz questions align with Bloom's Taxonomy levels"

**Assessment approaches:**
- Rubric-based evaluation of artifacts
- Peer review with justification of judgments
- Quality assessment against standards
- Recommendation tasks requiring justified decisions
- Editorial review identifying improvements

**Content generation implications:**
Evaluate-level content provides explicit criteria and rubrics, models evaluation processes with reasoning visible, presents work samples for learners to critique, and requires justification of judgments connecting evidence to standards.

### Create (Cognitive Level 6)

**Create** involves putting elements together to form a coherent or functional whole, reorganizing elements into a new pattern or structure. Creation requires originality and is the most cognitively complex level, building on all lower levels.

**Cognitive processes:**
- **Generating:** Hypothesizing based on criteria (e.g., "Propose alternative approaches to concept dependency mapping")
- **Planning:** Designing a procedure to accomplish a task (e.g., "Design a complete intelligent textbook project including timeline and skill sequencing")
- **Producing:** Inventing a product (e.g., "Develop a new skill for generating learning pathway visualizations")

**Characteristic action verbs:**
Create, design, construct, develop, formulate, author, generate, plan, produce, invent, devise, compose

**Example learning outcomes:**
- "Create new skills from scratch for specialized workflows"
- "Design and implement a complete intelligent textbook project"
- "Develop custom commands for project-specific tasks"
- "Construct a learning graph for a novel subject domain"

**Assessment approaches:**
- Project-based assessment requiring original artifacts
- Design challenges with multiple valid solutions
- Portfolio development demonstrating creative synthesis
- Capstone projects integrating multiple competencies
- Open-ended problems requiring innovative approaches

**Content generation implications:**
Create-level content provides open-ended challenges, offers frameworks and constraints fostering structured creativity, showcases examples of creative work highlighting key features, and scaffolds complex production through phase-wise guidance.
#### Diagram: Bloom's Taxonomy Application Distribution in Quality Courses

<iframe src="../../sims/bloom-s-taxonomy-application-distribution-in-quality-courses/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Bloom's Taxonomy Application Distribution in Quality Courses</summary>
    Type: chart

    Chart type: Horizontal stacked bar chart

    Purpose: Show recommended distribution of learning outcomes across cognitive levels

    Data (percentage of learning outcomes by level):
    - Remember: 10%
    - Understand: 20%
    - Apply: 25%
    - Analyze: 20%
    - Evaluate: 15%
    - Create: 10%

    Title: "Recommended Learning Outcome Distribution for Graduate-Level Courses"

    Bar segments:
    - Each cognitive level shown as different color segment
    - Percentages labeled within segments
    - Total sums to 100%

    Annotations:
    - Bracket grouping Remember+Understand+Apply: "45% Lower-order (foundational)"
    - Bracket grouping Analyze+Evaluate+Create: "45% Higher-order (mastery)"
    - Note: "Distribution should match target audience sophistication"

    Color scheme: Rainbow gradient from red (Remember) to purple (Create)

    Implementation: Chart.js horizontal stacked bar chart

---
**MicroSim Generator Recommendations:**

1. chartjs-generator (Score: 98/100) - Perfect for horizontal stacked bar chart showing percentage distribution across taxonomy levels - Chart.js explicitly mentioned
2. microsim-p5 (Score: 55/100) - Could create custom stacked bar but Chart.js already provides this
3. bubble-chart-generator (Score: 15/100) - Not comparing across two dimensions, just showing distribution
</details>

## Action Verbs for Learning Outcomes

Selecting appropriate action verbs for learning outcome statements ensures outcomes are measurable, aligned with cognitive levels, and actionable for assessment design. Each Bloom's Taxonomy level has characteristic verbs that signal the intended cognitive process.

**Verb selection principles:**

**Measurability:** Choose verbs describing observable behaviors. Avoid vague verbs like "know," "appreciate," or "believe" that don't specify demonstrable actions.

**Level alignment:** Ensure verb matches intended cognitive level. "List" signals Remember level; "compare" signals Understand level; "critique" signals Evaluate level.

**Assessment clarity:** Verb should clarify how competency will be measured. "Design" implies creating an artifact for evaluation; "explain" implies written or oral explanation.

**Specificity:** More specific verbs provide clearer guidance. "Classify concepts by taxonomy category" is clearer than "understand concept categories."

**Verb lists by cognitive level:**

**Remember:** Define, list, recall, recognize, identify, name, state, describe, label, match, select, memorize, repeat, retrieve

**Understand:** Explain, summarize, paraphrase, classify, categorize, compare, contrast, interpret, exemplify, illustrate, infer, predict, discuss, translate, convert

**Apply:** Apply, execute, implement, use, carry out, solve, demonstrate, operate, employ, practice, calculate, construct, modify, prepare, produce

**Analyze:** Analyze, differentiate, distinguish, organize, integrate, structure, attribute, deconstruct, diagram, outline, relate, subdivide, examine

**Evaluate:** Evaluate, judge, critique, assess, appraise, rate, verify, validate, test, measure, recommend, justify, argue, defend, support

**Create:** Create, design, construct, develop, formulate, author, generate, plan, produce, invent, devise, compose, compile, organize (into new structure)

When crafting learning outcomes, pair action verbs with appropriate objects and conditions:

- **Basic:** "Students will create skills" (action + object)
- **Better:** "Students will create new Claude Skills from scratch for specialized educational content workflows" (action + specific object + context)

The enhanced version clarifies what type of skill, the level of originality expected ("from scratch"), and the domain context ("educational content workflows"), providing much clearer guidance for both learners and assessment designers.

## Course Description Quality Scoring

Assessing course description quality systematically ensures sufficient detail and completeness for effective learning graph generation and downstream content creation. The course-description-analyzer skill provides automated quality assessment using a rubric-based approach.

**Quality dimensions and scoring:**

**Target Audience Definition (0-15 points):**
- 0-5: Generic or missing
- 6-10: Educational level specified, some context
- 11-15: Detailed audience with level, background, motivation, professional context

**Prerequisites (0-15 points):**
- 0-5: None stated or vague ("basic knowledge")
- 6-10: General prerequisites listed
- 11-15: Specific, granular prerequisites with clear scope

**Main Topics (0-20 points):**
- 0-7: Fewer than 10 topics or very vague
- 8-14: 10-20 topics with moderate specificity
- 15-20: 20+ topics, technically precise, well-organized

**Topics Excluded (0-10 points):**
- 0-3: No exclusions stated
- 4-7: Some exclusions but vague
- 8-10: Explicit exclusions with rationale

**Learning Outcomes (0-40 points):**
- 0-10: Missing or not aligned with Bloom's Taxonomy
- 11-25: Some outcomes, limited cognitive level coverage
- 26-35: Outcomes covering 4+ Bloom's levels with appropriate verbs
- 36-40: Comprehensive outcomes covering all 6 levels, well-distributed, measurable

**Total score interpretation:**
- 90-100: Excellent - ready for learning graph generation
- 70-89: Good - minor improvements recommended
- 50-69: Acceptable - significant improvements needed
- <50: Insufficient - major revision required before proceeding

Courses scoring below 70 should be revised before invoking learning-graph-generator, as quality deficiencies in the course description propagate through all downstream artifacts.
#### Diagram: Course Description Quality Rubric Visualization

<iframe src="../../sims/course-description-quality-rubric-visualization/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Course Description Quality Rubric Visualization</summary>
    Type: infographic

    Purpose: Present the quality scoring rubric in visual, interactive format

    Layout: Circular dashboard with five segments (one per quality dimension)

    Segments:
    1. Target Audience (15 points max) - Blue segment
    2. Prerequisites (15 points max) - Purple segment
    3. Main Topics (20 points max) - Green segment
    4. Exclusions (10 points max) - Orange segment
    5. Learning Outcomes (40 points max) - Gold segment

    Visual representation:
    - Each segment shows point value
    - Radial fill indicates score level (empty=0, full=max)
    - Color intensity indicates quality tier
    - Center displays total score and quality rating

    Interactive elements:
    - Hover over segment to see detailed rubric for that dimension
    - Click segment to expand with improvement recommendations
    - Central score updates dynamically if used as assessment tool

    Quality tiers:
    - 90-100: Excellent (dark green background)
    - 70-89: Good (light green background)
    - 50-69: Acceptable (yellow background)
    - <50: Insufficient (red background)

    Implementation: HTML/CSS/JavaScript with SVG circular dashboard

---
**MicroSim Generator Recommendations:**

1. microsim-p5 (Score: 92/100) - Excellent for custom circular dashboard with radial segments, interactive hover, and dynamic scoring visualization
2. chartjs-generator (Score: 75/100) - Could use radar/polar chart for quality dimensions but circular dashboard is more custom
3. mermaid-generator (Score: 25/100) - Not designed for circular dashboards or interactive scoring visualizations
</details>

### Assessing Course Descriptions

The process of evaluating course description quality combines automated analysis (via course-description-analyzer skill) with human judgment for pedagogical appropriateness.

**Automated assessment workflow:**

1. **Extract components:** Parse course description markdown to identify target audience, prerequisites, topics, exclusions, and learning outcomes sections
2. **Count and categorize:** Enumerate topics (should be 20+), count learning outcomes by Bloom's level
3. **Verb analysis:** Validate that learning outcomes use appropriate action verbs aligned with cognitive levels
4. **Bloom's distribution:** Calculate percentage of outcomes at each level, flag if concentrated in lower levels
5. **Completeness check:** Verify all required sections present
6. **Generate score:** Apply rubric, sum dimension scores, classify into quality tiers

**Human judgment considerations:**

- **Domain appropriateness:** Are topics relevant to stated subject matter?
- **Pedagogical progression:** Do topics build logically from foundational to advanced?
- **Audience alignment:** Do prerequisites and outcomes match stated audience sophistication?
- **Assessment feasibility:** Are learning outcomes actually measurable given typical assessment constraints?

**Common quality issues and remediation:**

| Issue | Remediation |
|-------|-------------|
| Missing exclusions section | Add 5-10 related topics explicitly out of scope |
| Bloom's concentration in Remember/Understand | Add Analyze, Evaluate, Create outcomes |
| Vague prerequisites | Specify granular knowledge domains with examples |
| Generic target audience | Add professional context, motivation, background detail |
| Insufficient topics (<15) | Expand with subtopics, tools, frameworks, standards |

Iterative refinement typically requires 2-3 cycles to reach quality scores above 85, but the investment dramatically improves downstream content quality.

## Summary

This chapter established the educational foundations for intelligent textbook creation, focusing on course description development and Bloom's Taxonomy application. You learned how to craft comprehensive course descriptions encompassing target audience definition, prerequisites, main topics, explicit exclusions, and learning outcomes aligned with the 2001 Bloom's Taxonomy revision.

We explored the six cognitive levels—Remember, Understand, Apply, Analyze, Evaluate, Create—examining characteristic cognitive processes, action verbs, example outcomes, and assessment approaches for each level. You learned how to select appropriate action verbs for measurable learning outcomes and how to assess course description quality using rubric-based scoring.

These educational frameworks provide the foundation for learning graph generation in subsequent chapters, ensuring AI-assisted content creation produces pedagogically sound, well-structured intelligent textbooks aligned with established instructional design principles.

**Concepts covered:** Course Description ✓, Target Audience Definition ✓, Course Prerequisites ✓, Main Topics Covered ✓, Topics Excluded from Course ✓, Learning Outcomes ✓, Bloom's Taxonomy ✓, Bloom's 2001 Revision ✓, Remember (Cognitive Level 1) ✓, Understand (Cognitive Level 2) ✓, Apply (Cognitive Level 3) ✓, Analyze (Cognitive Level 4) ✓, Evaluate (Cognitive Level 5) ✓, Create (Cognitive Level 6) ✓, Action Verbs for Learning Outcomes ✓, Course Description Quality Score ✓, Assessing Course Descriptions ✓

## References

1. [Bloom's Taxonomy Revised](https://thesecondprinciple.com/essential-teaching-skills/blooms-taxonomy-revised/) - 2024 - The Second Principle - Comprehensive educational resource examining the 2001 Anderson and Krathwohl revision of Bloom's Taxonomy, comparing classic and revised frameworks with detailed definitions and performance verbs for each cognitive level, essential for writing measurable learning outcomes.

2. [The ADDIE Model Explained: Evolution, Steps, and Applications for 2025](https://research.com/education/the-addie-model) - 2025 - Research.com - Detailed analysis of the ADDIE instructional design framework (Analyze, Design, Develop, Implement, Evaluate) with historical context and modern applications, providing systematic course development methodology that complements the intelligent textbook creation workflow.
