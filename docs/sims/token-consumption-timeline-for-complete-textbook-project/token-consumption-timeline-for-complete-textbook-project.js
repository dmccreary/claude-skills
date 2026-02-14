(function () {
  const milestones = [
    ['2026-01-01','Course description',8000,'Foundation'],
    ['2026-01-02','Learning graph generation',45000,'Foundation'],
    ['2026-01-03','Glossary generation',20000,'Support'],
    ['2026-01-04','Chapter outline',8000,'Support'],
    ['2026-01-06','Chapters batch 1',90000,'Content'],
    ['2026-01-09','Chapters batch 2',90000,'Content'],
    ['2026-01-12','Chapters batch 3',120000,'Content'],
    ['2026-01-15','Chapters batch 4',90000,'Content'],
    ['2026-01-17','Quiz batches',40000,'Content'],
    ['2026-01-19','MicroSim specs day 1',5000,'Enhancement'],
    ['2026-01-20','MicroSim specs day 2',5000,'Enhancement']
  ];

  const colorMap = {
    Foundation: '#3b82f6',
    Support: '#8b5cf6',
    Content: '#16a34a',
    Enhancement: '#f97316'
  };

  function init() {
    document.querySelector('main').innerHTML = `
      <div style="padding:10px;font-family:Arial,sans-serif;">
        <h2 style="margin:0 0 6px 0;">Token Consumption Timeline for Complete Textbook Project</h2>
        <p style="margin:0 0 8px 0;color:#475569;">Total project: ~530,000 tokens over ~20 days.</p>
        <div id="timeline" style="height:260px;border:1px solid #cbd5e1;"></div>
        <canvas id="area" height="220" style="margin-top:10px;border:1px solid #e2e8f0;background:#fff;"></canvas>
        <div id="detail" style="margin-top:8px;padding:8px;border:1px solid #e2e8f0;background:#f8fafc;color:#334155;">Hover timeline milestones for phase and token totals.</div>
      </div>`;

    const items = milestones.map((m, i) => ({
      id: i + 1,
      content: m[1],
      start: m[0],
      title: `${m[1]}: ${m[2].toLocaleString()} tokens`,
      style: `background:${colorMap[m[3]]};border-color:${colorMap[m[3]]};color:white;`
    }));

    const ds = new vis.DataSet(items);
    const tl = new vis.Timeline(document.getElementById('timeline'), ds, {
      min: '2025-12-31', max: '2026-01-22', orientation: 'top', zoomable: false, moveable: false
    });

    tl.on('select', (p) => {
      if (!p.items.length) return;
      const it = items[p.items[0]-1];
      document.getElementById('detail').textContent = `${it.content} | ${it.title}`;
    });

    let cumulative = 0;
    const labels = [];
    const values = [];
    milestones.forEach((m) => {
      cumulative += m[2];
      labels.push(m[0].slice(5));
      values.push(cumulative);
    });

    new Chart(document.getElementById('area'), {
      type: 'line',
      data: { labels, datasets: [{ label:'Cumulative tokens', data: values, fill:true, borderColor:'#2563eb', backgroundColor:'rgba(37,99,235,0.2)', tension:0.25 }] },
      options: {
        responsive:true,
        plugins:{legend:{display:true}},
        scales:{y:{beginAtZero:true,title:{display:true,text:'Cumulative tokens'}},x:{title:{display:true,text:'Day (MM-DD)'}}}
      }
    });
  }

  window.addEventListener('DOMContentLoaded', init);
})();
