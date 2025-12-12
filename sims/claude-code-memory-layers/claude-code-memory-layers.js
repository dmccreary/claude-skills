// Claude Code Memory Layers Infographic
// An interactive visualization showing the 5 memory layers and how they load

// Canvas dimensions
let canvasWidth = 800;
let drawHeight = 550;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;
let margin = 20;
let sliderLeftMargin = 140;
let defaultTextSize = 16;

// Animation state
let animationPhase = 0; // 0-5: loading each layer
let animationProgress = 0;
let isAnimating = false;
let animationSpeed = 2;

// Layer data - ordered by loading priority (highest first)
const layers = [
  {
    id: 0,
    name: "Enterprise Policy",
    priority: "1 (Highest)",
    color: "#e74c3c",
    locations: [
      "macOS: /Library/Application Support/ClaudeCode/CLAUDE.md",
      "Linux: /etc/claude-code/CLAUDE.md",
      "Windows: C:\\Program Files\\ClaudeCode\\CLAUDE.md"
    ],
    purpose: "Organization-wide instructions managed by IT/DevOps",
    examples: ["Company coding standards", "Security policies", "Compliance requirements"],
    sharedWith: "All users in organization",
    exampleRule: "Never commit secrets to git"
  },
  {
    id: 1,
    name: "Project Memory",
    priority: "2",
    color: "#e67e22",
    locations: ["./CLAUDE.md", "./.claude/CLAUDE.md"],
    purpose: "Team-shared instructions for the project",
    examples: ["Project architecture", "Coding standards", "Common workflows"],
    sharedWith: "Team members via source control",
    exampleRule: "Use 4-space indentation"
  },
  {
    id: 2,
    name: "Project Rules",
    priority: "3",
    color: "#f1c40f",
    locations: ["./.claude/rules/*.md"],
    purpose: "Modular, topic-specific project instructions",
    examples: ["Language-specific guidelines", "Testing conventions", "API standards"],
    sharedWith: "Team members via source control",
    exampleRule: "All functions must have JSDoc comments"
  },
  {
    id: 3,
    name: "User Memory",
    priority: "4 (Lowest)",
    color: "#3498db",
    locations: ["~/.claude/CLAUDE.md"],
    purpose: "Personal preferences for all projects",
    examples: ["Code styling preferences", "Personal tooling shortcuts", "Favorite patterns"],
    sharedWith: "Just you (all projects)",
    exampleRule: "Use 2-space indentation"
  },
  {
    id: 4,
    name: "Project Local Memory",
    priority: "N/A (gitignored)",
    color: "#9b59b6",
    locations: ["./CLAUDE.local.md"],
    purpose: "Personal project-specific preferences",
    examples: ["Your sandbox URLs", "Preferred test data", "Local dev settings"],
    sharedWith: "Just you (current project)",
    exampleRule: "My test server: localhost:3001"
  }
];

// Hover state
let hoveredLayer = -1;

// UI elements
let playButton;
let resetButton;
let speedSlider;

// Override example state
let showOverrideExample = false;

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  // Play/Reset buttons
  playButton = createButton('▶ Play Animation');
  playButton.position(10, drawHeight + 12);
  playButton.mousePressed(toggleAnimation);
  playButton.style('font-size', '14px');
  playButton.style('padding', '5px 10px');

  resetButton = createButton('↺ Reset');
  resetButton.position(140, drawHeight + 12);
  resetButton.mousePressed(resetAnimation);
  resetButton.style('font-size', '14px');
  resetButton.style('padding', '5px 10px');

  // Speed slider
  speedSlider = createSlider(0.5, 5, 2, 0.5);
  speedSlider.position(sliderLeftMargin + 120, drawHeight + 15);
  speedSlider.size(canvasWidth - sliderLeftMargin - 300);

  describe('Interactive infographic showing Claude Code memory layers with animation and hover details', LABEL);
}

