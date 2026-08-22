---
title: Learning Graphs and Concept Enumeration
description: Defines what a learning graph is, covers concept enumeration and label conventions, learning dependencies, and the learning-graph generator and its JSON schema.
generated_by: claude skill chapter-content-generator
date: 2026-08-22 15:20:00
version: 0.09
---

# Learning Graphs and Concept Enumeration

## Summary

This chapter defines what a learning graph is and introduces the learning-graph generator, then covers concept enumeration -- writing atomic, appropriately granular concept labels in Title Case under the length limit. It explains learning dependencies and how multiple valid learning pathways can exist through the same graph. Students will be able to enumerate a set of atomic concepts for a new topic after this chapter.

## Concepts Covered

This chapter covers the following 20 concepts from the learning graph:

1. Learning Graph
2. Concept
3. Learning Graph JSON Schema
4. Learning Graph Generator
5. Learning Graph as Roadmap
6. Concept Label
7. Atomic Concept
8. Concept Enumeration
9. Learning Dependency
10. Metadata Section
11. Multiple Learning Pathways
12. validate-learning-graph.py
13. Title Case Convention
14. Label Length Limit
15. Concept Granularity
16. Concept List File
17. ConceptID Field
18. Dependency Edge
19. Prerequisite Relationship
20. Concept Taxonomy

## Prerequisites

This chapter builds on concepts from:

- [1. Foundations of AI, Language Models, and Prompting](../01-foundations-ai-language-models/index.md)
- [3. Python Fundamentals for Skill Automation](../03-python-fundamentals-automation/index.md)
- [6. Agent Skill Fundamentals](../06-agent-skill-fundamentals/index.md)
- [7. Progressive Disclosure and Meta-Skill Routing](../07-progressive-disclosure-meta-skills/index.md)
- [12. Writing a Course Description](../12-writing-course-description/index.md)

---

