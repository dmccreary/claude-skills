Use the skill creator skill to create a new feature of an existing     
  skill.  The current skill is @skills/microsim-utils The new            
  feature I want is a process that builds a nice index.md page that      
  has infromative grid cells that describe each microsim.  To do         
  this we need to use the mkdocs-material grid layout.  There is an      
  example of this format here: https://raw.githubusercontent.com/dmc     
  creary/intro-to-physics-course/refs/heads/main/docs/sims/index.md.     
  If the user says "update the microsim listings" or "update the         
  list of microsims" or "Create a grid view of all the microsims" or     
  "generate a listing of all the microsims" this new feature should      
  be invoked.  Note that the title is also a link and the image          
  comes after the title/link.  After the image is a short descripton     
  of the MicroSim taken from the microsim index.md yml metadata          
  "description" field.  For any microsims that are missing the           
  description, please add it.  For any microsims that are missing        
  the image, use the ~/.local/bin/bk-capture-screenshot shell            
  script. Verify that the screen capture worked and if it did not        
  work, create a TODO.md record in the @docs/sims directory.  Log        
  the skill updates to logs/generate-microsim-index-skill.md