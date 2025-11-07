# Venn Diagram Skill 

!!! prompt
    Use the skill-generator skill to create a new skill called `venn-diagram-generator`.  This skill 
    will use the venn.js javascript library to create a new diagram.  The github repo for venn.js is 
    here: https://github.com/benfred/venn.js/.  The output of this skill will be the creation of a new 
    directory in the /docs/sims directory.  Each drawing must have a title as well as a directory name 
    in lowercase with dashes.  Use the existing microseism as templates.  Make sure you create an index.md
    file, a main.html, a script.js and if needed, a style.css file.  The drawing should be referenced by
    placing an <iframe> HTML element at the top of the index.md file.  If the user does not provide a 
    title, ask them for a title.  Place the new skill in /skills/venn-diagram-generator. 