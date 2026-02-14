function setup() {
  const cnv = createCanvas(1080, 560);
  cnv.parent(document.querySelector('main'));
  textFont('Arial');
}

const cols = ['Skill Type', 'Read', 'Grep', 'Glob', 'Write', 'Edit', 'Bash', 'WebFetch'];
const rows = [
  ['Quality Analyzer', 1,1,1,1,0,0,0],
  ['Content Generator',1,1,1,1,1,0,0],
  ['MicroSim Creator',1,1,1,1,0,0,1],
  ['Workflow Orchestrator',1,1,1,1,1,1,0],
  ['Script Executor',1,0,0,1,0,1,0],
];

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Skill Permission Matrix', 20, 34);
  textSize(13); fill('#475569'); text('✓ indicates typically required tool', 20, 56);

  const x0 = 20, y0 = 80;
  const widths = [280, 95, 95, 95, 95, 95, 95, 115];
  const rh = 68;

  let x = x0;
  for (let c=0;c<cols.length;c++) {
    fill('#e2e8f0'); stroke('#94a3b8'); rect(x, y0, widths[c], rh);
    noStroke(); fill('#0f172a'); textSize(13); textAlign(CENTER, CENTER);
    text(cols[c], x + widths[c]/2, y0 + rh/2);
    x += widths[c];
  }

  for (let r=0;r<rows.length;r++) {
    let xx = x0;
    for (let c=0;c<cols.length;c++) {
      const yy = y0 + rh * (r + 1);
      fill(c === 0 ? '#ffffff' : '#f8fafc'); stroke('#cbd5e1'); rect(xx, yy, widths[c], rh);
      noStroke(); textAlign(CENTER, CENTER);
      if (c === 0) {
        fill('#111827'); textSize(13); text(rows[r][0], xx + widths[c]/2, yy + rh/2);
      } else {
        const on = rows[r][c] === 1;
        fill(on ? '#16a34a' : '#94a3b8'); textSize(28); text(on ? '✓' : '·', xx + widths[c]/2, yy + rh/2 + (on ? -1 : 0));
      }
      xx += widths[c];
    }
  }

  // highlight most privileged row
  const yHi = y0 + rh * 4;
  noFill(); stroke('#f97316'); strokeWeight(3); rect(x0+1, yHi+1, widths.reduce((a,b)=>a+b,0)-2, rh-2);
  noStroke(); fill('#9a3412'); textSize(12); textAlign(LEFT, BASELINE);
  text('Workflow Orchestrator: broadest tool access', x0 + 8, yHi - 8);
}
