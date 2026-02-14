const sections = [
  { title: 'Core Files', items: ['SKILL.md', 'README.md', 'LICENSE'] },
  { title: 'Supporting Assets', items: ['scripts/', 'templates/', 'references/', 'examples/'] },
  { title: 'Documentation', items: ['INSTALL.md', 'usage examples', 'troubleshooting', 'changelog'] },
  { title: 'Testing & Quality', items: ['test cases', 'validation scripts', 'benchmarks'] },
  { title: 'Dependencies', items: ['requirements.txt', 'external tools', 'min Claude version'] },
  { title: 'Distribution', items: ['version number', 'git tag', 'archive package'] }
];

let boxes = [];

function setup() {
  const c = createCanvas(1000, 640);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  let y = 86;
  sections.forEach((s, si) => {
    s.items.forEach((it, ii) => {
      boxes.push({ s: si, i: ii, label: it, checked: si < 2, x: 40 + (si % 2) * 480, y: y + ii * 32 + Math.floor(si / 2) * 180 });
    });
  });
}

function progress() {
  const total = boxes.length;
  const done = boxes.filter((b) => b.checked).length;
  return { done, total, pct: Math.round((done / total) * 100) };
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); noStroke(); textSize(22); text('Skill Package Contents Checklist', 16, 30);

  for (let si = 0; si < sections.length; si++) {
    const x = 24 + (si % 2) * 480;
    const y = 60 + Math.floor(si / 2) * 180;
    fill('#dbeafe'); rect(x, y, 460, 160, 10);
    fill('#1e3a8a'); textSize(16); text(sections[si].title, x + 12, y + 24);
  }

  boxes.forEach((b) => {
    const hover = mouseX > b.x && mouseX < b.x + 380 && mouseY > b.y && mouseY < b.y + 24;
    fill(hover ? '#eef2ff' : '#ffffff'); stroke('#94a3b8'); rect(b.x, b.y, 380, 24, 5);
    noStroke(); fill(b.checked ? '#16a34a' : '#94a3b8'); textSize(14); text(b.checked ? '☑' : '☐', b.x + 8, b.y + 16);
    fill('#0f172a'); textSize(13); text(b.label, b.x + 30, b.y + 16);
  });

  const p = progress();
  fill('#e2e8f0'); rect(24, 602, 952, 20, 8);
  fill('#22c55e'); rect(24, 602, 952 * (p.pct / 100), 20, 8);
  fill('#0f172a'); textSize(12); text(`Progress: ${p.done}/${p.total} (${p.pct}%)`, 30, 617);
}

function mousePressed() {
  boxes.forEach((b) => {
    if (mouseX > b.x && mouseX < b.x + 380 && mouseY > b.y && mouseY < b.y + 24) b.checked = !b.checked;
  });
}
