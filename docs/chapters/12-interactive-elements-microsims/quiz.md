# Quiz: Interactive Elements and MicroSims

Test your understanding of MicroSims, p5.js, interactive simulations, directory structure, seeded randomness, interactive controls, and educational simulation design with these questions.

---

#### 1. What distinguishes a MicroSim from a traditional comprehensive educational simulation?

<div class="upper-alpha" markdown>
1. MicroSims use more advanced programming languages
2. MicroSims focus on a single concept with deliberately constrained scope
3. MicroSims require less computational power to run
4. MicroSims only work on desktop computers
</div>

??? question "Show Answer"
    The correct answer is **B**. MicroSims are deliberately constrained in scope to demonstrate a single concept or principle, allowing learners to develop intuition about specific phenomena without cognitive overload. Unlike traditional simulations that may attempt to model entire systems comprehensively, MicroSims provide focused, explorable experiences. Option A is incorrect as MicroSims use accessible libraries like p5.js, option C confuses scope with performance, and option D misrepresents platform compatibility.

    **Concept Tested:** MicroSim

    **See:** [Introduction to MicroSims](../../glossary.md#microsim)

---

#### 2. What is the primary advantage of using p5.js for educational MicroSim development?

<div class="upper-alpha" markdown>
1. It requires extensive programming knowledge to use effectively
2. It provides an intuitive immediate-mode graphics paradigm with built-in animation loops
3. It is the fastest graphics library available for JavaScript
4. It only works with specific educational content management systems
</div>

??? question "Show Answer"
    The correct answer is **B**. The p5.js library excels in educational contexts because it uses an intuitive immediate-mode graphics paradigm where you simply call functions to draw shapes, and provides built-in animation loops through the `draw()` function that executes continuously. This eliminates complex retained-mode graphics APIs and makes creating dynamic visualizations straightforward. Option A contradicts p5.js's accessibility focus, option C focuses on irrelevant performance comparisons, and option D misrepresents p5.js's platform independence.

    **Concept Tested:** p5.js JavaScript Library

    **See:** [The p5.js Foundation](../../glossary.md#p5js-javascript-library)

---

#### 3. According to the table comparing content types, what learning analytics potential do MicroSims provide compared to static text or images?

<div class="upper-alpha" markdown>
1. Minimal, similar to static content
2. Basic completion tracking only
3. Good correctness data like quizzes
4. Excellent interaction pattern tracking
</div>

??? question "Show Answer"
    The correct answer is **D**. MicroSims provide excellent learning analytics potential through interaction pattern tracking, far exceeding static text (minimal time-on-page data) or images. Interactive simulations capture how students manipulate parameters, which scenarios they explore, and where they spend time, creating rich data about learning behaviors. Option A mischaracterizes MicroSim capabilities, option B describes video analytics, and option C describes quiz analytics rather than simulation analytics.

    **Concept Tested:** Interactive Simulations

    **See:** [Introduction to MicroSims](../../glossary.md#microsim)

---

#### 4. What are the three mandatory files in every MicroSim directory?

<div class="upper-alpha" markdown>
1. script.js, style.css, and index.html
2. main.html, index.md, and metadata.json
3. simulation.js, documentation.md, and config.xml
4. canvas.html, readme.txt, and settings.json
</div>

??? question "Show Answer"
    The correct answer is **B**. Each MicroSim follows a standardized structure with three essential files: main.html (self-contained p5.js simulation), index.md (documentation and embedding page), and metadata.json (Dublin Core metadata). This organizational pattern separates concerns between the interactive simulation, its documentation, and its metadata. Options A, C, and D use different naming conventions that don't match the intelligent textbook framework standards.

    **Concept Tested:** MicroSim Directory Structure

    **See:** [MicroSim Directory Structure](../../glossary.md#microsim-directory-structure)

---

#### 5. Why must the main.html file be entirely self-contained except for the p5.js library?

<div class="upper-alpha" markdown>
1. To reduce file size and improve loading speed
2. To enable embedding via iframe without external dependency issues
3. To make the code easier for beginners to understand
4. To comply with HTML5 validation requirements
</div>

??? question "Show Answer"
    The correct answer is **B**. The main.html file must be fully self-contained so it can be embedded via iframe without external dependencies beyond the p5.js library itself (loaded from CDN). This ensures the simulation works reliably when sandboxed in an iframe without broken references to external CSS or JavaScript files. Option A confuses self-containment with optimization, option C misidentifies the primary purpose, and option D invokes irrelevant validation concerns.

    **Concept Tested:** main.html in MicroSims

    **See:** [Creating the main.html File](../../glossary.md#mainhtml-in-microsims)

---

#### 6. You are embedding a MicroSim that has an 800x600 canvas and a 200-pixel control panel. The simulation is in the same directory as your index.md file. Which iframe code is correct?

<div class="upper-alpha" markdown>
1. `<iframe src="main.html" width="800" height="600"></iframe>`
2. `<iframe src="./main.html" width="1000" height="600" frameborder="0"></iframe>`
3. `<iframe src="../main.html" width="1000" height="600"></iframe>`
4. `<iframe href="./main.html" width="1000" height="600"></iframe>`
</div>

??? question "Show Answer"
    The correct answer is **B**. The correct iframe uses `src="./main.html"` (relative path in same directory), width of 1000 (800 canvas + 200 controls), height of 600, and `frameborder="0"` for clean integration. Option A doesn't account for the control panel width, option C uses incorrect parent directory path, and option D uses `href` instead of `src` which is invalid for iframes.

    **Concept Tested:** Iframe Embedding

    **See:** [Iframe Embedding Techniques](../../glossary.md#iframe-embedding)

---

#### 7. What is the primary pedagogical benefit of implementing seeded randomness in educational MicroSims?

<div class="upper-alpha" markdown>
1. It makes simulations run faster by reducing computation
2. It enables reproducibility while maintaining variability across different scenarios
3. It prevents students from sharing their results with each other
4. It eliminates the need for user controls like sliders and buttons
</div>

??? question "Show Answer"
    The correct answer is **B**. Seeded randomness resolves the tension between variability (students see different scenarios) and reproducibility (same seed always produces same sequence). This enables debugging, instruction referencing specific scenarios, student comparison of approaches, and consistent documentation while maintaining the engagement value of randomness. Option A confuses seeding with performance, option C mischaracterizes the purpose, and option D is factually incorrect about control requirements.

    **Concept Tested:** Seeded Randomness

    **See:** [Ensuring Reproducibility with Seeded Randomness](../../glossary.md#seeded-randomness)

---

#### 8. You are creating a physics simulation where students should be able to adjust gravity continuously and observe immediate effects on falling objects. Which interactive control is most appropriate?

<div class="upper-alpha" markdown>
1. A button labeled "Change Gravity"
2. A dropdown menu with preset gravity values
3. A slider with range 0-20 m/s² with visible current value
4. A text input field where students type gravity values
</div>

??? question "Show Answer"
    The correct answer is **C**. Sliders provide continuous parameter adjustment with immediate visual feedback, making them ideal for exploring continuous phenomena like physical constants. A slider makes the relationship between input and output visible through analog manipulation, supporting development of quantitative intuition. Option A provides discrete rather than continuous control, option B limits exploration to presets, and option D requires explicit submission rather than immediate reactivity.

    **Concept Tested:** Interactive Controls (Sliders)

    **See:** [Interactive Controls: Sliders](../../glossary.md#interactive-controls-sliders)

---

#### 9. When designing a MicroSim, you notice that adding multiple visualization modes, parameter controls, and algorithm options has made the interface complex and confusing. According to educational simulation design principles, what should you do?

<div class="upper-alpha" markdown>
1. Add a detailed tutorial to explain all the features
2. Simplify the interface by removing less important features
3. Consider splitting the simulation into multiple focused MicroSims
4. Keep all features but hide them in advanced menus
</div>

??? question "Show Answer"
    The correct answer is **C**. The "Micro" in MicroSim is deliberate—simulations work best when demonstrating one concept clearly rather than modeling complex systems comprehensively. If you're adding many controls or modes, consider splitting into multiple MicroSims, each addressing a different facet of the broader topic. This prevents cognitive overload from extraneous details. Option A addresses symptoms rather than causes, option B may remove important features, and option D hides complexity rather than eliminating it.

    **Concept Tested:** Educational Simulation Design

    **See:** [Principles of Educational Simulation Design](../../glossary.md#educational-simulation-design)

---

#### 10. What information should be included in the educational section of a MicroSim's metadata.json file?

<div class="upper-alpha" markdown>
1. Only the file size and last modified date
2. Programming language version and dependencies
3. Learning objectives, Bloom's levels, prerequisites, estimated time, and difficulty
4. Student names and completion timestamps
</div>

??? question "Show Answer"
    The correct answer is **C**. The educational section of metadata.json extends Dublin Core for learning-specific purposes, including learning objectives (specific outcomes students should achieve), Bloom's levels addressed, prerequisites (required prior knowledge), estimated time (expected interaction duration), difficulty level, and keywords. This metadata supports discovery, LMS integration, and assessment alignment. Option A describes technical file metadata, option B describes the technical section, and option D confuses metadata with analytics data.

    **Concept Tested:** MicroSim Metadata

    **See:** [MicroSim Metadata Standards](../../glossary.md#microsim-metadata-standards)

---
