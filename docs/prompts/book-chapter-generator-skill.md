# Prompt to Create a Chapter Generator

!!! prompt
    Use the skill-creator skill to create a new skill called `book-chapter-generator`.
    This skill will look at the following resources:

    ## Input Resources
    1. Course Description at /docs/course-description.md
    2. Learning Graph at /docs/learning-graph/learning-graph.json
    3. Concept Taxonomy at /docs/learning-graph/concept-taxonomy.md

    ## Step 1: Design Chapters

    It will then suggest an outline of about 12 chapters for this book assuming you have about 200 concepts to cover.
    Each chapter will have a Chapter Title in Title Case and be no longer than 200 characters long.
    This is so that the listing of the chapters can fit on a single line per chapter.
    Use the course description and the learning graph to make sure that

    1. Each concept is covered once
    2. No concept is introduced before its dependencies are covered
    3. No chapter contains too many or two few concepts

    You may, at your discretion have as few as six chapters, or as many as 20 chapters.

    ## Step 2: Present Chapter Design to the User

    Present a simple list of Chapter Titles to the user.  Only present the
    Chapter Titles and a single sentence of what that chapter contains.
    You may also discuss any challenges you found and how your design met these challenges.

    Ask the user if they approve the design (y/n) and if no, what changes they want to make.

    ## Step 3: Generate the Chapter Outline Files

    For each chapter, create a "URL-PATH-NAME" which is only lowercase letters and dashes. Do not put any special characters in the URL-PATH-NAME.  Use abbreviations if you need to keep the URL-PATH-NAME short.

    Create a series of directories using the following structure where URL-PATH-NAME is the name for each chapter.

    ```
    chapters/index.md
    chapters/01-URL-PATH-NAME/index.md
    chapters/02-URL-PATH-NAME/index.md
    chapters/03-URL-PATH-NAME/index.md
    ```

    ## Step 4: Add Content to the Index of Each Chapter

    Add content to each chapter index.md file including:

    1. The Chapter Title in a level 1 header
    2. A summary of what is in the chapter in a level 2 ## Summary section
    3. A numbered markdown list of concepts in a level 2 ## Concepts Covered section
    4. A 'TODO: Generate Chapter Content" which will be used by a future skill

## Example of Usage

!!! prompt
    /skills

> /skills is running… 
  ⎿  Allowed 1 tools for this command

⏺ I'll list all available Claude skills for you.

⏺ Bash(~/bin/list-skills.sh --names-only)
  ⎿  book-chapter-generator        
     course-description-analyzer
     faq-generator
     … +10 lines (ctrl+o to expand)

⏺ Available Claude Skills (13 total)

  1. book-chapter-generator
  2. course-description-analyzer
  3. faq-generator
  4. glossary-generator
  5. install-learning-graph-viewer
  6. intelligent-textbook
  7. intelligent-textbook-creator
  8. learning-graph-generator
  9. microsim-p5
  10. moving-rainbow
  11. quiz-generator
  12. reference-generator
  13. skill-creator

  If you'd like more details about any specific skill, let me know and I can read its SKILL.md file
  for you.

!!! prompt
    run the book-chapter-generator skill 

⏺ I'll run the book-chapter-generator skill for you.

> The "book-chapter-generator" skill is running 

> The "book-chapter-generator" skill is running 

⏺ I'll help you generate a book chapter structure for your IT Management Graph textbook. Let me
  start by analyzing the input resources.

⏺ Read(docs/course-description.md)
  ⎿  Read 122 lines

⏺ Read(docs/learning-graph/learning-graph.json)
  ⎿  Read 2094 lines

⏺ Read(docs/learning-graph/concept-taxonomy.md)
  ⎿  Read 189 lines

⏺ I've successfully read all the input resources. Now let me analyze the learning graph to identify
  design constraints and create an optimal chapter structure.

  Analysis Summary

  Course: IT Management Graphs - From Legacy CMDB to Modern Graph-Based Solutions (ISMG 620)
  Total Concepts: 200
  Taxonomy Categories: 14 categories (ITIL, RDBMS, GRAPH, GOPS, QPERF, DATA, OBSRV, COMP, BIZS,
  ASSET, TRANS, AI, VALID, OPS)

  Let me analyze the dependency structure to design the chapters:

