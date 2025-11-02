# Getting Starting Using Intelligent Textbook Skills

## Downloading the Skills

The best way to download the skills is to use the git clone command:

```sh
cd proojects
git clone https://github.com/dmccreary/claude-skills.git
```

After you have downloaded the skills you have two options:

1. **Personal Level:** Install these skills for ALL your projects. (Recommended)
2. **Project Level:** Install these skills for a specific project

The first option will allow you to work on many different intelligent textbook projects without duplicating the skills on your local computer.  It is highly recommended.

The only reason that you might want to use the second option for specific projects is if you are doing complex development such as creating different versions of these skills.

## Installation for ALL projects

We will do this by creating a `symbolic link` from your home claude directory to the cloned out skills area.

In the example below, we assume you are in the `projects/claude-skills` area that you just cloned.

Run the script

```sh
cd scripts
./install-claude-skills.sh
```

You will see a log of all the skills that were correctly installed:

```
Created symlink: ~/.claude/skills/faq-generator -> /Users/dan/Documents/ws/claude-skills/skills/faq-generator
Created symlink: ~/.claude/skills/glossary-generator -> /Users/dan/Documents/ws/claude-skills/skills/glossary-generator
Created symlink: ~/.claude/skills/intelligent-textbook -> /Users/dan/Documents/ws/claude-skills/skills/intelligent-textbook
Created symlink: ~/.claude/skills/intelligent-textbook-creator -> /Users/dan/Documents/ws/claude-skills/skills/intelligent-textbook-creator
Created symlink: ~/.claude/skills/learning-graph-generator -> /Users/dan/Documents/ws/claude-skills/skills/learning-graph-generator
Created symlink: ~/.claude/skills/microsim-p5 -> /Users/dan/Documents/ws/claude-skills/skills/microsim-p5
Created symlink: ~/.claude/skills/moving-rainbow -> /Users/dan/Documents/ws/claude-skills/skills/moving-rainbow
Created symlink: ~/.claude/skills/quiz-generator -> /Users/dan/Documents/ws/claude-skills/skills/quiz-generator
```

## Getting Updates

These skills will be updated frequently.  To install the latest release, just run the git pull:

```sh
cd projects/claude-sills
git pull
```

## Details of the Installation script

The script will create a set of symbolic link commands, one for each skill file in this repo.

```sh
#!/bin/bash

   # Create the target directory if it doesn't exist
   # CHANGE $HOME to be the project you are working on
   # $HOME = ~
   # $HOME = /User/NAME/projects/PROJECT_NAME/.claude/skills
   mkdir -p $HOME/.claude/skills

   # Get the absolute path of the skills directory
   SKILLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/skills" && pwd)"

   # Create symbolic links for each skill folder
   for skill_dir in "$SKILLS_DIR"/*; do
       if [ -d "$skill_dir" ]; then
           skill_name=$(basename "$skill_dir")
           target_link="$HOME/.claude/skills/$skill_name"

           # Remove existing symlink if it exists
           if [ -L "$target_link" ]; then
               rm "$target_link"
           fi

           # Create the symbolic link
           ln -s "$skill_dir" "$target_link"
           echo "Created symlink: $HOME/.claude/skills/$skill_name -> $skill_dir"
       fi
   done

   echo "Done! All skill symlinks created in $HOME/.claude/skills"
```

If you want to change the links to work in your specific project, just change the
path where the links are created.

Change:

```sh
$HOME = ~
```

to be:

```sh
$HOME = /User/NAME/projects/PROJECT_NAME/.claude/skills
```

## Testing Your Skill List

```
What skills do you know about.  Check the ~/.claude/skills/ area.
```

Response:

```
You have 8 skills installed in ~/.claude/skills/:

  1. faq-generator - Generates FAQ content
  2. glossary-generator - Creates glossary entries
  3. intelligent-textbook - Works with intelligent textbook content
  4. intelligent-textbook-creator - Creates intelligent textbooks
  5. learning-graph-generator - Generates learning graphs
  6. microsim-p5 - Creates p5.js micro-simulations
  7. moving-rainbow - Creates moving rainbow animations
  8. quiz-generator - Generates quiz content
```

## Add the /skills Command

Sadly, Claude Code version: 2.0.31 does not know how to list the skills you have.
But if you are clever, you can add your own custom `slash command` that will list
them for you.

The secret is that both the ~/.claude and your project .claude have an optional
directory called /commands.  When you type "/skill" it will check those
locations for a command that matches what you type.

There are two steps:

1. You must create a file called skills.md in the `~/.claude/commands` area.
2. You must put a UNIX shell script (or Power shell script on Winodw) in your $PATH that will list the skills in the ~/.claude/skills area.

You will find a sample UNIX shell script in the [/scripts](https://github.com/dmccreary/claude-skills/blob/main/scripts/list-skills.sh) area of my [dmccreary](https://github.com/dmccreary[) ]claude-skills](https://github.com/dmccreary/claude-skills) GitHub repo.

You can use this command to install these two files.

Next, you can install a custom shell script that is called when you type the /skills command.

You can find a UNIX script in the `scripts/list-skills.sh`.  To bind this to the skills slash
command you must copy the file 'commands/skills.md' into your .claude/skills area.

## Installation Script for the Skills Command

You will find a UNIX shell command that will install the Skills Command here:

[]()

## Sample Skill Slash Command Execution

I just type '/sk` into Claude Code and you should see the code listed

![](../docs/img/claude-code-skill-command.png)

**Result:**

```
Available Claude Skills (8 total)

  Educational Content Creation:
  - faq-generator (user) - Generates FAQs from course content
  - glossary-generator (user) - Creates ISO 11179-compliant glossaries
  - quiz-generator (user) - Creates Bloom's Taxonomy-aligned quizzes

  Intelligent Textbook Development:
  - intelligent-textbook (user) - Complete workflow for AI-generated textbooks
  - intelligent-textbook-creator (user) - Creates MkDocs Material textbooks (Level 2-5)
  - learning-graph-generator (user) - Generates 200-concept learning graphs

  Interactive Simulations:
  - microsim-p5 (user) - Creates p5.js educational MicroSims

  Hardware Projects:
  - moving-rainbow (user) - MicroPython for Raspberry Pi Pico NeoPixels

  All 8 skills are from your user directory (~/.claude/skills/). No project-specific skills found in .claude/skills/.

```



