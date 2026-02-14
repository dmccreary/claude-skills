let state={concepts:200,orph:10,avg:3.2,chain:16,linear:35,tax:22,cycles:false,disc:false};
let target=0,shown=0;

function clamp(v,a,b){return Math.max(a,Math.min(b,v));}
function score(){
  const structural = state.cycles||state.disc ? 0 : 40;
  const conn = clamp(30 - Math.abs(state.orph-10)*1.1 - Math.abs(state.avg-3.2)*5 - Math.max(0,state.chain-18),0,30);
  const dist = clamp(20 - Math.abs(state.linear-35)*0.35 - Math.abs(state.concepts-200)*0.03,0,20);
  const tax = clamp(10 - Math.max(0,state.tax-25)*0.5,0,10);
  return {structural,conn,dist,tax,total:Math.round(structural+conn+dist+tax)};
}

function mkSlider(lbl,min,max,val,step,key){
  const wrap=createDiv('').parent('controls').style('margin-bottom','8px');
  createDiv(lbl).parent(wrap).style('font-size','12px');
  const s=createSlider(min,max,val,step).parent(wrap).style('width','260px');
  const out=createSpan(String(val)).parent(wrap).style('margin-left','8px').style('font-size','12px');
  s.input(()=>{state[key]=Number(s.value());out.html(s.value()); target=score().total;});
}

function mkCheck(lbl,key){const w=createDiv('').parent('controls').style('margin-bottom','6px');const c=createCheckbox(lbl,state[key]).parent(w);c.changed(()=>{state[key]=c.checked();target=score().total;});}

function setup(){
  const c=createCanvas(900,600); c.parent(document.querySelector('main'));
  createDiv('<div id="controls" style="position:absolute;left:610px;top:16px;width:280px;font-family:Arial"></div>');
  mkSlider('Number of Concepts',50,300,200,1,'concepts');
  mkSlider('Orphaned Nodes %',0,40,10,1,'orph');
  mkSlider('Avg Dependencies',1,6,3.2,0.1,'avg');
  mkSlider('Max Chain Length',5,35,16,1,'chain');
  mkSlider('Linear Chain %',10,80,35,1,'linear');
  mkSlider('Largest Taxonomy %',10,60,22,1,'tax');
  mkCheck('Has Cycles','cycles'); mkCheck('Has Disconnected Subgraphs','disc');
  const b1=createButton('Reset to Defaults').parent('controls').style('margin-right','6px');
  b1.mousePressed(()=>{state={concepts:200,orph:10,avg:3.2,chain:16,linear:35,tax:22,cycles:false,disc:false};location.reload();});
  const b2=createButton('Load Poor Graph').parent('controls').style('margin-right','6px');
  b2.mousePressed(()=>{state={concepts:220,orph:35,avg:1.4,chain:28,linear:70,tax:48,cycles:true,disc:true};target=score().total;});
  const b3=createButton('Load Excellent Graph').parent('controls');
  b3.mousePressed(()=>{state={concepts:200,orph:8,avg:3.3,chain:15,linear:34,tax:21,cycles:false,disc:false};target=score().total;});
  target=score().total; shown=target;
}

function gaugeColor(v){if(v<40)return color('#ef4444'); if(v<60)return color('#f97316'); if(v<75)return color('#eab308'); if(v<90)return color('#84cc16'); return color('#15803d');}

function draw(){
  background('#f8fafc');
  const s=score(); target=s.total; shown=lerp(shown,target,0.12);
  fill('#0f172a'); noStroke(); textSize(20); text('Learning Graph Quality Score Calculator',16,30);

  // gauge
  const cx=280, cy=250, r=150;
  strokeWeight(20); noFill();
  const seg=[40,20,15,15,10], cols=['#ef4444','#f97316','#eab308','#84cc16','#15803d'];
  let a=PI; for(let i=0;i<seg.length;i++){stroke(cols[i]); arc(cx,cy,r*2,r*2,a,a+PI*(seg[i]/100)); a+=PI*(seg[i]/100);}  
  noStroke(); fill(gaugeColor(shown)); textAlign(CENTER,CENTER); textSize(54); text(Math.round(shown),cx,250);
  fill('#334155'); textSize(14); text('Score / 100',cx,292);

  // bars
  const parts=[['Structural Validity',s.structural,40,'#3b82f6'],['Connectivity Quality',s.conn,30,'#22c55e'],['Distribution Quality',s.dist,20,'#f97316'],['Taxonomy Balance',s.tax,10,'#8b5cf6']];
  let y=360;
  textAlign(LEFT,BASELINE);
  for(const p of parts){
    fill('#111827');textSize(13);text(`${p[0]}: ${p[1].toFixed(1)}/${p[2]}`,60,y);
    fill('#e2e8f0');rect(60,y+8,460,16,6);
    fill(p[3]);rect(60,y+8,460*(p[1]/p[2]),16,6);
    y+=52;
  }
}
