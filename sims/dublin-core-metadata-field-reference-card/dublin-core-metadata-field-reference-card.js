const cards=[
['📚','Title','Primary name of the learning graph','String, 5-10 words','Graph Databases Learning Graph','#3b82f6'],
['📝','Description','Detailed summary of scope and audience','String, 1-3 sentences','200-concept graph for undergraduate...','#22c55e'],
['👤','Creator','Primary author or maintainer','String, name and affiliation','Dr. Jane Smith, State University','#8b5cf6'],
['📅','Date','Creation or last update date','ISO 8601: YYYY-MM-DD','2024-09-15','#f97316'],
['🔢','Version','Revision number for tracking changes','Semantic: MAJOR.MINOR.PATCH','1.2.0','#ef4444'],
['📄','Format','File format and version specification','String, format + version','vis-network JSON v9.1','#14b8a6'],
['⚖️','License','Usage rights and restrictions','License identifier','CC-BY-4.0','#eab308']
];

function setup(){const c=createCanvas(1220,620);c.parent(document.querySelector('main'));textFont('Arial');}
function draw(){
  background('#f8fafc');
  fill('#0f172a'); textSize(24); text('Dublin Core Metadata Field Reference Card',20,34);

  const cols=3, cardW=380, cardH=164, gap=20, x0=20, y0=72;
  for(let i=0;i<cards.length;i++){
    const r=Math.floor(i/cols), c=i%cols;
    const x=x0+c*(cardW+gap), y=y0+r*(cardH+gap);
    const over=mouseX>x&&mouseX<x+cardW&&mouseY>y&&mouseY<y+cardH;
    fill('#fff'); stroke(cards[i][5]); strokeWeight(over?4:2); rect(x,y,cardW,cardH,10);
    noStroke(); fill('#111827'); textSize(24); text(cards[i][0],x+14,y+32);
    textSize(16); text(cards[i][1],x+52,y+34);
    textSize(12); fill('#334155'); text(`Purpose: ${cards[i][2]}`,x+14,y+58,cardW-24,38);
    text(`Format: ${cards[i][3]}`,x+14,y+96,cardW-24,30);
    fill('#0f172a'); text(`Example: ${cards[i][4]}`,x+14,y+126,cardW-24,32);
    if(over){fill('#111827'); textSize(11); text('Validation: required, typed, and consistently formatted.',x+14,y+152);}
  }
}
