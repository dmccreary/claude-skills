# Intelligent Textbook

## Overview

The intelligent-textbook skill provides a comprehensive 12-step workflow for generating complete intelligent, interactive textbooks using AI assistance, from course description through concept mapping, dependency graphs, taxonomies, and interactive content creation with MicroSims.

## Purpose

This skill orchestrates the entire process of transforming a course idea into a complete, interactive intelligent textbook with structured learning paths, interactive visualizations, and AI-assisted content generation following educational best practices.

## Educational Foundations

Based on established educational frameworks:

- **Bloom's Taxonomy (2001)**: Six cognitive levels (Remember → Understand → Apply → Analyze → Evaluate → Create)
- **Scaffolding**: Building knowledge incrementally from prerequisites
- **Concept Dependencies**: Directed acyclic graphs (DAGs) showing learning prerequisites
- **Five Levels of Intelligence**: From static text (Level 1) to AI-powered personalization (Level 5)

## The 12-Step Workflow

### Foundation (Steps 1-2)
1. **Course Description Development**: Comprehensive foundation document with objectives, prerequisites, and outcomes
2. **Bloom's Taxonomy Integration**: Categorize learning objectives across cognitive levels

### Concept Mapping (Steps 3-6)
3. **Concept Enumeration**: Generate 150-250 key concepts in teaching order
4. **Concept Dependencies**: Create DAG showing prerequisite relationships
5. **Concept Taxonomy**: Organize into 10-12 thematic categories
6. **Learning Graph Visualization**: Interactive p5.js visualization of dependencies

### Content Development (Steps 7-9)
7. **Chapters and Sections Structure**: Organize learning graph into sequential textbook structure
8. **Content Generation for Sections**: Generate detailed educational content with examples, exercises, and assessments
9. **MicroSim Creation**: Build interactive p5.js simulations for key concepts

### Finalization (Steps 10-12)
10. **Site Assembly and Navigation**: Integrate content into MkDocs site with proper navigation
11. **Quality Assurance and Enhancement**: Review, test, and improve the complete textbook
12. **Deployment and Maintenance**: Publish to GitHub Pages and establish update processes

## Technology Stack

- **MkDocs with Material Theme**: Static site generation
- **p5.js**: Interactive simulations (MicroSims)
- **vis-network.js**: Learning graph visualization
- **Python**: Data processing scripts
- **GitHub Pages**: Hosting
- **Bash**: Utility scripts

## Key Features

- **Learning Graphs**: DAG-based concept dependencies for optimal teaching order
- **Interactive MicroSims**: p5.js simulations with educational focus
- **AI-Assisted Content**: Structured prompts for content generation
- **Multiple Learning Paths**: Support for different student backgrounds
- **Progressive Complexity**: Foundational to advanced concepts
- **Bloom's Alignment**: Content addressing all cognitive levels

## When to Use

Use this skill when users request:
- Creating educational content or textbooks
- Transforming course materials into interactive resources
- Building learning dependency graphs
- Developing comprehensive course materials
- Creating interactive educational simulations
- Implementing progressive levels of textbook intelligence

## Output Structure

```
docs/
├── index.md                    # Home page
├── tutorial/                   # MkDocs usage tutorials
├── concepts/                   # Educational concept explanations
├── chapters/                   # Main course content
│   ├── chapter-01/
│   │   ├── index.md
│   │   ├── section-01.md
│   │   └── section-02.md
│   └── chapter-02/
├── sims/                       # MicroSimulations
│   ├── index.md
│   ├── learning-graph/
│   └── [other-sims]/
├── workflow/                   # Documentation of this workflow
├── prompts/                    # Prompt library
├── css/extra.css              # Custom styling
├── js/extra.js                # Custom JavaScript
└── glossary.md                # Course glossary
```

## Quality Standards

A high-quality intelligent textbook should have:
- Comprehensive coverage of all enumerated concepts
- Logical progression following dependency graph
- Multiple Bloom's levels addressed
- Interactive elements (MicroSims, hands-on activities)
- Clear learning objectives for every chapter/section
- Scaffolded learning building from simple to complex
- Visual richness (diagrams, charts, visualizations)
- Practice opportunities at different difficulty levels
- Assessment alignment with objectives
- Professional, consistent formatting

## Success Criteria

- ✓ Comprehensive Coverage: All enumerated concepts explained
- ✓ Logical Progression: Content follows dependency graph
- ✓ Multiple Bloom's Levels: All cognitive levels addressed
- ✓ Interactive Elements: Includes MicroSims and activities
- ✓ Clear Objectives: Every chapter/section has measurable goals
- ✓ Scaffolded Learning: Builds from simple to complex
- ✓ Visual Richness: Diagrams, charts, visualizations included
- ✓ Practice Opportunities: Exercises at different levels
- ✓ Assessment Alignment: Tests match objectives and content
- ✓ Professional Presentation: Clean, consistent formatting
- ✓ Technical Quality: Builds without errors, all features work
- ✓ Maintainable: Well-organized, documented, version controlled

## Educational Principles

### Focused Scope
Each component addresses ONE specific learning objective. Don't attempt to teach an entire topic—focus on a single concept, relationship, or phenomenon.

### Immediate Feedback
Students must see the effects of their actions instantly. Simulations should update in real-time.

### Transparent Implementation
Code and explanations should be readable so educators and students can understand the underlying models.

### Progressive Complexity
Start with simple defaults that demonstrate core concepts. Allow students to increase complexity through parameter manipulation.

## Integration

This skill coordinates with all other skills in the suite:
- **course-description-analyzer**: Validates course foundations
- **learning-graph-generator**: Creates concept dependencies
- **book-chapter-generator**: Designs chapter structure
- **chapter-content-generator**: Generates detailed content
- **microsim-p5**: Creates interactive simulations
- **glossary-generator**: Generates term definitions
- **quiz-generator**: Creates assessments
- **reference-generator**: Adds academic references

## References

- [MkDocs Documentation](https://www.mkdocs.org)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [p5.js Reference](https://p5js.org/reference/)
- [Bloom's Taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)
