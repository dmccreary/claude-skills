# Book Build Workflow

## Overview

This interactive workflow diagram illustrates the complete process for building an intelligent textbook, from initial course description through final book metrics. The visualization shows the dependencies and sequence of steps required to create a comprehensive educational resource.

## Interactive Diagram

<iframe src="main.html" width="100%" height="1000px" scrolling="no"></iframe>
[Run the Book Build Workflow Fullscreen](main.html)

## Workflow Description

The book building process follows a structured, multi-phase approach that ensures comprehensive coverage and quality:

## Workflow Diagram Description Summary

This diagram illustrates the complete workflow for building an intelligent textbook,
from initial course description through final book metrics. The process begins with
creating a course description, which informs the learning graph generation. The learning
graph then guides the chapter structure, and individual chapters are developed in parallel.
Once content is complete, supporting materials (glossary, FAQ, quizzes, references) are
generated sequentially, while diagrams are created and analyzed for book metrics.


### Phase 1: Foundation

1. **Course Description** - The starting point where learning objectives, target audience, prerequisites, and course scope are defined
2. **Learning Graph** - A comprehensive concept dependency graph generated from the course description, typically containing 200+ interconnected concepts organized by Bloom's Taxonomy levels

### Phase 2: Structure

3. **Chapter Structure** - The learning graph is analyzed to create an optimal chapter organization that respects concept dependencies and distributes content evenly across 6-20 chapters

### Phase 3: Content Development

4. **Chapter 1, Chapter 2, etc.** - Individual chapters are developed in parallel, with each containing:
   - Concept-aligned content at appropriate reading level
   - Diagrams and infographics
   - Interactive MicroSims
   - Examples and exercises

5. **Content Complete** - A milestone indicating that all chapter content has been written and reviewed

### Phase 4: Supporting Materials

From the content complete milestone, two parallel tracks begin:

**Educational Resources Track:**
6. **Glossary** - Comprehensive term definitions following ISO 11179 standards, generated from learning graph concepts
7. **FAQ** - Frequently asked questions derived from course content, concepts, and common student queries
8. **Quizzes** - Chapter-based assessments with questions aligned to specific concepts and distributed across Bloom's Taxonomy levels
9. **References** - Curated, level-appropriate academic and professional resources

**Quality Assurance Track:**
10. **Diagrams** - Analysis and documentation of all visual elements and MicroSims
11. **Book Metrics** - Comprehensive statistics on chapters, concepts, word counts, assessments, and visualizations

## Workflow Steps

The diagram shows these key sequential and parallel processes:

- **Sequential Foundation**: Course Description → Learning Graph → Chapter Structure (must be done in order)
- **Parallel Chapter Development**: Chapters can be written concurrently once structure exists
- **Convergence Point**: All chapters feed into "Content Complete" milestone
- **Dual Completion Tracks**: Educational resources and quality metrics proceed independently after content completion

## Key Concepts

This workflow demonstrates several important project management and educational design principles:

- **Concept Dependencies**: Each step builds on previous work (e.g., learning graph informs chapter structure)
- **Parallel Processing**: Chapters can be developed simultaneously to accelerate timelines
- **Quality Gates**: "Content Complete" serves as a milestone before generating supporting materials
- **Comprehensive Coverage**: Both student-facing resources (glossary, FAQ) and quality metrics are generated
- **Systematic Approach**: Following this workflow ensures no critical components are omitted

## Related Concepts

- **Learning Graphs**: Concept dependency visualization
- **Bloom's Taxonomy**: Cognitive learning level classification
- **MicroSims**: Interactive educational simulations
- **Dublin Core Metadata**: Standardized resource description
- **ISO 11179**: Metadata registry standards for definitions

## Technical Details

- **Diagram Type**: Mermaid flowchart (top-down layout)
- **Nodes**: 12 process steps/milestones
- **Edges**: 12 dependencies/relationships
- **Styling**: Aliceblue backgrounds (#f0f8ff) for all nodes
- **Font Size**: 16px for optimal readability in iframe embedding

## Usage Notes

- Use zoom controls to examine details
- Click "Export SVG" to save a high-quality vector graphic
- Keyboard shortcuts: Ctrl/Cmd + Plus (zoom in), Ctrl/Cmd + Minus (zoom out), Ctrl/Cmd + 0 (reset)
