let bgPicker, fgPicker;
let ratio = 1;
let info = { aa: false, aaa: false, warn: false };

const presets = [
  { label: 'FOUND', bg: '#ff6b6b' },
  { label: 'BASIC', bg: '#ffa94d' },
  { label: 'ARCH', bg: '#ffd43b' },
  { label: 'IMPL', bg: '#69db7c' },
  { label: 'TOOL', bg: '#4dabf7' },
  { label: 'ADV', bg: '#b197fc' }
];

function hexToRgb(hex) {
  const h = hex.replace('#', '');
  return {
    r: parseInt(h.substring(0, 2), 16),
    g: parseInt(h.substring(2, 4), 16),
    b: parseInt(h.substring(4, 6), 16)
  };
}

function linear(v) {
  const c = v / 255;
  return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
}

function luminance(rgb) {
  return 0.2126 * linear(rgb.r) + 0.7152 * linear(rgb.g) + 0.0722 * linear(rgb.b);
}

function contrastRatio(bg, fg) {
  const l1 = luminance(hexToRgb(bg));
  const l2 = luminance(hexToRgb(fg));
  const light = Math.max(l1, l2);
  const dark = Math.min(l1, l2);
  return (light + 0.05) / (dark + 0.05);
}

function optimalFont(bg) {
  const black = contrastRatio(bg, '#000000');
  const white = contrastRatio(bg, '#ffffff');
  return black >= white ? '#000000' : '#ffffff';
}

function updateMetrics() {
  ratio = contrastRatio(bgPicker.value(), fgPicker.value());
  info.aa = ratio >= 4.5;
  info.aaa = ratio >= 7.0;
  info.warn = ratio < 3.0;
}

function addPresetButtons() {
  let x = 434;
  let y = 332;
  presets.forEach((p) => {
    const b = createButton(p.label);
    b.position(x, y);
    b.size(58, 26);
    b.style('font-size', '11px');
    b.mousePressed(() => {
      bgPicker.value(p.bg);
      fgPicker.value(optimalFont(p.bg));
      updateMetrics();
    });
    x += 62;
    if (x > 738) {
      x = 434;
      y += 30;
    }
  });
}

function setup() {
  const c = createCanvas(820, 520);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  bgPicker = createColorPicker('#FFA94D');
  bgPicker.position(560, 96);
  bgPicker.input(updateMetrics);

  fgPicker = createColorPicker('#000000');
  fgPicker.position(560, 146);
  fgPicker.input(updateMetrics);

  const autoBtn = createButton('Auto-Calculate Optimal Font Color');
  autoBtn.position(430, 196);
  autoBtn.size(300, 30);
  autoBtn.mousePressed(() => {
    fgPicker.value(optimalFont(bgPicker.value()));
    updateMetrics();
  });

  addPresetButtons();
  updateMetrics();
}

function drawPassFail(y, threshold, label) {
  const pass = ratio >= threshold;
  fill(pass ? '#166534' : '#991b1b');
  textSize(16);
  text(pass ? 'PASS' : 'FAIL', 340, y);
  fill('#334155');
  textSize(12);
  text(label, 238, y);
}

function draw() {
  updateMetrics();
  background('#f8fafc');

  fill('#0f172a');
  textSize(22);
  text('Color Accessibility Checker', 16, 30);

  fill('#e2e8f0');
  noStroke();
  rect(10, 50, 400, 460, 10);
  fill('#e2e8f0');
  rect(420, 50, 390, 460, 10);

  const bg = bgPicker.value();
  const fg = fgPicker.value();
  fill(bg);
  rect(36, 86, 350, 250, 8);

  fill(fg);
  textSize(14);
  text('The quick brown fox jumps over the lazy dog', 54, 138);
  textSize(18);
  text('The quick brown fox jumps', 54, 186);
  textSize(24);
  text('Sample Heading', 54, 236);

  fill('#334155');
  textSize(14);
  text('WCAG checks on current colors:', 36, 366);
  drawPassFail(392, 4.5, 'AA normal text (>= 4.5:1)');
  drawPassFail(416, 3.0, 'AA large text (>= 3.0:1)');
  drawPassFail(440, 7.0, 'AAA normal text (>= 7.0:1)');

  fill('#0f172a');
  textSize(15);
  text('Controls', 432, 80);
  fill('#334155');
  textSize(13);
  text('Background Color', 432, 112);
  text('Font Color', 432, 162);

  fill('#0f172a');
  textSize(14);
  text(`Contrast Ratio: ${ratio.toFixed(2)}:1`, 432, 252);
  text(`WCAG AA: ${info.aa ? 'Pass' : 'Fail'}`, 432, 278);
  text(`WCAG AAA: ${info.aaa ? 'Pass' : 'Fail'}`, 432, 302);

  if (info.warn) {
    fill('#b91c1c');
    textSize(12);
    text('Warning: Contrast ratio is below 3.0 (severe accessibility issue).', 432, 434, 355, 40);
  }
}
