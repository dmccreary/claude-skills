---
title: MkDocs GitHub Pages Deployment Workflow
description: Interactive Mermaid visualization showing mkdocs github pages deployment workflow
image: /sims/mkdocs-github-pages-deployment/mkdocs-github-pages-deployment.png
og:image: /sims/mkdocs-github-pages-deployment/mkdocs-github-pages-deployment.png
quality_score: 100
---


# MkDocs GitHub Pages Deployment Workflow


<iframe src="main.html" width="100%" height="600px"></iframe>


**Copy this iframe to your website:**

```html
<iframe src="https://dmccreary.github.io/ibook-skills/sims/mkdocs-github-pages-deployment/main.html" width="100%" height="600px"></iframe>
```


[Run MkDocs GitHub Pages Deployment Workflow in Fullscreen](main.html){ .md-button .md-button--primary }


This interactive diagram shows the complete workflow from local markdown editing to a published GitHub Pages site.

## Workflow Overview

The deployment process spans three distinct swimlanes:

1. **💻 Local Development** - Where content is created and verified
2. **🔧 Git/GitHub** - Version control and deployment automation
3. **🌐 GitHub Pages Service** - Automated hosting and CDN distribution

## Interactive Diagram



## Workflow Steps

### Local Development (Steps 1-5)

1. **Edit Markdown Files** - Author writes content in `/docs` folder using text editor or IDE
2. **mkdocs serve** - Launch local development server on `http://localhost:8000` to preview changes
3. **mkdocs build** - Generate static site in `/site` directory to verify build succeeds
4. **Build Successful?** - Check for errors in markdown parsing, missing files, or broken links
   - If No → Return to editing and fix errors
   - If Yes → Proceed to commit
5. **git add & commit** - Stage markdown source files and commit with descriptive message

### Git/GitHub Operations (Steps 6-8)

6. **git push origin main** - Upload source commits to GitHub repository main branch
7. **mkdocs gh-deploy** - Build site and force-push to gh-pages branch automatically
   - **Note:** `gh-deploy` handles both building and pushing to gh-pages in one command
8. **GitHub receives gh-pages push** - GitHub detects new commits to gh-pages branch

### GitHub Pages Service (Steps 9-11)

9. **GitHub Pages Build** - GitHub copies files from gh-pages branch to CDN hosting infrastructure
10. **Deploy to CDN** - Site deployed to global CDN with HTTPS enabled
11. **Site Live** - Documentation accessible worldwide at `username.github.io/repo-name/`
    - **Typical deployment time:** 1-2 minutes
    - Custom domain names are supported

## Key Concepts

### Swimlane Architecture

The diagram uses three swimlanes to show separation of concerns:
- **Local Development:** Developer's machine where content is created
- **Git/GitHub:** Version control and automation layer
- **GitHub Pages:** Managed hosting service

### Validation Loop

The workflow includes a critical validation step:
- Build errors (step 4) send you back to editing (step 1)
- This prevents deploying broken sites
- Fix errors locally before pushing to GitHub

### Continuous Development Cycle

After deployment completes:
- The dotted arrow shows the cycle continues
- Developers return to editing for the next update
- The process repeats for each change

### Dual Branch Strategy

MkDocs GitHub Pages uses two branches:
- **`main` branch:** Stores source markdown files, mkdocs.yml, theme customizations
- **`gh-pages` branch:** Stores built static HTML/CSS/JS files (auto-generated)

The `mkdocs gh-deploy` command automates:
1. Building the site locally
2. Force-pushing to the gh-pages branch
3. GitHub Pages detects the update and rebuilds

### Automation Benefits

Using `mkdocs gh-deploy` instead of manual deployment:
- ✓ One command handles build + deploy
- ✓ No need to manually switch branches
- ✓ Automatic timestamp and commit messages
- ✓ Built-in error checking
- ✓ Consistent deployment process

## Color Coding

- **Green:** Start and successful completion states
- **Blue:** Build and verification steps
- **Orange:** Git operations (add, commit, push)
- **Purple:** GitHub automated processes
- **Yellow:** Decision points requiring human input

## Common Issues and Solutions

### Build Fails Locally (Step 4)

**Symptoms:** `mkdocs build` reports errors

**Common causes:**
- Broken links in markdown
- Missing images or files
- Invalid YAML in mkdocs.yml
- Plugin errors

**Solution:** Read error messages carefully, fix issues, retry build

### Push to gh-pages Fails

**Symptoms:** `mkdocs gh-deploy` errors

