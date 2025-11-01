---
name: intelligent-textbook
description: Comprehensive workflow for generating intelligent textbooks using AI, from course description through concept mapping, dependency graphs, taxonomies, and interactive content creation with MicroSims. Use this when users request creating educational content, textbooks, course materials, learning graphs, or interactive educational simulations.
license: MIT
allowed-tools: ["Read", "Write", "Edit", "Bash", "Grep", "Glob", "WebFetch", "WebSearch"]
---

# Intelligent Textbook Generation

This skill guides you through the complete workflow for generating intelligent, interactive textbooks using AI assistance, MkDocs with Material theme, and p5.js-based MicroSimulations.

## Overview

Intelligent textbooks are educational resources that go beyond static content by incorporating:

- **Structured concept mapping** using learning graphs and dependency analysis
- **Interactive visualizations** (MicroSims) built with p5.js
- **AI-assisted content generation** following educational best practices
- **Bloom's Taxonomy alignment** for progressive skill development
- **Scaffolded learning paths** based on concept dependencies

This workflow transforms a course description into a complete, interactive educational resource.

---

## Core Principles

### Educational Foundations

1. **Bloom's Taxonomy (2001)**: Structure content across six cognitive levels
   - Remember ’ Understand ’ Apply ’ Analyze ’ Evaluate ’ Create
   - Use appropriate action verbs for each level
   - Scaffold learning from foundational to advanced concepts

2. **Scaffolding**: Build knowledge incrementally
   - Start with prerequisites and foundational concepts
   - Layer new concepts on mastered fundamentals
   - Provide support structures that can be gradually removed

3. **Concept Dependencies**: Establish clear learning prerequisites
   - Create directed acyclic graphs (DAGs) showing concept relationships
   - Ensure foundational concepts are taught before dependent ones
   - Support multiple learning paths based on student backgrounds

4. **Five Levels of Textbook Intelligence**:
   - Level 1: Static text and images
   - Level 2: Hyperlinked content with navigation
   - Level 3: Interactive elements and quizzes
   - Level 4: Adaptive content based on learner progress
   - Level 5: AI-powered personalization and generation

---

## Workflow Steps

### Step 1: Course Description Development

**Purpose**: Create a comprehensive foundation document that guides all subsequent development.

**Required Components**:

1. **Course Title**: Clear, descriptive name (e.g., "Introduction to Deep Learning with Python")
2. **Target Audience**: Specific learner demographics and background
3. **Prerequisites**: Prior knowledge concepts students should have mastered
4. **Course Description**: Narrative summary of coverage, methodology, and outcomes
5. **Learning Objectives**: Specific, measurable skills or knowledge students will gain
6. **Topics Covered**: Main subject areas or modules
7. **Course Duration**: Length and format (e.g., 8 weeks, 40 hours, online/in-person)
8. **Assessment Methods**: How progress is evaluated (projects, assignments, exams)
9. **Tools/Software Required**: Technical requirements and platforms
10. **Credits**: Academic credit value if applicable
11. **Instructor Information**: Relevant qualifications and experience

**Sample Prompt**:

```
Please help me create a detailed course description for a course on "[TOPIC]".
Include:

1. Course title
2. Target audience
3. Prerequisites
4. Detailed course description (narrative)
5. Numbered list of learning objectives
6. Topics covered
7. Course duration
8. Assessment methods
9. Tools/software required

Make the description comprehensive enough to guide the development of a complete textbook.
```

**Deliverable**: `course-description.md` file with all components

---

### Step 2: Bloom's Taxonomy Integration

**Purpose**: Categorize learning objectives across cognitive levels to ensure comprehensive coverage and progressive development.

**The Six Levels**:

1. **Remember** (Red/Foundation): Define, list, recall, identify
2. **Understand** (Orange/Roots): Summarize, paraphrase, classify, explain
3. **Apply** (Yellow/Trunk): Implement, execute, solve, use
4. **Analyze** (Green/Branches): Differentiate, organize, compare, attribute
5. **Evaluate** (Blue/Mid-branches): Judge, critique, check, assess
6. **Create** (Purple/Crown): Design, construct, plan, develop

**Process**:

1. Review each learning objective from the course description
2. Categorize objectives by Bloom's level
3. Identify gaps in cognitive level coverage
4. Rewrite or add objectives to ensure all levels are represented
5. Use appropriate action verbs for each level

**Sample Prompt**:

```
Using the 2001 Bloom's Taxonomy revision, please analyze the learning objectives
in the attached course description.

For each objective:
1. Identify its current Bloom's level
2. Rewrite it using appropriate action verbs if needed
3. Categorize it clearly

Then suggest additional objectives to ensure all six cognitive levels are
adequately represented in the course. Provide a distribution summary showing
how many objectives fall into each Bloom's level.
```

**Deliverable**: Enhanced course description with Bloom's-aligned learning objectives

---

### Step 3: Concept Enumeration

**Purpose**: Create a comprehensive inventory of all key concepts students must master.

**Guidelines**:

- Target: ~250 concepts per standard course (adjust based on scope and existing knowledge)
- Use concise concept labels in Title Case format
- Avoid unnecessary acronyms unless labels become too long
- Order concepts roughly in teaching sequence
- Each concept should be atomic (single, clear idea)

**Sample Prompt**:

```
You are an expert at generating high-quality concept labels for knowledge graphs
in online training courses.

Using the attached course description enhanced with Bloom's Taxonomy, please
generate a numbered list of 250 key concepts for this course. Use one line per
concept.

Format each concept as a short label in Title Case. Use acronyms only when
necessary for brevity.

Return the concepts in approximate teaching order, starting with foundational
prerequisites and progressing to advanced topics.
```

**Quality Checks**:

- Are concepts atomic (single ideas)?
- Is the scope appropriate (not too broad or narrow)?
- Do concepts progress logically?
- Are foundational concepts identified?
- Are there clear beginning and ending concepts?

**Deliverable**: `enumerated-concepts.md` - numbered list of concept labels

---

### Step 4: Concept Dependencies

**Purpose**: Create a directed acyclic graph (DAG) showing learning prerequisites and relationships.

**Key Concepts**:

- **Dependencies**: Concepts that must be mastered BEFORE learning a new concept
- **Directed Acyclic Graph (DAG)**: No circular dependencies (A depends on B, B depends on A)
- **Foundational Concepts**: Concepts with no dependencies (prerequisites)
- **Connected Graph**: All concepts should connect to at least one other concept
- **Multiple Paths**: Different learning sequences may exist based on student background

**CSV Format**:

```
ConceptID,ConceptLabel,Dependencies
1,Introduction to Programming,
2,Variables and Data Types,1
3,Control Flow,1|2
4,Functions,1|2|3
...
```

- **Column 1**: ConceptID (numeric identifier from enumeration)
- **Column 2**: ConceptLabel (exact label from enumeration)
- **Column 3**: Dependencies (pipe-delimited list of ConceptIDs that must be learned first)

**Sample Prompt**:

```
You are an expert at understanding learning dependencies and building learning
graphs using directed acyclic graphs (DAGs).

Using the attached enumerated-concepts.md file, create a fully connected concept
dependency graph.

Generate a CSV file with this format:
- Header row: ConceptID,ConceptLabel,Dependencies
- ConceptID: The number from the enumerated list
- ConceptLabel: The exact label from the enumerated list
- Dependencies: Pipe-delimited list of ConceptIDs that must be learned first
  (empty for foundational concepts)

Requirements:
1. All concepts must connect to at least one other concept
2. No circular dependencies (this must be a DAG)
3. Foundational concepts have empty Dependencies column
4. Dependencies should reflect true prerequisites (not just related topics)
5. Consider multiple valid learning paths where appropriate

Verify your results to ensure the graph is fully connected and acyclic.
```

**Quality Checks**:

- Are all concepts connected?
- Are there any circular dependencies?
- Do foundational concepts have empty dependencies?
- Are dependencies logical and necessary?
- Can you trace multiple valid learning paths?

**Deliverable**: `dependencies.csv` - complete dependency graph

---

### Step 5: Concept Taxonomy

**Purpose**: Organize concepts into a manageable classification system for visualization and navigation.

**Taxonomy Guidelines**:

- Target: 10-12 category labels
- Categories should be balanced (similar number of concepts each)
- Each concept assigned to exactly ONE primary category
- Common categories:
  - "Foundational Concepts" - prerequisites and basics
  - "Concept Definitions" - key terms and vocabulary
  - Domain-specific categories based on the course
  - "Miscellaneous" - concepts that don't fit elsewhere

**Process Overview**:

1. Generate taxonomy labels (10-12 categories)
2. Update dependencies CSV with TaxonomyID column
3. Create HTML legend for learning graph visualization

**Sample Prompts**:

**Part A - Generate Taxonomy**:
```
Using the enumerated-concepts.md file, organize these concepts into a taxonomy
of approximately 12 classifiers.

Guidelines:
1. First category: "Foundational Concepts" (prerequisites)
2. Second category: "Concept Definitions" (key terms)
3. Last category: "Miscellaneous"
4. Create 9 additional categories that evenly divide the remaining concepts

For each category, provide:
- Category label (Title Case)
- Brief definition
- Approximate concept count

Ensure categories are distinct, cover different aspects of the course, and
include abstract ideas, practical applications, and real-world examples.
```

**Part B - Update Dependencies CSV**:
```
Update the dependencies.csv file to add a new column called TaxonomyID.

For each concept, assign it to its PRIMARY taxonomy category (only one per concept).

New CSV format:
1. ConceptID (unchanged)
2. ConceptLabel (unchanged)
3. Dependencies (unchanged)
4. TaxonomyID (new - number 1-12 for the primary category)

Generate the complete updated CSV file.
```

**Part C - Generate HTML Legend**:
```
Create an HTML table legend for the learning graph viewer.

Format:
<table>
  <tr>
    <td>Foundational Concepts</td>
    <td style="background-color: red; color: white;">Red</td>
  </tr>
  <tr>
    <td>Category Name</td>
    <td style="background-color: orange; color: black;">Orange</td>
  </tr>
  ...
</table>

Use distinct colors for each category (red, orange, yellow, green, blue,
purple, pink, brown, gray, etc.). Ensure text is readable on each background.
```

**Deliverable**:
- Updated `dependencies.csv` with TaxonomyID column
- HTML legend code for learning graph visualization
- Taxonomy documentation

---

### Step 6: Learning Graph Visualization

**Purpose**: Create an interactive visualization of the concept dependency graph.

**Implementation**:

The learning graph is typically implemented as a p5.js-based MicroSim that:

1. Loads the dependencies CSV file
2. Visualizes concepts as nodes
3. Shows dependencies as directed edges
4. Colors nodes by taxonomy category
5. Provides interactivity (zoom, pan, click for details)
6. Displays the taxonomy legend

**Technical Components**:

- **Data Loading**: Parse CSV using PapaParse or similar
- **Graph Layout**: Use force-directed layout or hierarchical layout
- **Visualization**: p5.js for rendering
- **Interactivity**: Mouse events for node selection, tooltips, navigation
- **Responsive Design**: Adapt to different screen sizes

**Directory Structure**:
```
docs/sims/learning-graph/
   index.md              # Documentation page
   main.html             # Standalone visualization
   learning-graph.js     # p5.js implementation
   dependencies.csv      # Data file
   legend.html          # Taxonomy legend
```

**Sample index.md Structure**:
```markdown
# Learning Graph

This interactive visualization shows the dependencies between all concepts
in the course.

<iframe src="main.html" height="800px" width="100%" scrolling="no"
  style="overflow: hidden;"></iframe>

## How to Use

- **Zoom**: Mouse wheel or pinch gesture
- **Pan**: Click and drag
- **Select**: Click on a node to see details
- **Colors**: Each color represents a taxonomy category (see legend below)

## Taxonomy Legend

[Insert HTML legend here]

## About Dependencies

The arrows show which concepts must be learned before others...
```

**Deliverable**: Complete learning-graph MicroSim with visualization, data, and documentation

---

### Step 7: Chapters and Sections Structure

**Purpose**: Organize the learning graph into a sequential textbook structure.

**Approach**:

1. **Identify Major Topics**: Group related concepts from the learning graph
2. **Create Chapter Outline**: 8-12 chapters covering major topics
3. **Define Sections**: Break each chapter into 3-8 sections
4. **Map Concepts to Sections**: Assign enumerated concepts to specific sections
5. **Verify Dependency Order**: Ensure chapters/sections follow dependency graph