⏺ Based on my analysis of the 200 concepts and their 189 dependency relationships, I've designed a
  12-chapter structure that respects all dependencies and creates a logical learning progression
  from legacy ITIL/CMDB concepts through relational databases to modern graph-based solutions.

⏺ Proposed Chapter Structure

  I've designed a 12-chapter structure for your textbook covering 200 concepts.

  Chapters:

  1. Introduction to ITIL and Configuration Management (20 concepts)
  This foundational chapter introduces ITIL framework, configuration items, CMDB concepts, and
  traditional IT service management processes that set the stage for understanding why legacy
  approaches have limitations.
  2. IT Asset Management Fundamentals (7 concepts)
  This chapter covers asset management principles including IT assets, hardware assets, software
  assets, and their relationship to configuration management.
  3. Relational Database Fundamentals (20 concepts)
  This chapter introduces RDBMS concepts, SQL, database schemas, tables, keys, joins, and query
  operations that form the foundation for understanding CMDB technical limitations.
  4. Graph Theory and Graph Database Foundations (18 concepts)
  This chapter transitions from relational to graph concepts, introducing graph theory, nodes,
  edges, property graphs, directed/undirected graphs, and DAGs.
  5. Graph Database Technologies and Query Languages (8 concepts)
  This chapter covers practical graph database implementations including native graph storage, graph
   layers, Neo4j, and Cypher query language.
  6. Graph Traversal and Dependency Analysis (23 concepts)
  This chapter explores graph operations including traversal algorithms, dependency tracing, blast
  radius analysis, impact analysis, and various dependency types for IT management.
  7. Business Services and IT Portfolio Management (12 concepts)
  This chapter connects IT assets to business value through service mapping, business service
  mapping, application portfolios, and digital estate management.
  8. Data Quality and Data Management Excellence (26 concepts)
  This chapter covers data management principles, DMBOK framework, data quality dimensions,
  governance, metadata, data lineage, and master data management essential for effective IT
  management graphs.
  9. Query Performance and Real-Time Operations (18 concepts)
  This chapter addresses performance considerations including real-time queries, latency,
  scalability, graph complexity, and metrics critical for operational IT management systems.
  10. Observability, Monitoring, and Automated Discovery (13 concepts)
  This chapter covers modern observability practices, telemetry, OpenTelemetry, eBPF, automated
  discovery, topology mapping, and drift detection that enable self-updating IT management graphs.
  11. Compliance, Risk Management, and Security (15 concepts)
  This chapter addresses regulatory compliance (HIPAA, GDPR, DORA), risk management, audit trails,
  access control, and security models in the context of IT management graphs.
  12. Digital Transformation and Advanced Topics (20 concepts)
  This final chapter covers transformation strategies, vendor management, AI-assisted curation,
  graph RAG, knowledge graphs, validation, operational excellence, and the future of IT management
  systems.

  Design Challenges & Solutions:

  Challenge: The course has three major concept domains (ITIL/CMDB legacy, RDBMS fundamentals, Graph
   databases) that must be taught in sequence
  Solution: Structured the first 5 chapters as a clear progression from legacy (Ch 1-2) through
  relational databases (Ch 3) to graph fundamentals (Ch 4-5)

  Challenge: Graph operations (GOPS category) has 23 concepts with complex inter-dependencies
  Solution: Dedicated Chapter 6 entirely to graph traversal and dependency analysis after
  establishing graph fundamentals in Chapters 4-5

  Challenge: Data management (DATA category) contains 26 concepts spanning quality, governance, and
  operational concerns
  Solution: Concentrated these in Chapter 8 after covering business services (Ch 7) so students
  understand the context for why data quality matters

  Challenge: Several advanced topics (AI, transformation, operations) needed to come late but are
  spread across different taxonomy categories
  Solution: Combined AI & Analytics, Transformation, Data Validation, and Operations concepts into
  Chapter 12 as "Advanced Topics" since they all build on earlier concepts

  Challenge: Balancing chapter sizes while respecting dependencies
  Solution: Most chapters have 12-23 concepts (optimal range), with only Chapter 2 (7 concepts) and
  Chapter 5 (8 concepts) slightly below target, but these serve as important transitional chapters

  Challenge: Ensuring observability concepts come after monitoring fundamentals
  Solution: Placed observability in Chapter 10 after establishing operational contexts in earlier
  chapters

  Statistics:

  - Total chapters: 12
  - Average concepts per chapter: 16.7
  - Range: 7-26 concepts per chapter
  - All 200 concepts covered: ✓
  - All dependencies respected: ✓

  Do you approve this chapter structure? (y/n)

  If no, please specify what changes you'd like:
  - Different number of chapters?
  - Specific concepts moved to different chapters?
  - Chapter titles revised?
  - Different grouping strategy?

