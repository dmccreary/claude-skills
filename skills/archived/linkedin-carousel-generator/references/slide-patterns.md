# Slide Patterns (pptxgenjs)

Reusable pptxgenjs code patterns for the LinkedIn carousel. Every slide in the 13-slide deck
is a variant of one of these nine patterns. Colors (`C.primary`, `C.accent`) come from the
project's `mkdocs.yml` theme palette — never hardcode generic blues.

## Setup

```javascript
const pptxgen = require("pptxgenjs");
const pptx = new pptxgen();

pptx.defineLayout({ name: "SQUARE", width: 10, height: 10 });
pptx.layout = "SQUARE";

// Pull these from mkdocs.yml theme.palette
const C = {
  primary: "642580",     // theme.palette.primary, no leading #
  accent: "41BAC1",      // theme.palette.accent
  white: "FFFFFF",
  offWhite: "F7F5FA",
  ink: "212121",
  gray: "6B6B6B",
};

const FONT_TITLE = "Georgia";
const FONT_BODY = "Calibri";
```

## 1. Title / Cover Slide (slide 1)

Dark background, large title, mascot welcome pose bottom-corner or centered.

```javascript
function coverSlide(pptx, { title, subtitle, mascotPath }) {
  const s = pptx.addSlide();
  s.background = { color: C.primary };
  s.addText(title, {
    x: 0.6, y: 3.0, w: 8.8, h: 2.2,
    fontFace: FONT_TITLE, fontSize: 40, bold: true, color: C.white, align: "center",
  });
  s.addText(subtitle, {
    x: 0.6, y: 5.2, w: 8.8, h: 1.0,
    fontFace: FONT_BODY, fontSize: 18, color: C.white, align: "center",
  });
  if (mascotPath) {
    s.addImage({ path: mascotPath, x: 4.0, y: 6.4, w: 2.0, h: 2.0 });
  }
  s.addText("An Intelligent Textbook", {
    x: 0.6, y: 8.8, w: 8.8, h: 0.5,
    fontFace: FONT_BODY, fontSize: 14, color: C.accent, align: "center", italic: true,
  });
  return s;
}
```

## 2. Mascot-Aside Slide (slide 2)

Mascot image floated left/bottom, short narrative text to the right. Used for "Why This Book."

```javascript
function mascotAsideSlide(pptx, { heading, body, mascotPath }) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addImage({ path: mascotPath, x: 0.5, y: 3.8, w: 2.4, h: 2.4 });
  s.addText(heading, {
    x: 3.2, y: 0.8, w: 6.3, h: 1.2,
    fontFace: FONT_TITLE, fontSize: 30, bold: true, color: C.primary,
  });
  s.addText(body, {
    x: 3.2, y: 2.2, w: 6.3, h: 6.0,
    fontFace: FONT_BODY, fontSize: 18, color: C.ink, valign: "top", lineSpacing: 26,
  });
  return s;
}
```

## 3. Image-Aside Slide (slides 3, 9)

Text on one side, a screenshot/photo on the other. Set `imageSide: "right"` or `"left"`.

```javascript
function imageAsideSlide(pptx, { heading, body, imagePath, imageSide = "right" }) {
  const s = pptx.addSlide();
  s.background = { color: C.offWhite };
  const textX = imageSide === "right" ? 0.6 : 4.4;
  const imgX = imageSide === "right" ? 5.0 : 0.6;
  s.addText(heading, {
    x: textX, y: 0.7, w: 3.8, h: 1.0,
    fontFace: FONT_TITLE, fontSize: 26, bold: true, color: C.primary,
  });
  s.addText(body, {
    x: textX, y: 1.8, w: 3.8, h: 6.5,
    fontFace: FONT_BODY, fontSize: 16, color: C.ink, valign: "top", lineSpacing: 22,
  });
  s.addImage({ path: imagePath, x: imgX, y: 1.5, w: 4.4, h: 4.4, sizing: { type: "contain", w: 4.4, h: 4.4 } });
  return s;
}
```

## 4. Big-Numbers Slide (slide 4)

A row of 2-3 large stats with labels underneath. Used for coverage summary.

