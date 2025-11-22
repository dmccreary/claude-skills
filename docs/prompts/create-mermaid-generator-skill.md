# Create Mermaid Generator Skill

!!! prompt
    Use the skill-generator skill to create a new skill called `mermaid-generator`.  This will take an
    textual description of a workflow diagram and render it using the mermaid javascript library.  By 
    default it will use a top-down rendering and colorful backgrounds for each item.  All labels will 
    use a 16-point font.  Edges between items will also have a 16 label.  If the description of the 
    diagram is not complete, prompt the user for additional information.  All workflow diagrams must have
    a DIAGRAM_NAME in lower-case with only dashes.  Suggest a name if the user does not specify a name.

    Create the following files in the /docs/sims/{{DIAGRAM_NAME}} directory:

    1. index.md - with the <iframe> reference to it in the file
    2. main.html - the HTML file we reference in the <iframe src="main.html">
    3. script.js - javascript code
    4. style.css - CSS style sheet
    5. metadata.json - Dublin Core for search engine and reuse

⏺ I'll use the skill-creator skill to help you create a new mermaid-generator skill that generates
  workflow diagrams using the Mermaid JavaScript library.

> The "skill-creator" skill is running 

> The "skill-creator" skill is running 

⏺ I'll help you create the mermaid-generator skill. Let me start by understanding the skill
  requirements better with some clarifying questions.
                                                                                                   
⏺ User answered Claude's questions:
  ⎿  · What format should the mermaid-generator skill output? An HTML file with embedded Mermaid, 
     markdown with mermaid code blocks, or both? → Standalone HTML file
     · What types of Mermaid diagrams should this skill support? → Flowcharts
     · Where should the generated diagrams be saved in an intelligent textbook project? → /docs/sims
      and use a format similar to the other microsims that use an index.md, data.json, stylel.css, 
     main.html and script.js files in the /docs/sims/NAME
     · Should the skill include a reference guide for Mermaid syntax? → Yes, include reference

⏺ Perfect! Now I understand the requirements. The skill will:
  - Generate standalone HTML files in the MicroSim format
  - Focus on flowchart diagrams
  - Save to /docs/sims/NAME with the standard structure (index.md, metadata.json, style.css,
  main.html, script.js)
  - Include Mermaid syntax reference documentation

  Let me create this skill following the skill creation process.

⏺ Bash(python3 $HOME/.claude/skills/skill-creator/scripts/init_skill.py mermaid-generator --path
      $HOME/Documents/ws/claude-skills/skills)
  ⎿  🚀 Initializing skill: mermaid-generator                 
        Location: $HOME/Documents/ws/claude-skills/skills
     … +13 lines (ctrl+o to expand)

⏺ Read(skills/mermaid-generator/SKILL.md)
  ⎿  Read 86 lines

⏺ Bash(rm $HOME/Documents/ws/claude-skills/skills/mermaid-generator/scripts/example.py
      $HOME/Documents/ws/claude-skills/skills/mermaid-generator/references/a…)
  ⎿  (No content)

⏺ Fetch(`https://mermaid.js.org/syntax/flowchart.html`)
  ⎿  Received 188.5KB (200 OK)

⏺ Now I'll create the Mermaid syntax reference documentation:

