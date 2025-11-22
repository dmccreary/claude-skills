# Reference Generator Skill

!!! prompt
    Please use the skill creator for creating a new skill that creates high-quality references for a textbook.  The references should all be verified links.  Use the format 
  
  1. [Link Title](testing URL) - publication_date - publication_name - description of resource and relevancy to the
  textbook.  
  
  When you generate the references, look at the /docs/course-description.md file for the information such as grade-level, target-audience or prerequisites to gage the level of reader for the references.  For example a text for junior-high students should have fun and engaging references.  
  
  Generate 10 references for junior-high level texts, 
  20 for senior-high students, 
  30 for colleges level students and 
  40 for grad-school level textbooks.  
  
  Use more authoritative peer-reviewed papers for college level references.  Place the results of the references in the file /docs/references.md.  
  
  Note that some users might want to only add reference to the end of a chapter.  If you find chapter content, ask them if they want book-level or chapter-level references. 

  ## Claude Code Response

  I'll use the skill-creator to help you create a new skill for generating high-quality textbook references.

> The "skill-creator" skill is running 

> The "skill-creator" skill is running 

⏺ I'll help you create a high-quality reference generator skill for textbooks. Let me start by understanding the requirements and then create the
   skill.

⏺ Now let me initialize the skill:

⏺ Bash(python3 $HOME/.claude/skills/skill-creator/scripts/init_skill.py reference-generator --path $HOME/.claude/skills/)
  ⎿  🚀 Initializing skill: reference-generator
        Location: $HOME/.claude/skills/
     … +12 lines (ctrl+o to expand)

⏺ Now let me read the generated SKILL.md and update it:

⏺ Read(~/.claude/skills/reference-generator/SKILL.md)
  ⎿  Read 86 lines

⏺ Now let me create the comprehensive SKILL.md file:

