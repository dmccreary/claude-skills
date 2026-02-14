(function () {
  const containerStyle = 'height:560px;border:1px solid #cbd5e1;background:#f8fafc;';
  const nodes = [
    { id: 1, label: 'Learning Graphs', level: 0, color: '#7c3aed', font: {color:'#fff'} },
    { id: 2, label: 'Learning Graph', level: 1 },
    { id: 3, label: 'Concept Nodes', level: 1 },
    { id: 4, label: 'Dependency Edges', level: 1 },
    { id: 5, label: 'DAG', level: 1 },
    { id: 6, label: 'Prerequisite Relationships', level: 2 },
    { id: 7, label: 'Concept Dependencies', level: 2 },
    { id: 8, label: 'Learning Pathways', level: 2 },
    { id: 9, label: 'Graph Traversal', level: 2 },
    { id:10, label: 'Topological Sorting', level: 2 },
    { id:11, label: 'Circular Detection', level: 2 },
    { id:12, label: 'Visualization', level: 2 },
    { id:13, label: 'Concept Granularity', level: 2 },
    { id:14, label: 'Atomic Concepts', level: 2 },
    { id:15, label: 'Label Standards', level: 2 }
  ];
  const edges = [];
  for (let i = 2; i <= 15; i++) edges.push({ from: 1, to: i, arrows: 'to' });
  [[2,6],[4,7],[5,10],[5,11],[3,14],[3,15],[7,8],[9,10],[12,8]].forEach(([a,b])=>edges.push({from:a,to:b,arrows:'to',color:'#64748b'}));

  function render() {
    document.querySelector('main').innerHTML = `
      <div style="padding:8px;font-family:Arial,sans-serif;">
        <h2 style="margin:0 0 6px 0;">Topic-to-Concept Expansion Example</h2>
        <p style="margin:0 0 8px 0;color:#475569;">1 topic -> 10-20 concepts typical expansion</p>
        <div id="net" style="${containerStyle}"></div>
      </div>`;

    const data = { nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) };
    const options = {
      layout: { hierarchical: { enabled: true, direction: 'UD', sortMethod: 'directed', levelSeparation: 110, nodeSpacing: 120 } },
      nodes: { shape:'box', color:'#bfdbfe', borderWidth:1.5, font:{size:14} },
      edges: { smooth:true, color:'#334155' },
      physics: false,
      interaction: { hover: true }
    };
    new vis.Network(document.getElementById('net'), data, options);
  }

  window.addEventListener('DOMContentLoaded', render);
})();