⏺ Write(skills/mermaid-generator/references/mermaid-flowchart-syntax.md)
  ⎿  Wrote 271 lines to skills/mermaid-generator/references/mermaid-flowchart-syntax.md            
     # Mermaid Flowchart Syntax Reference
     This reference guide covers Mermaid flowchart syntax for generating interactive workflow
     diagrams.
     ## Basic Structure
     Every Mermaid flowchart starts with a direction declaration:
     ```mermaid
     flowchart TD
     … +261 lines (ctrl+o to expand)

⏺ Bash(mkdir -p $HOME/Documents/ws/claude-skills/skills/mermaid-generator/assets/template)
  ⎿  (No content)

⏺ Write(skills/mermaid-generator/assets/template/main.html)
  ⎿  Wrote 47 lines to skills/mermaid-generator/assets/template/main.html                          
     <!DOCTYPE html>
     <html lang="en">
     <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>{{TITLE}}</title>
         <link rel="stylesheet" href="style.css">
         <script type="module">
             import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
             mermaid.initialize({

     … +37 lines (ctrl+o to expand)

⏺ Write(skills/mermaid-generator/assets/template/style.css)
  ⎿  Wrote 165 lines to skills/mermaid-generator/assets/template/style.css
     /* Mermaid Diagram Stylesheet */
     :root {
         --primary-color: #667eea;
         --secondary-color: #764ba2;
         --background-color: #f8f9fa;
         --text-color: #2c3e50;
         --border-color: #dee2e6;
         --shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
     }
     … +155 lines (ctrl+o to expand)

⏺ Write(skills/mermaid-generator/assets/template/index.md)
  ⎿  Wrote 41 lines to skills/mermaid-generator/assets/template/index.md                           
     # {{TITLE}}
     ## Overview
     {{OVERVIEW}}
     ## Interactive Diagram
     <iframe src="main.html" width="100%" height="600px" style="border: 1px solid #ddd; 
     border-radius: 8px;"></iframe>
     … +31 lines (ctrl+o to expand)

⏺ Write(skills/mermaid-generator/assets/template/metadata.json)
  ⎿  Wrote 23 lines to skills/mermaid-generator/assets/template/metadata.json
     {
       "title": "{{TITLE}}",
       "description": "{{DESCRIPTION}}",
       "subject": "{{SUBJECT}}",
       "creator": "Claude AI with Mermaid Generator Skill",
       "date": "{{DATE}}",
       "type": "Interactive Workflow Diagram",
       "format": "text/html",
       "language": "en-US",
       "coverage": "{{COVERAGE}}",
     … +13 lines (ctrl+o to expand)

⏺ Write(skills/mermaid-generator/assets/template/script.js)
  ⎿  Wrote 200 lines to skills/mermaid-generator/assets/template/script.js              
     /**
      * Mermaid Diagram Interactive Features
      *
      * This file provides additional interactive functionality for the Mermaid diagram.
      * Mermaid.js handles the core diagram rendering automatically.
      */
     // Wait for the DOM to be fully loaded
     document.addEventListener('DOMContentLoaded', function() {
         console.log('Mermaid diagram loaded successfully');
     … +190 lines (ctrl+o to expand)

⏺ Write(skills/mermaid-generator/SKILL.md)
  ⎿  Updated skills/mermaid-generator/SKILL.md with 483 additions and 53 removals                
         1    ---
         2    name: mermaid-generator
         3 -  description: [TODO: Complete and informative explanation of what the skill does and
           -  when to use it. Include WHEN to use this skill - specific scenarios, file types, or
           -  tasks that trigger it.]
         3 +  description: This skill generates interactive workflow diagrams using the Mermaid 
           + JavaScript library. Use this skill when users request creating flowcharts, process 
           + diagrams, workflow visualizations, or decision trees for educational textbooks. The 
           + skill creates MicroSim packages with standalone HTML files featuring colorful 
           + backgrounds, 16-point fonts, and top-down rendering by default, saved to /docs/sims/
           +  following the MicroSim pattern.
         4    ---
         5    
         6 -  # Mermaid Generator
         6 +  # Mermaid Diagram Generator
         7    
         8    ## Overview
         9    
        10 -  [TODO: 1-2 sentences explaining what this skill enables]
        10 +  Generate interactive workflow diagrams using Mermaid.js for intelligent textbooks. 
           + Creates complete MicroSim packages with standalone HTML files, MkDocs integration, 
           + and Dublin Core metadata. Each diagram features colorful node backgrounds, 16-point 
           + fonts for optimal readability, and follows the educational MicroSim pattern.
        11    
        12 -  ## Structuring This Skill
        12 +  ## When to Use This Skill
        13    
        14 -  [TODO: Choose the structure that best fits this skill's purpose. Common patterns:
        14 +  Use the mermaid-generator skill when users request:
        15    
        16 -  **1. Workflow-Based** (best for sequential processes)
        17 -  - Works well when there are clear step-by-step procedures
        18 -  - Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → 
           - "Editing"
        19 -  - Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...
        16 +  - Workflow diagrams or process flows
        17 +  - Decision trees with branching logic
        18 +  - Algorithm visualizations
        19 +  - System architecture flows
        20 +  - Educational process diagrams
        21 +  - Step-by-step procedure illustrations
        22 +  - State transition diagrams
        23 +  - Any flowchart-style visualization
        24    
        25 -  **2. Task-Based** (best for tool collections)
        26 -  - Works well when the skill offers different operations/capabilities
        27 -  - Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract 
           - Text"
        28 -  - Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 
           - 2...
        25 +  **Example user requests:**
        26 +  - "Create a flowchart showing the software development lifecycle"
        27 +  - "Generate a workflow diagram for the scientific method"
        28 +  - "Make a decision tree for troubleshooting network issues"
        29 +  - "Visualize the process of photosynthesis as a diagram"
        30    
        31 -  **3. Reference/Guidelines** (best for standards or specifications)
        32 -  - Works well for brand guidelines, coding standards, or requirements
        33 -  - Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → 
           - "Features"
        34 -  - Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...
        31 +  ## Workflow
        32    
        33 -  **4. Capabilities-Based** (best for integrated systems)
        34 -  - Works well when the skill provides multiple interrelated features
        35 -  - Example: Product Management with "Core Capabilities" → numbered capability list
        36 -  - Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. 
           - Feature...
        33 +  ### Step 1: Gather Diagram Requirements
        34    
        35 -  Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., 
           - start with task-based, add workflow for complex operations).
        35 +  Analyze the user's description to extract:
        36    
        37 -  Delete this entire "Structuring This Skill" section when done - it's just 
           - guidance.]
        37 +  1. **Diagram Purpose**: What process or workflow is being illustrated?
        38 +  2. **Key Steps**: What are the main nodes/steps in the workflow?
        39 +  3. **Decision Points**: Are there branching decisions (if/then)?
        40 +  4. **Flow Direction**: Should it be top-down (TD), left-right (LR), or other?
        41 +  5. **Start/End Points**: Where does the process begin and end?
        42    
        43 -  ## [TODO: Replace with the first main section based on chosen structure]
        43 +  **If the description is incomplete or unclear**, prompt the user for additional 
           + information:
        44    
        45 -  [TODO: Add content here. See examples in existing skills:
        46 -  - Code samples for technical skills
        47 -  - Decision trees for complex workflows
        48 -  - Concrete examples with realistic user requests
        49 -  - References to scripts/templates/references as needed]
        45 +  ```
        46 +  To create an accurate workflow diagram, I need more information:
        47    
        48 +  1. What are the main steps in this process?
        49 +  2. Are there any decision points where the flow branches?
        50 +  3. What happens in success vs. error scenarios?
        51 +  4. Should this flow top-down or left-right?
        52 +  ```
        53 +  
        54 +  **Required information before proceeding:**
        55 +  - At least 3-5 distinct steps/nodes
        56 +  - Clear start and end points
        57 +  - Understanding of the flow sequence
        58 +  
        59 +  ### Step 2: Design the Mermaid Flowchart
        60 +  
        61 +  Consult `references/mermaid-flowchart-syntax.md` for detailed syntax guidance.
        62 +  
        63 +  **Design decisions:**
        64 +  
        65 +  1. **Choose node shapes** based on purpose:
        66 +     - Rounded rectangles `("Label")` for start/end
        67 +     - Rectangles `["Label"]` for process steps
        68 +     - Diamonds `{"Decision?"}` for decision points
        69 +     - Circles `(("Label"))` for connectors
        70 +  
        71 +  2. **Select color palette** from reference guide:
        72 +     - Vibrant (purple/blue/pink) for engaging diagrams
        73 +     - Professional (turquoise/mint/coral) for formal content
        74 +     - Ocean (blue spectrum) for technical content
        75 +     - Or create custom palette matching textbook theme
        76 +  
        77 +  3. **Define style classes** for consistent theming:
        78 +     ```
        79 +     classDef startNode 
           + fill:#667eea,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
        80 +     classDef processNode 
           + fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
        81 +     classDef decisionNode 
           + fill:#f093fb,stroke:#333,stroke-width:2px,color:#333,font-size:16px
        82 +     ```
        83 +  
        84 +  4. **Ensure 16pt fonts** for all nodes and edge labels:
        85 +     - Set `font-size:16px` in all classDef declarations
        86 +     - Apply to edge labels: `linkStyle default font-size:16px`
        87 +  
        88 +  5. **Use top-down direction** unless user specifies otherwise:
        89 +     ```
        90 +     flowchart TD
        91 +     ```
        92 +  
        93 +  **Example Mermaid code structure:**
        94 +  
        95 +  ```mermaid
        96 +  flowchart TD
        97 +      Start("Start Process"):::startNode
        98 +      Step1["Gather Input"]:::processNode
        99 +      Decision{"Valid Input?"}:::decisionNode
       100 +      Step2["Process Data"]:::processNode
       101 +      Success("Success"):::successNode
       102 +      Error("Error - Retry"):::errorNode
       103 +  
       104 +      Start --> Step1 --> Decision
       105 +      Decision -->|Yes| Step2 --> Success
       106 +      Decision -->|No| Error --> Step1
       107 +  
       108 +      classDef startNode 
           + fill:#667eea,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       109 +      classDef processNode 
           + fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       110 +      classDef decisionNode 
           + fill:#f093fb,stroke:#333,stroke-width:2px,color:#333,font-size:16px
       111 +      classDef successNode 
           + fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       112 +      classDef errorNode 
           + fill:#fa709a,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       113 +  
       114 +      linkStyle default stroke:#999,stroke-width:2px,font-size:16px
       115 +  ```
       116 +  
       117 +  ### Step 3: Create the MicroSim Directory Structure
       118 +  
       119 +  Create the diagram directory following the MicroSim pattern:
       120 +  
       121 +  ```bash
       122 +  mkdir -p /docs/sims/[diagram-name]
       123 +  ```
       124 +  
       125 +  **Naming convention:**
       126 +  - Use kebab-case (lowercase with hyphens)
       127 +  - Descriptive and concise
       128 +  - Examples: `software-lifecycle`, `scientific-method`, `network-troubleshooting`
       129 +  
       130 +  ### Step 4: Generate Files from Templates
       131 +  
       132 +  Use the template files in `assets/template/` as a starting point. Replace 
           + placeholders with actual content:
       133 +  
       134 +  #### 4.1 Create main.html
       135 +  
       136 +  Copy `assets/template/main.html` and replace these placeholders:
       137 +  
       138 +  - `{{TITLE}}`: Diagram title (e.g., "Software Development Lifecycle")
       139 +  - `{{SUBTITLE}}`: Brief subtitle (e.g., "Interactive Workflow Diagram")
       140 +  - `{{MERMAID_CODE}}`: The complete Mermaid flowchart code (from Step 2)
       141 +  - `{{DESCRIPTION}}`: 2-3 sentence explanation of the diagram
       142 +  
       143 +  **Important:** Ensure proper indentation of the Mermaid code within the `<div 
           + class="mermaid">` tag.
       144 +  
       145 +  #### 4.2 Create style.css
       146 +  
       147 +  Copy `assets/template/style.css` directly - no modifications needed unless custom 
           + styling is requested.
       148 +  
       149 +  The default stylesheet ensures:
       150 +  - 16px font size for diagram elements
       151 +  - Responsive design for mobile devices
       152 +  - Clean, professional appearance
       153 +  - Print-friendly styling
       154 +  
       155 +  #### 4.3 Create script.js
       156 +  
       157 +  Copy `assets/template/script.js` directly. This provides:
       158 +  - Zoom controls for large diagrams
       159 +  - Export to SVG functionality
       160 +  - Node interaction tracking
       161 +  - Accessibility features
       162 +  
       163 +  #### 4.4 Create index.md
       164 +  
       165 +  Copy `assets/template/index.md` and replace placeholders:
       166 +  
       167 +  - `{{TITLE}}`: Same as main.html title
       168 +  - `{{OVERVIEW}}`: 1-paragraph overview of the workflow
       169 +  - `{{DESCRIPTION}}`: Detailed description of the process
       170 +  - `{{WORKFLOW_STEPS}}`: Bulleted list of main steps:
       171 +    ```markdown
       172 +    1. **Step Name** - Description of what happens
       173 +    2. **Decision Point** - What decision is being made
       174 +    3. **Final Step** - How the process concludes
       175 +    ```
       176 +  - `{{KEY_CONCEPTS}}`: Bulleted list of educational concepts illustrated
       177 +  - `{{RELATED_CONCEPTS}}`: Links to related textbook sections or concepts
       178 +  
       179 +  #### 4.5 Create metadata.json
       180 +  
       181 +  Copy `assets/template/metadata.json` and replace placeholders:
       182 +  
       183 +  - `{{TITLE}}`: Diagram title
       184 +  - `{{DESCRIPTION}}`: Brief description
       185 +  - `{{SUBJECT}}`: Educational subject area (e.g., "Computer Science", "Biology")
       186 +  - `{{DATE}}`: Current date in ISO format (YYYY-MM-DD)
       187 +  - `{{COVERAGE}}`: Scope of content (e.g., "Introductory", "Advanced")
       188 +  - `{{AUDIENCE}}`: Target audience (e.g., "High School", "Undergraduate")
       189 +  - `{{NODE_COUNT}}`: Number of nodes in diagram
       190 +  - `{{EDGE_COUNT}}`: Number of edges/arrows in diagram
       191 +  - `{{CONCEPTS_LIST}}`: JSON array of concept labels (e.g., `"Algorithm Design", 
           + "Data Validation"`)
       192 +  - `{{BLOOM_LEVEL}}`: Highest Bloom's Taxonomy level addressed (e.g., "Understand", 
           + "Apply", "Analyze")
       193 +  
       194 +  **Example metadata.json:**
       195 +  
       196 +  ```json
       197 +  {
       198 +    "title": "Software Development Lifecycle",
       199 +    "description": "Interactive workflow diagram showing the phases of software 
           + development from planning through deployment",
       200 +    "subject": "Computer Science",
       201 +    "creator": "Claude AI with Mermaid Generator Skill",
       202 +    "date": "2025-11-06",
       203 +    "type": "Interactive Workflow Diagram",
       204 +    "format": "text/html",
       205 +    "language": "en-US",
       206 +    "coverage": "Introductory",
       207 +    "rights": "Educational Use",
       208 +    "audience": "Undergraduate",
       209 +    "diagram_type": "flowchart",
       210 +    "direction": "TD",
       211 +    "node_count": "8",
       212 +    "edge_count": "10",
       213 +    "concepts": [
       214 +      "Requirements Analysis",
       215 +      "System Design",
       216 +      "Implementation",
       217 +      "Testing",
       218 +      "Deployment",
       219 +      "Maintenance"
       220 +    ],
       221 +    "bloom_taxonomy": "Understand",
       222 +    "version": "1.0"
       223 +  }
       224 +  ```
       225 +  
       226 +  ### Step 5: Update MkDocs Navigation
       227 +  
       228 +  Add the new diagram to the textbook's navigation in `mkdocs.yml`:
       229 +  
       230 +  ```yaml
       231 +  nav:
       232 +    - Visualizations:
       233 +      - Software Lifecycle: sims/software-lifecycle/index.md
       234 +  ```
       235 +  
       236 +  Or integrate into relevant chapter navigation:
       237 +  
       238 +  ```yaml
       239 +  nav:
       240 +    - Chapter 3 - Software Engineering:
       241 +      - Introduction: chapters/03/index.md
       242 +      - Lifecycle Diagram: sims/software-lifecycle/index.md
       243 +  ```
       244 +  
       245 +  ### Step 6: Validate and Test
       246 +  
       247 +  Perform quality checks:
       248 +  
       249 +  1. **Syntax validation**: Ensure Mermaid code renders without errors
       250 +  2. **File structure**: Verify all 5 files are present (index.md, metadata.json, 
           + style.css, main.html, script.js)
       251 +  3. **Placeholder replacement**: Check that no `{{PLACEHOLDERS}}` remain
       252 +  4. **Font size verification**: Confirm 16px fonts in Mermaid code and CSS
       253 +  5. **Color contrast**: Ensure text is readable on colored backgrounds
       254 +  6. **Responsive design**: Test that diagram works on different screen sizes
       255 +  
       256 +  **Test the diagram:**
       257 +  
       258 +  ```bash
       259 +  cd /docs
       260 +  mkdocs serve
       261 +  # Navigate to http://localhost:8000/sims/[diagram-name]/
       262 +  ```
       263 +  
       264 +  Open main.html directly in browser to test standalone functionality.
       265 +  
       266 +  ### Step 7: Inform the User
       267 +  
       268 +  Provide a summary of what was created:
       269 +  
       270 +  ```
       271 +  Created interactive Mermaid workflow diagram: [Diagram Name]
       272 +  
       273 +  Location: /docs/sims/[diagram-name]/
       274 +  
       275 +  Files generated:
       276 +  ✓ main.html - Standalone interactive diagram
       277 +  ✓ index.md - MkDocs integration page
       278 +  ✓ style.css - Responsive styling
       279 +  ✓ script.js - Interactive features (zoom, export)
       280 +  ✓ metadata.json - Dublin Core metadata
       281 +  
       282 +  Features:
       283 +  • Top-down flowchart layout
       284 +  • Colorful node backgrounds for visual clarity
       285 +  • 16-point fonts for optimal readability
       286 +  • [X] nodes and [Y] edges
       287 +  • Zoom controls and SVG export
       288 +  
       289 +  The diagram illustrates: [brief description]
       290 +  
       291 +  To view:
       292 +  1. Standalone: Open /docs/sims/[diagram-name]/main.html
       293 +  2. In textbook: Run `mkdocs serve` and navigate to the page
       294 +  
       295 +  Next steps:
       296 +  - Add navigation link in mkdocs.yml
       297 +  - Reference from relevant chapter content
       298 +  - Consider creating related diagrams for connected concepts
       299 +  ```
       300 +  
       301 +  ## Best Practices
       302 +  
       303 +  ### Design Principles
       304 +  
       305 +  1. **Clarity over Complexity**: Keep diagrams focused on core workflow - if too 
           + complex, consider breaking into multiple diagrams
       306 +  2. **Consistent Styling**: Use the same color palette across related diagrams in a 
           + textbook
       307 +  3. **Meaningful Labels**: Use clear, concise labels (2-5 words max per node)
       308 +  4. **Logical Flow**: Ensure arrows flow in expected reading direction (top-down or 
           + left-right)
       309 +  5. **Color Semantics**: Use colors consistently (e.g., green for success, red for 
           + errors)
       310 +  
       311 +  ### Accessibility
       312 +  
       313 +  1. **Font Size**: Always use 16px minimum for readability
       314 +  2. **Color Contrast**: Ensure WCAG AA contrast ratios (4.5:1 minimum)
       315 +  3. **Text Alternatives**: Provide descriptive text in index.md
       316 +  4. **Semantic HTML**: Use proper heading structure in documentation
       317 +  
       318 +  ### Educational Integration
       319 +  
       320 +  1. **Align with Learning Goals**: Map diagram to specific learning objectives
       321 +  2. **Bloom's Taxonomy**: Tag with appropriate cognitive level
       322 +  3. **Concept Dependencies**: Link to prerequisite concepts in learning graph
       323 +  4. **Practice Exercises**: Consider adding comprehension questions in index.md
       324 +  
       325 +  ### Common Patterns
       326 +  
       327 +  **Linear Process Flow:**
       328 +  ```
       329 +  Start → Step 1 → Step 2 → Step 3 → End
       330 +  ```
       331 +  
       332 +  **Decision Tree:**
       333 +  ```
       334 +  Start → Decision 1 (Yes/No)
       335 +    ├─ Yes → Action A → End
       336 +    └─ No → Decision 2 (Yes/No)
       337 +        ├─ Yes → Action B → End
       338 +        └─ No → Action C → End
       339 +  ```
       340 +  
       341 +  **Loop/Iteration:**
       342 +  ```
       343 +  Start → Initialize → Process → Check Complete?
       344 +    ├─ No → Process (loop back)
       345 +    └─ Yes → End
       346 +  ```
       347 +  
       348 +  **Error Handling:**
       349 +  ```
       350 +  Start → Try Action → Success?
       351 +    ├─ Yes → Continue → End
       352 +    └─ No → Error Handler → Retry or Exit
       353 +  ```
       354 +  
       355 +  ## Troubleshooting
       356 +  
       357 +  ### Common Issues
       358 +  
       359 +  **Issue: Mermaid code doesn't render**
       360 +  - Check for syntax errors (missing quotes, brackets)
       361 +  - Ensure `flowchart TD` directive is first line
       362 +  - Verify no reserved keywords used as IDs (like "end" in lowercase)
       363 +  
       364 +  **Issue: Fonts not 16px**
       365 +  - Verify `font-size:16px` in all classDef declarations
       366 +  - Check `linkStyle default font-size:16px` is present
       367 +  - Ensure style.css includes `.mermaid .node text` styling
       368 +  
       369 +  **Issue: Colors not showing**
       370 +  - Confirm classDef declarations come after flowchart code
       371 +  - Verify `:::className` syntax on nodes
       372 +  - Check hex color codes are valid
       373 +  
       374 +  **Issue: Diagram too large/small**
       375 +  - Adjust node count (split into multiple diagrams if >15 nodes)
       376 +  - Use zoom controls in script.js
       377 +  - Modify CSS max-width settings
       378 +  
       379 +  **Issue: Labels cut off or truncated**
       380 +  - Shorten label text
       381 +  - Use markdown strings for auto-wrapping: `A["Text **bold**"]`
       382 +  - Increase diagram container width in CSS
       383 +  
       384    ## Resources
       385    
       386 -  This skill includes example resource directories that demonstrate how to organize 
           - different types of bundled resources:
       386 +  ### Bundled References
       387    
       388 -  ### scripts/
       389 -  Executable code (Python/Bash/etc.) that can be run directly to perform specific 
           - operations.
       388 +  - **`references/mermaid-flowchart-syntax.md`**: Comprehensive Mermaid syntax guide 
           + with examples, node shapes, styling options, and color palettes
       389    
       390 -  **Examples from other skills:**
       391 -  - PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities 
           - for PDF manipulation
       392 -  - DOCX skill: `document.py`, `utilities.py` - Python modules for document 
           - processing
       390 +  ### Bundled Templates
       391    
       392 -  **Appropriate for:** Python scripts, shell scripts, or any executable code that 
           - performs automation, data processing, or specific operations.
       392 +  - **`assets/template/main.html`**: Standalone HTML diagram template
       393 +  - **`assets/template/style.css`**: Responsive stylesheet with 16px fonts
       394 +  - **`assets/template/script.js`**: Interactive features (zoom, export, tracking)
       395 +  - **`assets/template/index.md`**: MkDocs integration template
       396 +  - **`assets/template/metadata.json`**: Dublin Core metadata template
       397    
       398 -  **Note:** Scripts may be executed without loading into context, but can still be 
           - read by Claude for patching or environment adjustments.
       398 +  ### External Resources
       399    
       400 -  ### references/
       401 -  Documentation and reference material intended to be loaded into context to inform 
           - Claude's process and thinking.
       400 +  - Mermaid.js Documentation: https://mermaid.js.org/
       401 +  - MkDocs Material Theme: https://squidfunk.github.io/mkdocs-material/
       402 +  - Dublin Core Metadata: https://www.dublincore.org/specifications/dublin-core/
       403    
       404 -  **Examples from other skills:**
       405 -  - Product management: `communication.md`, `context_building.md` - detailed workflow
           -  guides
       406 -  - BigQuery: API reference documentation and query examples
       407 -  - Finance: Schema documentation, company policies
       404 +  ## Examples
       405    
       406 -  **Appropriate for:** In-depth documentation, API references, database schemas, 
           - comprehensive guides, or any detailed information that Claude should reference while
           -  working.
       406 +  ### Example 1: Simple Linear Workflow
       407    
       408 -  ### assets/
       409 -  Files not intended to be loaded into context, but rather used within the output 
           - Claude produces.
       408 +  **User Request:** "Create a diagram showing the steps of making coffee"
       409    
       410 -  **Examples from other skills:**
       411 -  - Brand styling: PowerPoint template files (.pptx), logo files
       412 -  - Frontend builder: HTML/React boilerplate project directories
       413 -  - Typography: Font files (.ttf, .woff2)
       410 +  **Generated Mermaid Code:**
       411    
       412 -  **Appropriate for:** Templates, boilerplate code, document templates, images, 
           - icons, fonts, or any files meant to be copied or used in the final output.
       412 +  ```mermaid
       413 +  flowchart TD
       414 +      Start("Start"):::startNode
       415 +      Step1["Boil Water"]:::processNode
       416 +      Step2["Grind Coffee Beans"]:::processNode
       417 +      Step3["Add Coffee to Filter"]:::processNode
       418 +      Step4["Pour Hot Water"]:::processNode
       419 +      Step5["Wait 4 Minutes"]:::processNode
       420 +      End("Enjoy Coffee!"):::endNode
       421    
       422 -  ---
       422 +      Start --> Step1 --> Step2 --> Step3 --> Step4 --> Step5 --> End
       423    
       424 -  **Any unneeded directories can be deleted.** Not every skill requires all three 
           - types of resources.
       424 +      classDef startNode 
           + fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       425 +      classDef processNode 
           + fill:#95e1d3,stroke:#333,stroke-width:2px,color:#333,font-size:16px
       426 +      classDef endNode 
           + fill:#6c5ce7,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       427 +  
       428 +      linkStyle default stroke:#999,stroke-width:2px,font-size:16px
       429 +  ```
       430 +  
       431 +  ### Example 2: Decision-Based Workflow
       432 +  
       433 +  **User Request:** "Create a flowchart for troubleshooting a computer that won't 
           + start"
       434 +  
       435 +  **Generated Mermaid Code:**
       436 +  
       437 +  ```mermaid
       438 +  flowchart TD
       439 +      Start("Computer Won't Start"):::startNode
       440 +      Check1{"Is it plugged in?"}:::decisionNode
       441 +      Fix1["Plug in power cable"]:::processNode
       442 +      Check2{"Does it have power?"}:::decisionNode
       443 +      Check3{"Do you hear beeps?"}:::decisionNode
       444 +      Fix2["Check power supply"]:::processNode
       445 +      Fix3["Check RAM seating"]:::processNode
       446 +      Fix4["Call technician"]:::processNode
       447 +      Success("Computer Started!"):::successNode
       448 +  
       449 +      Start --> Check1
       450 +      Check1 -->|No| Fix1 --> Check2
       451 +      Check1 -->|Yes| Check2
       452 +      Check2 -->|No| Fix2 --> Success
       453 +      Check2 -->|Yes| Check3
       454 +      Check3 -->|Yes| Fix3 --> Success
       455 +      Check3 -->|No| Fix4
       456 +  
       457 +      classDef startNode 
           + fill:#667eea,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       458 +      classDef processNode 
           + fill:#764ba2,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       459 +      classDef decisionNode 
           + fill:#f093fb,stroke:#333,stroke-width:2px,color:#333,font-size:16px
       460 +      classDef successNode 
           + fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       461 +  
       462 +      linkStyle default stroke:#999,stroke-width:2px,font-size:16px
       463 +  ```
       464 +  
       465 +  ### Example 3: Loop-Based Algorithm
       466 +  
       467 +  **User Request:** "Visualize a simple search algorithm"
       468 +  
       469 +  **Generated Mermaid Code:**
       470 +  
       471 +  ```mermaid
       472 +  flowchart TD
       473 +      Start("Start Search"):::startNode
       474 +      Input["Get search target"]:::processNode
       475 +      Init["Set index = 0"]:::processNode
       476 +      Loop["Check array[index]"]:::processNode
       477 +      Match{"Match found?"}:::decisionNode
       478 +      End{"More items?"}:::decisionNode
       479 +      Increment["index = index + 1"]:::processNode
       480 +      Success("Return index"):::successNode
       481 +      Fail("Return -1"):::errorNode
       482 +  
       483 +      Start --> Input --> Init --> Loop --> Match
       484 +      Match -->|Yes| Success
       485 +      Match -->|No| End
       486 +      End -->|Yes| Increment --> Loop
       487 +      End -->|No| Fail
       488 +  
       489 +      classDef startNode 
           + fill:#0083b0,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       490 +      classDef processNode 
           + fill:#00b4d8,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       491 +      classDef decisionNode 
           + fill:#90e0ef,stroke:#333,stroke-width:2px,color:#333,font-size:16px
       492 +      classDef successNode 
           + fill:#48cae4,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       493 +      classDef errorNode 
           + fill:#0077b6,stroke:#333,stroke-width:2px,color:#fff,font-size:16px
       494 +  
       495 +      linkStyle default stroke:#999,stroke-width:2px,font-size:16px
       496 +  ```
       497 +  
       498 +  ## Integration with Other Skills
       499 +  
       500 +  This skill works well with other intelligent textbook skills:
       501 +  
       502 +  - **learning-graph-generator**: Create diagrams for concepts in the learning graph
       503 +  - **chapter-content-generator**: Embed diagrams in chapter content
       504 +  - **microsim-p5**: Use Mermaid for static workflow diagrams, p5.js for dynamic 
           + simulations
       505 +  - **quiz-generator**: Create questions about workflow understanding
       506 +  - **glossary-generator**: Define terms used in diagram labels
       507 +  
       508 +  ## Version History
       509 +  
       510 +  **v1.0** - Initial release
       511 +  - Flowchart diagram generation
       512 +  - MicroSim package creation
       513 +  - 16pt fonts and colorful styling
       514 +  - Top-down rendering default
       515 +  - Dublin Core metadata support

⏺ Bash(python3 $HOME/.claude/skills/skill-creator/scripts/package_skill.py
      $HOME/Documents/ws/claude-skills/skills/mermaid-generator)
  ⎿  📦 Packaging skill: $HOME/Documents/ws/claude-skills/skills/mermaid-generator

     🔍 Validating skill...
     … +11 lines (ctrl+o to expand)

⏺ Perfect! I've successfully created the mermaid-generator skill. Here's what was built:

  Created Skill: mermaid-generator

  Location: $HOME/Documents/ws/claude-skills/skills/mermaid-generator/

  Packaged file: mermaid-generator.zip (ready for distribution)

  Skill Components

  Core Workflow (SKILL.md):
  - 7-step process for generating Mermaid workflow diagrams
  - Includes requirement gathering with user prompts for incomplete descriptions
  - Design guidance for colorful backgrounds and 16pt fonts
  - MicroSim directory structure creation
  - Template-based file generation
  - MkDocs navigation integration
  - Validation and testing procedures

  Reference Documentation:
  - references/mermaid-flowchart-syntax.md - Comprehensive guide covering:
    - Node shapes (rectangles, diamonds, circles, etc.)
    - Edge types and labeled transitions
    - Styling with 16px fonts
    - Three color palettes (Vibrant, Professional, Ocean)
    - Common workflow patterns
    - Interactive features

  Template Assets (assets/template/):
  1. main.html - Standalone Mermaid diagram with CDN loading
  2. style.css - Responsive styling with 16px font enforcement
  3. script.js - Interactive features (zoom controls, SVG export, node tracking)
  4. index.md - MkDocs integration template with placeholders
  5. metadata.json - Dublin Core metadata template

  Key Features

  - Top-down rendering by default (flowchart TD)
  - 16-point fonts enforced in both CSS and Mermaid classDef
  - Colorful backgrounds with three pre-defined palettes
  - MicroSim pattern compatibility (saves to /docs/sims/NAME/)
  - User prompting when diagram description is incomplete
  - Complete examples including linear workflows, decision trees, and loops
  - Integration guidance with other intelligent textbook skills

  Usage

  To use this skill:

  1. Install globally:
  # Extract mermaid-generator.zip to ~/.claude/skills/
  unzip mermaid-generator.zip -d ~/.claude/skills/
  2. Invoke the skill:
  /skill mermaid-generator
  3. Example request:
  "Create a flowchart showing the software development lifecycle"

  Validation Status

  ✅ All validation checks passed:
  - YAML frontmatter format correct
  - Skill naming conventions followed
  - Complete description provided
  - All template files present
  - Reference documentation included

  The skill is now ready to generate interactive Mermaid workflow diagrams for your intelligent
  textbooks!






