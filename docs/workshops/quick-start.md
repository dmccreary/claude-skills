# Quickstart to Building an Intelligent Textbook

This file assumes you have doe the [Workshop Prework](./workshop-prework.md)

Before you begin, you should have the following installed:

1. Claude - just type `claude` the command line.
1. Python 3
2. A conda virtual environment with Python 3 installed called "mkdocs"
3. pip - the python installer package
4. mkdocs mkdocs-material
5. Any image processing tools that you will need to build the preview images for the social preview images
6. The `gh` unix command that does github manipulations

## Setup

Copy these lines into Claude one at a time and verify they work.

!!! prompt
    Create a directory called "projects" in my home directory and change directory (cd) into that new projects directory.

    Clone the following repo into my `conda virtual environment called "mkdocs"` https://github.com/dmccreary/claude-skills

    Add the BK_HOME to my shell startup file (.bashrc on WST or .zshrc on MacOS)
    and set it to ~/projects/claude-skills so the shell scripts run.  See the README for details: ~/projects/claude-skills/scripts/README.md

    Run the projects/claude-skills/scripts/bk-install-skills shell script

    Run the projects/claude-skills/scripts/bk-install-skills shell script

    Run the "bk" command to verify the command line utilities all work

    Ask Claude "what skills do you know?"

    Create the conda virtual environment called "mkdocs" and add the mkdocs-material python library into it.

    Create a new github repository for me called `my-intelligent-book` or another similar name that identifies my book like "pre-calculus-course".

    Clone the `my-intelligent-book` repo into my projects directory.

    Copy a mkdocs.yml file from your favorite book (calculus, statistics, physics, linux, computer science).  Get the full list here: https://dmccreary.github.io/intelligent-textbooks/case-studies/ or have Claude generate one for you.

    Create a detailed course description on the subject SUBJECT_NAME and include all the things you would see in a detailed course description including learing objectives categorized by the 2001 Bloom Taxonomy.

    Run the /course-description-analyzer on my course description

    Get the quality score above 85.

    Run the /learning-graph-generation skill

    Run the /book-chapter-generator

    Run the /book-installer skill and create a mascot (copy the prompts into an image generator like OpenAI ChatGPG DALL-E or Google nano-banana)

    For each of the chapters in @docs/chapters/*/index.md run the /chapter-content-generator

    Run the /glossary-generator skill

    Run the /faq-generator-skill

    For each chapter in @docs/chapters/*/index.md run the quiz generator and put the quiz in the chapter directory with a file name quiz.md

    Run the /references-generator skill and create a references.md file in each chapter generator

    For each #### Diagram in @docs/chapter/01*/index.md run the /microsim-generator skill

    Repeat this for each chapter and check the quality of each MicroSim

    Run the ~./.local/bin/bk-capture-screenshot script on each of the microsims
    in @docs/sims/* using the parameters <dir> <delay=3> <height> where height is
    taken from the iframe in the index.md of the microsim directory.

    Run the /book-installer skill that generates the @docs/sims/index.md which generates mkdocs material grid cards for every microsim.

    Run the ~/.local/bin/bk-generate-book-metrics which will generate the metrics for the entire book and create a markdown report in the @docs/learning-graph

    Run the  ~/.local/bin/bk-diagram-reports
    which will generate the diagram metrics for the entire book and create a markdown report in the @docs/learning-graph

    Run the  ~/.local/bin/bk-install-social-override-plugin

    Run the mkdocs build program and repair any missing links

    Run the /book-installer generate a LinkedIn announcement
