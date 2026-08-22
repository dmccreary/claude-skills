# Glossary Quality Report

Assessment of the 570-term glossary generated from the 570-concept learning graph.

## Coverage

| Measure | Value |
|---------|-------|
| Terms defined | 570 |
| Concepts in the learning graph | 570 |
| Coverage | 100% |
| Definitions with no matching concept | 0 |

Every concept label in [learning-graph.csv](./learning-graph.csv) has exactly one
definition, and no definition exists for a term outside the graph.

## ISO 11179 Compliance

| Criterion | Result |
|-----------|--------|
| Precise | Definitions state meaning directly, without hedging |
| Concise | 81.2% fall within a 15-60 word band |
| Distinct | 0 duplicate definition bodies |
| Non-circular | 0 definitions restate their own full term |
| Free of business rules | Definitions describe what a term is, not who may use it |

Circularity is measured by checking whether a definition repeats the complete
term it defines. Partial word overlap (for example, the word "skill" appearing
in the definition of "Skill Packaging") is not circularity and is not counted.

## Definition Length

| Measure | Value |
|---------|-------|
| Mean | 17.4 words |
| Median | 17 words |
| Shortest | 9 words |
| Longest | 32 words |
| Within 15-60 words | 463 (81.2%) |
| Under 12 words | 18 |
| Over 60 words | 0 |

Lengths exclude the example sentence. The mean sits slightly below the 20-word
guidance, which reflects a deliberate bias toward brevity: conciseness is itself
an ISO 11179 criterion, and padding definitions to reach a word count would work
against precision.

## Examples and Structure

| Measure | Value |
|---------|-------|
| Terms with an example | 384 (67.4%) |
| Target range | 60-80% |
| Section dividers or category headers | 0 |
| Header levels other than the term header | 0 |
| Horizontal rules | 0 |

The glossary is a flat alphabetical list with no letter dividers and no thematic
grouping. Alphabetical order is the only organizing principle.

## Cross-Reference Integrity

All 143 glossary links elsewhere in `docs/` were re-checked after
regeneration. Anchors orphaned by term renaming were remapped to their current
equivalents. Zero broken glossary anchors remain.

## Recommendations

- 18 definitions fall under 12 words. Review whether each still fully
  conveys its meaning: Batch Screenshot Capture, Chapter Concept List, Claude Max Plan Limits, Comment System, CSV Parsing in Python, Freely-Licensed Images, GitHub Projects Kanban, MicroSim Quality Score, Multiple-Choice Question, Note and Tip Admonitions
- No definition exceeds the 60-word ceiling.
- No circular definitions were detected.
- Example coverage sits inside the target band; the terms still lacking an
  example are mostly script names and self-evident file roles.
