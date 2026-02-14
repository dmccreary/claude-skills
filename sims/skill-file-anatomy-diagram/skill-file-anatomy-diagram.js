function setup() {
  const cnv = createCanvas(1000, 620);
  cnv.parent(document.querySelector('main'));
  textFont('Courier New');
}

function drawBox(x, y, w, h, c, lbl) {
  fill(c); stroke('#334155'); strokeWeight(1.5);
  rect(x, y, w, h, 6);
  noStroke(); fill('#0f172a'); textSize(13); text(lbl, x + 10, y + 20);
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); textFont('Arial');
  text('Skill File Anatomy (SKILL.md)', 20, 34);
  textFont('Courier New'); textSize(13);

  drawBox(80, 70, 620, 180, '#fef3c7', 'YAML Frontmatter (machine-readable metadata)');
  fill('#111827');
  text('---', 100, 102);
  text('name: skill-name', 100, 126);
  text('description: One-line purpose of this skill', 100, 150);
  text('license: MIT', 100, 174);
  text('allowed-tools:', 100, 198);
  text('- read', 130, 222); text('- write', 210, 222); text('- bash', 300, 222);
  text('---', 100, 246);

  drawBox(80, 270, 620, 280, '#ffffff', 'Markdown Body (human-readable workflow)');
  fill('#111827');
  text('## Overview', 100, 304);
  text('## When to Use', 100, 336);
  text('## Workflow', 100, 368);
  text('1. Validate inputs', 130, 394);
  text('2. Read required files', 130, 420);
  text('3. Generate/update outputs', 130, 446);
  text('4. Verify and report', 130, 472);
  text('## Resources', 100, 510);

  // Annotation rail
  stroke('#2563eb'); strokeWeight(2); line(740, 80, 740, 540);
  noStroke(); fill('#1e3a8a'); textFont('Arial'); textSize(13);
  text('name: skill invocation id', 760, 122);
  text('description: listed in /skills', 760, 156);
  text('allowed-tools: permission scope', 760, 190);
  text('Workflow section: execution steps', 760, 380);
  text('Resources: references and templates', 760, 514);

  // Connectors
  stroke('#2563eb');
  line(730, 118, 520, 118);
  line(730, 154, 420, 154);
  line(730, 188, 470, 188);
  line(730, 376, 280, 376);
  line(730, 510, 240, 510);
}
