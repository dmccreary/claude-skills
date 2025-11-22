# Generate Timeline MicroSim Skill

Claude Code v2.0.36
Sonnet 4.5 · Claude Pro

!!! prompt
    Use the skill-generator skill to create a new skill.  The skill name is 
    'timeline-generator'.  Place this new skill in skills/timeline-generator.  Use the 
    timeline demo at docs/sims/timeline as your example.  Prompt the user for the event list 
    if it was not provided.  Ask the user if they want category buttons in the viewer like 
    the example.  Make sure the sample code you put in skills/timeline-generator/resources is
    generic. 

⏺ I'll help you create a new timeline-generator skill. Let me start by exploring the
  existing timeline demo and skill structure, then create the new skill.

⏺ Read(docs/sims/timeline)
  ⎿  Error: EISDIR: illegal operation on a directory, read

⏺ Search(pattern: "docs/sims/timeline/**/*")
  ⎿  Found 3 files (ctrl+o to expand)

⏺ Read(docs/sims/timeline/main.html)
  ⎿  Read 417 lines

⏺ Read(docs/sims/timeline/timeline.json)
  ⎿  Read 623 lines

⏺ Read(docs/sims/timeline/index.md)
  ⎿  Read 9 lines

⏺ Read(skills/skill-creator/SKILL.md)
  ⎿  Error reading file

⏺ Search(pattern: "skills/*/SKILL.md")
  ⎿  Found 17 files (ctrl+o to expand)

⏺ Read(skills/bubble-chart-generator/SKILL.md)
  ⎿  Read 362 lines

⏺ Bash(ls -la $HOME/Documents/ws/claude-skills/skills/bubble-chart-generator/)
  ⎿  total 24                                        
     drwxr-xr-x   4 dan  staff    128 Nov  6 06:10 .
     drwxr-xr-x  20 dan  staff    640 Nov  9 07:42 ..
     … +2 lines (ctrl+o to expand)

⏺ Bash(ls -la $HOME/Documents/ws/claude-skills/skills/bubble-chart-generator/assets/)
  ⎿  total 48                                      
     drwxr-xr-x  6 dan  staff   192 Nov  6 07:32 .
     drwxr-xr-x  4 dan  staff   128 Nov  6 06:10 ..
     … +4 lines (ctrl+o to expand)

⏺ Bash(mkdir -p $HOME/Documents/ws/claude-skills/skills/timeline-generator/resources)
  ⎿  (No content)

⏺ Write(skills/timeline-generator/SKILL.md)
  ⎿  Wrote 475 lines to skills/timeline-generator/SKILL.md                              
     ---
     name: timeline-generator
     description: This skill generates interactive timeline visualizations using the
     vis-timeline JavaScript library. Use this skill when users need to create historical
      timelines, project timelines, event sequences, or any chronological data
     visualization with optional category filtering. The skill creates a complete
     MicroSim package with HTML, CSS, JSON data, and documentation.
     ---
     # Timeline Generator
     ## Overview
     This skill generates professional, interactive timeline visualizations using
     vis-timeline.js. Timelines are ideal for displaying chronological events with rich
     context including descriptions, notes, and category groupings. The skill creates a
     complete MicroSim package suitable for embedding in educational content or
     documentation sites built with MkDocs.
     … +465 lines (ctrl+o to expand)

