# Quiz: Claude Skills Architecture and Development

Test your understanding of skill directory structure, supporting assets, testing, security, distribution, Git commands, and Python package management with these questions.

---

#### 1. What is the primary skill definition file that serves as the entry point for Claude?

<div class="upper-alpha" markdown>
1. README.md
2. SKILL.md
3. config.json
4. skill-definition.txt
</div>

??? question "Show Answer"
    The correct answer is **B**. SKILL.md serves as both the entry point for Claude and documentation for developers. Its YAML frontmatter defines metadata including name, description, and optionally allowed-tools, while the markdown body contains the detailed workflow instructions that Claude executes when the skill is invoked. Options A, C, and D reference files not used as skill definition files in the Claude Skills architecture.

    **Concept Tested:** Skill Directory Structure

    **See:** [Skill Directory Structure](../../glossary.md#skill-directory-structure)

---

#### 2. Which category of supporting assets provides computational capabilities for tasks that exceed Claude's direct tool access?

<div class="upper-alpha" markdown>
1. Template files
2. Reference documentation
3. Python scripts
4. Configuration files
</div>

??? question "Show Answer"
    The correct answer is **C**. Python scripts provide computational capabilities for tasks that exceed Claude's direct tool access or require specialized algorithms. Common use cases include data transformation, graph analysis, quality validation, and format conversion. Template files provide structured content patterns, reference documentation provides detailed guidelines, and configuration files are not a primary supporting asset category.

    **Concept Tested:** Python Scripts in Skills

    **See:** [Python Scripts in Skills](../../glossary.md#python-scripts-in-skills)

---

#### 3. What is the purpose of reference documentation files in Claude Skills?

<div class="upper-alpha" markdown>
1. To execute automated data processing
2. To provide detailed specifications and guidelines without cluttering SKILL.md
3. To store user preferences
4. To generate test cases
</div>

??? question "Show Answer"
    The correct answer is **B**. Reference documentation files provide detailed specifications, guidelines, and context that inform skill execution without cluttering the main SKILL.md workflow. These files are typically loaded at specific points in the workflow when detailed information is needed, such as reading-level guidelines or content-element-type specifications. Options A, C, and D describe functions not served by reference documentation.

    **Concept Tested:** Reference Documentation in Skills

    **See:** [Reference Documentation in Skills](../../glossary.md#reference-documentation-in-skills)

---

#### 4. Which testing strategy verifies that a skill performs correctly with missing files or malformed data?

<div class="upper-alpha" markdown>
1. Unit testing
2. Edge case testing
3. End-to-end testing
4. Regression testing
</div>

??? question "Show Answer"
    The correct answer is **B**. Edge case testing verifies behavior with missing files, malformed data, or unusual inputs that fall outside normal operating conditions. This testing strategy ensures skills handle exceptional situations gracefully rather than failing unexpectedly. Unit testing checks individual components, end-to-end testing validates complete workflows, and regression testing ensures existing functionality remains intact after changes.

    **Concept Tested:** Skill Testing and Debugging

    **See:** [Skill Testing and Debugging](../../glossary.md#skill-testing-and-debugging)

---

#### 5. In Claude Skills security model, what is the principle behind the allowed-tools field?

<div class="upper-alpha" markdown>
1. Maximum privilege to enable all features
2. Least privilege, granting only necessary tools
3. Equal privilege across all skills
4. Dynamic privilege based on user role
</div>

??? question "Show Answer"
    The correct answer is **B**. The allowed-tools field implements the principle of least privilege, granting only the tools necessary for the skill's function. This security mechanism prevents skills from performing unintended operations by restricting access to specific Claude Code tools. Options A, C, and D describe security principles not used in the Claude Skills permission model.

    **Concept Tested:** Security in Skill Execution

    **See:** [Security in Skill Execution](../../glossary.md#security-in-skill-execution)

---

#### 6. Where are globally installed skills stored to make them available across all projects?

<div class="upper-alpha" markdown>
1. /usr/local/bin/skills/
2. .claude/skills/ in the project directory
3. ~/.claude/skills/ in the user's home directory
4. /opt/claude/global-skills/
</div>

??? question "Show Answer"
    The correct answer is **C**. Global skill installation places skills in `~/.claude/skills/` in the user's home directory, making them available across all Claude Code sessions regardless of current working directory. Project-specific skills are stored in `.claude/skills/` within a project directory. Options A and D reference directories not used by Claude Skills.

    **Concept Tested:** Installing Skills Globally

    **See:** [Installing Skills Globally](../../glossary.md#installing-skills-globally)

---

#### 7. A developer needs to create a skill that will be used across multiple intelligent textbook projects with identical functionality. Should they use global or project-specific installation?

<div class="upper-alpha" markdown>
1. Project-specific, to ensure each project can customize the skill
2. Global, to enable reusability without duplicating the skill in each project
3. Both simultaneously, to provide redundancy
4. Neither, skills cannot be shared across projects
</div>

??? question "Show Answer"
    The correct answer is **B**. Global installation is ideal for general-purpose skills that apply across many projects, providing reusability without duplication. The skill can be modified once to affect all projects. Project-specific installation is more appropriate when skills contain project-specific logic or when different projects require different versions. Options C and D describe incorrect installation approaches.

    **Concept Tested:** Installing Skills Globally

    **See:** [Installing Skills Globally vs Project-Specific](../../glossary.md#installing-skills-globally)

---

#### 8. What is the purpose of the `git status` command?

<div class="upper-alpha" markdown>
1. To create a new commit
2. To display the current state of the working directory and staging area
3. To upload changes to GitHub
4. To merge two branches
</div>

??? question "Show Answer"
    The correct answer is **B**. The `git status` command displays the current state of the working directory and staging area, showing modified files, untracked files, staged changes, branch information, and sync status with remote. This command helps developers understand repository state before committing changes. Options A, C, and D describe the functions of `git commit`, `git push`, and `git merge` respectively.

    **Concept Tested:** Git Status Command

    **See:** [Git Status Command](../../glossary.md#git-status-command)

---

#### 9. A skill requires the Python packages pandas, networkx, and matplotlib. How should these dependencies be documented and installed?

<div class="upper-alpha" markdown>
1. List them in a README file and ask users to install manually
2. Include them in SKILL.md frontmatter
3. Document them in requirements.txt and install with pip install -r requirements.txt
4. Embed installation commands directly in the skill workflow
</div>

??? question "Show Answer"
    The correct answer is **C**. Python package dependencies should be documented in a `requirements.txt` file specifying exact versions (e.g., `pandas==2.1.0`), then installed using `pip install -r requirements.txt`. This approach ensures reproducible environments and follows Python packaging best practices. Option A lacks automation, option B misuses frontmatter, and option D conflates dependency installation with skill execution.

    **Concept Tested:** pip Package Management

    **See:** [Installing Python Packages](../../glossary.md#installing-python-packages)

---

#### 10. Why is distributing skills via Git repositories more flexible than packaged archives?

<div class="upper-alpha" markdown>
1. Git repositories are smaller in file size
2. Git repositories enable version control, collaborative development, and easy updates
3. Git repositories work offline while archives require internet
4. Git repositories don't require documentation
</div>

??? question "Show Answer"
    The correct answer is **B**. Git repositories provide the most flexible and maintainable distribution method because they enable version control (complete change history), collaborative development (forks and pull requests), issue tracking, and easy updates (users can pull latest changes). Archive distribution sacrifices these benefits but reduces installation barriers for non-technical users. Options A, C, and D provide incorrect or misleading comparisons.

    **Concept Tested:** Skill Distribution Methods

    **See:** [Skill Distribution Methods](../../glossary.md#skill-distribution-methods)

---

## Quiz Statistics

- **Total Questions:** 10
- **Bloom's Taxonomy Distribution:**
  - Remember: 3 questions (30%)
  - Understand: 3 questions (30%)
  - Apply: 3 questions (30%)
  - Analyze: 1 question (10%)
- **Concepts Covered:** 13 of 22 chapter concepts (59%)
