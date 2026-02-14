(function () {
  const labels = ['Remember','Understand','Apply','Analyze','Evaluate','Create'];
  const values = [10,20,25,20,15,10];
  const colors = ['#ef4444','#f97316','#eab308','#22c55e','#3b82f6','#8b5cf6'];

  const annot = {
    id: 'annot',
    afterDatasetsDraw(chart) {
      const { ctx, chartArea } = chart;
      const x0 = chart.scales.x.getPixelForValue(0);
      const x45 = chart.scales.x.getPixelForValue(45);
      const x90 = chart.scales.x.getPixelForValue(90);
      const y = chart.getDatasetMeta(0).data[0].y;

      ctx.save();
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(x0, y - 48); ctx.lineTo(x45, y - 48); ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(x45, y - 66); ctx.lineTo(x90, y - 66); ctx.stroke();

      ctx.fillStyle = '#334155';
      ctx.font = '12px Arial';
      ctx.fillText('45% Lower-order (foundational)', x0 + 2, y - 60);
      ctx.fillText('45% Higher-order (mastery)', x45 + 2, y - 78);
      ctx.fillText('Distribution should match target audience sophistication.', chartArea.left, chartArea.bottom + 24);
      ctx.restore();
    }
  };

  function init() {
    document.querySelector('main').innerHTML = '<div style="height:520px;padding:12px;background:#f8fafc"><canvas id="c"></canvas></div>';
    new Chart(document.getElementById('c'), {
      type: 'bar',
      data: {
        labels: ['Recommended Distribution'],
        datasets: labels.map((l, i) => ({ label: l, data: [values[i]], backgroundColor: colors[i], borderWidth: 1 }))
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: { display: true, text: 'Recommended Learning Outcome Distribution for Graduate-Level Courses', font: { size: 18 } },
          tooltip: { callbacks: { label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.x}%` } },
          legend: { position: 'bottom' }
        },
        scales: {
          x: { stacked: true, min: 0, max: 100, title: { display: true, text: 'Percentage of Learning Outcomes' } },
          y: { stacked: true }
        }
      },
      plugins: [annot]
    });
  }

  window.addEventListener('DOMContentLoaded', init);
})();