**Sample Prompt**:

```
Using the learning graph with all concepts and dependencies, create a textbook
chapter structure.

Requirements:
1. Generate 8-12 chapter titles that cover all major topics
2. For each chapter, create 3-8 section titles
3. Map each enumerated concept to a specific chapter and section
4. Ensure the sequence respects the dependency graph (prerequisites come first)
5. Balance chapter lengths (similar concept counts)

Output format:
# Chapter 1: [Title]
## Section 1.1: [Title]
- Concept 1, Concept 5, Concept 12
## Section 1.2: [Title]
- Concept 3, Concept 7
...
```

**Deliverable**: `chapters-outline.md` with complete structure and concept mapping

---

### Step 8: Content Generation for Sections

**Purpose**: Generate detailed educational content for each section following best practices.

**Content Components**:

1. **Introduction**: Overview and learning objectives for the section
2. **Core Content**: Detailed explanations with examples
3. **Visual Elements**: Diagrams, charts, or MicroSim embeds
4. **Worked Examples**: Step-by-step demonstrations
5. **Practice Problems**: Exercises for students (with solutions)
6. **Summary**: Key takeaways and concept review
7. **Assessments**: Quizzes or checkpoints aligned with Bloom's levels

**Sample Prompt**:

```
Generate comprehensive educational content for:

**Chapter [N]: [Chapter Title]**
**Section [N.M]: [Section Title]**

**Concepts covered**: [List from chapter outline]
**Prerequisites**: [Concepts that must be mastered first]
**Bloom's levels to address**: [Remember through Create]

Generate markdown content including:

1. **Section Introduction** (2-3 paragraphs)
   - Why this topic matters
   - How it connects to previous/future concepts
   - What students will learn

2. **Core Content** (structured subsections)
   - Clear explanations using analogies and examples
   - Progressive complexity (simple ’ advanced)
   - Multiple representations (text, visual, code, etc.)

3. **Worked Examples** (2-3 detailed examples)
   - Step-by-step solutions
   - Explanations of reasoning
   - Common pitfalls to avoid

4. **Interactive Elements**
   - Suggest MicroSim ideas if appropriate
   - Links to related concepts

5. **Practice Exercises** (5-8 problems)
   - Range from basic to challenging
   - Align with different Bloom's levels
   - Include brief solution guidance

6. **Section Summary**
   - Key concepts reviewed
   - Connections to broader course goals

7. **Assessment Questions** (3-5 questions)
   - Multiple choice, short answer, or applied problems
   - Cover different Bloom's levels
   - Include answer key with explanations

Use clear markdown formatting, admonitions (!!! note, !!! warning, !!! tip),
and maintain an encouraging, accessible tone.
```

**Quality Standards**:

- Content respects concept dependencies
- Multiple Bloom's levels represented
- Clear progression from simple to complex
- Examples are relevant and diverse
- Language is appropriate for target audience
- Formatting is consistent and clean

**Deliverable**: Markdown file for each section with complete educational content

---

### Step 9: MicroSim Creation

**Purpose**: Build interactive p5.js simulations to visualize and explore concepts.

**When to Create MicroSims**:

- Visual concepts that benefit from dynamic representation
- Complex processes that unfold over time
- Parameter exploration (what happens when X changes?)
- Difficult-to-grasp abstractions that need concrete representation
- Concepts with multiple perspectives or approaches

**MicroSim Structure**:

```
docs/sims/[simulation-name]/
   index.md          # Documentation and embedding page
   main.html         # Standalone HTML with p5.js
   [name].js         # Optional separate JavaScript file
```

**Template Usage**:

Use the templates in `docs/sims/templates/`:
- `index.md` - Standard documentation structure
- `index-social-override.md` - With custom Open Graph image
- JavaScript structure examples

**Key Features**:

1. **Seeded Randomness**: Reproducible variations
2. **Interactive Controls**: Sliders, buttons for parameter adjustment
3. **Real-time Updates**: Immediate visual feedback
4. **Responsive Design**: Works on different screen sizes
5. **Educational Focus**: Clarity over complexity
6. **Self-Contained**: Runs standalone or embedded