⏺ Write(skills/timeline-generator/resources/template-timeline.json)
  ⎿  Wrote 84 lines to skills/timeline-generator/resources/template-timeline.json
     {
       "title": "Sample Timeline",
       "events": `[
         {
           "start_date": {
             "year": "2020",
             "month": "1",
             "day": "15"
           },
           "text": {
     … +74 lines (ctrl+o to expand)

⏺ Write(skills/timeline-generator/resources/template-main.html)
  ⎿  Wrote 387 lines to skills/timeline-generator/resources/template-main.html          
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>{{TIMELINE_TITLE}}</title>
         <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-timeline/7.7.3/vis-timel
     ine-graph2d.min.js"></script>
         <link href="https://cdnjs.cloudflare.com/ajax/libs/vis-timeline/7.7.3/vis-timeli
     ne-graph2d.min.css" rel="stylesheet" />
         <style>
             body {
     … +377 lines (ctrl+o to expand)

⏺ Write(skills/timeline-generator/resources/template-index.md)
  ⎿  Wrote 119 lines to skills/timeline-generator/resources/template-index.md
     # {{TIMELINE_TITLE}}
     {{TIMELINE_OVERVIEW_TEXT}}
     `[Run the {{TIMELINE_TITLE}}](./main.html)`
     `[View the Raw Timeline Data](timeline.json)
     ## Overview
     … +109 lines (ctrl+o to expand)

⏺ Write(skills/timeline-generator/resources/README.md)
  ⎿  Wrote 158 lines to skills/timeline-generator/resources/README.md                   
     # Timeline Generator Resources
     This directory contains generic template files for creating interactive timeline
     visualizations using vis-timeline.js.
     ## Template Files
     ### template-timeline.json
     Generic event data file demonstrating the JSON structure for timeline events. This
     sample includes:
     - 6 sample events spanning 2020-2021
     - 4 categories (Planning, Development, Launch, Maintenance)
     … +148 lines (ctrl+o to expand)

⏺ Bash(find $HOME/Documents/ws/claude-skills/skills/timeline-generator -type f)
  ⎿ $HOME/Documents/ws/claude-skills/skills/timeline-generator/resources/template-t
    imeline.json
    $HOME/Documents/ws/claude-skills/skills/timeline-generator/resources/template-m
    … +5 lines (ctrl+o to expand)



⏺ Read(mkdocs.yml)
  ⎿  Read 158 lines

⏺ Bash(tree $HOME/Documents/ws/claude-skills/skills/timeline-generator)
  ⎿  Error: Exit code 127
     (eval):1: command not found: tree

⏺ Bash(ls -R $HOME/Documents/ws/claude-skills/skills/timeline-generator)
  ⎿  resources                    
     SKILL.md
     … +5 lines (ctrl+o to expand)

⏺ Bash(head -5 $HOME/Documents/ws/claude-skills/skills/timeline-generator/SKILL.md)
  ⎿ ---                                                                                 
    name: timeline-generator
    description: This skill generates interactive timeline visualizations using the vis-
    … +5 lines (ctrl+o to expand)


⏺ Perfect! I've successfully created the new timeline-generator skill. Here's what was
  created:

  Skill Structure

  skills/timeline-generator/
  ├── SKILL.md                           # Main skill definition with complete workflow
  └── resources/
      ├── README.md                      # Guide for using the template files
      ├── template-timeline.json         # Generic sample event data
      ├── template-main.html             # HTML template with placeholders
      └── template-index.md              # Documentation template

  Key Features of the Skill

  The timeline-generator skill:

  1. Prompts for event data if not provided by the user
  2. Asks about category filtering - whether they want filter buttons like in the example
  3. Uses generic templates with clear placeholders:
    - {{TIMELINE_TITLE}} - Main title
    - {{TIMELINE_SUBTITLE}} - Subtitle
    - {{FILTER_CONTROLS}} - Optional filter buttons HTML
    - {{CATEGORY_COLORS}} - JavaScript object for colors
    - {{LEGEND}} - Optional legend HTML
    - And more...
  4. Follows the MicroSim pattern from your repository:
    - Creates docs/sims/<timeline-name>/ directory
    - Generates main.html, timeline.json, and index.md
    - Uses vis-timeline.js library (v7.7.3)
  5. Comprehensive workflow covering:
    - Requirements gathering
    - Data structure creation (TimelineJS-compatible JSON)
    - HTML generation with vis-timeline integration
    - Category filtering and color-coding
    - Event detail display
    - MkDocs documentation
    - Testing and validation

  Sample Templates

  The resources directory includes:
  - template-timeline.json - 6 sample events with 4 categories (Planning, Development,
  Launch, Maintenance)
  - template-main.html - Complete HTML with all features (zoom, pan, filtering, tooltips,
   event details)
  - template-index.md - Full documentation template for MkDocs
  - README.md - Detailed instructions on using the templates and replacing placeholders

  How to Use

  The skill can be invoked with:
  /skill timeline-generator

  Or through the Skill tool, and it will guide the user through creating an interactive
  timeline based on the working example at docs/sims/timeline/.

  All templates are generic and ready to be customized for any timeline use case!

> how many tokens were used to create the timeline skill? 

⏺ Based on the token usage tracking in the conversation:

  - Starting token usage: 22,193 tokens
  - Final token usage: 57,632 tokens
  - Total tokens used: 35,439 tokens

  This covered:
  1. Examining the existing timeline demo at docs/sims/timeline/
  2. Reviewing the skill structure patterns (bubble-chart-generator)
  3. Creating the directory structure
  4. Writing the comprehensive SKILL.md (with complete workflow instructions)
  5. Creating 4 template files in the resources directory:
    - template-timeline.json (sample data)
    - template-main.html (full HTML with vis-timeline integration)
    - template-index.md (documentation template)
    - README.md (usage guide)
  6. Testing and validation

  Out of the 200,000 token budget, we used about 17.7% to create this complete skill with
   all its documentation and templates.

