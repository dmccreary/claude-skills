#!/bin/bash

# List all Claude skills with their descriptions
# Extracts name and description from YAML frontmatter in SKILL.md files

USER_SKILLS_DIR="$HOME/.claude/skills"
PROJECT_SKILLS_DIR=".claude/skills"

echo "Available Claude Skills"
echo "======================="
echo ""

# Function to process skills in a directory
process_skills_dir() {
    local skills_dir="$1"
    local location="$2"

    # Check if skills directory exists
    if [ ! -d "$skills_dir" ]; then
        return
    fi

    # Loop through each directory in skills/
    for skill_dir in "$skills_dir"/*; do
        # Skip if not a directory
        if [ ! -d "$skill_dir" ]; then
            continue
        fi

        skill_name=$(basename "$skill_dir")
        skill_md="$skill_dir/SKILL.md"

        # Check if SKILL.md exists
        if [ ! -f "$skill_md" ]; then
            echo "⚠️  $skill_name: No SKILL.md file found"
            echo ""
            continue
        fi

        # Extract name and description from YAML frontmatter
        # Read lines between --- markers and extract name and description
        in_frontmatter=0
        name=""
        description=""

        while IFS= read -r line; do
            # Check for YAML frontmatter delimiters
            if [[ "$line" == "---" ]]; then
                if [ $in_frontmatter -eq 0 ]; then
                    in_frontmatter=1
                else
                    # End of frontmatter, stop reading
                    break
                fi
                continue
            fi

            # If we're in frontmatter, extract name and description
            if [ $in_frontmatter -eq 1 ]; then
                if [[ "$line" =~ ^name:\ * ]]; then
                    name=$(echo "$line" | sed 's/^name: *//')
                elif [[ "$line" =~ ^description:\ * ]]; then
                    # Handle multi-line descriptions
                    description=$(echo "$line" | sed 's/^description: *//')
                fi
            fi
        done < "$skill_md"

        # Display the skill information
        if [ -n "$name" ]; then
            echo "📘 Skill: $name ($location)"
        else
            echo "📘 Skill: $skill_name ($location)"
        fi

        if [ -n "$description" ]; then
            echo "   Description: $description"
        else
            echo "   Description: (No description found)"
        fi

        echo ""
    done
}

# Process user skills directory
process_skills_dir "$USER_SKILLS_DIR" "user"

# Process project skills directory
process_skills_dir "$PROJECT_SKILLS_DIR" "project"

echo "======================="

# Count total skills from both directories
# Note: Use -type d,l to count both directories and symlinks
user_count=0
project_count=0

if [ -d "$USER_SKILLS_DIR" ]; then
    user_count=$(find "$USER_SKILLS_DIR" -mindepth 1 -maxdepth 1 \( -type d -o -type l \) 2>/dev/null | wc -l | tr -d ' ')
fi

if [ -d "$PROJECT_SKILLS_DIR" ]; then
    project_count=$(find "$PROJECT_SKILLS_DIR" -mindepth 1 -maxdepth 1 \( -type d -o -type l \) 2>/dev/null | wc -l | tr -d ' ')
fi

total_count=$((user_count + project_count))
echo "Total skills: $total_count (user: $user_count, project: $project_count)"