> y 

⏺ Great! I'll now generate the chapter structure. Let me start by creating the directory structure:

⏺ Bash(mkdir -p chapters/01-intro-to-itil-and-config-mgmt chapters/02-it-asset-management
      chapters/03-relational-database-fundamentals chapters/04-graph-theory-and-dat…)
  ⎿  (No content)

⏺ Now let me create the main chapters index file:

⏺ Write(chapters/index.md)
  ⎿  Wrote 38 lines to chapters/index.md                                                           
     # Chapters
     This textbook is organized into 12 chapters covering 200 concepts.
     ## Chapter Overview
     1. [Introduction to ITIL and Configuration 
     Management](01-intro-to-itil-and-config-mgmt/index.md) - This foundational chapter introduces
     ITIL framework, configuration items, CMDB concepts, and traditional IT service management
     processes that set the stage for understanding why legacy approaches have limitations.
     2. [IT Asset Management Fundamentals](02-it-asset-management/index.md) - This chapter covers
     asset management principles including IT assets, hardware assets, software assets, and their
     relationship to configuration management.
     … +28 lines (ctrl+o to expand)

⏺ Now I'll create the individual chapter index files. Let me start with Chapter 1:

⏺ Write(chapters/01-intro-to-itil-and-config-mgmt/index.md)
  ⎿  Wrote 42 lines to chapters/01-intro-to-itil-and-config-mgmt/index.md                          
     # Introduction to ITIL and Configuration Management
     ## Summary
     This foundational chapter introduces the Information Technology Infrastructure Library (ITIL)
     framework and its approach to configuration management. You'll learn about configuration items,
      the Configuration Management Database (CMDB), and traditional IT service management processes
     including service support, service delivery, change management, incident management, and
     problem management. This chapter establishes the historical context and legacy approaches that
     led to the need for modern graph-based solutions, setting the stage for understanding why
     traditional CMDB implementations have consistently failed despite decades of investment.
     ## Concepts Covered
     This chapter covers the following 20 concepts from the learning graph:
     … +32 lines (ctrl+o to expand)

⏺ Write(chapters/02-it-asset-management/index.md)
  ⎿  Wrote 28 lines to chapters/02-it-asset-management/index.md                                    
     # IT Asset Management Fundamentals
     ## Summary
     This chapter focuses on IT asset management principles and practices, building on the
     configuration management concepts from Chapter 1. You'll learn the distinctions between asset
     management and configuration management, and understand how assets are categorized and tracked
     within IT organizations. This chapter provides essential context for understanding how IT
     resources are inventoried and managed, which becomes critical when we later explore how graph
     databases can represent these assets and their relationships more effectively than traditional
     approaches.
     ## Concepts Covered
     This chapter covers the following 7 concepts from the learning graph:
     … +18 lines (ctrl+o to expand)

⏺ Write(chapters/03-relational-database-fundamentals/index.md)
  ⎿  Wrote 41 lines to chapters/03-relational-database-fundamentals/index.md                       
     # Relational Database Fundamentals
     ## Summary
     This chapter provides a comprehensive introduction to relational database management systems
     (RDBMS), SQL, and the structural elements that define relational databases including schemas,
     tables, keys, and joins. You'll learn how RDBMS systems store and query data, understand the
     role of indexes and query optimization, and explore concepts like schema rigidity and
     evolution. This technical foundation is essential for understanding why traditional CMDBs built
      on RDBMS technology struggle with the complex relationship management required for modern IT
     estates, particularly when handling transitive dependencies and multi-hop queries.
     ## Concepts Covered
     This chapter covers the following 20 concepts from the learning graph:
     … +31 lines (ctrl+o to expand)

