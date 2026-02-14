(function () {
  const labels = ['Iteration 1','Iteration 2','Iteration 3','Iteration 4','Iteration 5'];
  const quality = [45,62,78,88,91];
  const notes = [
    'Initial draft - missing concepts, wrong reading level',
    'Added concept coverage constraints - improved but verbose',
    'Refined reading-level parameters - closer to target',
    'Added interactive element specs - exceeds threshold',
    'Minor refinements - consistent quality achieved'
  ];

  const custom = {
    id: 'notes',
    afterDatasetsDraw(chart) {
      const { ctx } = chart;
      ctx.save();
      ctx.font = '12px Arial';
      ctx.fillStyle = '#334155';
      chart.getDatasetMeta(0).data.forEach((pt, i) => {
        ctx.fillText(notes[i], pt.x + 8, pt.y - 10);
      });
      ctx.restore();
    }
  };

  function init() {
    document.querySelector('main').innerHTML = '<div style="height:560px;padding:10px;background:#f8fafc;"><canvas id="c"></canvas></div>';
    new Chart(document.getElementById('c'), {
      type: 'line',
      data: {
        labels,
        datasets: [
          {
            label: 'Quality Score',
            data: quality,
            borderColor: '#2563eb',
            backgroundColor: 'rgba(37,99,235,0.12)',
            fill: false,
            tension: 0.25,
            pointRadius: 5
          },
          {
            label: 'Quality Threshold',
            data: labels.map(() => 85),
            borderColor: '#dc2626',
            borderDash: [8,6],
            pointRadius: 0
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { position: 'top' },
          title: { display: true, text: 'Prompt Quality Improvement Across Iterations', font: {size: 18} },
          tooltip: { callbacks: { label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y}` } }
        },
        scales: {
          y: {
            min: 0, max: 100,
            title: { display: true, text: 'Quality Score (0-100)' }
          },
          x: { title: { display: true, text: 'Iteration Number' } }
        }
      },
      plugins: [custom]
    });

    // shaded acceptable quality zone
    const zone = document.createElement('div');
    zone.style.position = 'absolute';
    zone.style.right = '18px';
    zone.style.top = '52px';
    zone.style.padding = '3px 8px';
    zone.style.background = '#dcfce7';
    zone.style.border = '1px solid #86efac';
    zone.style.font = '12px Arial';
    zone.textContent = 'Acceptable Quality Zone (>=85)';
    document.querySelector('main div').style.position = 'relative';
    document.querySelector('main div').appendChild(zone);
  }

  window.addEventListener('DOMContentLoaded', init);
})();
