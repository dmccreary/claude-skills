---
title: Learning Graph Data Formats and Taxonomy
description: Covers the CSV and vis-network JSON formats that encode a learning graph, directed acyclic graph structure, cycle detection, and taxonomy categorization.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 15:35:00
version: 0.09
---

# Learning Graph Data Formats and Taxonomy

## Summary

This chapter covers the pipe-delimited CSV format and the vis-network JSON format -- nodes, edges, groups, and metadata sections -- that together encode a learning graph. It explains TaxonomyID assignment, taxonomy category naming, and the `taxonomy-names.json` and `color-config.json` files that drive the graph viewer's legend. Students will be able to convert a CSV learning graph into vis-network JSON after this chapter.

## Concepts Covered

This chapter covers the following 20 concepts from the learning graph:

1. Dublin Core Metadata
2. JSON Schema Validation
3. Pipe-Delimited Dependencies
4. Directed Acyclic Graph
5. TaxonomyID
6. Taxonomy Category Naming
7. Nodes Section
8. Edges Section
9. Learning Graph CSV Format
10. Cycle Detection
11. Foundational Concept
12. Terminal Node
13. Orphaned Node
14. Linear Chain Detection
15. Indegree Analysis
16. Outdegree Analysis
17. Taxonomy Distribution
18. taxonomy-names.json File
19. color-config.json File
20. Groups Section

## Prerequisites

This chapter builds on concepts from:

- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [14. Learning Graphs and Concept Enumeration](../14-learning-graphs-concept-enumeration/index.md)

---

!!! mascot-welcome "Same graph, two file formats."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A learning graph starts life as a spreadsheet a human can review, then becomes a JSON file a browser can render. This chapter shows you both, and how they're checked for correctness. Right tool, right task!

## Two Formats, One Graph

Authors review a learning graph as the **learning graph CSV format**: a tabular file holding one row per teachable idea with its identifier, label, prerequisite list, and category — easy to skim, sort, and edit in a spreadsheet. Because a single concept can have several prerequisites, that prerequisite list uses **pipe-delimited dependencies**: a storage convention listing several prerequisite identifiers in one spreadsheet cell separated by vertical bars, like `13|31` meaning "depends on concepts 13 and 31."

```csv
ConceptID,ConceptLabel,Dependencies,TaxonomyID
33,Level 2 Interactive Content,13|32,FOUND
```

That single CSV row expands into three separate places once converted to JSON. The **nodes section** lists every teachable idea with its identifier, label, and category assignment; the **edges section** lists every ordering relationship as a pair of identifiers; the **groups section** defines each category's display name, color, and font, which together form the legend you saw in Chapter 14's graph viewer.

## Directed Acyclic Graphs and Cycle Detection

For a dependency structure to produce a valid teaching order at all, it must be a **directed acyclic graph**: a structure of nodes and one-way arrows containing no path that returns to its starting node, guaranteeing a valid ordering exists. Checking that property is **cycle detection**: checking a directed structure for any closed loop, which would make a consistent teaching order impossible — if concept A depends on B, B depends on C, and C depends back on A, there's no valid place to start.

!!! mascot-thinking "A cycle means the graph is asking for something impossible."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Picture a cycle as three people who each refuse to speak until the person before them has spoken — the conversation can never start. That's exactly why cycle detection isn't optional polish; a graph with even one cycle simply cannot be taught in any order.

#### Diagram: Three-Color DFS Cycle Detection

<iframe src="../../sims/three-color-dfs/main.html" width="100%" height="520px" scrolling="no"></iframe>

<details markdown="1">
<summary>Three-Color DFS Cycle Detection (reused MicroSim)</summary>
Type: graph-model
**sim-id:** three-color-dfs<br/>
**Library:** vis-network<br/>
**Status:** Reused<br/>
**Source:** docs/sims/three-color-dfs

Reused from this book's own MicroSim catalog. Learning objective: Analyze how the three-color depth-first-search algorithm marks nodes to detect a cycle in a learning graph.
</details>

## Where a Graph Begins and Ends

