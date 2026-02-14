const goodHeader=['ConceptID','ConceptLabel','Dependencies','TaxonomyID'];
const goodRows=[
['1','Artificial Intelligence','','FOUND'],
['2','Claude AI','1','BASIC'],
['3','Large Language Models','2','BASIC'],
['4','Prompt Engineering','3','SKILL'],
['5','Learning Graph','1|4','CORE']
];
const badRows=[
['1','artificial intelligence','','found'],
['3','Large Language Models','2','BASIC'],
['4','Prompt Engineering','5','SKILL']
];

const BASE_W = 1240;
const BASE_H = 500;
let scaleFactor = 1;

function getCanvasWidth() {
  const main = document.querySelector('main');
  if (!main) return BASE_W;
  const w = main.clientWidth || BASE_W;
  return Math.min(BASE_W, Math.max(320, w));
}

function resizeToContainer() {
  const w = getCanvasWidth();
  scaleFactor = w / BASE_W;
  resizeCanvas(w, Math.round(BASE_H * scaleFactor));
}

function setup(){
  const c=createCanvas(BASE_W, BASE_H);
  c.parent(document.querySelector('main'));
  textFont('Arial');
  resizeToContainer();
}

function drawTable(x,y,rows,good=true){
  const w=[100,280,170,130], rh=34;
  let xx=x;
  fill('#e2e8f0'); stroke('#94a3b8');
  for(let i=0;i<4;i++){rect(xx,y,w[i],rh); noStroke(); fill('#111827'); textSize(12); textAlign(CENTER,CENTER); text(goodHeader[i],xx+w[i]/2,y+rh/2); stroke('#94a3b8'); fill('#e2e8f0'); xx+=w[i];}
  for(let r=0;r<rows.length;r++){
    xx=x;
    for(let c=0;c<4;c++){
      fill('#fff'); stroke('#cbd5e1'); rect(xx,y+rh*(r+1),w[c],rh);
      noStroke(); fill('#111827'); textSize(12); textAlign(LEFT,CENTER); text(rows[r][c],xx+6,y+rh*(r+1)+rh/2);
      xx+=w[c];
    }
  }
}

function drawDiagram(){
  background('#f8fafc');
  fill('#0f172a'); textSize(24); text('CSV File Format Example with Validation',20,34);

  fill('#166534'); textSize(16); text('Correct CSV Format',20,72);
  drawTable(20,86,goodRows,true);
  fill('#166534'); textSize(13);
  text('✓ Sequential IDs starting at 1\n✓ Title Case labels\n✓ Pipe-delimited dependencies\n✓ Empty dependencies for foundational concept', 20, 306);

  fill('#b91c1c'); textSize(16); text('Common Errors',680,72);
  drawTable(680,86,badRows,false);
  fill('#b91c1c'); textSize(13);
  text('✗ Row 1: Not Title Case\n✗ Row 1: TaxonomyID not uppercase\n✗ Missing ConceptID 2\n✗ Row 3: dependency on non-existent concept 5', 680, 236);
}

function draw(){
  background('#f8fafc');
  push();
  scale(scaleFactor);
  drawDiagram();
  pop();
}

function windowResized() {
  resizeToContainer();
}
