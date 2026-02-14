# Introduction to Learning Graphs

## Summary

This chapter introduces learning graphs, a powerful tool for mapping the knowledge structure of your course. You'll learn about concept nodes, dependency edges, and how they form a Directed Acyclic Graph (DAG) that represents prerequisite relationships. The chapter explains how concept dependencies create learning pathways that guide students through material in an optimal sequence.

You'll also learn practical strategies for optimizing your Claude usage, understanding 4-hour usage windows and Claude Pro limitations, which will help you work efficiently as you generate learning graphs and other content in later chapters.

## Concepts Covered

This chapter covers the following 12 concepts from the learning graph:

1. Learning Graph
2. Concept Nodes in Learning Graphs
3. Dependency Edges in Learning Graphs
4. Directed Acyclic Graph (DAG)
5. Prerequisite Relationships
6. Concept Dependencies
7. Learning Pathways
8. 4-Hour Usage Windows
9. Claude Pro Limitations
10. Optimizing Claude Usage
11. Content Generation Process
12. Chapter Structure

## Prerequisites

This chapter builds on concepts from:

- [Chapter 1: Introduction to AI and Intelligent Textbooks](../01-intro-ai-intelligent-textbooks/index.md)

---

## What is a Learning Graph?

A learning graph is a directed graph data structure that maps the conceptual landscape of a course domain, explicitly representing concepts as nodes and prerequisite dependencies as edges. This formalization of knowledge structure enables systematic curriculum design, optimal content sequencing, and adaptive learning pathways that respect conceptual dependencies.

Unlike linear course outlines or topic lists, learning graphs capture the inherent relationships among concepts, distinguishing foundational knowledge from advanced topics and identifying prerequisite chains that must be respected for effective learning. By encoding these relationships explicitly, learning graphs enable both human instructional designers and AI systems to reason about pedagogical sequencing, identify knowledge gaps, and generate content that builds systematically from simple to complex.

For intelligent textbook creation, the learning graph serves multiple critical functions:

**Concept inventory:** Comprehensive enumeration of all concepts the course addresses, typically 150-250 concepts for a semester-length course

**Dependency specification:** Explicit prerequisite relationships determining which concepts must be understood before others

**Chapter organization foundation:** Grouping concepts into chapters that respect dependencies and maintain appropriate scope

**Content generation guide:** Informing AI skills about which concepts to cover, in what order, and with what assumed background

**Assessment alignment:** Enabling quiz and exercise generation that tests concepts learners should have mastered at each stage

The graph structure provides computational tractability—algorithms can verify the graph is a valid DAG (Directed Acyclic Graph), compute topological orderings for valid learning sequences, identify strongly connected components indicating circular dependencies that must be resolved, and calculate concept depth as a proxy for difficulty.

#### Diagram: Learning Graph Structure Visualization

<iframe src="../../sims/learning-graph-structure-visualization/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Learning Graph Structure Visualization</summary>
    Type: graph-model

    Purpose: Illustrate the node-edge structure of a learning graph with sample concepts

    Node types:
    1. Foundational Concepts (red circles, no incoming edges)
       - Example: "Artificial Intelligence"
       - Example: "Claude AI"

    2. Intermediate Concepts (orange circles, some incoming edges)
       - Example: "Large Language Models"
       - Example: "Prompt Engineering"

    3. Advanced Concepts (yellow circles, multiple incoming edges)
       - Example: "Learning Graph Generation"
       - Example: "Skill Workflow Design"

    Edge types:
    - Dependency edges (black arrows)
      - From prerequisite to dependent concept
      - Example: "Artificial Intelligence" → "Claude AI"
      - Example: "Claude AI" → "Large Language Models"
      - Example: "Large Language Models" → "Prompt Engineering"
      - Example: "Prompt Engineering" → "Skill Workflow Design"

    Sample data (subset of Chapter 1-3 concepts):
    - Artificial Intelligence (foundational)
      └─→ Claude AI (intermediate)
          ├─→ Large Language Models (intermediate)
          │   └─→ Prompt Engineering (intermediate)
          │       └─→ Learning Graph Generation (advanced)
          └─→ Claude Code Interface (intermediate)
              └─→ Claude Skill (intermediate)
                  └─→ Skill Workflow Design (advanced)

    Layout: Hierarchical top-down with foundational concepts at top

    Interactive features:
    - Hover node: Show concept description
    - Click node: Highlight all prerequisites (incoming edges) and dependents (outgoing edges)
    - Color coding by depth: foundational (red), intermediate (orange), advanced (yellow)
    - Zoom and pan controls

    Visual styling:
    - Node size proportional to number of dependents
    - Edge thickness constant
    - Clear labels on nodes

    Implementation: vis-network JavaScript library
    Canvas size: 800x600px

