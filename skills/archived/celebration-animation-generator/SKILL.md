---
name: celebration-animation-generator
description: This skill generates self-contained p5.js celebration animations for educational MicroSims. Use this skill when users request creating new celebration animations, particle effects, reward animations, or visual feedback for student achievements. The skill creates a new animation JavaScript file in /docs/sims/shared/animations/ and integrates it with the animation-lib-tester MicroSim for testing.
---

# Celebration Animation Generator

## Overview

This skill generates self-contained p5.js celebration animation modules for the reading-for-kindergarten intelligent textbook project. Each animation is a single JavaScript file that can be copied into any MicroSim folder to provide visual celebration feedback when students complete tasks correctly.

## When to Use This Skill

Use this skill when users request:
- Creating a new celebration animation (e.g., "baseballs exploding", "butterflies flying")
- Adding particle effects for student rewards
- Generating visual feedback animations for educational games
- Expanding the celebration animation library

## Workflow

### Step 1: Parse the Animation Request

Extract from the user's description:
1. **Object/Shape**: What is being animated (baseballs, hearts, butterflies, etc.)
2. **Motion Pattern**: How it moves (exploding, floating, falling, zooming, etc.)
3. **Origin Point**: Where it starts (bottom center, top, sides, center, etc.)
4. **Suggested Name**: Derive a kebab-case filename (e.g., "baseball-explosion.js")

### Step 2: Generate the Animation File

Create a new JavaScript file in `/docs/sims/shared/animations/` following the template pattern in `references/animation-template.md`.

Key requirements:
- Use a **unique particle array name** (e.g., `baseballExplosionParticles`)
- Use a **unique suffix for helper functions** to avoid conflicts (e.g., `drawBaseballBE()`)
- Include all four standard API functions:
  - `create[Name](params, speedMultiplier)` - Initialize particles
  - `updateAndDraw[Name]()` - Physics and rendering
  - `is[Name]Active()` - Check if animation is playing
  - `clear[Name]()` - Stop animation immediately
- Support `speedMultiplier` parameter (0.5=slow, 1.0=medium, 1.8=fast)
- Use the standard rainbow color palette for variety

### Step 3: Update the Animation Library Tester

After creating the animation file, update `/docs/sims/animation-lib-tester/` to include the new animation:

1. **main.html**: Add a new `<script>` import for the animation file
2. **animation-lib-tester.js**:
   - Add the animation name to the `animationTypes` array
   - Add `updateAndDraw[Name]()` call in the `draw()` function
   - Add `clear[Name]()` call in the `triggerCelebration()` function
   - Add a new case in the switch statement to trigger the animation

### Step 4: Update the README

Add the new animation to `/docs/sims/shared/animations/README.md`:
- Add row to the "Available Animations" table
- Add API documentation section with function signature and description

## Animation Patterns Reference

### Motion Patterns

| Pattern | Description | Example Use |
|---------|-------------|-------------|
| Burst Up | Objects shoot upward from a point with gravity | Book Burst, Alphabet Fireworks |
| Float Up | Objects gently float upward | Yellow Stars, Balloons |
| Fall Down | Objects fall from top | Happy Star Sprinkle, Confetti, Spark Shower |
| Explode Out | Objects radiate outward from center | Rainbow Sparkle Burst, Magic Book Bloom |
| Zoom Across | Objects move horizontally | Reading Rocket Zoom |
| Pop/Bounce | Objects appear, bounce, then pop | Giggle Glitter Pop |

### Standard Color Palette

```javascript
const rainbowColors = [
  '#FF6B6B', // red
  '#FF8E53', // orange
  '#FFD93D', // yellow
  '#6BCB77', // green
  '#4D96FF', // blue
  '#9B59B6', // purple
  '#FF6B9D'  // pink
];
```

### Common Particle Properties

```javascript
{
  x, y,           // Position
  vx, vy,         // Velocity
  size,           // Size/radius
  alpha,          // Transparency (0-255)
  fadeRate,       // How fast alpha decreases
  rotation,       // Current angle
  rotationSpeed,  // Angular velocity
  color,          // p5.js color object
  gravity,        // Downward acceleration (for burst patterns)
  wobble,         // Oscillation factor (for floating patterns)
  trail: []       // Array of past positions (for trail effects)
}
```

## File Naming Convention

- Use kebab-case for filename: `baseball-explosion.js`
- Use PascalCase for function names: `createBaseballExplosion()`
- Use camelCase for particle array: `baseballExplosionParticles`
- Add unique suffix to helper functions: `drawBaseballBE()`

## Example: Creating "Baseball Explosion"

For request: "Baseballs exploding from the bottom middle of the screen"

1. **Filename**: `baseball-explosion.js`
2. **Motion**: Burst Up pattern (like Book Burst)
3. **Object**: Baseball with red stitching
4. **Functions**:
   - `createBaseballExplosion(centerX, startY, speedMultiplier)`
   - `updateAndDrawBaseballExplosion()`
   - `isBaseballExplosionActive()`
   - `clearBaseballExplosion()`

## Resources

### references/animation-template.md
Contains the complete template for a new animation file with all required functions and documentation structure.