Some structural roles matter enough to have their own names. A **foundational concept** is a teachable idea with no prerequisites, serving as an entry point where a learner can begin — this book's own graph has six of them, including "Artificial Intelligence" and "Git." A **terminal node** is a teachable idea that has prerequisites but that nothing else depends on, representing a natural endpoint of a route. An **orphaned node** is a teachable idea with no incoming and no outgoing arrows, disconnected from the rest of the structure — and unlike a foundational or terminal node, it always indicates a defect rather than a valid structural role.

!!! mascot-warning "An orphaned node is invisible to every learning pathway."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A concept with zero connections in either direction can never be reached by any learning pathway and never leads anywhere either — it's dead weight in the graph. Always check for orphaned nodes before treating a graph as finished; they're easy to miss by eye in a graph with hundreds of concepts.

One more pattern worth flagging is **linear chain detection**: identifying long runs where each idea depends only on the one immediately before it, which suggests missing relationships and a single rigid route rather than the richer, more connected structure a real subject usually has.

## Measuring Structure: Indegree and Outdegree

Two simple counts reveal a lot about a graph's shape. **Indegree analysis** counts how many ideas depend on each idea, revealing which are most heavily relied upon and therefore most important to explain well. **Outdegree analysis** counts how many prerequisites each idea declares, revealing ideas that may be too demanding to introduce at one point if that count runs unusually high.

## Validating the Shape: JSON Schema

Before any of these checks run, the file itself has to be well-formed. **JSON schema validation** is checking a structured data file against a formal description of its required shape, catching missing or malformed fields automatically — before cycle detection or indegree analysis can even run meaningfully. Every valid graph file also carries **Dublin Core metadata**: a standard set of descriptive fields such as title, creator, date, and rights, used to make the resource identifiable and citable, living inside the metadata section you met in Chapter 14.

## Taxonomy: TaxonomyID, Naming, and Distribution

Every concept also belongs to a category. A **TaxonomyID** is a short uppercase abbreviation identifying that category, used in the data files and as the group key in a rendered diagram — `FOUND`, `LGRAPH`, `MSIM`, and the other codes you've seen in every chapter's concept list so far. Choosing those codes well is **taxonomy category naming**: choosing descriptive category names that communicate their contents to a reader rather than only to the system.

!!! mascot-tip "A good category name explains itself before you open it."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    "Learning Graphs" tells a reader what's inside; "Category 7" doesn't. Spend the extra thirty seconds naming a taxonomy category something a stranger could guess correctly.

#### Diagram: Taxonomy Distribution

<iframe src="../../sims/taxonomy-distribution-pie/main.html" width="100%" height="460px" scrolling="no"></iframe>

<details markdown="1">
<summary>Taxonomy Distribution (reused MicroSim)</summary>
Type: chart
**sim-id:** taxonomy-distribution-pie<br/>
**Library:** Chart.js<br/>
**Status:** Reused<br/>
**Source:** docs/sims/taxonomy-distribution-pie

Reused from this book's own MicroSim catalog. Learning objective: Evaluate whether any single taxonomy category dominates this book's 570-concept graph, using its actual **taxonomy distribution** — the count and percentage of ideas falling into each category, used to detect imbalance.
</details>

Two small files keep that whole system consistent across regenerations. The **taxonomy-names.json file** maps short category abbreviations to human-readable names, required so reports and diagram legends display meaningful labels instead of raw codes. The **color-config.json file** stores the assignment of a display color to each category, ensuring the same category keeps the same color every time the graph is regenerated — without it, "FOUND" might render blue one week and orange the next.

## Key Takeaways

- The **CSV format**, using **pipe-delimited dependencies**, is what an author edits; it converts into a JSON file's **nodes**, **edges**, and **groups sections**.
- A valid graph must be a **directed acyclic graph**, confirmed by **cycle detection**; **JSON schema validation** and **Dublin Core metadata** check the file's shape and provenance.
- **Foundational concepts**, **terminal nodes**, and (as a defect) **orphaned nodes** are structural roles; **linear chain detection**, **indegree**, and **outdegree analysis** reveal shape problems.
- A **TaxonomyID** and thoughtful **taxonomy category naming** organize concepts; **taxonomy distribution** checks for imbalance, kept consistent via **taxonomy-names.json** and **color-config.json**.

!!! mascot-celebration "You can now read a raw learning graph file cover to cover."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    CSV or JSON, nodes or edges, TaxonomyID or full category name — none of it is a mystery anymore. Right tool, right task!
