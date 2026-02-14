(function(){
  const n=200;
  const labels=Array.from({length:n},(_,i)=>i+1);
  const found=labels.map(i=> i<=20 ? Math.max(0,22-i*0.8) : 0);
  const pre=labels.map(i=> i<10 ? i*1.2 : i<=180 ? 18 + 8*Math.sin(i/28) : Math.max(0,20-(i-180)*1.5));
  const adv=labels.map(i=> i<150 ? 0 : Math.min(24,(i-150)*0.5));

  const ann={
    id:'ann',
    afterDatasetsDraw(chart){
      const {ctx,scales}=chart;ctx.save();ctx.fillStyle='#334155';ctx.font='12px Arial';
      ctx.fillText('Foundational concepts: early in topological order', scales.x.getPixelForValue(8), scales.y.getPixelForValue(52));
      ctx.fillText('Prerequisite concepts: core middle sections', scales.x.getPixelForValue(65), scales.y.getPixelForValue(34));
      ctx.fillText('Advanced concepts: late in order, require integration', scales.x.getPixelForValue(152), scales.y.getPixelForValue(16));
      ctx.restore();
    }
  };

  function init(){
    document.querySelector('main').innerHTML='<div style="height:560px;padding:12px;background:#f8fafc"><canvas id="c"></canvas></div>';
    new Chart(document.getElementById('c'),{
      type:'line',
      data:{labels,datasets:[
        {label:'Foundational (0 deps)',data:found,borderColor:'#ef4444',backgroundColor:'rgba(239,68,68,0.35)',fill:true,pointRadius:0,tension:.25,stack:'s'},
        {label:'Prerequisite (1-3 deps)',data:pre,borderColor:'#f97316',backgroundColor:'rgba(249,115,22,0.35)',fill:true,pointRadius:0,tension:.25,stack:'s'},
        {label:'Advanced (4+ deps)',data:adv,borderColor:'#eab308',backgroundColor:'rgba(234,179,8,0.35)',fill:true,pointRadius:0,tension:.25,stack:'s'}
      ]},
      options:{
        responsive:true,maintainAspectRatio:false,
        plugins:{title:{display:true,text:'Concept Depth Progression Across Learning Graph',font:{size:18}},legend:{position:'bottom'}},
        scales:{x:{title:{display:true,text:'Concept position in topological order (1-200)'},ticks:{maxTicksLimit:12}},y:{title:{display:true,text:'Cumulative count by depth tier'},beginAtZero:true,max:60}}
      },
      plugins:[ann]
    });
  }
  window.addEventListener('DOMContentLoaded',init);
})();
