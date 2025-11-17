# MicroSim Matcher Skill

Use the skill-creator skill to generate a new skill called the `microsim-matcher`.

Here are the requirements for the `microsim-matcher` skill:

Your job is to find the best matches between a diagram specification and a microsim generator skill.

1. The input to the `microsim-matcher` skill will be a single 'diagram specification' file of a diagram, infographic or microsim
2. Your task is to analyze the file and then create a ranking of the quality of matches between the specification and the capabilities of a microsim-generator skill.
3. A list of the microsims you can consider and their capabilities is located at @docs/skill-descriptions/microsims/index.md
4. Each MicroSim generator has a short description in that file and a detailed description in its own markdown file in that directory.
5. The full skill file for each MicroSim generator is located in the skills directory.  You can access the SKILL.md file with each skill to get a clear idea of what that skill does and when to use that skill

The output of this skill is a ranked list of the top microsim skills that should be used for this skill.
Return a numbered list that includes the skill name, a match score from (0-100) and a reason this score has a specific value