const dims = [
  { name: 'Target Audience', max: 15, color: '#3b82f6', score: 12 },
  { name: 'Prerequisites', max: 15, color: '#8b5cf6', score: 11 },
  { name: 'Main Topics', max: 20, color: '#22c55e', score: 16 },
  { name: 'Exclusions', max: 10, color: '#f97316', score: 7 },
  { name: 'Learning Outcomes', max: 40, color: '#eab308', score: 31 }
];

let hoverIdx = -1;

function setup() {
  const c = createCanvas(980, 620);
  c.parent(document.querySelector('main'));
  textFont('Arial');
}

function tier(total) {
  if (total >= 90) return ['Excellent', '#166534'];
  if (total >= 70) return ['Good', '#15803d'];
  if (total >= 50) return ['Acceptable', '#ca8a04'];
  return ['Insufficient', '#b91c1c'];
}

function draw() {
  background('#f8fafc');
  const total = dims.reduce((a,d)=>a+d.score,0);
  const [label, tierColor] = tier(total);

  fill('#0f172a'); textSize(22);
  text('Course Description Quality Rubric Visualization', 20, 34);

  const cx=320, cy=330, rOuter=210, rInner=90;
  let a=-HALF_PI;
  hoverIdx=-1;

  for(let i=0;i<dims.length;i++){
    const d=dims[i];
    const frac=d.max/100;
    const a2=a+TWO_PI*frac;
    const over=dist(mouseX,mouseY,cx,cy) < rOuter && dist(mouseX,mouseY,cx,cy) > rInner && atan2(mouseY-cy,mouseX-cx) >= a && atan2(mouseY-cy,mouseX-cx) <= a2;
    if(over) hoverIdx=i;

    // base segment
    noStroke(); fill('#e2e8f0');
    arc(cx,cy,rOuter*2,rOuter*2,a,a2,PIE);
    // fill by score ratio
    const fillA = a + (a2-a)*(d.score/d.max);
    fill(d.color);
    arc(cx,cy,rOuter*2,rOuter*2,a,fillA,PIE);
    // donut hole mask
    fill('#f8fafc');
    arc(cx,cy,rInner*2,rInner*2,a,a2,PIE);

    a=a2;
  }

  fill(tierColor); textAlign(CENTER,CENTER); textSize(36); text(total, cx, cy-10);
  fill('#334155'); textSize(16); text(label, cx, cy+28);
  textSize(12); text('out of 100', cx, cy+50);

  // Right panel details
  fill('#fff'); stroke('#cbd5e1'); rect(560,90,390,470,10);
  noStroke(); fill('#111827'); textAlign(LEFT,TOP); textSize(16);
  text('Rubric Dimensions', 580, 110);
  textSize(13);

  let y=145;
  for(let i=0;i<dims.length;i++){
    const d=dims[i];
    fill(d.color); rect(580,y+2,10,10);
    fill('#111827');
    text(`${d.name}: ${d.score}/${d.max}`, 598, y);
    y+=28;
  }

  y += 8;
  fill('#475569');
  text('Quality tiers:\n90-100 Excellent\n70-89 Good\n50-69 Acceptable\n<50 Insufficient', 580, y);

  if(hoverIdx>=0){
    const d=dims[hoverIdx];
    fill('#0f172a'); textSize(14);
    text(`Selected: ${d.name}\nScore: ${d.score}/${d.max}`, 580, 370);
  }
}