!!! mascot-welcome "The map behind this entire book."
    ![Kit waves hello with their tool satchel](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every chapter you've read so far — its order, its prerequisites, even which concepts landed together — came from one structure. This chapter shows you that structure directly. Right tool, right task!

## What Is a Learning Graph?

A **learning graph** is a directed structure whose nodes are teachable ideas and whose arrows indicate which ideas should be understood before others. Each node is a **concept**: a single teachable idea in a course, small enough to be explained on its own and named with a short label. This book's own learning graph has 570 of them, and you can explore all of them below.

#### Diagram: This Book's Learning Graph

<iframe src="../../sims/graph-viewer/main.html" width="100%" height="560px" scrolling="no"></iframe>

<details markdown="1">
<summary>This Book's Learning Graph (reused MicroSim)</summary>
Type: graph-model
**sim-id:** graph-viewer<br/>
**Library:** vis-network<br/>
**Status:** Reused<br/>
**Source:** docs/sims/graph-viewer

Reused from this book's own MicroSim catalog — this is the live viewer for `learning-graph.json`, the actual 570-concept graph this book was generated from. Learning objective: Analyze the structure of a real learning graph, including its foundational nodes, taxonomy categories, and dependency chains.
</details>

Beyond powering chapter design, a learning graph works as a **learning graph as roadmap**: the use of a dependency structure as a navigational aid that shows a learner where they are and what must come next — that's exactly what the "Prerequisites" section at the top of every chapter in this book is doing for you.

## Concept Enumeration: Finding the Atomic Ideas

Building a graph like the one above starts with **concept enumeration**: the process of deriving the full set of teachable ideas from a course description, before any ordering is assigned. Each idea enumerated needs to be an **atomic concept**: a teachable idea that cannot be usefully divided further without losing meaning, making it a suitable single node — "Learning Graphs" is too broad to be one node; "Concept Enumeration" and "Learning Dependency" are each atomic enough to stand alone.

!!! mascot-thinking "Granularity is a dial, not a fixed rule."
    ![Kit thinking with a paw on their chin](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    **Concept granularity** is the chosen level of detail at which ideas are separated, balancing a graph that's too coarse to guide sequencing against one too fine to read. There's no universal right answer — a 570-concept graph like this book's is fine-grained enough to sequence 31 distinct chapters, but a shorter course might do just as well with 150.

## Writing a Concept Label

Once an idea is enumerated, it needs a **concept label**: the short name identifying it, written in title case and constrained in length so it displays legibly in a network diagram. That's two separate rules working together: the **Title Case Convention** — capitalization applying initial capitals to principal words, used for consistency across labels and headings — and the **label length limit**: the maximum character count for a node name, set so text fits inside a rendered box without truncation (32 characters, in this project's convention).

!!! mascot-tip "Write the label like a box, not a sentence."
    ![Kit holding up a tool with a knowing look](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    "The Concept of Tokenization in Language Models" will truncate in a network diagram. "Tokenization" won't. When in doubt, write the shortest label that's still unambiguous, and let the chapter prose carry the nuance.

Every enumerated concept gets a **ConceptID field**: the unique integer identifying it, used to reference it from dependency lists and graph files, and is recorded first in a **concept list file**: the numbered document listing every teachable idea with its identifier, produced for author review before dependencies are mapped — the raw material this book's own `concept-list.md` is built from.

## Learning Dependencies and Prerequisite Relationships

Once concepts exist, they need to be connected. A **learning dependency** is a relationship asserting that one idea should be understood before another can be taught effectively, recorded in the graph file as a **dependency edge**: the arrow representing a single ordering relationship between two ideas. Each edge encodes a **prerequisite relationship**: the specific pairing in which one idea must precede another, forming the basis of a recommended teaching order — exactly the relationships Chapter 17's chapter-structure design will later respect when it assigns concepts to chapters.

## Multiple Learning Pathways

A well-formed graph rarely has just one valid reading order. **Multiple learning pathways** is the property of a well-formed structure that several valid routes exist through the material, rather than one fixed sequence — two readers could study this book's concepts in a different order and both end up with every prerequisite satisfied, as long as neither skips ahead of a dependency.

## The Learning Graph Generator and Its JSON Schema

The **learning graph generator** is the skill that converts a course description into a validated graph with categories, quality reports, and a viewer-ready data file — the skill that produced the very graph rendered above. Its output must conform to the **learning graph JSON schema**: the formal description of the required structure of a graph file, used to validate generated output automatically, including a **metadata section**: the part of a graph file carrying descriptive information about the work, such as title, creator, date, and license.

!!! mascot-warning "Never trust a graph you haven't validated."
    ![Kit holding up a caution paw](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A generated graph can look plausible and still contain a structural defect. Always run **validate-learning-graph.py** — the program that checks a generated graph file against its formal schema and reports any structural violation — before treating a graph as ready for chapter design.

Finally, every concept gets grouped by a **concept taxonomy**: a set of categories used to group teachable ideas by subject area, providing color coding and distribution analysis — the 14 categories, from `FOUND` to `PUBLISH`, that colored every node in the viewer above.

## Key Takeaways

- A **learning graph** connects atomic **concepts** with directed edges, and doubles as a **roadmap** for readers.
- **Concept enumeration** produces **atomic concepts** at a deliberately chosen **granularity**, each written as a **concept label** following the **Title Case convention** and the **label length limit**, tracked by a **ConceptID** in a **concept list file**.
- A **learning dependency** becomes a **dependency edge** encoding a **prerequisite relationship**; a well-formed graph supports **multiple learning pathways**, not just one.
- The **learning graph generator** produces output conforming to the **learning graph JSON schema**, including a **metadata section** and a **concept taxonomy** — always checked by **validate-learning-graph.py** before it's trusted.

!!! mascot-celebration "You just read the map that built this book."
    ![Kit celebrating with arms raised](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    That graph you explored above isn't a diagram *about* this book — it's the actual structure that decided what you'd learn, and in what order, in every chapter so far. Right tool, right task!
