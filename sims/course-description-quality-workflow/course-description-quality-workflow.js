// Course Description Quality Impact on Workflow Infographic
// Interactive p5.js visualization showing how quality affects the textbook generation workflow

// Canvas dimensions
let canvasWidth = 800;
let drawHeight = 680;
let controlHeight = 100;
let canvasHeight = drawHeight + controlHeight;
let margin = 20;
let defaultTextSize = 16;

// Data variables
let infographicData;
let nodes = [];
let edges = [];
let groups = {};
let hoveredNode = null;

function preload() {
  infographicData = loadJSON('data.json');
}

function setup() {
  updateCanvasSize();
  const canvas = createCanvas(canvasWidth, canvasHeight);
  canvas.parent(document.querySelector('main'));

  // Parse data
  parseData();

  describe('Interactive infographic showing how course description quality affects the intelligent textbook generation workflow', LABEL);
}

function draw() {
  updateCanvasSize();

  // Drawing area background
  fill('aliceblue');
  rect(0, 0, width, drawHeight);

  // Detail display area background
  fill('white');
  rect(0, drawHeight, width, controlHeight);

  // Draw edges first (behind nodes)
  drawEdges();

  // Draw nodes
  drawNodes();

  // Draw tooltip if hovering over a node
  drawTooltip();

  // Draw detail panel for hovered node
  drawDetailPanel();

  // Draw annotations
  drawAnnotations();
}

function parseData() {
  // Parse groups
  if (infographicData.groups) {
    groups = infographicData.groups;
  }

  // Parse nodes
  nodes = infographicData.nodes.map(n => ({
    id: n.id,
    label: n.label || '',
    x: n.x || 0,
    y: n.y || 0,
    group: n.group || 'default',
    shortDescription: n.shortDescription || '',
    fullDescription: n.fullDescription || '',
    shape: n.shape || (groups[n.group]?.shape || 'ellipse'),
    color: n.color || (groups[n.group]?.color || '#97C2FC'),
    borderColor: n.borderColor || (groups[n.group]?.borderColor || '#2B7CE9'),
    borderWidth: n.borderWidth || 2,
    size: n.size || 60,
    icon: n.icon || null
  }));

  // Parse edges
  edges = infographicData.edges.map(e => ({
    from: e.from,
    to: e.to,
    label: e.label || '',
    color: e.color || '#848484',
    width: e.width || 1,
    dashes: e.dashes || false,
    smooth: e.smooth || { type: 'continuous', roundness: 0.5 }
  }));
}

function drawNodes() {
  hoveredNode = null;

  for (let node of nodes) {
    // Check if mouse is hovering over this node
    let d = dist(mouseX, mouseY, node.x, node.y);
    let isHovered = d < node.size;

    if (isHovered && mouseY < drawHeight) {
      hoveredNode = node;
    }

    // Draw node shape
    push();
    stroke(node.borderColor);
    strokeWeight(isHovered ? node.borderWidth + 2 : node.borderWidth);
    fill(node.color);

    if (node.shape === 'ellipse' || node.shape === 'circle') {
      ellipse(node.x, node.y, node.size * 2);
    } else if (node.shape === 'box' || node.shape === 'square') {
      rectMode(CENTER);
      rect(node.x, node.y, node.size * 3, node.size * 1.4, 5);
    } else if (node.shape === 'diamond') {
      drawDiamond(node.x, node.y, node.size);
    }

    pop();

    // Draw label
    fill(0);
    noStroke();
    textAlign(CENTER, CENTER);
    textSize(13);
    textStyle(BOLD);

    // Handle multi-line labels
    let lines = node.label.split('\n');
    let startY = node.y - ((lines.length - 1) * 8);
    for (let i = 0; i < lines.length; i++) {
      text(lines[i], node.x, startY + i * 16);
    }
    textStyle(NORMAL);
  }
}

function drawDiamond(x, y, size) {
  beginShape();
  vertex(x, y - size);           // top
  vertex(x + size, y);           // right
  vertex(x, y + size);           // bottom
  vertex(x - size, y);           // left
  endShape(CLOSE);
}

