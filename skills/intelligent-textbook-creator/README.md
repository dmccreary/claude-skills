# Intelligent Textbook Creator Skill

A comprehensive Claude skill for creating intelligent, interactive textbooks using MkDocs with Material theme, learning graphs, MicroSims, and AI-assisted content generation.

## What This Skill Does

This skill guides users through creating Level 2-5 intelligent textbooks following a structured workflow:

1. **Course Description**: Define scope, audience, and learning objectives
2. **Concept Enumeration**: Generate 150-250 key concepts
3. **Dependency Mapping**: Create learning graph (DAG) showing prerequisites
4. **Taxonomy Creation**: Organize concepts into categories
5. **Content Generation**: Build chapters, glossary, and interactive elements
6. **Deployment**: Publish to GitHub Pages

## When to Use

Use this skill when someone wants to:
- Create an interactive educational textbook or course material
- Transform static content into intelligent learning experiences
- Build learning dependency graphs (concept maps)
- Add interactive p5.js simulations (MicroSims) to educational content
- Generate structured educational content using AI prompts
- Implement progressive levels of textbook intelligence

## Features

### Five Levels of Intelligence

- **Level 1**: Static textbooks (skip this)
- **Level 2**: Interactive content with MicroSims, search, glossary ⭐ **Primary Focus**
- **Level 3**: Adaptive learning paths based on user performance
- **Level 4**: AI chatbot integration for tutoring
- **Level 5**: Autonomous AI-generated personalized lessons

### Key Components

- **Learning Graphs**: DAG-based concept dependency maps
- **MicroSims**: Interactive p5.js simulations (~670px wide)
- **AI Prompts**: Structured prompts for content generation
- **Quality Framework**: 20-question assessment across 5 dimensions
- **MkDocs Integration**: Material theme with full customization

## Files Structure

```
intelligent-textbook-creator/
├── SKILL.md                          # Main skill instructions
├── README.md                         # This file
└── references/                       # Detailed reference materials
    ├── prompts-guide.md             # Complete AI prompt collection
    ├── microsim-templates.md        # p5.js templates and patterns
    ├── mkdocs-config.md             # Complete mkdocs.yml examples
    ├── quality-framework.md         # 20-question assessment
    └── advanced-features.md         # Level 3-5 implementation
```

## Quick Start

When using this skill with Claude, Claude will:

1. **Assess** your current state and experience level
2. **Guide** you through the 5-step workflow sequentially
3. **Generate** content using AI prompts as needed
4. **Build** MicroSims for key concepts
5. **Deploy** your textbook to GitHub Pages

## Prerequisites

Users should have:
- Basic understanding of markdown
- GitHub account (for deployment)
- Willingness to learn mkdocs basics
- A topic/subject to teach

No programming experience required for Level 2!

## Example Use Cases

### Computer Science
- Interactive programming tutorials
- Algorithm visualizations
- Data structure explorations

### Mathematics
- Calculus with interactive graphs
- Linear algebra visualizations
- Statistics simulations

### Science
- Physics simulations
- Chemistry molecular models
- Biology process animations

### Business
- Marketing analytics dashboards
- Financial modeling tools
- Project management simulations

## Technical Stack

- **MkDocs**: Static site generator
- **Material Theme**: Modern, responsive design
- **p5.js**: Interactive simulations library
- **Python**: Build tooling and analytics
- **GitHub Pages**: Free hosting
- **Optional**: Firebase (Level 3+), Claude API (Level 4+)

## Progressive Disclosure

The skill uses progressive disclosure:
- **SKILL.md**: Core workflow and procedures (~3k words)
- **References**: Detailed templates and examples (~20k words total)

Claude loads references only when needed, keeping context efficient.

## Learning Graph Foundation

The learning graph is the foundation that enables all intelligence levels:
- **Level 2**: Provides structure for navigation
- **Level 3**: Enables adaptive pathways
- **Level 4**: Gives context to AI chatbot
- **Level 5**: Powers autonomous content generation

## Success Criteria

A successful intelligent textbook should:
- Implement Level 2 features at minimum
- Include 150+ concepts with dependency graph
- Have 5+ interactive MicroSims
- Provide comprehensive glossary
- Be mobile-responsive and accessible
- Be publicly deployed

## Support

For questions about:
- **MkDocs**: https://www.mkdocs.org/
- **Material Theme**: https://squidfunk.github.io/mkdocs-material/
- **p5.js**: https://p5js.org/
- **This Repository**: https://github.com/dmccreary/intelligent-textbooks/

## License

This skill inherits the license from the parent intelligent-textbooks repository (CC BY-NC-SA 4.0).

## Credits

Based on the intelligent-textbooks framework by Dan McCreary and contributors.

Inspired by Neal Stephenson's "The Diamond Age" concept of the Young Lady's Illustrated Primer.

---

**Remember**: Start with Level 2. The learning graph is the foundation. Don't attempt Level 5 before establishing Level 2.
