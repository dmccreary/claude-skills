---
name: comparison-table-generator
description: This skill generates interactive comparison table MicroSims for educational content. Use this skill when users need to create side-by-side comparisons of items with star ratings (1-5 scale), difficulty badges (Easy/Medium/Hard), logos, hover tooltips, and description columns. The skill creates a complete MicroSim package with HTML, CSS, logos directory, index.md documentation, and metadata.json, then updates mkdocs.yml navigation.
---

# Comparison Table Generator

## Overview

This skill generates interactive comparison table MicroSims that allow students to compare multiple items across several criteria. Each table includes color-coded star ratings, difficulty/category badges, logos, hover tooltips with descriptions, and a responsive design. The output follows the microsim-standardization skill standards including proper index.md documentation, metadata.json with Dublin Core elements, and mkdocs.yml navigation updates.

## When to Use This Skill

Use this skill when:

- Creating educational comparisons (e.g., programming languages, frameworks, tools, distributions)
- Building decision-making aids with multiple criteria
- Presenting rated comparisons with visual indicators
- Need interactive tables with hover tooltips for additional context

## Workflow

### Step 1: Gather Requirements

Ask the user for the following information:

1. **Table Title**: The main title for the comparison (e.g., "Linux Distribution Comparison")
2. **MicroSim Name**: Kebab-case directory name (e.g., `linux-distro-comparison`)
3. **Items to Compare**: List of 3-8 items with:
   - Item name
   - Logo filename (SVG preferred, 32x32px)
   - Tooltip description (1-2 sentences)
4. **Rating Columns**: 1-4 rating criteria (each rated 1-5 stars)
5. **Difficulty/Category Column**: Optional column with Easy/Medium/Hard badges (or custom categories)
6. **Description Column**: Text column header (e.g., "Best For", "Use Case")
7. **Legend Items**: Descriptions for difficulty badges

### Step 2: Create Directory Structure

Create the MicroSim directory at `docs/sims/[microsim-name]/` with:

```
docs/sims/[microsim-name]/
├── index.md          # Documentation page
├── main.html         # Interactive comparison table
├── style.css         # Styling with star colors, badges, tooltips
├── metadata.json     # Dublin Core metadata
└── logos/            # SVG logo files for each item
    ├── item1.svg
    ├── item2.svg
    └── ...
```

### Step 3: Generate main.html

Use the template in `assets/main-template.html` as the base. Key customization points:

1. **Title**: Update the `<title>` and `<h2>` elements
2. **Table Headers**: Customize the `<thead>` columns
3. **Table Rows**: For each item, create a `<tr>` with:
   - `data-tooltip` attribute containing the item description
   - Logo + name cell using `.distro-cell` class
   - Rating cells with appropriate star counts and color classes
   - Difficulty badge with appropriate class (easy/medium/hard)
   - Description text cell
4. **Legend**: Update legend badges to match the difficulty column categories

**Star Rating Pattern:**
```html
<!-- 4 out of 5 stars (yellow-green) -->
<td class="rating">
    <span class="stars stars-4">★★★★</span>
    <span class="stars-empty">★</span>
</td>
```