---
**MicroSim Generator Recommendations:**

1. vis-network (Score: 98/100) - Perfect for interactive network graph with nodes/edges, physics layout, hierarchical positioning, and hover tooltips - vis-network explicitly mentioned
2. microsim-p5 (Score: 70/100) - Could create custom network visualization but vis-network already optimized for this
3. mermaid-generator (Score: 50/100) - Could show flowchart but lacks physics-based layout and interactive graph features
</details>

## Concept Nodes in Learning Graphs

Concept nodes represent atomic knowledge units—discrete, well-defined ideas, procedures, or principles that learners must understand or demonstrate. Each node in the learning graph corresponds to a single concept with a unique identifier and human-readable label.

**Node attributes:**

**ConceptID:** Integer identifier (1 to n) uniquely identifying the concept within the graph. Sequential numbering simplifies reference but does not imply pedagogical ordering—dependency edges, not ID sequence, determine learning order.

**ConceptLabel:** Human-readable title following Title Case convention, maximum 32 characters. Labels should be precise, domain-standard terminology. Examples: "Directed Acyclic Graph (DAG)," "Bloom's Taxonomy," "MicroSim Development."

**TaxonomyID** (optional): Category identifier grouping related concepts for organizational purposes. Discussed in detail in Chapter 7.

**Concept granularity principles:**

**Atomic:** Each concept represents a single, cohesive idea. "Graph Databases" is too broad; split into "Graph Database Architecture," "Graph Query Languages," "Graph Database Use Cases."

**Assessable:** Concept should be specific enough to create targeted assessment items. Can you write a quiz question testing this concept specifically?

**Prerequisite-friendly:** Concept scope enables clear prerequisite relationships. "All of Machine Learning" cannot be a prerequisite; "Supervised Learning Basics" can.

**Terminology-aligned:** Use domain-standard terms. In educational technology, "Bloom's Taxonomy" not "Learning Objectives Framework"; in graph theory, "Directed Acyclic Graph (DAG)" not "Non-circular graph."

For this intelligent textbooks course, the learning graph contains approximately 200 concepts spanning foundational AI knowledge through advanced skill development, each meeting these granularity criteria to enable precise dependency mapping and content generation.

## Dependency Edges in Learning Graphs

Dependency edges represent prerequisite relationships: an edge from concept A to concept B indicates that learners should understand A before attempting to learn B. These directed edges encode the pedagogical ordering constraints that chapter sequencing and content generation must respect.

**Edge semantics:**

A directed edge A → B means:
- A is a prerequisite for B
- B depends on A
- A should be taught before B
- Learners must master A to understand B fully

Multiple incoming edges indicate multiple prerequisites. If edges point from A → C and B → C, learners should understand both A and B before tackling C.

**Dependency strength considerations:**

Not all dependencies are equally strong. Some relationships are absolute prerequisites (cannot understand concept B without A), while others are helpful background (B is easier with A but technically independent). For simplicity, the learning graph generator typically models only strong dependencies, accepting some pedagogical discretion in ordering concepts with weak relationships.

**Transitive dependencies:**

If A → B and B → C, then A is transitively prerequisite to C even without a direct A → C edge. Learning graph algorithms leverage transitivity to compute full prerequisite sets without requiring explicit edges for every relationship. This keeps the graph sparse and maintainable.

**Common dependency patterns:**

**Sequential chains:** A → B → C → D represents a linear learning sequence common in skill development (e.g., "Install Skill" → "List Skills" → "Invoke Skill" → "Create Custom Skill")

