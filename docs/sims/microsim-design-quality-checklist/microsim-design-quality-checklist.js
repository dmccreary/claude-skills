const groups = [
  { t: 'Learning Design', items: ['Clear objective', 'Bloom alignment', 'Concept focus'] },
  { t: 'Interaction', items: ['Immediate feedback', 'Controls intuitive', 'Reset behavior'] },
  { t: 'Accessibility', items: ['Readable text', 'Color contrast', 'Keyboard-friendly'] },
  { t: 'Technical', items: ['No console errors', 'Responsive embed', 'Fast render'] },
  { t: 'Assessment', items: ['Guided exploration', 'Misconception checks', 'Exportable results'] }
];

let checks = [];

function setup() {
  const c = createCanvas(1000, 760);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  let y = 90;
  groups.forEach((g, gi) => {
    g.items.forEach((it, ii) => checks.push({ gi, ii, it, x: 36 + (gi % 2) * 480, y: y + ii * 36 + floor(gi / 2) * 190, on: false }));
  });
}

function summary() {
  const total = checks.length;
  const done = checks.filter((c) => c.on).length;
  return { total, done, pct: round((done / total) * 100) };
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('MicroSim Design Quality Checklist', 16, 32);

  for (let gi = 0; gi < groups.length; gi++) {
    const x = 20 + (gi % 2) * 480;
    const y = 60 + floor(gi / 2) * 190;
    fill('#e2e8f0'); stroke('#cbd5e1'); rect(x, y, 460, 170, 10);
    noStroke(); fill('#1e3a8a'); textSize(16); text(groups[gi].t, x + 12, y + 24);
  }

  checks.forEach((c) => {
    const hover = mouseX > c.x && mouseX < c.x + 360 && mouseY > c.y && mouseY < c.y + 28;
    fill(hover ? '#eef2ff' : '#ffffff'); stroke('#cbd5e1'); rect(c.x, c.y, 360, 28, 6);
    noStroke(); fill(c.on ? '#16a34a' : '#94a3b8'); textSize(15); text(c.on ? '☑' : '☐', c.x + 8, c.y + 19);
    fill('#0f172a'); textSize(13); text(c.it, c.x + 32, c.y + 19);
  });

  const s = summary();
  fill('#e2e8f0'); noStroke(); rect(20, 726, 960, 20, 8);
  fill('#22c55e'); rect(20, 726, 960 * (s.pct / 100), 20, 8);
  fill('#0f172a'); textSize(12); text(`Progress: ${s.done}/${s.total} (${s.pct}%)`, 28, 740);
}

function mousePressed() {
  checks.forEach((c) => {
    if (mouseX > c.x && mouseX < c.x + 360 && mouseY > c.y && mouseY < c.y + 28) c.on = !c.on;
  });
}
