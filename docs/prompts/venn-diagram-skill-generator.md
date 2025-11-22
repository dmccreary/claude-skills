# Venn Diagram Skill 

!!! prompt
    Use the skill-generator skill to create a new skill called `venn-diagram-generator`.  This skill 
    will use the venn.js javascript library to create a new diagram.  The github repo for venn.js is 
    here: https://github.com/benfred/venn.js/.  The output of this skill will be the creation of a new 
    directory in the /docs/sims directory.  Each drawing must have a title as well as a directory name 
    in lowercase with dashes.  Use the existing microseism as templates.  Make sure you create an index.md
    file, a main.html, a script.js and if needed, a style.css file.  The drawing should be referenced by
    placing an <iframe> HTML element at the top of the index.md file.  If the user does not provide a 
    title, ask them for a title.  Place the new skill in /skills/venn-diagram-generator. 


## Results


Claude Code v2.0.35
Sonnet 4.5 · Claude Pro

⏺ I'll help you create the venn-diagram-generator skill using the skill-creator skill. Let me invoke
   it now.

> The "skill-creator" skill is running 

⏺ I'll create the venn-diagram-generator skill following the skill creation process. Let me start by
   setting up a todo list to track the work.

⏺ Now let me understand the requirements better by examining an existing microsim to use as a
  template.

⏺ Search(pattern: "**/microsim-p5/assets/template/**")
  ⎿  Found 0 files 

⏺ Bash(find $HOME/Documents/ws/claude-skills/docs/sims -type d -maxdepth 1)
  ⎿  find: $HOME/Documents/ws/claude-skills/docs/sims: No such file or directory

⏺ Read(skills/microsim-p5/SKILL.md)
  ⎿  Read 667 lines

⏺ Read(skills/mermaid-generator/assets/template/index.md)
  ⎿  Read 42 lines

⏺ Read(skills/mermaid-generator/SKILL.md)
  ⎿  Read 517 lines

⏺ Now let me also check the mermaid-generator's template files to understand the structure better:

⏺ Bash(find $HOME/Documents/ws/claude-skills/skills/mermaid-generator -type f -name "*.html" -o
      -name "*.css" -o -name "*.js" -o -name "*.json" | head -10)
  ⎿  $HOME/Documents/ws/claude-skills/skills/mermaid-generator/assets/template/metadata.json
     $HOME/Documents/ws/claude-skills/skills/mermaid-generator/assets/template/script.js
     $HOME/Documents/ws/claude-skills/skills/mermaid-generator/assets/template/main.html
     $HOME/Documents/ws/claude-skills/skills/mermaid-generator/assets/template/style.css

⏺ Read(skills/mermaid-generator/assets/template/main.html)
  ⎿  Read 47 lines

⏺ Read(skills/mermaid-generator/assets/template/metadata.json)
  ⎿  Read 23 lines

⏺ Now let me check where the init_skill.py script is located:

⏺ Search(pattern: "**/init_skill.py")
  ⎿  Found 0 files 

⏺ Bash(ls -la $HOME/Documents/ws/claude-skills/scripts/)
  ⎿  total 56                                       
     drwxr-xr-x   7 dan  staff   224 Nov  3 10:14 .
     drwxr-xr-x@ 21 dan  staff   672 Nov  6 21:27 ..
     … +5 lines (ctrl+o to expand)

⏺ The init_skill.py script isn't available in this repository, so I'll manually create the skill
  directory structure. Let me create the venn-diagram-generator skill directory:

⏺ Bash(mkdir -p $HOME/Documents/ws/claude-skills/skills/venn-diagram-generator/assets/template &&
      mkdir -p $HOME/Documents/ws/claude-skills/skills/venn-diagr…)
  ⎿  (No content)

⏺ Now let me research the venn.js library from its GitHub repository:

⏺ Fetch(`https://github.com/benfred/venn.js/`)
  ⎿  Received 339.6KB (200 OK)

⏺ Web Search("venn.js CDN jsdelivr unpkg 2024 2025")
  ⎿  Did 1 search in 17s                                                                           