function draw() {
  updateCanvasSize();

  // Drawing area background
  fill('aliceblue');
  stroke('silver');
  strokeWeight(1);
  rect(0, 0, canvasWidth, drawHeight);

  // Control area background
  fill('white');
  noStroke();
  rect(0, drawHeight, canvasWidth, controlHeight);

  // Title
  fill('#2c3e50');
  textSize(24);
  textAlign(CENTER, TOP);
  noStroke();
  text('Claude Code Memory Layers', canvasWidth / 2, 15);

  textSize(14);
  fill('#7f8c8d');
  text('Hover over layers for details • Higher priority rules override lower ones', canvasWidth / 2, 45);

  // Get speed from slider
  animationSpeed = speedSlider.value();

  // Update animation
  if (isAnimating) {
    animationProgress += animationSpeed;
    if (animationProgress >= 100) {
      animationProgress = 0;
      animationPhase++;
      if (animationPhase > 5) {
        animationPhase = 5;
        isAnimating = false;
        showOverrideExample = true;
        playButton.html('▶ Play Again');
      }
    }
  }

  // Draw the layers
  drawLayers();

  // Draw hover info panel
  if (hoveredLayer >= 0) {
    drawInfoPanel(layers[hoveredLayer]);
  }

  // Draw override example if animation complete
  if (showOverrideExample && animationPhase >= 5) {
    drawOverrideExample();
  }

  // Draw loading indicator
  drawLoadingIndicator();

  // Control labels
  fill('#2c3e50');
  textSize(14);
  textAlign(LEFT, CENTER);
  text('Speed: ' + speedSlider.value().toFixed(1) + 'x', sliderLeftMargin + 130 + speedSlider.width + 10, drawHeight + 25);
}

function drawLayers() {
  const layerHeight = 70;
  const layerSpacing = 8;
  const startY = 80;
  const leftX = 30;
  const layerWidth = canvasWidth * 0.45;

  textAlign(LEFT, CENTER);

  for (let i = 0; i < layers.length; i++) {
    const layer = layers[i];
    const y = startY + i * (layerHeight + layerSpacing);

    // Check hover first
    const isHovered = mouseX >= leftX && mouseX <= leftX + layerWidth &&
                      mouseY >= y && mouseY <= y + layerHeight;

    // Determine visibility based on animation phase
    let alpha = 0;
    let scaleVal = 1;
    let isLowContrast = false;

    if (i < animationPhase) {
      // Fully loaded
      alpha = 255;
      scaleVal = 1;
    } else if (i === animationPhase && isAnimating) {
      // Currently loading
      alpha = map(animationProgress, 0, 100, 80, 255);
      scaleVal = map(animationProgress, 0, 100, 0.95, 1);
    } else if (!isAnimating && animationPhase === 0) {
      // Show all layers with low contrast before animation starts
      alpha = 120;
      scaleVal = 1;
      isLowContrast = true;
    } else {
      // Not yet loaded during animation
      alpha = 60;
      scaleVal = 0.98;
      isLowContrast = true;
    }

    // Boost alpha on hover
    if (isHovered) {
      hoveredLayer = i;
      alpha = 255;
      isLowContrast = false;
    }

    if (alpha > 0) {
      push();

      // Apply scale from center
      const centerX = leftX + layerWidth / 2;
      const centerY = y + layerHeight / 2;
      translate(centerX, centerY);
      scaleVal = constrain(scaleVal, 0.9, 1.1);

      // Layer box with shadow on hover
      if (isHovered) {
        fill(0, 0, 0, 30);
        noStroke();
        rect(-layerWidth/2 * scaleVal + 4, -layerHeight/2 * scaleVal + 4,
             layerWidth * scaleVal, layerHeight * scaleVal, 8);
      }

      // Layer background
      const c = color(layer.color);
      c.setAlpha(alpha);
      fill(c);
      stroke(isHovered ? '#2c3e50' : '#bdc3c7');
      strokeWeight(isHovered ? 3 : 1);
      rect(-layerWidth/2 * scaleVal, -layerHeight/2 * scaleVal,
           layerWidth * scaleVal, layerHeight * scaleVal, 8);

      // Always show layer name (low or high contrast based on state)
      if (isLowContrast) {
        // Low contrast version - just show name centered
        const textAlpha = 180;
        fill(255, 255, 255, textAlpha);
        textSize(18);
        textAlign(CENTER, CENTER);
        textStyle(BOLD);
        text(layer.name, 0, 0);
        textStyle(NORMAL);
      } else {
        // Full contrast version with all details
        // Priority badge
        fill(255, 255, 255, alpha * 0.9);
        noStroke();
        ellipse(-layerWidth/2 * scaleVal + 25, 0, 35, 35);

        fill(0, 0, 0, alpha);
        textSize(12);
        textAlign(CENTER, CENTER);
        text(layer.priority.split(' ')[0], -layerWidth/2 * scaleVal + 25, 0);

        // Layer name
        fill(255, 255, 255, alpha);
        textSize(18);
        textAlign(LEFT, CENTER);
        textStyle(BOLD);
        text(layer.name, -layerWidth/2 * scaleVal + 50, -5);

        // Shared with indicator
        textStyle(NORMAL);
        textSize(12);
        fill(255, 255, 255, alpha * 0.8);
        text('Shared: ' + layer.sharedWith, -layerWidth/2 * scaleVal + 50, 18);
      }

      pop();
    }
  }

  // Reset hover if not over any layer
  if (hoveredLayer >= 0) {
    const layer = layers[hoveredLayer];
    const y = startY + hoveredLayer * (layerHeight + layerSpacing);
    const isStillHovered = mouseX >= leftX && mouseX <= leftX + layerWidth &&
                           mouseY >= y && mouseY <= y + layerHeight;
    if (!isStillHovered) {
      hoveredLayer = -1;
    }
  }
}

