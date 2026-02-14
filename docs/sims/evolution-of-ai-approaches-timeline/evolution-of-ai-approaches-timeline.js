(function () {
  const events = [
    ["1957-01-01", "Perceptron", "Foundations", "Rosenblatt introduces the perceptron, one of the first trainable neural network models."],
    ["1958-01-01", "LISP", "Foundations", "LISP becomes a core language for symbolic AI research."],
    ["1965-01-01", "ELIZA", "Foundations", "Early natural language chatbot demonstrates pattern-based conversation."],
    ["1969-01-01", "Perceptrons Critique", "Foundations", "Minsky and Papert highlight limitations of single-layer perceptrons."],
    ["1974-01-01", "First AI Winter", "Foundations", "Funding and optimism decline as systems fail to scale."],
    ["1980-01-01", "Expert Systems Boom", "Foundations", "Rule-based systems see major commercial adoption."],
    ["1986-01-01", "Backpropagation", "Foundations", "Backpropagation is popularized for training multi-layer networks."],
    ["1989-01-01", "LeNet", "Foundations", "Convolutional networks show strong performance on digit recognition."],
    ["1997-05-11", "Deep Blue", "Foundations", "IBM Deep Blue defeats world chess champion Garry Kasparov."],
    ["2001-01-01", "Random Forests", "Foundations", "Ensemble learning methods become practical baselines for ML."],
    ["2006-01-01", "Deep Learning Revival", "Foundations", "Layer-wise pretraining revives deep neural network research."],
    ["2009-01-01", "ImageNet Dataset", "Foundations", "Large-scale labeled datasets accelerate supervised computer vision."],
    ["2011-01-01", "IBM Watson", "Foundations", "Watson wins Jeopardy!, showcasing industrial NLP systems."],

    ["2012-09-01", "AlexNet", "Vision", "Deep CNNs dramatically improve ImageNet benchmark performance."],
    ["2013-01-01", "Word2Vec", "Vision", "Distributed word vectors become a standard NLP representation."],
    ["2014-06-01", "Seq2Seq", "Vision", "Encoder-decoder sequence modeling enables modern neural translation."],
    ["2014-10-01", "GANs", "Vision", "Generative adversarial networks introduce adversarial generative learning."],
    ["2015-12-10", "ResNet", "Vision", "Residual connections allow very deep neural networks to train reliably."],
    ["2016-03-15", "AlphaGo", "Vision", "DeepMind AlphaGo defeats Lee Sedol, a milestone in planning + deep learning."],

    ["2017-06-01", "Attention Is All You Need", "Transformers", "Transformer architecture introduces self-attention as the core mechanism."],
    ["2018-06-01", "GPT-1", "Transformers", "Generative pretraining + fine-tuning shows transfer learning for NLP."],
    ["2018-10-01", "BERT", "Transformers", "Bidirectional transformers become dominant for language understanding."],
    ["2019-02-14", "GPT-2", "Transformers", "Larger generative models demonstrate coherent long-form text generation."],
    ["2019-10-01", "T5", "Transformers", "Text-to-text framing unifies many NLP tasks in one architecture."],

    ["2020-05-28", "GPT-3", "LLMs", "175B-parameter LLM enables strong few-shot text generation."],
    ["2021-01-05", "DALL-E", "LLMs", "Text-to-image generation starts to become mainstream."],
    ["2021-01-14", "CLIP", "LLMs", "Joint vision-language models unlock zero-shot image classification."],
    ["2021-06-29", "GitHub Copilot", "LLMs", "AI-assisted coding reaches wide developer adoption."],
    ["2022-01-27", "InstructGPT", "LLMs", "RLHF improves helpfulness and instruction-following behavior."],
    ["2022-11-30", "ChatGPT", "LLMs", "Conversational AI adoption scales globally."],
    ["2023-03-14", "GPT-4", "LLMs", "Multimodal and stronger reasoning capabilities expand use cases."],

    ["2021-01-01", "Anthropic Founded", "Claude", "Anthropic is founded with a focus on AI safety and reliability."],
    ["2022-12-15", "Constitutional AI Paper", "Claude", "Constitutional AI formalizes preference modeling via principles."],
    ["2023-03-14", "Claude 1", "Claude", "Claude is released for early users and partners."],
    ["2023-07-11", "Claude 2", "Claude", "Long-context assistance and improved writing/coding support."],
    ["2024-03-04", "Claude 3 Family", "Claude", "Haiku, Sonnet, and Opus models launch with stronger performance."],
    ["2024-06-20", "Artifacts", "Claude", "Interactive artifact workflows improve iterative content creation."],
    ["2024-10-22", "Extended Thinking", "Claude", "Reasoning-focused workflows become first-class capabilities."],

    ["2024-05-01", "Claude Code", "DevTools", "Terminal-native assistant workflows for software and content projects."],
    ["2024-11-25", "MCP Protocol", "DevTools", "Model Context Protocol enables tool/resource integration patterns."],
    ["2025-01-15", "Skill Pattern Matures", "DevTools", "Reusable skill workflows standardize agent task execution."],
    ["2025-02-10", "Claude Skills Announced", "DevTools", "Claude Skills announcement formalizes modular capability packages."],

    ["2012-01-01", "Dropout", "Foundations", "Regularization via dropout improves generalization in deep nets."],
    ["2013-01-01", "RNN Language Modeling", "Foundations", "Neural language models begin to outperform classic n-gram baselines."],
    ["2015-01-01", "Batch Normalization", "Foundations", "Batch norm stabilizes and speeds up training for deep architectures."],
    ["2016-01-01", "Neural Machine Translation", "Transformers", "End-to-end neural translation becomes practical at production scale."],
    ["2018-01-01", "Transformer XL", "Transformers", "Long-range dependency modeling improves context handling."],
    ["2020-01-01", "Retrieval-Augmented Generation", "LLMs", "RAG combines retrieval with generation for grounded responses."],
    ["2021-01-01", "Instruction Tuning", "LLMs", "Instruction-following behavior improves through task mixture finetuning."],
    ["2023-01-01", "Open-Weights Momentum", "LLMs", "Open model ecosystem expands experimentation and deployment options."],
    ["2024-01-01", "Long-Context Race", "LLMs", "Vendors compete on context windows for large document workflows."],
    ["2025-01-01", "Agentic Workflows", "DevTools", "Tool-using assistants become standard in developer productivity."],
    ["2025-06-01", "Textbook Automation", "DevTools", "Educational content pipelines integrate graph, glossary, and quiz generation."]
  ];

  const categoryColors = {
    Foundations: "#2563eb",
    Vision: "#0ea5e9",
    Transformers: "#7c3aed",
    LLMs: "#10b981",
    Claude: "#f59e0b",
    DevTools: "#ef4444"
  };

  let selectedCategory = "All";

  function createLayout() {
    document.body.style.margin = "0";
    document.body.style.fontFamily = "Arial, Helvetica, sans-serif";
    const main = document.querySelector("main");
    main.innerHTML = `
      <section style="padding:12px; background:linear-gradient(120deg,#0f172a,#1e293b); color:white;">
        <h1 style="margin:0; font-size:24px;">Evolution of AI Approaches Timeline</h1>
        <p style="margin:6px 0 0 0; opacity:.9;">52 milestones from 1957 to 2025 across six AI eras</p>
      </section>
      <section style="padding:10px; border-bottom:1px solid #e5e7eb; display:flex; flex-wrap:wrap; gap:8px;" id="filters"></section>
      <section id="timeline" style="height:470px; border-bottom:1px solid #e5e7eb;"></section>
      <section id="details" style="padding:10px; background:#f8fafc; min-height:130px;">
        <strong>Event details</strong>
        <p style="margin:6px 0 0 0;">Click an event to view full context.</p>
      </section>
    `;

    const filters = ["All", ...Object.keys(categoryColors)];
    const filterHost = document.getElementById("filters");
    filters.forEach((cat) => {
      const btn = document.createElement("button");
      btn.textContent = cat;
      btn.style.border = "1px solid #cbd5e1";
      btn.style.borderRadius = "999px";
      btn.style.padding = "6px 10px";
      btn.style.cursor = "pointer";
      btn.style.background = cat === "All" ? "#111827" : "white";
      btn.style.color = cat === "All" ? "white" : "#111827";
      btn.onclick = () => {
        selectedCategory = cat;
        [...filterHost.children].forEach((c) => {
          c.style.background = "white";
          c.style.color = "#111827";
        });
        btn.style.background = "#111827";
        btn.style.color = "white";
        renderTimeline();
      };
      filterHost.appendChild(btn);
    });
  }

  let timeline;
  function buildItems() {
    const filtered = selectedCategory === "All"
      ? events
      : events.filter((e) => e[2] === selectedCategory);

    return filtered.map((e, i) => ({
      id: i + 1,
      content: e[1],
      start: e[0],
      title: `${e[1]} (${e[2]})`,
      className: `cat-${e[2]}`,
      category: e[2],
      description: e[3]
    }));
  }

  function addDynamicCategoryStyles() {
    const style = document.createElement("style");
    const css = Object.entries(categoryColors).map(([k, v]) =>
      `.vis-item.cat-${k}{background:${v};border-color:${v};color:#fff;}`
    ).join("\n");
    style.textContent = css;
    document.head.appendChild(style);
  }

  function renderTimeline() {
    const container = document.getElementById("timeline");
    const items = new vis.DataSet(buildItems());
    const options = {
      stack: false,
      horizontalScroll: true,
      zoomKey: "ctrlKey",
      maxHeight: 470,
      min: "1955-01-01",
      max: "2026-12-31",
      orientation: "top",
      tooltip: { followMouse: true, overflowMethod: "cap" }
    };

    if (timeline) timeline.destroy();
    timeline = new vis.Timeline(container, items, options);

    timeline.on("select", (props) => {
      const id = props.items[0];
      if (!id) return;
      const ev = items.get(id);
      document.getElementById("details").innerHTML = `
        <strong>${ev.content}</strong> <span style="color:#475569;">(${ev.start.slice(0,4)} • ${ev.category})</span>
        <p style="margin:6px 0 0 0;">${ev.description}</p>
      `;
    });
  }

  window.addEventListener("DOMContentLoaded", () => {
    createLayout();
    addDynamicCategoryStyles();
    renderTimeline();
  });
})();
