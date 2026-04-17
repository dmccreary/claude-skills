# Slide Patterns Library

Reusable pptxgenjs code patterns for common slide types. Each pattern includes the JavaScript code and design rationale.

## Setup Boilerplate

```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "Author Name";
pres.title = "Presentation Title";

// Color system — derive from textbook's CLAUDE.md
const C = {
  primary: "283593",
  primaryDark: "1A237E",
  primaryLight: "5C6BC0",
  primaryBg: "E8EAF6",
  accent: "FF8F00",
  accentLight: "FFE082",
  white: "FFFFFF",
  offWhite: "F5F5F5",
  black: "212121",
  gray: "757575",
  lightGray: "E0E0E0",
  red: "C62828",
  green: "2E7D32",
  teal: "00897B",
};

const TITLE_FONT = "Georgia";
const BODY_FONT = "Calibri";
```

## Pattern 1: Title Slide (Dark)

```javascript
const s = pres.addSlide();
s.background = { color: C.primaryDark };
s.addText("SUBTITLE LABEL", {
  x: 0.8, y: 1.0, w: 8.4, h: 0.6,
  fontSize: 18, fontFace: BODY_FONT, color: C.accent, charSpacing: 6,
});
s.addText("Main Title\nLine Two", {
  x: 0.8, y: 1.6, w: 8.4, h: 2.0,
  fontSize: 48, fontFace: TITLE_FONT, color: C.white, bold: true,
});
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 3.8, w: 2.5, h: 0.06, fill: { color: C.accent },
});
s.addText("Subtitle or tagline", {
  x: 0.8, y: 4.1, w: 8.4, h: 0.5,
  fontSize: 20, fontFace: BODY_FONT, color: C.primaryLight, italic: true,
});
s.addText("Author Name  |  organization.com", {
  x: 0.8, y: 4.8, w: 8.4, h: 0.4,
  fontSize: 14, fontFace: BODY_FONT, color: C.gray,
});
```

## Pattern 2: Section Divider (Dark)

```javascript
const s = pres.addSlide();
s.background = { color: C.primaryDark };
s.addText("Section Title", {
  x: 0.8, y: 1.5, w: 8.4, h: 1.5,
  fontSize: 44, fontFace: TITLE_FONT, color: C.white, bold: true,
});
s.addText("Subtitle or key quote", {
  x: 0.8, y: 3.0, w: 8.4, h: 0.8,
  fontSize: 20, fontFace: BODY_FONT, color: C.accentLight,
});
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 3.9, w: 2, h: 0.06, fill: { color: C.accent },
});
```

## Pattern 3: Big Number (Dark, Full-Screen Stat)

```javascript
const s = pres.addSlide();
s.background = { color: C.primaryDark };
s.addText("85%", {
  x: 0, y: 0.5, w: 10, h: 3,
  fontSize: 120, fontFace: TITLE_FONT, color: C.accent, bold: true,
  align: "center", valign: "middle",
});
s.addText("of career success comes from\ncommunication skills", {
  x: 0, y: 3.2, w: 10, h: 1.2,
  fontSize: 24, fontFace: BODY_FONT, color: C.white, align: "center",
});
s.addText("Source attribution", {
  x: 0, y: 4.7, w: 10, h: 0.4,
  fontSize: 12, fontFace: BODY_FONT, color: C.primaryLight, align: "center",
});
```

## Pattern 4: Before/After Comparison

```javascript
const s = pres.addSlide();
s.background = { color: C.white };
s.addText("Before vs. After Title", {
  x: 0.8, y: 0.3, w: 8.4, h: 0.7,
  fontSize: 32, fontFace: TITLE_FONT, color: C.primary, bold: true, margin: 0,
});

// Before column
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.3, w: 4.3, h: 3.0, fill: { color: "FFF3E0" }, // warm orange bg
});
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.5, y: 1.3, w: 4.3, h: 0.06, fill: { color: C.red }, // red accent bar
});
s.addText("Before", {
  x: 0.7, y: 1.5, w: 3.9, h: 0.4,
  fontSize: 14, fontFace: BODY_FONT, color: C.red, bold: true,
});
s.addText("Content here...", {
  x: 0.7, y: 2.0, w: 3.9, h: 2.0,
  fontSize: 14, fontFace: BODY_FONT, color: C.black,
});

// After column
s.addShape(pres.shapes.RECTANGLE, {
  x: 5.2, y: 1.3, w: 4.3, h: 3.0, fill: { color: "E8F5E9" }, // light green bg
});
s.addShape(pres.shapes.RECTANGLE, {
  x: 5.2, y: 1.3, w: 4.3, h: 0.06, fill: { color: C.green }, // green accent bar
});
s.addText("After", {
  x: 5.4, y: 1.5, w: 3.9, h: 0.4,
  fontSize: 14, fontFace: BODY_FONT, color: C.green, bold: true,
});
s.addText("Content here...", {
  x: 5.4, y: 2.0, w: 3.9, h: 2.0,
  fontSize: 14, fontFace: BODY_FONT, color: C.black,
});
```

## Pattern 5: Evidence Stack (3 Cards)

```javascript
const s = pres.addSlide();
s.background = { color: C.white };
s.addText("Title", {
  x: 0.8, y: 0.3, w: 8.4, h: 0.7,
  fontSize: 32, fontFace: TITLE_FONT, color: C.primary, bold: true, margin: 0,
});

const items = [
  { title: "Source 1", finding: "Key finding text", y: 1.4 },
  { title: "Source 2", finding: "Key finding text", y: 2.5 },
  { title: "Source 3", finding: "Key finding text", y: 3.6 },
];
items.forEach((e) => {
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: e.y, w: 8.4, h: 0.9, fill: { color: C.primaryBg },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.8, y: e.y, w: 0.08, h: 0.9, fill: { color: C.primary },
  });
  s.addText(e.title, {
    x: 1.1, y: e.y + 0.05, w: 7.9, h: 0.4,
    fontSize: 14, fontFace: BODY_FONT, color: C.primary, bold: true,
  });
  s.addText(e.finding, {
    x: 1.1, y: e.y + 0.45, w: 7.9, h: 0.35,
    fontSize: 16, fontFace: BODY_FONT, color: C.black,
  });
});
```

