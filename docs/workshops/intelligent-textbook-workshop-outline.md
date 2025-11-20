# Intelligent Textbook Creation Workshop

**Duration:** 2 hours

**Prerequisites:**
- Course description prepared
- Claude Code installed with all skills loaded and usage visible
- Users know how to check and extend their own token usage: [https://claude.ai/settings/usage](https://claude.ai/settings/usage)
- Basic familiarity with markdown and command-line tools

**Workshop Goal:** By the end of this workshop, participants will understand the intelligent textbook 
creation workflow and have generated core components for their own textbook using Claude skills.

## Workshop Outline

### Part 1: Introduction & Setup (15 minutes)

#### 1.1 Welcome & Overview (5 min)

- What are intelligent textbooks? (5 levels of intelligence)
- Why use Claude skills for textbook creation?
- Workshop structure and expected outcomes

#### 1.2 Environment Setup (10 min)

- Verify Claude Code installation
- List available skills with `/skills` command
- Review course description format
- Clone starter template or create new MkDocs project

**Hands-on:** Each participant runs `./scripts/list-skills.sh` and verifies their course description file exists.

---

### Part 2: Foundation - Course Description & Learning Graph (30 minutes)

#### 2.1 Course Description Quality (10 min)
- Components of a quality course description
- ISO 11179 standards for definitions
- Bloom's Taxonomy integration

**Demo:** Use `/skill course-description-analyzer` on sample course description

**Hands-on:** Participants analyze their own course descriptions and refine based on feedback

#### 2.2 Learning Graph Generation (20 min)
- What is a learning graph? (concepts + dependencies)
- DAG (Directed Acyclic Graph) constraints
- Taxonomy categorization (12 categories)
- Quality metrics interpretation

**Demo:**
1. Generate learning graph with `/skill learning-graph-generator`
2. Review generated files in `docs/learning-graph/`:
   - `learning-graph.csv` (concept list with dependencies)
   - `quality-metrics.md` (validation report)
   - `learning-graph.json` (vis-network visualization data)

**Hands-on:** Each participant generates their learning graph and reviews quality metrics

---

### Part 3: Content Generation Workflow (40 minutes)

#### 3.1 Glossary Creation (10 min)
- ISO 11179 definition standards (precise, concise, distinct, non-circular)
- Automatic glossary generation from concept list

**Demo:** Use `/skill glossary-generator` to create `docs/glossary.md`

**Hands-on:** Participants generate glossaries and review 3-5 definitions for quality

#### 3.2 Chapter Structure Planning (10 min)
- Concept-to-chapter mapping
- Respecting dependency order
- Balancing chapter length and complexity

**Demo:** Use `/skill book-chapter-generator` to create chapter structure

**Discussion:** How were concepts distributed across chapters? Does the ordering make pedagogical sense?

#### 3.3 Chapter Content Generation (15 min)
- Content generation at appropriate reading level
- Bloom's Taxonomy level distribution
- Non-text elements (diagrams, infographics, MicroSims)

**Demo:** Generate content for one chapter with `/skill chapter-content-generator`

**Review together:**
- Markdown structure and formatting
- Admonitions and callouts
- Practice problems and worked examples

**Hands-on:** Participants generate content for their first chapter

#### 3.4 Quiz Generation (5 min)
- Bloom's Taxonomy-aligned questions
- Concept mapping to learning graph
- Interactive quiz format

**Demo:** Use `/skill quiz-generator` for a sample chapter

**Hands-on:** Participants generate quiz for their first chapter

---

### Part 4: Interactive Elements - MicroSims (25 minutes)

#### 4.1 Introduction to MicroSims (5 min)
- What are MicroSims? (interactive p5.js simulations)
- MicroSim directory structure (`docs/sims/[sim-name]/`)
- Educational value of interactivity

#### 4.2 p5.js MicroSim Creation (10 min)
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