**Sample Prompt**:

```
Create an interactive p5.js MicroSimulation to visualize [CONCEPT].

Requirements:

1. **Educational Goal**: Help students understand [specific aspect]

2. **Interactive Parameters**:
   - [Parameter 1]: Range [min-max], affects [what]
   - [Parameter 2]: Range [min-max], affects [what]
   - [Parameter 3]: Range [min-max], affects [what]

3. **Visual Representation**:
   - Clear, uncluttered design
   - Appropriate colors and labels
   - Smooth animations if dynamic
   - Responsive to window size

4. **Technical Requirements**:
   - Use p5.js from CDN
   - Seeded randomness for reproducibility
   - HTML5 form controls for parameters
   - Reset and randomize functions
   - Canvas size: 800x600 or responsive

5. **Documentation**:
   - Embed in index.md with iframe
   - Explain what the simulation shows
   - Describe each parameter's effect
   - Suggest explorations for students

Generate:
1. main.html (complete standalone file)
2. index.md (documentation with iframe embed)
3. Optional: separate .js file if complex

Ensure the simulation is immediately understandable and educationally valuable.
```

**Quality Standards**:

- Clear visual design without clutter
- Intuitive controls with labels
- Meaningful parameter ranges
- Smooth performance (no lag)
- Educational value is obvious
- Works standalone and embedded
- Mobile-friendly if possible

**Deliverable**: Complete MicroSim directory with HTML, JS, and documentation

---

### Step 10: Site Assembly and Navigation

**Purpose**: Integrate all content into a coherent MkDocs site with proper navigation.

**MkDocs Configuration** (`mkdocs.yml`):

```yaml
site_name: [Course Title]
site_description: [Course Description]
site_author: [Author Name]
site_url: [URL]

theme:
  name: material
  palette:
    primary: [color]
    accent: [color]
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - search.suggest
    - search.highlight

nav:
  - Home: index.md
  - Tutorial:
    - Getting Started: tutorial/getting-started.md
    - [Other tutorial pages]
  - Concepts:
    - [Concept explanation pages]
  - Course Content:
    - Chapter 1: chapters/chapter-01/index.md
      - Section 1.1: chapters/chapter-01/section-01.md
      - Section 1.2: chapters/chapter-01/section-02.md
    - Chapter 2: chapters/chapter-02/index.md
      - [Sections...]
  - MicroSims:
    - Overview: sims/index.md
    - Learning Graph: sims/learning-graph/index.md
    - [Other simulations]
  - Resources:
    - Glossary: glossary.md
    - References: references.md

plugins:
  - search
  - social

extra:
  social:
    - icon: fontawesome/brands/github
      link: [GitHub URL]
```

**Directory Organization**:

```
docs/
   index.md                    # Home page
   tutorial/                   # MkDocs usage tutorials
   concepts/                   # Educational concept explanations
   chapters/                   # Main course content
      chapter-01/
         index.md
         section-01.md
         section-02.md
      chapter-02/
   sims/                       # MicroSimulations
      index.md
      learning-graph/
      [other-sims]/
      templates/              # Templates for new sims
   workflow/                   # Documentation of this workflow
   prompts/                    # Prompt library
   css/
      extra.css              # Custom styling
   js/
      extra.js               # Custom JavaScript
   img/                        # Images and diagrams
   glossary.md                 # Course glossary
```

**Navigation Best Practices**:

1. **Logical Hierarchy**: Group related content
2. **Progressive Disclosure**: Don't overwhelm with too many top-level items
3. **Clear Labels**: Descriptive, concise navigation text
4. **Breadcrumbs**: Enable navigation features in Material theme
5. **Search**: Ensure search plugin is configured
6. **Cross-linking**: Link related concepts throughout content

**Deliverable**: Complete, navigable MkDocs site with all content integrated

---

### Step 11: Quality Assurance and Enhancement

**Purpose**: Review, test, and improve the complete textbook.

**Quality Checks**:

**1. Content Quality**
- [ ] All concepts from enumeration are covered
- [ ] Dependencies are respected in content order
- [ ] Bloom's taxonomy levels are represented throughout
- [ ] Examples are clear, relevant, and diverse
- [ ] Explanations are accessible to target audience
- [ ] Mathematical notation is correct
- [ ] Code examples run without errors

