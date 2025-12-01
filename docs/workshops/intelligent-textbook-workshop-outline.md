# Intelligent Textbook Creation Workshop

**Duration:** 2 hours

!!! note "Update"
    We are hosting one at [The Thinking Spot](https://www.thethinkingspot.us/) on Monday Dec. 1st from 6:30 pm to 8:30 pm. Please let Dan know if you can attend.

[Cheat Sheet (PDF)](https://github.com/dmccreary/claude-skills/blob/main/slides/Workshop-Cheat-Sheet.pdf)

## Prerequisites

- Please come with a detailed course description prepared and ask your AI to classify learning objectives using the 2001 Bloom Taxonomy
- Please make sure that Claude Code installed with all skills loaded and usage visible
   Test: `> What skills do you know?`
- Users know how to check and extend their own token usage: [https://claude.ai/settings/usage](https://claude.ai/settings/usage)
- Basic familiarity with markdown and command-line tools

**Workshop Goal:** By the end of this workshop, participants will understand the intelligent textbook 
creation workflow and have generated core components for their own textbook using Claude Code skills.

## Workshop Outline

### Step 1: Introduction & Setup

#### 1.1 Welcome & Overview

- What are intelligent textbooks? (5 levels of intelligence)
- What is Claude Code?  How is it different that just using the web-based Claude or ChatGPT?
- Can I use Cursor or Windsurf
- Why use Claude Code Skills for textbook creation?
- Workshop structure and expected outcomes

#### 1.2 Environment Setup

Our book building tools depend on Claude Code Skills and the mkdocs build system.
The following shows how these tools also depend on other systems.

<iframe src="../../sims/install-book-env/main.html" width="100%" height="500px"></iframe>
[Fullscreen](../sims/install-book-env/main.html)

- Verify Claude Code installation
- List available skills with `/skills` command
- Review course description format
- Clone starter template or create new MkDocs project

**Hands-on:** Each participant runs `./scripts/list-skills.sh` and verifies their course description file exists.

---

### Step 2: Course Description

#### Course Description Quality
- Components of a quality course description
- Use Bloom's 2001 Taxonomy to list the learning objectives of the course
- Create precise definitions of terms you plan to use in the course

**Demo:** Use `/skill course-description-analyzer` on sample course description.  The goal is to
get your course description above 85 of 100 points before you go to the next step (learning graph generation)

**Hands-on:** Participants analyze their own course descriptions and refine based on feedback

### Step 3: Learning Graph Generation

- What is a learning graph? (concepts + dependencies)
- DAG (Directed Acyclic Graph) constraints
- No circular links (bk-check-loops)
- Taxonomy categorization (12 categories)
- Quality metrics interpretation

**Demo:**
1. Generate learning graph with `/skill learning-graph-generator`
2. Review generated files in `docs/learning-graph/`:
   - `learning-graph.csv` (concept list with dependencies)
   - `quality-metrics.md` (validation report)
   - `learning-graph.json` (vis-network visualization data)

**Hands-on:** Each participant generates their learning graph and reviews quality metrics

### Step 4: View and Edit Your Learning Graph

`> run the install-learning-graph-viewer skill`

Note that you may need to redo the legend for color and ordering of the taxonomy.

---

### Step 5: Generate Book Structure

`> run the book-chapter-generator skill`

After this step there will be a docs/chapters directory with one directory for each chapter.
The index.md file has a overview of each chapter and a list of the concepts that must be covered in the chapter

**Discussion:** How were concepts distributed across chapters? Does the ordering make pedagogical sense?

!!! tip
   By looking at the shell output you can see tradeoffs of breaking different concepts into balanced chapters.
   You can also try `log this session to logs/book-chapter-generator.md`

### Step 6: Generate Content
- Concept-to-chapter mapping
- Respecting dependency order
- Balancing chapter length and complexity

`run the chapter-content-generator on chapter 1 @docs/chapters/01-*/index.md`

Repeat this for several chapters

**Review together:**
- Markdown structure and formatting
- Admonitions and callouts
- Breaking up the "Wall of Text" problem
- Insertion of non-pure-text items (lists, tables, MicroSims)

The remainder of this class is "Supplementary Materials"

### Step 7: Glossary Creation 
- ISO 11179 definition standards (precise, concise, distinct, non-circular)
- Automatic glossary generation from concept list and terms in chapters
- Suggest terms that might have been missed

**Demo:** Use `run the glossary-generator skill` to create `docs/glossary.md`

**Hands-on:** Participants generate glossaries and review 3-5 definitions for qualit

**Demo:** Generate content for one chapter with `/skill chapter-content-generator`

**Hands-on:** Participants generate content for their first chapter

### Step 8: FAQ Generation

- The default generate about 70 FAQs but you can ask for fewer or more
- Use for helping chatbots get started
- Used to map multiple intents into standardized responses

#### Step 9: Quiz Generation (5 min)
- Bloom's Taxonomy-aligned questions
- Concept mapping to learning graph
- Interactive quiz format

**Demo:** Use `/skill quiz-generator` for a sample chapter

**Hands-on:** Participants generate quiz for their first chapter

---

### Step 10 Interactive Elements - MicroSims

#### Introduction to MicroSims 
- What are MicroSims? (interactive p5.js simulations)
- MicroSim directory structure (`docs/sims/[sim-name]/`)
- Designed for reuse and placement in any chapter or any website
- Use `iframe` to insert into a chapter
- Educational value of interactivity
- There are over 10 types of stills that know how to create MicroSims

#### p5.js MicroSim Creation
- Two-region pattern (drawing canvas + controls)
- Seeded randomness for reproducibility
- Iframe embedding in chapter content

**Demo:** Create a simple MicroSim with `/skill microsim-p5`
- Example: Visualizing slope and y-intercept changes in linear equations
- Show `main.html` structure
- Show `index.md` documentation with iframe

#### 4.3 Alternative Visualization Skills (10 min)
- **Chart.js** - data visualizations (bar, line, pie charts)
- **Mermaid** - flowcharts and process diagrams
- **Timeline** - chronological event sequences
- **Venn diagrams** - set relationships
- **Maps** - geographic visualizations

**Demo:** Quick examples of 2-3 different visualization types

**Discussion:** Which visualization types best suit different subject areas?

---

### Part 5: Quality Assurance & Deployment (10 minutes)

#### 5.1 Metrics & Validation (5 min)
- Book metrics generation (word counts, concept coverage)
- Chapter-level metrics
- Quality score interpretation

**Demo:** Use `/skill book-metrics-generator` to create comprehensive metrics report

#### 5.2 Site Building & Deployment (5 min)
- MkDocs build process
- Local preview with `mkdocs serve`
- GitHub Pages deployment with `mkdocs gh-deploy`

**Demo:** Build and preview site locally

**Hands-on:** Participants preview their textbook site at `http://localhost:8000`

---

### Part 6: Wrap-up & Next Steps (10 minutes)

#### 6.1 Complete Workflow Review (5 min)
**The 12-step intelligent textbook workflow:**

1. Course Description Development
2. Bloom's Taxonomy Integration
3. Concept Enumeration (200 concepts)
4. Concept Dependencies (DAG)
5. Concept Taxonomy Categorization
6. Learning Graph Visualization
7. Chapter/Section Structure
8. Chapter Content Generation
9. MicroSim Creation
10. Glossary & FAQ Generation
11. Quality Assurance (metrics)
12. Site Deployment

#### 6.2 Advanced Topics & Resources (3 min)
- FAQ generation from course content
- Reference list generation
- Custom skill creation
- Contributing to the skills repository

#### 6.3 Q&A and Troubleshooting (2 min)
- Common issues and solutions
- Where to get help (GitHub issues, documentation)

---

## Workshop Materials Checklist

**Before the workshop:**
- [ ] Sample course descriptions (3-4 different subjects)
- [ ] Claude Code installed on all machines
- [ ] Skills repository cloned and installed
- [ ] MkDocs and Material theme installed
- [ ] Python environment with required packages

**Handouts:**
- [ ] Quick reference card with all skill commands
- [ ] Bloom's Taxonomy cognitive levels chart
- [ ] ISO 11179 definition standards checklist
- [ ] Troubleshooting guide

**Sample Projects:**
- [ ] Complete example textbook (e.g., "Introduction to Programming")
- [ ] Partially completed textbook for hands-on practice
- [ ] Template course-description.md files

---

## Post-Workshop Follow-up

**Immediate next steps for participants:**
1. Complete chapter generation for remaining chapters
2. Generate FAQs with `/skill faq-generator`
3. Create 5-10 MicroSims for key concepts
4. Run quality metrics and address gaps
5. Deploy to GitHub Pages

**Extended learning:**
- Join the Claude skills community
- Contribute new skills or improvements
- Share completed textbooks for peer review
- Explore Level 4+ intelligence features (adaptive learning)

---

## Facilitator Notes

**Time Management:**
- Parts 1-2 must stay on schedule (foundation is critical)
- Part 3 can flex ±5 minutes based on group needs
- Part 4 is most likely to run over - have backup time
- Part 6 can be shortened if needed

**Common Issues:**
- Learning graph generation may fail if course description lacks detail
- Quality scores <70 require iteration on concept enumeration
- Circular dependencies in graphs require manual CSV editing
- MicroSim generation requires clear concept specifications

**Engagement Strategies:**
- Pair programming during hands-on sections
- Share screens to show different subject area examples
- Use chat for questions during demos
- Create shared document for troubleshooting tips

**Success Metrics:**
- 80%+ participants generate a learning graph
- 60%+ participants generate at least one chapter
- 100% participants can preview their site locally
- Post-workshop survey shows confidence in using skills independently