**Fan-in (convergence):** Multiple prerequisites converging on advanced concept (e.g., "Course Description" → "Learning Graph Generation" ← "Bloom's Taxonomy")

**Fan-out (divergence):** Foundational concept enabling multiple dependent concepts (e.g., "Claude Code Interface" → "File System Access," "Command Execution," "Context Management")
#### Diagram: Dependency Pattern Examples

<iframe src="../../sims/dependency-pattern-examples/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Dependency Pattern Examples</summary>
    Type: diagram

    Purpose: Illustrate common patterns of dependencies in learning graphs

    Patterns to show:

    1. Sequential Chain (left section):
       A → B → C → D
       Label: "Linear progression"
       Example: "Basic Skill" → "Intermediate Skill" → "Advanced Skill" → "Expert Skill"

    2. Fan-In / Convergence (center section):
       A ─┐
       B ─┤→ D
       C ─┘
       Label: "Multiple prerequisites converge"
       Example: "Course Description," "Bloom's Taxonomy," "Prompt Engineering" all point to "Learning Graph Generation"

    3. Fan-Out / Divergence (right section):
           ┌→ B
       A ──┼→ C
           └→ D
       Label: "Foundation enables multiple concepts"
       Example: "Claude Code Interface" enables "File Access," "Command Execution," "Tool Integration"

    Visual style: Clean arrow diagrams with labeled nodes

    Color scheme: Blue nodes, black arrows, green labels

    Annotations:
    - "Sequential: Common in skill acquisition"
    - "Fan-in: Advanced concepts require integration"
    - "Fan-out: Foundational concepts are highly leveraged"

    Implementation: SVG diagram with clear geometric layout

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (Score: 88/100) - Excellent for showing three common dependency patterns with clean arrow diagrams
2. microsim-p5 (Score: 75/100) - Could create custom diagrams for each pattern with geometric layouts
3. vis-network (Score: 60/100) - Could show as networks but simple pattern diagrams better served by Mermaid
</details>

## Directed Acyclic Graph (DAG) Requirement

A valid learning graph must be a Directed Acyclic Graph (DAG)—a directed graph containing no cycles. This mathematical constraint ensures a valid pedagogical ordering exists: there is some sequence in which concepts can be taught such that all prerequisites precede their dependents.

**Why DAGs are necessary:**

If the graph contained a cycle (A → B → C → A), it would imply:
- A must be learned before B
- B must be learned before C
- C must be learned before A
- Therefore A must be learned before itself—a logical impossibility

Cycles indicate errors in dependency specification that must be resolved before content generation proceeds. Common causes include:

- **Circular reasoning:** Defining A in terms of B and B in terms of A
- **Granularity mismatch:** Concepts at wrong abstraction levels creating spurious dependencies
- **Bidirectional relationships:** True bidirectional relationships (A influences B, B influences A) should be split into unidirectional dependencies based on pedagogical primacy

**DAG verification:**

The learning-graph-generator skill and quality validation scripts check for cycles using standard graph algorithms:

1. **Depth-first search (DFS):** Traverse the graph marking nodes as "visiting" and "visited"; encountering a "visiting" node indicates a back edge and therefore a cycle
2. **Topological sort:** Attempt to produce topological ordering; if impossible, cycles exist
3. **Strongly connected components:** Compute SCCs; any component with >1 node indicates a cycle

If cycles are detected, the validation report identifies the concepts involved, enabling manual resolution before proceeding with chapter generation.

**Topological ordering:**

A DAG admits at least one topological ordering—a linear sequence of concepts such that for every edge A → B, A appears before B in the sequence. This ordering provides one valid teaching sequence, though multiple valid orderings typically exist.

Chapter generation leverages topological ordering to group concepts into sequential chapters while respecting dependencies. Concepts with no incoming edges (foundational) appear in early chapters; concepts with many incoming edges (advanced, integrative) appear in later chapters.
#### Diagram: DAG vs Cyclic Graph Comparison

