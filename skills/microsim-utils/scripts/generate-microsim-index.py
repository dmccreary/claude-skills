# generate MicroSim index page and TODO list for missing screenshots
# This script scans the docs/sims directory for MicroSim subdirectories,
# extracts metadata from their index.md files, and generates an index.md listing 
# all the MicroSims with their titles, descriptions, and screenshots. 
# It also creates a TODO.md file listing any MicroSims that are missing screenshots.
import os
import re

base_dir = "docs/sims"
sims = []
missing_screenshots = []

# ensure TODO directory ignored
for item in os.listdir(base_dir):
    sim_dir = os.path.join(base_dir, item)
    if not os.path.isdir(sim_dir) or item == "TODO":
        continue
        
    index_file = os.path.join(sim_dir, "index.md")
    if not os.path.exists(index_file):
        continue
        
    with open(index_file, 'r') as f:
        content = f.read()
        
    # parse frontmatter
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # get title
        title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else item
        
        # get description
        desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
        description = desc_match.group(1).strip() if desc_match else f"Interactive MicroSim for {title.lower()}."
        
        # rewrite frontmatter if description missing
        if not desc_match:
            new_frontmatter = frontmatter.rstrip() + f"\ndescription: {description}\n"
            new_content = parts[0] + "---" + new_frontmatter + "---" + parts[2]
            with open(index_file, 'w') as f:
                f.write(new_content)
                
        sims.append({
            "name": item,
            "title": title,
            "description": description
        })
        
        # check screenshot
        screenshot_file = os.path.join(sim_dir, f"{item}.png")
        if not os.path.exists(screenshot_file):
            missing_screenshots.append(item)

# Sort by title
sims.sort(key=lambda x: x["title"].lower())

# Generate index.md
index_content = """---
title: List of MicroSims for Theory of Knowledge
description: A list of all the MicroSims used in the Theory of Knowledge course
image: /sims/index-screen-image.png
og:image: /sims/index-screen-image.png
hide:
    toc
---

# List of MicroSims for Theory of Knowledge

Interactive Micro Simulations to help students learn Theory of Knowledge fundamentals.

<div class="grid cards" markdown>

"""

for sim in sims:
    index_content += f"""-   **[{sim['title']}](./{sim['name']}/index.md)**\n\n"""
    index_content += f"""    ![{sim['title']}](./{sim['name']}/{sim['name']}.png)\n\n"""
    index_content += f"""    {sim['description']}\n\n"""

index_content += "</div>\n"

with open(os.path.join(base_dir, "index.md"), 'w') as f:
    f.write(index_content)

# write TODO.md
todo_path = os.path.join(base_dir, "TODO.md")
if missing_screenshots:
    todo_content = "# MicroSim Screenshot TODO\n\nThis file tracks MicroSims that need screenshots captured.\n\n## Missing Screenshots\n\nRun the following commands to capture missing screenshots:\n\n"
    for item in missing_screenshots:
        todo_content += f"### {item}\n```bash\n~/.local/bin/bk-capture-screenshot docs/sims/{item}\n```\n\n"
    with open(todo_path, 'w') as f:
        f.write(todo_content)

print(f"Processed {len(sims)} MicroSims.")
print(f"Missing screenshots logged: {len(missing_screenshots)}")
