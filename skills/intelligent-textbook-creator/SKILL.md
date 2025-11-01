---
name: "intelligent-textbook-creator"
description: "This skill should be used when someone wants to create an intelligent, interactive textbook using MkDocs Material theme with learning graphs, MicroSims (p5.js simulations), and AI-assisted content generation. Supports creating Level 2-5 intelligent textbooks following the five-level intelligence framework."
---

# Intelligent Textbook Creator

Create intelligent, interactive textbooks using MkDocs with Material theme, learning dependency graphs, interactive p5.js simulations (MicroSims), and AI-assisted content generation workflows.

## When to Use This Skill

Use this skill when someone wants to:
- Create an interactive educational textbook or course material
- Transform static educational content into intelligent learning experiences
- Build learning dependency graphs showing concept prerequisites
- Add interactive simulations (MicroSims) to educational content
- Generate structured educational content using AI prompts
- Implement progressive levels of textbook intelligence (Levels 2-5)

## Overview of Intelligent Textbooks

Intelligent textbooks progress through five levels of sophistication:

1. **Level 1 - Static**: Text and images only (skip this - traditional textbooks)
2. **Level 2 - Interactive**: Hyperlinks, videos, quizzes, MicroSims, glossary, analytics **(PRIMARY FOCUS)**
3. **Level 3 - Adaptive**: Personalized learning paths using concept dependency graphs
4. **Level 4 - AI Chatbot**: LLM-powered tutoring with GraphRAG architecture
5. **Level 5 - Autonomous**: Real-time AI-generated personalized lessons

Start with Level 2 (interactive content) as the foundation. Higher levels build upon this base.

## Core Concept: Learning Graphs

Learning graphs are **Directed Acyclic Graphs (DAGs)** where:
- **Nodes** = Concepts (abstract units of knowledge)
- **Edges** = Prerequisites (concept A must be learned before concept B)
- **Directed** = One-way relationships
- **Acyclic** = No circular dependencies

Learning graphs determine optimal teaching order and enable adaptive navigation for Level 3+ textbooks.

## The 5-Step Creation Workflow

Follow this sequential process to create an intelligent textbook:

### Step 1: Create Detailed Course Description

Define the complete scope and structure of the course.

**Required Components**:
- Course title and tagline
- Target audience and personas
- Prerequisites
- Learning objectives aligned with Bloom's Taxonomy (Remember → Understand → Apply → Analyze → Evaluate → Create)
- Key topics and concepts
- Assessment methods
- Capstone projects
- Technical requirements

**Reference**: See `references/prompts-guide.md` for the full course description template (prompt 00).

**Bloom's Taxonomy** ensures comprehensive coverage from foundational recall to higher-order thinking. Each level uses specific action verbs (define, explain, apply, analyze, evaluate, create).

### Step 2: Enumerate Concepts

Generate a comprehensive inventory of 150-250 key concepts.

**Process**:
- List all concepts in roughly foundational-to-advanced order
- Use Title Case for concept labels
- Number sequentially
- Include: Core concepts, terminology, tools, methods, patterns

**Output Format**:
```
1. Foundation Concept A
2. Foundation Concept B
3. Basic Term X
...
250. Advanced Application Z
```

**Reference**: Use prompt 02 from `references/prompts-guide.md`.

### Step 3: Create Concept Dependency Graph

Map prerequisite relationships between concepts.

**Process**:
- Create CSV with structure: `ConceptID,ConceptLabel,Dependencies`
- Dependencies column: Pipe-delimited list of prerequisite ConceptIDs (e.g., `1|2|5`)
- Foundation concepts have empty Dependencies column
- Ensures no circular dependencies (must be DAG)

**Example CSV**:
```csv
ConceptID,ConceptLabel,Dependencies
1,Foundation Concept A,
2,Foundation Concept B,
3,Intermediate Concept,1|2
4,Advanced Concept,3
```

**Reference**: Use prompt 03 from `references/prompts-guide.md`.

**This CSV determines optimal teaching order** using topological sorting algorithms.

### Step 4: Create Concept Taxonomy

Organize concepts into 10-12 thematic categories for better navigation.

**Process**:
- Define category names (e.g., "Foundation Concepts", "Terms & Definitions", "Advanced Techniques")
- Assign each concept to its primary category
- Add TaxonomyID column to CSV
- Generate color-coded HTML legend

**Reference**: Use prompt 04 from `references/prompts-guide.md`.

### Step 5: Generate Glossary

Create ISO 11179 compliant definitions for all concepts.

**For each concept include**:
- Term name
- Clear definition (1-2 sentences)
- Context and examples
- Related terms (cross-references)

**Output**: `docs/glossary.md` with alphabetically sorted, linked terms.

## Technical Setup

### Initial Installation

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

