(function () {
  const labels = ['4 weeks','6 weeks','8 weeks','12 weeks','15 weeks','30 weeks'];
  const recommended = [80,100,130,180,200,400];
  const low = [60,80,110,160,180,350];
  const high = [100,120,150,200,220,450];

  const plugin = {
    id: 'ranges',
    afterDatasetsDraw(chart) {
      const {ctx, scales} = chart;
      const meta = chart.getDatasetMeta(0);
      ctx.save();
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 2;
      meta.data.forEach((bar, i) => {
        const x = bar.x;
        const y1 = scales.y.getPixelForValue(low[i]);
        const y2 = scales.y.getPixelForValue(high[i]);
        ctx.beginPath();
        ctx.moveTo(x, y1); ctx.lineTo(x, y2); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x-6,y1); ctx.lineTo(x+6,y1); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(x-6,y2); ctx.lineTo(x+6,y2); ctx.stroke();
      });

      // shaded optimal region 180-220
      const yTop = scales.y.getPixelForValue(220);
      const yBottom = scales.y.getPixelForValue(180);
      ctx.fillStyle = 'rgba(34,197,94,0.12)';
      ctx.fillRect(scales.x.left, yTop, scales.x.right - scales.x.left, yBottom - yTop);

      ctx.fillStyle = '#166534';
      ctx.font = '12px Arial';
      ctx.fillText('Optimal range for semester courses (180-220)', scales.x.left + 8, yTop - 4);

      const x15 = meta.data[4].x;
      const y15 = meta.data[4].y;
      ctx.fillStyle = '#1f2937';
      ctx.fillText('Standard semester course', x15 + 16, y15 - 8);

      const x30 = meta.data[5].x;
      const y30 = meta.data[5].y;
      ctx.fillText('Split into fall/spring learning graphs', x30 - 120, y30 - 24);
      ctx.restore();
    }
  };

  function init() {
    document.querySelector('main').innerHTML = '<div style="height:560px;padding:12px;background:#f8fafc"><canvas id="c"></canvas></div>';
    new Chart(document.getElementById('c'), {
      type: 'bar',
      data: {
        labels,
        datasets: [{
          label: 'Recommended Concept Count',
          data: recommended,
          backgroundColor: '#3b82f6',
          borderColor: '#1d4ed8',
          borderWidth: 1.5
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          title: {display:true, text:'Recommended Concept Count by Course Duration', font:{size:18}},
          legend: {display:true}
        },
        scales: {
          x: { title: {display:true, text:'Course Duration'} },
          y: { beginAtZero:true, max:500, title:{display:true, text:'Recommended Concept Count'} }
        }
      },
      plugins: [plugin]
    });
  }

  window.addEventListener('DOMContentLoaded', init);
})();
