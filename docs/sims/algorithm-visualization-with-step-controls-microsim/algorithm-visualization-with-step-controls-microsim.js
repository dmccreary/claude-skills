let arr = [];
let i = 0, j = 0, sortedFrom = -1, comparisons = 0;
let autoRun = false, lastStep = 0;
let speedSlider;

function resetArray(size = 12) {
  arr = Array.from({ length: size }, () => Math.floor(random(20, 260)));
  i = 0; j = 0; sortedFrom = arr.length; comparisons = 0; autoRun = false;
}

function oneStep() {
  if (i >= arr.length - 1) return;
  comparisons++;
  if (arr[j] > arr[j + 1]) {
    const t = arr[j]; arr[j] = arr[j + 1]; arr[j + 1] = t;
  }
  j++;
  if (j >= arr.length - i - 1) {
    sortedFrom = arr.length - i - 1;
    i++; j = 0;
  }
}

function setup() {
  const c = createCanvas(940, 640);
  c.parent(document.querySelector('main'));
  textFont('Arial');

  createButton('Step Forward').position(640, 110).mousePressed(oneStep);
  createButton('Step to End of Pass').position(740, 110).mousePressed(() => {
    const target = arr.length - i - 1;
    while (j < target) oneStep();
  });
  createButton('Reset').position(640, 146).mousePressed(() => resetArray(arr.length));
  createButton('Auto Run').position(700, 146).mousePressed(() => autoRun = !autoRun);

  speedSlider = createSlider(100, 2000, 500, 50);
  speedSlider.position(640, 190);
  speedSlider.style('width', '220px');

  const sizeSelect = createSelect();
  sizeSelect.position(640, 226);
  [5, 8, 12, 16].forEach((v) => sizeSelect.option(String(v)));
  sizeSelect.selected('12');
  sizeSelect.changed(() => resetArray(Number(sizeSelect.value())));

  resetArray(12);
}

function drawBars() {
  const x0 = 24, yBase = 560, w = 560;
  const bw = w / arr.length;
  for (let k = 0; k < arr.length; k++) {
    if (k >= sortedFrom) fill('#22c55e');
    else fill('#3b82f6');
    if (k === j || k === j + 1) fill('#f59e0b');
    rect(x0 + k * bw, yBase - arr[k], bw - 4, arr[k], 4);
  }
}

function draw() {
  background('#f8fafc');
  fill('#0f172a'); textSize(22); text('Algorithm Visualization with Step Controls', 16, 30);
  fill('#ffffff'); stroke('#cbd5e1'); rect(12, 46, 600, 580, 10);
  noStroke();
  drawBars();

  fill('#ffffff'); stroke('#cbd5e1'); rect(624, 46, 304, 580, 10);
  noStroke(); fill('#0f172a'); textSize(14);
  text(`Pass: ${i + 1}`, 640, 86);
  text(`Comparisons: ${comparisons}`, 640, 320);
  text(`State: comparing index ${j} and ${j + 1}`, 640, 348, 260, 60);
  text(`Speed: ${speedSlider.value()}ms`, 640, 178);
  text('Array Size', 640, 220);

  if (autoRun && millis() - lastStep > speedSlider.value()) {
    oneStep();
    lastStep = millis();
  }
}
