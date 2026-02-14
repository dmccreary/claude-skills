const stages = [
  { key: 'author', title: '1. Author CSV', tool: 'Spreadsheet', output: 'learning-graph.csv', note: 'ConceptID, ConceptLabel, Dependencies, TaxonomyID' },
  { key: 'validate', title: '2. Validate Structure', tool: 'analyze-graph.py', output: 'quality-metrics.md', note: 'Checks DAG rules and quality metrics' },
  { key: 'taxonomy', title: '3. Analyze Distribution', tool: 'taxonomy-distribution.py', output: 'taxonomy-distribution.md', note: 'Checks category balance and counts' },
  { key: 'convert', title: '4. Convert to JSON', tool: 'csv-to-json.py', output: 'learning-graph.json', note: 'Builds nodes/edges + metadata' },
  { key: 'visualize', title: '5. Visualize Graph', tool: 'Browser + vis-network', output: 'Interactive Graph', note: 'Explore, zoom, filter by taxonomy' }
];

let selected = 0;

function setup() {
  const c = createCanvas(1200, 620);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawStage(i, x, y, w, h) {
  const active = i === selected;
  fill(active ? '#dbeafe' : '#ffffff');
  stroke(active ? '#1d4ed8' : '#94a3b8');
  strokeWeight(active ? 3 : 1.5);
  rect(x, y, w, h, 10);

  noStroke();
  fill('#0f172a');
  textSize(15);
  text(stages[i].title, x + 12, y + 24);
  fill('#334155');
  textSize(12);
  text(`Tool: ${stages[i].tool}`, x + 12, y + 48);
  text(`Output: ${stages[i].output}`, x + 12, y + 68);
}

function drawArrow(x1, y1, x2, y2, colorHex) {
  stroke(colorHex);
  strokeWeight(2);
  line(x1, y1, x2, y2);
  const ang = atan2(y2 - y1, x2 - x1);
  push();
  translate(x2, y2);
  rotate(ang);
  noStroke();
  fill(colorHex);
  triangle(0, 0, -10, 4, -10, -4);
  pop();
}

function draw() {
  background('#f8fafc');
  fill('#0f172a');
  noStroke();
  textSize(22);
  text('Python Learning Graph Processing Pipeline', 16, 30);

  const startX = 20;
  const y = 100;
  const w = 220;
  const h = 120;
  const gap = 16;

  for (let i = 0; i < stages.length; i++) {
    const x = startX + i * (w + gap);
    drawStage(i, x, y, w, h);
    if (i < stages.length - 1) {
      drawArrow(x + w, y + 60, x + w + gap - 6, y + 60, '#1f2937');
    }
  }

  fill('#fff7ed');
  stroke('#fb923c');
  strokeWeight(2);
  rect(20, 270, 780, 150, 10);
  noStroke();
  fill('#9a3412');
  textSize(16);
  text('Quality Feedback Loop', 34, 295);
  fill('#7c2d12');
  textSize(13);
  text('If validation fails or taxonomy is unbalanced, update the CSV and run the pipeline again.', 34, 320);

  drawArrow(360, 270, 130, 238, '#ea580c');
  drawArrow(596, 270, 180, 238, '#ea580c');

  fill('#eff6ff');
  stroke('#3b82f6');
  rect(820, 270, 360, 300, 10);
  noStroke();
  fill('#0f172a');
  textSize(18);
  text('Selected Stage Details', 836, 300);
  fill('#334155');
  textSize(14);
  text(stages[selected].title, 836, 332);
  text(`Tool: ${stages[selected].tool}`, 836, 360);
  text(`Output: ${stages[selected].output}`, 836, 388);
  text(stages[selected].note, 836, 422, 330, 120);

  textSize(12);
  fill('#475569');
  text('Click a stage card to inspect that step.', 836, 552);
}

function mousePressed() {
  const startX = 20;
  const y = 100;
  const w = 220;
  const h = 120;
  const gap = 16;
  for (let i = 0; i < stages.length; i++) {
    const x = startX + i * (w + gap);
    if (mouseX >= x && mouseX <= x + w && mouseY >= y && mouseY <= y + h) {
      selected = i;
      break;
    }
  }
}
