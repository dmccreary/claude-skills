const nodes = [
  ['<!DOCTYPE html>', 40, 70, '#e5e7eb'],
  ['<html>', 80, 130, '#dbeafe'],
  ['<head>', 140, 200, '#fef3c7'],
  ['<body>', 140, 390, '#dcfce7'],
  ['meta/title/script/style', 220, 250, '#fde68a'],
  ['<main>', 220, 440, '#bbf7d0'],
  ['<div id="canvas-container">', 300, 480, '#bfdbfe'],
  ['<aside id="controls">', 300, 525, '#bfdbfe'],
  ['<script> p5.js code', 220, 575, '#fed7aa'],
  ['setup() / draw() / handlers', 320, 620, '#fdba74']
];

const edges = [
  [0,1],[1,2],[1,3],[2,4],[3,5],[5,6],[5,7],[3,8],[8,9]
];

function setup() {
  const c = createCanvas(1220, 700);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawArrow(a, b) {
  stroke('#334155'); strokeWeight(2);
  const x1 = nodes[a][1] + 90, y1 = nodes[a][2] + 28;
  const x2 = nodes[b][1] + 90, y2 = nodes[b][2];
  line(x1, y1, x2, y2);
  push(); translate(x2, y2); const ang = atan2(y2 - y1, x2 - x1); rotate(ang);
  noStroke(); fill('#334155'); triangle(0, 0, -10, 4, -10, -4); pop();
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(24); text('Basic MicroSim Template Structure', 16, 32);

  edges.forEach(([a,b]) => drawArrow(a,b));

  nodes.forEach((n) => {
    const hover = mouseX > n[1] && mouseX < n[1] + 180 && mouseY > n[2] && mouseY < n[2] + 56;
    fill(n[3]); stroke(hover ? '#1d4ed8' : '#94a3b8'); strokeWeight(hover ? 3 : 1.5);
    rect(n[1], n[2], 180, 56, 8);
    noStroke(); fill('#0f172a'); textSize(13); textAlign(CENTER, CENTER); text(n[0], n[1] + 90, n[2] + 28); textAlign(LEFT, BASELINE);
  });

  fill('#334155'); textSize(12);
  text('Document structure (gray), metadata/resources (yellow), layout regions (green/blue), simulation logic (orange).', 16, 686);
}