**2. Technical Quality**
- [ ] All MicroSims load and function correctly
- [ ] Embedded iframes display properly
- [ ] Navigation links work (no broken links)
- [ ] Site builds without errors (`mkdocs build`)
- [ ] Images load and display correctly
- [ ] Responsive design works on mobile/tablet
- [ ] Search functionality works

**3. Educational Quality**
- [ ] Learning objectives are measurable
- [ ] Assessments align with objectives
- [ ] Scaffolding is appropriate
- [ ] Prerequisites are clear
- [ ] Multiple learning paths are supported
- [ ] Feedback and solutions are provided
- [ ] Glossary is complete and accurate

**4. User Experience**
- [ ] Home page is welcoming and informative
- [ ] Navigation is intuitive
- [ ] Content is easy to scan (headings, lists, formatting)
- [ ] Visual hierarchy is clear
- [ ] Loading times are reasonable
- [ ] Accessibility standards are met

**Testing Process**:

1. **Build Test**: `mkdocs build --strict` (catches warnings as errors)
2. **Local Server**: `mkdocs serve` and manually navigate all pages
3. **MicroSim Testing**: Open each simulation and test all controls
4. **Cross-browser Testing**: Check in multiple browsers if possible
5. **Mobile Testing**: Test responsive design on small screens
6. **Link Checking**: Verify all internal and external links work

**Enhancement Opportunities**:

- Add more diagrams or visualizations
- Create additional MicroSims for complex concepts
- Expand glossary with more terms
- Add more practice problems
- Include case studies or real-world applications
- Create summary/cheat sheets
- Add FAQ section
- Include video embeds if available

**Sample Prompt for Quality Review**:

```
Please review the attached [section/chapter/page] for:

1. **Content Quality**
   - Accuracy and correctness
   - Clarity of explanations
   - Appropriate difficulty level
   - Adequate examples

2. **Educational Effectiveness**
   - Alignment with learning objectives
   - Bloom's taxonomy coverage
   - Scaffolding and progression
   - Assessment quality

3. **Technical Quality**
   - Markdown formatting
   - Links and references
   - Code examples (if any)
   - Image references

4. **Improvement Suggestions**
   - What's missing or unclear?
   - Where could examples help?
   - What concepts need more explanation?
   - What interactive elements would help?

Provide specific, actionable feedback with examples.
```

**Deliverable**: Quality assurance report and enhanced content

---

### Step 12: Deployment and Maintenance

**Purpose**: Publish the textbook and establish processes for ongoing updates.

**Deployment Options**:

**1. GitHub Pages** (recommended for open educational resources):

```bash
# One-time setup
git init
git remote add origin [repository-url]

# Configure gh-pages deployment
mkdocs gh-deploy

# This builds the site and pushes to gh-pages branch
# Site will be available at: https://[username].github.io/[repository]/
```

**2. Other Hosting**:
- Netlify: Connect GitHub repo, auto-deploy on commits
- Vercel: Similar to Netlify
- Custom server: Build locally, upload `site/` directory

**Configuration for GitHub Pages**:

```yaml
# mkdocs.yml
site_url: https://[username].github.io/[repository]/
repo_url: https://github.com/[username]/[repository]
repo_name: [repository]

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/[username]/[repository]
```

**Post-Deployment Testing**:

1. [ ] Site loads at production URL
2. [ ] All navigation works
3. [ ] MicroSims load correctly
4. [ ] Images display properly
5. [ ] Search works
6. [ ] Social cards generate correctly (if enabled)
7. [ ] Analytics tracking works (if configured)

**Maintenance Workflow**:

1. **Content Updates**:
   - Edit markdown files locally
   - Test with `mkdocs serve`
   - Commit changes to git
   - Deploy with `mkdocs gh-deploy` (or push for auto-deploy)

2. **Version Control**:
   - Use semantic versioning for major updates
   - Tag releases in git
   - Maintain CHANGELOG.md
   - Document breaking changes

3. **Community Engagement** (for open resources):
   - Enable GitHub Issues for feedback
   - Review and merge pull requests
   - Respond to questions
   - Incorporate community improvements