function drawInfoPanel(layer) {
  const panelX = canvasWidth * 0.52;
  const panelY = 80;
  const panelWidth = canvasWidth * 0.45;
  const panelHeight = 250;

  // Panel background
  fill(255, 255, 255, 245);
  stroke('#bdc3c7');
  strokeWeight(2);
  rect(panelX, panelY, panelWidth, panelHeight, 10);

  // Header with layer color
  fill(layer.color);
  noStroke();
  rect(panelX, panelY, panelWidth, 40, 10, 10, 0, 0);

  // Layer name in header
  fill(255);
  textSize(18);
  textStyle(BOLD);
  textAlign(LEFT, CENTER);
  text(layer.name, panelX + 15, panelY + 20);

  // Priority badge
  fill(255, 255, 255, 200);
  textSize(12);
  textAlign(RIGHT, CENTER);
  text('Priority: ' + layer.priority, panelX + panelWidth - 15, panelY + 20);

  // Content
  let contentY = panelY + 55;
  textStyle(NORMAL);
  textAlign(LEFT, TOP);

  // Purpose
  fill('#2c3e50');
  textSize(14);
  textStyle(BOLD);
  text('Purpose:', panelX + 15, contentY);
  textStyle(NORMAL);
  textSize(13);
  fill('#34495e');
  text(layer.purpose, panelX + 15, contentY + 18, panelWidth - 30);

  contentY += 50;

  // Locations
  fill('#2c3e50');
  textSize(14);
  textStyle(BOLD);
  text('Location(s):', panelX + 15, contentY);
  textStyle(NORMAL);
  textSize(11);
  fill('#7f8c8d');
  for (let i = 0; i < min(layer.locations.length, 2); i++) {
    text('• ' + layer.locations[i], panelX + 15, contentY + 18 + i * 15);
  }

  contentY += 55;

  // Examples
  fill('#2c3e50');
  textSize(14);
  textStyle(BOLD);
  text('Use Case Examples:', panelX + 15, contentY);
  textStyle(NORMAL);
  textSize(12);
  fill('#34495e');
  for (let i = 0; i < min(layer.examples.length, 3); i++) {
    text('• ' + layer.examples[i], panelX + 15, contentY + 18 + i * 16);
  }

  contentY += 70;

  // Example rule
  fill('#27ae60');
  textSize(12);
  textStyle(ITALIC);
  text('Example rule: "' + layer.exampleRule + '"', panelX + 15, contentY);
  textStyle(NORMAL);
}

