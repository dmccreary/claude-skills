const oldTax = ['Evaluation','Synthesis','Analysis','Application','Comprehension','Knowledge'];
const newTax = ['Create','Evaluate','Analyze','Apply','Understand','Remember'];

function setup() {
  const cnv = createCanvas(1020, 620);
  cnv.parent(document.querySelector('main'));
  textFont('Arial');
}

function drawPyramid(x, yTop, levelW, levelH, labels, palette, title) {
  fill('#0f172a'); noStroke(); textSize(18); text(title, x - 10, yTop - 18);
  for (let i = 0; i < labels.length; i++) {
    const w = levelW + i * 28;
    const y = yTop + i * levelH;
    const xLeft = x + (labels.length - i - 1) * 14;
    fill(palette[i]); stroke('#334155'); strokeWeight(1.3);
    rect(xLeft, y, w, levelH - 4, 6);
    noStroke(); fill('#111827'); textSize(14); textAlign(CENTER, CENTER);
    text(labels[i], xLeft + w / 2, y + (levelH - 4) / 2);
  }
}

function draw() {
  background('#f8fafc');
  textAlign(LEFT, BASELINE);
  fill('#0f172a'); textSize(24); text("Bloom's Taxonomy: 1956 vs 2001", 20, 34);

  const leftColors = ['#fecaca','#fca5a5','#f87171','#ef4444','#dc2626','#b91c1c'];
  const rightColors = ['#ddd6fe','#c4b5fd','#a78bfa','#8b5cf6','#7c3aed','#6d28d9'];

  drawPyramid(90, 90, 180, 70, oldTax, leftColors, 'Original (1956): Noun-based categories');
  drawPyramid(560, 90, 180, 70, newTax, rightColors, 'Revised (2001): Verb-based processes');

  // Transformation arrows
  stroke('#334155'); strokeWeight(2); fill('#334155');
  function arrow(x1,y1,x2,y2,label){
    line(x1,y1,x2,y2);
    const a=atan2(y2-y1,x2-x1);
    push(); translate(x2,y2); rotate(a); triangle(0,0,-10,5,-10,-5); pop();
    noStroke(); textSize(12); text(label, (x1+x2)/2 + 6, (y1+y2)/2 - 6); stroke('#334155');
  }

  arrow(410, 470, 560, 470, 'Knowledge -> Remember');
  arrow(396, 400, 574, 400, 'Comprehension -> Understand');
  arrow(355, 190, 588, 120, 'Synthesis -> Create (moved up)');
  arrow(340, 120, 603, 190, 'Evaluation -> Evaluate');

  noStroke(); fill('#334155'); textSize(14);
  text('Create elevated to the highest level, emphasizing generative thinking.', 20, 598);
}
