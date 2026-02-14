let cards = [
  ['ls', 'List files', 'ls -la'],
  ['cd', 'Change directory', 'cd docs/chapters'],
  ['pwd', 'Print working directory', 'pwd'],
  ['mkdir', 'Create directory', 'mkdir new-chapter'],
  ['cat', 'Read file', 'cat index.md'],
  ['python', 'Run script', 'python analyze-graph.py in.csv out.md']
];

function setup() {
  const c = createCanvas(980, 760);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawTerminal(x, y, w, h) {
  fill('#111827'); stroke('#0f172a'); rect(x, y, w, h, 10);
  fill('#1f2937'); noStroke(); rect(x, y, w, 34, 10, 10, 0, 0);
  fill('#ef4444'); circle(x + 16, y + 17, 9);
  fill('#f59e0b'); circle(x + 32, y + 17, 9);
  fill('#10b981'); circle(x + 48, y + 17, 9);

  fill('#e5e7eb'); textSize(13); text('Terminal - /docs/learning-graph', x + 62, y + 22);
  fill('#a7f3d0'); textSize(15); text('user@macbook learning-graph % python analyze-graph.py learning-graph.csv quality-metrics.md', x + 16, y + 62, w - 30, 80);
  fill('#86efac'); textSize(14); text('✓ Analysis complete: quality score = 88\n✓ Output written to quality-metrics.md', x + 16, y + 112);
}

function drawPatterns(x, y) {
  fill('#0f172a'); textSize(18); text('Command Syntax Patterns', x, y);
  const p = [
    ['command', 'ls'],
    ['command -flag', 'ls -la'],
    ['command arg', 'cd docs/chapters'],
    ['command -flag arg1 arg2', 'python script.py in.csv out.md']
  ];
  for (let i = 0; i < p.length; i++) {
    fill('#ffffff'); stroke('#cbd5e1'); rect(x, y + 14 + i * 46, 440, 40, 8);
    noStroke(); fill('#1e3a8a'); textSize(13); text(p[i][0], x + 12, y + 38 + i * 46);
    fill('#334155'); text(p[i][1], x + 190, y + 38 + i * 46);
  }
}

function drawGrid(x, y) {
  fill('#0f172a'); textSize(18); text('Essential Commands for Textbook Workflow', x, y);
  for (let i = 0; i < cards.length; i++) {
    const cx = x + (i % 3) * 308;
    const cy = y + 16 + Math.floor(i / 3) * 112;
    const hover = mouseX > cx && mouseX < cx + 290 && mouseY > cy && mouseY < cy + 98;
    fill(hover ? '#dbeafe' : '#ffffff'); stroke('#cbd5e1'); rect(cx, cy, 290, 98, 8);
    noStroke(); fill('#1e40af'); textSize(18); text(cards[i][0], cx + 12, cy + 30);
    fill('#334155'); textSize(12); text(cards[i][1], cx + 12, cy + 52);
    text(cards[i][2], cx + 12, cy + 74, 270, 30);
  }
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Command-Line Interface Basics', 16, 30);
  drawTerminal(16, 46, 948, 180);
  drawPatterns(16, 252);
  drawGrid(16, 468);
}
