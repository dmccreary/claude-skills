const features = [
  {
    name: 'Navigation',
    standard: 'Simple vertical menu with limited hierarchy.',
    material: 'Multi-level navigation, sections, tabs, and instant page transitions.'
  },
  {
    name: 'Search',
    standard: 'Basic keyword search.',
    material: 'Search suggestions, result highlighting, keyboard-friendly navigation.'
  },
  {
    name: 'Visual Design',
    standard: 'Minimal default styling.',
    material: 'Material Design components, strong theming, optional dark mode.'
  },
  {
    name: 'Content Features',
    standard: 'Core markdown rendering.',
    material: 'Admonitions, tabs, annotations, icons, enhanced content blocks.'
  },
  {
    name: 'Mobile Experience',
    standard: 'Basic responsive behavior.',
    material: 'Touch-optimized drawer, adaptive navigation, better small-screen UX.'
  },
  {
    name: 'Performance',
    standard: 'Traditional full page loads.',
    material: 'Instant loading with prefetching and improved navigation flow.'
  }
];

let selected = 0;
let darkMode = false;

function setup() {
  const c = createCanvas(1100, 560);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawFeatureList(x, y, w, h) {
  fill(darkMode ? '#1e293b' : '#ffffff');
  stroke(darkMode ? '#334155' : '#cbd5e1');
  rect(x, y, w, h, 10);

  noStroke();
  fill(darkMode ? '#e2e8f0' : '#0f172a');
  textSize(16);
  text('Features', x + 12, y + 26);

  const rowH = 42;
  for (let i = 0; i < features.length; i++) {
    const ry = y + 40 + i * rowH;
    if (i === selected) {
      fill('#bfdbfe');
      rect(x + 8, ry - 2, w - 16, rowH - 4, 6);
    }
    fill('#1e293b');
    textSize(13);
    text(features[i].name, x + 16, ry + 20);
  }
}

function drawComparison(x, y, w, h) {
  const bg = darkMode ? '#0f172a' : '#f8fafc';
  fill(bg);
  stroke(darkMode ? '#334155' : '#cbd5e1');
  rect(x, y, w, h, 10);

  const colW = (w - 30) / 2;
  const item = features[selected];

  fill('#dbeafe');
  noStroke();
  rect(x + 10, y + 52, colW, h - 64, 8);
  fill('#fee2e2');
  rect(x + 20 + colW, y + 52, colW, h - 64, 8);

  fill('#1e3a8a');
  textSize(18);
  text('Standard MkDocs', x + 22, y + 82);
  fill('#991b1b');
  text('Material for MkDocs', x + 32 + colW, y + 82);

  fill('#1f2937');
  textSize(14);
  text(item.standard, x + 22, y + 112, colW - 22, 180);
  text(item.material, x + 32 + colW, y + 112, colW - 22, 180);

  fill(darkMode ? '#e2e8f0' : '#0f172a');
  textSize(20);
  text(item.name, x + 12, y + 30);
}

function drawToggle(x, y, w, h) {
  fill(darkMode ? '#334155' : '#e2e8f0');
  stroke('#64748b');
  rect(x, y, w, h, 16);
  const knobX = darkMode ? x + w - 24 : x + 8;
  fill('#ffffff');
  noStroke();
  circle(knobX, y + h / 2, 18);
  fill(darkMode ? '#e2e8f0' : '#334155');
  textSize(12);
  text('Dark Mode Example', x - 130, y + 18);
}

function draw() {
  background(darkMode ? '#0b1220' : '#eef2ff');
  fill(darkMode ? '#f8fafc' : '#0f172a');
  noStroke();
  textSize(22);
  text('Material Theme Features Interactive Comparison', 16, 32);

  drawFeatureList(20, 54, 280, 480);
  drawComparison(320, 54, 760, 480);
  drawToggle(980, 14, 100, 24);
}

function mousePressed() {
  const rowH = 42;
  for (let i = 0; i < features.length; i++) {
    const ry = 54 + 40 + i * rowH;
    if (mouseX >= 28 && mouseX <= 292 && mouseY >= ry - 2 && mouseY <= ry + rowH - 6) {
      selected = i;
      return;
    }
  }

  if (mouseX >= 980 && mouseX <= 1080 && mouseY >= 14 && mouseY <= 38) {
    darkMode = !darkMode;
  }
}
