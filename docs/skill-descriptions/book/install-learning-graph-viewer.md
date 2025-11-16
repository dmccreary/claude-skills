# Install the earning Graph Viewer MicroSim

Skill: install-learning-graph-viewer (user)
This skill installs an interactive learning graph viewer application into an
  intelligent textbook project. Use this skill when working with a textbook that has a
  learning-graph.json file and needs a visual, interactive graph exploration tool with search,
  filtering, and statistics capabilities.

## Steps

## Step 1: Copy Files

Copies the 4 files from the learning-graphs repo:

https://github.com/dmccreary/learning-graphs/tree/main/docs/sims/graph-viewer

1. index.md
2. main.html
3. style.css
4. script.js

This is a vis-network application with a legend and search.

## Step 2: Replace the TITLE in the main.html

This step pulls the title from the learning-graph.json metadata title and places
it in the main.html file.

## Step 3: Update the mkdocs.yml file

```yml
 - MicroSims:
    - List of MicroSims: sims/index.md
    - Graph Viewer: sims/graph-viewer/in
```
