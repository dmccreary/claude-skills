# MicroSim Standardization  Skill

!!! prompt
    Run the skill-generation skill.  Create a new skill called 'microsim-standardization'.  It will 
    get passed a directory of a current MicroSim.  The MicroSim might use a variety of javaScript 
    libraries.  However, they all need to have specific features.  Your task is to go through a 
    checklist of things the MicroSim should have and create a TODO list of all the upgrade to a 
    MicroSim standard. Then present the user with that TODO list.  Ask the user if you should proceed 
    (y/n) and then if the user says yes, make the changes.  Here is a list:  

    1. Check if the index.md file is present
    2. Check that the index.md file has yml metadata at the top (title, description, quality_score, 
    images for social preview) etc.
    3. Check that the title is immediatly after the yml metadata in level 1 header
    4. Check that an iframe element is after the level 1 title and that the iframe references the 
    main.html
    5. Check that a sample iframe in a html block is after the iframe with the text "Copy this iframe 
    to your website:"
    6. Check that there is a metadata.json file with Dublin core data in the file
    7. Validate the metadata.json file with the microsim schema in the assets of the skill
    8. Make sure there is a [Run in fullscreen](main.html){ .md-button .md-button--primary } after the 
    iframe example
    9. If the MicroSim is a p5.js MicroSim, check if there is a link such as [Edit in the p5.js 
    Editor](https://editor.p5js.org/dmccreary/sketches/P5_ID) link, if the link does not exist, prompt 
    the user for a path to their sketch.
    10. Check if there is a level 2 header after this frontmatter that describes the MicroSim and how 
    to use it.
    11. If a Lesson Plan does not exist in level 2 header, ask the user if you should create it
    12. Where appropriate, add a level 2 Reference