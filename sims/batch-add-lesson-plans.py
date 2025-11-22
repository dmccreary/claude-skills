#!/usr/bin/env python3
"""
Batch add lesson plans to high-priority MicroSims
"""

import os
from pathlib import Path

SIMS_DIR = Path(__file__).parent

# Lesson plans for each MicroSim
LESSON_PLANS = {
    "microsim-file-relationship-diagram": """## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Understand** (Understand) the file structure and relationships in MicroSim projects
- **Analyze** (Analyze) dependencies between HTML, CSS, JavaScript, and metadata files
- **Apply** (Apply) MicroSim structural patterns to create new interactive visualizations
- **Evaluate** (Evaluate) whether a MicroSim meets structural quality standards
- **Create** (Create) properly structured MicroSim directories with all required files

### Target Audience

- **Primary**: Educational technology developers, MicroSim creators
- **Secondary**: Web developers learning educational content patterns
- **Level**: Undergraduate web development or professional development
- **Prerequisites**: Basic HTML, CSS, and JavaScript knowledge

### Activities

**Activity 1: File Relationship Identification (15 minutes)**

1. Examine the diagram and identify which file is the entry point (index.md)
2. Trace the path from index.md to main.html through the iframe element
3. Identify how main.html loads style.css and script.js
4. List the purpose of metadata.json in the MicroSim structure

**Activity 2: Dependency Analysis (20 minutes)**

1. Count how many files directly depend on main.html (1: index.md via iframe)
2. Identify files that could be optional vs. required for minimum functionality
3. Discuss: Why is metadata.json separate from index.md YAML frontmatter?
4. Create a checklist of required files for a valid MicroSim

**Activity 3: Create a MicroSim Structure (45 minutes)**

1. Create a new MicroSim directory following the kebab-case naming convention
2. Generate all 5 core files: index.md, main.html, style.css, script.js, metadata.json
3. Implement a simple interactive visualization (student's choice: chart, diagram, animation)
4. Test that the iframe embed works correctly in index.md

**Activity 4: Quality Validation (20 minutes)**

Using the microsim-standardization checklist:

1. Verify your MicroSim has all required files
2. Check that metadata.json contains all 9 Dublin Core fields
3. Ensure index.md has proper YAML frontmatter with image references
4. Calculate your MicroSim's quality score using the rubric

### Assessment

**Formative Assessment:**
- During Activity 1: Can students correctly identify file dependencies?
- During Activity 3: Does the created MicroSim follow the correct structure?

**Summative Assessment:**

Create a complete MicroSim from scratch that meets these criteria:

1. **Structure** (30 points): All required files present and properly named
2. **Functionality** (30 points): Interactive visualization works in iframe
3. **Metadata** (20 points): Complete Dublin Core metadata and YAML frontmatter
4. **Documentation** (20 points): Clear index.md with overview and usage instructions

**Success Criteria:**
- MicroSim achieves quality score ≥ 80/100
- All file relationships function correctly
- Documentation clearly explains the visualization's purpose
""",

    "mkdocs-github-pages-deployment": """## Lesson Plan

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
""",

    "orphaned-nodes-identification": """## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Identify** (Remember) orphaned nodes in directed graphs using visual analysis
- **Analyze** (Analyze) the pedagogical implications of concepts with no dependents
- **Evaluate** (Evaluate) whether orphaned nodes indicate quality issues or valid terminal concepts
- **Apply** (Apply) graph analysis techniques to improve learning graph structure
- **Create** (Create) recommendations for resolving orphaned node issues

### Target Audience

- **Primary**: Instructional designers working with learning graphs
- **Secondary**: Curriculum developers, educational data analysts
- **Level**: Graduate education programs or professional development
- **Prerequisites**: Understanding of directed graphs and learning graph concepts

### Activities

**Activity 1: Orphaned Node Detection (15 minutes)**

1. Examine the chart showing orphaned nodes vs. integrated concepts
2. Calculate what percentage of the 200-concept graph consists of orphaned nodes
3. Identify the maximum in-degree for integrated concepts
4. Discuss: Is having 8 orphaned nodes (4%) a problem for a 200-concept graph?

**Activity 2: Root Cause Analysis (25 minutes)**

For each identified orphaned node, determine the likely cause:

1. **Too advanced**: Concept has no simpler concepts depending on it
2. **Too specific**: Niche topic not needed for other concepts
3. **Incorrectly placed**: Should be in a different domain/course
4. **Valid terminal**: Legitimate endpoint in the learning progression

Categorize the 8 orphaned nodes using these criteria.

**Activity 3: Resolution Strategies (30 minutes)**

For 3 different orphaned nodes, propose resolution strategies:

1. **Option 1**: Remove the orphaned concept entirely (when appropriate?)
2. **Option 2**: Add dependent concepts that build on it
3. **Option 3**: Merge it with a related concept
4. **Option 4**: Keep as-is (justify why it's a valid terminal concept)

Write a 1-paragraph rationale for each chosen strategy.

**Activity 4: Graph Quality Improvement (40 minutes)**

Using a provided learning graph CSV:

1. Run a script to identify all orphaned nodes (in-degree = 0 from other concepts)
2. Visualize orphaned vs. integrated concepts using Chart.js
3. Propose 5 new concepts that could depend on orphaned nodes
4. Update the CSV to add these dependencies and verify orphans are resolved

### Assessment

**Formative Assessment:**
- During Activity 2: Can students correctly categorize orphaned node types?
- During Activity 3: Do resolution strategies match the orphaned node characteristics?

**Summative Assessment:**

Analyze and improve a learning graph with orphaned nodes:

1. **Detection** (25 points): Correctly identify all orphaned nodes in a 150-concept graph
2. **Analysis** (30 points): Categorize each orphaned node by type with clear rationale
3. **Resolution Plan** (25 points): Propose specific, actionable fixes for each orphan
4. **Implementation** (20 points): Update graph structure and verify improvement

**Success Criteria:**
- Orphaned node percentage reduced to <3%
- All remaining orphans justified as valid terminal concepts
- No new orphans introduced during resolution
- Graph maintains DAG structure (no cycles)
""",

    "taxonomy-distribution-pie": """## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Interpret** (Understand) taxonomy distribution patterns in learning graphs
- **Analyze** (Analyze) whether concept categorization is balanced across domains
- **Evaluate** (Evaluate) the appropriateness of taxonomy category percentages
- **Apply** (Apply) Chart.js pie chart techniques to visualize categorical data
- **Create** (Create) custom taxonomy schemes for new subject domains

### Target Audience

- **Primary**: Instructional designers, curriculum developers
- **Secondary**: Data visualization specialists, educational researchers
- **Level**: Graduate education or professional development
- **Prerequisites**: Basic statistics, familiarity with learning graphs

### Activities

**Activity 1: Distribution Analysis (20 minutes)**

1. Identify the three largest taxonomy categories in the pie chart
2. Calculate what percentage of concepts fall outside the top 3 categories
3. Determine if any single category exceeds 30% (potential over-concentration)
4. Compare the largest and smallest categories - what's the ratio?

**Activity 2: Balance Evaluation (25 minutes)**

Using taxonomic distribution best practices:

1. Assess whether the distribution indicates good coverage across domains
2. Identify any categories that seem under-represented (<3%)
3. Evaluate if any categories could be merged due to semantic overlap
4. Propose an "ideal" distribution for a well-balanced course (percentages for each category)

**Activity 3: Interactive Chart Modification (30 minutes)**

1. Modify the Chart.js data array to represent your own course's concept distribution
2. Add a new taxonomy category and update colors appropriately
3. Implement hover tooltips showing concept count + percentage
4. Add a legend positioned to the right of the chart

**Activity 4: Create Custom Taxonomy (45 minutes)**

For a new course domain (e.g., "Introduction to Cybersecurity"):

1. Design 8-12 taxonomy categories that span the subject comprehensively
2. Assign 3-letter abbreviation codes to each category
3. Create a balanced target distribution (sum to 100%)
4. Generate a pie chart visualization with your taxonomy and target percentages
5. Write 2-3 sentences explaining your category choices

### Assessment

**Formative Assessment:**
- During Activity 1: Can students correctly calculate percentages from visual data?
- During Activity 4: Do custom taxonomy categories cover the domain comprehensively?

**Summative Assessment:**

Design and visualize a complete taxonomy system:

1. **Taxonomy Design** (30 points): Create 10-12 categories for a specified subject
   - Categories are mutually exclusive
   - Complete domain coverage
   - Clear, descriptive labels

2. **Distribution Planning** (25 points): Assign target percentages summing to 100%
   - No category exceeds 30%
   - Justification for distribution choices

3. **Visualization** (25 points): Create functional Chart.js pie chart
   - Accurate data representation
   - Appropriate color scheme
   - Readable labels and legend

4. **Documentation** (20 points): Write taxonomy usage guidelines
   - When to use each category
   - Example concepts for each
   - Decision criteria for edge cases

**Success Criteria:**
- Taxonomy categories are comprehensive and non-overlapping
- Distribution is balanced without over-concentration
- Visualization clearly communicates proportions
- Documentation enables consistent categorization
""",

    "test-world-cities": """## Lesson Plan

### Learning Objectives

After completing this lesson, students will be able to:

- **Understand** (Understand) how Leaflet.js renders interactive web maps
- **Apply** (Apply) geographic coordinate systems to place markers on maps
- **Analyze** (Analyze) the trade-offs between different map tile providers
- **Create** (Create) custom interactive maps with markers and popups
- **Evaluate** (Evaluate) map visualizations for clarity and information density

### Target Audience

- **Primary**: Web developers, data visualization specialists
- **Secondary**: Geographic information systems (GIS) students, digital cartographers
- **Level**: Undergraduate computer science or professional development
- **Prerequisites**: Basic JavaScript, HTML, and CSS; understanding of latitude/longitude

### Activities

**Activity 1: Map Interaction Exploration (15 minutes)**

1. Pan across the map to view all continents
2. Zoom in to street level on 3 different cities
3. Click markers to view city information popups
4. Compare the map styles between OpenStreetMap and other tile providers (if multiple available)
5. Note: How does the map behave on mobile vs. desktop?

**Activity 2: Coordinate Analysis (20 minutes)**

1. Verify 5 city coordinates are accurate using an external source (e.g., Google Maps)
2. Calculate the distance between Tokyo (35.68°N, 139.65°E) and São Paulo (23.55°S, 46.63°W)
3. Identify which cities are in the Southern Hemisphere (latitude < 0)
4. Explain why London has negative longitude despite being far from the Prime Meridian

**Activity 3: Add Your Own Markers (35 minutes)**

1. Choose 5 cities not currently on the map
2. Look up their latitude/longitude coordinates
3. Add JavaScript code to place markers for these cities:
   ```javascript
   L.marker([latitude, longitude]).addTo(map)
     .bindPopup('<b>City Name</b><br>Country<br>Population: X');
   ```
4. Customize marker icons or colors for different continents
5. Verify all markers appear correctly when the map loads

**Activity 4: Create a Thematic Map (50 minutes)**

Design a map showing:

1. **Theme selection**: Choose a topic (e.g., capital cities, UNESCO sites, tech hubs)
2. **Data collection**: Gather 15-20 locations with coordinates
3. **Marker customization**: Use different icons/colors for categories
4. **Popup content**: Include relevant information (population, facts, images)
5. **Map bounds**: Set initial view to show all markers
6. **Deployment**: Test the map in fullscreen and iframe modes

### Assessment

**Formative Assessment:**
- During Activity 2: Can students correctly interpret latitude/longitude coordinates?
- During Activity 3: Do added markers appear in correct geographic locations?

**Summative Assessment:**

Create a complete custom interactive map:

1. **Data Quality** (25 points): Accurate coordinates for 15+ locations
2. **Visualization Design** (30 points): Effective use of markers, popups, and zoom levels
3. **Interactivity** (20 points): Smooth panning, zooming, and popup functionality
4. **Code Quality** (15 points): Clean JavaScript, proper Leaflet.js API usage
5. **Documentation** (10 points): README explaining map theme and data sources

**Success Criteria:**
- Map loads without errors and displays all markers
- Coordinate accuracy within 0.1 degrees
- Popups provide useful contextual information
- Map is responsive and works on mobile devices
- Initial view shows all markers within bounds

### Extension Activities

- **Advanced**: Implement clustering for overlapping markers at low zoom levels
- **Integration**: Load marker data from external GeoJSON file
- **Styling**: Create custom map tiles or use Mapbox for advanced styling
- **Analytics**: Add heatmap layer showing data density
"""
}

