const criteria = [
  {q:'Title Case capitalization?', good:'Learning Graph Quality Metrics', bad:'learning graph quality metrics'},
  {q:'<= 32 characters?', good:'Graph Database Architecture (28)', bad:'Comprehensive Overview of Graph Database Architectures and Patterns (72)'},
  {q:'Domain-standard terminology?', good:"Bloom's Taxonomy", bad:'Educational Goal Levels'},
  {q:'Singular form (unless standard plural)?', good:'Concept Node', bad:'Concept Nodes'},
  {q:'Noun form rather than gerund?', good:'Dependency Mapping', bad:'Mapping Dependencies'},
  {q:'No redundant words?', good:'Claude Skills', bad:'Claude Skills System Framework'}
];
let selected = -1;

function setup(){const c=createCanvas(1180,620);c.parent(document.querySelector('main'));textFont('Arial');}
function draw(){
  background('#f8fafc');
  fill('#0f172a');textSize(24);text('Concept Label Quality Checklist',20,34);
  textSize(13);fill('#475569');text('Click a criterion for additional guidance. All 6 criteria must pass.',20,56);

  const x=20,y=80,rowH=82,w=1140;
  selected=-1;
  for(let i=0;i<criteria.length;i++){
    const yy=y+i*rowH;
    const over=mouseX>x&&mouseX<x+w&&mouseY>yy&&mouseY<yy+rowH-6;
    if(over) selected=i;
    fill(over?'#eef2ff':'#ffffff'); stroke('#cbd5e1'); rect(x,yy,w,rowH-6,8);

    noStroke(); textSize(28); fill('#16a34a'); text('✓', x+16, yy+43);
    fill('#111827'); textSize(15); text(criteria[i].q, x+58, yy+28);
    fill('#166534'); textSize(13); text('Good: '+criteria[i].good, x+58, yy+50);
    fill('#b91c1c'); text('Avoid: '+criteria[i].bad, x+58, yy+69);
  }

  fill('#fff7ed'); stroke('#fdba74'); rect(760,82,400,140,8);
  noStroke(); fill('#9a3412'); textSize(14); text('Validation Rule', 776, 108);
  fill('#7c2d12'); textSize(13); text('A label is valid only when all checklist items pass.\nThis supports clean dependencies and consistent graph quality.', 776, 132);

  if(selected>=0){
    fill('#ecfeff'); stroke('#67e8f9'); rect(760,238,400,178,8);
    noStroke(); fill('#0e7490'); textSize(14); text('Why this matters', 776, 264);
    fill('#164e63'); textSize(13);
    text(`Criterion: ${criteria[selected].q}\n\nGood example aligns with standards and\nimproves searchability, assessment, and\ndependency clarity across chapters.`, 776, 288);
  }
}
function mousePressed(){ redraw(); }
