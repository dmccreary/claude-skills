const rows=[
['Purpose','Unique identifier for programmatic reference','Human-readable concept name'],
['Format','Integer (1 to n)','String (Title Case, <=32 chars)'],
['Mutability','Immutable after dependencies set','Refinable during development'],
['Used in','Dependencies field, validation scripts','Generated content, UI, assessments'],
['Ordering significance','No semantic ordering','N/A (dependencies define order)'],
['Uniqueness','Must be unique across graph','Should be unique (avoid duplicates)'],
['Example','42','Directed Acyclic Graph (DAG)']
];

function setup(){const c=createCanvas(1220,560);c.parent(document.querySelector('main'));textFont('Arial');}
function draw(){
  background('#f8fafc');
  fill('#0f172a');textSize(24);text('ConceptID vs ConceptLabel Comparison',20,34);

  const x0=20,y0=76; const w=[260,430,430], rh=58;
  const head=['Aspect','ConceptID','ConceptLabel'];
  let x=x0;
  for(let i=0;i<3;i++){fill('#e2e8f0');stroke('#94a3b8');rect(x,y0,w[i],48);noStroke();fill('#111827');textAlign(CENTER,CENTER);textSize(32);text(head[i],x+w[i]/2,y0+24);x+=w[i];}

  textAlign(LEFT,TOP);
  for(let r=0;r<rows.length;r++){
    x=x0;const y=y0+48+r*rh;
    for(let c=0;c<3;c++){
      fill(c===1?'#eff6ff':c===2?'#f0fdf4':'#fff');stroke('#cbd5e1');rect(x,y,w[c],rh);
      noStroke();fill('#111827');textSize(28);text(rows[r][c],x+8,y+8,w[c]-16,rh-12);
      x+=w[c];
    }
  }

  fill('#475569');textSize(13);text('ConceptID enables robust dependency tracking; ConceptLabel provides clarity for human readers.',20,548);
}
