# Learning Graph

The learning graph captures how concepts in {{SITE_NAME}} depend on each
other. It is a Directed Acyclic Graph (DAG) — every concept has a path back to
one or more foundational concepts that have no prerequisites.

Once the `learning-graph-generator` skill runs, this section will be populated
with:

- **Course Description Assessment** — quality review of `course-description.md`
- **Concept Enumeration** — the ~200 concepts the book will cover
- **Concept Taxonomy** — concepts grouped into 8–12 categories
- **Graph Quality Analysis** — DAG structure, foundational and terminal nodes
- **Taxonomy Distribution** — concept count per taxonomy category

Use the `book-installer` skill (option 23) to add an interactive graph viewer
once `learning-graph.json` exists.
