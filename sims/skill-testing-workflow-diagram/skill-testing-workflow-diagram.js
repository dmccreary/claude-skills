const nodes = [
  { id: 'start', t: 'Write/Update\nSKILL.md', x: 90, y: 80, c: '#bfdbfe', shape: 'rect' },
  { id: 'invoke', t: 'Invoke Skill\nwith Test Data', x: 90, y: 180, c: '#bfdbfe', shape: 'rect' },
  { id: 'monitor', t: 'Monitor\nExecution', x: 90, y: 280, c: '#bfdbfe', shape: 'rect' },
  { id: 'ok', t: 'Execution\nSuccessful?', x: 350, y: 280, c: '#fde68a', shape: 'diamond' },
  { id: 'validate', t: 'Validate\nOutput Quality', x: 580, y: 220, c: '#bbf7d0', shape: 'rect' },
  { id: 'quality', t: 'Output Meets\nRequirements?', x: 580, y: 320, c: '#fde68a', shape: 'diamond' },
  { id: 'ready', t: 'Skill Ready\nfor Use', x: 810, y: 220, c: '#86efac', shape: 'rect' },
  { id: 'error', t: 'Analyze\nError', x: 580, y: 430, c: '#fed7aa', shape: 'rect' },
  { id: 'root', t: 'Identify\nRoot Cause', x: 810, y: 430, c: '#fed7aa', shape: 'rect' },
  { id: 'update', t: 'Update SKILL.md\nor Assets', x: 810, y: 320, c: '#fecaca', shape: 'rect' }
];

const edges = [
  ['start', 'invoke', ''], ['invoke', 'monitor', ''], ['monitor', 'ok', ''],
  ['ok', 'validate', 'Yes'], ['ok', 'error', 'No'],
  ['validate', 'quality', ''], ['quality', 'ready', 'Yes'], ['quality', 'update', 'No'],
  ['error', 'root', ''], ['root', 'update', ''], ['update', 'invoke', 'Loop']
];

function byId(id) { return nodes.find((n) => n.id === id); }
function hit(n) { return mouseX > n.x && mouseX < n.x + 170 && mouseY > n.y && mouseY < n.y + 66; }

function setup() {
  const c = createCanvas(1000, 560);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawBox(n) {
  const h = hit(n);
  stroke(h ? '#1d4ed8' : '#64748b');
  strokeWeight(h ? 3 : 1.5);
  fill(n.c);
  if (n.shape === 'diamond') {
    quad(n.x + 85, n.y, n.x + 170, n.y + 33, n.x + 85, n.y + 66, n.x, n.y + 33);
  } else {
    rect(n.x, n.y, 170, 66, 8);
  }
  noStroke();
  fill('#0f172a');
  textAlign(CENTER, CENTER);
  textSize(13);
  text(n.t, n.x + 85, n.y + 33);
}

function arrow(a, b, lbl) {
  stroke('#334155');
  strokeWeight(2);
  const x1 = a.x + 170, y1 = a.y + 33;
  const x2 = b.x, y2 = b.y + 33;
  if (a.x > b.x) {
    line(a.x, y1, a.x - 20, y1);
    line(a.x - 20, y1, a.x - 20, y2);
    line(a.x - 20, y2, x2, y2);
    drawHead(x2, y2, PI);
    if (lbl) label(lbl, (a.x + x2) / 2 - 30, y2 - 10);
    return;
  }
  line(x1, y1, x2, y2);
  drawHead(x2, y2, atan2(y2 - y1, x2 - x1));
  if (lbl) label(lbl, (x1 + x2) / 2, (y1 + y2) / 2 - 10);
}

function drawHead(x, y, a) {
  push(); translate(x, y); rotate(a); noStroke(); fill('#334155'); triangle(0, 0, -10, 4, -10, -4); pop();
}
function label(t, x, y) { noStroke(); fill('#0f172a'); textSize(11); textAlign(CENTER, CENTER); text(t, x, y); }

function draw() {
  background('#f8fafc');
  fill('#0f172a'); noStroke(); textAlign(LEFT, BASELINE); textSize(22);
  text('Skill Testing Workflow Diagram', 16, 30);

  edges.forEach(([a, b, l]) => arrow(byId(a), byId(b), l));
  nodes.forEach(drawBox);

  const hovered = nodes.find(hit);
  fill('#e2e8f0'); rect(16, 500, 968, 46, 8);
  fill('#334155'); textSize(12);
  text(hovered ? `Hover: ${hovered.t.replace('\n', ' ')}.` : 'Hover a node to inspect each phase of the testing loop.', 26, 528);
}