```javascript
function bigNumbersSlide(pptx, { heading, stats, footer }) {
  // stats: [{ number: "38", label: "Chapters" }, ...]
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.6, w: 8.8, h: 1.0,
    fontFace: FONT_TITLE, fontSize: 28, bold: true, color: C.primary, align: "center",
  });
  const colW = 8.8 / stats.length;
  stats.forEach((stat, i) => {
    s.addText(stat.number, {
      x: 0.6 + i * colW, y: 2.5, w: colW, h: 1.6,
      fontFace: FONT_TITLE, fontSize: 54, bold: true, color: C.accent, align: "center",
    });
    s.addText(stat.label, {
      x: 0.6 + i * colW, y: 4.1, w: colW, h: 0.8,
      fontFace: FONT_BODY, fontSize: 16, color: C.ink, align: "center",
    });
  });
  if (footer) {
    s.addText(footer, {
      x: 0.6, y: 8.4, w: 8.8, h: 1.2,
      fontFace: FONT_BODY, fontSize: 15, color: C.gray, align: "center", valign: "top",
    });
  }
  return s;
}
```

## 5. Icon-Row Slide (slides 5, 8)

A horizontal row of 3-4 short icon+label+caption blocks. No paragraphs — this pattern exists
specifically to enforce "no walls of text."

```javascript
function iconRowSlide(pptx, { heading, items }) {
  // items: [{ emoji: "▶️", label: "Run", caption: "Instantly, in the browser" }, ...]
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.6, w: 8.8, h: 1.0,
    fontFace: FONT_TITLE, fontSize: 28, bold: true, color: C.primary, align: "center",
  });
  const colW = 8.8 / items.length;
  items.forEach((item, i) => {
    s.addText(item.emoji, {
      x: 0.6 + i * colW, y: 2.6, w: colW, h: 1.2, fontSize: 44, align: "center",
    });
    s.addText(item.label, {
      x: 0.6 + i * colW, y: 4.0, w: colW, h: 0.6,
      fontFace: FONT_BODY, fontSize: 18, bold: true, color: C.primary, align: "center",
    });
    s.addText(item.caption, {
      x: 0.6 + i * colW, y: 4.6, w: colW, h: 1.4,
      fontFace: FONT_BODY, fontSize: 13, color: C.gray, align: "center", valign: "top",
    });
  });
  return s;
}
```

## 6. Pose-Grid Slide (slide 6)

Mascot pose thumbnails in a row/grid, each labeled with its role. Use the poses that actually
exist in `docs/img/mascot/` and their roles from the character sheet — do not invent poses.

```javascript
function poseGridSlide(pptx, { heading, mascotName, poses }) {
  // poses: [{ path: "docs/img/mascot/welcome.png", role: "Chapter openings" }, ...]
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.5, w: 8.8, h: 0.9,
    fontFace: FONT_TITLE, fontSize: 26, bold: true, color: C.primary, align: "center",
  });
  const perRow = 3;
  const cellW = 8.8 / perRow;
  poses.forEach((pose, i) => {
    const col = i % perRow, row = Math.floor(i / perRow);
    const x = 0.6 + col * cellW, y = 1.8 + row * 3.0;
    s.addImage({ path: pose.path, x: x + cellW / 2 - 0.75, y, w: 1.5, h: 1.5 });
    s.addText(pose.role, {
      x, y: y + 1.6, w: cellW, h: 0.7,
      fontFace: FONT_BODY, fontSize: 13, color: C.ink, align: "center",
    });
  });
  return s;
}
```

## 7. Badge-Callout Slide (slide 9, license)

A centered icon/badge with a short headline and one supporting sentence. Low text density.

```javascript
function badgeCalloutSlide(pptx, { heading, body, badgePath }) {
  const s = pptx.addSlide();
  s.background = { color: C.offWhite };
  s.addImage({ path: badgePath, x: 3.5, y: 1.2, w: 3.0, h: 3.0 });
  s.addText(heading, {
    x: 0.6, y: 4.6, w: 8.8, h: 0.9,
    fontFace: FONT_TITLE, fontSize: 26, bold: true, color: C.primary, align: "center",
  });
  s.addText(body, {
    x: 1.2, y: 5.6, w: 7.6, h: 3.0,
    fontFace: FONT_BODY, fontSize: 17, color: C.ink, align: "center", valign: "top", lineSpacing: 24,
  });
  return s;
}
```

## 8. Checklist Recap Slide (slide 12)

