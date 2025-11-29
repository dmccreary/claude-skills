// Color Wheel with Named Colors MicroSim
// This simulation displays a color wheel with dots representing web-safe named colors.
// Hover over any dot to see the color name and RGB values in the control region.

// Canvas dimensions
let canvasWidth = 400;
let drawHeight = 400;
let controlHeight = 60;
let canvasHeight = drawHeight + controlHeight;
let margin = 25;
let defaultTextSize = 16;

// Color wheel parameters
let wheelRadius;
let centerX;
let centerY;
let dotRadius = 10;

// Current hovered color
let hoveredColor = null;

// Web-safe named colors with their RGB values
// Organized by approximate hue position on the color wheel
const namedColors = [
    // Reds (0-15 degrees)
    { name: "Red", r: 255, g: 0, b: 0 },
    { name: "Crimson", r: 220, g: 20, b: 60 },
    { name: "DarkRed", r: 139, g: 0, b: 0 },
    { name: "FireBrick", r: 178, g: 34, b: 34 },
    { name: "IndianRed", r: 205, g: 92, b: 92 },

    // Red-Oranges (15-30 degrees)
    { name: "Tomato", r: 255, g: 99, b: 71 },
    { name: "Coral", r: 255, g: 127, b: 80 },
    { name: "OrangeRed", r: 255, g: 69, b: 0 },
    { name: "Salmon", r: 250, g: 128, b: 114 },
    { name: "LightSalmon", r: 255, g: 160, b: 122 },

    // Oranges (30-45 degrees)
    { name: "Orange", r: 255, g: 165, b: 0 },
    { name: "DarkOrange", r: 255, g: 140, b: 0 },
    { name: "SandyBrown", r: 244, g: 164, b: 96 },
    { name: "Peru", r: 205, g: 133, b: 63 },

    // Yellow-Oranges (45-60 degrees)
    { name: "Gold", r: 255, g: 215, b: 0 },
    { name: "Goldenrod", r: 218, g: 165, b: 32 },
    { name: "DarkGoldenrod", r: 184, g: 134, b: 11 },
    { name: "Moccasin", r: 255, g: 228, b: 181 },

    // Yellows (60-75 degrees)
    { name: "Yellow", r: 255, g: 255, b: 0 },
    { name: "LightYellow", r: 255, g: 255, b: 224 },
    { name: "Khaki", r: 240, g: 230, b: 140 },
    { name: "PaleGoldenrod", r: 238, g: 232, b: 170 },

    // Yellow-Greens (75-105 degrees)
    { name: "YellowGreen", r: 154, g: 205, b: 50 },
    { name: "GreenYellow", r: 173, g: 255, b: 47 },
    { name: "Chartreuse", r: 127, g: 255, b: 0 },
    { name: "LawnGreen", r: 124, g: 252, b: 0 },

    // Greens (105-150 degrees)
    { name: "Lime", r: 0, g: 255, b: 0 },
    { name: "LimeGreen", r: 50, g: 205, b: 50 },
    { name: "ForestGreen", r: 34, g: 139, b: 34 },
    { name: "Green", r: 0, g: 128, b: 0 },
    { name: "DarkGreen", r: 0, g: 100, b: 0 },
    { name: "SeaGreen", r: 46, g: 139, b: 87 },
    { name: "MediumSeaGreen", r: 60, g: 179, b: 113 },
    { name: "SpringGreen", r: 0, g: 255, b: 127 },
    { name: "PaleGreen", r: 152, g: 251, b: 152 },

    // Cyan-Greens (150-180 degrees)
    { name: "MediumAquamarine", r: 102, g: 205, b: 170 },
    { name: "Aquamarine", r: 127, g: 255, b: 212 },
    { name: "Turquoise", r: 64, g: 224, b: 208 },
    { name: "MediumTurquoise", r: 72, g: 209, b: 204 },
    { name: "LightSeaGreen", r: 32, g: 178, b: 170 },

    // Cyans (180-195 degrees)
    { name: "Cyan", r: 0, g: 255, b: 255 },
    { name: "Aqua", r: 0, g: 255, b: 255 },
    { name: "DarkCyan", r: 0, g: 139, b: 139 },
    { name: "Teal", r: 0, g: 128, b: 128 },
    { name: "PaleTurquoise", r: 175, g: 238, b: 238 },

    // Light Blues (195-210 degrees)
    { name: "LightCyan", r: 224, g: 255, b: 255 },
    { name: "CadetBlue", r: 95, g: 158, b: 160 },
    { name: "PowderBlue", r: 176, g: 224, b: 230 },
    { name: "LightBlue", r: 173, g: 216, b: 230 },
    { name: "SkyBlue", r: 135, g: 206, b: 235 },

    // Blues (210-240 degrees)
    { name: "DeepSkyBlue", r: 0, g: 191, b: 255 },
    { name: "DodgerBlue", r: 30, g: 144, b: 255 },
    { name: "CornflowerBlue", r: 100, g: 149, b: 237 },
    { name: "SteelBlue", r: 70, g: 130, b: 180 },
    { name: "RoyalBlue", r: 65, g: 105, b: 225 },
    { name: "Blue", r: 0, g: 0, b: 255 },
    { name: "MediumBlue", r: 0, g: 0, b: 205 },
    { name: "DarkBlue", r: 0, g: 0, b: 139 },
    { name: "Navy", r: 0, g: 0, b: 128 },

    // Blue-Violets (240-270 degrees)
    { name: "MediumSlateBlue", r: 123, g: 104, b: 238 },
    { name: "SlateBlue", r: 106, g: 90, b: 205 },
    { name: "DarkSlateBlue", r: 72, g: 61, b: 139 },
    { name: "BlueViolet", r: 138, g: 43, b: 226 },
    { name: "Indigo", r: 75, g: 0, b: 130 },

    // Purples/Violets (270-300 degrees)
    { name: "Purple", r: 128, g: 0, b: 128 },
    { name: "DarkViolet", r: 148, g: 0, b: 211 },
    { name: "DarkOrchid", r: 153, g: 50, b: 204 },
    { name: "MediumOrchid", r: 186, g: 85, b: 211 },
    { name: "Orchid", r: 218, g: 112, b: 214 },
    { name: "Violet", r: 238, g: 130, b: 238 },
    { name: "Plum", r: 221, g: 160, b: 221 },
    { name: "Magenta", r: 255, g: 0, b: 255 },
    { name: "Fuchsia", r: 255, g: 0, b: 255 },

    // Magentas/Pinks (300-330 degrees)
    { name: "MediumVioletRed", r: 199, g: 21, b: 133 },
    { name: "DeepPink", r: 255, g: 20, b: 147 },
    { name: "HotPink", r: 255, g: 105, b: 180 },
    { name: "PaleVioletRed", r: 219, g: 112, b: 147 },

    // Pinks/Roses (330-360 degrees)
    { name: "Pink", r: 255, g: 192, b: 203 },
    { name: "LightPink", r: 255, g: 182, b: 193 },
    { name: "MistyRose", r: 255, g: 228, b: 225 },
    { name: "LavenderBlush", r: 255, g: 240, b: 245 }
];

