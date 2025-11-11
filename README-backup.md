# Claude Skills for Intelligent Textbooks

[![GitHub](https://img.shields.io/badge/GitHub-dmccreary%2Fclaude--skills-blue?logo=github)](https://github.com/dmccreary/claude-skills)
[![MkDocs](https://img.shields.io/badge/Made%20with-MkDocs-526CFE?logo=materialformkdocs)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Claude AI](https://img.shields.io/badge/Powered%20by-Claude%20AI-DA7857?logo=anthropic)](https://claude.ai)

A curated collection of Claude AI skills and workflows for creating intelligent, interactive educational textbooks with learning graphs, MicroSims, and AI-assisted content generation.

**Website**: [https://dmccreary.github.io/claude-skills/](https://dmccreary.github.io/claude-skills/)

---

## Overview

This repository contains a comprehensive set of skills for building Level 2 intelligent textbooks using Claude AI. Each skill is designed to work as an autonomous agent that helps automate specific aspects of educational content creation, from learning graph generation to interactive simulations.

## Features

- **Learning Graph Generation** - Create structured knowledge graphs with 200+ concepts, dependencies, and taxonomy categorization
- **Glossary Generation** - Generate ISO 11179-compliant glossaries with precise, standardized definitions
- **Quiz Generation** - Create Bloom's Taxonomy-aligned multiple-choice assessments
- **FAQ Generation** - Build comprehensive FAQ sections from course content
- **MicroSim Creation** - Develop interactive p5.js educational simulations
- **Intelligent Textbook Workflows** - Complete end-to-end textbook creation pipelines
- **MCP Servers** - Zero-token tools for efficient operations (NEW!)

## Available Skills

### Educational Content Creation
- **faq-generator** - Generates FAQs from course content, learning graphs, and glossary terms
- **glossary-generator** - Creates ISO 11179-compliant glossaries from learning graph concepts
- **quiz-generator** - Generates Bloom's Taxonomy-aligned multiple-choice quizzes

### Intelligent Textbook Development
- **intelligent-textbook** - Complete workflow for AI-generated intelligent textbooks
- **intelligent-textbook-creator** - Creates interactive MkDocs Material textbooks (Level 2-5)
- **learning-graph-generator** - Generates 200-concept learning graphs with dependencies

### Interactive Simulations
- **microsim-p5** - Creates educational MicroSims using p5.js with interactive controls

### Hardware Projects
- **moving-rainbow** - Generates MicroPython programs for Raspberry Pi Pico with NeoPixel LED strips

### MCP Servers (Zero-Token Tools)
- **skills-lister** - Lists all available Claude skills with zero token usage via MCP
  - See [mcp-servers/README.md](mcp-servers/README.md) for setup instructions

## Getting Started

### Installation

1. Clone this repository:
```bash
git clone https://github.com/dmccreary/claude-skills.git
cd claude-skills
```

2. Install skills to your Claude environment:
```bash
# Create symlinks to make skills available globally
./scripts/install-skills.sh
```

3. List available skills:
```bash
./scripts/list-skills.sh
```

### Using Skills with Claude Code

Skills can be invoked in Claude Code using the `/skill` command:

```bash
/skill intelligent-textbook
```

Or directly through the Skill tool when working with Claude.

## Documentation

Full documentation is available at [https://dmccreary.github.io/claude-skills/](https://dmccreary.github.io/claude-skills/)

## Project Structure

```
claude-skills/
├── skills/                  # Skill definitions
│   ├── faq-generator/
│   ├── glossary-generator/
│   ├── intelligent-textbook/
│   └── ...
├── mcp-servers/            # MCP servers for zero-token operations
│   └── skills-lister/     # Lists skills with 0 tokens
├── scripts/                 # Utility scripts
├── docs/                    # MkDocs documentation
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is built with and depends on several outstanding open source projects:

### Core Technologies
- **[Claude AI](https://www.anthropic.com/claude)** by Anthropic - Advanced AI assistant powering the skill workflows
- **[MkDocs](https://www.mkdocs.org/)** - Fast, simple static site generator for project documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** - Beautiful, feature-rich documentation theme

### JavaScript Libraries
- **[p5.js](https://p5js.org/)** - Creative coding library for interactive educational simulations (MicroSims)
- **[Vis.js Network](https://visjs.github.io/vis-network/docs/network/)** - Network visualization for learning graphs

### Python Libraries
- **[PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)** - Enhanced Markdown extensions for Python-Markdown
  - Superfences for code blocks
  - Highlight for syntax highlighting
  - Details for collapsible sections
  - Admonitions for callouts

### Educational Frameworks
- **[Bloom's Taxonomy](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy)** - Educational framework for cognitive skill development
- **[ISO 11179](https://www.iso.org/standard/50340.html)** - Metadata registry standards for glossary definitions
- **[Dublin Core](https://www.dublincore.org/)** - Metadata standards for educational resources

### Development Tools
- **[GitHub Pages](https://pages.github.com/)** - Hosting for documentation site
- **[Bash](https://www.gnu.org/software/bash/)** - Shell scripting for automation

### Hardware Platforms (for moving-rainbow skill)
- **[Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)** - Microcontroller platform
- **[MicroPython](https://micropython.org/)** - Python for microcontrollers
- **[NeoPixel](https://www.adafruit.com/category/168)** by Adafruit - Addressable RGB LEDs


Special thanks to the open source community for making projects like this possible!

## Contact

**Author**: [Dan McCreary](https://www.linkedin.com/in/danmccreary/)


For questions, suggestions, or feedback, please open an issue on GitHub.