A vertical list of 5-6 short checkmarked phrases — the single strongest fact pulled from each
of slides 2-11, condensed to a few words each. This slide exists to close the loop before the
CTA; it fails if any line runs longer than roughly seven words.

```javascript
function checklistRecapSlide(pptx, { heading, items }) {
  // items: ["450 concepts, 0 dependency violations", "31 interactive MicroSims", ...]
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.6, w: 8.8, h: 1.0,
    fontFace: FONT_TITLE, fontSize: 28, bold: true, color: C.primary, align: "center",
  });
  const rowH = 6.8 / items.length;
  items.forEach((item, i) => {
    const y = 1.9 + i * rowH;
    s.addText("✅", {
      x: 0.9, y, w: 0.6, h: rowH, fontSize: 22, valign: "middle",
    });
    s.addText(item, {
      x: 1.6, y, w: 7.2, h: rowH,
      fontFace: FONT_BODY, fontSize: 18, bold: true, color: C.ink, valign: "middle",
    });
  });
  return s;
}
```

## 9. Closing CTA Slide (slide 13)

Dark background matching slide 1 — bookends the deck.

```javascript
function closingCtaSlide(pptx, { headline, siteUrl, repoUrl, mascotPath }) {
  const s = pptx.addSlide();
  s.background = { color: C.primary };
  if (mascotPath) {
    s.addImage({ path: mascotPath, x: 4.0, y: 1.0, w: 2.0, h: 2.0 });
  }
  s.addText(headline, {
    x: 0.6, y: 3.4, w: 8.8, h: 1.2,
    fontFace: FONT_TITLE, fontSize: 30, bold: true, color: C.white, align: "center",
  });
  s.addText(siteUrl, {
    x: 0.6, y: 5.0, w: 8.8, h: 0.6,
    fontFace: FONT_BODY, fontSize: 20, bold: true, color: C.accent, align: "center",
  });
  if (repoUrl) {
    s.addText(repoUrl, {
      x: 0.6, y: 5.7, w: 8.8, h: 0.5,
      fontFace: FONT_BODY, fontSize: 15, color: C.white, align: "center",
    });
  }
  s.addText("Free & open source — built with Claude AI skills", {
    x: 0.6, y: 8.6, w: 8.8, h: 0.6,
    fontFace: FONT_BODY, fontSize: 13, italic: true, color: C.white, align: "center",
  });
  return s;
}
```

## Assembling the 13 Slides

```javascript
coverSlide(pptx, { title: "...", subtitle: "...", mascotPath: "docs/img/mascot/welcome.png" });
mascotAsideSlide(pptx, { heading: "Why This Book", body: "...", mascotPath: "docs/img/mascot/thinking.png" });
imageAsideSlide(pptx, { heading: "Learning Graph", body: "...", imagePath: "linkedin/slides/learning-graph-zoom.png", imageSide: "right" });
bigNumbersSlide(pptx, { heading: "Coverage", stats: [...], footer: "..." });
iconRowSlide(pptx, { heading: "See It. Run It. Modify It.", items: [...] });
poseGridSlide(pptx, { heading: "Meet the Mascot", mascotName: "...", poses: [...] });
imageAsideSlide(pptx, { heading: "31 MicroSims", body: "...", imagePath: "linkedin/slides/microsim-preview.png", imageSide: "left" });
iconRowSlide(pptx, { heading: "Beyond the Chapters", items: [...] }); // glossary/FAQ/quiz/references
badgeCalloutSlide(pptx, { heading: "Open License", body: "...", badgePath: "docs/img/license.png" });
// slide 10 (adaptivity) and 11 (continuous enrichment): reuse iconRowSlide or imageAsideSlide,
// whichever fits the specific content better
checklistRecapSlide(pptx, { heading: "Why Students & Teachers Love It", items: [
  "450 concepts, 0 dependency violations",
  "31 interactive MicroSims",
  "338 glossary terms, 380 quiz questions",
  "Free & open source, no accounts required",
  "Skills-based framework — easy to adapt for your class",
] });
closingCtaSlide(pptx, { headline: "...", siteUrl: "...", repoUrl: "...", mascotPath: "docs/img/mascot/celebration.png" });

await pptx.writeFile({ fileName: "linkedin/<kebab-title>-carousel.pptx" });
```
