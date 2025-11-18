# Security Zones Diagram

**Chapter:** 09 - Claude Skills Architecture Development
**Generator:** mermaid-generator
**Match Score:** 94/100
**Difficulty:** Medium

## Specification

<summary>Security Zones Diagram</summary>
    Type: diagram

    Purpose: Illustrate the security boundaries and permission levels for skill execution

    Components to show:
    - Three concentric security zones (circles):
      - Inner zone (green): "Project Directory" - full read/write access
      - Middle zone (yellow): "User Skills Directory (~/.claude/skills)" - read access
      - Outer zone (red): "System Directories" - no access
    - Skill execution context (box) positioned in inner zone
    - Permission gates (shield icons) at zone boundaries
    - Arrows showing allowed/blocked access patterns

    Access patterns:
    - Green arrow: Project directory → full access (read/write)
    - Yellow arrow: Skills directory → read-only access
    - Red X: System directories → blocked

    Labels:
    - "Skill Execution Sandbox" (inner box)
    - "Default Allowed: Read/Write" (green zone)
    - "Default Allowed: Read-Only" (yellow zone)
    - "Permission Required" (red zone)
    - Permission gate icons with labels: "User Approval Required"

    Additional elements:
    - Small icons representing file operations (read, write, execute)
    - Legend explaining zone colors and access levels

    Style: Concentric circles with clear visual hierarchy

    Color scheme:
    - Green: Allowed operations
    - Yellow: Restricted operations
    - Red: Blocked operations
    - Blue: Skill execution context

    Implementation: SVG diagram or Mermaid.js