⏺ Write(~/.claude/skills/reference-generator/SKILL.md)
  ⎿  Updated ../../../.claude/skills/reference-generator/SKILL.md with 173 additions and 52 removals                                          
         1    ---
         2    name: reference-generator
         3 -  description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this 
           - skill - specific scenarios, file types, or tasks that trigger it.]
         3 +  description: This skill generates curated, verified reference lists for textbooks with level-appropriate resources (10 for 
           + junior-high, 20 for senior-high, 30 for college, 40 for graduate). References are formatted with links, publication details, and 
           + relevance descriptions. Use this skill when working with intelligent textbooks that need academic references, either book-level 
           + or chapter-level.
         4    ---
         5    
         6    # Reference Generator
         7    
         8    ## Overview
         9    
        10 -  [TODO: 1-2 sentences explaining what this skill enables]
        10 +  Generate high-quality, verified reference lists for educational textbooks with level-appropriate content and quantity. The skill
           +  analyzes course descriptions to determine the target audience and creates references that match the readers' level, from fun and
           +  engaging resources for junior-high students to authoritative peer-reviewed papers for graduate students.
        11    
        12 -  ## Structuring This Skill
        12 +  ## When to Use This Skill
        13    
        14 -  [TODO: Choose the structure that best fits this skill's purpose. Common patterns:
        14 +  Use this skill when:
        15 +  - Creating a new intelligent textbook that needs a comprehensive reference list
        16 +  - Adding references to an existing textbook
        17 +  - Updating or expanding references for educational content
        18 +  - A user explicitly requests reference generation
        19    
        20 -  **1. Workflow-Based** (best for sequential processes)
        21 -  - Works well when there are clear step-by-step procedures
        22 -  - Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
        23 -  - Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...
        20 +  ## Reference Generation Workflow
        21    
        22 -  **2. Task-Based** (best for tool collections)
        23 -  - Works well when the skill offers different operations/capabilities
        24 -  - Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
        25 -  - Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...
        22 +  ### Step 1: Analyze the Course Description
        23    
        24 -  **3. Reference/Guidelines** (best for standards or specifications)
        25 -  - Works well for brand guidelines, coding standards, or requirements
        26 -  - Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
        27 -  - Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...
        24 +  Read the `/docs/course-description.md` file to determine:
        25 +  - **Grade level** or target audience (junior-high, senior-high, college, graduate)
        26 +  - **Prerequisites** - indicates reader sophistication
        27 +  - **Subject matter** - determines reference topics
        28 +  - **Learning objectives** - guides reference selection
        29    
        30 -  **4. Capabilities-Based** (best for integrated systems)
        31 -  - Works well when the skill provides multiple interrelated features
        32 -  - Example: Product Management with "Core Capabilities" → numbered capability list
        33 -  - Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...
        30 +  The grade level determines:
        31 +  - **Junior-high (middle school)**: 10 references - fun, engaging, visual resources
        32 +  - **Senior-high (high school)**: 20 references - mix of accessible and academic sources
        33 +  - **College (undergraduate)**: 30 references - more academic, some peer-reviewed papers
        34 +  - **Graduate (masters/PhD)**: 40 references - heavily peer-reviewed, authoritative sources
        35    
        36 -  Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., start with task-based, add workflow for complex
           -  operations).
        36 +  ### Step 2: Check for Chapter-Level Content
        37    
        38 -  Delete this entire "Structuring This Skill" section when done - it's just guidance.]
        38 +  Before generating references, search for chapter content in the textbook:
        39    
        40 -  ## [TODO: Replace with the first main section based on chosen structure]
        40 +  ```bash
        41 +  # Look for chapter files
        42 +  find /docs -name "chapter*.md" -o -name "*-chapter-*.md"
        43 +  ```
        44    
        45 -  [TODO: Add content here. See examples in existing skills:
        46 -  - Code samples for technical skills
        47 -  - Decision trees for complex workflows
        48 -  - Concrete examples with realistic user requests
        49 -  - References to scripts/templates/references as needed]
        45 +  If chapter content exists, use the AskUserQuestion tool to ask:
        46 +  - "Would you like book-level references (in /docs/references.md) or chapter-level references (at the end of each chapter)?"
        47    
        48 -  ## Resources
        48 +  ### Step 3: Generate References with Verification
        49    
        50 -  This skill includes example resource directories that demonstrate how to organize different types of bundled resources:
        50 +  For each reference, perform the following:
        51    
        52 -  ### scripts/
        53 -  Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.
        52 +  1. **Search for authoritative sources** using WebSearch tool
        53 +  2. **Verify each URL** using WebFetch to ensure the link is valid and accessible
        54 +  3. **Format according to the standard template** (see Format Specification below)
        55    
        56 -  **Examples from other skills:**
        57 -  - PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
        58 -  - DOCX skill: `document.py`, `utilities.py` - Python modules for document processing
        56 +  **Quality Guidelines by Level:**
        57    
        58 -  **Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or 
           - specific operations.
        58 +  **Junior-High (10 references):**
        59 +  - Educational websites with interactive content
        60 +  - Videos from reputable educational channels
        61 +  - Visual resources, infographics, and animations
        62 +  - Age-appropriate articles from educational publishers
        63 +  - Museums, science centers, and educational organizations
        64    
        65 -  **Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment 
           - adjustments.
        65 +  **Senior-High (20 references):**
        66 +  - Mix of educational websites and academic sources
        67 +  - Reputable news organizations and science journalism
        68 +  - Educational videos and documentaries
        69 +  - Introduction to academic journals (more accessible papers)
        70 +  - Government and NGO educational resources
        71    
        72 -  ### references/
        73 -  Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.
        72 +  **College (30 references):**
        73 +  - Peer-reviewed journal articles (50%+ of references)
        74 +  - Academic textbooks and monographs
        75 +  - University course materials and lectures
        76 +  - Research institution publications
        77 +  - Industry white papers and technical reports
        78    
        79 -  **Examples from other skills:**
        80 -  - Product management: `communication.md`, `context_building.md` - detailed workflow guides
        81 -  - BigQuery: API reference documentation and query examples
        82 -  - Finance: Schema documentation, company policies
        79 +  **Graduate (40 references):**
        80 +  - Heavily weighted toward peer-reviewed journals (70%+ of references)
        81 +  - Seminal papers in the field
        82 +  - Recent research (last 5 years) showing current state of field
        83 +  - Meta-analyses and systematic reviews
        84 +  - Academic books from university presses
        85    
        86 -  **Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information
           -  that Claude should reference while working.
        86 +  ### Step 4: Format Each Reference
        87    
        88 -  ### assets/
        89 -  Files not intended to be loaded into context, but rather used within the output Claude produces.
        88 +  Use the following format for every reference:
        89    
        90 -  **Examples from other skills:**
        91 -  - Brand styling: PowerPoint template files (.pptx), logo files
        92 -  - Frontend builder: HTML/React boilerplate project directories
        93 -  - Typography: Font files (.ttf, .woff2)
        90 +  ```markdown
        91 +  1. [Link Title](URL) - YYYY-MM-DD - Publication Name - Brief description of resource and specific relevance to the textbook 
           + topic.
        92 +  ```
        93    
        94 -  **Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or 
           - used in the final output.
        94 +  **Format Specifications:**
        95 +  - **Link Title**: Exact title of the article, paper, video, or resource
        96 +  - **URL**: Verified, working link (use WebFetch to confirm)
        97 +  - **Date**: Publication date in YYYY-MM-DD format (use YYYY-MM or YYYY if day/month unavailable)
        98 +  - **Publication Name**: Journal, website, organization, or publisher
        99 +  - **Description**: 1-2 sentences explaining what the resource covers and why it's relevant to this specific textbook
       100    
       101 +  **Example References:**
       102 +  
       103 +  ```markdown
       104 +  1. [How Neural Networks Really Work](https://distill.pub/2020/circuits/zoom-in/) - 2020-03-10 - Distill - Interactive 
           + visualization explaining the inner workings of neural networks through explorable explanations, perfect for visual learners 
           + beginning their ML journey.
       105 +  
       106 +  2. [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - 2017-06-12 - arXiv - Seminal paper introducing the 
           + Transformer architecture that revolutionized natural language processing and forms the foundation for modern LLMs like GPT and 
           + BERT.
       107 +  
       108 +  3. [Khan Academy: Introduction to Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms) - 2024-01-15 - 
           + Khan Academy - Free, interactive course covering fundamental algorithms including sorting and searching, with visualizations and 
           + practice exercises suitable for high school students.
       109 +  ```
       110 +  
       111 +  ### Step 5: Write References to File
       112 +  
       113 +  **For book-level references:**
       114 +  Create or overwrite `/docs/references.md` with:
       115 +  
       116 +  ```markdown
       117 +  # References
       118 +  
       119 +  This textbook draws upon the following high-quality resources:
       120 +  
       121 +  [Generated numbered list of references]
       122 +  
       123    ---
       124 +  *References last updated: [Current Date]*
       125 +  ```
       126    
       127 -  **Any unneeded directories can be deleted.** Not every skill requires all three types of resources.
       127 +  **For chapter-level references:**
       128 +  Append to each chapter file (e.g., `/docs/chapter-01.md`):
       129 +  
       130 +  ```markdown
       131 +  
       132 +  ## References
       133 +  
       134 +  [Generated numbered list of references for this chapter]
       135 +  ```
       136 +  
       137 +  ### Step 6: Validation and Reporting
       138 +  
       139 +  After generating references:
       140 +  
       141 +  1. **Count the references** to ensure correct quantity for level
       142 +  2. **Verify all URLs** were checked with WebFetch
       143 +  3. **Report summary** to user:
       144 +     - Number of references generated
       145 +     - Target level identified
       146 +     - File location
       147 +     - Any URLs that failed verification (if any)
       148 +  
       149 +  ## URL Verification Process
       150 +  
       151 +  **Critical**: Every URL must be verified before inclusion.
       152 +  
       153 +  ```python
       154 +  # Use WebFetch for each URL
       155 +  WebFetch(url=reference_url, prompt="Is this page accessible? Provide the title and a brief description of the content.")
       156 +  ```
       157 +  
       158 +  If a URL returns an error or redirect:
       159 +  - Try to find an updated or archived version
       160 +  - Use Internet Archive / Wayback Machine if appropriate
       161 +  - Skip the reference if no valid URL exists
       162 +  - Note in the report any references that couldn't be verified
       163 +  
       164 +  ## Reference Quality Checklist
       165 +  
       166 +  Before finalizing references, ensure:
       167 +  - [ ] Correct quantity for target level (10/20/30/40)
       168 +  - [ ] All URLs verified and accessible
       169 +  - [ ] Publication dates included
       170 +  - [ ] Mix of resource types (articles, videos, papers)
       171 +  - [ ] Descriptions explain relevance to textbook
       172 +  - [ ] Academic rigor matches target audience
       173 +  - [ ] No duplicate sources
       174 +  - [ ] Proper formatting throughout
       175 +  
       176 +  ## Example Usage Scenarios
       177 +  
       178 +  **Scenario 1: New textbook**
       179 +  ```
       180 +  User: "Generate references for my textbook"
       181 +  → Read /docs/course-description.md
       182 +  → Identify level (e.g., college)
       183 +  → Check for chapters (none found)
       184 +  → Generate 30 verified references
       185 +  → Write to /docs/references.md
       186 +  ```
       187 +  
       188 +  **Scenario 2: Existing textbook with chapters**
       189 +  ```
       190 +  User: "Add references to my course"
       191 +  → Read /docs/course-description.md
       192 +  → Find chapter files exist
       193 +  → Ask: "Book-level or chapter-level references?"
       194 +  → User selects chapter-level
       195 +  → Generate references for each chapter
       196 +  → Append to each chapter file
       197 +  ```
       198 +  
       199 +  ## Resources
       200 +  
       201 +  This skill uses web-based verification tools built into Claude Code:
       202 +  - **WebSearch**: Find authoritative sources on topics
       203 +  - **WebFetch**: Verify URLs are accessible and extract metadata
       204 +  - **AskUserQuestion**: Clarify book-level vs chapter-level preference
       205 +  
       206 +  No additional scripts, references, or assets are required for this skill.

