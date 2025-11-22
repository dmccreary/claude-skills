# Quiz: Learning Graph Quality and Validation

Test your understanding of DAG validation, quality metrics, circular dependency detection, and taxonomy distribution analysis with these questions.

---

#### 1. What is the time complexity of the DFS-based cycle detection algorithm used to validate learning graphs?

<div class="upper-alpha" markdown>
1. O(V) where V is the number of vertices
2. O(V + E) where V is vertices and E is edges
3. O(V²) for all possible vertex pairs
4. O(E log E) where E is the number of edges
</div>

??? question "Show Answer"
    The correct answer is **B**. The depth-first search (DFS) algorithm with cycle detection runs in O(V + E) time complexity, where it must visit each vertex once and traverse each edge once. This linear-time algorithm is efficient for validating learning graphs. Option A ignores edge traversal, option C suggests an unnecessarily expensive approach, and option D describes a sorting algorithm complexity.

    **Concept Tested:** DAG Validation

    **See:** [DAG Validation](../../glossary.md#dag-validation)

---

#### 2. During DFS-based cycle detection, what does encountering a gray node indicate?

<div class="upper-alpha" markdown>
1. A node that has never been visited before
2. A completed node with all descendants explored
3. A back edge indicating a cycle has been detected
4. A forward edge indicating valid progression
</div>

??? question "Show Answer"
    The correct answer is **C**. In the three-color DFS algorithm, gray nodes are currently being explored (on the recursion stack). Encountering a gray node during traversal means you've found a back edge pointing to an ancestor, which indicates a cycle. White nodes (option A) are unvisited, black nodes (option B) are completed, and option D describes a tree edge, not a back edge.

    **Concept Tested:** Circular Dependency Detection

    **See:** [Circular Dependency Detection](../../glossary.md#circular-dependency-detection)

---

#### 3. What does an orphaned node in a learning graph represent?

<div class="upper-alpha" markdown>
1. A concept with zero dependencies (foundational concept)
2. A concept that no other concepts depend upon (outdegree = 0)
3. A concept in a disconnected subgraph
4. A concept with exactly one dependency
</div>

??? question "Show Answer"
    The correct answer is **B**. An orphaned node has an outdegree of zero, meaning no other concepts depend on it. These are terminal or culminating concepts. Option A describes foundational concepts (indegree = 0, not orphaned), option C describes disconnected components (a different issue), and option D is arbitrary and doesn't define orphaned status.

    **Concept Tested:** Orphaned Nodes

    **See:** [Orphaned Nodes](../../glossary.md#orphaned-nodes)

---

#### 4. In a healthy learning graph, what percentage of concepts should typically be orphaned nodes?

<div class="upper-alpha" markdown>
1. 0-2% (essentially none)
2. 5-10% (terminal concepts)
3. 25-30% (significant portion)
4. 50%+ (majority of concepts)
</div>

??? question "Show Answer"
    The correct answer is **B**. A well-designed learning graph typically has 5-10% orphaned nodes representing culminating concepts and specialized topics. Too few orphaned nodes (option A) suggests incomplete terminal concepts, while too many (options C and D) indicates concepts that may be improperly isolated, missing dependent concepts, or too specialized for the course scope.

    **Concept Tested:** Quality Metrics for Graphs

    **See:** [Orphaned Nodes](../../glossary.md#orphaned-nodes)

---

#### 5. You run analyze-graph.py and discover your learning graph contains a cycle: A → B → C → D → A. What is the recommended approach to resolve this?

<div class="upper-alpha" markdown>
1. Remove all concepts involved in the cycle
2. Add more dependencies to strengthen the relationships
3. Identify pedagogical primacy and remove the weakest dependency edge
4. Convert all dependencies to bidirectional relationships
</div>

??? question "Show Answer"
    The correct answer is **C**. To break a cycle, examine the concepts involved to determine which dependency is weakest or least pedagogically justified, then remove that edge. This preserves the important prerequisite relationships while eliminating the cycle. Option A discards valuable concepts unnecessarily, option B would worsen the problem, and option D would create more cycles, violating the DAG requirement.

    **Concept Tested:** Circular Dependency Detection

    **See:** [Circular Dependency Detection](../../glossary.md#circular-dependency-detection)

---

#### 6. What is the optimal range for average dependencies per concept in a learning graph?

<div class="upper-alpha" markdown>
1. 0.5-1.0 dependencies
2. 2.0-4.5 dependencies
3. 6.0-8.0 dependencies
4. 10+ dependencies
</div>

??? question "Show Answer"
    The correct answer is **B**. The optimal average dependencies per concept is 2.0-4.5, balancing prerequisite completeness with learner accessibility. Below 2.0 (option A) suggests overly linear graphs, while above 5.0 (options C and D) may indicate over-specification of prerequisites or unrealistic prerequisite burdens on learners.

    **Concept Tested:** Average Dependencies Per Concept

    **See:** [Average Dependencies Per Concept](../../glossary.md#average-dependencies-per-concept)

---

#### 7. A learning graph has 200 concepts and 620 total dependency edges. What is the average dependencies per concept, and how should this be interpreted?

<div class="upper-alpha" markdown>
1. 3.1 dependencies; optimal for intermediate course
2. 0.32 dependencies; too linear
3. 31 dependencies; severe over-specification
4. 620 dependencies; calculation error
</div>

??? question "Show Answer"
    The correct answer is **A**. Average dependencies = Total Edges / Total Nodes = 620 / 200 = 3.1 dependencies per concept. This falls within the ideal 2.0-4.5 range for intermediate courses with moderate integration. Option B incorrectly inverts the calculation, option C misplaces the decimal, and option D confuses the total edges with average.

    **Concept Tested:** Average Dependencies Per Concept

    **See:** [Average Dependencies Per Concept](../../glossary.md#average-dependencies-per-concept)

---

#### 8. Your learning graph quality report shows a score of 68. What action should you take?

<div class="upper-alpha" markdown>
1. Proceed immediately with content generation
2. Address several issues before content generation
3. Completely restart the learning graph from scratch
4. Ignore the score as it's not meaningful
</div>

??? question "Show Answer"
    The correct answer is **B**. A quality score of 68 falls in the "Acceptable" range (60-74), which means there are several issues to address before content generation but the graph doesn't require complete restructuring. The score indicates specific problems that can be identified and corrected. Option A ignores quality concerns, option C is unnecessarily drastic, and option D dismisses a valuable quality metric.

    **Concept Tested:** Learning Graph Quality Score

    **See:** [Learning Graph Quality Score](../../glossary.md#learning-graph-quality-score)

---

#### 9. In taxonomy distribution analysis, what threshold indicates over-representation of a single category?

<div class="upper-alpha" markdown>
1. Any category exceeding 10%
2. Any category exceeding 20%
3. Any category exceeding 30%
4. Any category exceeding 50%
</div>

??? question "Show Answer"
    The correct answer is **C**. Over-representation occurs when a single taxonomy category exceeds 30% of total concepts, indicating imbalanced coverage that may result from scope creep, expert bias, or incomplete mapping in other categories. Options A and B set the threshold too low for natural emphasis areas, while option D sets it too high, allowing excessive concentration.

    **Concept Tested:** Avoiding Over-Representation

    **See:** [Avoiding Over-Representation](../../glossary.md#avoiding-over-representation)

---

#### 10. Which Python script converts learning graph CSV format to vis-network JSON format for visualization?

<div class="upper-alpha" markdown>
1. analyze-graph.py
2. csv-to-json.py
3. taxonomy-distribution.py
4. validate-dependencies.py
</div>

??? question "Show Answer"
    The correct answer is **B**. The csv-to-json.py script performs the conversion from CSV (ConceptID, ConceptLabel, Dependencies, TaxonomyID) to vis-network JSON format with nodes, edges, groups, and metadata sections. The analyze-graph.py script (option A) performs quality validation, taxonomy-distribution.py (option C) analyzes category balance, and option D is not a real script in the toolkit.

    **Concept Tested:** csv-to-json.py Script

    **See:** [csv-to-json.py Script](../../glossary.md#csv-to-jsonpy-script)

---

## Quiz Statistics

- **Total Questions:** 10
- **Bloom's Taxonomy Distribution:**
  - Remember: 2 questions (20%)
  - Understand: 3 questions (30%)
  - Apply: 4 questions (40%)
  - Analyze: 1 question (10%)
- **Concepts Covered:** 10 of 16 chapter concepts (63%)
