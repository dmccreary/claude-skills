---
title: Adding Taxonomy to CSV Workflow
description: Interactive Mermaid visualization showing adding taxonomy to csv workflow
image: /sims/adding-taxonomy-workflow/adding-taxonomy-workflow.png
og:image: /sims/adding-taxonomy-workflow/adding-taxonomy-workflow.png
quality_score: 80
---
# Adding Taxonomy to CSV Workflow

<iframe src="main.html" width="100%" height="1200px"></iframe>

**Copy this iframe to your website:**

```html
<iframe src="https://dmccreary.github.io/claude-skills/sims/adding-taxonomy-workflow/main.html" width="100%" height="600px"></iframe>
```

[Run Adding Taxonomy to CSV Workflow in Fullscreen](main.html){ .md-button .md-button--primary }


This interactive Mermaid diagram shows the complete workflow for adding taxonomy categorization to a learning graph CSV file.

## Interactive Diagram

## Process Overview

This workflow demonstrates how to add taxonomy categorization to an existing learning graph CSV file. The process supports both automated (script-based) and manual categorization approaches.

### Key Steps

1. **Identify Natural Categories** - Review concept labels and group by topic, domain, or complexity level
2. **Design Taxonomy Abbreviations** - Create 3-5 letter codes (FOUND, BASIC, ARCH, etc.)
3. **Choose Categorization Method** - Select between automated (add-taxonomy.py) or manual assignment
4. **Review Assignments** - Check that categorization makes logical sense
5. **Validate Distribution** - Run taxonomy-distribution.py to ensure balance
6. **Adjust if Needed** - Refine categories until distribution is balanced (no category > 30%)

### Decision Points

**Automated vs Manual:** The add-taxonomy.py script uses keyword matching for initial suggestions, best for large graphs (150+ concepts). Manual assignment gives more control, recommended for smaller graphs or specialized domains.

**Distribution Check:** A balanced distribution ensures no single taxonomy dominates. Target: no category exceeding 30% of total concepts.