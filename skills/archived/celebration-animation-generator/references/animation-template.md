# Animation Template

This is the standard template for creating a new celebration animation module. Replace all `[PLACEHOLDERS]` with appropriate values.

## File Header

```javascript
// [filename].js - Self-contained celebration animation
// [Brief description of what the animation shows]
// Copy this file into your MicroSim folder to use
//
// Usage:
//   1. Include this file in your main.html: <script src="[filename].js"></script>
//   2. Call create[Name](params) when celebration should trigger
//   3. Call updateAndDraw[Name]() in your draw() loop
//
// Example:
//   function onGameWin() {
//     create[Name](canvasWidth/2, drawHeight);
//   }
//   function draw() {
//     // ... your drawing code ...
//     updateAndDraw[Name](); // Draw celebration on top
//   }
```

## Complete Template

```javascript
// [filename].js - Self-contained celebration animation
// [Brief description]
// Copy this file into your MicroSim folder to use
//
// Usage:
//   1. Include this file in your main.html: <script src="[filename].js"></script>
//   2. Call create[Name](centerX, startY) when celebration should trigger
//   3. Call updateAndDraw[Name]() in your draw() loop

let [uniqueParticleArrayName] = [];

// Standard rainbow colors for variety
const [uniqueColorsName] = [
  '#FF6B6B', '#FF8E53', '#FFD93D', '#6BCB77',
  '#4D96FF', '#9B59B6', '#FF6B9D'
];

/**
 * Create [animation name] celebration
 * @param {number} centerX - X position to start from
 * @param {number} startY - Y position to start from
 * @param {number} speedMultiplier - Speed adjustment (default 1.0, use 1.8 for fast, 0.5 for slow)
 */
function create[Name](centerX, startY, speedMultiplier = 1.0) {
  [uniqueParticleArrayName] = [];
  for (let i = 0; i < [PARTICLE_COUNT]; i++) {
    // Calculate initial position and velocity based on motion pattern
    let angle = random([ANGLE_RANGE]);
    let speed = random([SPEED_RANGE]) * speedMultiplier;
    let particleColor = color([uniqueColorsName][floor(random([uniqueColorsName].length))]);

    [uniqueParticleArrayName].push({
      x: centerX,
      y: startY,
      vx: cos(angle) * speed,
      vy: sin(angle) * speed,
      size: random([SIZE_RANGE]),
      rotation: random(-0.3, 0.3),
      rotationSpeed: random(-0.08, 0.08) * speedMultiplier,
      alpha: 255,
      fadeRate: [FADE_RATE] * speedMultiplier,
      color: particleColor,
      gravity: [GRAVITY] * speedMultiplier
      // Add any animation-specific properties here
    });
  }
}

/**
 * Update physics and draw all particles
 * Call this in your draw() loop
 */
function updateAndDraw[Name]() {
  for (let i = [uniqueParticleArrayName].length - 1; i >= 0; i--) {
    let p = [uniqueParticleArrayName][i];

    // Update physics
    p.x += p.vx;
    p.y += p.vy;
    p.vy += p.gravity;  // Apply gravity if used
    p.rotation += p.rotationSpeed;
    p.alpha -= p.fadeRate;

    // Draw the object
    push();
    translate(p.x, p.y);
    rotate(p.rotation);

    // [DRAWING CODE HERE]
    // Use p.color, p.alpha, p.size for consistency
    // Example:
    fill(red(p.color), green(p.color), blue(p.color), p.alpha);
    noStroke();
    ellipse(0, 0, p.size);

    pop();

    // Remove faded particles
    if (p.alpha <= 0) {
      [uniqueParticleArrayName].splice(i, 1);
    }
  }
}

/**
 * Check if the animation is still playing
 * @returns {boolean} True if particles are still visible
 */
function is[Name]Active() {
  return [uniqueParticleArrayName].length > 0;
}

/**
 * Clear all particles immediately
 */
function clear[Name]() {
  [uniqueParticleArrayName] = [];
}

// Add any helper drawing functions with unique suffix
// Example: function draw[Object][Suffix](x, y, size) { ... }
```

## Motion Pattern Templates

### Burst Up (like Book Burst)
Objects shoot upward from a point, arc, and fall with gravity.

```javascript
function create[Name](centerX, startY, speedMultiplier = 1.0) {
  [particleArray] = [];
  for (let i = 0; i < 20; i++) {
    let angle = random(-PI * 0.8, -PI * 0.2); // Upward arc spread
    let speed = random(8, 14) * speedMultiplier;
    [particleArray].push({
      x: centerX,
      y: startY,
      vx: cos(angle) * speed,
      vy: sin(angle) * speed,
      // ... other properties
      gravity: 0.15 * speedMultiplier
    });
  }
}
```

### Float Up (like Yellow Stars, Balloons)
Objects gently float upward with wobble.

```javascript
function create[Name](centerX, startY, spreadWidth = 200, speedMultiplier = 1.0) {
  [particleArray] = [];
  for (let i = 0; i < 25; i++) {
    [particleArray].push({
      x: centerX + random(-spreadWidth/2, spreadWidth/2),
      y: startY + random(-50, 0),
      vx: random(-1, 1) * speedMultiplier,
      vy: random(-2.5, -1.5) * speedMultiplier,
      wobble: random(0.02, 0.04) * speedMultiplier,
      wobbleOffset: random(TWO_PI),
      // ... other properties
    });
  }
}

// In updateAndDraw:
p.x += p.vx + sin(frameCount * p.wobble + p.wobbleOffset) * 0.3;
p.y += p.vy;
```