## Pattern 6: Three Pillars/Columns

```javascript
const pillars = [
  { title: "Pillar 1", desc: "Description", color: C.primary },
  { title: "Pillar 2", desc: "Description", color: C.teal },
  { title: "Pillar 3", desc: "Description", color: C.accent },
];
pillars.forEach((p, i) => {
  const x = 0.5 + i * 3.2;
  s.addShape(pres.shapes.RECTANGLE, {
    x: x, y: 1.5, w: 2.9, h: 3, fill: { color: C.offWhite },
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: x, y: 1.5, w: 2.9, h: 0.08, fill: { color: p.color },
  });
  s.addText(p.title, {
    x: x, y: 2.0, w: 2.9, h: 0.8,
    fontSize: 24, fontFace: TITLE_FONT, color: p.color, bold: true, align: "center",
  });
  s.addText(p.desc, {
    x: x, y: 3.0, w: 2.9, h: 0.5,
    fontSize: 16, fontFace: BODY_FONT, color: C.gray, align: "center",
  });
});
```

## Pattern 7: Interactive Beat / Challenge

```javascript
const s = pres.addSlide();
s.background = { color: C.white };
s.addText("Challenge Title", {
  x: 0.8, y: 0.3, w: 8.4, h: 0.7,
  fontSize: 32, fontFace: TITLE_FONT, color: C.primary, bold: true, margin: 0,
});
s.addShape(pres.shapes.RECTANGLE, {
  x: 1.5, y: 1.5, w: 7, h: 2.5, fill: { color: C.primaryBg },
});
s.addText("The challenge prompt\ngoes here.", {
  x: 1.5, y: 1.7, w: 7, h: 1.5,
  fontSize: 36, fontFace: TITLE_FONT, color: C.primary, align: "center", bold: true,
});
s.addText("Instructions. Time limit. Go.", {
  x: 1.5, y: 3.2, w: 7, h: 0.6,
  fontSize: 20, fontFace: BODY_FONT, color: C.accent, align: "center", bold: true,
});
```

## Pattern 8: Numbered Action Items

```javascript
const actions = [
  { num: "1", title: "First action", desc: "Details here" },
  { num: "2", title: "Second action", desc: "Details here" },
  { num: "3", title: "Third action", desc: "Details here" },
];
actions.forEach((a, i) => {
  const y = 1.2 + i * 1.4;
  s.addShape(pres.shapes.OVAL, {
    x: 0.8, y: y + 0.1, w: 0.7, h: 0.7, fill: { color: C.primary },
  });
  s.addText(a.num, {
    x: 0.8, y: y + 0.1, w: 0.7, h: 0.7,
    fontSize: 24, fontFace: TITLE_FONT, color: C.white,
    align: "center", valign: "middle", bold: true,
  });
  s.addText(a.title, {
    x: 1.8, y: y, w: 7.4, h: 0.45,
    fontSize: 20, fontFace: BODY_FONT, color: C.black, bold: true,
  });
  s.addText(a.desc, {
    x: 1.8, y: y + 0.5, w: 7.4, h: 0.7,
    fontSize: 14, fontFace: BODY_FONT, color: C.gray,
  });
});
```

## Pattern 9: Final Quote (Dark)

```javascript
const s = pres.addSlide();
s.background = { color: C.primaryDark };
s.addText("The quote text\ngoes here.", {
  x: 0.8, y: 1.0, w: 8.4, h: 1.8,
  fontSize: 40, fontFace: TITLE_FONT, color: C.white, bold: true,
});
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 2.9, w: 2, h: 0.06, fill: { color: C.accent },
});
s.addText("The punchline.", {
  x: 0.8, y: 3.2, w: 8.4, h: 1.0,
  fontSize: 40, fontFace: TITLE_FONT, color: C.accent, bold: true,
});
```

## Pattern 10: Thank You / Close (Dark)

```javascript
const s = pres.addSlide();
s.background = { color: C.primaryDark };
s.addText("Thank You", {
  x: 0.8, y: 1.2, w: 8.4, h: 1.2,
  fontSize: 48, fontFace: TITLE_FONT, color: C.white, bold: true,
});
s.addShape(pres.shapes.RECTANGLE, {
  x: 0.8, y: 2.5, w: 2, h: 0.06, fill: { color: C.accent },
});
s.addText("Speaker Name", {
  x: 0.8, y: 2.9, w: 8.4, h: 0.5,
  fontSize: 22, fontFace: BODY_FONT, color: C.white,
});
s.addText("organization.com", {
  x: 0.8, y: 3.4, w: 8.4, h: 0.4,
  fontSize: 16, fontFace: BODY_FONT, color: C.primaryLight,
});
s.addText("email@example.com", {
  x: 0.8, y: 3.8, w: 8.4, h: 0.4,
  fontSize: 14, fontFace: BODY_FONT, color: C.gray,
});
```

## Speaker Notes Pattern

```javascript
s.addNotes(
  "TIMING: XX:XX\n\n" +
  "SAY: 'The narrative the speaker delivers...'\n\n" +
  "META-MOMENT: 'Notice what I just did? That was [framework name].'\n\n" +
  "TRANSITION: 'Bridge sentence to next slide.'\n\n" +
  "AUDIENCE PULSE: Pause 3 seconds after this point."
);
```