<iframe src="../../sims/dag-vs-cyclic-graph-comparison/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>DAG vs Cyclic Graph Comparison</summary>
    Type: diagram

    Purpose: Contrast valid DAG learning graph with invalid cyclic graph

    Components to show (side-by-side):

    Left side - Valid DAG:
    A → B → C
    A → C (additional edge showing transitive relationship is fine)
    Label: "Valid Learning Graph (DAG)"
    Annotation: "Can be ordered: A, B, C or A, C, B"
    Check mark: ✓ "Pedagogically sound"

    Right side - Invalid Cyclic Graph:
    A → B → C → A (cycle shown with circular arrow)
    Label: "Invalid Learning Graph (Contains Cycle)"
    Annotation: "Cannot be ordered: A requires A as prerequisite!"
    X mark: ✗ "Logically impossible"

    Visual style: Side-by-side comparison with clear labels

    Color scheme: Green for valid DAG, red for invalid cycle

    Implementation: SVG diagram showing both structures

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (Score: 90/100) - Great for side-by-side graph comparison showing valid DAG vs cyclic structure with clear annotations
2. vis-network (Score: 80/100) - Could show both graphs interactively with cycle highlighted, good for demonstrating invalid structure
3. microsim-p5 (Score: 70/100) - Could create custom comparison with animated cycle detection
</details>

## Prerequisite Relationships and Learning Pathways

Prerequisite relationships define the pedagogical ordering constraints that shape content sequencing. Understanding how prerequisites propagate through the graph and define valid learning pathways is essential for chapter organization and adaptive content delivery.

**Direct vs transitive prerequisites:**

- **Direct prerequisites:** Explicitly encoded edges. A → B means A is a direct prerequisite of B.
- **Transitive prerequisites:** Implied by paths through the graph. If A → B → C, then A is a transitive prerequisite of C even without edge A → C.

The full prerequisite set for concept C includes all nodes from which C is reachable via directed paths. This set defines what learners must have mastered before tackling C.

**Learning pathways:**

A learning pathway is a valid sequence of concepts respecting all prerequisite relationships. Multiple pathways typically exist from foundational to advanced concepts, offering flexibility in curriculum design.

For example, given this fragment:
```
Artificial Intelligence → Claude AI → Large Language Models
Artificial Intelligence → Prompt Engineering
Large Language Models → Learning Graph Generation
Prompt Engineering → Learning Graph Generation
```

Valid pathways to "Learning Graph Generation" include:
1. AI → Claude AI → LLMs → Learning Graph Generation
2. AI → Prompt Engineering → Learning Graph Generation (missing LLM prerequisite)
3. AI → Claude AI → LLMs → Learning Graph Generation (via Prompt Engineering also)

The existence of multiple pathways enables curriculum designers to emphasize different aspects—a theoretically-oriented course might emphasize the LLM pathway, while a practitioner-oriented course might emphasize prompt engineering.

**Adaptive sequencing:**

For Level 4-5 intelligent textbooks implementing adaptive content, learning pathways enable dynamic prerequisite checking. Before presenting concept C, assess whether learner has demonstrated mastery of prerequisite concepts in C's full prerequisite set. If gaps exist, recommend remediating those prerequisites before advancing.

This prerequisite-aware adaptation ensures learners don't encounter content requiring background they haven't yet developed, reducing confusion and improving learning efficiency.

## Concept Dependencies in Practice

Mapping concept dependencies is the most cognitively demanding aspect of learning graph creation. This process requires deep domain expertise to identify which relationships are true prerequisites versus merely related topics.

**Dependency identification heuristics:**

**Definitional dependencies:** If concept B's definition references concept A, A is likely prerequisite to B. "Directed Acyclic Graph" definition references "directed graph"; therefore "Directed Graph" → "Directed Acyclic Graph."

**Procedural dependencies:** If procedure B requires executing procedure A as a substep, A precedes B. "Invoking Skills" requires "Installing Skills"; therefore "Installing Skills" → "Invoking Skills."

**Conceptual foundation:** If understanding B requires conceptual framework from A, A precedes B. Understanding "Learning Graph Quality Metrics" requires understanding "Learning Graph"; therefore "Learning Graph" → "Learning Graph Quality Metrics."

**Tool/artifact dependencies:** If working with artifact B requires having created artifact A, A precedes B. "Chapter Content Generation" requires "Chapter Structure"; therefore "Chapter Structure" → "Chapter Content Generation."

**Common dependency specification errors:**