// Convert RGB to HSL and return hue in degrees (0-360)
function rgbToHue(r, g, b) {
    r /= 255;
    g /= 255;
    b /= 255;

    let max = Math.max(r, g, b);
    let min = Math.min(r, g, b);
    let h = 0;

    if (max === min) {
        h = 0; // achromatic
    } else {
        let d = max - min;
        switch (max) {
            case r:
                h = ((g - b) / d + (g < b ? 6 : 0)) / 6;
                break;
            case g:
                h = ((b - r) / d + 2) / 6;
                break;
            case b:
                h = ((r - g) / d + 4) / 6;
                break;
        }
    }

    return h * 360;
}

// Calculate saturation for positioning (distance from center)
function rgbToSaturation(r, g, b) {
    r /= 255;
    g /= 255;
    b /= 255;

    let max = Math.max(r, g, b);
    let min = Math.min(r, g, b);
    let l = (max + min) / 2;
    let s = 0;

    if (max !== min) {
        let d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
    }

    return s;
}

function setup() {
    updateCanvasSize();
    const canvas = createCanvas(canvasWidth, canvasHeight);
    var mainElement = document.querySelector('main');
    canvas.parent(mainElement);

    textSize(defaultTextSize);

    // Calculate color wheel parameters
    updateWheelParameters();

    // Calculate position for each color based on hue
    for (let c of namedColors) {
        c.hue = rgbToHue(c.r, c.g, c.b);
        c.saturation = rgbToSaturation(c.r, c.g, c.b);
    }

    describe('Interactive color wheel showing web-safe named colors. Hover over dots to see color names and RGB values.', LABEL);
}

function updateWheelParameters() {
    centerX = canvasWidth / 2;
    centerY = drawHeight / 2;
    wheelRadius = min(canvasWidth, drawHeight) / 2 - margin - 20;
}

