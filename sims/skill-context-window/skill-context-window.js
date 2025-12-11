// Skill Context Window MicroSim
// Demonstrates the three layers of progressive disclosure in Claude Skills:
// Frontmatter Layer -> SKILL.md File Layer -> Assets/Resources Layer

// Canvas dimensions - REQUIRED structure
let canvasWidth = 600;
let drawHeight = 500;
let controlHeight = 25;
let canvasHeight = drawHeight + controlHeight;
let margin = 25;
let defaultTextSize = 16;

// Triangle dimensions
let triangleBase;
let triangleHeight;
let triangleTop;
let triangleBottom;

// Layer boundaries (y-coordinates)
let assetsLayerTop;
let skillFileLayerTop;
let frontmatterLayerTop;

// Hover state
let hoveredLayer = null; // 'assets', 'skillfile', 'frontmatter', or null

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  // Calculate triangle dimensions
  calculateTriangle();

  describe('Skill Context Window visualization showing three layers of progressive disclosure: Frontmatter (always loaded), SKILL.md File (when triggered), and Assets/Resources (as needed)');
}

function draw() {
  updateCanvasSize();

  // Drawing area (white background)
  fill('white');
  rect(0, 0, width, drawHeight);

  // Control area (white background)
  fill('white');
  rect(0, drawHeight, width, controlHeight);

  // Draw the three layers
  drawAssetsLayer();
  drawSkillFileLayer();
  drawFrontmatterLayer();

  // Draw triangle outlines
  drawTriangleOutlines();

  // Place the title at the top
  fill('black');
  textSize(32);
  textAlign(CENTER, BOTTOM);
  noStroke();
  textStyle(NORMAL);
  text('Skill Context Window', canvasWidth/2, margin*2-10);
  textSize(20);
  textStyle(ITALIC); 
  text('The context window is a public good', canvasWidth/2, margin*2+ 10);

  // Reset text settings
  textAlign(LEFT, CENTER);
  textSize(defaultTextSize);

  // Check for hover and draw infobox
  checkHover();
  drawInfoBox();

  // Draw hint text in control area when not hovering
  drawControlAreaHint();
}

function calculateTriangle() {
  triangleBase = canvasWidth - 2 * margin;
  triangleHeight = drawHeight - 80; // Leave room for title
  triangleTop = 60;
  triangleBottom = triangleTop + triangleHeight;

  // Each layer is 1/3 of the triangle height
  frontmatterLayerTop = triangleTop;
  skillFileLayerTop = triangleTop + triangleHeight / 3;
  assetsLayerTop = triangleTop + 2 * triangleHeight / 3;
}

function getTriangleWidthAtY(y) {
  // Calculate the width of the triangle at a given y position
  // Triangle is narrow at top (small y) and wide at bottom (large y)
  let relativeY = y - triangleTop;
  let ratio = relativeY / triangleHeight;
  return triangleBase * ratio;
}

function drawAssetsLayer() {
  // Draw light green background for assets layer (loaded as needed)
  fill('#E8F5E9');
  noStroke();

  // Calculate triangle points for assets layer
  let assetsTop = assetsLayerTop;
  let assetsWidthAtTop = getTriangleWidthAtY(assetsTop);
  let centerX = canvasWidth / 2;

  beginShape();
  vertex(centerX - assetsWidthAtTop / 2, assetsTop);
  vertex(centerX + assetsWidthAtTop / 2, assetsTop);
  vertex(centerX + triangleBase / 2, triangleBottom);
  vertex(centerX - triangleBase / 2, triangleBottom);
  endShape(CLOSE);

  // Draw layer label
  fill('black');
  textSize(18);
  textAlign(CENTER, CENTER);
  noStroke();
  text('Assets, References,', centerX, assetsLayerTop + (triangleBottom - assetsLayerTop) / 2 - 12);
  text('Templates & Scripts', centerX, assetsLayerTop + (triangleBottom - assetsLayerTop) / 2 + 12);

  // Add loading indicator
  textSize(14);
  fill('#2E7D32');
  text('(Loaded as needed)', centerX, assetsLayerTop + (triangleBottom - assetsLayerTop) / 2 + 35);
}

