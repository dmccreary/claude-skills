# Quiz: Concept Enumeration and Dependencies

Test your understanding of concept enumeration, dependency mapping, CSV file formats, and taxonomy categorization with these questions.

---

#### 1. What is the recommended target number of concepts for a standard semester-length course learning graph?

<div class="upper-alpha" markdown>
1. 50-75 concepts
2. 100-150 concepts
3. 180-220 concepts
4. 300-400 concepts
</div>

??? question "Show Answer"
    The correct answer is **C**. A semester-length course typically targets approximately 200 concepts (range 180-220), which aligns with cognitive load principles, provides adequate assessment coverage, and fits semester pacing of 45 contact hours. This yields about 13 minutes per concept for instruction. Option A would lack depth, option B would be appropriate for shorter courses, and option D would overwhelm learners and instructors.

    **Concept Tested:** Generating 200 Concepts

    **See:** [Generating 200 Concepts](../../glossary.md#generating-200-concepts)

---

#### 2. Which of the following concept labels correctly follows Title Case convention?

<div class="upper-alpha" markdown>
1. "learning graph generation"
2. "Learning Graph Generation"
3. "LEARNING GRAPH GENERATION"
4. "Learning graph generation"
</div>

??? question "Show Answer"
    The correct answer is **B**. Title Case capitalizes the first letter of major words while keeping articles, conjunctions, and short prepositions lowercase. "Learning Graph Generation" correctly capitalizes all three major words. Option A uses sentence case (incorrect), option C uses all caps (incorrect), and option D incorrectly keeps "graph" and "generation" lowercase.

    **Concept Tested:** Title Case Convention

    **See:** [Title Case Convention](../../glossary.md#title-case-convention)

---

#### 3. What is the maximum character length permitted for a concept label, including spaces?

<div class="upper-alpha" markdown>
1. 16 characters
2. 24 characters
3. 32 characters
4. 64 characters
</div>

??? question "Show Answer"
    The correct answer is **C**. Concept labels must not exceed 32 characters including spaces. This constraint ensures labels fit in UI elements like navigation menus, graph node displays, and table columns without truncation. Options A and B are too restrictive and would prevent descriptive labels, while option D would allow overlength labels that break visual layouts.

    **Concept Tested:** Maximum Character Length

    **See:** [Maximum Character Length](../../glossary.md#maximum-character-length)

---

#### 4. A proposed concept is titled "Complete Overview of All Machine Learning Algorithms and Their Applications." What is the primary problem with this concept?

<div class="upper-alpha" markdown>
1. It violates the Title Case convention
2. It lacks atomic granularity and is too coarse
3. It exceeds 32 characters but is otherwise acceptable
4. It uses technical jargon inappropriately
</div>

??? question "Show Answer"
    The correct answer is **B**. This concept is far too coarse, encompassing multiple distinct ideas that should be separate atomic concepts. It cannot be assessed specifically, has unclear dependencies, and would generate overly general content. While it also exceeds 32 characters (option C is partially true), the fundamental issue is granularity—even if shortened, it remains too broad. Options A and D are not the main problems.

    **Concept Tested:** Concept Granularity

    **See:** [Concept Granularity](../../glossary.md#concept-granularity)

---

#### 5. In the CSV format for learning graphs, how are multiple dependencies represented in the Dependencies field?

<div class="upper-alpha" markdown>
1. Comma-separated list (e.g., "1,2,3")
2. Pipe-delimited list (e.g., "1|2|3")
3. Semicolon-separated list (e.g., "1;2;3")
4. Space-separated list (e.g., "1 2 3")
</div>

??? question "Show Answer"
    The correct answer is **B**. The Dependencies column uses pipe (|) delimiters to separate multiple prerequisite ConceptIDs, enabling compact representation like "5|7|8" for a concept depending on concepts 5, 7, and 8. Comma delimiters (option A) would conflict with CSV field separators, while semicolons and spaces (options C and D) are not the standard format and may cause parsing errors.

    **Concept Tested:** Pipe-Delimited Dependencies

    **See:** [Pipe-Delimited Dependencies](../../glossary.md#pipe-delimited-dependencies)

---

#### 6. If a learning graph CSV contains the row "5,Directed Acyclic Graph,3|4,CORE", what does this indicate?

<div class="upper-alpha" markdown>
1. Concept 5 has no dependencies and is foundational
2. Concept 5 depends on concepts 3 and 4
3. Concepts 3 and 4 both depend on concept 5
4. Concept 5 is invalid because it has two dependencies
</div>

??? question "Show Answer"
    The correct answer is **B**. The Dependencies field "3|4" indicates that concept 5 depends on both concepts 3 and 4 as prerequisites. This creates edges 3 → 5 and 4 → 5 in the learning graph. Option A misreads the non-empty Dependencies field, option C reverses the dependency direction, and option D incorrectly suggests multiple dependencies are invalid.

    **Concept Tested:** Dependencies Field

    **See:** [Dependencies Field](../../glossary.md#dependencies-field)

---

#### 7. You are creating a learning graph and want to add a new concept about "Python list comprehensions." You determine it requires understanding of both "Python lists" (concept 12) and "For loops" (concept 15). How should you represent this in the CSV?

<div class="upper-alpha" markdown>
1. Add two separate rows, one for each dependency
2. Add one row with Dependencies field "12|15"
3. Add one row with Dependencies field "15|12"
4. Add two edges in a separate edges table
</div>

??? question "Show Answer"
    The correct answer is **B**. You create a single row for the new concept with the Dependencies field containing "12|15" (or "15|12"—order doesn't matter within the pipe-delimited list). This single compact representation creates both prerequisite relationships. Option A would create duplicate concept entries (invalid), option C is equivalent to B (either order is fine), and option D describes a different data model not used in the CSV format.

    **Concept Tested:** Dependency Mapping Process

    **See:** [Dependency Mapping Process](../../glossary.md#dependency-mapping-process)

---

#### 8. What percentage of concepts in a well-balanced learning graph should typically be foundational concepts with zero dependencies?

<div class="upper-alpha" markdown>
1. 1-3%
2. 5-10%
3. 20-30%
4. 40-50%
</div>

??? question "Show Answer"
    The correct answer is **B**. Foundational concepts with zero dependencies should represent 5-10% of total concepts (about 10-20 concepts in a 200-concept graph), serving as entry points. Too few (option A) suggests missing entry points or circular dependencies, while too many (options C and D) suggests the course lacks depth or includes unnecessary prerequisites.

    **Concept Tested:** Foundational Concepts

    **See:** [Foundational, Prerequisite, and Advanced Concepts](../../glossary.md#foundational-concepts)

---

#### 9. In a 200-concept learning graph, approximately how many concepts should be advanced/integrative concepts with 4 or more dependencies?

<div class="upper-alpha" markdown>
1. 10-20 concepts (5-10%)
2. 40-60 concepts (20-30%)
3. 100-120 concepts (50-60%)
4. 160-180 concepts (80-90%)
</div>

??? question "Show Answer"
    The correct answer is **B**. Advanced concepts with 4+ dependencies should represent 20-30% of the graph (40-60 concepts in a 200-concept graph), representing learning culmination and integration. Option A suggests insufficient advanced content, while options C and D indicate over-specification of prerequisites or insufficiently atomic concepts that should be split.

    **Concept Tested:** Advanced Concepts

    **See:** [Foundational, Prerequisite, and Advanced Concepts](../../glossary.md#foundational-concepts)

---

#### 10. What is the primary purpose of the TaxonomyID field in the learning graph CSV?

<div class="upper-alpha" markdown>
1. To assign unique identifiers to each concept
2. To categorize concepts into thematic groups for quality analysis
3. To specify the teaching order of concepts
4. to track which Bloom's Taxonomy level each concept addresses
</div>

??? question "Show Answer"
    The correct answer is **B**. The TaxonomyID field categorizes concepts into thematic groups (like FOUND, BASIC, ARCH, IMPL), enabling quality assessment (balanced coverage), chapter organization (grouping related concepts), and navigation enhancement (filtering by category). Option A confuses it with ConceptID, option C confuses it with dependency ordering, and option D confuses it with Bloom's Taxonomy cognitive levels (a different framework).

    **Concept Tested:** Taxonomy

    **See:** [Taxonomy and Concept Categorization](../../glossary.md#concept-categorization)

---

## Quiz Statistics

- **Total Questions:** 10
- **Bloom's Taxonomy Distribution:**
  - Remember: 2 questions (20%)
  - Understand: 3 questions (30%)
  - Apply: 4 questions (40%)
  - Analyze: 1 question (10%)
- **Concepts Covered:** 10 of 18 chapter concepts (56%)
