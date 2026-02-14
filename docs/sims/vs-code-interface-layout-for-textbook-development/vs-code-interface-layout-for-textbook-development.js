let selected = 'Explorer';
const panes = [
  ['Explorer', 20, 90, 180, 500, '#dbeafe'],
  ['Editor', 210, 90, 520, 500, '#ffffff'],
  ['Terminal', 210, 600, 520, 120, '#111827'],
  ['Outline', 740, 90, 240, 240, '#dcfce7'],
  ['Preview', 740, 340, 240, 250, '#fef3c7']
];

function setup() {
  const c = createCanvas(1000, 760);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('VS Code Interface Layout for Textbook Development', 16, 32);

  fill('#1f2937'); rect(16, 52, 968, 28, 8);
  fill('#e5e7eb'); textSize(12); text('claude-skills - Visual Studio Code', 28, 70);

  panes.forEach((p) => {
    const hover = mouseX > p[1] && mouseX < p[1] + p[2] && mouseY > p[3] && mouseY < p[3] + p[4];
    fill(p[5]); stroke(hover ? '#1d4ed8' : '#cbd5e1'); strokeWeight(hover ? 2.5 : 1.2); rect(p[1], p[3], p[2], p[4], 8);
    noStroke(); fill(p[0] === 'Terminal' ? '#a7f3d0' : '#0f172a'); textSize(14); text(p[0], p[1] + 10, p[3] + 22);
    if (hover) selected = p[0];
  });

  fill('#334155'); textSize(12);
  text('Hover panes to inspect layout role. Recommended flow: Explorer -> Editor -> Terminal -> Preview.', 20, 744);

  fill('#ffffff'); stroke('#cbd5e1'); rect(20, 600, 180, 120, 8);
  noStroke(); fill('#0f172a'); textSize(14); text('Selected Pane', 30, 624);
  textSize(18); fill('#1e3a8a'); text(selected, 30, 656);
}
