# Celebration Animation Template

Complete template for a new p5.js celebration animation module in
`/docs/sims/shared/animations/`. Copy this pattern, substitute `{{NAME}}` with the
PascalCase animation name (e.g. `BaseballExplosion`) and `{{SUFFIX}}` with a short unique
suffix for helper functions (e.g. `BE`), and fill in the particle physics for the requested
motion pattern (see celebration-guide.md's Motion Patterns table).

Every animation file MUST expose exactly these four functions, and nothing else global,
so multiple animation files can be loaded into the same MicroSim without colliding.

```javascript
/**
 * {{NAME}} celebration animation
 * Motion pattern: {{MOTION_PATTERN}}   e.g. Burst Up, Float Up, Fall Down, Explode Out
 * Origin: {{ORIGIN_POINT}}             e.g. bottom center, top, sides, center
 */

// Unique particle array name — must not collide with other loaded animations
let {{name}}Particles = [];

// Unique suffix on every helper function for the same reason
function draw{{SUFFIX}}(p) {
    push();
    translate(p.x, p.y);
    rotate(p.rotation);
    // Draw a single particle's shape here — the specific object/shape from
    // the animation request (baseballs, hearts, butterflies, etc).
    pop();
}

const {{name}}Colors = [
    '#FF6B6B', // red
    '#FF8E53', // orange
    '#FFD93D', // yellow
    '#6BCB77', // green
    '#4D96FF', // blue
    '#9B59B6', // purple
    '#FF6B9D'  // pink
];

/**
 * Initialize particles. Call once when the celebration should start.
 * @param {number} centerX - horizontal origin
 * @param {number} startY - vertical origin
 * @param {number} speedMultiplier - 0.5 = slow, 1.0 = medium, 1.8 = fast (default 1.0)
 */
function create{{NAME}}(centerX, startY, speedMultiplier = 1.0) {
    {{name}}Particles = [];
    const count = 30; // tune per animation
    for (let i = 0; i < count; i++) {
        {{name}}Particles.push({
            x: centerX,
            y: startY,
            vx: (random(-1, 1)) * speedMultiplier,
            vy: (random(-3, -1)) * speedMultiplier,
            size: random(8, 16),
            alpha: 255,
            fadeRate: random(2, 4),
            rotation: random(TWO_PI),
            rotationSpeed: random(-0.1, 0.1),
            color: color(random({{name}}Colors)),
            gravity: 0.15 // omit or set to 0 for float/zoom patterns
        });
    }
}

/**
 * Call every frame from draw(). Updates physics and renders all particles.
 * Removes particles once fully faded.
 */
function updateAndDraw{{NAME}}() {
    for (let i = {{name}}Particles.length - 1; i >= 0; i--) {
        const p = {{name}}Particles[i];

        p.x += p.vx;
        p.y += p.vy;
        p.vy += p.gravity || 0;
        p.rotation += p.rotationSpeed;
        p.alpha -= p.fadeRate;

        if (p.alpha <= 0) {
            {{name}}Particles.splice(i, 1);
            continue;
        }

        push();
        tint(255, p.alpha);
        fill(red(p.color), green(p.color), blue(p.color), p.alpha);
        draw{{SUFFIX}}(p);
        pop();
    }
}

/** True while any particle is still active. */
function is{{NAME}}Active() {
    return {{name}}Particles.length > 0;
}

/** Stop the animation immediately, discarding all particles. */
function clear{{NAME}}() {
    {{name}}Particles = [];
}
```

## Naming Checklist

Before saving the file, verify:

- [ ] Filename is kebab-case: `{{kebab-name}}.js`
- [ ] Particle array is camelCase with no suffix collision: `{{name}}Particles`
- [ ] All four API functions use the exact PascalCase name: `create{{NAME}}`,
      `updateAndDraw{{NAME}}`, `is{{NAME}}Active`, `clear{{NAME}}`
- [ ] Internal helper functions carry the unique suffix: `draw{{SUFFIX}}()`
- [ ] `speedMultiplier` scales velocity, not particle count or size
- [ ] No `console.log`, no global variables besides the particle array

## Integration Reminder

After creating the file, celebration-guide.md Step 3 requires wiring it into
`/docs/sims/animation-lib-tester/` (script import, `animationTypes` entry, `draw()` call,
`triggerCelebration()` call) and Step 4 requires a README entry in
`/docs/sims/shared/animations/README.md`.
