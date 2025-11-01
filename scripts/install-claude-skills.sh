#!/bin/bash

   # Create the target directory if it doesn't exist
   mkdir -p ~/.claude/skills

   # Get the absolute path of the skills directory
   SKILLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../skills" && pwd)"

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
           echo "Created symlink: ~/.claude/skills/$skill_name -> $skill_dir"
       fi
   done

   echo "Done! All skill symlinks created in ~/.claude/skills"
