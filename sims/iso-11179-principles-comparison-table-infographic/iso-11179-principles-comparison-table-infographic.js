const rows = [
  ['Precise', 'Exact, unambiguous', '"small simulation thing"', '"single-concept interactive simulation"', 'No vague words'],
  ['Concise', 'Minimal words', '"particular level at which..."', '"grade-level complexity of text"', 'Under ~20 words'],
  ['Distinct', 'Different from similar terms', '"Chapter: a section"', '"major textbook unit for related concepts"', 'Unique differentiator'],
  ['Non-circular', 'Term not used in definition', '"Content generation is generating content"', '"automated creation from structured inputs"', 'Remove term/synonyms'],
  ['Free of business rules', 'Defines what it is', '"Glossary should be ..."', '"alphabetically organized collection of definitions"', 'Avoid should/must']
];

let showChecks = -1;

function setup() {
  const c = createCanvas(1240, 700);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('ISO 11179 Principles Comparison', 16, 30);

  const x = [20, 170, 390, 660, 930];
  const w = [150, 220, 260, 260, 290];
  const h = 44;
  const headers = ['Principle', 'What It Means', 'Violation Example', 'Compliant Example', 'Quick Check'];
  for (let i = 0; i < 5; i++) { fill('#dbeafe'); stroke('#93c5fd'); rect(x[i], 60, w[i], h); noStroke(); fill('#1e3a8a'); textSize(13); text(headers[i], x[i] + 8, 87); }

  rows.forEach((r, ri) => {
    const y = 104 + ri * 110;
    for (let i = 0; i < 5; i++) {
      const bg = i === 2 ? '#fee2e2' : i === 3 ? '#dcfce7' : '#ffffff';
      fill(bg); stroke('#cbd5e1'); rect(x[i], y, w[i], 104);
      noStroke(); fill('#0f172a'); textSize(12);
      text(r[i], x[i] + 8, y + 18, w[i] - 16, 90);
    }
  });

  fill('#334155'); textSize(12); text('Click a row to toggle quick-check emphasis.', 20, 686);
  if (showChecks >= 0) {
    fill('#1d4ed8'); text(rows[showChecks][4], 320, 686);
  }
}

function mousePressed() {
  for (let i = 0; i < rows.length; i++) {
    const y = 104 + i * 110;
    if (mouseY > y && mouseY < y + 104) { showChecks = showChecks === i ? -1 : i; return; }
  }
}
