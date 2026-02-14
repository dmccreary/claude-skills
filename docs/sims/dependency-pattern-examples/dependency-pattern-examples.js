(function () {
  const info = {
    A1: 'Sequential chain: linear progression through skill levels.',
    D1: 'Fan-in: multiple prerequisites converge on one advanced concept.',
    F1: 'Fan-out: one foundational concept enables multiple branches.'
  };

  function init() {
    const main = document.querySelector('main');
    main.style.display = 'grid';
    main.style.gridTemplateColumns = '70% 30%';
    main.style.height = '600px';
    main.innerHTML = `
      <section style="padding:10px;background:#f8fafc;overflow:auto;"><div id="mmd" class="mermaid">
flowchart LR
  subgraph S1[Sequential Chain]
    A1[A] --> B1[B] --> C1[C] --> D1a[D]
  end

  subgraph S2[Fan-In / Convergence]
    A2[Course Description] --> D2[Learning Graph\nGeneration]
    B2[Bloom's Taxonomy] --> D2
    C2[Prompt Engineering] --> D2
  end

  subgraph S3[Fan-Out / Divergence]
    F1[Claude Code Interface] --> G1[File Access]
    F1 --> G2[Command Execution]
    F1 --> G3[Tool Integration]
  end

  classDef node fill:#60a5fa,stroke:#1e3a8a,color:#111,font-size:15px
  class A1,B1,C1,D1a,A2,B2,C2,D2,F1,G1,G2,G3 node
  linkStyle default stroke:#111827,stroke-width:2px
      </div></section>
      <section style="padding:12px;border-left:1px solid #e2e8f0;background:#fff;">
        <h3 style="margin:0 0 10px 0;">Pattern Annotations</h3>
        <p style="margin:0 0 6px 0;color:#166534;">Sequential: common in staged skill acquisition.</p>
        <p style="margin:0 0 6px 0;color:#166534;">Fan-in: advanced concepts require integration.</p>
        <p style="margin:0;color:#166534;">Fan-out: foundational concepts are highly leveraged.</p>
      </section>
    `;

    mermaid.initialize({startOnLoad:false,theme:'default',flowchart:{htmlLabels:true,useMaxWidth:true}});
    mermaid.run({nodes:[document.getElementById('mmd')]});
  }

  window.addEventListener('DOMContentLoaded', init);
})();
