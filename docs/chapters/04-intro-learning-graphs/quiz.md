# Quiz: Introduction to Learning Graphs

Test your understanding of learning graphs, concept nodes, dependency edges, and Claude usage optimization with these questions.

---

#### 1. What is the primary purpose of a learning graph in intelligent textbook creation?

<div class="upper-alpha" markdown>
1. To create visual diagrams for textbook covers
2. To map conceptual landscape with prerequisite dependencies explicitly
3. To track student progress through course material
4. To organize bibliography references by topic
</div>

??? question "Show Answer"
    The correct answer is **B**. A learning graph is a directed graph data structure that maps the conceptual landscape of a course domain, explicitly representing concepts as nodes and prerequisite dependencies as edges. This formalization enables systematic curriculum design, optimal content sequencing, and adaptive learning pathways. Option A confuses visual design with conceptual structure, option C describes a learning management system feature rather than a learning graph's design purpose, and option D describes bibliography organization, not concept dependency mapping.

    **Concept Tested:** Learning Graph

    **See:** [What is a Learning Graph?](../../glossary.md#learning-graph)

---

#### 2. What distinguishes concept nodes from general graph vertices in a learning graph?

<div class="upper-alpha" markdown>
1. Concept nodes represent atomic knowledge units with unique identifiers
2. Concept nodes can only contain numbers, not text labels
3. Concept nodes are always colored red in visualizations
4. Concept nodes must have exactly three dependencies
</div>

??? question "Show Answer"
    The correct answer is **A**. Concept nodes represent atomic knowledge units—discrete, well-defined ideas, procedures, or principles that learners must understand. Each node has a unique ConceptID and human-readable ConceptLabel, making them distinct from generic graph vertices. Option B is false as concept nodes require text labels, option C incorrectly describes visualization conventions, and option D states an arbitrary constraint that doesn't exist.

    **Concept Tested:** Concept Nodes in Learning Graphs

    **See:** [Concept Nodes in Learning Graphs](../../glossary.md#concept-nodes-in-learning-graphs)

---

#### 3. In a learning graph, what does a directed edge from concept A to concept B indicate?

<div class="upper-alpha" markdown>
1. A and B are completely unrelated concepts
2. A is prerequisite to B, and B depends on A
3. B must be taught before A in all circumstances
4. A and B should appear in the same chapter
</div>

??? question "Show Answer"
    The correct answer is **B**. A directed edge A → B means A is a prerequisite for B, B depends on A, A should be taught before B, and learners must master A to understand B fully. This encodes the pedagogical ordering constraint. Option A contradicts the purpose of edges (showing relationships), option C reverses the dependency direction, and option D describes chapter organization which is influenced by but not directly determined by single edges.

    **Concept Tested:** Dependency Edges in Learning Graphs

    **See:** [Dependency Edges in Learning Graphs](../../glossary.md#dependency-edges-in-learning-graphs)

---

#### 4. Why must a valid learning graph be a Directed Acyclic Graph (DAG)?

<div class="upper-alpha" markdown>
1. To make the graph easier to draw on paper
2. To reduce the number of concepts required
3. To ensure a valid pedagogical ordering exists without circular dependencies
4. To limit the graph to exactly 200 concepts
</div>

??? question "Show Answer"
    The correct answer is **C**. A DAG constraint ensures no cycles exist, which means there is some valid sequence in which concepts can be taught such that all prerequisites precede their dependents. If a cycle existed (A → B → C → A), it would create a logical impossibility where A must be learned before itself. Option A trivializes a fundamental mathematical requirement, option B is unrelated to the DAG property, and option D confuses DAG requirements with concept count recommendations.

    **Concept Tested:** Directed Acyclic Graph (DAG)

    **See:** [Directed Acyclic Graph (DAG) Requirement](../../glossary.md#directed-acyclic-graph-dag)

---

#### 5. A learning graph contains concepts X, Y, and Z with dependencies X → Y → Z. What type of prerequisite relationship exists between X and Z?

<div class="upper-alpha" markdown>
1. Direct prerequisite (explicit edge required)
2. Transitive prerequisite (implied by path)
3. No prerequisite relationship exists
4. Bidirectional prerequisite relationship
</div>

??? question "Show Answer"
    The correct answer is **B**. X is a transitive prerequisite to Z because there exists a path X → Y → Z even without a direct edge X → Z. Transitive dependencies are implied by paths through the graph and don't require explicit edges, keeping the graph sparse and maintainable. Option A would require adding a redundant direct edge, option C is false as the relationship clearly exists via the path, and option D describes cycles which violate the DAG constraint.

    **Concept Tested:** Prerequisite Relationships

    **See:** [Prerequisite Relationships and Learning Pathways](../../glossary.md#prerequisite-relationships)

---

#### 6. If your learning graph generation consumes 40,000 tokens, approximately how long must you wait before those tokens become available again in your Claude Pro account?

<div class="upper-alpha" markdown>
1. Immediately, tokens regenerate instantly
2. 1 hour from the generation time
3. 4 hours from the generation time
4. 24 hours from the generation time
</div>

??? question "Show Answer"
    The correct answer is **C**. Claude Pro accounts operate on rolling 4-hour usage windows. Token consumption from any operation remains unavailable for 4 hours after that operation. This means tokens used for learning graph generation become available again 4 hours later, not immediately, after 1 hour, or after a full day. Understanding this window helps plan multi-stage textbook generation workflows.

    **Concept Tested:** 4-Hour Usage Windows

    **See:** [Understanding 4-Hour Usage Windows](../../glossary.md#4-hour-usage-windows)

---

#### 7. What is the recommended approach for managing Claude Pro token budgets when generating a complete intelligent textbook?

<div class="upper-alpha" markdown>
1. Generate all content in a single session to maximize efficiency
2. Front-load high-token operations, then interleave with low-token tasks
3. Avoid using Claude Pro and rely only on free tier access
4. Wait until all chapters are manually written before using Claude
</div>

??? question "Show Answer"
    The correct answer is **B**. Effective token management involves front-loading high-token operations (learning graph generation, chapter content) early in sessions to maximize productive token use, then interleaving with low-token tasks (file organization, manual review, formatting) while waiting for token restoration. Option A ignores token limits, option C contradicts the premise of using AI for textbook generation, and option D defeats the purpose of AI-assisted content creation.

    **Concept Tested:** Optimizing Claude Usage

    **See:** [Optimizing Claude Usage for Learning Graph Generation](../../glossary.md#optimizing-claude-usage)

---

#### 8. Given a learning graph fragment where "Programming Basics" has no incoming edges and enables both "Variables" and "Functions," which pattern does this illustrate?

<div class="upper-alpha" markdown>
1. Fan-in (convergence) pattern
2. Fan-out (divergence) pattern
3. Sequential chain pattern
4. Circular dependency pattern
</div>

??? question "Show Answer"
    The correct answer is **B**. Fan-out (divergence) occurs when a foundational concept enables multiple dependent concepts. "Programming Basics" with no incoming edges (foundational) pointing to both "Variables" and "Functions" exemplifies this pattern. Option A would require multiple concepts pointing to one advanced concept, option C would require a linear A → B → C sequence, and option D describes an invalid cycle.

    **Concept Tested:** Concept Dependencies

    **See:** [Dependency Edges in Learning Graphs](../../glossary.md#dependency-edges-in-learning-graphs)

---

#### 9. For a 13-chapter textbook with balanced concept distribution, approximately how many concepts should each chapter contain?

<div class="upper-alpha" markdown>
1. 5-8 concepts per chapter
2. 12-18 concepts per chapter
3. 25-30 concepts per chapter
4. 40-50 concepts per chapter
</div>

??? question "Show Answer"
    The correct answer is **B**. With a target of approximately 200 concepts for a semester-length course and 13 chapters, balanced distribution yields 12-18 concepts per chapter (200 ÷ 13 ≈ 15). This produces manageable chapters of 3,500-5,000 words that respect cognitive load principles. Option A would create overly shallow chapters, while options C and D would overwhelm learners with excessive concepts per chapter.

    **Concept Tested:** Chapter Structure

    **See:** [Chapter Structure and Token Budgeting](../../glossary.md#chapter-structure-and-token-budgeting)

---

#### 10. Which statement best describes the relationship between concept depth and chapter placement in a well-structured textbook?

<div class="upper-alpha" markdown>
1. All concepts should have equal depth regardless of chapter
2. Foundational concepts with zero dependencies appear in early chapters
3. Advanced concepts with many dependencies appear in early chapters
4. Chapter placement is random and unrelated to concept depth
</div>

??? question "Show Answer"
    The correct answer is **B**. Topological ordering of the learning graph ensures foundational concepts with zero incoming edges (no dependencies) appear in early chapters, while concepts with many incoming edges (advanced, integrative) appear in later chapters. This respects prerequisite relationships and creates natural learning progression. Option A ignores dependency structure, option C reverses the logical ordering, and option D contradicts systematic curriculum design principles.

    **Concept Tested:** Learning Pathways

    **See:** [Prerequisite Relationships and Learning Pathways](../../glossary.md#prerequisite-relationships)

---

## Quiz Statistics

- **Total Questions:** 10
- **Bloom's Taxonomy Distribution:**
  - Remember: 3 questions (30%)
  - Understand: 3 questions (30%)
  - Apply: 3 questions (30%)
  - Analyze: 1 question (10%)
- **Concepts Covered:** 10 of 12 chapter concepts (83%)