function drawSkillFileLayer() {
  // Draw light blue background for SKILL.md file layer (loaded when triggered)
  fill('#E3F2FD');
  noStroke();

  let centerX = canvasWidth / 2;
  let skillFileWidthAtTop = getTriangleWidthAtY(skillFileLayerTop);
  let assetsWidthAtTop = getTriangleWidthAtY(assetsLayerTop);

  beginShape();
  vertex(centerX - skillFileWidthAtTop / 2, skillFileLayerTop);
  vertex(centerX + skillFileWidthAtTop / 2, skillFileLayerTop);
  vertex(centerX + assetsWidthAtTop / 2, assetsLayerTop);
  vertex(centerX - assetsWidthAtTop / 2, assetsLayerTop);
  endShape(CLOSE);

  // Draw layer label
  fill('black');
  textSize(18);
  textAlign(CENTER, CENTER);
  noStroke();
  text('SKILL.md File', centerX, skillFileLayerTop + (assetsLayerTop - skillFileLayerTop) / 2 - 8);

  // Add loading indicator
  textSize(14);
  fill('#1565C0');
  text('(When skill triggers)', centerX, skillFileLayerTop + (assetsLayerTop - skillFileLayerTop) / 2 + 15);
}

function drawFrontmatterLayer() {
  // Draw light yellow background for frontmatter layer (always loaded)
  fill('#FFF9C4');
  noStroke();

  let centerX = canvasWidth / 2;
  let skillFileWidthAtTop = getTriangleWidthAtY(skillFileLayerTop);

  beginShape();
  vertex(centerX, frontmatterLayerTop);
  vertex(centerX + skillFileWidthAtTop / 2, skillFileLayerTop);
  vertex(centerX - skillFileWidthAtTop / 2, skillFileLayerTop);
  endShape(CLOSE);

  // Draw layer label
  fill('black');
  textSize(18);
  textAlign(CENTER, CENTER);
  noStroke();
  text('SKILL.md Frontmatter', centerX, frontmatterLayerTop + (skillFileLayerTop - frontmatterLayerTop) / 2 - 8 + 50);

  // Add loading indicator
  textSize(14);
  fill('#F57F17');
  text('(Always in context)', centerX, frontmatterLayerTop + (skillFileLayerTop - frontmatterLayerTop) / 2 + 15 + 43);
}

function drawTriangleOutlines() {
  // Draw outlines for the triangle sections
  stroke('#757575');
  strokeWeight(2);
  noFill();

  let centerX = canvasWidth / 2;

  // Outer triangle
  triangle(
    centerX, triangleTop,
    centerX - triangleBase / 2, triangleBottom,
    centerX + triangleBase / 2, triangleBottom
  );

  // Lines separating layers
  let skillFileWidth = getTriangleWidthAtY(skillFileLayerTop);
  let assetsWidth = getTriangleWidthAtY(assetsLayerTop);

  line(centerX - skillFileWidth / 2, skillFileLayerTop, centerX + skillFileWidth / 2, skillFileLayerTop);
  line(centerX - assetsWidth / 2, assetsLayerTop, centerX + assetsWidth / 2, assetsLayerTop);
}

function checkHover() {
  if (mouseX >= 0 && mouseX <= canvasWidth && mouseY >= triangleTop && mouseY <= triangleBottom) {
    if (isPointInAssetsLayer(mouseX, mouseY)) {
      hoveredLayer = 'assets';
    } else if (isPointInSkillFileLayer(mouseX, mouseY)) {
      hoveredLayer = 'skillfile';
    } else if (isPointInFrontmatterLayer(mouseX, mouseY)) {
      hoveredLayer = 'frontmatter';
    } else {
      hoveredLayer = null;
    }
  } else {
    hoveredLayer = null;
  }
}

function isPointInAssetsLayer(x, y) {
  if (y < assetsLayerTop || y > triangleBottom) return false;

  let centerX = canvasWidth / 2;
  let widthAtY = getTriangleWidthAtY(y);
  let leftEdge = centerX - widthAtY / 2;
  let rightEdge = centerX + widthAtY / 2;

  return x >= leftEdge && x <= rightEdge;
}

function isPointInSkillFileLayer(x, y) {
  if (y < skillFileLayerTop || y > assetsLayerTop) return false;

  let centerX = canvasWidth / 2;
  let widthAtY = getTriangleWidthAtY(y);
  let leftEdge = centerX - widthAtY / 2;
  let rightEdge = centerX + widthAtY / 2;

  return x >= leftEdge && x <= rightEdge;
}

