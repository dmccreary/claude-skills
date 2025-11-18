# Terminal Workflow for Textbook Development

**Chapter:** 13 - Dev Tools Version Control Deployment
**Generator:** mermaid-generator
**Match Score:** 95/100
**Difficulty:** Medium

## Specification

<summary>Terminal Workflow for Textbook Development</summary>
    Type: workflow

    Purpose: Illustrate the typical terminal command sequence for developing and deploying textbook content

    Visual style: Flowchart with terminal command boxes and decision points

    Steps:
    1. Start: "Open project in VS Code"
       Hover text: "File → Open Folder, select textbook repository"

    2. Process: "Open integrated terminal (Ctrl+`)"
       Hover text: "Terminal opens in project root directory"

    3. Process: "mkdocs serve"
       Hover text: "Starts development server on localhost:8000"

    4. Decision: "Need to run Python scripts?"
       Hover text: "Learning graph analysis, content generation, etc."

    5a. Process: "Create new terminal (+)"
        Hover text: "Keep mkdocs serve running in first terminal"

    5b. Continue to step 6

    6. Process: "Edit markdown files"
       Hover text: "Changes auto-reload in browser within 1-2 seconds"

    7. Process: "python docs/learning-graph/analyze-graph.py"
       Hover text: "Validate learning graph quality and structure"

    8. Decision: "Quality check passed?"
       Hover text: "Review quality-metrics.md for issues"

    9a. Process: "Fix identified issues"
        Hover text: "Edit learning-graph.csv, re-run analysis"
        Returns to step 6

    9b. Continue to step 10

    10. Process: "git add . && git commit -m 'message'"
        Hover text: "Stage all changes and create commit"

    11. Process: "git push origin main"
        Hover text: "Push commits to GitHub repository"

    12. Process: "mkdocs gh-deploy"
        Hover text: "Build site and deploy to GitHub Pages"

    13. End: "Textbook published"
        Hover text: "Changes live at https://username.github.io/textbook-name"

    Color coding:
    - Blue: Terminal commands
    - Yellow: Decision points
    - Green: Git operations
    - Orange: Deployment steps

    Swimlanes:
    - Terminal 1 (Development Server)
    - Terminal 2 (Script Execution)
    - Terminal 3 (Git Operations)

    Implementation: SVG flowchart with interactive hover states (HTML/CSS/JavaScript)