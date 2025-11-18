# MicroSim File Relationship Diagram

A block diagram showing how the three core MicroSim files (index.md, main.html, metadata.json) relate to each other and integrate into the MkDocs intelligent textbook architecture.

[Run the MicroSim File Relationship Diagram](./main.html){: .md-button .md-button--primary }

[View Diagram Metadata](metadata.json){: .md-button }

## Overview

This diagram illustrates the complete architecture of a MicroSim package within an intelligent textbook built on MkDocs. It shows how students navigate from the textbook to interactive simulations, the role of security boundaries (iframes), and how metadata enables discovery and LMS integration.

Understanding this architecture is essential for:

- **Textbook Authors**: Creating and organizing MicroSim content
- **Developers**: Implementing new MicroSims or debugging integration issues
- **Instructors**: Understanding how simulations are isolated and secured
- **Students**: Appreciating the technical infrastructure supporting their learning

## Diagram Components

### Documentation Layer

#### MkDocs Navigation

The top-level site navigation structure that organizes the intelligent textbook. MkDocs generates this navigation from the `mkdocs.yml` configuration file, creating a hierarchical menu that students use to browse chapters, concepts, and visualizations.

**Purpose**: Provides the entry point for student exploration

**Location**: Configured in `mkdocs.yml` at repository root

#### index.md (Documentation Page)

The student-facing documentation page that provides context, instructions, and learning objectives for each MicroSim. This markdown file is where students first land when navigating to a visualization.

**Purpose**: Educational context and simulation embedding

**Location**: `docs/sims/{name}/index.md`

**Contents**:

- MicroSim title and overview
- Learning objectives aligned to Bloom's Taxonomy
- Iframe embed displaying the simulation
- Usage instructions and controls explanation
- Related concepts and cross-references
- Educational context and applications

### Integration Layer

#### iframe Element

An HTML iframe embedded within `index.md` that loads `main.html`. The iframe creates a **security boundary** that isolates the simulation from the parent MkDocs page.

**Purpose**: Sandbox isolation and security

**Security Benefits**:

- Prevents simulation from accessing parent page DOM
- Protects user data and site navigation from simulation code
- Ensures simulation errors don't crash the entire page
- Enables safe execution of experimental or untrusted code

**Implementation**: Standard HTML iframe with sandbox attributes

### Simulation Layer

#### main.html (Interactive HTML)

A self-contained HTML page that implements the interactive visualization using p5.js or other JavaScript libraries. This file includes all necessary HTML, CSS, and JavaScript to render and control the simulation.

**Purpose**: Interactive educational visualization

**Location**: `docs/sims/{name}/main.html`

**Features**:

- Loads p5.js library from CDN (no local dependencies)
- Implements setup() and draw() functions for p5.js
- Provides interactive controls (sliders, buttons, inputs)
- Responds to user input with real-time visual feedback
- Can run standalone (outside of MkDocs)

**Self-Contained Design**: main.html includes all assets inline or loads from CDNs, making it portable and easy to share independently of the textbook.

#### p5.js Simulation

The canvas-based rendering powered by the p5.js library. This is what students see and interact with—the visual representation of concepts through animation, interactivity, and dynamic feedback.

**Purpose**: Visual concept demonstration