function drawEdges() {
  for (let edge of edges) {
    let fromNode = nodes.find(n => n.id === edge.from);
    let toNode = nodes.find(n => n.id === edge.to);

    if (!fromNode || !toNode) continue;

    push();
    stroke(edge.color);
    strokeWeight(edge.width);

    if (edge.dashes) {
      drawingContext.setLineDash([5, 5]);
    }

    // Draw arrow line
    drawArrow(fromNode.x, fromNode.y, toNode.x, toNode.y, edge.color);

    drawingContext.setLineDash([]);
    pop();

    // Draw edge label if exists
    if (edge.label) {
      let midX = (fromNode.x + toNode.x) / 2;
      let midY = (fromNode.y + toNode.y) / 2;

      // Background for label
      push();
      fill(255, 255, 255, 200);
      noStroke();
      let labelWidth = textWidth(edge.label) + 10;
      rectMode(CENTER);
      rect(midX, midY, labelWidth, 20, 3);
      pop();

      // Label text
      fill(50);
      noStroke();
      textAlign(CENTER, CENTER);
      textSize(11);
      textStyle(BOLD);
      text(edge.label, midX, midY);
      textStyle(NORMAL);
    }
  }
}

function drawArrow(x1, y1, x2, y2, arrowColor) {
  // Draw line
  line(x1, y1, x2, y2);

  // Calculate arrow head
  let angle = atan2(y2 - y1, x2 - x1);
  let arrowSize = 10;

  push();
  translate(x2, y2);
  rotate(angle);
  fill(arrowColor);
  noStroke();
  triangle(0, 0, -arrowSize, -arrowSize/2, -arrowSize, arrowSize/2);
  pop();
}

function drawTooltip() {
  if (!hoveredNode || mouseY >= drawHeight) return;

  let tooltipText = hoveredNode.shortDescription;
  if (!tooltipText) return;

  // Measure tooltip dimensions
  textSize(13);
  let tooltipWidth = min(textWidth(tooltipText) + 20, 300);
  let tooltipHeight = 30;
  let padding = 10;

  // Position tooltip near mouse, but keep within drawing bounds
  let tooltipX = mouseX + 15;
  let tooltipY = mouseY - 20;

  // Adjust if tooltip would go off right edge
  if (tooltipX + tooltipWidth > width - padding) {
    tooltipX = mouseX - tooltipWidth - 15;
  }

  // Adjust if tooltip would go off left edge
  if (tooltipX < padding) {
    tooltipX = padding;
  }

  // Adjust if tooltip would go off top edge
  if (tooltipY < padding) {
    tooltipY = mouseY + 20;
  }

  // Adjust if tooltip would go off bottom of drawing area
  if (tooltipY + tooltipHeight > drawHeight - padding) {
    tooltipY = drawHeight - tooltipHeight - padding;
  }

  // Draw tooltip background
  push();
  fill(255, 255, 220);
  stroke(100);
  strokeWeight(1);
  rect(tooltipX, tooltipY, tooltipWidth, tooltipHeight, 5);

  // Draw tooltip text
  fill(0);
  noStroke();
  textAlign(LEFT, CENTER);
  textSize(13);
  text(tooltipText, tooltipX + 10, tooltipY + tooltipHeight / 2);
  pop();
}

function drawDetailPanel() {
  push();
  fill(0);
  noStroke();
  textAlign(LEFT, TOP);
  textSize(defaultTextSize);

  let panelX = margin;
  let panelY = drawHeight + 10;
  let panelWidth = width - 2 * margin;

  if (hoveredNode) {
    // Display node label as header
    textSize(18);
    textStyle(BOLD);
    text(hoveredNode.label.replace(/\n/g, ' '), panelX, panelY);

    // Display full description
    textSize(14);
    textStyle(NORMAL);

    // Strip HTML tags for display
    let displayText = hoveredNode.fullDescription.replace(/<[^>]*>/g, '');

    // Wrap text to fit panel width
    let words = displayText.split(' ');
    let line = '';
    let y = panelY + 28;

    for (let word of words) {
      let testLine = line + word + ' ';
      if (textWidth(testLine) > panelWidth && line.length > 0) {
        text(line, panelX, y);
        line = word + ' ';
        y += 18;
        if (y > drawHeight + controlHeight - 20) break; // Prevent overflow
      } else {
        line = testLine;
      }
    }
    if (y <= drawHeight + controlHeight - 20) {
      text(line, panelX, y);
    }
  } else {
    // Default message when nothing is hovered
    textStyle(ITALIC);
    fill(100);
    textSize(14);
    text('Hover over any node to see detailed information...', panelX, panelY);
  }

  pop();
}

function drawAnnotations() {
  push();
  textAlign(CENTER, CENTER);
  textSize(11);
  fill(80);
  textStyle(ITALIC);

  // Top annotation
  text('Quality threshold: 70+ acceptable, 85+ excellent', width/2, 25);

  // Bottom annotation
  text('Investing time in course description quality pays exponential dividends', width/2, drawHeight - 15);

  pop();
}

function windowResized() {
  updateCanvasSize();
  resizeCanvas(canvasWidth, canvasHeight);
}

function updateCanvasSize() {
  const container = document.querySelector('main');
  if (container) {
    canvasWidth = container.offsetWidth;
  }
}
