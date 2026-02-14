(function () {
  const labels = [
    "MicroSims with parameter controls",
    "Self-grading quizzes with explanations",
    "Interactive graph visualizations",
    "Code playgrounds with instant execution",
    "Clickable infographics (progressive disclosure)",
    "Embedded videos with checkpoints",
    "Accordion sections",
    "Static diagrams with zoom"
  ];
  const values = [92, 87, 84, 81, 76, 68, 52, 45];

  const barColors = labels.map((_, i) => i < 3 ? "#b45309" : "#fbbf24");

  const annotationPlugin = {
    id: "customNotes",
    afterDatasetsDraw(chart) {
      const { ctx, scales } = chart;
      ctx.save();
      ctx.fillStyle = "#334155";
      ctx.font = "12px Arial";

      const y0 = chart.getDatasetMeta(0).data[0].y;
      const y2 = chart.getDatasetMeta(0).data[2].y;
      const xBracket = scales.x.getPixelForValue(95);

      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(xBracket, y0 - 12);
      ctx.lineTo(xBracket + 10, y0 - 12);
      ctx.lineTo(xBracket + 10, y2 + 12);
      ctx.lineTo(xBracket, y2 + 12);
      ctx.stroke();
      ctx.fillText("Highest engagement", xBracket + 14, y0 + 4);
      ctx.fillText("prioritize in textbook design", xBracket + 14, y0 + 20);

      const yMicro = chart.getDatasetMeta(0).data[0].y;
      const xMicro = scales.x.getPixelForValue(92);
      ctx.beginPath();
      ctx.moveTo(xMicro + 10, yMicro - 20);
      ctx.lineTo(xMicro + 70, yMicro - 45);
      ctx.stroke();
      ctx.fillText("Enables experimentation", xMicro + 74, yMicro - 48);
      ctx.fillText("and discovery learning", xMicro + 74, yMicro - 34);

      ctx.fillStyle = "#475569";
      ctx.fillText("Data synthesized from educational research on digital learning", 16, chart.height - 8);
      ctx.restore();
    }
  };

  function init() {
    const main = document.querySelector("main");
    main.innerHTML = `
      <div style="height:560px;padding:12px;background:#fffbeb;">
        <canvas id="engagementChart"></canvas>
      </div>
    `;

    const ctx = document.getElementById("engagementChart");
    new Chart(ctx, {
      type: "bar",
      data: {
        labels,
        datasets: [{
          label: "Engagement Score",
          data: values,
          backgroundColor: barColors,
          borderColor: "#78350f",
          borderWidth: 1.2
        }]
      },
      options: {
        indexAxis: "y",
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          title: {
            display: true,
            text: "Student Engagement by Interactive Element Type",
            color: "#111827",
            font: { size: 18 }
          },
          tooltip: {
            callbacks: {
              label: (ctx2) => ` Engagement score: ${ctx2.parsed.x}/100`
            }
          }
        },
        scales: {
          x: {
            min: 0,
            max: 100,
            title: { display: true, text: "Engagement score (0-100)" },
            grid: { color: "#fde68a" }
          },
          y: {
            ticks: { color: "#1f2937", font: { size: 12 } }
          }
        }
      },
      plugins: [annotationPlugin]
    });
  }

  window.addEventListener("DOMContentLoaded", init);
})();
