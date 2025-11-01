#!/bin/bash

# List all Claude skills with their descriptions
# Supports multiple output formats: text, csv, json, markdown

SKILLS_DIR="$HOME/.claude/skills"
FORMAT="${1:-text}"  # Default to text format

# Check if skills directory exists
if [ ! -d "$SKILLS_DIR" ]; then
    echo "Error: Skills directory not found at $SKILLS_DIR" >&2
    exit 1
fi

# Function to strip quotes from strings
strip_quotes() {
    echo "$1" | sed 's/^["'\'']\(.*\)["'\'']$/\1/'
}

# Array to store skill data
declare -a names
declare -a descriptions
declare -a locations

# Collect all skill data
for skill_dir in "$SKILLS_DIR"/*; do
    if [ ! -d "$skill_dir" ]; then
        continue
    fi

    skill_name=$(basename "$skill_dir")
    skill_md="$skill_dir/SKILL.md"

    if [ ! -f "$skill_md" ]; then
        continue
    fi

    # Extract name and description from YAML frontmatter
    in_frontmatter=0
    name=""
    description=""

    while IFS= read -r line; do
        if [[ "$line" == "---" ]]; then
            if [ $in_frontmatter -eq 0 ]; then
                in_frontmatter=1
            else
                break
            fi
            continue
        fi

        if [ $in_frontmatter -eq 1 ]; then
            if [[ "$line" =~ ^name:\ * ]]; then
                name=$(echo "$line" | sed 's/^name: *//')
                name=$(strip_quotes "$name")
            elif [[ "$line" =~ ^description:\ * ]]; then
                description=$(echo "$line" | sed 's/^description: *//')
                description=$(strip_quotes "$description")
            fi
        fi
    done < "$skill_md"

    # Store the data
    if [ -z "$name" ]; then
        name="$skill_name"
    fi
    if [ -z "$description" ]; then
        description="No description available"
    fi

    names+=("$name")
    descriptions+=("$description")
    locations+=("$skill_dir")
done

# Output based on format
case "$FORMAT" in
    text)
        echo "Available Claude Skills"
        echo "======================="
        echo ""
        for i in "${!names[@]}"; do
            echo "📘 Skill: ${names[$i]}"
            echo "   Description: ${descriptions[$i]}"
            echo "   Location: ${locations[$i]}"
            echo ""
        done
        echo "======================="
        echo "Total skills: ${#names[@]}"
        ;;

    csv)
        echo "Name,Description,Location"
        for i in "${!names[@]}"; do
            # Escape quotes and commas in CSV
            name_csv="${names[$i]//\"/\"\"}"
            desc_csv="${descriptions[$i]//\"/\"\"}"
            loc_csv="${locations[$i]//\"/\"\"}"
            echo "\"$name_csv\",\"$desc_csv\",\"$loc_csv\""
        done
        ;;

    json)
        echo "{"
        echo "  \"skills\": ["
        for i in "${!names[@]}"; do
            # Escape quotes and backslashes for JSON
            name_json="${names[$i]//\\/\\\\}"
            name_json="${name_json//\"/\\\"}"
            desc_json="${descriptions[$i]//\\/\\\\}"
            desc_json="${desc_json//\"/\\\"}"
            loc_json="${locations[$i]//\\/\\\\}"
            loc_json="${loc_json//\"/\\\"}"

            echo "    {"
            echo "      \"name\": \"$name_json\","
            echo "      \"description\": \"$desc_json\","
            echo "      \"location\": \"$loc_json\""
            if [ $i -eq $((${#names[@]} - 1)) ]; then
                echo "    }"
            else
                echo "    },"
            fi
        done
        echo "  ],"
        echo "  \"total\": ${#names[@]}"
        echo "}"
        ;;

    markdown|md)
        echo "# Available Claude Skills"
        echo ""
        echo "| Skill Name | Description | Location |"
        echo "|------------|-------------|----------|"
        for i in "${!names[@]}"; do
            # Escape pipe characters in markdown
            name_md="${names[$i]//|/\\|}"
            desc_md="${descriptions[$i]//|/\\|}"
            loc_md="${locations[$i]//|/\\|}"
            echo "| **$name_md** | $desc_md | \`$loc_md\` |"
        done
        echo ""
        echo "**Total skills:** ${#names[@]}"
        ;;

    *)
        echo "Error: Unknown format '$FORMAT'" >&2
        echo "Usage: $0 [text|csv|json|markdown]" >&2
        exit 1
        ;;
esac