4. **Analytics and Improvement**:
   - Monitor Google Analytics (if configured)
   - Track popular pages
   - Identify drop-off points
   - Gather user feedback
   - Iterate based on data

**Sample Deployment Commands**:

```bash
# Local development
conda activate mkdocs
mkdocs serve
# Open http://localhost:8000

# Build only (test)
mkdocs build --strict

# Deploy to GitHub Pages
mkdocs gh-deploy

# Check for broken links (using external tool)
# Install: pip install pytest-check-links
pytest --check-links docs/
```

**Deliverable**: Live, publicly accessible textbook with maintenance processes

---

## Additional Workflows

### Glossary Generation

**Purpose**: Create a comprehensive glossary of all technical terms.

**Sample Prompt**:

```
Based on all enumerated concepts and chapter content, generate a comprehensive
glossary of technical terms.

For each term:
1. **Term**: Formatted in bold
2. **Definition**: Clear, concise explanation (2-3 sentences)
3. **Context**: Where it's used in the course
4. **Related Terms**: Links to related glossary entries

Format as markdown with alphabetical organization:

# Glossary

## A

**Algorithm**: A step-by-step procedure for solving a problem or accomplishing
a task. In this course, algorithms are used to process data and make decisions.
*Related terms*: [Function](#function), [Pseudocode](#pseudocode)

Sort alphabetically and ensure all key concepts from the course are included.
```

---

### FAQ Generation

**Purpose**: Anticipate and answer common student questions.

**Sample Prompt**:

```
Generate a comprehensive FAQ section for this course covering:

1. **General Course Questions**
   - Who is this course for?
   - What prerequisites do I need?
   - How long will it take?

2. **Technical Questions**
   - What software do I need?
   - How do I set up my environment?
   - Where can I get help with code?

3. **Content Questions**
   - What if I don't understand a concept?
   - Are there additional resources?
   - How do I know I'm ready to move on?

4. **Assessment Questions**
   - How are exercises graded?
   - What if I get stuck on a problem?
   - Are solutions provided?

Format each Q&A clearly:

**Q: [Question]**
**A:** [Detailed answer with examples or links if helpful]
```

---

### Figure and Diagram Generation

**Purpose**: Create visual representations of concepts.

**Approaches**:

1. **AI Image Generation**: Use DALL-E, Midjourney, or similar for conceptual illustrations
2. **Diagramming Tools**: Use Mermaid, PlantUML, or draw.io for technical diagrams
3. **Code-Generated**: Use Python (matplotlib, seaborn) for data visualizations
4. **MicroSims**: Use p5.js for interactive visual representations

**Sample Prompt for Mermaid Diagram**:

```
Create a Mermaid diagram showing [concept/process/architecture].

Requirements:
- Clear labels on all elements
- Logical flow from left to right or top to bottom
- Color coding if multiple types of elements
- Legend if needed

Format for MkDocs embedding:
```mermaid
[diagram code]
```

Explain what the diagram illustrates and highlight key elements.
```

---

### Interactive Infographic Creation

**Purpose**: Combine text, visuals, and interaction for engaging content presentation.

**Sample Prompt**:

```
Create an interactive HTML infographic explaining [concept].

Requirements:

1. **Visual Structure**
   - Clear visual hierarchy
   - Progressive disclosure (reveal information step-by-step)
   - Responsive design

2. **Content Sections**
   - Introduction/overview
   - Key statistics or facts
   - Process or workflow
   - Examples or case studies
   - Summary/takeaways

3. **Interactive Elements**
   - Click to reveal details
   - Hover for tooltips
   - Smooth animations
   - Navigation between sections

4. **Technical**
   - Self-contained HTML file
   - CSS for styling (inline or embedded)
   - Vanilla JavaScript (no frameworks needed)
   - Works offline

Generate complete HTML code ready to embed in MkDocs or use standalone.
```

---

## Best Practices

### Content Creation

