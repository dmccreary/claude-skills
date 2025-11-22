# Quiz: Development Tools, Version Control, and Deployment

Test your understanding of Visual Studio Code, command-line interfaces, Bash shell scripting, file operations, script permissions, symlinks, and the complete textbook development workflow with these questions.

---

#### 1. Why is Visual Studio Code preferred over traditional word processors like Microsoft Word for intelligent textbook development?

<div class="upper-alpha" markdown>
1. VS Code has better spell-checking capabilities
2. VS Code is optimized for web-based markdown content with integrated terminal and Git support
3. VS Code produces smaller file sizes than Word documents
4. VS Code is the only editor that can open markdown files
</div>

??? question "Show Answer"
    The correct answer is **B**. Traditional word processors are optimized for print documents with fixed page layouts, while intelligent textbooks are dynamic, web-based resources built from markdown source files. VS Code provides markdown editing with live preview, integrated Git support, built-in terminal for MkDocs commands, and extension ecosystem—all optimized for this workflow. Option A is incorrect as both have spell-checking, option C confuses file format with editor choice, and option D is factually wrong.

    **Concept Tested:** Visual Studio Code

    **See:** [Visual Studio Code](../../glossary.md#visual-studio-code)

---

#### 2. What is the recommended workflow for efficient content development in VS Code?

<div class="upper-alpha" markdown>
1. Write all content first, then run mkdocs serve once at the end
2. Open project folder, start mkdocs serve, edit in split view with preview, save frequently
3. Edit directly in the browser at localhost:8000
4. Write content in Word, then copy-paste into VS Code
</div>

??? question "Show Answer"
    The correct answer is **B**. A typical content development session follows this pattern: open the project folder, start the development server with `mkdocs serve`, navigate to target chapter, edit in split view with markdown preview, save frequently, and preview in browser. This workflow enables rapid iteration where changes are immediately reflected in the browser within 1-2 seconds. Options A and D don't leverage the live preview capability, while option C misunderstands where editing occurs.

    **Concept Tested:** VS Code for Content Development

    **See:** [VS Code for Content Development](../../glossary.md#vs-code-for-content-development)

---

#### 3. What is a key advantage of using the integrated terminal in VS Code instead of a separate terminal application?

<div class="upper-alpha" markdown>
1. The integrated terminal runs commands faster than external terminals
2. The integrated terminal automatically opens in the project root and provides output linking to files
3. The integrated terminal is the only way to run Python scripts
4. The integrated terminal prevents all command-line errors
</div>

??? question "Show Answer"
    The correct answer is **B**. The integrated terminal eliminates context switching, automatically opens in the project root directory, and provides output linking where clicking file paths in error messages jumps to that file. It also supports split terminals for running multiple commands simultaneously. Option A confuses integration with performance, option C is factually incorrect, and option D misrepresents terminal capabilities.

    **Concept Tested:** Terminal in VS Code

    **See:** [Terminal in VS Code](../../glossary.md#terminal-in-vs-code)

---

#### 4. What is the distinction between a terminal, a shell, and Bash?

<div class="upper-alpha" markdown>
1. They are three different names for the same thing
2. Terminal is the application, shell is the command interpreter, Bash is a specific shell implementation
3. Bash is the newest version that replaces terminals and shells
4. Terminal runs on Windows, shell runs on macOS, Bash runs on Linux
</div>

??? question "Show Answer"
    The correct answer is **B**. Terminal is the application that provides a text interface (e.g., Terminal.app), shell is the program that interprets commands (e.g., Bash, Zsh, Fish), and Bash is a specific shell implementation currently most widely used on Unix-like systems. These are distinct components with different roles. Options A and C incorrectly conflate the terms, while option D mischaracterizes platform associations.

    **Concept Tested:** Bash

    **See:** [Bash](../../glossary.md#bash)

---

#### 5. You need to execute a Python script located at `docs/learning-graph/analyze-graph.py` with two arguments: `learning-graph.csv` and `quality-metrics.md`. What is the correct command structure?

<div class="upper-alpha" markdown>
1. `analyze-graph.py python learning-graph.csv quality-metrics.md`
2. `python docs/learning-graph/analyze-graph.py learning-graph.csv quality-metrics.md`
3. `run python --script analyze-graph.py --input learning-graph.csv --output quality-metrics.md`
4. `execute docs/learning-graph/analyze-graph.py (learning-graph.csv, quality-metrics.md)`
</div>

??? question "Show Answer"
    The correct answer is **B**. Bash commands follow the structure `command [options] [arguments]`. Here, `python` is the command, `docs/learning-graph/analyze-graph.py` is the first argument (script to execute), and the CSV and MD files are additional arguments. Option A reverses command and script, option C uses non-existent syntax, and option D uses invalid parenthetical argument notation.

    **Concept Tested:** Bash

    **See:** [Bash Command Structure](../../glossary.md#bash)

---

#### 6. What does the command `cd ../..` do?

<div class="upper-alpha" markdown>
1. Navigate to the current directory twice
2. Navigate up two levels to the grandparent directory
3. Navigate to the user's home directory
4. Display the contents of the parent directory
</div>

??? question "Show Answer"
    The correct answer is **B**. The `..` (double dot) represents the parent directory. Therefore, `cd ..` moves up one level, and `cd ../..` moves up two levels to the grandparent directory. Option A misunderstands the `..` notation, option C confuses `..` with `~` (home directory), and option D describes `ls ..` not `cd ..`.

    **Concept Tested:** Directory Navigation

    **See:** [Directory Navigation](../../glossary.md#directory-navigation)

---

#### 7. You need to create a new chapter directory structure at `docs/chapters/14-future-directions/`. Which command accomplishes this most efficiently?

<div class="upper-alpha" markdown>
1. `mkdir docs; mkdir docs/chapters; mkdir docs/chapters/14-future-directions`
2. `mkdir -p docs/chapters/14-future-directions`
3. `touch docs/chapters/14-future-directions`
4. `cd docs/chapters/14-future-directions`
</div>

??? question "Show Answer"
    The correct answer is **B**. The `mkdir -p` command creates the directory and all necessary parent directories in a single operation. The `-p` flag means "create parents as needed." Option A is unnecessarily verbose and would fail if docs already exists, option C creates a file not a directory, and option D attempts to navigate to a non-existent directory without creating it.

    **Concept Tested:** File Creation and Editing

    **See:** [File Creation and Editing](../../glossary.md#file-creation-and-editing)

---

#### 8. Your shell script `install-claude-skills.sh` gives a "Permission denied" error when you try to run it with `./install-claude-skills.sh`. What is the most likely cause and solution?

<div class="upper-alpha" markdown>
1. The file doesn't exist; create it with `touch install-claude-skills.sh`
2. The script lacks execute permissions; fix with `chmod +x install-claude-skills.sh`
3. The file is corrupted; delete and recreate it
4. The script is in the wrong directory; move it to /usr/bin
</div>

??? question "Show Answer"
    The correct answer is **B**. Unix-like systems require files to have execute permissions before they can be run as scripts. The `chmod +x` command adds execute permission for the owner, allowing the script to be executed. Option A would produce "No such file" not "Permission denied," option C misdiagnoses the issue, and option D is unnecessary and potentially problematic for local scripts.

    **Concept Tested:** Script Execution Permissions

    **See:** [Script Execution Permissions](../../glossary.md#script-execution-permissions)

---

#### 9. What is the primary advantage of using symbolic links (symlinks) for Claude skill installation rather than copying files?

<div class="upper-alpha" markdown>
1. Symlinks use significantly less disk space than copies
2. Symlinks automatically update when original files change, avoiding manual synchronization
3. Symlinks work on all operating systems including Windows
4. Symlinks are more secure than file copies
</div>

??? question "Show Answer"
    The correct answer is **B**. Symlinks create a reference in `~/.claude/skills/` that points to original skill files in the project repository. When original files are updated, changes are immediately reflected in all projects using that symlink, eliminating manual re-copying and synchronization. While option A is technically true, it's not the primary advantage. Options C and D are incorrect regarding symlink characteristics.

    **Concept Tested:** Symlink Creation

    **See:** [Symlink Creation](../../glossary.md#symlink-creation)

---

#### 10. In the capstone project workflow, what is the correct sequence of major phases?

<div class="upper-alpha" markdown>
1. Deployment → Course Design → Content Creation → Integration
2. Content Creation → Course Design → Integration → Deployment
3. Course Design → Content Creation → Integration → Deployment
4. Integration → Content Creation → Course Design → Deployment
</div>

??? question "Show Answer"
    The correct answer is **C**. The capstone project follows a logical progression: Phase 1 Course Design (course description, learning graph, chapter structure), Phase 2 Content Creation (chapter content, interactive elements, supporting resources), Phase 3 Integration and Quality Assurance (MkDocs configuration, testing, validation), and Phase 4 Deployment (GitHub repository setup, GitHub Pages deployment). This sequence ensures each phase builds on previous work. All other options present illogical orderings that would create workflow problems.

    **Concept Tested:** Capstone: Complete Textbook Project

    **See:** [Capstone: Complete Textbook Project](../../glossary.md#capstone-complete-textbook-project)

---
