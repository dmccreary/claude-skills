const points=[
  {x:0.08,t:'All of Programming',zone:'coarse'},
  {x:0.18,t:'Complete Database Theory',zone:'coarse'},
  {x:0.30,t:'Everything About AI',zone:'coarse'},
  {x:0.50,t:'Directed Acyclic Graph (DAG)',zone:'optimal'},
  {x:0.57,t:"Bloom's Taxonomy",zone:'optimal'},
  {x:0.63,t:'Claude Skill',zone:'optimal'},
  {x:0.78,t:'Third Parameter of Function X',zone:'fine'},
  {x:0.88,t:'Step 2b of Procedure Y',zone:'fine'},
  {x:0.95,t:'Specific Code Line 147',zone:'fine'}
];

function setup(){const c=createCanvas(1180,620);c.parent(document.querySelector('main'));textFont('Arial');}
function draw(){
  background('#f8fafc');
  fill('#0f172a'); textSize(24); text('Concept Granularity Spectrum Visualization',20,34);
  fill('#475569'); textSize(13); text('Granularity consistency is more important than perfection.',20,56);

  const x=70,y=260,w=1040,h=72;
  noStroke(); fill('#ef4444'); rect(x,y,w*0.33,h,8,0,0,8);
  fill('#22c55e'); rect(x+w*0.33,y,w*0.34,h);
  fill('#ef4444'); rect(x+w*0.67,y,w*0.33,h,0,8,8,0);

  fill('#fff'); textSize(16); textAlign(CENTER,CENTER);
  text('Too Broad - Must Split', x+w*0.165, y+h/2);
  text('Atomic - Target Granularity', x+w*0.50, y+h/2);
  text('Too Narrow - Must Merge', x+w*0.835, y+h/2);

  // markers
  for(const p of points){
    const px=x+p.x*w;
    stroke('#1f2937'); line(px,y-90,px,y-2);
    noStroke(); fill(p.zone==='optimal'?'#16a34a':'#b91c1c'); ellipse(px,y-96,9,9);
    fill('#111827'); textSize(12); textAlign(CENTER,BASELINE);
    text(p.t,px,y-102,190,80);
  }

  textAlign(LEFT,BASELINE);
  fill('#7f1d1d'); textSize(13);
  text('Too coarse problems: cannot assess, vague dependencies, generic content.', 70, 390);
  fill('#166534'); text('Optimal characteristics: assessable, clear dependencies, substantial content.', 70, 414);
  fill('#7f1d1d'); text('Too fine problems: trivial assessment, dependency explosion, minimal content.', 70, 438);

  // target arrow
  stroke('#1d4ed8'); strokeWeight(2);
  line(x+w*0.52,470,x+w*0.52,360);
  line(x+w*0.52,360,x+w*0.52-8,372);
  line(x+w*0.52,360,x+w*0.52+8,372);
  noStroke(); fill('#1d4ed8'); textSize(13);
  textAlign(CENTER,BASELINE);
  text('Target ~200 concepts at this granularity', x+w*0.52, 494);
}
