# Claude Skills for Intelligent Textbooks

[![MkDocs](https://img.shields.io/badge/Made%20with-MkDocs-526CFE?logo=materialformkdocs)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/View%20on-GitHub%20Pages-blue?logo=github)](https://dmccreary.github.io/ibook-skills/)
[![GitHub](https://img.shields.io/badge/GitHub-dmccreary%2Fclaude--skills-blue?logo=github)](https://github.com/dmccreary/ibook-skills)
[![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-DA7857?logo=anthropic)](https://claude.ai/code)
[![Claude Skills](https://img.shields.io/badge/Uses-Claude%20Skills-DA7857?logo=anthropic)](https://github.com/dmccreary/ibook-skills)
[![p5.js](https://img.shields.io/badge/p5.js-ED225D?logo=p5.js&logoColor=white)](https://p5js.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## View the Live Site

Visit the interactive documentation at: [https://dmccreary.github.io/ibook-skills/](https://dmccreary.github.io/ibook-skills/)

## Overview

**Claude Skills for Intelligent Textbooks** is a comprehensive collection of AI-powered skills and workflows designed to revolutionize educational content creation. Built with Claude AI and optimized for intelligent textbook development, this repository provides educators and content creators with powerful tools to generate interactive, standards-based educational materials at scale.

This project enables the creation of **Level 2+ intelligent textbooks** using MkDocs with the Material theme, incorporating learning graphs, concept dependencies, interactive p5.js simulations (MicroSims), and AI-assisted content generation. Every skill follows educational best practices including Bloom's Taxonomy (2001 revision) for learning outcomes, ISO 11179 standards for terminology definitions, and concept dependency graphs to ensure proper prerequisite sequencing.

Whether you're an educator building course materials, a technical writer creating documentation, or a developer interested in educational technology, these Claude skills provide a systematic, AI-powered approach to creating comprehensive, interactive educational content. The skills can generate everything from foundational learning graphs with 200+ concepts to interactive quizzes, glossaries, FAQs, and engaging simulations—all following rigorous quality standards.

## Site Status and Metrics

| Metric | Count |
|--------|-------|
| Concepts in Learning Graph | 200 |
| Chapters | 13 |
| Markdown Files | 103 |
| Total Words | 233,548 |
| MicroSims | 5 |
| Glossary Terms | 200 |
| FAQ Questions | 64 |
| Quiz Questions | 520 |
| Equations | 49 |
| Images | 11 |
| References | 30 |

**Completion Status:** Approximately 90% complete (content generation and skill development phase)

**Skills Available:** 19 specialized skills covering learning graphs, content generation, interactive visualizations, and educational assessments.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic familiarity with markdown and command line

### Clone the Repository

```bash
git clone https://github.com/dmccreary/ibook-skills.git
cd ibook-skills
```

### Install Dependencies

This project uses MkDocs with the Material theme:

```bash
pip install mkdocs
pip install mkdocs-material
pip install pymdown-extensions
```

### Build and Serve Locally

Build the documentation site:

```bash
mkdocs build
```

Serve locally for development (with live reload):

```bash
mkdocs serve
```

Open your browser to `http://localhost:8000`

### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

This will build the site and push it to the `gh-pages` branch.

### Using the Skills

**Option 1: Global Installation (All Projects)**

Create symlinks to make skills available globally:

```bash
cd scripts
./install-ibook-skills.sh
```

This installs skills to `~/.claude/skills/` for use across all Claude Code projects.

**Option 2: Project-Specific Installation**

Skills in this repository are automatically available when working within this project directory.

**Invoke a skill in Claude Code:**

```
Use the learning-graph-generator skill to create a concept graph for my course
```

Or use the slash command:

```
/skill learning-graph-generator
```

**List available skills:**

```bash
./scripts/list-skills.sh
```

### Using the Documentation Site

**Navigation:**

- Use the left sidebar to browse chapters and skill descriptions
- Click the search icon (🔍) to search all content
- Each chapter includes quizzes for self-assessment
- The Learning Graph section shows concept dependencies and quality metrics

**Interactive MicroSims:**

- Found in the "MicroSims" section of the documentation
- Each simulation runs standalone in your browser
- Adjust parameters with sliders and interactive controls
- View source code and customize for your own use

**Customization:**

- Edit markdown files in `docs/` to modify content
- Modify `mkdocs.yml` to change site structure and navigation
- Add your own MicroSims in `docs/sims/[microsim-name]/`
- Customize theme colors and styles in `docs/css/extra.css`
- Create custom skills in `skills/[skill-name]/SKILL.md`

## Repository Structure

```
ibook-skills/
├── docs/                          # MkDocs documentation source
│   ├── chapters/                  # 13 chapters on intelligent textbook creation
│   │   ├── 01-intro-ai-intelligent-textbooks/
│   │   │   ├── index.md          # Chapter content
│   │   │   └── quiz.md           # Chapter quiz (40 questions)
│   │   └── ...
│   ├── sims/                      # Interactive p5.js MicroSims
│   │   ├── graph-viewer/         # Learning graph visualization
│   │   │   ├── main.html         # Standalone simulation
│   │   │   └── index.md          # Documentation
│   │   └── ...
│   ├── learning-graph/            # Learning graph data and analysis
│   │   ├── concept-list.md       # 200 concepts enumerated
│   │   ├── learning-graph.csv    # Concept dependencies (DAG)
│   │   ├── learning-graph.json   # vis-network JSON format
│   │   ├── quality-metrics.md    # Graph quality analysis
│   │   └── taxonomy-distribution.md
│   ├── skill-descriptions/        # Documentation for each skill
│   ├── prompts/                   # Example prompts for skill usage
│   ├── glossary.md                # ISO 11179-compliant definitions (200 terms)
│   ├── faq.md                     # Frequently asked questions (64 Q&A)
│   └── references.md              # Curated references (30 sources)
├── skills/                        # Claude AI skill definitions
│   ├── learning-graph-generator/
│   │   ├── SKILL.md               # Skill definition and workflow
│   │   ├── analyze-graph.py       # DAG validation script
│   │   ├── csv-to-json.py         # Convert to vis-network format
│   │   └── taxonomy-distribution.py
│   ├── glossary-generator/        # Generates ISO 11179 glossaries
│   ├── quiz-generator/            # Creates Bloom's Taxonomy quizzes
│   ├── faq-generator/             # Builds comprehensive FAQs
│   ├── microsim-p5/               # Creates p5.js simulations
│   ├── readme-generator/          # Generates README files
│   └── ...                        # 19 total skills
├── scripts/                       # Utility scripts
│   ├── install-ibook-skills.sh   # Install skills globally
│   ├── list-skills.sh             # List available skills
│   └── list-skills-format.sh      # Format skill list (JSON, CSV)
├── commands/                      # Slash commands
│   └── skills.md                  # /skills command
├── mkdocs.yml                     # MkDocs configuration
├── CLAUDE.md                      # Instructions for Claude Code
└── README.md                      # This file
```

## Reporting Issues

Found a bug, typo, or have a suggestion for improvement? Please report it:

[GitHub Issues](https://github.com/dmccreary/ibook-skills/issues)

When reporting issues, please include:

- Clear description of the problem or suggestion
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Screenshots or error messages (if applicable)
- Skill name and version (if skill-specific)
- Browser/environment details (for MicroSim issues)

## License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**You are free to:**

- **Share** — Copy and redistribute the material in any medium or format
- **Adapt** — Remix, transform, and build upon the material

**Under the following terms:**

- **Attribution** — Give appropriate credit with a link to the original repository
- **NonCommercial** — No commercial use without explicit permission
- **ShareAlike** — Distribute your contributions under the same license

**Attribution Example:**

```
This work is based on "Claude Skills for Intelligent Textbooks" by Dan McCreary,
available at https://github.com/dmccreary/ibook-skills, licensed under CC BY-NC-SA 4.0.
```

See [license details](https://creativecommons.org/licenses/by-nc-sa/4.0/) for the full legal text.

## Acknowledgements

This project is built on the shoulders of giants in the open source community. We are deeply grateful to:

### Documentation and Build Tools

- **[MkDocs](https://www.mkdocs.org/)** - Fast, simple static site generator optimized for project documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - Beautiful, responsive Material Design theme with advanced features

### Interactive Visualizations and Creative Coding

- **[p5.js](https://p5js.org/)** - Creative coding library from NYU ITP for interactive educational simulations
- **[vis-network](https://visjs.org/)** - Network visualization library for learning graph exploration
- **[Chart.js](https://www.chartjs.org/)** - Interactive charts for data visualization
- **[Mermaid](https://mermaid.js.org/)** - Diagram and flowchart generation from text

### Python Ecosystem

- **[Python](https://www.python.org/)** community - Data processing, analysis, and automation tools
- **[PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)** - Enhanced Markdown extensions

### AI and Machine Learning

- **[Claude AI](https://claude.ai)** by Anthropic - Advanced AI assistant powering content generation and skill workflows
- **[Claude Code](https://claude.ai/code)** - AI-powered coding assistant enabling autonomous skill execution

### Hosting and Deployment

- **[GitHub Pages](https://pages.github.com/)** - Free hosting for open source documentation projects
- **[GitHub](https://github.com/)** - Version control and collaboration platform

### Hardware and MicroPython (for moving-rainbow skill)

- **[Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)** - Affordable microcontroller platform
- **[MicroPython](https://micropython.org/)** - Python 3 for microcontrollers
- **[NeoPixel](https://www.adafruit.com/category/168)** by Adafruit - Addressable RGB LED technology

### Educational Standards and Frameworks

- **[Bloom's Taxonomy](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy)** - Framework for categorizing cognitive learning objectives
- **[ISO 11179](https://www.iso.org/standard/50340.html)** - International standard for metadata registries (glossary definitions)
- **[Dublin Core](https://www.dublincore.org/)** - Metadata standards for educational resources

Special thanks to the educators, developers, and maintainers who contribute to making educational resources accessible, interactive, and open to all. Your work enables projects like this to exist and thrive.

## Contact

**Dan McCreary**

- LinkedIn: [linkedin.com/in/danmccreary](https://www.linkedin.com/in/danmccreary/)
- GitHub: [@dmccreary](https://github.com/dmccreary)

Questions, suggestions, or collaboration opportunities? Feel free to connect on LinkedIn or open an issue on GitHub. I'm particularly interested in:

- Feedback on skill effectiveness and quality
- Suggestions for new skills or features
- Collaboration on educational technology projects
- Use cases and success stories from educators

## How to Cite

If you use these Claude skills in your research, teaching, or projects, please cite:

```
McCreary, D. (2024). Claude Skills for Intelligent Textbooks. GitHub.
https://github.com/dmccreary/ibook-skills
```

**BibTeX:**

```bibtex
@misc{mccreary2024claudeskills,
  author = {McCreary, Dan},
  title = {Claude Skills for Intelligent Textbooks},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/dmccreary/ibook-skills},
  note = {A collection of AI-powered skills for creating intelligent educational content}
}
```

## Available Skills

This repository includes 19 specialized skills for intelligent textbook creation:

### Core Educational Skills

1. **course-description-analyzer** - Validates and enhances course descriptions
2. **learning-graph-generator** - Creates 200-concept dependency graphs (DAG structure)
3. **book-chapter-generator** - Designs optimal chapter structure from learning graphs
4. **chapter-content-generator** - Generates comprehensive chapter content with examples
5. **glossary-generator** - Creates ISO 11179-compliant glossaries
6. **faq-generator** - Generates FAQs from course content and learning graphs
7. **quiz-generator** - Creates Bloom's Taxonomy-aligned assessments
8. **reference-generator** - Curates academic references by education level

### Interactive Content Skills

9. **microsim-p5** - Creates educational p5.js simulations with interactive controls
10. **microsim-standardization** - Validates and upgrades MicroSim quality
11. **bubble-chart-generator** - Creates Chart.js bubble visualizations for priority matrices
12. **timeline-generator** - Generates interactive timeline visualizations
13. **mermaid-generator** - Creates workflow diagrams and flowcharts
14. **venn-diagram-generator** - Generates interactive Venn diagrams
15. **vis-network** - Creates network visualizations and graph explorers

### Workflow and Orchestration Skills

16. **intelligent-textbook** - Complete 12-step textbook generation workflow
17. **intelligent-textbook-creator** - Creates MkDocs Material textbook projects
18. **install-learning-graph-viewer** - Installs interactive graph exploration tools
19. **readme-generator** - Generates comprehensive README files (this skill!)


For detailed documentation on each skill, see the [skill descriptions](https://dmccreary.github.io/ibook-skills/skill-descriptions/) in the documentation site.

---

**Built with Claude Code** | **Powered by Claude AI** | **Open Educational Resources**