### Fall Down (like Confetti, Spark Shower)
Objects fall from top of screen.

```javascript
function create[Name](areaWidth, floorY, speedMultiplier = 1.0) {
  [particleArray] = [];
  for (let i = 0; i < 80; i++) {
    [particleArray].push({
      x: random(areaWidth),
      y: random(-100, -10), // Start above screen
      vx: random(-1, 1) * speedMultiplier,
      vy: random(3, 5) * speedMultiplier,
      wobble: random(0.03, 0.08) * speedMultiplier,
      floorY: floorY,
      // ... other properties
    });
  }
}

// In updateAndDraw - remove when past floor:
if (p.y > p.floorY + 30) {
  p.alpha = 0;
}
```

### Explode Out (like Rainbow Sparkle Burst)
Objects radiate outward from center point.

```javascript
function create[Name](centerX, centerY, speedMultiplier = 1.0) {
  [particleArray] = [];
  for (let i = 0; i < 60; i++) {
    let angle = random(TWO_PI); // All directions
    let speed = random(3, 6) * speedMultiplier;
    [particleArray].push({
      x: centerX,
      y: centerY,
      vx: cos(angle) * speed,
      vy: sin(angle) * speed,
      // ... other properties
    });
  }
}

// In updateAndDraw - slow down over time:
p.vx *= 0.98;
p.vy *= 0.98;
```

### Zoom Across (like Reading Rockets)
Objects move horizontally across screen.

```javascript
function create[Name](areaWidth, areaHeight, speedMultiplier = 1.0) {
  [particleArray] = [];
  for (let i = 0; i < 8; i++) {
    let startSide = random() > 0.5;
    let baseSpeed = random(5, 8) * speedMultiplier;
    [particleArray].push({
      x: startSide ? -30 : areaWidth + 30,
      y: random(80, areaHeight - 80),
      vx: startSide ? baseSpeed : -baseSpeed,
      vy: random(-0.5, 0.5) * speedMultiplier,
      areaWidth: areaWidth,
      trail: [],
      // ... other properties
    });
  }
}

// In updateAndDraw - remove when off screen:
if (p.x < -50 || p.x > p.areaWidth + 50) {
  p.alpha = 0;
}
```

## Drawing Examples

### Simple Circle
```javascript
fill(red(p.color), green(p.color), blue(p.color), p.alpha);
noStroke();
ellipse(0, 0, p.size);
```

### Circle with Dark Edge (for visibility on light backgrounds)
```javascript
stroke(80, 80, 120, p.alpha * 0.9);
strokeWeight(1.5);
fill(red(p.color), green(p.color), blue(p.color), p.alpha);
ellipse(0, 0, p.size);
```

### Star Shape
```javascript
fill(red(p.color), green(p.color), blue(p.color), p.alpha);
noStroke();
drawStarShape[Suffix](0, 0, p.size / 2, p.size, 5);

// Helper function (use unique suffix!)
function drawStarShape[Suffix](x, y, radius1, radius2, npoints) {
  let angle = TWO_PI / npoints;
  let halfAngle = angle / 2.0;
  beginShape();
  for (let a = -PI / 2; a < TWO_PI - PI / 2; a += angle) {
    let sx = x + cos(a) * radius2;
    let sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = x + cos(a + halfAngle) * radius1;
    sy = y + sin(a + halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}
```

### Rectangle (for confetti)
```javascript
fill(red(p.color), green(p.color), blue(p.color), p.alpha);
noStroke();
rect(-p.width / 2, -p.height / 2, p.width, p.height, 2);
```

### Sports Ball (Baseball example)
```javascript
// Ball body
fill(255, 255, 255, p.alpha);
stroke(200, 200, 200, p.alpha);
strokeWeight(1);
ellipse(0, 0, p.size);

// Red stitching
stroke(200, 50, 50, p.alpha);
strokeWeight(1.5);
noFill();
arc(-p.size * 0.15, 0, p.size * 0.5, p.size * 0.8, -PI/2, PI/2);
arc(p.size * 0.15, 0, p.size * 0.5, p.size * 0.8, PI/2, -PI/2);
```

## Integration Checklist

After creating the animation file, update these files:

### 1. main.html - Add script import
```html
<script src="../shared/animations/[filename].js"></script>
```

### 2. animation-lib-tester.js - Add to animationTypes array
```javascript
let animationTypes = [
  'Book Burst',
  // ... existing animations ...
  '[Display Name]'  // Add new animation
];
```

### 3. animation-lib-tester.js - Add updateAndDraw call in draw()
```javascript
// In draw() function, after existing updateAndDraw calls:
updateAndDraw[Name]();
```

### 4. animation-lib-tester.js - Add clear call in triggerCelebration()
```javascript
// In triggerCelebration(), after existing clear calls:
clear[Name]();
```

### 5. animation-lib-tester.js - Add case in switch statement
```javascript
case '[Display Name]':
  create[Name](canvasWidth / 2, drawHeight, speedMultiplier);
  break;
```

### 6. README.md - Add to documentation table
```markdown
| `[filename].js` | [Display Name] | [Brief description] |
```

### 7. README.md - Add API section
```markdown
### [Display Name]
\`\`\`javascript
create[Name](centerX, startY, speedMultiplier = 1.0)
\`\`\`
[Description of what the animation does and how to use it.]
```
