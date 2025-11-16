# Intelligent Textbook Creator

## Overview

The intelligent-textbook-creator skill guides the creation of intelligent, interactive textbooks using MkDocs with Material theme, learning dependency graphs, interactive p5.js simulations (MicroSims), and AI-assisted content generation workflows. It supports creating Level 2-5 intelligent textbooks following the five-level intelligence framework.

## Purpose

This skill provides a structured approach to transform educational content into intelligent learning experiences with progressive levels of sophistication, from basic interactivity (Level 2) to autonomous AI-generated personalized lessons (Level 5).

## Five Levels of Textbook Intelligence

1. **Level 1 - Static**: Text and images only (traditional textbooks)
2. **Level 2 - Interactive**: Hyperlinks, videos, quizzes, MicroSims, glossary, analytics ⭐ **PRIMARY FOCUS**
3. **Level 3 - Adaptive**: Personalized learning paths using concept dependency graphs
4. **Level 4 - AI Chatbot**: LLM-powered tutoring with GraphRAG architecture
5. **Level 5 - Autonomous**: Real-time AI-generated personalized lessons

## Core Concept: Learning Graphs

Learning graphs are Directed Acyclic Graphs (DAGs) where:

- **Nodes** = Concepts (abstract units of knowledge)
- **Edges** = Prerequisites (concept A must be learned before concept B)
- **Directed** = One-way relationships
- **Acyclic** = No circular dependencies

Learning graphs determine optimal teaching order and enable adaptive navigation for Level 3+ textbooks.

## The 5-Step Creation Workflow

### Step 1: Create Detailed Course Description

Define complete scope and structure with:
- Course title and tagline
- Target audience and personas
- Prerequisites
- Learning objectives aligned with Bloom's Taxonomy
- Key topics and concepts
- Assessment methods
- Capstone projects
- Technical requirements

### Step 2: Enumerate Concepts

Generate comprehensive inventory of 150-250 key concepts:
- Use Title Case format
- Number sequentially
- Order roughly foundational-to-advanced
- Include: Core concepts, terminology, tools, methods, patterns

### Step 3: Create Concept Dependency Graph

Map prerequisite relationships:
- CSV format: `ConceptID,ConceptLabel,Dependencies`
- Dependencies: Pipe-delimited list of prerequisite ConceptIDs
- Foundation concepts have empty Dependencies column
- Ensures no circular dependencies (must be DAG)

### Step 4: Create Concept Taxonomy

Organize into 10-12 thematic categories:
- Define category names and abbreviations
- Assign each concept to primary category
- Add TaxonomyID column to CSV
- Generate color-coded HTML legend

### Step 5: Generate Glossary

Create ISO 11179 compliant definitions:
- Term name
- Clear definition (1-2 sentences)
- Context and examples
- Related terms (cross-references)

## Technical Setup

### Installation

```bash
# Create conda environment
conda create -n mkdocs python=3
conda activate mkdocs
pip install mkdocs "mkdocs-material[imaging]"

# For social card generation (macOS)
brew install cairo freetype libffi libjpeg libpng zlib
export DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib
```

### Project Structure

```
my-textbook/
├── mkdocs.yml              # Main configuration
├── docs/
│   ├── index.md           # Home page
│   ├── glossary.md        # Term definitions
│   ├── concepts/          # Educational theory
│   ├── tutorial/          # Getting started
│   ├── workflows/         # Processes
│   ├── prompts/           # AI prompts
│   ├── sims/              # MicroSims
│   ├── css/extra.css      # Custom styling
│   └── js/extra.js        # Custom JavaScript
├── src/                   # Python utilities
└── plugins/               # Custom plugins
```

### Essential mkdocs.yml Configuration

```yaml
site_name: My Intelligent Textbook
site_url: https://username.github.io/my-textbook/

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
    - content.code.copy

plugins:
  - search
  - social

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences

extra_css:
  - css/extra.css
```

### Development Commands

```bash
mkdocs serve       # Local dev server (http://localhost:8000)
mkdocs build       # Build static site
mkdocs gh-deploy   # Deploy to GitHub Pages
```

## Creating Interactive MicroSims

MicroSims are self-contained p5.js simulations with two key regions:

1. **Drawing Region** (70% top): Canvas for visualization (aliceblue background)
2. **Control Region** (30% bottom): Interactive controls (white background)

### MicroSim Directory Structure