⏺ Fetch(`https://cdnjs.com/libraries/venn.js/0.2.14`)
  ⎿  Received 91.1KB (200 OK)

⏺ Now let me create the template files for the venn-diagram-generator skill. First, let me create
  the main.html template:

⏺ Write(skills/venn-diagram-generator/assets/template/main.html)
  ⎿  Wrote 40 lines to skills/venn-diagram-generator/assets/template/main.html            
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>{{TITLE}}</title>
         <link rel="stylesheet" href="style.css">
         <!-- D3.js v7 - Required dependency for venn.js -->
         <script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
         <!-- venn.js library -->
     … +30 lines (ctrl+o to expand)

⏺ Write(skills/venn-diagram-generator/assets/template/style.css)
  ⎿  Wrote 191 lines to skills/venn-diagram-generator/assets/template/style.css
     /* Venn Diagram MicroSim Stylesheet */
     * {
         box-sizing: border-box;
         margin: 0;
         padding: 0;
     }
     body {
         font-family: Arial, Helvetica, sans-serif;
     … +181 lines (ctrl+o to expand)

⏺ Write(skills/venn-diagram-generator/assets/template/script.js)
  ⎿  Wrote 101 lines to skills/venn-diagram-generator/assets/template/script.js
     // Venn Diagram Configuration and Rendering
     // This script is populated with data specific to each diagram
     // Venn diagram data - Replace {{VENN_DATA}} with actual sets data
     var sets = {{VENN_DATA}};
     // Color configuration - Replace {{COLOR_SCHEME}} with actual colors
     var colorScheme = {{COLOR_SCHEME}};
     // Initialize the Venn diagram
     … +91 lines (ctrl+o to expand)

⏺ Write(skills/venn-diagram-generator/assets/template/index.md)
  ⎿  Wrote 49 lines to skills/venn-diagram-generator/assets/template/index.md
     ---
     title: {{TITLE}}
     description: {{META_DESCRIPTION}}
     ---
     # {{TITLE}}
     ## Overview
     {{OVERVIEW}}
     … +39 lines (ctrl+o to expand)

⏺ Write(skills/venn-diagram-generator/assets/template/metadata.json)
  ⎿  Wrote 24 lines to skills/venn-diagram-generator/assets/template/metadata.json
     {
       "title": "{{TITLE}}",
       "description": "{{DESCRIPTION}}",
       "subject": "{{SUBJECT}}",
       "creator": "Claude AI with Venn Diagram Generator Skill",
       "date": "{{DATE}}",
       "type": "Interactive Venn Diagram",
       "format": "text/html",
       "language": "en-US",
       "coverage": "{{COVERAGE}}",
     … +14 lines (ctrl+o to expand)

⏺ Write(skills/venn-diagram-generator/references/venn-js-reference.md)
  ⎿  Wrote 398 lines to skills/venn-diagram-generator/references/venn-js-reference.md              
     # venn.js Reference Guide
     ## Overview
     venn.js is a JavaScript library for laying out area-proportional Venn and Euler diagrams. It
     uses D3.js for rendering SVG visualizations.
     ## Dependencies
     - **D3.js v7+** - Required for DOM manipulation and SVG rendering
     - CDN: `https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js`
     … +388 lines (ctrl+o to expand)

⏺ Now let me create the main SKILL.md file:

⏺ Write(skills/venn-diagram-generator/SKILL.md)
  ⎿  Wrote 612 lines to skills/venn-diagram-generator/SKILL.md                                     
     ---
     name: venn-diagram-generator
     description: This skill generates interactive Venn diagram visualizations using the venn.js
     JavaScript library. Use this skill when users request creating Venn diagrams, set
     visualizations, overlap diagrams, or comparison charts for educational textbooks. The skill
     creates complete MicroSim packages with standalone HTML files featuring colorful circles, clear
      labels, and interactive tooltips, saved to /docs/sims/ following the MicroSim pattern.
     ---
     # Venn Diagram Generator
     ## Overview
     Generate interactive Venn diagram visualizations using venn.js and D3.js for intelligent
     textbooks. Creates complete MicroSim packages with standalone HTML files, MkDocs integration,
     and Dublin Core metadata. Each diagram features customizable colors, interactive tooltips, and
     follows the educational MicroSim pattern for seamless integration into educational content.
     … +602 lines (ctrl+o to expand)

⏺ Let me check if there's a packaging script available:

⏺ Search(pattern: "**/package_skill.py")
  ⎿  Found 0 files 

⏺ Since there's no packaging script, let me create the zip file manually:

⏺ Bash(cd $HOME/Documents/ws/claude-skills/skills && zip -r venn-diagram-generator.zip
      venn-diagram-generator/)
  ⎿    adding: venn-diagram-generator/ (stored 0%)                                  
       adding: venn-diagram-generator/references/ (stored 0%)
       adding: venn-diagram-generator/references/venn-js-reference.md (deflated 64%)
     … +8 lines (ctrl+o to expand)

⏺ Bash(mv $HOME/Documents/ws/claude-skills/skills/venn-diagram-generator.zip
      $HOME/Documents/ws/claude-skills/)
  ⎿  (No content)

⏺ Perfect! I've successfully created the venn-diagram-generator skill. Here's what was created:

  Skill Created: venn-diagram-generator

  Location: $HOME/Documents/ws/claude-skills/skills/venn-diagram-generator/

  Package: venn-diagram-generator.zip (in project root)

  Files Generated

  Core Skill File

  - SKILL.md - Complete skill definition with:
    - Comprehensive workflow (7 steps)
    - When to use this skill
    - Best practices for educational Venn diagrams
    - Common patterns (2, 3, and 4-circle diagrams)
    - Troubleshooting guide
    - 3 detailed examples

  Template Assets (assets/template/)

  - main.html - Standalone HTML with venn.js (0.2.20) and D3.js (7.9.0) from CDN
  - style.css - Responsive stylesheet with tooltips, 16px fonts, print-friendly styles
  - script.js - Interactive venn.js initialization with hover effects and tooltips
  - index.md - MkDocs integration template with iframe embed
  - metadata.json - Dublin Core metadata template

  Reference Documentation (references/)

  - venn-js-reference.md - Comprehensive guide covering:
    - venn.js data format and API
    - 2, 3, and 4+ circle diagram examples
    - Color schemes for education
    - Styling and interactivity patterns
    - Troubleshooting common issues
    - Best practices

  Key Features

  The skill will:
  1. Ask for a title if not provided by the user
  2. Generate interactive Venn diagrams with 2-4 circles
  3. Create complete MicroSim packages in /docs/sims/[diagram-name]/
  4. Include customizable color schemes
  5. Provide interactive tooltips on hover
  6. Ensure responsive design for mobile and desktop
  7. Use educational-friendly 16px fonts for readability
  8. Follow the MicroSim pattern from your existing skills

  Technology Stack:
  - venn.js 0.2.20 - Venn diagram layout engine
  - D3.js 7.9.0 - SVG rendering and interactivity
  - CDN-hosted libraries (no installation needed)

  Installation

  To use this skill globally:

  # Create symlink to make skill available system-wide
  ln -s $HOME/Documents/ws/claude-skills/skills/venn-diagram-generator
  ~/.claude/skills/venn-diagram-generator

  Or for project-specific use, the skill is ready to use from the current location.

  Example Usage

  When users request:
  - "Create a Venn diagram comparing Python, JavaScript, and Java"
  - "Make a 2-circle Venn diagram showing cats and dogs"
  - "Generate a diagram showing the overlap between AI, ML, and Data Science"

  The skill will generate a complete MicroSim with all necessary files following your established
  patterns.

  Next Steps

  1. Test the skill by invoking it with a sample request
  2. Review the generated SKILL.md for any adjustments
  3. Consider adding the skill to your documentation
  4. Update .gitignore if the zip file shouldn't be committed

  The skill follows the same structure and conventions as your mermaid-generator and microsim-p5
  skills, ensuring consistency across your skill collection.



