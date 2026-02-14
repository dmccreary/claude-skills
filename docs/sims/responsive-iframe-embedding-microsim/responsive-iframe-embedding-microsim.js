let wSlider, hSlider, responsiveCheck, borderCheck;

function setup() {
  const c = createCanvas(1020, 680);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  wSlider = createSlider(300, 1200, 1000, 10); wSlider.position(740, 120); wSlider.style('width', '240px');
  hSlider = createSlider(200, 800, 600, 10); hSlider.position(740, 170); hSlider.style('width', '240px');
  responsiveCheck = createCheckbox('Responsive Wrapper', false); responsiveCheck.position(740, 220);
  borderCheck = createCheckbox('Show Frame Border', true); borderCheck.position(740, 250);
  createButton('Reset').position(740, 290).mousePressed(() => location.reload());
}

function drawFrame(x, y, w, h, label, col) {
  fill(col); stroke('#334155'); rect(x, y, w, h, 8);
  noStroke(); fill('#0f172a'); textSize(12); text(label, x + 8, y + 18);
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Responsive Iframe Embedding Demo', 16, 32);

  const vw = wSlider.value();
  const vh = hSlider.value();

  const scale = min(680 / vw, 560 / vh);
  const ox = 24, oy = 70;
  const pageW = vw * scale, pageH = vh * scale;

  drawFrame(ox, oy, pageW, pageH, 'MkDocs Page', '#e5e7eb');

  let iframeW = responsiveCheck.checked() ? pageW - 70 : 560 * scale;
  let iframeH = responsiveCheck.checked() ? iframeW * 0.6 : 340 * scale;
  const ix = ox + 30, iy = oy + 40;

  fill('#ffffff'); stroke(borderCheck.checked() ? '#0f172a' : '#e5e7eb'); rect(ix, iy, iframeW, iframeH, 6);
  noStroke(); fill('#334155'); textSize(12); text('Iframe Boundary', ix + 8, iy + 18);

  drawFrame(ix + 12, iy + 28, max(80, iframeW - 24), max(50, iframeH - 40), 'MicroSim Canvas', '#dbeafe');

  fill('#ffffff'); stroke('#cbd5e1'); rect(720, 70, 290, 580, 10);
  noStroke(); fill('#0f172a'); textSize(16); text('Controls', 736, 100);
  textSize(13); text(`Viewport Width: ${vw}px`, 736, 116);
  text(`Viewport Height: ${vh}px`, 736, 166);
  text(`Iframe: ${round(iframeW / scale)} x ${round(iframeH / scale)} px`, 736, 340);

  fill('#334155'); textSize(12);
  text('Gray = parent page\nWhite = iframe boundary\nBlue = embedded simulation\nToggle responsive mode to see clipping vs scaling behavior.', 736, 390, 250, 140);
}