```
docs/sims/[sim-name]/
├── index.md           # Documentation page
├── main.html          # Standalone HTML
└── [sim-name].js      # p5.js code
```

### Design Specifications

- **Width**: ~670 pixels (fits MkDocs content area)
- **Height**: drawHeight + controlHeight
- **Border**: 2-pixel border for visual clarity
- **Responsive**: Use `windowResized()` handler
- **Library**: p5.js from CDN

## AI-Assisted Content Generation

The framework includes 18+ structured prompts:

### Core Learning Graph Prompts

Located in `docs/prompts/learning-graph/`:
1. **00-course-description.md**: Complete course specification
2. **01-personas.md**: User persona generation
3. **02-enumerate-concepts.md**: Generate 150-250 concepts
4. **03-dependency-graph.md**: Create prerequisite CSV
5. **04-taxonomy.md**: Organize into categories

### Additional Content Prompts

- Chapter content generation
- Quality metrics assessment
- FAQ creation
- Glossary generation with ISO 11179 definitions

## Deployment

### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

This will:
1. Build the static site
2. Create/update gh-pages branch
3. Push to GitHub
4. Make site live at `https://username.github.io/repo-name/`

## Quality Assessment

Evaluate textbooks across five dimensions:

1. **Intelligence Level** (L1-L5): Which features are implemented?
2. **Content Quality**: Accuracy, comprehensiveness, Bloom's coverage
3. **Pedagogical Effectiveness**: Scaffolding, assessments, feedback
4. **Technical Implementation**: Performance, accessibility, compatibility
5. **User Experience**: Navigation, design, engagement

## Advanced Features (Level 3-5)

### Level 3: Adaptive Learning
- User authentication and tracking
- Track concept mastery per user
- Use learning graph for personalized paths
- Recommend next concepts based on performance

### Level 4: AI Chatbot Integration
- Integrate Claude or GPT-4
- Implement GraphRAG (Graph-enhanced RAG)
- Context-aware tutoring
- Natural language Q&A

### Level 5: Autonomous Generation
- Real-time lesson generation
- Personalized MicroSim creation
- Reinforcement learning from user data
- Self-improving content

## Best Practices

### Content Organization
- Start with learning graph (Steps 1-5) before writing content
- Use concept dependencies to determine chapter order
- One concept per page or section
- Link related concepts explicitly

### MicroSim Design
- Keep interactions simple and intuitive
- Show concepts visually, don't just explain
- Include reset/restart functionality
- Provide visual feedback for all interactions
- Test on mobile devices

### AI-Assisted Content
- Use prompts iteratively, not one-shot
- Always review and edit AI output for accuracy
- Maintain consistent voice and style
- Fact-check technical accuracy
- Customize prompts for your specific domain

### Performance
- Optimize images (use WebP format)
- Lazy-load MicroSims where possible
- Minimize external dependencies
- Leverage MkDocs built-in caching

### Accessibility
- Add alt text to all images
- Use semantic HTML in custom components
- Ensure keyboard navigation works
- Test with screen readers
- Maintain WCAG-compliant color contrast

## Success Criteria

A successful intelligent textbook should:
- [ ] Implement Level 2 features minimum
- [ ] Include complete learning graph (150+ concepts with dependencies)
- [ ] Have dependency-driven content structure
- [ ] Include 5+ interactive MicroSims
- [ ] Provide comprehensive glossary
- [ ] Be deployed and publicly accessible
- [ ] Be mobile-responsive
- [ ] Follow accessibility guidelines (WCAG)
- [ ] Include clear learning objectives for each section

## Integration

This skill coordinates all other textbook creation skills:
- **course-description-analyzer**: Validates and scores course descriptions
- **learning-graph-generator**: Creates concept dependency graphs
- **book-chapter-generator**: Designs chapter structure
- **chapter-content-generator**: Generates detailed chapter content
- **microsim-p5**: Creates interactive simulations
- **glossary-generator**: Generates term definitions
- **quiz-generator**: Creates assessments
- **faq-generator**: Generates FAQs
- **reference-generator**: Adds academic references

## Key Principle

**Start with Level 2 (interactive content). The learning graph is the foundation that enables all higher levels. Don't attempt Level 5 features before establishing Level 2.**

## References

- MkDocs: https://www.mkdocs.org
- Material Theme: https://squidfunk.github.io/mkdocs-material/
- p5.js: https://p5js.org/reference/
- Bloom's Taxonomy: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/