function drawOverrideExample() {
  const boxX = canvasWidth * 0.52;
  const boxY = 345;
  const boxWidth = canvasWidth * 0.45;
  const boxHeight = 185;

  // Override example box
  fill(255, 255, 255, 245);
  stroke('#27ae60');
  strokeWeight(2);
  rect(boxX, boxY, boxWidth, boxHeight, 10);

  // Header
  fill('#27ae60');
  noStroke();
  rect(boxX, boxY, boxWidth, 35, 10, 10, 0, 0);

  fill(255);
  textSize(16);
  textStyle(BOLD);
  textAlign(LEFT, CENTER);
  text('Override Example: Indentation Rule', boxX + 15, boxY + 17);

  // Content
  textStyle(NORMAL);
  fill('#2c3e50');
  textSize(13);
  textAlign(LEFT, TOP);

  let y = boxY + 50;

  // User memory (lower priority - crossed out)
  fill('#3498db');
  text('User Memory (Priority 4):', boxX + 15, y);
  fill('#95a5a6');
  textStyle(ITALIC);
  text('"Use 2-space indentation"', boxX + 180, y);

  // Strikethrough line
  stroke('#e74c3c');
  strokeWeight(2);
  line(boxX + 180, y + 8, boxX + boxWidth - 30, y + 8);
  noStroke();

  y += 30;

  // Project memory (higher priority - active)
  textStyle(NORMAL);
  fill('#e67e22');
  text('Project Memory (Priority 2):', boxX + 15, y);
  fill('#27ae60');
  textStyle(BOLD);
  text('"Use 4-space indentation"  ✓', boxX + 190, y);

  y += 35;

  // Result explanation
  textStyle(NORMAL);
  fill('#7f8c8d');
  textSize(12);
  text('Result: Project rule overrides user preference.', boxX + 15, y);
  text('Claude will use 4-space indentation for this project.', boxX + 15, y + 18);

  y += 45;

  // Visual representation
  fill('#ecf0f1');
  stroke('#bdc3c7');
  strokeWeight(1);
  rect(boxX + 15, y, boxWidth - 30, 35, 5);

  fill('#2c3e50');
  textSize(11);
  noStroke();
  textAlign(LEFT, CENTER);
  text('function example() {', boxX + 25, y + 12);
  text('    return true;  // 4 spaces', boxX + 25, y + 25);
  fill('#27ae60');
  text('← Project rule wins', boxX + 200, y + 25);
}

function drawLoadingIndicator() {
  const indicatorX = 30;
  const indicatorY = drawHeight - 60;
  const indicatorWidth = canvasWidth * 0.45;

  // Loading status text
  fill('#2c3e50');
  textSize(14);
  textStyle(BOLD);
  textAlign(LEFT, TOP);

  let statusText = '';
  if (animationPhase === 0 && !isAnimating) {
    statusText = 'Click "Play Animation" to see how rules load';
  } else if (animationPhase < 5) {
    statusText = 'Loading: ' + (animationPhase < layers.length ? layers[animationPhase].name : 'Complete');
  } else {
    statusText = 'All memory layers loaded!';
  }

  text(statusText, indicatorX, indicatorY);
  textStyle(NORMAL);

  // Progress bar background
  fill('#ecf0f1');
  stroke('#bdc3c7');
  strokeWeight(1);
  rect(indicatorX, indicatorY + 22, indicatorWidth, 20, 5);

  // Progress bar fill
  noStroke();
  const totalProgress = (animationPhase * 100 + (isAnimating ? animationProgress : 0)) / 5;
  const progressWidth = map(totalProgress, 0, 100, 0, indicatorWidth - 4);

  // Gradient effect using segments
  for (let i = 0; i < min(animationPhase + 1, 5); i++) {
    const segmentWidth = (indicatorWidth - 4) / 5;
    const segmentX = indicatorX + 2 + i * segmentWidth;
    let segmentFill = segmentWidth;

    if (i === animationPhase && isAnimating) {
      segmentFill = map(animationProgress, 0, 100, 0, segmentWidth);
    } else if (i > animationPhase) {
      segmentFill = 0;
    }

    if (segmentFill > 0) {
      fill(layers[i].color);
      rect(segmentX, indicatorY + 24, segmentFill, 16, i === 0 ? 3 : 0, i === 4 ? 3 : 0, i === 4 ? 3 : 0, i === 0 ? 3 : 0);
    }
  }

  // Progress percentage
  fill('#2c3e50');
  textSize(11);
  textAlign(CENTER, CENTER);
  text(floor(totalProgress) + '%', indicatorX + indicatorWidth / 2, indicatorY + 32);
}

function toggleAnimation() {
  if (animationPhase >= 5) {
    resetAnimation();
  }
  isAnimating = !isAnimating;
  playButton.html(isAnimating ? '⏸ Pause' : '▶ Play Animation');
}

function resetAnimation() {
  animationPhase = 0;
  animationProgress = 0;
  isAnimating = false;
  showOverrideExample = false;
  playButton.html('▶ Play Animation');
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(canvasWidth, canvasHeight);
}

function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) {
    canvasWidth = min(container.offsetWidth, 900);
    if (typeof speedSlider !== 'undefined') {
      speedSlider.size(canvasWidth - sliderLeftMargin - 300);
    }
  }
}