⏺ Now let me clean up the example files that aren't needed:

⏺ Bash(rm -rf $HOME/.claude/skills/reference-generator/scripts $HOME/.claude/skills/reference-generator/references
      $HOME/.claude/skills/reference-genera…)
  ⎿  (No content)

⏺ Now let me package the skill:

⏺ Bash(python3 $HOME/.claude/skills/skill-creator/scripts/package_skill.py $HOME/.claude/skills/reference-generator)
  ⎿  📦 Packaging skill: $HOME/.claude/skills/reference-generator

     🔍 Validating skill...
     … +5 lines (ctrl+o to expand)

⏺ Perfect! I've successfully created the reference-generator skill for creating high-quality textbook references. Here's what was created:

  Skill Overview

  The reference-generator skill automatically creates curated, verified reference lists for educational textbooks with the following features:

  Key Features

  1. Level-Appropriate Quantities
    - Junior-high: 10 references (fun, engaging, visual)
    - Senior-high: 20 references (mix of accessible and academic)
    - College: 30 references (50%+ peer-reviewed)
    - Graduate: 40 references (70%+ peer-reviewed)
  2. Automatic Level Detection
    - Reads /docs/course-description.md to identify target audience
    - Analyzes grade level, prerequisites, and learning objectives
    - Adjusts reference quality and quantity accordingly
  3. URL Verification
    - Every URL is verified using WebFetch before inclusion
    - Handles redirects and broken links
    - Suggests archived versions if needed
  4. Flexible Output
    - Book-level references → /docs/references.md
    - Chapter-level references → appended to each chapter
    - Automatically detects existing chapters and asks user preference
  5. Proper Formatting
    - Format: [Title](URL) - YYYY-MM-DD - Publication - Description and relevance
    - Includes publication dates and source names
    - Descriptions explain relevance to the specific textbook

  Workflow

  When invoked, the skill will:
  1. Analyze the course description to determine level
  2. Check for existing chapter content
  3. Ask user preference (book-level or chapter-level) if chapters exist
  4. Generate appropriate number of references with verification
  5. Format and write to the correct location
  6. Report summary with any issues

  Package Location

  The skill has been packaged and saved to:
  $HOME/Documents/ws/claude-skills/reference-generator.zip

  The skill is also installed in your skills directory at:
  ~/.claude/skills/reference-generator/

  You can now use this skill by invoking it when working on textbook projects that need references!

