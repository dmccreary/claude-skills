# Workshop Pre-Work

Before you come to the workshop you must have Claude Code installed
with all the intelligent textbook skills installed in a Claude Code
skills directory.  You should also have a GitHub account
created and an initial GitHub repository setup with a
template intelligent textbook installed in the GitHub
repository.  Having all these components installed
before you come to our class allows us all to focus
on creation of the textbook, not the installation of
the software.

!!! Note
    Claude Code is a Linux shell system.  You must have one of the following:

    1. A Mac running MacOS or Linux
    2. A PC running Linux
    3. A virtual machine such as Docker running Linux
    4. A Raspberry Pi
    5. A Windows system running WSL (Windows System for Linux)
    6. A cloud-server account running Linux

    Claude Code does not run well on native Windows.

Here are some of the steps:

1. Create a GitHub account
2. Create a new repository within that GitHub account (your book repo called `my-intelligent-book` or similar)
3. Create a Claude Code Pro ($20/month) or Max($100/month) account
4. Install Claude Code on your computer using the [Quickstart](https://code.claude.com/docs/en/quickstart)
5. Configure Claude Code to use your Claude account using the `claude` command followed by the `/login` command
6. On a Mac, install the homebrew package installer: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`. Note you MUST have admin rights to install brew on your Mac.  On a Windows system install the WSL (Windows System for Linux).
7. Use brew or apt to install the `gh` unix command that syncs your Claude Code to your GitHub account
8. Configure Claude Code to be able to execute git commands for you and authenticate to your GitHub account by typing `configure github authentication using the gh command` into Claude
9. Create a ~/projects directory and `cd` into that directory
10. Clone your book repo using the `git clone` command
11. Clone the Claude Skills Report for intelligent books with `git clone https://github.com/dmccreary/claude-skills`
12. Edit your `~/.zshrc` file and add both `export BK_HOME="$HOME/projects/claude-skills"` and `export PATH="$HOME/.local/bin:$PATH"` and save your file
13. Update your shell with `source ~/.zshrc`
14. `cd` into the claude-skills using `cd ~/projects/claude-skills`
15. Run `./scripts/bk-install-scripts`
16. Run `./scripts/bk-install-skills`
17. Run `bk-install-mkdocs`
18. Run `cd my-intelligent-book`
19. Run `mkdocs new .`
20. Run `git status`
21. Run `git add *`
22. Run `git commit -m "initial checkin"`
22. Run `git push`
23. Run `mkdocs gh-deploy`

## Testing Your Installation

You should now be able to see your skills in your `~/.claude/skills` directory:

```sh
ls ~/.claude/skills
```

```
book-chapter-generator			glossary-generator			moving-rainbow
book-metrics-generator			installer				pi-keys-generator
causal-loop-microsim-generator.zip	learning-graph-generator		quiz-generator
chapter-content-generator		linkedin-announcement-generator		readme-generator
concept-classifier			microsim-generator			reference-generator
faq-generator				microsim-utils				skill-creator
```

You can verify the book building shell command `bk` is working by just typing:

```sh
bk
```

```
════════════════════════════════════════════════════════════════
Build/Book Utilities
════════════════════════════════════════════════════════════════
BK_HOME: /Users/dan/Documents/ws/claude-skills

   1. bk                                  Build/Book utilities menu
   2. bk-analyze-skill-usage              Generate a comprehensive skill usage analysis r...
   3. bk-batch-capture-screenshots        Batch Screenshot Capture for MicroSims
   4. bk-capture-screenshot               Capture a screenshot of a MicroSim using Chrome...
   5. bk-check-loops                      Check for loops/cycles in a learning graph
   6. bk-check-social-media               Verify Open Graph social media tags in a MicroS...
   7. bk-diagram-reports                  Generates comprehensive diagram and MicroSim re...
   8. bk-generate-book-metrics            Generates comprehensive metrics reports for int...
   9. bk-install-mkdocs                   Install MkDocs environment with Conda
  10. bk-install-scripts                  Creates symbolic links for all bk* scripts in $...
  11. bk-install-skills                   Creates symbolic links in ~/.claude/skills/ for...
  12. bk-install-skills-codex             Creates symbolic links in ~/.codex/skills/ for ...
  13. bk-install-social-override-plugin   Installs social_override plugin for mkdocs-mate...
  14. bk-list-skills                      List all Claude skills with their descriptions
  15. bk-microsim-quality-report-generator Generate quality reports for MicroSims
  16. bk-resize-images                    Compresses large images to approximately 300KB ...
  17. bk-status                           Check the status of an intelligent textbook pro...

════════════════════════════════════════════════════════════════
Usage: bk - show this menu
       bk [number] - run the corresponding script
════════════════════════════════════════════════════════════════
```

You should be able see your book in HTML form:

[http://GITHUB_ID.github.io/my-intelligent-book](http://GITHUB_ID.github.io/my-intelligent-book)

## Testing Skills

Ask claude what skills he knows about

`claude`
> What skills do you know about for building intelligent textbooks and MicroSims?