| Error Type | Description | Example | Resolution |
|------------|-------------|---------|------------|
| Over-specification | Adding unnecessary edges | Direct edge A → C when A → B → C exists | Remove redundant A → C edge |
| Under-specification | Missing critical prerequisites | B depends on A but no edge exists | Add missing A → B edge |
| Circular dependencies | Cycle in dependency graph | A → B → C → A | Identify pedagogical primacy, break cycle |
| Granularity mismatch | Concepts at wrong abstraction level | "All of Programming" → specific concept | Refactor to atomic concepts |

The learning-graph-generator skill uses the course description's topic list and learning outcomes to infer likely dependencies, but manual review and refinement typically improves accuracy. Chapter 6 discusses quality validation metrics that identify potential dependency errors.
#### Diagram: Dependency Mapping Decision Tree

<iframe src="../../sims/dependency-mapping-decision-tree/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Dependency Mapping Decision Tree</summary>
    Type: workflow

    Purpose: Guide users in determining whether concept A should be prerequisite to concept B

    Visual style: Decision tree with yes/no branches

    Decision points:
    1. Start: "Is concept B defined using concept A?"
       Yes → "A is prerequisite to B"
       No → Continue to 2

    2. "Does understanding B require the framework or principles from A?"
       Yes → "A is likely prerequisite to B"
       No → Continue to 3

    3. "Does the procedure/skill B include executing procedure A as a substep?"
       Yes → "A is prerequisite to B"
       No → Continue to 4

    4. "Does B build directly on examples or cases from A?"
       Yes → "A is likely prerequisite to B"
       No → Continue to 5

    5. "Are A and B simply related topics without pedagogical ordering?"
       Yes → "No prerequisite relationship (related but independent)"
       No → "Consider creating edge A → B if learners benefit from A before B"

    Terminal nodes:
    - "A is prerequisite to B" (green) - Add edge A → B
    - "A is likely prerequisite to B" (yellow) - Add edge, mark for review
    - "No prerequisite relationship" (gray) - No edge needed
    - "Consider edge" (orange) - Judgment call based on course design

    Color coding:
    - Green: Strong prerequisite
    - Yellow: Probable prerequisite
    - Orange: Weak/optional prerequisite
    - Gray: No relationship

    Implementation: SVG decision tree with diamond decision nodes

---
**MicroSim Generator Recommendations:**

1. mermaid-generator (Score: 95/100) - Perfect for decision tree with yes/no branches, terminal nodes, and color-coded outcomes
2. microsim-p5 (Score: 70/100) - Could create custom interactive decision tree with color-coded paths
3. vis-network (Score: 35/100) - Could show as network but decision tree needs specific branching structure
</details>

## Optimizing Claude Usage for Learning Graph Generation

Generating comprehensive learning graphs with 200+ concepts and their dependencies is one of the most token-intensive operations in intelligent textbook creation. Strategic Claude usage optimization ensures you remain within 4-hour window budgets while producing high-quality graphs.

### Understanding 4-Hour Usage Windows

As introduced in Chapter 2, Claude Pro accounts operate on rolling 4-hour usage windows. Token consumption from learning graph generation—typically 30,000-50,000 tokens for a complete graph including quality validation—remains unavailable for 4 hours after generation.

For multi-textbook projects, this creates a planning consideration: stagger learning graph generation across days rather than generating multiple graphs in rapid succession. Alternatively, complete learning graph generation early in a session, then proceed with lower-token operations (skill installation, file organization, markdown formatting) while waiting for token restoration.

**Usage planning strategies:**

**Front-load generation:** Start sessions with high-token operations (learning graph generation, chapter content generation) to maximize productive use of available tokens before approaching limits.

**Interleave with low-token tasks:** After generating a learning graph, switch to reviewing output quality, manually refining concepts, or organizing project files—tasks requiring minimal Claude interaction.

**Session boundaries:** If approaching token limits, pause substantive generation and resume after the 4-hour window. Use intervening time for manual quality review or skill familiarization.

**Batch processing:** If generating learning graphs for multiple related courses, consolidate generation into dedicated sessions, leveraging shared context from related domains to improve efficiency.

### Claude Pro Limitations and Planning

