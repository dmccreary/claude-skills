(function () {
  const events = [
    ['2026-02-14T09:00:00', 'Generate Chapter 1', -30000],
    ['2026-02-14T09:30:00', 'Generate glossary', -15000],
    ['2026-02-14T11:00:00', 'Generate Chapter 2', -30000],
    ['2026-02-14T13:00:00', 'Restore 9:00 tokens', +30000],
    ['2026-02-14T13:30:00', 'Restore 9:30 tokens', +15000],
    ['2026-02-14T15:00:00', 'Restore 11:00 tokens', +30000],
    ['2026-02-14T17:00:00', 'Fully replenished', 0]
  ];

  function render() {
    const main = document.querySelector('main');
    main.innerHTML = `
      <div style="padding:10px;font-family:Arial,sans-serif;">
        <h2 style="margin:0 0 6px 0;">5-Hour Token Window Visualization</h2>
        <p style="margin:0 0 8px 0;color:#475569;">12-hour view of token consumption and rolling restoration.</p>
        <div id="timeline" style="height:260px;border:1px solid #cbd5e1;"></div>
        <div id="bars" style="margin-top:10px;display:grid;grid-template-columns:repeat(7,1fr);gap:8px;height:220px;"></div>
        <div id="detail" style="margin-top:8px;padding:8px;border:1px solid #e2e8f0;background:#f8fafc;color:#334155;">Hover bars or click timeline events for token details.</div>
      </div>
    `;

    const data = new vis.DataSet(events.map((e, i) => ({
      id: i + 1,
      content: e[1],
      start: e[0],
      className: e[2] < 0 ? 'consume' : (e[2] > 0 ? 'restore' : 'neutral'),
      delta: e[2]
    })));

    const style = document.createElement('style');
    style.textContent = `.vis-item.consume{background:#f97316;border-color:#c2410c;color:#fff}
      .vis-item.restore{background:#16a34a;border-color:#166534;color:#fff}
      .vis-item.neutral{background:#64748b;border-color:#334155;color:#fff}`;
    document.head.appendChild(style);

    const timeline = new vis.Timeline(document.getElementById('timeline'), data, {
      min: '2026-02-14T08:30:00',
      max: '2026-02-14T17:30:00',
      zoomMin: 1000 * 60 * 30,
      zoomMax: 1000 * 60 * 60 * 12,
      orientation: 'top'
    });

    let available = 100000;
    const bars = document.getElementById('bars');
    events.forEach((e, idx) => {
      available += e[2];
      const used = 100000 - available;
      const col = document.createElement('div');
      col.style.display = 'flex';
      col.style.flexDirection = 'column';
      col.style.justifyContent = 'flex-end';
      col.style.border = '1px solid #e2e8f0';
      col.style.background = '#fff';
      col.style.padding = '4px';

      const usedBar = document.createElement('div');
      usedBar.style.height = `${Math.max(0, used / 1000)}px`;
      usedBar.style.background = '#f97316';
      usedBar.title = `Consumed: ${used.toLocaleString()}`;

      const availBar = document.createElement('div');
      availBar.style.height = `${Math.max(0, available / 1000)}px`;
      availBar.style.background = '#3b82f6';
      availBar.title = `Available: ${available.toLocaleString()}`;

      const label = document.createElement('div');
      label.style.fontSize = '11px';
      label.style.marginTop = '4px';
      label.style.textAlign = 'center';
      label.textContent = new Date(e[0]).toLocaleTimeString([], {hour: 'numeric', minute:'2-digit'});

      col.appendChild(usedBar);
      col.appendChild(availBar);
      col.appendChild(label);
      col.onmouseenter = () => {
        document.getElementById('detail').textContent = `${e[1]} | delta ${e[2] > 0 ? '+' : ''}${e[2].toLocaleString()} | available ${available.toLocaleString()}`;
      };
      bars.appendChild(col);
    });

    timeline.on('select', (props) => {
      if (!props.items.length) return;
      const it = data.get(props.items[0]);
      document.getElementById('detail').textContent = `${it.content}: ${it.delta > 0 ? '+' : ''}${it.delta.toLocaleString()} tokens at ${new Date(it.start).toLocaleTimeString()}`;
    });
  }

  window.addEventListener('DOMContentLoaded', render);
})();
