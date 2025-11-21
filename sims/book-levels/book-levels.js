// Five Levels of Intelligent Textbooks Infographics (Updated)
// Adds a red dashed rectangle around the top three layers with a label "Highly Regulated Textbooks".
// Responsive design retained.

let containerWidth; // calculated by container
let containerHeight = 500; // fixed height on page
let canvasWidth = 500;

// Variables for the stair diagram
let layers = [];
let descriptions = [];
let currentHover = -1;
let m; // margins around the steps
let mt; // margin from the top
let sw; // next step width
let step_width; // total step width
let sh; // step height

function setup() {
    // Create a canvas to match the parent container's size
    updateCanvasSize();
    const canvas = createCanvas(containerWidth, containerHeight);
    const mainElement = document.querySelector('main');
    canvas.parent(mainElement);

    // Initialize the layout
    updateLayout();

    // Define the descriptions
    descriptions = [
        "Level 1: Static Textbooks are traditional printed or digital formats with no interactive elements. They are composed purely of text and static images, with fixed content that doesn't adapt to the learner. Over 90% of textbooks used by college students today remain at Level 1. They're suitable for simple content delivery where interaction isn't necessary.",
        "Level 2: Interactive Content Textbooks incorporate digital elements that engage readers beyond passive consumption. Features include keyword search, hyperlinks, embedded videos, simple quizzes, AI-generated MicroSims, detailed glossary, social sharing compatibility, and usage analytics. These textbooks are cost-effective enhancements that improve engagement with multimedia elements.",
        "Level 3: Adaptive Textbooks dynamically adjust content based on user input, performance, and behavior. They use personalized learning pathways through deterministic rules, concept graph traversal algorithms, content selection based on assessment performance, and continuous recording of concept mastery. Implementation requires data management systems, graph algorithms, and raises privacy considerations.",
        "Level 4: Textbooks with Chatbots integrate intelligent conversational interfaces providing real-time assistance. They use Large Language Models (LLMs) as tutoring assistants, employ GraphRAG architecture combining multiple AI technologies, and provide real-time feedback on student questions. These systems can balance between powerful LLMs and cost-effective smaller models for privacy and efficiency.",
        "Level 5: Autonomous AI Textbooks represent the future of educational content where AI-driven systems fully understand individual learner needs and autonomously generate personalized learning experiences. They feature deep understanding of student knowledge, real-time generation of customized lessons, complete adaptability to learning styles, and human-like tutoring capabilities. This level remains aspirational, requiring advanced hardware and more reliable LLMs."
    ];
}

function updateLayout() {
    // Calculate responsive dimensions based on container width
    m = max(10, containerWidth * 0.03); // margins around the steps
    mt = 60; // margin from the top is fixed

    // Adjust step sizes based on container width
    if (containerWidth < 400) {
        sw = 30; // next step width for small screens
        step_width = 70; // total step width for small screens
        sh = 50; // step height for small screens
    } else if (containerWidth < 600) {
        sw = 40; // next step width for medium screens
        step_width = 90; // total step width for medium screens
        sh = 55; // step height for medium screens
    } else {
        sw = 60; // next step width for large screens
        step_width = 120; // total step width for large screens
        sh = 60; // step height for large screens
    }

    // Define the layers and labels
    layers = [
        {x: m,      y: sh*4+mt, w: canvasWidth - sw,   h: sh, level: "Level 1 - Static Textbooks", color: "red",    tcolor: "white" },
        {x: sw+m,   y: sh*3+mt, w: canvasWidth - sw*2, h: sh, level: "Level 2 - Interactive Content", color: "#4682B4", tcolor: "white" },
        {x: sw*2+m, y: sh*2+mt, w: canvasWidth - sw*3, h: sh, level: "Level 3 - Adaptive Textbooks", color: "#20B2AA", tcolor: "white" },
        {x: sw*3+m, y: sh*1+mt, w: canvasWidth - sw*4, h: sh, level: "L4 - Chatbot Integration",    color: "#9370DB", tcolor: "white" },
        {x: sw*4+m, y: mt,      w: canvasWidth - sw*5, h: sh, level: "L5 - Autonomous AI",         color: "gold",    tcolor: "black" }
    ];

    // Shorten labels for very small screens
    if (containerWidth < 500) {
        layers[0].level = "L1 - Static";
        layers[1].level = "L2 - Interactive";
        layers[2].level = "L3 - Adaptive";
        layers[3].level = "L4 - Chatbots";
        layers[4].level = "L5 - AI";
    }
}

