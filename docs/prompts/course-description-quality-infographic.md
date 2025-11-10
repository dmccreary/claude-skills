# Generate Course Description Quality Workflow Infographic
Claude Code v2.0.36
Sonnet 4.5 · Claude Pro

> use the infographic-generator-p5 to create a new infographic from the following 
description: <summary>Course Description Quality Impact on Workflow</summary>
    Type: workflow

    Purpose: Show how course description quality affects subsequent skill outputs

    Visual style: Flowchart with quality branching

    Steps:
    1. Start: "Course Description Created"

    2. Decision: "Quality Score ≥ 70?"
       Hover text: "Assessed using course-description-analyzer skill"

    3a. High Quality Path (Score ≥ 70):
        - Process: "Learning graph generation"
          Hover text: "200 relevant concepts with accurate dependencies"
        - Process: "Glossary generation"
          Hover text: "Precise definitions aligned with concepts"
        - Process: "Chapter structure"
          Hover text: "Logical sequencing respecting prerequisites"
        - Result: "High-quality textbook with minimal manual correction"

    3b. Low Quality Path (Score < 70):
        - Process: "Learning graph generation"
          Hover text: "Generic or off-target concepts, unclear dependencies"
        - Process: "Manual correction required"
          Hover text: "Significant effort to refine concepts and relationships"
        - Process: "Regenerate downstream artifacts"
          Hover text: "Glossary, chapters must be redone with corrected graph"
        - Result: "Extended development time, inconsistent quality"

    Annotations:
    - "Investing time in course description quality pays exponential dividends"
    - "Quality threshold: 70+ for acceptable, 85+ for excellent"

    Color coding:
    - Green: High-quality path
    - Orange: Low-quality path requiring rework
    - Blue: Assessment and decision points 
  ⎿ ⧉ Selected 39 lines from docs/chapters/03-course-design-educational-theory/index.md in 
    Visual Studio Code

⏺ I'll use the infographic-generator-p5 skill to create this workflow diagram showing how
   course description quality impacts the entire textbook development process.
  ⎿  Error: Unknown skill: infographic-generator-p5

⏺ Let me check if the skill exists in the directory:

⏺ Read(skills/infographic-generator-p5/SKILL.md)
  ⎿  Error reading file

⏺ Bash(ls -la skills/infographic-generator-p5/)
  ⎿  total 0                                                           
     drwxr-xr-x   3 dan  staff   96 Nov  9 12:45 .
     drwxr-xr-x  22 dan  staff  704 Nov  9 12:53 ..
     drwxr-xr-x   5 dan  staff  160 Nov  9 12:56 infograph-generator-p5

⏺ Bash(find skills/infographic-generator-p5/ -type f)
  ⎿ skills/infographic-generator-p5/infograph-generator-p5/references/vis-network-parame
    ters.md
    skills/infographic-generator-p5/infograph-generator-p5/SKILL.md
    … +4 lines (ctrl+o to expand)


⏺ Let me read the skill definition:

⏺ Read(skills/infographic-generator-p5/infograph-generator-p5/SKILL.md)
  ⎿  Read 582 lines

⏺ I found the infographic-generator-p5 skill! This will create a p5.js-based interactive
  flowchart showing how course description quality impacts the textbook development
  workflow. Let me create this for you.

⏺ Now I'll create the infographic. First, let me plan the node structure:

  - Start node (gray): "Course Description Created"
  - Decision node (blue, diamond): "Quality Score ≥ 70?"
  - High Quality Path (green): Learning graph → Glossary → Chapter structure →
  High-quality textbook
  - Low Quality Path (orange): Learning graph → Manual correction → Regenerate artifacts
  → Extended development time

⏺ Bash(mkdir -p docs/sims/course-quality-workflow)
  ⎿  (No content)

