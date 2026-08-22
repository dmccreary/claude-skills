---
title: Color Wheel with Named Colors
description: An interactive color wheel displaying web-safe named colors. Hover over any color dot to see the color name, RGB values, and hex code.
image: /sims/color-wheel-with-named-colors/color-wheel-with-named-colors.png
og:image: /sims/color-wheel-with-named-colors/color-wheel-with-named-colors.png
twitter:image: /sims/color-wheel-with-named-colors/color-wheel-with-named-colors.png
social:
   cards: false
---

# Color Wheel with Named Colors

<iframe src="main.html" height="462px" width="100%" scrolling="no"></iframe>

[Run the Color Wheel MicroSim Fullscreen](./main.html){ .md-button .md-button--primary }
<br/>
[Edit the Color Wheel MicroSim with the p5.js editor](https://editor.p5js.org/)

## Embedding This MicroSim

You can include this MicroSim on your website using the following `iframe`:

```html
<iframe src="https://dmccreary.github.io/ibook-skills/sims/color-wheel-with-named-colors/main.html" height="462px" scrolling="no"></iframe>
```

## Description

This interactive MicroSim displays a color wheel with dots representing over 80 web-safe named colors. Each color dot is positioned on the wheel based on its hue value, with the saturation determining how far from the center the dot appears.

When you hover over any color dot:

- The color name is displayed in bold
- The RGB values are shown (e.g., RGB(255, 0, 0))
- The hexadecimal color code is displayed (e.g., #FF0000)
- The hue angle in degrees is shown

## Learning Objectives

After using this MicroSim, students will be able to:

1. **Remember** - Recall common web-safe color names and their approximate positions on the color wheel
2. **Understand** - Explain the relationship between a color's hue and its position on the color wheel
3. **Apply** - Use appropriate named colors in web design projects
4. **Analyze** - Compare similar colors and understand the differences in their RGB values

## Color Organization

The colors are organized on the wheel according to their hue:

- **Reds (0-30 degrees)**: Red, Crimson, Tomato, Coral
- **Oranges (30-60 degrees)**: Orange, DarkOrange, Gold
- **Yellows (60-90 degrees)**: Yellow, Khaki, Chartreuse
- **Greens (90-150 degrees)**: Lime, Green, SeaGreen
- **Cyan-Blues (150-210 degrees)**: Cyan, Turquoise, SkyBlue
- **Blues (210-270 degrees)**: Blue, DodgerBlue, Navy
- **Purples (270-330 degrees)**: Purple, Violet, Magenta
- **Pinks (330-360 degrees)**: Pink, HotPink, DeepPink

## Technical Details

- **Framework**: p5.js
- **Number of Colors**: 82 web-safe named colors
- **Color Positioning**: Based on HSL color model hue and saturation
- **Responsive**: Width-responsive design adapts to container size

## Lesson Plan

### Introduction (5 minutes)

Introduce students to the concept of named colors in web development. Explain that CSS supports over 140 named colors that can be used instead of hex codes or RGB values.

### Exploration (10 minutes)

Have students explore the color wheel:

1. Find all the shades of blue
2. Compare "Red" to "Crimson" to "DarkRed"
3. Locate complementary colors (opposite sides of the wheel)
4. Find colors with similar RGB values

### Application (10 minutes)

Students choose a color scheme for a hypothetical website:

1. Pick a primary color from the wheel
2. Find 2-3 complementary or analogous colors
3. Note the color names and RGB values

### Discussion (5 minutes)

Discuss when to use named colors vs. custom RGB/hex values. Named colors are easier to remember and read in code, but offer less precision than custom color values.

## Related Resources

- [MDN Web Docs: Color names](https://developer.mozilla.org/en-US/docs/Web/CSS/named-color)
- [W3Schools: CSS Colors](https://www.w3schools.com/colors/colors_names.asp)
- [Color Theory Basics](https://www.colormatters.com/color-and-design/basic-color-theory)
