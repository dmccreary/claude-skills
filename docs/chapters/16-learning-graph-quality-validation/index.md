---
title: Learning Graph Quality Validation
description: Covers the Python scripts and structural checks that validate a learning graph, the quality score, and the review workflow that remediates defects before content generation.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 15:50:00
version: 0.09
---

# Learning Graph Quality Validation

## Summary

This chapter covers the quality checks a learning graph must pass: cycle detection, self-dependency checks, orphaned and disconnected nodes, indegree and outdegree analysis, and dependency chain length. It introduces the learning graph quality score, the interactive graph viewer, and the review workflow used to remediate a low-scoring graph. Students will be able to run the graph's quality checks and interpret the resulting report after this chapter.

## Concepts Covered

This chapter covers the following 19 concepts from the learning graph:

1. vis-network JSON Format
2. add-taxonomy.py Script
3. Self-Dependency Check
4. Disconnected Subgraph
5. Dependency Chain Length
6. Average Dependencies
7. Category Over-Representation
8. Learning Graph Viewer
9. csv-to-json.py Script
10. taxonomy-distribution.py
11. check-loops.py Script
12. Learning Graph Quality Score
13. Graph Legend and Colors
14. Concept Search in Viewer
15. Quality Metrics Report
16. analyze-graph.py Script
17. Graph Remediation
18. Graph Review Workflow
19. Concept List Review

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [7. Progressive Disclosure and Meta-Skill Routing](../07-progressive-disclosure-meta-skills/index.md)
- [14. Learning Graphs and Concept Enumeration](../14-learning-graphs-concept-enumeration/index.md)
- [15. Learning Graph Data Formats and Taxonomy](../15-learning-graph-formats-taxonomy/index.md)

---

!!! mascot-welcome "Trust, but verify the graph."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    A generated graph can look finished and still hide a defect. This chapter is the actual battery of checks this book's own 570-concept graph passed before a single chapter was structured. Right tool, right task!

## The Python Scripts Behind Quality Checks

Five small Python programs do this chapter's real work. The **analyze-graph.py script** examines a dependency file and reports structural measurements including loops, entry points, endpoints, and connectivity. The **csv-to-json.py script** converts the tabular dependency file into the viewer-ready format, generating the legend from category definitions. The **add-taxonomy.py script** assigns category abbreviations to rows of a dependency file. **taxonomy-distribution.py** counts ideas per category and writes a distribution report, flagging categories that exceed the share threshold. The **check-loops.py script** searches a dependency file specifically for closed paths and reports the identifiers involved in each.

| Script | What It Checks or Produces |
|--------|------------------------------|
| `analyze-graph.py` | Loops, entry points, endpoints, connectivity |
| `csv-to-json.py` | Viewer-ready JSON, with legend |
| `add-taxonomy.py` | Category assignment per row |
| `taxonomy-distribution.py` | Per-category counts and over-representation |
| `check-loops.py` | Specific cycle identifiers, if any exist |

## Structural Checks: Loops, Self-Dependencies, and Disconnection

Beyond a full cycle, one narrower bug is worth checking on its own: a **self-dependency check** verifies that no idea lists itself as its own prerequisite — an easy mistake to introduce by hand, and an easy one to miss by eye in a long CSV. A **disconnected subgraph** is a cluster of ideas linked to one another but not reachable from the main body of the structure — worse than a single orphaned node, because an entire cluster can look internally consistent while being invisible to every learning pathway that starts from a foundational concept. And at the taxonomy level, **category over-representation** is the condition in which one category holds a disproportionate share of all ideas, suggesting it should be subdivided — this book's own taxonomy report keeps every one of its 14 categories under 12% of the total, well below the 30% ceiling used as a quality threshold.

!!! mascot-warning "A self-dependency slips past a quick read every time."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Nobody writes "Tokenization depends on Tokenization" on purpose — it usually comes from a copy-paste error in a dependency cell. It's invisible in a casual read-through of a 570-row spreadsheet, which is exactly why it needs its own automated check rather than relying on a human catching it.

