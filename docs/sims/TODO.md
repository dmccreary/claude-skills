# MicroSim Screenshot TODO

This file tracks MicroSims that need screenshots captured.

**Generated:** 2026-01-28
**Total Missing:** 6 screenshots

## Missing Screenshots

Run the following commands to capture missing screenshots:

### book-build-workflow

```bash
~/.local/bin/bk-capture-screenshot docs/sims/book-build-workflow
```

### certificate-generator

```bash
~/.local/bin/bk-capture-screenshot docs/sims/certificate-generator
```

### claude-code-memory-layers

```bash
~/.local/bin/bk-capture-screenshot docs/sims/claude-code-memory-layers
```

### claude-code-tshirt-design

```bash
~/.local/bin/bk-capture-screenshot docs/sims/claude-code-tshirt-design
```

### graph-color-test

```bash
~/.local/bin/bk-capture-screenshot docs/sims/graph-color-test
```

### three-color-dfs

```bash
~/.local/bin/bk-capture-screenshot docs/sims/three-color-dfs
```

## Batch Capture Command

To capture all missing screenshots at once, run:

```bash
~/.local/bin/bk-capture-screenshot docs/sims/book-build-workflow && \
~/.local/bin/bk-capture-screenshot docs/sims/certificate-generator && \
~/.local/bin/bk-capture-screenshot docs/sims/claude-code-memory-layers && \
~/.local/bin/bk-capture-screenshot docs/sims/claude-code-tshirt-design && \
~/.local/bin/bk-capture-screenshot docs/sims/graph-color-test && \
~/.local/bin/bk-capture-screenshot docs/sims/three-color-dfs
```

## Notes

- The screenshot capture tool uses Chrome headless mode
- Default wait time is 3 seconds for JavaScript to render
- For complex animations, add a delay parameter: `~/.local/bin/bk-capture-screenshot docs/sims/<name> 5`
- Screenshots are saved as `<microsim-name>.png` in the MicroSim directory