Star color classes:
- `stars-5`: Green (#22c55e) - Excellent
- `stars-4`: Yellow-green (#84cc16) - Very Good
- `stars-3`: Orange (#f59e0b) - Good/Average
- `stars-2`: Red-orange (#f97316) - Below Average
- `stars-1`: Red (#ef4444) - Poor

**First Row Note:** The first row's tooltip automatically appears BELOW instead of above to avoid being hidden by the header.

### Step 4: Generate style.css

Copy the template from `assets/style-template.css`. The CSS includes:

- Star rating color system (5-color scale)
- Difficulty badge styling (easy/medium/hard)
- Pure CSS hover tooltips with smooth transitions
- First-row tooltip fix (displays below instead of above)
- Responsive design for mobile/tablet
- Consistent row heights for logo alignment

Customization may be needed for:
- Custom badge categories (beyond easy/medium/hard)
- Custom color schemes
- Additional column types

### Step 5: Create index.md

Use the template in `assets/index-template.md` to create documentation that includes:

1. **YAML Frontmatter**: title, description, quality_score
2. **Title**: Level 1 header matching the table title
3. **Iframe**: Embedded view of main.html
4. **Fullscreen Button**: Link to view main.html fullscreen
5. **About Section**: Explanation of the comparison
6. **Rating Explanations**: What each rating criterion measures
7. **Item Summaries**: Brief description of each compared item
8. **Learning Objectives**: Bloom's Taxonomy-aligned objectives

### Step 6: Create metadata.json

Create Dublin Core metadata following the schema in `assets/metadata-schema.json`:

```json
{
  "title": "Comparison Table Title",
  "description": "Interactive comparison table showing...",
  "creator": "Author Name",
  "date": "YYYY-MM-DD",
  "subject": ["comparison", "keyword1", "keyword2"],
  "type": "Interactive Simulation",
  "format": "text/html",
  "language": "en-US",
  "rights": "CC BY 4.0",
  "educationalLevel": "High School",
  "learningResourceType": "comparison table",
  "library": "CSS (no JavaScript library)"
}
```

### Step 7: Add Logo Files

Place SVG logo files in the `logos/` subdirectory:

- Recommended size: 32x32px
- SVG format preferred for scalability
- Name files with kebab-case matching item names (e.g., `debian.svg`, `arch-linux.svg`)

If logos are not provided, prompt the user to:
1. Provide logo files to copy
2. Provide URLs to download logos from
3. Create simple placeholder SVG icons

### Step 8: Update mkdocs.yml Navigation

Add the new MicroSim to the site navigation in `mkdocs.yml`:

1. Find the `nav:` section
2. Locate or create the "Simulations" or "MicroSims" section
3. Add an entry for the new comparison table:

```yaml
nav:
  - Simulations:
    - Comparison Table Name: sims/microsim-name/index.md
```

### Step 9: Validate and Report

After creating all files:

1. Verify all files exist in the directory
2. Validate metadata.json against the schema
3. Check that iframe height is appropriate (typically 400-600px based on row count)
4. Report the created files and their locations
5. Suggest running `mkdocs serve` to preview the result

## Customization Options

### Custom Badge Categories

To use categories other than Easy/Medium/Hard:

1. Add new CSS classes in style.css following the `.difficulty` pattern
2. Update the legend to explain the new categories
3. Use consistent color coding (green=good, yellow=neutral, red=challenging)

### Custom Color Schemes

The default uses semantic colors (green=good, red=poor). To customize:

1. Modify `.stars-1` through `.stars-5` in style.css
2. Ensure sufficient contrast for accessibility
3. Update legend if color meanings change

### Additional Column Types

The template supports:
- **Rating columns**: Star ratings 1-5
- **Badge columns**: Categorical badges with colors
- **Text columns**: Plain text descriptions
- **Logo+Name columns**: Image with text

For new column types, add appropriate CSS classes.

## Resources

### assets/main-template.html

Complete HTML template for the comparison table with:
- Comprehensive HTML comments explaining each section
- Sample data rows demonstrating all patterns
- Proper tooltip structure with data-tooltip attributes
- Legend and source attribution sections

### assets/style-template.css

Complete CSS stylesheet including:
- Documented lessons learned section
- Star rating color classes
- Difficulty badge styling
- Tooltip system with first-row fix
- Responsive breakpoints

### assets/index-template.md

Documentation template following microsim-standardization standards:
- YAML frontmatter with SEO fields
- Iframe embed patterns
- Section structure for educational content
- Learning objectives template

### assets/metadata-schema.json

JSON Schema for validating metadata.json files (copied from microsim-standardization skill).

### assets/metadata-template.json

Sample metadata.json with all Dublin Core fields.

## Notes

- **Iframe Height**: Calculate based on number of rows. Approximately 60px per row + 150px for header/legend. Default 470px works for 5 rows.
- **Tooltip Length**: Keep tooltips under 200 characters for readability.
- **Logo Consistency**: Ensure all logos use the same dimensions to prevent row height shifting.
- **First Row Tooltips**: The CSS automatically positions the first row's tooltip below to avoid header overlap.
- **Accessibility**: Use semantic color coding and ensure text has sufficient contrast.
