# Git Workflow for Skill Development

**Chapter:** 09 - Claude Skills Architecture Development
**Generator:** mermaid-generator
**Match Score:** 95/100
**Difficulty:** Medium

## Specification

<summary>Git Workflow for Skill Development</summary>
    Type: workflow

    Purpose: Illustrate the typical Git workflow for developing and publishing a skill

    Visual style: Linear workflow with Git command boxes

    Steps:
    1. Start: "Clone Repository"
       Command: `git clone https://github.com/user/claude-skills`
       Hover text: "Create local copy of repository"

    2. Process: "Create Feature Branch (optional)"
       Command: `git checkout -b new-skill-feature`
       Hover text: "Isolate development work from main branch"

    3. Process: "Develop Skill"
       Activities: "Write SKILL.md, create scripts, test thoroughly"
       Hover text: "Iterative development and testing cycle"

    4. Process: "Check Status"
       Command: `git status`
       Output: "Modified: skills/new-skill/SKILL.md (red)"
       Hover text: "Review what files changed"

    5. Process: "Stage Changes"
       Command: `git add skills/new-skill/`
       Output: "Staged: skills/new-skill/SKILL.md (green)"
       Hover text: "Prepare files for commit"

    6. Process: "Commit Changes"
       Command: `git commit -m "Add new-skill with Python validation"`
       Output: "1 file changed, 245 insertions(+)"
       Hover text: "Create snapshot with descriptive message"

    7. Decision: "Ready to Publish?"
       Hover text: "Has skill been tested? Documentation complete?"

    8a. Process: "Continue Development" (if not ready)
        Loops back to: "Develop Skill"

    8b. Process: "Push to Remote" (if ready)
        Command: `git push origin main`
        Output: "Branch 'main' set up to track 'origin/main'"
        Hover text: "Upload commits to GitHub"

    9. End: "Skill Published"
       Hover text: "Changes available on remote repository"

    Color coding:
    - Blue: Git commands
    - Green: Successful operations
    - Yellow: Decision points
    - Orange: Development activities

    Visual elements:
    - Git logo icon at start
    - GitHub logo icon at end
    - Command terminal icons for Git operations
    - Branch diagram showing feature branch merging to main