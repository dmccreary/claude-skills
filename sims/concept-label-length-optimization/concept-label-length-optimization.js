const rows=[
['Comprehensive Course Description Development',45,'Course Description',20],
['Learning Graph Dependency Edge Validation',45,'Dependency Edge Validation',30],
['MicroSim Specification and Implementation',46,'MicroSim Implementation',25],
['Chapter Content Generation Process Workflow',48,'Chapter Content Generation',28],
['Interactive Element Types and Specifications',49,'Interactive Element Types',29]
];

function setup(){const c=createCanvas(1200,560);c.parent(document.querySelector('main'));textFont('Arial');}
function draw(){
  background('#f8fafc');
  fill('#0f172a'); textSize(24); text('Concept Label Length Optimization',20,34);
  fill('#475569'); textSize(13); text('Optimization preserves meaning while meeting <=32 character constraint.',20,56);

  const cols=[420,140,420,140], x0=20,y0=84,h=74;
  const heads=['Too Long (>32 chars)','Character Count','Optimized (<32 chars)','Character Count'];
  let x=x0;
  for(let i=0;i<4;i++){fill('#e2e8f0');stroke('#94a3b8');rect(x,y0,cols[i],46);noStroke();fill('#111827');textSize(13);textAlign(CENTER,CENTER);text(heads[i],x+cols[i]/2,y0+23);x+=cols[i];}
  textAlign(LEFT,BASELINE);

  for(let r=0;r<rows.length;r++){
    const y=y0+46+r*h; x=x0;
    for(let c=0;c<4;c++){
      fill(c===0?'#fee2e2':c===2?'#dcfce7':'#ffffff'); stroke('#cbd5e1'); rect(x,y,cols[c],h);
      noStroke(); fill('#111827'); textSize(12);
      if(c===1||c===3){ textAlign(CENTER,CENTER); text(rows[r][c],x+cols[c]/2,y+h/2); textAlign(LEFT,BASELINE);} else text(rows[r][c],x+10,y+26,cols[c]-16,46);
      x+=cols[c];
    }
    fill('#16a34a'); textSize(13); text('↓ ' + (rows[r][1]-rows[r][3]) + ' chars', 1040, y+44);
  }
}
