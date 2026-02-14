const levels = [
  { name: "Level 1: Static Content", color: "#ef4444", caps: ["Fixed text and images", "Linear reading"] },
  { name: "Level 2: Hyperlinked Navigation", color: "#f97316", caps: ["Internal links and TOC", "Search functionality", "Includes Level 1"] },
  { name: "Level 3: Interactive Elements", color: "#eab308", caps: ["MicroSims and quizzes", "Interactive visualizations", "Includes Levels 1-2"] },
  { name: "Level 4: Adaptive Content", color: "#22c55e", caps: ["Prerequisite checking", "Personalized pathways", "Includes Levels 1-3"] },
  { name: "Level 5: AI Personalization", color: "#8b5cf6", caps: ["Generative explanations", "Conversational tutoring", "Includes Levels 1-4"] }
];

let hovered = -1;

function setup() {
  const cnv = createCanvas(1000, 560);
  cnv.parent(document.querySelector('main'));
  textFont('Arial');
}

function draw() {
  background('#f8fafc');
  noStroke();

  fill('#0f172a');
  textSize(24);
  text('Five Levels of Textbook Intelligence', 20, 34);
  textSize(14);
  fill('#475569');
  text('Higher levels include all capabilities of lower levels', 20, 56);

  const baseX = 40;
  const baseY = 500;
  const stepW = 150;
  const stepH = 82;

  hovered = -1;

  for (let i = 0; i < levels.length; i++) {
    const x = baseX + i * stepW;
    const y = baseY - (i + 1) * stepH;
    const w = stepW;
    const h = stepH;

    const over = mouseX >= x && mouseX <= x + w && mouseY >= y && mouseY <= y + h;
    if (over) hovered = i;

    fill(levels[i].color);
    rect(x, y, w, h, 8);

    fill('#ffffff');
    textSize(12);
    textStyle(BOLD);
    text(levels[i].name, x + 8, y + 20, w - 16, h - 16);
    textStyle(NORMAL);
  }

  // Highlight course focus: Levels 2-3
  noFill();
  stroke('#0f172a');
  strokeWeight(3);
  const l2x = baseX + 1 * stepW;
  const l3x = baseX + 2 * stepW;
  const top = baseY - 3 * stepH;
  rect(l2x - 8, top - 8, (l3x + stepW) - l2x + 16, (3 * stepH) + 16, 10);
  noStroke();
  fill('#0f172a');
  textSize(13);
  text('This course focuses here', l2x, top - 14);

  // Upward arrow
  stroke('#0f172a');
  strokeWeight(2);
  line(850, 480, 850, 110);
  line(850, 110, 840, 124);
  line(850, 110, 860, 124);
  noStroke();
  fill('#0f172a');
  textSize(13);
  text('Increasing intelligence\nand personalization', 865, 150);

  // Detail panel
  fill('#e2e8f0');
  rect(620, 210, 350, 300, 10);
  fill('#111827');
  textSize(16);
  text('Capabilities', 640, 238);

  if (hovered >= 0) {
    fill(levels[hovered].color);
    rect(640, 250, 300, 34, 6);
    fill('#fff');
    textSize(13);
    textStyle(BOLD);
    text(levels[hovered].name, 648, 271);
    textStyle(NORMAL);
    fill('#111827');
    textSize(13);
    let y = 306;
    for (const c of levels[hovered].caps) {
      text(`• ${c}`, 648, y);
      y += 24;
    }
  } else {
    fill('#334155');
    textSize(13);
    text('Hover a level in the staircase\nto view capabilities.', 640, 280);
  }
}
