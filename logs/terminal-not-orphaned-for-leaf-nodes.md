# Terminology Update: Terminal Nodes vs. Orphaned Nodes

**Date:** 2026-03-16
**Task:** Rename "orphaned node" (outdegree=0) to "terminal node" across the entire repository and establish precise new definitions for both terms.

## New Definitions

- **Terminal node**: A node with no outbound edges (outdegree=0) but has inbound edges. Nothing depends on it, but it has prerequisites. Valid and expected in learning graphs — represents culminating or specialized concepts at the end of a dependency chain.
- **Orphaned node**: A node with NO inbound AND no outbound edges (zero total edges). Completely disconnected from the graph, making the learning graph invalid. Must be fixed.

## Motivation

The old definition conflated two distinct concepts. Nodes with outdegree=0 were called "orphaned," implying a problem, when in fact they are natural endpoints in a learning path (5-15% is healthy). True orphans — completely disconnected nodes — are the actual quality issue. The rename makes the terminology precise, consistent with graph theory, and eliminates confusion in educational content.

## Files Updated (~40+ files across 10 parallel agents)

### Core Definitions
| File | Changes |
|------|---------|
| `CLAUDE.md` | Quality metrics: added terminal node definition, redefined orphan |
| `docs/glossary.md` | Redefined "Orphaned Nodes", added new "Terminal Nodes" entry |

### Skills
| File | Changes |
|------|---------|
| `skills/learning-graph-generator/SKILL.md` | Updated terminal node guidance |
| `skills/learning-graph-generator/analyze-graph.py` | Renamed `find_orphaned_nodes` → `find_terminal_nodes`, all variables and report text |
| `skills/learning-graph-generator/validate-learning-graph.py` | Clarified orphan = completely disconnected (correct usage kept) |
| `skills/learning-graph-generator/README.md` | Updated sample output |
| `skills/book-chapter-generator/SKILL.md` | "Orphaned concepts" → "Terminal concepts" in 3 locations |

### Chapter Content
| File | Changes |
|------|---------|
| `docs/chapters/06-learning-graph-quality-validation/index.md` | Section header, definitions, percentages, quality scoring, MicroSim references, best practices |
| `docs/chapters/06-learning-graph-quality-validation/quiz.md` | Quiz questions 3 and 4 rewritten with new terminology |
| `docs/chapters/07-taxonomy-data-formats/index.md` | Python variable names `orphaned_pct` → `terminal_pct` |
| `docs/chapters/index.md` | Chapter 6 description |

### Learning Graph Data
| File | Changes |
|------|---------|
| `docs/learning-graph/concept-list.md` | "83. Orphaned Nodes" → "83. Terminal Nodes" |
| `docs/learning-graph/learning-graph.csv` | Concept label updated |
| `docs/learning-graph/learning-graph.json` | Node label updated |
| `docs/learning-graph/quality-metrics.md` | Section header and recommendation text |
| `docs/learning-graph/analyze-graph.py` | Function and variable renames (mirrors skills version) |
| `docs/learning-graph/validate-learning-graph.py` | Clarified orphan messaging (correct usage kept) |
| `docs/learning-graph/diagrams.csv` | Diagram name |
| `docs/learning-graph/diagram-table.md` | Link text |
| `docs/learning-graph/diagram-details.md` | Heading and description |
| `docs/learning-graph/diagrams.html` | Table cell text |
| `docs/learning-graph/faq-quality-report.md` | Concept reference |
| `docs/learning-graph/faq-coverage-gaps.md` | Reference text |
| `docs/learning-graph/microsim-quality-report.md` | MicroSim name |
| `docs/learning-graph/progress.md` | Quality assessment notes |
| `docs/learning-graph/details-analysis.md` | Summary and purpose text |

### Quiz and FAQ Data
| File | Changes |
|------|---------|
| `docs/learning-graph/quizzes/chapter-06-quiz-metadata.json` | Question text, concept names, source links |
| `docs/learning-graph/quiz-bank.json` | Question text and concept references |
| `docs/learning-graph/faq-chatbot-training.json` | FAQ answers rewritten with new definitions |
| `docs/faq.md` | FAQ section rewritten, percentage guidance updated |

### MicroSims
| File | Changes |
|------|---------|
| `docs/sims/orphaned-nodes-identification/main.html` | All labels, variables, annotations (directory name kept for URL stability) |
| `docs/sims/orphaned-nodes-identification/index.md` | Title, description, all content |
| `docs/sims/orphaned-nodes-identification/metadata.json` | Title, description, learning objectives |
| `docs/sims/index.md` | Listing title and description |
| `docs/sims/graph-viewer/index.md` | Clarified orphan = completely disconnected (correct usage) |
| `docs/sims/learning-graph-quality-score-calculator-microsim/*.js` | Slider label |

### Configuration and Navigation
| File | Changes |
|------|---------|
| `mkdocs.yml` | Nav text updated |

### Batch Scripts and Utilities
| File | Changes |
|------|---------|
| `src/microsim-batch/batch-add-lesson-plans.py` | Lesson plan content updated |
| `src/utilities/batch-add-lesson-plans.py` | Same changes |

### Prompts and Specs
| File | Changes |
|------|---------|
| `docs/prompts/generate-content-for-6-7.md` | ~20 edits across all orphaned→terminal references |
| `docs/prompts/generate-chapter-structure.md` | Chapter 6 description (2 locations) |
| `docs/learning-graph/medium-diagrams/specs/06-orphaned-nodes-identification-chart.md` | Content updated, file renamed to `06-terminal-nodes-identification-chart.md` |
| `docs/learning-graph/medium-diagrams/generation-report.md` | Chart title |
| `docs/learning-graph/medium-diagrams/execution-plan.md` | Chart title and spec reference |
| `docs/skill-descriptions/book/learning-graph-generator.md` | Description distinguishes terminal from orphaned |
| `docs/workshops/intelligent-textbook-cheat-sheet.md` | Clarified orphan definition |

### Log Files
| File | Changes |
|------|---------|
| `logs/generate-diagrams.md` | Chart titles and descriptions |
| `logs/medium-diagram-generation.md` | Chart title |
| `logs/session-final-summary.md` | Chart title |

## Intentionally Unchanged

- **Directory name** `docs/sims/orphaned-nodes-identification/` — kept for URL stability
- **CSS class names** (`.orphaned`, `.orphaned-card`) — internal styling hooks only
- **Image file paths** — reference existing PNG files
- **`validate-learning-graph.py`** (both copies) — correctly uses "orphaned" for truly disconnected nodes (zero edges)
- **`docs/sims/graph-viewer/script.js`** — correctly identifies fully disconnected nodes as orphans
- **`docs/prompts/update-skill-descriptions.md`** — uses "orphaned file" in plain English sense (not graph terminology)
- **Shell script directory lists** (`batch-capture-screenshots.sh`, etc.) — reference directory names

## Approach

Used 10 parallel agents to update all files simultaneously, grouped by functional area. Final grep verification confirmed all remaining "orphan" references are either directory paths, correct usage of the new orphan definition, or plain English usage unrelated to graph theory.