⏺ Write(chapters/04-graph-theory-and-database-foundations/index.md)
  ⎿  Wrote 39 lines to chapters/04-graph-theory-and-database-foundations/index.md                  
     # Graph Theory and Graph Database Foundations
     ## Summary
     This chapter marks the transition from relational to graph-based thinking by introducing
     fundamental graph theory concepts and their application to database systems. You'll learn about
      nodes, edges, vertices, relationships, and property graphs, understanding how these structures
      naturally represent connected data. The chapter covers different types of graphs including
     directed and undirected graphs, and introduces Directed Acyclic Graphs (DAGs) which are
     particularly important for dependency management. You'll also explore graph traversal
     fundamentals and basic graph algorithms that form the foundation for the advanced dependency
     analysis covered in later chapters.
     ## Concepts Covered
     This chapter covers the following 18 concepts from the learning graph:
     … +29 lines (ctrl+o to expand)

⏺ Write(chapters/05-graph-database-technologies/index.md)
  ⎿  Wrote 29 lines to chapters/05-graph-database-technologies/index.md                            
     # Graph Database Technologies and Query Languages
     ## Summary
     This chapter moves from graph theory to practical graph database implementation by examining
     different approaches to storing and querying graph data. You'll learn the critical distinction
     between native graph storage and graph layers built on top of relational databases,
     understanding the performance implications of each approach. The chapter introduces Neo4j as a
     leading native graph database platform and teaches Cypher query language, providing hands-on
     skills for working with graph databases. You'll also explore how graph queries enable pattern
     matching and relationship-based querying that would be cumbersome or impossible in SQL.
     ## Concepts Covered
     This chapter covers the following 8 concepts from the learning graph:
     … +19 lines (ctrl+o to expand)

⏺ Write(chapters/06-graph-traversal-and-dependency-analysis/index.md)
  ⎿  Wrote 45 lines to chapters/06-graph-traversal-and-dependency-analysis/index.md                
     # Graph Traversal and Dependency Analysis
     ## Summary
     This comprehensive chapter explores how graph traversal techniques enable sophisticated
     dependency analysis for IT management. You'll learn how to trace dependencies upstream and
     downstream, calculate blast radius for change impact, perform root cause analysis, and map
     complex dependency chains. The chapter covers various types of dependencies including service
     dependencies, application dependencies, and infrastructure dependencies, while teaching
     practical techniques for detecting circular dependencies and managing dependency maps. This
     represents the core capability that makes graph databases superior to relational systems for IT
      management, enabling real-time transitive dependency analysis that would require complex
     recursive joins in SQL.
     ## Concepts Covered
     This chapter covers the following 23 concepts from the learning graph:
     … +35 lines (ctrl+o to expand)

⏺ Write(chapters/07-business-services-and-portfolio/index.md)
  ⎿  Wrote 34 lines to chapters/07-business-services-and-portfolio/index.md                        
     # Business Services and IT Portfolio Management
     ## Summary
     This chapter connects technical IT infrastructure to business value by exploring how business
     and technical services are defined, mapped, and managed. You'll learn how service mapping
     techniques link technical resources to business capabilities, enabling organizations to
     understand the business impact of technical changes. The chapter covers application portfolio
     management, digital estate concepts, IT portfolio management, and service level agreements
     (SLAs), showing how graph-based approaches provide the real-time visibility needed to manage
     complex service dependencies and ensure business continuity.
     ## Concepts Covered
     This chapter covers the following 12 concepts from the learning graph:
     … +24 lines (ctrl+o to expand)

⏺ Write(chapters/08-data-quality-and-management/index.md)
  ⎿  Wrote 47 lines to chapters/08-data-quality-and-management/index.md                            
     # Data Quality and Data Management Excellence
     ## Summary
     This chapter addresses the critical importance of data quality and governance for effective IT
     management graphs. You'll learn about the DMBOK (Data Management Body of Knowledge) framework
     and its application to IT management data, exploring data quality dimensions including
     accuracy, completeness, consistency, timeliness, and validity. The chapter covers essential
     data management concepts including metadata, data lineage, data catalogs, master data
     management, and reference data. You'll understand the roles of data stewards, data owners, and
     data custodians, and learn how policy enforcement and access control protect sensitive IT
     management information. This foundation is essential because even the most sophisticated graph
     database is only as valuable as the quality of data it contains.
     ## Concepts Covered
     This chapter covers the following 26 concepts from the learning graph:
     … +37 lines (ctrl+o to expand)