Beyond the rolling 4-hour windows, Claude Pro imposes additional constraints worth understanding for project planning:

**Daily aggregate limits:** While usage regenerates on a rolling 4-hour basis, there may be aggregate daily limits preventing sustained high-volume usage. For most textbook projects, this is non-binding, but multi-book endeavors should confirm current Claude Pro tier limits.

**Model access:** Claude Pro provides access to the highest-capability models (Opus, Sonnet 4.5) essential for complex reasoning tasks like dependency mapping and quality validation. The learning-graph-generator skill leverages these capabilities to produce coherent, well-structured concept graphs.

**Priority access:** During high-demand periods, Pro accounts receive priority, reducing latency for time-sensitive work.

For professional textbook development projects, the Pro subscription proves essential—free-tier limitations would severely constrain the multi-chapter generation workflows this course teaches.

### Content Generation Process and Token Management

The intelligent textbook workflow involves multiple content generation stages, each with different token consumption profiles:

| Stage | Typical Token Consumption | Frequency | Optimization Strategy |
|-------|---------------------------|-----------|----------------------|
| Course Description | 5,000-10,000 | Once per project | Front-load, high value per token |
| Learning Graph Generation | 30,000-50,000 | Once per project | Front-load, critical foundation |
| Glossary Generation | 15,000-25,000 | Once per project | After learning graph validation |
| Chapter Outline Generation | 5,000-10,000 | Once per project | Batch with other planning |
| Chapter Content Generation | 20,000-40,000 per chapter | 10-15 times | Spread across sessions |
| Quiz Generation | 5,000-10,000 per chapter | 10-15 times | Batch multiple chapters |
| MicroSim Specification | 3,000-8,000 per sim | 15-30 times | Generate as needed during content creation |

**Token optimization tactics:**

**Leverage file-based context:** Rather than maintaining entire learning graphs in conversation context, the learning-graph-generator writes to CSV files. Subsequent skills read these files, avoiding context re-transmission.

**Incremental generation:** Generate chapter content incrementally rather than attempting entire books in single sessions. Each chapter is independent after outline completion.

**Skill specialization:** Purpose-built skills with focused contexts consume fewer tokens than general-purpose interactions attempting equivalent tasks.

**Quality thresholds:** Establish acceptable quality thresholds (e.g., learning graph quality score ≥ 70) that balance perfection against token expenditure. Iterating to 95+ consumes disproportionate tokens for marginal improvement.

### Chapter Structure and Token Budgeting

Chapter structure significantly impacts token consumption during content generation. The chapter outline produced by book-chapter-generator determines how many concepts each chapter covers, directly affecting content generation token usage.

**Chapter sizing heuristics:**

**Balanced chapters:** Aim for 12-18 concepts per chapter. This produces ~3,500-5,000 word chapters requiring ~25,000-35,000 tokens to generate.

**Front-loaded chapters:** Foundational chapters with many prerequisite concepts may be larger (20-25 concepts). Budget proportionally more tokens.

**Advanced synthesis chapters:** Later chapters integrating previous concepts may have fewer new concepts (8-12) but require deeper treatment. Token consumption remains moderate due to referencing rather than re-explaining prerequisites.

For a 13-chapter textbook, total chapter content generation consumes ~325,000-455,000 tokens across all chapters. At 20,000 tokens per 4-hour window (hypothetical limit), this spans ~16-23 windows or 64-92 hours of rolling window time. Distributed across 2-3 weeks with 3-4 hours of generation work daily, this comfortably fits within Claude Pro capabilities.

**Parallelization considerations:**

While Claude Code itself operates sequentially within a session, you can run multiple independent Claude Code sessions across different projects or chapter generation tasks. This "poor man's parallelization" enables working on Chapter 1 content while Chapter 2 quiz generation runs in a separate session, effectively doubling throughput within token budget constraints.
#### Diagram: Token Consumption Timeline for Complete Textbook Project

<iframe src="../../sims/token-consumption-timeline-for-complete-textbook-project/main.html" width="100%" height="600px" scrolling="no"></iframe>
<!-- TODO: adjust the height of the iframe -->
TODO: Generate Microsim