function draw() {
    updateCanvasSize();
    updateWheelParameters();

    // Draw background
    fill('aliceblue');
    stroke('silver');
    strokeWeight(1);
    rect(0, 0, canvasWidth, drawHeight);

    // Control area background
    fill('white');
    noStroke();
    rect(0, drawHeight, canvasWidth, controlHeight);

    // Draw title
    fill('black');
    noStroke();
    textAlign(CENTER, TOP);
    textSize(24);
    text('Color Wheel with Named Colors', centerX, 10);

    // Draw color wheel background
    drawColorWheel();

    // Draw center circle (white)
    fill(255);
    stroke(200);
    strokeWeight(1);
    circle(centerX, centerY, 60);

    // Check for hover and draw color dots
    hoveredColor = null;
    let minDist = Infinity;

    for (let c of namedColors) {
        // Position based on hue (angle) and saturation (radius)
        let angle = radians(c.hue - 90); // -90 to start at top
        // Saturation determines distance from center (0.3 to 1.0 of wheel radius)
        let distFromCenter = map(c.saturation, 0, 1, wheelRadius * 0.35, wheelRadius * 0.92);

        let dotX = centerX + cos(angle) * distFromCenter;
        let dotY = centerY + sin(angle) * distFromCenter;

        // Store position for hover detection
        c.x = dotX;
        c.y = dotY;

        // Check if mouse is hovering over this dot
        let d = dist(mouseX, mouseY, dotX, dotY);
        if (d < dotRadius + 5 && d < minDist) {
            minDist = d;
            hoveredColor = c;
        }
    }

    // Draw all dots
    for (let c of namedColors) {
        let isHovered = (c === hoveredColor);

        // Draw dot with the actual color
        fill(c.r, c.g, c.b);
        stroke(isHovered ? 'black' : 'white');
        strokeWeight(isHovered ? 3 : 2);
        circle(c.x, c.y, (isHovered ? dotRadius * 1.5 : dotRadius) * 2);
    }

    // Draw control area content
    drawControlArea();
}

function drawColorWheel() {
    // Draw color wheel using HSB color mode
    push();
    colorMode(HSB, 360, 100, 100);
    noStroke();

    // Draw the wheel in segments
    let segments = 360;
    for (let i = 0; i < segments; i++) {
        let angle1 = radians(i - 90);
        let angle2 = radians(i + 1 - 90);

        // Draw gradient from center to edge
        for (let r = 30; r < wheelRadius; r += 3) {
            let sat = map(r, 30, wheelRadius, 0, 100);
            fill(i, sat, 100);

            let x1 = centerX + cos(angle1) * r;
            let y1 = centerY + sin(angle1) * r;
            let x2 = centerX + cos(angle2) * r;
            let y2 = centerY + sin(angle2) * r;
            let x3 = centerX + cos(angle2) * (r + 3);
            let y3 = centerY + sin(angle2) * (r + 3);
            let x4 = centerX + cos(angle1) * (r + 3);
            let y4 = centerY + sin(angle1) * (r + 3);

            quad(x1, y1, x2, y2, x3, y3, x4, y4);
        }
    }

    pop();

    // Draw wheel border
    noFill();
    stroke(100);
    strokeWeight(2);
    circle(centerX, centerY, wheelRadius * 2);
}

function drawControlArea() {
    fill('black');
    noStroke();
    textAlign(LEFT, CENTER);
    textSize(defaultTextSize);

    if (hoveredColor) {
        // Show color swatch
        fill(hoveredColor.r, hoveredColor.g, hoveredColor.b);
        stroke('black');
        strokeWeight(2);
        rect(15, drawHeight + 12, 36, 36, 5);

        // Show color name
        fill('black');
        noStroke();
        textSize(20);
        textStyle(BOLD);
        text(hoveredColor.name, 65, drawHeight + 22);

        // Show RGB values
        textSize(16);
        textStyle(NORMAL);
        let rgbText = `RGB(${hoveredColor.r}, ${hoveredColor.g}, ${hoveredColor.b})`;
        text(rgbText, 65, drawHeight + 44);

        // Show hex value
        let hexValue = '#' +
            hoveredColor.r.toString(16).padStart(2, '0').toUpperCase() +
            hoveredColor.g.toString(16).padStart(2, '0').toUpperCase() +
            hoveredColor.b.toString(16).padStart(2, '0').toUpperCase();

        textAlign(RIGHT, CENTER);
        text(hexValue, canvasWidth - 20, drawHeight + 22);

        // Show hue value
        text(`Hue: ${Math.round(hoveredColor.hue)}°`, canvasWidth - 20, drawHeight + 44);
    } else {
        // Show instruction
        textAlign(CENTER, CENTER);
        textSize(18);
        fill(100);
        text('Hover over a color dot to see its name and values', centerX, drawHeight + 30);
    }
}

function windowResized() {
    updateCanvasSize();
    resizeCanvas(canvasWidth, canvasHeight);
    updateWheelParameters();
    redraw();
}

function updateCanvasSize() {
    const container = document.querySelector('main').getBoundingClientRect();
    canvasWidth = Math.floor(container.width);
}