⏺ Write(chapters/09-query-performance-and-real-time-ops/index.md)
  ⎿  Wrote 40 lines to chapters/09-query-performance-and-real-time-ops/index.md                    
     # Query Performance and Real-Time Operations
     ## Summary
     This chapter examines the performance characteristics that make graph databases suitable for
     real-time operational IT management. You'll learn about real-time query capabilities, query
     latency, response time metrics, and the performance implications of different query approaches.
      The chapter explores scalability patterns including horizontal and vertical scaling, and
     introduces graph-specific metrics such as graph complexity, graph density, node degree,
     in-degree, and out-degree. You'll understand how these metrics affect query performance and
     system design, and learn why native graph databases can execute complex multi-hop queries in
     sub-second timeframes while equivalent SQL queries with recursive joins may take minutes or
     fail entirely. This performance advantage is fundamental to enabling real-time impact analysis
     during incidents.
     ## Concepts Covered
     This chapter covers the following 18 concepts from the learning graph:
     … +30 lines (ctrl+o to expand)

⏺ Write(chapters/10-observability-and-automated-discovery/index.md)
  ⎿  Wrote 35 lines to chapters/10-observability-and-automated-discovery/index.md                  
     # Observability, Monitoring, and Automated Discovery
     ## Summary
     This chapter explores how modern observability practices and automated discovery tools can
     continuously update IT management graphs without manual intervention. You'll learn about
     observability fundamentals, monitoring systems, telemetry collection, and cutting-edge
     technologies like OpenTelemetry and eBPF (Extended Berkeley Packet Filter) that enable
     automated dependency discovery. The chapter covers network topology, service topology, dynamic
     topology mapping, and techniques for configuration drift detection. You'll understand how these
      automated approaches address one of the key failures of traditional CMDBs, which relied on
     manual data entry and quickly became outdated, by enabling self-updating IT management graphs
     that reflect the true current state of the IT environment.
     ## Concepts Covered
     This chapter covers the following 13 concepts from the learning graph:
     … +25 lines (ctrl+o to expand)

⏺ Write(chapters/11-compliance-risk-and-security/index.md)
  ⎿  Wrote 37 lines to chapters/11-compliance-risk-and-security/index.md                           
     # Compliance, Risk Management, and Security
     ## Summary
     This chapter addresses how IT management graphs support regulatory compliance, risk management,
      and security governance in modern organizations. You'll learn about major regulatory
     frameworks including HIPAA (Health Insurance Portability and Accountability Act), GDPR (General
      Data Protection Regulation), and DORA (Digital Operational Resilience Act), understanding how
     graph-based dependency analysis enables continuous compliance checking. The chapter covers
     audit trails, compliance reporting, risk assessment methodologies, and security models
     including role-based access control (RBAC). You'll understand how graph traversal queries can
     instantly identify all systems processing regulated data, trace data flows across system
     boundaries, and verify that security controls are properly configured throughout the IT estate,
      capabilities that are critical for demonstrating compliance to auditors and regulators.
     ## Concepts Covered
     This chapter covers the following 15 concepts from the learning graph:

     … +27 lines (ctrl+o to expand)

⏺ Write(chapters/12-digital-transformation-and-advanced-topics/index.md)
  ⎿  Wrote 43 lines to chapters/12-digital-transformation-and-advanced-topics/index.md             
     # Digital Transformation and Advanced Topics
     ## Summary
     This final chapter synthesizes earlier concepts and explores advanced topics for implementing
     IT management graphs at enterprise scale. You'll learn about digital transformation strategies,
      IT modernization initiatives, and practical migration approaches for moving from legacy CMDB
     systems to graph-based solutions. The chapter covers vendor management and evaluation of major
     platforms including ServiceNow, Dynatrace, and Atlassian, helping you make build-versus-buy
     decisions and calculate total cost of ownership (TCO) and return on investment (ROI). Advanced
     topics include AI-assisted curation, graph RAG (Retrieval Augmented Generation), knowledge
     graphs, and semantic models that enhance IT management graphs with machine learning
     capabilities. You'll also explore business rules, exception reporting, anomaly detection, and
     operational metrics that enable continuous improvement and operational excellence in managing
     modern digital estates.
     ## Concepts Covered
     This chapter covers the following 20 concepts from the learning graph:
     … +33 lines (ctrl+o to expand)

