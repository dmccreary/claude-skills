# MkDocs GitHub Pages Deployment Workflow

This interactive diagram shows the complete workflow from local markdown editing to a published GitHub Pages site.

## Workflow Overview

The deployment process spans three distinct swimlanes:

1. **💻 Local Development** - Where content is created and verified
2. **🔧 Git/GitHub** - Version control and deployment automation
3. **🌐 GitHub Pages Service** - Automated hosting and CDN distribution

## Interactive Diagram

<iframe src="main.html" width="100%" height="900px" style="border: 2px solid #ccc; border-radius: 8px;"></iframe>

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

## References

- [MkDocs Documentation](https://www.mkdocs.org/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [mkdocs gh-deploy command](https://www.mkdocs.org/user-guide/deploying-your-docs/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