Create this directory structure:

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
│   │   └── learning-graph/
│   ├── sims/              # MicroSims
│   │   ├── templates/
│   │   └── [sim-name]/
│   │       ├── index.md
│   │       ├── main.html
│   │       └── [sim-name].js
│   ├── css/
│   │   └── extra.css
│   └── js/
│       └── extra.js
├── src/                   # Python utilities
└── plugins/               # Custom plugins
```

### Configure mkdocs.yml

Essential configuration (see `references/mkdocs-config.md` for complete example):

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

MicroSims are self-contained p5.js simulations that make concepts interactive and visual.

### MicroSim Directory Structure

For each simulation:
```
docs/sims/[sim-name]/
├── index.md           # Documentation page
├── main.html          # Standalone HTML
└── [sim-name].js      # p5.js code
```

### MicroSim Design Specifications

- **Width**: ~670 pixels (fits MkDocs content area)
- **Layout**: Two regions
  - Top 70%: Drawing region (aliceblue background)
  - Bottom 30%: Controls (white background)
- **Border**: 2-pixel border for visual clarity
- **Responsive**: Use `windowResized()` handler
- **Library**: p5.js from CDN

### Implementation Templates

See `references/microsim-templates.md` for:
- Complete main.html boilerplate
- Standard p5.js code pattern
- Responsive canvas sizing
- Interaction handling
- Embedding instructions

### Common MicroSim Types

Prioritize creating these useful simulations:
1. **Learning Graph Viewer**: Interactive DAG visualization
2. **Bloom's Taxonomy Pyramid**: Cognitive level hierarchy
3. **Concept Explorer**: Click to view prerequisites
4. **Progress Tracker**: Visual learning path
5. **Process Flowcharts**: Animated workflows

## Using AI Prompts for Content Generation

The framework includes 18+ structured prompts for AI-assisted content creation.

### Core Learning Graph Prompts (5 sequential)

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

**Reference**: Complete prompt catalog in `references/prompts-guide.md`.

### How to Use Prompts

1. Copy prompt text from markdown files
2. Replace placeholders with course-specific information
3. Submit to AI (Claude, GPT-4, etc.)
4. Review and refine output
5. Integrate into textbook structure

**Example Workflow**:
```
Course Description (prompt 00)
  → Enumerate Concepts (prompt 02)
    → Dependency Graph (prompt 03)
      → Taxonomy (prompt 04)
        → Complete Learning Graph!
```

## Deployment

### Deploy to GitHub Pages

Single command deployment:
```bash
mkdocs gh-deploy
```

This will:
1. Build the static site
2. Create/update gh-pages branch
3. Push to GitHub
4. Make site live at `https://username.github.io/repo-name/`

### Iterative Development

1. Add content → `mkdocs serve` to preview locally
2. Test MicroSims in browser
3. Commit changes to main branch
4. Deploy with `mkdocs gh-deploy`
5. Repeat

## Quality Assessment

Evaluate textbooks across five dimensions:

1. **Intelligence Level** (L1-L5): Which features are implemented?
2. **Content Quality**: Accuracy, comprehensiveness, Bloom's coverage
3. **Pedagogical Effectiveness**: Scaffolding, assessments, feedback
4. **Technical Implementation**: Performance, accessibility, compatibility
5. **User Experience**: Navigation, design, engagement

**Reference**: See `references/quality-framework.md` for the 20-question assessment framework.

## Python Utilities

Leverage analytical tools in `src/site-analytics/`:

- **get-metrics-json.py**: Basic metrics (word count, images, MicroSims, glossary)
- **advanced-metrics.py**: Comprehensive quality assessment
- **sort-glossary.py**: Alphabetize glossary
- **csv-to-json.py**: Format conversion for learning graphs

## Advanced Features (Level 3-5)

Once Level 2 is complete, implement higher levels:

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

**Reference**: See `references/advanced-features.md` for implementation details.

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

## Troubleshooting

### MkDocs Build Issues
```bash
rm -rf site/     # Clear cache
mkdocs build     # Rebuild
```

### MicroSim Not Loading
- Check browser console for JavaScript errors
- Verify p5.js CDN URL is accessible
- Test in incognito mode (cache issues)

### GitHub Pages Not Updating
```bash
mkdocs gh-deploy --force
```

### Dependency Graph Errors
- Check for circular dependencies
- Validate all ConceptIDs exist
- Ensure pipe delimiter (|) in Dependencies
- Verify CSV format

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

## Example Complete Workflow

### Day 1: Foundation
1. Install MkDocs and dependencies
2. Create project structure
3. Write detailed course description (Step 1)
4. Define learning objectives using Bloom's Taxonomy

### Day 2: Concept Mapping
5. Enumerate 150-250 concepts (Step 2)
6. Create dependency graph CSV (Step 3)
7. Define taxonomy categories (Step 4)
8. Validate graph (no cycles, all connected)

### Day 3: Initial Content
9. Generate glossary from concepts (Step 5)
10. Create home page and navigation
11. Write first chapter using AI prompts
12. Test with `mkdocs serve`

### Day 4: Interactivity
13. Create first MicroSim from template
14. Embed in relevant chapter
15. Add learning graph visualization
16. Test all interactive elements

### Day 5: Deploy
17. Add custom styling (CSS)
18. Generate quality metrics
19. Review with assessment framework
20. Deploy to GitHub Pages with `mkdocs gh-deploy`

### Ongoing: Iterate
- Add chapters following learning graph order
- Create more MicroSims for key concepts
- Gather user feedback
- Plan Level 3+ features based on usage

---

## Using This Skill

When helping someone create an intelligent textbook:

1. **Assess**: Determine current state and experience level
2. **Guide**: Follow the 5-step workflow sequentially
3. **Generate**: Use AI prompts to assist content creation
4. **Build**: Create MicroSims for key concepts
5. **Deploy**: Get it live, then iterate

**Key Principle**: Start with Level 2 (interactive content). The learning graph is the foundation that enables all higher levels. Don't attempt Level 5 features before establishing Level 2.
