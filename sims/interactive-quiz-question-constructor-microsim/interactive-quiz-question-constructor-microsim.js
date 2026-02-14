const bloom = ['Remember', 'Understand', 'Apply', 'Analyze', 'Evaluate', 'Create'];
let selectedBloom = 1;
let selectedKey = 0;
let score = 62;
let stemInput, answerInputs = [], conceptSelect, statusMsg = 'Click Analyze Quality to evaluate.';

function setup() {
  const c = createCanvas(1020, 720);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  stemInput = createInput('Which graph query pattern best traverses 3-hop dependencies efficiently?');
  stemInput.position(20, 96); stemInput.size(610, 28);

  conceptSelect = createSelect();
  conceptSelect.position(20, 138); conceptSelect.size(220, 30);
  ['Graph Database', 'Learning Graph', 'Dependency Mapping', 'Bloom Taxonomy'].forEach((v) => conceptSelect.option(v));

  for (let i = 0; i < 4; i++) {
    const inp = createInput(['Recursive path query', 'Full table scan', 'Manual CSV review', 'Random walk'][i]);
    inp.position(20, 252 + i * 46); inp.size(520, 30);
    answerInputs.push(inp);

    const btn = createButton(['A', 'B', 'C', 'D'][i]);
    btn.position(548, 252 + i * 46); btn.size(32, 30);
    btn.mousePressed(() => { selectedKey = i; });
  }

  const analyze = createButton('Analyze Quality');
  analyze.position(20, 460);
  analyze.mousePressed(() => {
    const len = stemInput.value().length;
    score = 40 + Math.min(30, Math.floor(len / 4)) + (selectedBloom * 3);
    score = Math.min(98, score);
    statusMsg = score >= 70 ? 'Acceptable question quality.' : 'Needs revision: improve clarity/distractors.';
  });

  const preview = createButton('Preview Question');
  preview.position(140, 460);
  preview.mousePressed(() => { statusMsg = `Preview ready. Correct key: ${['A','B','C','D'][selectedKey]}.`; });

  const reset = createButton('Reset');
  reset.position(270, 460);
  reset.mousePressed(() => location.reload());
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Interactive Quiz Question Constructor', 16, 30);

  fill('#ffffff'); stroke('#cbd5e1'); rect(12, 46, 640, 660, 10);
  noStroke(); fill('#0f172a'); textSize(14); text('Stem', 20, 86);
  fill('#334155'); textSize(12); text(`Characters: ${stemInput.value().length}`, 540, 86);

  fill('#0f172a'); textSize(14); text('Concept', 20, 134);
  text('Bloom Level', 270, 134);

  for (let i = 0; i < bloom.length; i++) {
    fill(selectedBloom === i ? '#bfdbfe' : '#e2e8f0'); rect(270 + i * 58, 140, 54, 28, 6);
    fill('#0f172a'); textSize(10); textAlign(CENTER, CENTER); text(bloom[i][0], 297 + i * 58, 154); textAlign(LEFT, BASELINE);
    if (mouseIsPressed && mouseX > 270 + i * 58 && mouseX < 324 + i * 58 && mouseY > 140 && mouseY < 168) selectedBloom = i;
  }

  fill('#0f172a'); textSize(14); text('Answer Options (click A/B/C/D to set correct key)', 20, 236);
  fill('#334155'); textSize(12); text(`Selected Key: ${['A','B','C','D'][selectedKey]}`, 20, 448);

  fill('#ffffff'); stroke('#cbd5e1'); rect(668, 46, 340, 660, 10);
  noStroke(); fill('#0f172a'); textSize(18); text('Quality Feedback', 684, 78);

  fill('#e2e8f0'); rect(684, 98, 308, 16, 8);
  fill(score >= 70 ? '#22c55e' : '#f59e0b'); rect(684, 98, 308 * (score / 100), 16, 8);
  fill('#0f172a'); textSize(13); text(`Score: ${score}/100`, 684, 132);

  const metrics = [
    ['Stem clarity', Math.min(20, Math.floor(stemInput.value().length / 6))],
    ['Distractor plausibility', 15],
    ['Homogeneity', 12],
    ['Bloom alignment', 8 + selectedBloom],
    ['Concept alignment', 13],
    ['Explanation quality', 10]
  ];
  let y = 164;
  metrics.forEach(([k, v]) => {
    fill('#334155'); textSize(12); text(`${k}: ${v}`, 684, y);
    y += 24;
  });

  fill(score >= 70 ? '#166534' : '#991b1b'); textSize(12); text(statusMsg, 684, 332, 300, 60);
  fill('#334155'); text('Tip: use specific verbs and plausible distractors.', 684, 370, 300, 60);
}