⏺ Now let me update the mkdocs.yml navigation. First, let me read the current file:

⏺ Read(mkdocs.yml)
  ⎿  Read 81 lines

⏺ Now I'll update the mkdocs.yml file to add the Chapters section:

⏺ Update(mkdocs.yml)
  ⎿  Updated mkdocs.yml with 14 additions                                                        
       10      - Home: index.md
       11      - About: about.md
       12      - Course Description: course-description.md
       13 +    - Chapters:
       14 +      - Overview: chapters/index.md
       15 +      - Chapter 1 - Introduction to ITIL and Configuration Management: 
          + chapters/01-intro-to-itil-and-config-mgmt/index.md
       16 +      - Chapter 2 - IT Asset Management Fundamentals: 
          + chapters/02-it-asset-management/index.md
       17 +      - Chapter 3 - Relational Database Fundamentals: 
          + chapters/03-relational-database-fundamentals/index.md
       18 +      - Chapter 4 - Graph Theory and Graph Database Foundations: 
          + chapters/04-graph-theory-and-database-foundations/index.md
       19 +      - Chapter 5 - Graph Database Technologies and Query Languages: 
          + chapters/05-graph-database-technologies/index.md
       20 +      - Chapter 6 - Graph Traversal and Dependency Analysis: 
          + chapters/06-graph-traversal-and-dependency-analysis/index.md
       21 +      - Chapter 7 - Business Services and IT Portfolio Management: 
          + chapters/07-business-services-and-portfolio/index.md
       22 +      - Chapter 8 - Data Quality and Data Management Excellence: 
          + chapters/08-data-quality-and-management/index.md
       23 +      - Chapter 9 - Query Performance and Real-Time Operations: 
          + chapters/09-query-performance-and-real-time-ops/index.md
       24 +      - Chapter 10 - Observability, Monitoring, and Automated Discovery: 
          + chapters/10-observability-and-automated-discovery/index.md
       25 +      - Chapter 11 - Compliance, Risk Management, and Security: 
          + chapters/11-compliance-risk-and-security/index.md
       26 +      - Chapter 12 - Digital Transformation and Advanced Topics: 
          + chapters/12-digital-transformation-and-advanced-topics/index.md
       27      - Learning Graph:
       28        - Introduction: learning-graph/index.md
       29        - Course Description Assessment: learning-graph/course-description-assessment.md

⏺ Perfect! Chapter structure generated successfully!

  Summary

  I've successfully created the complete chapter structure for your IT Management Graph textbook:

  Created Files:

  - chapters/index.md (main chapter overview)
  - 12 chapter directories with index files:
    - 01-intro-to-itil-and-config-mgmt/index.md (20 concepts)
    - 02-it-asset-management/index.md (7 concepts)
    - 03-relational-database-fundamentals/index.md (20 concepts)
    - 04-graph-theory-and-database-foundations/index.md (18 concepts)
    - 05-graph-database-technologies/index.md (8 concepts)
    - 06-graph-traversal-and-dependency-analysis/index.md (23 concepts)
    - 07-business-services-and-portfolio/index.md (12 concepts)
    - 08-data-quality-and-management/index.md (26 concepts)
    - 09-query-performance-and-real-time-ops/index.md (18 concepts)
    - 10-observability-and-automated-discovery/index.md (13 concepts)
    - 11-compliance-risk-and-security/index.md (15 concepts)
    - 12-digital-transformation-and-advanced-topics/index.md (20 concepts)
  - Updated mkdocs.yml with complete chapter navigation

  Next Steps:

  1. Review the chapter structure: Run mkdocs serve and navigate to the Chapters section
  2. Each chapter index.md has "TODO: Generate Chapter Content" as a placeholder
  3. Use a chapter content generation skill (when ready) to populate each chapter with detailed
  content
  4. All 200 concepts are assigned and all dependencies are respected

  Statistics:

  - Total chapters: 12
  - Total concepts assigned: 200
  - All dependencies respected: ✓
  - Average concepts per chapter: 16.7
  - Range: 7-26 concepts per chapter

  The chapter structure is now ready for content generation!