1. **Use Clear Language**: Avoid jargon unless necessary (and define it)
2. **Provide Examples**: Multiple examples covering different scenarios
3. **Use Analogies**: Connect new concepts to familiar ideas
4. **Show Visually**: Diagrams, charts, and simulations enhance understanding
5. **Include Interactivity**: Active engagement improves retention
6. **Test Knowledge**: Frequent low-stakes assessments
7. **Give Feedback**: Explain why answers are correct or incorrect
8. **Scaffold Properly**: Build complexity gradually
9. **Link Concepts**: Explicitly show relationships between ideas
10. **Encourage Practice**: Provide ample opportunities for application

### AI Prompting

1. **Be Specific**: Provide detailed requirements and constraints
2. **Give Context**: Include relevant background and files
3. **Set Standards**: Specify quality expectations
4. **Request Format**: Clearly state desired output format
5. **Iterate**: Refine prompts based on outputs
6. **Review Critically**: AI outputs require human verification
7. **Provide Examples**: Show what good looks like
8. **Check Facts**: Verify accuracy of AI-generated content
9. **Maintain Voice**: Ensure consistent tone across AI-generated sections
10. **Combine Strengths**: Use AI for drafts, humans for refinement

### MicroSim Design

1. **Educational First**: Clarity over complexity
2. **Focused Scope**: One concept per simulation
3. **Intuitive Controls**: Self-explanatory interface
4. **Immediate Feedback**: Real-time visual response
5. **Meaningful Parameters**: Adjustments that reveal insights
6. **Performance**: Smooth, responsive interaction
7. **Accessibility**: Works on various devices
8. **Documentation**: Clear explanation of what's being shown
9. **Exploration**: Encourage experimentation
10. **Integration**: Connect to textbook content

---

## Troubleshooting

### Common Issues

**MkDocs Build Errors**:
- Check YAML syntax in `mkdocs.yml` (indentation matters)
- Verify all referenced files exist
- Use `mkdocs build --strict` to catch warnings

**MicroSims Not Loading**:
- Check iframe src paths are correct
- Verify p5.js CDN link is accessible
- Test main.html standalone first
- Check browser console for errors

**Broken Links**:
- Use relative paths for internal links
- Verify file paths match directory structure
- Test all links after deployment

**Dependency Graph Issues**:
- Verify CSV format (proper delimiters, no extra commas)
- Check for circular dependencies
- Ensure all ConceptIDs are valid references

**Navigation Problems**:
- Verify `nav` section in `mkdocs.yml` matches directory structure
- Use correct file paths (relative to docs/ directory)
- Check for typos in filenames

---

## Success Criteria

A high-quality intelligent textbook should:

 **Comprehensive Coverage**: All enumerated concepts are explained
 **Logical Progression**: Content follows dependency graph
 **Multiple Bloom's Levels**: Addresses all cognitive levels
 **Interactive Elements**: Includes MicroSims and hands-on activities
 **Clear Learning Objectives**: Every chapter/section has measurable goals
 **Scaffolded Learning**: Builds from simple to complex
 **Visual Richness**: Includes diagrams, charts, and visualizations
 **Practice Opportunities**: Exercises at different difficulty levels
 **Assessment Alignment**: Tests match objectives and content
 **Accessible Language**: Appropriate for target audience
 **Professional Presentation**: Clean, consistent formatting
 **Technical Quality**: Builds without errors, all features work
 **Maintainable**: Well-organized, documented, version controlled
 **Discoverable**: Good SEO, clear navigation, working search

---

## Getting Help

- **MkDocs Documentation**: https://www.mkdocs.org
- **Material Theme**: https://squidfunk.github.io/mkdocs-material/
- **p5.js Reference**: https://p5js.org/reference/
- **Bloom's Taxonomy**: https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/
- **This Repository**: Check `/docs/tutorial/` and `/docs/concepts/` for additional guidance

---

## Conclusion

This workflow transforms a course idea into a complete, interactive intelligent textbook. By following these steps systematically and leveraging AI assistance appropriately, you can create high-quality educational resources that engage learners and facilitate deep understanding.

Remember:
- **Quality over speed**: Take time to refine content
- **User-centered design**: Always consider the learner's perspective
- **Iterative improvement**: Gather feedback and continuously enhance
- **Educational rigor**: Maintain high standards for accuracy and pedagogy
- **Technical excellence**: Ensure all interactive elements work flawlessly

Good luck with your intelligent textbook creation!
