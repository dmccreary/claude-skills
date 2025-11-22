# Quiz: MkDocs Platform and Documentation

Test your understanding of MkDocs, Material theme, configuration, navigation, version control, and GitHub deployment with these questions.

---

#### 1. What is MkDocs primarily designed for?

<div class="upper-alpha" markdown>
1. Building e-commerce websites
2. Creating project documentation from markdown files
3. Managing relational databases
4. Developing mobile applications
</div>

??? question "Show Answer"
    The correct answer is **B**. MkDocs is a static site generator specifically designed for building project documentation from markdown files. Unlike general-purpose static site generators, MkDocs focuses exclusively on documentation workflows, providing features such as automatic navigation generation, built-in search, and live preview during development. Options A, C, and D describe purposes unrelated to MkDocs's documentation-focused design.

    **Concept Tested:** MkDocs

    **See:** [MkDocs: The Documentation Platform](../../glossary.md#mkdocs)

---

#### 2. Which file serves as the central configuration document for a MkDocs site?

<div class="upper-alpha" markdown>
1. config.json
2. settings.ini
3. mkdocs.yml
4. site.xml
</div>

??? question "Show Answer"
    The correct answer is **C**. The `mkdocs.yml` file serves as the central configuration document for your documentation site, written in YAML format. This file specifies site metadata, theme configuration, navigation structure, plugin settings, and markdown extensions in a hierarchical structure. Options A, B, and D reference files not used by MkDocs for configuration.

    **Concept Tested:** MkDocs Configuration File

    **See:** [MkDocs Configuration File (mkdocs.yml)](../../glossary.md#mkdocs-configuration-file)

---

#### 3. What does the Material for MkDocs theme add beyond basic MkDocs functionality?

<div class="upper-alpha" markdown>
1. Only color scheme customization
2. Database integration capabilities
3. Advanced features like instant loading, search highlighting, and dark mode
4. Built-in web server functionality
</div>

??? question "Show Answer"
    The correct answer is **C**. The Material theme extends MkDocs with powerful capabilities including instant loading (JavaScript-based navigation), search highlighting with keyboard navigation, code annotation, content tabs, admonitions, dark mode toggle, and social card generation. These features transform standard MkDocs sites into modern, responsive documentation portals. Option A understates the theme's capabilities, while options B and D describe features not provided by the theme.

    **Concept Tested:** MkDocs Material Theme

    **See:** [MkDocs Material Theme](../../glossary.md#mkdocs-material-theme)

---

#### 4. What markdown syntax is used to create an admonition in MkDocs?

<div class="upper-alpha" markdown>
1. Three exclamation points followed by the admonition type
2. Square brackets with the word "note" inside
3. A hash symbol followed by the admonition type
4. Curly braces surrounding the admonition content
</div>

??? question "Show Answer"
    The correct answer is **A**. Admonitions use three exclamation points (`!!!`) followed by the admonition type (such as note, tip, warning, danger). For example: `!!! note "Optional Title"` creates a note admonition. Collapsible admonitions use `???` instead of `!!!`. Options B, C, and D describe incorrect syntax that is not used for MkDocs admonitions.

    **Concept Tested:** Admonitions in MkDocs

    **See:** [Admonitions in MkDocs](../../glossary.md#admonitions-in-mkdocs)

---

#### 5. In Git version control, what is a commit?

<div class="upper-alpha" markdown>
1. A temporary backup of files
2. A snapshot of files at a specific point in time with a descriptive message
3. An automatic sync with the cloud
4. A request to download code from GitHub
</div>

??? question "Show Answer"
    The correct answer is **B**. A commit is a snapshot of files at a specific point in time with a descriptive message explaining what changed and why. Commits create permanent records in the repository history that can be referenced, compared, or restored later. Option A mischaracterizes commits as temporary, option C describes cloud sync functionality, and option D describes cloning or pulling, not committing.

    **Concept Tested:** Version Control Basics

    **See:** [Version Control Basics](../../glossary.md#version-control-basics)

---

#### 6. Which Git command uploads local commits to a remote repository like GitHub?

<div class="upper-alpha" markdown>
1. git commit
2. git add
3. git push
4. git clone
</div>

??? question "Show Answer"
    The correct answer is **C**. The `git push` command uploads local commits to a remote repository (typically GitHub), making changes available to collaborators and for deployment. `git commit` creates local snapshots, `git add` stages files, and `git clone` creates a copy of a remote repository. Only `git push` transfers local commits to remote servers.

    **Concept Tested:** Git Push Command

    **See:** [Git Push Command](../../glossary.md#git-push-command)

---

#### 7. A team is building documentation for a software project and needs to ensure that markdown lists render correctly. What formatting requirement must they follow?

<div class="upper-alpha" markdown>
1. Lists must use tabs instead of spaces for indentation
2. Lists must always be numbered, never bulleted
3. A blank line must precede markdown lists
4. Lists cannot contain more than five items
</div>

??? question "Show Answer"
    The correct answer is **C**. MkDocs requires that markdown lists and tables be preceded by a blank line to ensure proper parsing and rendering. This seemingly minor detail prevents parsing errors and ensures consistent formatting. Option A is incorrect (MkDocs uses spaces, not tabs), option B incorrectly limits list types, and option D imposes a nonexistent restriction.

    **Concept Tested:** Markdown Formatting Basics

    **See:** [Markdown Formatting Basics](../../glossary.md#markdown-formatting-basics)

---

#### 8. An educational project needs documentation that works offline, has no security vulnerabilities from dynamic components, and can be hosted anywhere. Which approach best meets these requirements?

<div class="upper-alpha" markdown>
1. WordPress blog with database backend
2. Static site generation with MkDocs
3. Dynamic web application with user authentication
4. Cloud-based content management system
</div>

??? question "Show Answer"
    The correct answer is **B**. Static site generation with MkDocs provides all requested features: offline functionality (pre-generated HTML), minimal security vulnerabilities (no dynamic server components or databases), and hosting flexibility (can be served from any web server or CDN). Options A, C, and D all involve dynamic components, databases, or specific hosting requirements that create security concerns and reduce portability.

    **Concept Tested:** MkDocs

    **See:** [MkDocs: The Documentation Platform](../../glossary.md#mkdocs)

---

#### 9. Why does the Material theme's navigation structure benefit from explicit configuration in mkdocs.yml rather than automatic generation from file structure?

<div class="upper-alpha" markdown>
1. Automatic generation is not supported by the Material theme
2. Explicit configuration provides intentional ordering that supports pedagogical progressions
3. File-based navigation causes security vulnerabilities
4. Explicit configuration reduces build time significantly
</div>

??? question "Show Answer"
    The correct answer is **B**. Explicit navigation configuration in the `nav:` section of mkdocs.yml provides precise control over menu ordering, section grouping, and hierarchy. For intelligent textbooks with complex chapter hierarchies, intentional information architecture that reflects pedagogical sequencing (foundational concepts before advanced material) provides better user experience than filesystem-derived ordering. Options A, C, and D provide incorrect rationales for explicit configuration.

    **Concept Tested:** Navigation Structure in MkDocs

    **See:** [Navigation Structure in MkDocs](../../glossary.md#navigation-structure-in-mkdocs)

---

#### 10. What does the `mkdocs gh-deploy` command accomplish?

<div class="upper-alpha" markdown>
1. Downloads the MkDocs theme from GitHub
2. Creates a new GitHub repository
3. Builds the documentation and deploys it to the gh-pages branch
4. Configures Git credentials for authentication
</div>

??? question "Show Answer"
    The correct answer is **C**. The `mkdocs gh-deploy` command automates the GitHub Pages deployment workflow by building the documentation, committing the output to the `gh-pages` branch, and pushing to GitHub in a single operation. This keeps source markdown files and build artifacts completely separated while enabling one-command deployment. Options A, B, and D describe unrelated operations.

    **Concept Tested:** GitHub Pages Deployment

    **See:** [GitHub Pages Deployment](../../glossary.md#github-pages-deployment)

---

## Quiz Statistics

- **Total Questions:** 10
- **Bloom's Taxonomy Distribution:**
  - Remember: 3 questions (30%)
  - Understand: 3 questions (30%)
  - Apply: 3 questions (30%)
  - Analyze: 1 question (10%)
- **Concepts Covered:** 10 of 10 chapter concepts (100%)
