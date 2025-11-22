# Quiz: Taxonomy and Data Formats

Test your understanding of taxonomy categorization, vis-network JSON format, Dublin Core metadata, and Python processing scripts with these questions.

---

#### 1. What is the recommended length for TaxonomyID abbreviations in learning graph CSV files?

<div class="upper-alpha" markdown>
1. 1-2 letters for brevity
2. 3-5 letters for balance
3. 6-10 letters for clarity
4. 15+ letters for full descriptiveness
</div>

??? question "Show Answer"
    The correct answer is **B**. TaxonomyID abbreviations should be 3-5 letters, balancing compactness in CSV files and visualizations with sufficient distinctiveness and mnemonics. Option A is too short to be distinctive, while options C and D defeat the purpose of abbreviation and would clutter visualizations.

    **Concept Tested:** TaxonomyID Abbreviations

    **See:** [TaxonomyID Abbreviations](../../glossary.md#taxonomyid-abbreviations)

---

#### 2. In the vis-network JSON format, which section defines visual styling like background color and node shape for each taxonomy category?

<div class="upper-alpha" markdown>
1. metadata section
2. groups section
3. nodes section
4. edges section
</div>

??? question "Show Answer"
    The correct answer is **B**. The groups section defines visual styling (color, font, shape) for each TaxonomyID category, enabling consistent color-coded visualization. The metadata section (option A) contains descriptive information about the graph, the nodes section (option C) contains concept objects, and the edges section (option D) contains dependency relationships.

    **Concept Tested:** Groups Section in JSON

    **See:** [Groups Section in JSON](../../glossary.md#groups-section-in-json)

---

#### 3. What are the four primary sections of the vis-network JSON format for learning graphs?

<div class="upper-alpha" markdown>
1. header, concepts, relationships, footer
2. metadata, groups, nodes, edges
3. title, categories, vertices, links
4. description, taxonomy, elements, connections
</div>

??? question "Show Answer"
    The correct answer is **B**. The vis-network JSON format organizes learning graph data into four sections: metadata (information about the graph), groups (visual styling), nodes (concept objects), and edges (dependency relationships). Options A, C, and D use incorrect terminology that doesn't match the vis-network specification.

    **Concept Tested:** vis-network JSON Format

    **See:** [vis-network JSON Format](../../glossary.md#vis-network-json-format)

---

#### 4. In the nodes section of vis-network JSON, what three required properties must each node object contain?

<div class="upper-alpha" markdown>
1. name, color, size
2. id, label, group
3. number, title, category
4. key, value, type
</div>

??? question "Show Answer"
    The correct answer is **B**. Each node object requires three properties: id (numeric identifier matching ConceptID), label (human-readable concept name), and group (TaxonomyID category for styling). Options A, C, and D use incorrect property names that don't conform to the vis-network schema.

    **Concept Tested:** Nodes Section in JSON

    **See:** [Nodes Section in JSON](../../glossary.md#nodes-section-in-json)

---

#### 5. You are converting a learning graph CSV row with ConceptID=10 and Dependencies="3|7|9". How many edge objects will be created in the vis-network JSON?

<div class="upper-alpha" markdown>
1. 1 edge object (one concept, one entry)
2. 2 edge objects (pipe creates pairs)
3. 3 edge objects (one for each dependency)
4. 4 edge objects (including the concept itself)
</div>

??? question "Show Answer"
    The correct answer is **C**. The Dependencies field "3|7|9" indicates three prerequisites, so three edge objects must be created: {from: 3, to: 10}, {from: 7, to: 10}, and {from: 9, to: 10}. Each dependency creates one edge pointing from the prerequisite to the dependent concept. Options A, B, and D misunderstand the one-to-one mapping of dependencies to edges.

    **Concept Tested:** Edges Section in JSON

    **See:** [Edges Section in JSON](../../glossary.md#edges-section-in-json)

---

#### 6. Which Dublin Core metadata field should use ISO 8601 format (YYYY-MM-DD)?

<div class="upper-alpha" markdown>
1. Title
2. Creator
3. Date
4. License
</div>

??? question "Show Answer"
    The correct answer is **C**. The Date metadata field should use ISO 8601 format (YYYY-MM-DD) for unambiguous, machine-parseable dates like "2024-09-15". Title (option A) is a descriptive string, Creator (option B) contains author information, and License (option D) uses license identifiers like "CC-BY-4.0".

    **Concept Tested:** Date Metadata Field

    **See:** [Date Metadata Field](../../glossary.md#date-metadata-field)

---

#### 7. In semantic versioning for learning graphs, what does incrementing the MINOR version number indicate?

<div class="upper-alpha" markdown>
1. Incompatible changes like restructuring categories
2. Backwards-compatible additions like new concepts
3. Bug fixes like correcting typos
4. Complete rewrite of the learning graph
</div>

??? question "Show Answer"
    The correct answer is **B**. In semantic versioning (MAJOR.MINOR.PATCH), incrementing MINOR indicates backwards-compatible additions such as adding new concepts or refining dependencies. MAJOR increments (option A) indicate breaking changes, PATCH increments (option C) indicate corrections, and option D would be a MAJOR version change, not MINOR.

    **Concept Tested:** Version Metadata Field

    **See:** [Version Metadata Field](../../glossary.md#version-metadata-field)

---

#### 8. According to WCAG accessibility guidelines, what is the minimum contrast ratio required for normal text?

<div class="upper-alpha" markdown>
1. 2:1 contrast ratio
2. 3:1 contrast ratio
3. 4.5:1 contrast ratio
4. 7:1 contrast ratio
</div>

??? question "Show Answer"
    The correct answer is **C**. WCAG AA level requires a minimum 4.5:1 contrast ratio for normal text to ensure readability for users with visual impairments. Option B (3:1) is the requirement for large text, option A is insufficient, and option D (7:1) is the enhanced AAA level for normal text, exceeding the minimum.

    **Concept Tested:** Font Colors for Readability

    **See:** [Font Colors for Readability](../../glossary.md#font-colors-for-readability)

---

#### 9. What is the recommended approach when a single taxonomy category contains 35% of all concepts in your learning graph?

<div class="upper-alpha" markdown>
1. Accept it as natural emphasis on an important topic
2. Review for over-representation and rebalance categories
3. Delete all concepts in the over-represented category
4. Change all concepts to use the same category
</div>

??? question "Show Answer"
    The correct answer is **B**. When a category exceeds 30% (the over-representation threshold), you should review it to identify concepts that could be consolidated, expand under-represented categories, or reclassify borderline concepts to achieve better balance. Option A ignores a quality issue, option C is unnecessarily destructive, and option D would eliminate the benefits of categorization.

    **Concept Tested:** Category Distribution

    **See:** [Category Distribution Analysis](../../glossary.md#category-distribution)

---

#### 10. Which script should you run to analyze whether your learning graph has balanced representation across taxonomy categories?

<div class="upper-alpha" markdown>
1. analyze-graph.py
2. csv-to-json.py
3. taxonomy-distribution.py
4. balance-categories.py
</div>

??? question "Show Answer"
    The correct answer is **C**. The taxonomy-distribution.py script analyzes the distribution of concepts across taxonomy categories, calculating percentages and identifying over- or under-represented categories. The analyze-graph.py script (option A) performs structural validation and quality scoring, csv-to-json.py (option B) converts formats, and option D is not a real script in the toolkit.

    **Concept Tested:** Python Scripts for Processing

    **See:** [Python Scripts for Processing](../../glossary.md#python-scripts-for-processing)

---

## Quiz Statistics

- **Total Questions:** 10
- **Bloom's Taxonomy Distribution:**
  - Remember: 3 questions (30%)
  - Understand: 3 questions (30%)
  - Apply: 3 questions (30%)
  - Analyze: 1 question (10%)
- **Concepts Covered:** 10 of 22 chapter concepts (45%)