<details markdown="1">
    <summary>Token Consumption Timeline for Complete Textbook Project</summary>
    Type: timeline

    Purpose: Show typical token consumption across complete intelligent textbook project lifecycle

    Time period: 0-20 days (typical project timeline)

    Orientation: Horizontal timeline with cumulative token consumption shown as area chart below

    Events and token consumption:
    - Day 1: Course description (8,000 tokens)
    - Day 2: Learning graph generation (45,000 tokens)
    - Day 3: Glossary generation (20,000 tokens)
    - Day 4: Chapter outline (8,000 tokens)
    - Days 5-14: Chapter content generation, ~3 chapters every 2-3 days (30,000 tokens per chapter × 13 = 390,000 tokens distributed)
    - Days 15-18: Quiz generation batches (8,000 tokens per batch × 5 batches = 40,000 tokens)
    - Days 19-20: MicroSim specifications as needed (5,000 tokens per day)

    Visual elements:
    - Timeline with major milestones
    - Area chart showing cumulative token consumption
    - Shaded regions indicating 4-hour window regeneration
    - Annotations showing total tokens per phase

    Color coding:
    - Blue: Foundation phase (course description, learning graph)
    - Purple: Supporting content phase (glossary, outlines)
    - Green: Content generation phase (chapters, quizzes)
    - Orange: Enhancement phase (MicroSims)

    Annotations:
    - "Total project: ~530,000 tokens"
    - "Spread across 20 days: ~26,500 tokens/day average"
    - "Well within Claude Pro capabilities with planning"

    Interactive features:
    - Hover over timeline points to see specific token amounts
    - Hover over area chart to see cumulative consumption

    Implementation: HTML/CSS/JavaScript with Chart.js timeline and area chart

---
**MicroSim Generator Recommendations:**

1. timeline-generator (Score: 95/100) - Perfect for project timeline with events over 20 days, includes timeline visualization with phase tracking
2. chartjs-generator (Score: 90/100) - Excellent for area chart showing cumulative token consumption over time - Chart.js explicitly mentioned
3. microsim-p5 (Score: 65/100) - Could create custom timeline with area chart but standard libraries already provide this
</details>

## Summary

This chapter introduced learning graphs as formalized knowledge structures representing concepts as nodes and prerequisite dependencies as edges. You learned how learning graphs function as Directed Acyclic Graphs (DAGs) ensuring valid pedagogical orderings exist, and how prerequisite relationships define learning pathways through course content.

We explored concept nodes with their atomic granularity principles and dependency edges encoding prerequisite relationships. You learned to distinguish direct from transitive dependencies, identify common dependency patterns (sequential chains, fan-in, fan-out), and recognize why the DAG constraint is mathematically necessary for coherent curriculum design.

Finally, we addressed practical Claude usage optimization for learning graph generation, exploring how 4-hour usage windows, token budgeting across project phases, and chapter sizing decisions impact sustainable textbook development workflows. These foundations prepare you for Chapter 5's deep dive into the mechanics of concept enumeration and dependency mapping.

**Concepts covered:** Learning Graph ✓, Concept Nodes in Learning Graphs ✓, Dependency Edges in Learning Graphs ✓, Directed Acyclic Graph (DAG) ✓, Prerequisite Relationships ✓, Concept Dependencies ✓, Learning Pathways ✓, 4-Hour Usage Windows ✓, Claude Pro Limitations ✓, Optimizing Claude Usage ✓, Content Generation Process ✓, Chapter Structure ✓

## References

1. [The Theory Underlying Concept Maps and How to Construct Them](https://cmap.ihmc.us/docs/theory-of-concept-maps) - 2008 - Joseph D. Novak & Alberto J. Cañas - Foundational paper explaining the theoretical basis for concept mapping rooted in Ausubel's learning psychology, detailing how hierarchical concept structures facilitate meaningful learning, directly applicable to understanding learning graph design principles.

2. [A systematic literature review of knowledge graph construction and application in education](https://pmc.ncbi.nlm.nih.gov/articles/PMC10847940/) - 2024 - PMC - Comprehensive review examining knowledge graph methodologies and applications in personalized learning, curriculum design, concept mapping, and educational content recommendation systems, providing research-based validation for learning graph approaches in intelligent textbooks.