function isPointInFrontmatterLayer(x, y) {
  if (y < frontmatterLayerTop || y > skillFileLayerTop) return false;

  let centerX = canvasWidth / 2;
  let widthAtY = getTriangleWidthAtY(y);
  let leftEdge = centerX - widthAtY / 2;
  let rightEdge = centerX + widthAtY / 2;

  return x >= leftEdge && x <= rightEdge;
}

function drawInfoBox() {
  if (hoveredLayer === null) return;

  // Define infobox content based on hovered layer
  let title = '';
  let content = '';
  let sizeInfo = '';

  if (hoveredLayer === 'frontmatter') {
    title = 'SKILL.md Frontmatter';
    content = 'Name and description metadata (~100 words / ~130 tokens). Always loaded into context when Claude starts. This allows Claude to decide when to invoke the skill based on user requests.';
    sizeInfo = 'Size: ~100 words (~130 tokens) | Loading: At startup';
  } else if (hoveredLayer === 'skillfile') {
    title = 'SKILL.md File';
    content = 'Complete skill instructions and workflows (<5k words / ~6.5k tokens). Loaded when the skill is triggered or invoked. Contains detailed procedural knowledge, step-by-step instructions, and usage examples.';
    sizeInfo = 'Size: <5k words (~6.5k tokens) | Loading: When triggered';
  } else if (hoveredLayer === 'assets') {
    title = 'Assets, References, Templates & Scripts';
    content = 'Bundled resources loaded as needed. Scripts can be executed without loading into context. References and templates are loaded when Claude determines they are needed for the task. This provides unlimited extensibility.';
    sizeInfo = 'Size: Unlimited* | Loading: As needed';
  }

  // Calculate box dimensions
  let boxWidth = 380;
  let boxHeight = 160;
  let boxX = mouseX + 15;
  let boxY = mouseY + 15;

  // Keep box on screen
  if (boxX + boxWidth > canvasWidth - 10) {
    boxX = mouseX - boxWidth - 15;
  }
  if (boxY + boxHeight > drawHeight - 10) {
    boxY = mouseY - boxHeight - 15;
  }

  // Draw box background with shadow effect
  fill(0, 0, 0, 30);
  noStroke();
  rect(boxX + 4, boxY + 4, boxWidth, boxHeight, 8);

  // Draw main box with border
  fill(255, 255, 255, 250);
  stroke(100);
  strokeWeight(2);
  rect(boxX, boxY, boxWidth, boxHeight, 8);

  // Draw title bar with color based on layer
  if (hoveredLayer === 'frontmatter') {
    fill('#F57F17'); // Yellow-orange
  } else if (hoveredLayer === 'skillfile') {
    fill('#1565C0'); // Blue
  } else if (hoveredLayer === 'assets') {
    fill('#2E7D32'); // Green
  }
  noStroke();
  rect(boxX, boxY, boxWidth, 35, 8, 8, 0, 0);

  // Draw title text
  fill(255);
  textSize(16);
  textAlign(LEFT, CENTER);
  textStyle(BOLD);
  text(title, boxX + 12, boxY + 18);

  // Draw content text with word wrapping
  fill(50);
  textSize(14);
  textStyle(NORMAL);
  textAlign(LEFT, TOP);

  let words = content.split(' ');
  let line = '';
  let yPos = boxY + 45;
  let maxWidth = boxWidth - 24;

  for (let word of words) {
    let testLine = line + word + ' ';
    let testWidth = textWidth(testLine);

    if (testWidth > maxWidth && line.length > 0) {
      text(line, boxX + 12, yPos);
      line = word + ' ';
      yPos += 18;
    } else {
      line = testLine;
    }
  }
  text(line, boxX + 12, yPos);

  // Draw size info at bottom
  yPos += 25;
  fill(100);
  textSize(12);
  textStyle(ITALIC);
  text(sizeInfo, boxX + 12, yPos);
}

function drawControlAreaHint() {
  if (hoveredLayer === null) {
    fill('#666');
    textSize(14);
    textAlign(CENTER, CENTER);
    textStyle(ITALIC);
    noStroke();
    text('Hover over region to see details', canvasWidth / 2, drawHeight + controlHeight / 2);
  }
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(canvasWidth, canvasHeight);
  calculateTriangle();
}

function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) {
    canvasWidth = container.offsetWidth;
  }
}
