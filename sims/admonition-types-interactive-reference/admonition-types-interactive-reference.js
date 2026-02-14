const types = [
  { kind: 'note', color: '#3b82f6', icon: 'i', msg: 'Remember to save your work frequently.' },
  { kind: 'tip', color: '#16a34a', icon: 'bulb', msg: 'Use keyboard shortcuts to speed up navigation.' },
  { kind: 'warning', color: '#f59e0b', icon: '!', msg: 'This operation cannot be undone.' },
  { kind: 'danger', color: '#dc2626', icon: '!!', msg: 'Deleting this file will remove all data.' },
  { kind: 'example', color: '#8b5cf6', icon: '{}', msg: '```bash\nmkdocs serve\n```' },
  { kind: 'quote', color: '#6b7280', icon: '"', msg: 'Documentation is a love letter that you write to your future self.' }
];

let showSyntax = true;
let copyFlashUntil = 0;

function mdSnippet(kind, msg) {
  return `!!! ${kind}\n    ${msg}`;
}

function setup() {
  const c = createCanvas(1040, 560);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  const toggle = createButton('Toggle Syntax / Rendered');
  toggle.position(16, 12);
  toggle.mousePressed(() => {
    showSyntax = !showSyntax;
  });

  const copy = createButton('Copy Selected Markdown');
  copy.position(210, 12);
  copy.mousePressed(async () => {
    const first = types[0];
    try {
      await navigator.clipboard.writeText(mdSnippet(first.kind, first.msg));
      copyFlashUntil = millis() + 1400;
    } catch (e) {
      // Ignore clipboard failures in restricted contexts.
    }
  });
}

function drawCard(t, x, y, w, h) {
  fill('#ffffff');
  stroke(t.color);
  strokeWeight(2);
  rect(x, y, w, h, 10);

  noStroke();
  fill(t.color);
  circle(x + 24, y + 24, 26);
  fill('#ffffff');
  textSize(11);
  textAlign(CENTER, CENTER);
  text(t.icon, x + 24, y + 24);

  textAlign(LEFT, BASELINE);
  fill('#0f172a');
  textSize(16);
  text(t.kind.toUpperCase(), x + 48, y + 30);

  if (showSyntax) {
    fill('#f8fafc');
    stroke('#cbd5e1');
    rect(x + 14, y + 42, w - 28, h - 56, 6);
    noStroke();
    fill('#334155');
    textSize(12);
    text(mdSnippet(t.kind, t.msg), x + 22, y + 62, w - 44, h - 70);
  } else {
    fill('#f1f5f9');
    noStroke();
    rect(x + 14, y + 42, w - 28, h - 56, 6);
    fill('#1f2937');
    textSize(12);
    text(t.msg, x + 22, y + 64, w - 44, h - 74);
  }
}

function draw() {
  background('#f8fafc');
  fill('#0f172a');
  noStroke();
  textSize(22);
  text('Admonition Types Interactive Reference', 16, 50);

  const cols = 3;
  const cardW = 326;
  const cardH = 220;
  const gap = 16;
  const x0 = 16;
  const y0 = 74;

  for (let i = 0; i < types.length; i++) {
    const r = Math.floor(i / cols);
    const c = i % cols;
    const x = x0 + c * (cardW + gap);
    const y = y0 + r * (cardH + gap);
    drawCard(types[i], x, y, cardW, cardH);
  }

  fill('#334155');
  textSize(12);
  text(showSyntax ? 'Mode: Markdown syntax view' : 'Mode: Rendered output view', 16, 548);

  if (millis() < copyFlashUntil) {
    fill('#166534');
    text('Copied markdown snippet for NOTE admonition.', 220, 548);
  }
}
