// Bouncing Ball example - use as a template for other sims
// This simulation shows a ball bouncing around inside a drawing region.
// The design is width responsive so it adjusts to the width of container as it resizes.
// Note that the width of the slider must also change with a window resize event
// MicroSim template version 2026.02

// global variables for width and height
let containerWidth; // this values is calculated by container upon init and changed on resize
// the temporary width of the entire canvas
let canvasWidth = 400;
// A fixed top drawing region above the interactive controls
// Do not place any controls such as buttons or sliders in the drawing region
let drawHeight = 400;
// The control region has all the user interface controls (buttons, sliders with labels and values)
// control region height - use 30 pixels for each slider
let controlHeight = 30;
// The total hight of both the drawing region height + the control region height
let canvasHeight = drawHeight + controlHeight;
let containerHeight = canvasHeight; // fixed height on page determined by MicroSim author

// margin around the active plotting region
let margin = 25;
// the left margin of the slider to provide room for the labels and values
let sliderLeftMargin = 160;
// larger text so students in the back of the room can read the labels
let defaultTextSize = 16;

// application specific global variables
let r = 20; // radius of the ball

// set the initial position of the ball in the middle of the drawing region
let x = canvasWidth/2;
let y = drawHeight/2;
let speed = 3; // default speed
// direction of motion
let dx = speed;
let dy = speed;
// global variable for speed slider since the resize function needs to access it
let speedSlider;
// Start/Pause button and running state
let startButton;
let isRunning = false; // default state is paused

function setup() {
  updateCanvasSize() // set the container dimensions to get the correct container width
  const canvas = createCanvas(containerWidth, containerHeight);
  var mainElement = document.querySelector('main');
  canvas.parent(mainElement);

  textSize(16);

  // Create Start/Pause button
  startButton = createButton('Start');
  startButton.position(10, drawHeight + 5);
  startButton.mousePressed(toggleSimulation);

  speedSlider = createSlider(0, 20, speed);
  speedSlider.position(sliderLeftMargin, drawHeight + 5);
  speedSlider.size(canvasWidth - sliderLeftMargin - margin);

  describe('Interactive bouncing ball simulation with speed control and start/pause button', LABEL);
}

function draw() {
  // check for window resize
  updateCanvasSize();

  // fill drawing area with very light blue background - MicroSim standard style
  fill('aliceblue');
  // draw a light gray border around the both the drawing region and the control region
  stroke('silver');
  strokeWeight(1);
  rect(0, 0, canvasWidth, drawHeight);

  // fill control area with a white background
  fill('white');
  rect(0, drawHeight, canvasWidth, canvasHeight-drawHeight); 
  // get the new speed from the UI
  speed = speedSlider.value();

  // Title
  fill('black');
  noStroke();
  textAlign(CENTER, TOP);
  textSize(32);
  text('Bouncing Ball Simulation', canvasWidth/2, margin);
  // stroke();

  // Only update position when running
  if (isRunning) {
    // adjust the x and y directions
    if (dx > 0) dx = speed;
       else dx = -speed;

    if (dy > 0) dy = speed;
       else dy = -speed;

    // Add the current speed to the position.
    x += dx;
    y += dy;

    // checks for edges right or left
    if ((x > width-r) || (x < r)) {
      dx = dx * -1; // change direction
    }
    if ((y > drawHeight - r) || (y < r)) {
      dy = dy * -1;
    }
  }

  // draw the ball
  fill('blue');
  circle(x, y, r*2);

  // draw the label and value for the speed slider
  // use text align RIGHT if you have many rows of sliders
  fill('black');
  // Always put a noStroke() before any text - no exceptions
  noStroke();
  textAlign(LEFT, CENTER);
  textSize(defaultTextSize);
  // Note that the label and values are both in a single text - do not separate
  text('Speed: ' + speed, 70, drawHeight+15);
}

// Toggle between running and paused states
function toggleSimulation() {
  isRunning = !isRunning;
  startButton.html(isRunning ? 'Pause' : 'Start');
}

// These two functions must be present for width responsiveness MicroSims
// this function is called whenever the browser window is resized
function windowResized() {
  // Update canvas size when the container resizes
  updateCanvasSize();
  resizeCanvas(containerWidth, containerHeight);
  // resize the speed slider and any other sliders here
  speedSlider.size(canvasWidth - sliderLeftMargin - margin);
  redraw();
}

function updateCanvasSize() {
  // Get the width of the <main> element
  const container = document.querySelector('main').getBoundingClientRect();
  containerWidth = Math.floor(container.width);  // Avoid fractional pixels
  // update the canvas width to be the container width
  canvasWidth = containerWidth;
}