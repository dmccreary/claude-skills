const steps = [
  { title: 'Step 1: Identify Audience Keywords', detail: 'IT professionals and system administrators suggest post-secondary audience.', c: '#dbeafe' },
  { title: 'Step 2: Analyze Prerequisites', detail: 'SQL + ITSM experience rules out junior/senior high levels.', c: '#dcfce7' },
  { title: 'Step 3: Evaluate Depth Indicators', detail: 'Applied modern tech focus is college-level, not research-heavy graduate level.', c: '#f3e8ff' },
  { title: 'Step 4: Determine Reading Level', detail: 'Result: College/University level with practical examples and moderate terminology density.', c: '#fef3c7' }
];
let openStep = 0;

function setup() {
  const c = createCanvas(840, 980);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawStep(s, i, y) {
  const expanded = openStep === i;
  fill(s.c); stroke(expanded ? '#1d4ed8' : '#94a3b8'); strokeWeight(expanded ? 2.5 : 1.2);
  rect(20, y, 800, expanded ? 190 : 90, 10);
  noStroke(); fill('#0f172a'); textSize(18); text(s.title, 34, y + 34);
  textSize(13); fill('#334155'); text(expanded ? s.detail : 'Click to expand details.', 34, y + 62, 770, 110);
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Worked Example: Determine Reading Level', 16, 30);
  fill('#334155'); textSize(13); text('Problem: Determine reading level for "Introduction to Graph Databases for IT Management".', 16, 54);

  fill('#ffffff'); stroke('#cbd5e1'); rect(20, 72, 800, 96, 10);
  noStroke(); fill('#0f172a'); textSize(13);
  text('Target Audience: IT professionals and system administrators\nPrerequisites: relational databases, SQL, IT service management frameworks', 34, 104);

  let y = 188;
  for (let i = 0; i < steps.length; i++) {
    drawStep(steps[i], i, y);
    y += (openStep === i ? 210 : 108);
  }

  fill('#166534'); textSize(18); text('Final Determination: College/University Level', 26, 954);
}

function mousePressed() {
  let y = 188;
  for (let i = 0; i < steps.length; i++) {
    const h = openStep === i ? 190 : 90;
    if (mouseX > 20 && mouseX < 820 && mouseY > y && mouseY < y + h) {
      openStep = openStep === i ? -1 : i;
      return;
    }
    y += (openStep === i ? 210 : 108);
  }
}