function draw() {
    background('aliceblue');

    // Title
    const titleSize = constrain(containerWidth * 0.035, 16, 22);
    textSize(titleSize);
    textAlign(CENTER, TOP);
    fill(0);
    noStroke();
    text("The Five Levels of Intelligent Textbooks", width / 2, 10);

    // Step text size
    const stepTextSize = constrain(containerWidth * 0.03, 12, 24);
    textSize(stepTextSize);
    textAlign(CENTER, CENTER);

    // Draw layers
    for (let i = 0; i < layers.length; i++) {
        const l = layers[i];
        fill(l.color);

        if (i === currentHover) {
            stroke('blue');
            strokeWeight(4);
        } else {
            noStroke();
        }

        rect(l.x, l.y, l.w, l.h - 2);
        fill(l.tcolor);
        noStroke();
        text(l.level, l.x + l.w / 2, l.y + l.h / 2);
    }

    // --- New Feature: Red dashed rectangle around top three layers ---
    const left   = layers[2].x;
    const topR   = layers[4].y;
    const right  = layers[2].x + layers[2].w;
    const bottom = layers[2].y + layers[2].h - 2;
    const rectW  = right - left;
    const rectH  = bottom - topR;

    push();
    noFill();
    stroke('red');
    strokeWeight(2);
    drawingContext.setLineDash([8, 5]); // Dash pattern
    rect(left - 4, topR - 4, rectW + 8, rectH + 8);
    drawingContext.setLineDash([]); // Reset dash
    pop();

    // Label for the new rectangle
    const labelSize = constrain(containerWidth * 0.025, 12, 18);
    textSize(labelSize);
    fill('red');
    noStroke();
    textAlign(CENTER, BOTTOM);
    text("Highly Regulated Textbooks", left + rectW / 2, topR - 6);

    // Description area position
    const descriptionY = sh * 5 + mt + 10;

    // Display description text
    if (currentHover !== -1) {
        const descTextSize = constrain(containerWidth * 0.025, 11, 16);
        textSize(descTextSize);
        fill(0);
        textAlign(LEFT, TOP);
        noStroke();

        const descWidth = containerWidth - 40;
        text(descriptions[currentHover], 20, descriptionY, descWidth, 200);
    } else {
        const defaultTextSize = constrain(containerWidth * 0.03, 14, 18);
        textSize(defaultTextSize);
        fill(0);
        textAlign(CENTER, CENTER);
        text("Hover over a level to see details", width / 2, descriptionY + 30);
    }
}

function mouseMoved() {
    currentHover = -1;
    for (let i = 0; i < layers.length; i++) {
        const l = layers[i];
        if (mouseX >= l.x && mouseX <= l.x + l.w && mouseY >= l.y && mouseY <= l.y + l.h) {
            currentHover = i;
            break;
        }
    }
}

function touchStarted() {
    for (let i = 0; i < layers.length; i++) {
        const l = layers[i];
        if (mouseX >= l.x && mouseX <= l.x + l.w && mouseY >= l.y && mouseY <= l.y + l.h) {
            currentHover = i;
            return false; // Prevent default
        }
    }
    return false;
}

function windowResized() {
    updateCanvasSize();
    updateLayout();
    resizeCanvas(containerWidth, containerHeight);
    redraw();
}

function updateCanvasSize() {
    const container = document.querySelector('main').getBoundingClientRect();
    containerWidth = Math.floor(container.width);
    canvasWidth = containerWidth;
}