**Common causes:**
- No write permission to repository
- Network connectivity issues
- Large files exceeding GitHub limits

**Solution:** Check repository permissions, verify network connection

### Site Not Updating After Deployment

**Symptoms:** Changes don't appear on live site

**Common causes:**
- Browser cache showing old version
- GitHub Pages build still in progress
- Deployment to wrong repository

**Solutions:**
- Hard refresh browser (Ctrl+Shift+R or Cmd+Shift+R)
- Wait 1-2 minutes for GitHub Pages build
- Verify repository settings → Pages → Source is gh-pages branch

## Best Practices

1. **Always test locally first** - Use `mkdocs serve` before committing
2. **Run `mkdocs build` before deploying** - Catch errors early
3. **Use descriptive commit messages** - Helps track content changes
4. **Deploy main branch separately** - Push source code before running gh-deploy
5. **Monitor deployment time** - Typical deployment takes 1-2 minutes
6. **Keep .gitignore updated** - Don't commit the `/site` directory

## Related Workflows

- **Git Workflow for Skill Development** - Version control best practices
- **MkDocs Build Process Workflow** - Detailed build pipeline
- **Terminal Workflow for Textbook Development** - Multi-terminal development setup

## Technical Details

- **Diagram Type:** Mermaid flowchart with swimlanes (subgraphs)
- **Visualization Library:** Mermaid 10.x
- **Font Size:** 16px (classroom-readable)
- **Responsive:** Adapts to container width
- **Accessibility:** WCAG AA compliant color contrast

## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Understand** (Understand) the complete deployment workflow for MkDocs sites on GitHub Pages
- **Apply** (Apply) GitHub Actions for automated documentation deployment
- **Analyze** (Analyze) the differences between local builds and CI/CD deployments
- **Evaluate** (Evaluate) deployment configurations for correctness and security
- **Create** (Create) automated deployment pipelines for documentation sites

### Target Audience

- **Primary**: Web developers, documentation engineers, DevOps practitioners
- **Secondary**: Technical writers, open source maintainers
- **Level**: Intermediate to advanced (requires Git and CI/CD familiarity)
- **Prerequisites**: Basic Git, GitHub, command line, and YAML syntax

### Activities

**Activity 1: Workflow Stage Mapping (15 minutes)**

1. Identify all decision points in the deployment workflow (commit to main?, build successful?)
2. Trace the path from "Push to main branch" through to "Site live on GitHub Pages"
3. List what happens during the "Install Dependencies" stage
4. Explain why "Deploy to gh-pages branch" happens after build verification

**Activity 2: Failure Scenario Analysis (25 minutes)**

1. What happens if the MkDocs build fails? (Trace the "No" path from "Build Successful?")
2. Identify 3 common causes of build failures (missing files, invalid YAML, broken links)
3. For each failure cause, describe how you would debug using GitHub Actions logs
4. Discuss: Why is it better to fail at the build stage than after deployment?

**Activity 3: Implement Your Own Deployment (60 minutes)**

1. Fork a sample MkDocs repository or use your own documentation project
2. Create a `.github/workflows/deploy.yml` file following the workflow diagram
3. Configure GitHub Pages settings to use the gh-pages branch
4. Make a test commit and verify automated deployment works
5. Check that your site is live at `https://username.github.io/repo-name`

**Activity 4: Deployment Optimization (30 minutes)**

1. Add build caching to speed up dependency installation
2. Implement branch protection rules to prevent failed builds from deploying
3. Add deployment status badges to your README.md
4. Configure custom domain (if available) or document the process

### Assessment

**Formative Assessment:**
- During Activity 1: Can students correctly trace workflow paths?
- During Activity 3: Does the deployment pipeline execute successfully?

**Summative Assessment:**

Implement a complete documentation deployment system:

1. **Workflow Implementation** (35 points): Functional GitHub Actions workflow
2. **Build Configuration** (25 points): Correct MkDocs configuration and dependencies
3. **Deployment Verification** (20 points): Site successfully deploys and is accessible
4. **Documentation** (20 points): README with deployment instructions and troubleshooting

**Success Criteria:**
- Automated deployment triggers on commits to main branch
- Build failures are caught before deployment
- Site updates appear within 2-3 minutes of commits
- Deployment process is documented for team members


## References

- [MkDocs Documentation](https://www.mkdocs.org/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [mkdocs gh-deploy command](https://www.mkdocs.org/user-guide/deploying-your-docs/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)


## Overview

This MicroSim uses Mermaid to provide an interactive visualization.