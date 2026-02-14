(function () {
  const chapters = ['Ch 1', 'Ch 2', 'Ch 3', 'Ch 4', 'Ch 5'];
  const datasets = [
    { label: 'Remember', data: [5, 6, 4, 7, 5], color: 'rgba(239,68,68,0.75)' },
    { label: 'Understand', data: [7, 8, 9, 8, 7], color: 'rgba(249,115,22,0.75)' },
    { label: 'Apply', data: [4, 5, 6, 5, 6], color: 'rgba(234,179,8,0.75)' },
    { label: 'Analyze', data: [2, 3, 3, 2, 3], color: 'rgba(34,197,94,0.75)' },
    { label: 'Evaluate', data: [1, 1, 2, 2, 1], color: 'rgba(59,130,246,0.75)' },
    { label: 'Create', data: [1, 0, 1, 1, 1], color: 'rgba(139,92,246,0.75)' }
  ];

  let grouped = false;
  let chart;

  const annotations = {
    id: 'totalLabels',
    afterDatasetsDraw(c) {
      const { ctx } = c;
      const totals = chapters.map((_, i) => datasets.reduce((acc, d) => acc + d.data[i], 0));
      ctx.save();
      ctx.font = '12px Arial';
      ctx.fillStyle = '#334155';
      totals.forEach((t, i) => {
        const x = c.scales.x.getPixelForValue(i);
        const y = c.scales.y.getPixelForValue(t) - 8;
        ctx.textAlign = 'center';
        ctx.fillText(`${t} questions`, x, y);
      });
      ctx.restore();
    }
  };

  function buildConfig() {
    return {
      type: 'bar',
      data: {
        labels: chapters,
        datasets: datasets.map((d) => ({
          label: d.label,
          data: d.data,
          backgroundColor: d.color,
          borderColor: d.color.replace('0.75', '1'),
          borderWidth: 1,
          stack: grouped ? undefined : 'total'
        }))
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { mode: 'nearest', intersect: true },
        plugins: {
          title: {
            display: true,
            text: "Bloom's Taxonomy Distribution Analyzer",
            font: { size: 20 }
          },
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              label(ctx) {
                const total = datasets.reduce((acc, d) => acc + d.data[ctx.dataIndex], 0);
                const pct = Math.round((ctx.parsed.y / total) * 100);
                return `${ctx.dataset.label}: ${ctx.parsed.y} (${pct}%)`;
              }
            }
          }
        },
        scales: {
          x: { stacked: !grouped, title: { display: true, text: 'Quiz Chapter' } },
          y: { stacked: !grouped, beginAtZero: true, title: { display: true, text: 'Number of Questions' } }
        }
      },
      plugins: [annotations]
    };
  }

  function init() {
    const main = document.querySelector('main');
    main.innerHTML = `
      <div style="padding:12px;background:#f8fafc;height:620px;box-sizing:border-box;">
        <div style="margin-bottom:8px;display:flex;gap:8px;align-items:center;">
          <button id="toggle" style="padding:6px 10px;">Switch to Grouped</button>
          <span style="font-size:12px;color:#475569;">Click legend items to show/hide Bloom levels.</span>
        </div>
        <canvas id="chart"></canvas>
      </div>`;

    const ctx = document.getElementById('chart');
    chart = new Chart(ctx, buildConfig());

    document.getElementById('toggle').addEventListener('click', () => {
      grouped = !grouped;
      chart.destroy();
      chart = new Chart(ctx, buildConfig());
      document.getElementById('toggle').textContent = grouped ? 'Switch to Stacked' : 'Switch to Grouped';
    });
  }

  window.addEventListener('DOMContentLoaded', init);
})();