⏺ Write(docs/sims/course-quality-workflow/data.json)
  ⎿  Wrote 201 lines to docs/sims/course-quality-workflow/data.json                     
     {
       "metadata": {
         "title": "Course Description Quality Impact on Workflow",
         "description": "An interactive infographic showing how course description 
     quality affects subsequent skill outputs in the intelligent textbook generation 
     process",
         "author": "Claude Skills",
         "created": "2025-01-09"
       },
       "groups": {
         "start": {
           "color": "#9CA3AF",
     … +191 lines (ctrl+o to expand)

⏺ Write(docs/sims/course-quality-workflow/course-quality-workflow.js)
  ⎿  Wrote 348 lines to docs/sims/course-quality-workflow/course-quality-workflow.js    
     // Course Description Quality Impact on Workflow Infographic
     // Interactive p5.js visualization showing how quality affects the textbook 
     generation workflow
     // Canvas dimensions
     let canvasWidth = 800;
     let drawHeight = 680;
     let controlHeight = 140;
     let canvasHeight = drawHeight + controlHeight;
     let margin = 20;
     let defaultTextSize = 16;
     … +338 lines (ctrl+o to expand)

⏺ Write(docs/sims/course-quality-workflow/main.html)
  ⎿  Wrote 45 lines to docs/sims/course-quality-workflow/main.html                
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Course Description Quality Impact on Workflow</title>
         <script src="https://cdn.jsdelivr.net/npm/p5@1.11.10/lib/p5.js"></script>
         <style>
             body {
                 margin: 0px;
     … +35 lines (ctrl+o to expand)

⏺ Write(docs/sims/course-quality-workflow/index.md)
  ⎿  Wrote 118 lines to docs/sims/course-quality-workflow/index.md                      
     ---
     title: Course Description Quality Impact on Workflow
     description: Interactive infographic showing how course description quality affects
     the intelligent textbook generation workflow
     ---
     # Course Description Quality Impact on Workflow
     <iframe src="main.html" width="100%" height="870px" style="border: 1px solid #ddd; 
     border-radius: 8px;" scrolling="no"></iframe>
     `[View Fullscreen](./main.html){ .md-button .md-button--primary }
     … +108 lines (ctrl+o to expand)

⏺ Read(mkdocs.yml)
  ⎿  Read 175 lines

⏺ Update(mkdocs.yml)
  ⎿  Updated mkdocs.yml with 1 addition                                             
        98        - Concept Length Histogram: sims/concept-length-histogram/index.md
        99        - Claude Code Timeline: sims/claude-code-timeline/index.md
       100        - Skill Impact Chart: sims/skill-impact-chart/index.md
       101 +      - Course Quality Workflow: sims/course-quality-workflow/index.md
       102      
       103      - Prompts:
       104        - List of Prompts: prompts/index.md

⏺ Perfect! I've successfully created the Course Description Quality Impact on Workflow
  infographic using the infographic-generator-p5 skill. Here's what was generated:

  Created Files

  All files are in /docs/sims/course-quality-workflow/:

  1. data.json - Node and edge data with 10 nodes representing the workflow:
    - 1 start node (Course Description Created)
    - 1 decision node (Quality Score ≥ 70?)
    - 3 high-quality path nodes (green)
    - 3 low-quality path nodes (orange)
    - 2 result nodes (outcomes)
  2. course-quality-workflow.js - Interactive p5.js visualization with:
    - Hover tooltips for quick descriptions
    - Detail panel showing full descriptions
    - Color-coded paths (green for high-quality, orange for low-quality)
    - Arrows showing workflow direction
    - Annotations highlighting key insights
  3. main.html - Standalone HTML page with p5.js CDN integration
  4. index.md - Comprehensive documentation including:
    - Embedded iframe of the infographic
    - Usage instructions
    - Detailed explanation of both workflow paths
    - Quality threshold information
    - Legend for colors and shapes

  Updated

  - mkdocs.yml - Added navigation entry under MicroSims section (line 101)

  Visual Design

  The infographic features:
  - Blue diamond for the decision point (Quality Score ≥ 70?)
  - Green path showing smooth workflow with quality score ≥ 70
  - Orange path showing problematic workflow with score < 70
  - Interactive hover - see detailed descriptions for each step
  - Annotations - "Quality threshold: 70+ acceptable, 85+ excellent"

  Next Steps

  To view the infographic locally:

  mkdocs serve

  Then navigate to the MicroSims section → Course Quality Workflow

  The infographic clearly demonstrates your key insight: investing time in course 
  description quality pays exponential dividends throughout the entire textbook
  generation process!