**Library**: p5.js loaded from CDN (https://cdn.jsdelivr.net/npm/p5)

**Rendering**: HTML5 Canvas element

**Capabilities**:

- Real-time graphics rendering
- Mouse and keyboard interaction
- Animation and motion
- Mathematical visualizations
- Data-driven graphics

### Metadata Layer

#### metadata.json (Dublin Core Metadata)

Structured metadata following Dublin Core standards that describes the MicroSim for discovery, cataloging, and external integration. This JSON file enables machine-readable description of educational content.

**Purpose**: Discovery, cataloging, and LMS integration

**Location**: `docs/sims/{name}/metadata.json`

**Standards**:

- **Dublin Core**: International metadata standard
- **Bloom's Taxonomy**: Cognitive level classification
- **Educational Metadata**: Learning objectives, prerequisites, concepts

**Fields Include**:

- Title, description, subject area
- Creator, date created, version
- Educational level, audience, coverage
- Bloom's Taxonomy classification
- Concept tags and keywords
- Technical specifications

#### Learning Management System (Optional)

External educational platforms like Canvas, Moodle, or Blackboard can import MicroSim metadata to integrate simulations into course catalogs, assignments, and learning paths.

**Purpose**: External course integration

**Connection**: Reads `metadata.json` for import

**Use Cases**:

- Course catalog listings
- Assignment creation
- Learning objective mapping
- Student progress tracking
- Content discovery and search

## Information Flows

### Primary Navigation Flow (Student Experience)

This is the path a student follows from textbook navigation to interactive simulation:

1. **Browse Navigation** → Student explores the MkDocs site navigation menu
2. **Click MicroSim Link** → Selects a visualization from navigation or chapter content
3. **Load Documentation Page** → `index.md` loads with context and instructions
4. **View Embedded Simulation** → iframe displays `main.html` in isolated sandbox
5. **Interact with Canvas** → Student manipulates controls and observes p5.js rendering

**Total Time**: < 2 seconds from click to interactive simulation

**Student Perspective**: Seamless transition from reading to interaction

### Metadata Flow (Discovery & Cataloging)

How metadata enables discovery and external integration:

1. **MicroSim Created** → `metadata.json` generated with Dublin Core fields
2. **Describes Documentation** → Metadata references `index.md` as the primary resource
3. **Catalog Indexing** → Search tools and catalogs read metadata for discovery
4. **LMS Import** → External systems consume metadata for course integration
5. **Student Discovery** → Students find MicroSims through search and recommendations

**Benefits**:

- Consistent metadata across all MicroSims
- Machine-readable educational content
- Interoperability with external systems
- Enhanced discoverability

### Security Boundary Flow

How the iframe provides isolation:

1. **iframe Loads** → Parent page (`index.md`) creates iframe element
2. **Sandbox Applied** → Browser enforces security restrictions on iframe content
3. **main.html Loads** → Simulation HTML loads in isolated context
4. **Same-Origin Policy** → Simulation cannot access parent page JavaScript/DOM
5. **Safe Execution** → Simulation runs with limited permissions

**Security Guarantees**:

- Simulation cannot modify textbook navigation
- Simulation cannot read user session data
- Simulation errors remain contained
- Untrusted code can be safely demonstrated

## File Structure Example

```
docs/sims/pendulum-motion/
├── index.md           # Documentation page with iframe embed
├── main.html          # Interactive p5.js simulation
├── metadata.json      # Dublin Core metadata
└── README.md          # Developer notes (optional)
```

Each MicroSim follows this standard structure, making them:

- **Predictable**: Developers know where to find components
- **Portable**: Entire directory can be copied/shared
- **Self-Contained**: All assets in one location
- **Discoverable**: Consistent metadata format

## Integration with MkDocs

### Navigation Configuration

MicroSims are added to the textbook navigation in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Chapters:
      - Chapter 1: chapters/01/index.md
      - Chapter 2: chapters/02/index.md
  - MicroSims:
      - Pendulum Motion: sims/pendulum-motion/index.md
      - Wave Interference: sims/wave-interference/index.md
```

### Embedding in Chapters

MicroSims can also be embedded directly in chapter content:

```markdown
## Interactive Demonstration

See how pendulum period depends on length:

<iframe src="../../sims/pendulum-motion/main.html"
        width="100%" height="600"
        frameborder="0"></iframe>

[View full documentation](../../sims/pendulum-motion/index.md)
```

### Cross-References

Chapters reference MicroSims to reinforce concepts:

```markdown
The concept of harmonic motion is demonstrated in the
[Pendulum Motion MicroSim](../sims/pendulum-motion/index.md).
```

## Technical Details

### Technologies Used

- **MkDocs**: Static site generator
- **Material for MkDocs**: Theme with enhanced features
- **p5.js**: Creative coding library for canvas rendering
- **HTML5 iframe**: Sandboxing and isolation
- **Dublin Core**: Metadata standard
- **JSON**: Structured data format

### Browser Compatibility

- **Modern Browsers**: Chrome, Firefox, Safari, Edge (latest versions)
- **Mobile Support**: Responsive design works on tablets and phones
- **Canvas Support**: Requires HTML5 canvas (all modern browsers)

### Performance Considerations

- **CDN Loading**: p5.js loaded from fast CDN
- **Lazy Loading**: iframes load only when scrolled into view
- **Caching**: Browser caches static resources
- **Optimization**: MicroSims designed to run at 60fps

## Use Cases

This architectural pattern enables:

### Educational Content

- Interactive concept demonstrations
- Algorithm visualizations
- Mathematical function plotters
- Scientific simulations
- Data structure animations

### Content Portability

- Share individual MicroSims independently
- Embed in other websites via iframe
- Export to SCORM packages for LMS
- Archive for long-term preservation

### Development Workflows

- Develop simulations separately from textbook
- Test in standalone mode (main.html)
- Integrate into documentation when complete
- Update simulations without regenerating entire textbook

## Best Practices

### For Authors

1. **Document First**: Write clear `index.md` with learning objectives before creating simulation
2. **Test Standalone**: Verify `main.html` works independently before embedding
3. **Complete Metadata**: Fill all Dublin Core fields in `metadata.json`
4. **Consistent Naming**: Use kebab-case for directory names

### For Developers

1. **Self-Contained HTML**: Keep all CSS/JS inline or load from CDN (no local dependencies)
2. **Responsive Design**: Ensure simulation works on various screen sizes
3. **Error Handling**: Gracefully handle edge cases and invalid inputs
4. **Performance**: Target 60fps for smooth animations

### For Instructors

1. **Explain Isolation**: Help students understand why iframes provide security
2. **Link to Documentation**: Always reference `index.md` rather than embedding raw `main.html`
3. **Leverage Metadata**: Use `metadata.json` for course catalog integration
4. **Assign Exploration**: Encourage students to explore MicroSim source code

## Related Documentation

- [MicroSim Creation Guide](../../chapters/12-interactive-elements-microsims/index.md)
- [p5.js Documentation](https://p5js.org/)
- [MkDocs Material Documentation](https://squidfunk.github.io/mkdocs-material/)
- [Dublin Core Metadata Initiative](https://www.dublincore.org/)

## References

- **MkDocs**: Static site generator for documentation - https://www.mkdocs.org/
- **Material for MkDocs**: Feature-rich theme - https://squidfunk.github.io/mkdocs-material/
- **p5.js**: Creative coding for the web - https://p5js.org/
- **Dublin Core**: Metadata standards - https://www.dublincore.org/
- **iframe Security**: HTML5 sandbox attributes - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe
