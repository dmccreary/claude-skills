(function(){
  function init(){
    const main=document.querySelector('main');
    main.style.display='grid';main.style.gridTemplateColumns='68% 32%';main.style.height='640px';
    main.innerHTML=`<section style="padding:10px;background:#f8fafc;overflow:auto;"><div id="mmd" class="mermaid">
flowchart LR
  subgraph CSV[CSV Format]
    C1["ConceptID"]
    C2["ConceptLabel"]
    C3["Dependencies"]
    C4["TaxonomyID"]
  end

  subgraph JSON[JSON Output]
    N1["nodes[].id"]
    N2["nodes[].label"]
    N3["nodes[].group"]
    E1["edges[].from/to"]
  end

  C1 --> N1
  C2 --> N2
  C4 --> N3
  C3 -->|"split by |"| E1

  X1["Row: 2, Dependencies, 1, BASIC"] --> X2["Node: {id:2,label:'Dependencies',group:'BASIC'}"]
  X1 --> X3["Edge: {from:1,to:2}"]

  Y1["Row: 3, DAG, 1|2, ARCH"] --> Y2["Node: {id:3,label:'DAG',group:'ARCH'}"]
  Y1 --> Y3["Edges: {from:1,to:3} and {from:2,to:3}"]

  classDef direct fill:#fb923c,stroke:#9a3412,color:#111827,font-size:14px
  classDef xform fill:#a78bfa,stroke:#5b21b6,color:#111827,font-size:14px
  class C1,C2,C4,N1,N2,N3 direct
  class C3,E1,xform
  linkStyle default stroke:#1f2937,stroke-width:2px
    </div></section>
    <section style="padding:12px;border-left:1px solid #e2e8f0;background:#fff;"><h3 style="margin:0 0 10px 0;">Mapping Notes</h3><p style="margin:0 0 6px 0;color:#334155;font-size:14px;">Orange arrows: direct 1:1 mapping.</p><p style="margin:0 0 6px 0;color:#334155;font-size:14px;">Purple path: dependencies transformed into multiple edges.</p><p style="margin:0;color:#334155;font-size:14px;">Empty dependencies create foundational nodes with no incoming edges.</p></section>`;

    mermaid.initialize({startOnLoad:false,theme:'default',flowchart:{htmlLabels:true,useMaxWidth:true}});
    mermaid.run({nodes:[document.getElementById('mmd')]});
  }
  window.addEventListener('DOMContentLoaded',init);
})();
