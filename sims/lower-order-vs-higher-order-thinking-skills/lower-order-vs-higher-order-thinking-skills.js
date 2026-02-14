function setup() {
  const c = createCanvas(1000, 620);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function draw() {
  background('#f8fafc');
  fill('#0f172a');
  textSize(24);
  text('Lower-Order vs Higher-Order Thinking Skills', 20, 34);

  const cx = 360;
  const topY = 90;
  const h = 420;
  const w = 420;
  const midY = topY + h / 2;

  // Pyramid shape
  noStroke();
  fill('#facc15');
  triangle(cx, topY, cx - w / 2, midY, cx + w / 2, midY);
  fill('#60a5fa');
  quad(cx - w / 2, midY, cx + w / 2, midY, cx + w / 2 - 80, topY + h, cx - w / 2 + 80, topY + h);

  // Divider and outlines
  stroke('#1f2937');
  strokeWeight(2);
  line(cx - w / 2, midY, cx + w / 2, midY);
  noFill();
  beginShape();
  vertex(cx, topY);
  vertex(cx - w / 2, midY);
  vertex(cx - w / 2 + 80, topY + h);
  vertex(cx + w / 2 - 80, topY + h);
  vertex(cx + w / 2, midY);
  endShape(CLOSE);

  noStroke();
  fill('#111827');
  textAlign(CENTER, CENTER);
  textSize(17);
  text('Higher-Order Thinking Skills (HOTS)', cx, topY + 70);
  textSize(20);
  text('Analyze • Evaluate • Create', cx, topY + 120);

  textSize(17);
  text('Lower-Order Thinking Skills (LOTS)', cx, midY + 65);
  textSize(20);
  text('Remember • Understand • Apply', cx, midY + 115);

  // Info boxes
  textAlign(LEFT, TOP);
  fill('#fef9c3');
  stroke('#a16207');
  rect(660, 140, 310, 150, 8);
  noStroke();
  fill('#111827');
  textSize(14);
  text('HOTS\nFocus on critical thinking and creation\n\nDemonstrate deeper learning\nand professional competence.', 676, 160);

  fill('#dbeafe');
  stroke('#1d4ed8');
  rect(660, 320, 310, 150, 8);
  noStroke();
  fill('#111827');
  text('LOTS\nFocus on knowledge acquisition\nand application\n\nEssential foundation, but\ninsufficient for mastery alone.', 676, 340);

  fill('#334155');
  textSize(13);
  text('Educational research note: well-designed courses often include 60-70% HOTS outcomes.', 20, 586);
}
