// Automatic alignment of both the label and value to the left of sliders
// create a div and use the inline-block display style to align the label and value to the left of the slider control.
// canvas dimensions
let canvasWidth = 240;
let drawHeight = 240;
let controlHeight = 50;
let canvasHeight = drawHeight + controlHeight;

// sliders
let radiusSlider;
let strokeSlider;
let radiusValue;
let strokeValue;

function setup() {
  createCanvas(canvasWidth, canvasHeight);

  // Global font for all DOM controls
  document.body.style.fontFamily =
    'system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif';

  // ---- Radius Control Row ----
  let radiusRow = createDiv();
  radiusRow.position(10, drawHeight+5);

  // Create the label, value and slider control
  let radiusLabel = createSpan('Radius: ');
  radiusLabel.parent(radiusRow);
  styleLabel(radiusLabel);

  radiusValue = createSpan('40');
  radiusValue.parent(radiusRow);
  styleValue(radiusValue);

  radiusSlider = createSlider(10, 80, 40, 1);
  radiusSlider.parent(radiusRow);

  // ---- Stroke Width Control Row ----
  let strokeRow = createDiv();
  strokeRow.position(10, drawHeight + 25);

  let strokeLabel = createSpan('Border: ');
  strokeLabel.parent(strokeRow);
  styleLabel(strokeLabel);

  strokeValue = createSpan('4');
  strokeValue.parent(strokeRow);
  styleValue(strokeValue);

  strokeSlider = createSlider(0, 10, 4, 1);
  strokeSlider.parent(strokeRow);
}

function draw() {
  fill('aliceblue');
  stroke('silver');
  strokeWeight(1);
  // make the background of the drawing region lightblue
  rect(0,0, canvasWidth, drawHeight);
  // make the background of the control region white
  fill('white');
  rect(0, drawHeight, canvasWidth, controlHeight);
  
  let radius = radiusSlider.value();
  let strokeW = strokeSlider.value();

  // Update displayed values
  radiusValue.html(radius);
  strokeValue.html(strokeW);

  stroke('blue');
  strokeWeight(strokeW);
  fill('cornflowerblue');

  circle(width / 2, drawHeight / 2, radius * 2);
}

// ---- Shared styling helpers for the label and values ----
function styleLabel(el) {
  el.style('display', 'inline-block');
  el.style('width', '60px');
}

function styleValue(el) {
  el.style('display', 'inline-block');
  el.style('width', '30px');
}
