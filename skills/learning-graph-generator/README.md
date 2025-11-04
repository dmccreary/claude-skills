# JSON Schema for Learning Graph

The file [learning-graph-schema.json](learning-graph-schema.json) contains a JSON schema
for validating a learning graph.

## Unix Shell Script

We have provided a UNIX shell script for running a validator on any learning graph.
Just pass the file name as the first parameter to the `validate-learning-graph.sh` file.

```sh
./validate-learning-graph.sh ../../docs/vis/combined-viewer/learning-graph.json 
```

**Sample Response:**

```
Validating learning graph...
Input file: ../../docs/vis/combined-viewer/learning-graph.json
Schema file: /Users/dan/Documents/ws/learning-graphs/src/schema/learning-graph-schema.json

✓ Validation successful!

Summary:
  Title: Graph Theory Learning Graph
  Creator: Dan McCreary
  Version: 1.0
  Groups: 10
  Nodes: 25
  Edges: 24
  Orphan nodes: 0

✓ Learning graph is valid!
```

## Schema Overview

  The schema validates learning graphs using JSON Schema Draft 2020-12 and includes:

### Metadata Section (required)

  - Required fields:
    - **title:** The learning graph title
    - **description:** Detailed description
  - Optional fields:
    - **dcreator:** Author/organization
    - **ddate:** Creation date (YYYY-MM-DD format)
    - **dversion:** Version number (e.g., "1.0")
    - **dformat:** Format specification
    - **dschema:** URL to this schema
    - **dlicense:** License information

### Groups Section (required)

  Taxonomy groups with styling properties:
  - Required: color (CSS color value)
  - Optional:
    - font (with color and size properties)
    - shape (default shape for group)

### Nodes Section (required)

  Array of concept nodes with:
  - Required: id, label, group
  - Optional: shape, color, font, x, y, fixed, hidden
  - All styling can override group defaults

### Edges Section (required)

  Array of dependency edges with:
  - Required: from, to (node IDs)
  - Optional: id, label, arrows, color, width, dashes

  Validation Features

  - ✓ Validates data types (string, integer, number, boolean, array, object)
  - ✓ Enforces required fields
  - ✓ Validates CSS color patterns (#hex, named colors, rgb/rgba)
  - ✓ Validates date format (YYYY-MM-DD)
  - ✓ Validates version format (semantic versioning)
  - ✓ Validates URI format for schema URL
  - ✓ Validates shape enums (box, circle, star, etc.)
  - ✓ Enforces minimum values (IDs >= 1, sizes >= 1, etc.)
  - ✓ Prevents additional properties where appropriate

  ## Sample Verification

  ✓ Schema is valid JSON
  ✓ All required keys present in learning-graph.json
  ✓ Metadata fields: 8 properties
  ✓ Groups count: 10
  ✓ Nodes count: 25
  ✓ Edges count: 24

