(function () {
  const nodes = [
    {id:1,label:'Artificial\nIntelligence',group:'found',title:'Foundational concept'},
    {id:2,label:'Claude AI',group:'inter',title:'Depends on AI fundamentals'},
    {id:3,label:'Large Language\nModels',group:'inter',title:'Intermediate concept'},
    {id:4,label:'Prompt\nEngineering',group:'inter',title:'Intermediate concept'},
    {id:5,label:'Learning Graph\nGeneration',group:'adv',title:'Advanced concept'},
    {id:6,label:'Claude Code\nInterface',group:'inter',title:'Intermediate concept'},
    {id:7,label:'Claude Skill',group:'inter',title:'Intermediate concept'},
    {id:8,label:'Skill Workflow\nDesign',group:'adv',title:'Advanced concept'}
  ];
  const edges = [
    {from:1,to:2,arrows:'to'},
    {from:2,to:3,arrows:'to'},
    {from:3,to:4,arrows:'to'},
    {from:4,to:5,arrows:'to'},
    {from:2,to:6,arrows:'to'},
    {from:6,to:7,arrows:'to'},
    {from:7,to:8,arrows:'to'}
  ];

  function init() {
    document.querySelector('main').innerHTML = `
      <div style="padding:8px;font-family:Arial,sans-serif;">
        <h2 style="margin:0 0 6px 0;">Learning Graph Structure Visualization</h2>
        <p style="margin:0 0 8px 0;color:#475569;">Foundational -> Intermediate -> Advanced concepts with prerequisite edges</p>
        <div id="net" style="height:600px;border:1px solid #cbd5e1;background:#f8fafc;"></div>
      </div>`;

    const data = { nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) };
    const options = {
      layout: { hierarchical: { enabled:true, direction:'UD', levelSeparation:120, nodeSpacing:130 } },
      groups: {
        found: { color:{background:'#ef4444',border:'#991b1b'}, font:{color:'#fff'} },
        inter: { color:{background:'#f59e0b',border:'#92400e'}, font:{color:'#111'} },
        adv: { color:{background:'#facc15',border:'#a16207'}, font:{color:'#111'} }
      },
      nodes: { shape:'dot', size:20, font:{size:13, multi:'html'} },
      edges: { color:'#1f2937', width:2, arrows:{to:{enabled:true}} },
      interaction: { hover:true },
      physics: false
    };

    const network = new vis.Network(document.getElementById('net'), data, options);
    network.on('click', (params)=>{
      if(!params.nodes.length) return;
      const n=params.nodes[0];
      const connected = network.getConnectedNodes(n);
      const all = data.nodes.getIds();
      data.nodes.update(all.map(id => ({id, opacity: connected.includes(id) || id===n ? 1 : 0.25 })));
      data.edges.update(data.edges.get().map(e => ({id:e.id, color: (e.from===n || e.to===n) ? '#2563eb' : '#94a3b8' })));
    });
  }

  window.addEventListener('DOMContentLoaded', init);
})();