## Measuring Depth and Density

Two more numbers describe a graph's overall shape. **Dependency chain length** is the number of steps in the longest path from an entry point to a final idea, indicating how deep the material runs — this book's own graph has a maximum chain length of 25 steps, from a foundational concept like "Python" all the way to the capstone project concept. **Average dependencies** is the mean number of prerequisites per idea, used as a health measure; values that are too low suggest missing relationships that should have been captured during concept enumeration.

!!! mascot-thinking "Chain length tells you how far a reader has to travel."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    A chain length of 25 doesn't mean 25 chapters of straight-line reading — remember multiple learning pathways from Chapter 14. It means the *deepest* single thread of prerequisites is 25 steps long, which is exactly the kind of number that tells you a 31-chapter structure, not a 10-chapter one, is the right size for this material.

## The Learning Graph Quality Score

All of these checks roll up into one number: the **learning graph quality score**, a composite rating derived from structural checks such as absence of loops, connectivity, and dependency density. That score, along with the individual measurements behind it, is written to a **quality metrics report**: the generated document presenting structural measurements of a graph together with recommendations for improvement — this project's own quality gate for the entire learning graph stage of the pipeline.

## Reviewing Before You Build: Workflow and Remediation

Automated checks catch structural defects; they don't catch a concept that's simply wrong or a category that's misnamed. That's what the **graph review workflow** is for: the author-led inspection of a generated structure before content generation begins, when corrections are still inexpensive. Its cheapest phase happens earliest — **concept list review**: examining and editing the enumerated ideas before dependencies are assigned, since later changes propagate through every downstream artifact once chapters and content are built on top of them.

!!! mascot-tip "The earlier you catch a defect, the cheaper it is to fix."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Fixing a mislabeled concept during concept list review costs one edit. Fixing the same mislabeled concept after 31 chapters have already been written around it costs 31 edits. Review early, on purpose.

Whatever the report finds, fixing it is **graph remediation**: correcting structural defects a quality report identifies, such as removing a loop or connecting an isolated idea, then re-running the checks to confirm the fix actually worked.

## The Viewer's Own Features

The graph viewer you explored in Chapter 14 is itself an instance of the **vis-network JSON format**: the specific arrangement of nodes, edges, and groups expected by the JavaScript library that renders that interactive diagram. As a whole, it's a **learning graph viewer**: an interactive simulation that renders a graph file, allowing readers to pan, zoom, search, and inspect relationships, built on **graph legend and colors** — the key mapping each displayed color to its category, letting a reader interpret the diagram at a glance — and **concept search in viewer**: a control that locates a named idea within the rendered diagram and brings it into view. Scroll back to [Chapter 14's live viewer](../14-learning-graphs-concept-enumeration/index.md#what-is-a-learning-graph) and try searching for a concept from this chapter's own list — you'll see it highlighted, colored by category, exactly where these quality checks placed it.

## Key Takeaways

- Five scripts — **analyze-graph.py**, **csv-to-json.py**, **add-taxonomy.py**, **taxonomy-distribution.py**, and **check-loops.py** — do the actual structural checking.
- Beyond full cycles, watch for a **self-dependency**, a **disconnected subgraph**, and **category over-representation**.
- **Dependency chain length** and **average dependencies** describe a graph's depth and density; both roll up into the **learning graph quality score** and its **quality metrics report**.
- A **graph review workflow**, starting with cheap **concept list review**, catches what automated checks can't; **graph remediation** fixes what the checks do find.
- The **learning graph viewer** — built on the **vis-network JSON format**, with a **legend** and **concept search** — is where all of this becomes something a reader can actually explore.

!!! mascot-celebration "You could validate a new learning graph from scratch."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Every check in this chapter is one this book's own graph actually passed — zero cycles across 570 concepts and 1,137 edges. You now know exactly how to prove that for a graph of your own. Right tool, right task!
