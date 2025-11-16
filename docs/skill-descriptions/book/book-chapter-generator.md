# Book Chapter Generator

## Overview

The book-chapter-generator skill generates optimal chapter structures for intelligent textbooks by analyzing course descriptions, learning graphs, and concept dependencies to distribute content evenly across 6-20 chapters while respecting prerequisite relationships.

## Purpose

This skill automates the design of chapter organization for educational textbooks, ensuring logical progression from foundational to advanced concepts based on the learning graph's directed acyclic graph (DAG) structure.

## Key Features

- **Prerequisite-Based Organization**: Chapters follow concept dependencies from the learning graph
- **Even Distribution**: Balances content across 6-20 chapters (typically 10-15 for most courses)
- **Taxonomy Integration**: Uses concept categories to group related topics
- **Chapter Structure**: Creates `/docs/chapters/` directory with numbered subdirectories
- **Chapter Metadata**: Generates index.md for each chapter with title, summary, and concept list

## When to Use

Use this skill after:
- Learning graph has been generated (learning-graph.json exists)
- Course description is finalized
- Concept taxonomy has been established
- Before generating chapter content

## Workflow Steps

### Step 1: Analyze Learning Graph
Reads the learning graph to understand:
- Total number of concepts (~200)
- Concept dependencies (DAG structure)
- Foundational vs advanced concepts
- Concept categories from taxonomy

### Step 2: Determine Chapter Count
Calculates optimal number of chapters based on:
- Total concepts (aim for 10-20 concepts per chapter)
- Course level (junior-high: 6-10, high school: 10-15, college: 12-18, graduate: 15-20)
- Natural topic boundaries
- User preferences

### Step 3: Group Concepts into Chapters
Organizes concepts following these principles:
- **Respect Dependencies**: Prerequisites must come before dependent concepts
- **Logical Grouping**: Related concepts (same taxonomy category) grouped together
- **Progressive Difficulty**: Foundational concepts early, advanced concepts later
- **Balanced Distribution**: Roughly equal concepts per chapter

### Step 4: Create Chapter Directory Structure
Generates folder hierarchy:
```
docs/chapters/
├── index.md                    # Table of contents
├── 01-introduction/
│   └── index.md               # Chapter 1 metadata
├── 02-foundational-concepts/
│   └── index.md               # Chapter 2 metadata
├── 03-core-principles/
│   └── index.md               # Chapter 3 metadata
└── ...
```

### Step 5: Generate Chapter Index Files
Creates index.md for each chapter containing:
- **Title**: Descriptive chapter title (Title Case)
- **Summary**: 2-3 sentence overview of chapter content
- **Concept List**: Numbered list of concepts covered (from learning graph)
- **Prerequisites**: Required prior knowledge
- **Learning Objectives**: What students will learn

### Step 6: Create Table of Contents
Generates `/docs/chapters/index.md` with:
- Overview of the textbook structure
- Numbered list of all chapters with summaries
- Concept count per chapter
- Estimated reading time

### Step 7: Update MkDocs Navigation
Adds chapter structure to mkdocs.yml:
```yaml
nav:
  - Chapters:
      - Overview: chapters/index.md
      - 1. Introduction: chapters/01-introduction/index.md
      - 2. Foundational Concepts: chapters/02-foundational-concepts/index.md
      - ...
```

## Chapter Organization Patterns

### Introductory Chapter (Chapter 1)
- Welcome and motivation
- Course overview
- Prerequisites review
- Key terminology introduction
- Roadmap for learning

### Foundational Chapters (2-4)
- Basic concepts with zero or few dependencies
- Core vocabulary
- Fundamental principles
- Simple examples

### Intermediate Chapters (5-10)
- Building on foundations
- Integration of concepts
- Real-world applications
- More complex examples

### Advanced Chapters (11+)
- High-dependency concepts
- Synthesis and integration
- Advanced techniques
- Capstone project preparation

## Quality Standards

A well-structured chapter organization should have:
- Clear progression from simple to complex
- No concept appears before its prerequisites
- Balanced chapter sizes (10-20 concepts each)
- Logical topic groupings
- Clear chapter titles that indicate content
- Comprehensive coverage of all learning graph concepts

## Output Files

1. `/docs/chapters/index.md`: Table of contents
2. `/docs/chapters/NN-chapter-name/index.md`: Chapter metadata files
3. Updated `mkdocs.yml`: Navigation structure

## Integration

This skill coordinates with:
- **learning-graph-generator**: Uses the DAG structure and concept list
- **chapter-content-generator**: Provides structure for content generation
- **glossary-generator**: Concepts align with glossary terms
- **quiz-generator**: Each chapter gets assessment aligned with concepts

## Best Practices

1. **Chapter Size**: Aim for 10-20 concepts per chapter (adjust for complexity)
2. **Naming**: Use descriptive, parallel chapter titles (all nouns or all gerunds)
3. **Dependencies**: Always verify prerequisites are in earlier chapters
4. **Taxonomy**: Group related taxonomy categories together when possible
5. **Balance**: Avoid one very short or very long chapter
6. **Preview**: Show what's coming in chapter summaries
7. **Review**: Reference earlier concepts when introducing new ones

## Example Chapter Structure

For a 200-concept course on Machine Learning:

1. **Introduction to Machine Learning** (12 concepts)
   - Foundational terminology, motivation, overview
2. **Mathematical Foundations** (18 concepts)
   - Linear algebra, calculus, probability
3. **Data Preprocessing** (15 concepts)
   - Cleaning, transformation, feature engineering
4. **Supervised Learning: Regression** (20 concepts)
   - Linear regression, polynomial, regularization
5. **Supervised Learning: Classification** (22 concepts)
   - Logistic regression, decision trees, SVM
6. **Unsupervised Learning** (18 concepts)
   - Clustering, dimensionality reduction
7. **Neural Networks** (20 concepts)
   - Perceptrons, backpropagation, activation functions
8. **Deep Learning** (25 concepts)
   - CNNs, RNNs, transformers
9. **Model Evaluation** (16 concepts)
   - Metrics, cross-validation, bias-variance
10. **Advanced Topics and Applications** (20 concepts)
    - Transfer learning, reinforcement learning, capstone

## References

- [Learning Graph Generator](./learning-graph-generator.md)
- [Chapter Content Generator](./chapter-content-generator.md)
- [Course Description Analyzer](./course-description-analyzer.md)