def add_lesson_plan(microsim_name, lesson_plan_text):
    """Add lesson plan to a MicroSim's index.md before References section"""
    index_path = SIMS_DIR / microsim_name / 'index.md'

    if not os.path.exists(index_path):
        print(f"  ✗ index.md not found for {microsim_name}")
        return False

    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if lesson plan already exists
    if '## Lesson Plan' in content:
        print(f"  ○ Lesson plan already exists")
        return False

    # Find insertion point (before References or Related Resources or at end)
    if '## References' in content:
        new_content = content.replace('## References', lesson_plan_text + '\n\n## References')
    elif '## Related Resources' in content:
        new_content = content.replace('## Related Resources', lesson_plan_text + '\n\n## Related Resources')
    else:
        # Add at end
        new_content = content.rstrip() + '\n\n' + lesson_plan_text + '\n'

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ Added lesson plan")
    return True


def main():
    print("Adding Lesson Plans to High-Priority MicroSims")
    print("=" * 60)

    added = 0
    skipped = 0

    for microsim_name, lesson_plan in LESSON_PLANS.items():
        print(f"\n{microsim_name}:")
        if add_lesson_plan(microsim_name, lesson_plan):
            added += 1
        else:
            skipped += 1

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"✓ Lesson plans added: {added}")
    print(f"○ Skipped: {skipped}")
    print("=" * 60)


if __name__ == '__main__':
    main()
