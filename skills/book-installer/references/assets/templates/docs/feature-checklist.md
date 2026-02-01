# Intelligent Textbook Feature Checklist

This checklist helps authors and product managers understand what features are available in the MkDocs Material intelligent textbook ecosystem. For each feature, you'll see whether it's implemented in this book and how much effort it takes to add.

!!! note
    A level 2+ textbook is one that has rich interactivity but does not store any
    personal student data. A level 2+ textbook can be converted to a level 3
    textbook by sending event data to a learning record store (LRS) to create
    a hyper-personalized learning experience for each student. The five levels
    of intelligent textbooks are described in the [Intelligent Textbooks](https://dmccreary.github.io/intelligent-textbooks/) course.

An **intelligent textbook** goes beyond static text to include interactive simulations, personalized learning paths, auto-graded quizzes, and AI-generated content. This checklist tracks which of these capabilities are present in this textbook.

**Legend:**

- :white_check_mark: Feature is implemented and working
- :x: Feature is not yet implemented
- :construction: Feature is partially implemented

## Effort Levels

| Level | Description | Human Time | With GenAI | With GenAI Skills |
|-------|-------------|------------|------------|-------------------|
| **Trivial** | Config change or copy template | Minutes | Seconds | Seconds |
| **Low** | Single file creation with standard content | Hours | Minutes | Seconds |
| **Medium** | Multiple files, some customization needed | Day | Hours | Minutes |
| **High** | Significant content generation or custom code | Days | Hours | Minutes |
| **Very High** | Complex integration, AI generation, or external tools | Week+ | Day | Hours |

---

## Basic Features

These features come by default with MkDocs Material or require minimal configuration.

| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| Navigation sidebar | {navigation_sidebar} | Trivial | Left-side menu showing all chapters and sections |
| Search functionality | {search_functionality} | Trivial | Instant search across all pages as you type |
| Table of contents (per page) | {table_of_contents} | Trivial | Right-side outline of headings on current page |
| Site title and description | {site_title} | Trivial | In `mkdocs.yml` |
| Site author metadata | {site_author} | Trivial | In `mkdocs.yml` |
| GitHub repository link | {github_repo} | Trivial | `repo_url` configured |
| Custom logo | {custom_logo} | Trivial | Custom logo in header |
| Custom favicon | {custom_favicon} | Trivial | Custom icon in browser tab |
| Color theme (primary/accent) | {color_theme} | Trivial | Custom color palette |
| Footer navigation (prev/next) | {footer_navigation} | Trivial | Previous/Next chapter links at bottom of each page |
| Navigation expand on hover | {navigation_expand} | Trivial | Sidebar sections expand when you hover over them |
| Back to top button | {back_to_top} | Trivial | Floating button to scroll back to page top |
| Navigation path breadcrumbs | {breadcrumbs} | Trivial | Shows path like "Home > Chapter 3 > Feedback" |
| Section index pages | {section_index} | Trivial | Each folder can have its own landing page |
| License page | {license_page} | Low | Standard CC license template |
| Contact page | {contact_page} | Low | Contact form or info |
| About page (detailed) | {about_page} | Low | Exists but minimal content |
| How We Built This Site | {how_we_built} | Medium | Describe tools and process |
| Copyright on every footer | {copyright_footer} | Trivial | Copyright notice in footer |

---

## Intermediate Features

These features require plugins, extensions, or moderate configuration.

### Content Enhancement

These features make your content more engaging and easier to read.

| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| GLightBox (image zoom) | {glightbox} | Low | Click any image for lightbox popup; requires `mkdocs-glightbox` Python library |
| KaTeX equation rendering | {katex} | Low | Display beautiful math equations; uses `\(...\)` for inline, `$$...$$` for display |
| MathJax equation rendering | {mathjax} | Low | Alternative math rendering with broader LaTeX support |
| Admonitions (callout boxes) | {admonitions} | Trivial | Colored boxes for notes, warnings, tips, and examples |
| Code blocks with copy button | {code_copy_button} | Trivial | One-click copy for all code examples |
| Syntax highlighting with line numbers | {syntax_highlighting} | Trivial | Code colored by language (Python, JavaScript, etc.) |
| Tabbed content blocks | {tabbed_content} | Trivial | Switch between versions (e.g., Python vs. pseudocode) |
| Task list checkboxes | {task_lists} | Trivial | Interactive checklists like [ ] and [x] |
| Mark/highlight text | {mark_highlight} | Trivial | Use `==text==` syntax to highlight important phrases in yellow |
| Strikethrough text | {strikethrough} | Trivial | Use `~~text~~` syntax to cross out deprecated or incorrect info |
| Magic links (auto-linking) | {magic_links} | Trivial | URLs and emails automatically become clickable |
| Snippets (file includes) | {snippets} | Trivial | Use `--8<-- "file.md"` syntax to include content from other files |
| Emoji support | {emoji} | Trivial | Use :emoji_name: shortcodes like :rocket: |
| Collapsible details blocks | {collapsible_details} | Trivial | Hide/show content with expandable sections |
| Mermaid diagrams | {mermaid} | Trivial | Flowcharts, sequence diagrams from text |

### Site-Wide Resources

These are pages and files that support the entire textbook rather than individual chapters.

| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| Glossary | {glossary} | Medium | {glossary_term_count} terms with ISO 11179 compliant definitions |
| FAQ page | {faq} | Medium | {faq_question_count} answers to common student questions |
| References page | {references} | Medium | Curated bibliography with links per chapter or site-wide |
| Custom CSS styling | {custom_css} | Low | Override theme colors, fonts, and layouts |
| Custom JavaScript | {custom_js} | Low | Add interactivity beyond built-in features |
| Google Analytics | {google_analytics} | Trivial | Track page views and user behavior |

### Publishing Features

These features help your textbook look professional when shared on social media.

| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| Social media preview cards | {social_media_cards} | Medium | Auto-generated images shown when sharing links |
| Edit page button | {edit_page_button} | Trivial | "Edit this page" link to GitHub for community contributions |

---

## Advanced Features

These features require significant effort, custom code, or AI assistance.

### Interactive Learning

MicroSims are small, browser-based simulations that let students experiment with concepts.

| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| MicroSims (interactive simulations) | {microsims} | High | {microsim_count} browser-based apps for hands-on learning |
| MicroSim index catalog | {microsim_index} | Medium | Visual gallery with cards showing all available simulations |
| Per-chapter quizzes | {per_chapter_quizzes} | High | {quiz_file_count} quiz files with questions aligned to learning objectives |

### Learning Graph System

A learning graph maps every concept in the course and shows which concepts depend on others.

| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| Course description | {course_description} | Medium | Goals and outcomes using Bloom's Taxonomy levels |
| Concept list (~200-300 concepts) | {concept_list} | High | Every topic students need to learn, extracted with AI help |
| Learning graph CSV | {learning_graph_csv} | High | Spreadsheet defining which concepts depend on others |
| Learning graph JSON | {learning_graph_json} | Low | Machine-readable format for the graph viewer |
| Learning graph viewer (vis-network) | {graph_viewer} | Medium | Interactive diagram where you can click and explore concepts |
| Concept taxonomy classification | {concept_taxonomy} | Medium | Grouping concepts into categories |
| Quality metrics report | {quality_metrics} | Low | Statistics about graph completeness and structure |
| Book metrics | {book_metrics} | Medium | Word counts, reading time, and chapter statistics |
| Chapter metrics | {chapter_metrics} | Medium | Detailed stats for each chapter individually |
| Glossary quality report | {glossary_quality_report} | Low | Check definitions follow standards |
| FAQ quality report | {faq_quality_report} | Low | Check FAQ completeness |
| FAQ coverage gaps | {faq_coverage_gaps} | Low | Find concepts not addressed in FAQ |
| Quiz generation report | {quiz_generation_report} | Low | Quality report for generated quizzes |

### Content Generation

These features involve creating the actual educational content.

| Feature | Status | Effort | Notes |
|---------|--------|--------|-------|
| Chapter content | {chapters} | Very High | {chapter_count} chapters with full text, examples, and exercises |
| Sample prompts collection | {prompts_collection} | Medium | Saved AI prompts so content can be regenerated consistently |

---

## Feature Dependencies

Some features require others to be implemented first.

```
Course Description
    └── Concept List
        └── Learning Graph (CSV)
            ├── Learning Graph (JSON)
            │   └── Graph Viewer
            ├── Glossary
            │   └── Glossary Quality Report
            ├── FAQ
            │   ├── FAQ Quality Report
            │   └── FAQ Coverage Gaps
            └── Chapter Content
                ├── Per-Chapter Quizzes
                ├── Per-Chapter References
                └── Book/Chapter Metrics
```

---

## Cost Considerations

Most intelligent textbook features use free, open-source software.

| Feature Category | License Cost | Notes |
|------------------|--------------|-------|
| MkDocs Material | Free (MIT) | Static site generator and theme |
| Python dependencies | Free | Pillow and CairoSVG for social preview images |
| vis-network.js | Free (MIT) | JavaScript library for interactive graph diagrams |
| p5.js | Free (LGPL) | JavaScript library for creative coding and simulations |
| KaTeX | Free (MIT) | Fast math equation rendering in the browser |
| AI image generation | **$20+/month** | Required for creating infographics with DALL-E or ImageFX |
| Claude/ChatGPT for content | Varies | Used to draft chapters, quizzes, and glossary entries |

---

## Quick Start: Adding Missing Features

Start with the easiest wins and work your way up.

### Highest Impact, Lowest Effort

These can be done in under an hour:

1. **License page** - Copy the standard Creative Commons template
2. **Contact page** - Add author email or feedback form
3. **Edit page button** - One line in `mkdocs.yml` enables "Suggest an edit" links
4. **Social media cards** - Auto-generate preview images when shared

### Medium Effort, High Value

These use Claude Code skills to generate content:

1. **Glossary** - Use the glossary-generator skill to create searchable definitions
2. **FAQ** - Use the faq-generator skill to answer common student questions
3. **Book metrics** - Use the book-metrics-generator skill to track completeness
4. **Per-chapter quizzes** - Use the quiz-generator skill for auto-graded practice

### High Effort, Transformative

These take more time but significantly enhance the learning experience:

1. **Additional MicroSims** - Each simulation takes 2-4 hours; aim for 10-20 total
2. **AI-generated infographics** - Requires paid image generation subscription
3. **Instructor's guide** - Helps teachers adopt your textbook

---

*Generated by book-installer feature-checklist-generator*

*Last updated: {generation_date}*
