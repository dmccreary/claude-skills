---
name: chapter-image-enhancer
description: >
  Add freely-licensed maps, photos, and diagrams to textbook chapters by finding images
  from Wikimedia Commons and US government sources, downloading and optimizing them, and
  inserting them with proper captions and attribution. Use this skill whenever a user wants
  to add visuals, images, photos, or maps to a chapter, make a chapter more visual, or says
  a chapter needs pictures. Also trigger when the user mentions "chapter images", "add photos",
  "find images for", "visual enhancement", or "image credits".
---

# Chapter Image Enhancer

Add high-quality, freely-licensed images to intelligent textbook chapters. This skill finds relevant maps and photos from public domain and Creative Commons sources, downloads and optimizes them for web, inserts them at appropriate locations with captions, and adds proper attribution.

## When to Use

- A chapter is text-heavy and would benefit from maps, photos, or diagrams
- The user asks to "add images", "make it more visual", or "find photos for" a chapter
- A chapter covers geographic, scientific, or visual topics where images are essential
- After chapter content is generated but before final publication

## Image Source Priority

The skill uses only images compatible with CC BY-NC-SA 4.0 textbooks. Search in this order:

### Tier 1: US Government (Public Domain — No Restrictions)

US federal government works are public domain and the safest to use:

- **USDA** — hardiness zone maps, soil maps, agricultural photos
- **EPA** — ecoregion maps, environmental data visualizations
- **USGS** — topographic maps, geological surveys, satellite imagery
- **USFWS** — wildlife and habitat photos (Fish & Wildlife Service)
- **US Forest Service** — forest and wilderness photos
- **NOAA** — weather, climate, and ocean imagery
- **NASA** — Earth observation and satellite photos
- **NPS** — National Park Service landscape photos
- **Library of Congress** — historical photos and maps

### Tier 2: Wikimedia Commons (CC BY or CC BY-SA)

Wikimedia Commons hosts millions of freely-licensed educational images:

- **CC BY 2.0/3.0/4.0** — attribution required, fully compatible
- **CC BY-SA 2.0/3.0/4.0** — attribution + share-alike, compatible with CC BY-NC-SA
- **CC0 / Public Domain** — no restrictions

Avoid these licenses (incompatible with CC BY-NC-SA 4.0):

- **CC BY-ND** — No Derivatives conflicts with SA
- **All Rights Reserved** — cannot use without explicit permission
- **CC BY-NC-ND** — No Derivatives is incompatible

### Tier 3: State Government and University Sources

State works are NOT automatically public domain (unlike federal). Check terms of use individually. Many state agencies and universities grant educational use.

## Workflow

### Step 1: Analyze the Chapter

Read the chapter's `index.md` to understand:

- The chapter title and main topic
- Major H2 sections — each is a candidate for an image
- What types of images would be most helpful (maps, photos, diagrams, charts)
- The subject domain (geography, biology, history, etc.) to guide image search

Identify 3-6 insertion points where an image would add the most value. Prioritize:

1. Geographic topics → maps
2. Species or organisms → photos
3. Processes or systems → diagrams
4. Historical topics → archival photos
5. Locations or landmarks → landscape photos

### Step 2: Find Images

For each insertion point, find a suitable image.

**Using the Wikimedia API to get correct download URLs:**

The Wikimedia API reliably returns actual image URLs (direct curl/wget often fails due to hash-path issues):

```python
import urllib.request, json

title = "File:Example_Image.jpg"
api_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.request.quote(title)}&prop=imageinfo&iiprop=url&iiurlwidth=1280&format=json"
req = urllib.request.Request(api_url, headers={"User-Agent": "TextbookProject/1.0 (Educational; CC-BY-NC-SA)"})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read())
    pages = data["query"]["pages"]
    for pid, page in pages.items():
        if "imageinfo" in page:
            url = page["imageinfo"][0].get("thumburl", page["imageinfo"][0]["url"])
```

The `iiurlwidth=1280` parameter requests a pre-scaled thumbnail — this is faster than downloading the full-resolution original and resizing locally.

**For US Government sources**, direct URLs typically work fine with curl.

**Important**: Always verify the license before downloading. On Wikimedia Commons, check the file page for the license template. For US government images, confirm they come from a federal (not state or contractor) source.

### Step 3: Download Images

Create a directory for the chapter's images:

```
docs/img/chapters/XX-chapter-name/
```

Download with Python's `urllib` (more reliable than curl for Wikimedia):

```python
import urllib.request

headers = {"User-Agent": "TextbookProject/1.0 (Educational)"}
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = resp.read()
    with open(filepath, "wb") as f:
        f.write(data)
```

Note: Wikimedia rate-limits aggressively. If you get HTTP 429, wait 5 seconds and retry. Download images sequentially, not in parallel.

### Step 4: Optimize for Web

Resize and compress images using Pillow:

```python
from PIL import Image

img = Image.open(path)
max_width = 1200

if img.width > max_width:
    ratio = max_width / img.width
    img = img.resize((max_width, int(img.height * ratio)), Image.LANCZOS)

if path.endswith('.png') and img.mode != 'RGBA':
    # Convert to JPEG for smaller file size (unless transparency needed)
    img.convert('RGB').save(path.replace('.png', '.jpg'), 'JPEG', quality=82, optimize=True)
else:
    img.save(path, optimize=True)
```

Target file sizes:

- Photos: under 500KB (JPEG quality 80-85)
- Maps: under 600KB (JPEG if no transparency, PNG if needed)
- Diagrams: under 300KB (PNG for sharp lines)

### Step 5: Insert Images into the Chapter

Place each image at the identified insertion point using standard Markdown image syntax. Include a caption in italics below the image:

```markdown
![Descriptive alt text for accessibility](../../img/chapters/XX-name/filename.jpg)
*Caption describing the image content and context. Source: Creator Name (License).*
```

**Placement rules:**

- Insert images immediately after the section heading (H2) they relate to, before the first paragraph of text
- One blank line before the image, one blank line after the caption
- The alt text should describe the image content for screen readers
- The caption should explain what the reader is looking at and credit the source

**Caption format:**

```
*[Description of what the image shows]. [Source attribution] ([License]).*
```

Examples:

```markdown
*Big Bluestem grass towering in a tallgrass prairie. Photo: Jennifer Briggs / USFWS (CC BY 2.0).*
*EPA Level III Ecoregions of Minnesota. Source: U.S. Environmental Protection Agency (public domain).*
```

### Step 6: Add Image Credits Section

Add an "Image Credits" section at the bottom of the chapter, before the "See Annotated References" link (or before "## Concepts Covered" if no references link exists):

```markdown
## Image Credits

- [Brief description]: [Creator/Organization] ([License])
- [Brief description]: [Creator/Organization] ([License])
```

This serves as a consolidated attribution block for all images in the chapter, making license compliance easy to verify.

### Step 7: Build and Verify

Run `mkdocs build` (or the project's build command) to verify:

- No broken image paths
- Images render at correct locations
- GLightbox (if installed) enables click-to-zoom
- Page load time is reasonable

## License Compatibility Quick Reference

| Source License | Compatible with CC BY-NC-SA 4.0? | Attribution Required? |
|----------------|----------------------------------|----------------------|
| Public Domain (US Gov) | Yes | No (but good practice) |
| CC0 | Yes | No |
| CC BY 2.0/3.0/4.0 | Yes | Yes |
| CC BY-SA 2.0/3.0/4.0 | Yes | Yes (SA carries through) |
| CC BY-NC 2.0/3.0/4.0 | Yes | Yes |
| CC BY-NC-SA | Yes (same license) | Yes |
| CC BY-ND | **No** | N/A |
| CC BY-NC-ND | **No** | N/A |
| All Rights Reserved | **No** | N/A |

## Common Pitfalls

1. **Wikimedia download URLs**: Never guess the hash path. Always use the Wikimedia API to get the actual URL. The hash path (`/a/ab/File.jpg`) is computed from the filename and is easy to get wrong.

2. **State government images**: Unlike federal works, state government images are NOT automatically public domain. Check each state's terms of use.

3. **Flickr uploads on Commons**: Many Wikimedia Commons photos were uploaded from Flickr. The license shown on Commons is what matters (it was verified at upload time), even if the Flickr page has since changed.

4. **Missing alt text**: Every image must have descriptive alt text for accessibility. Describe what the image shows, not just its title.

5. **Oversized images**: Always resize before committing. A 5MB photo will slow page loads significantly. Target 1200px max width and under 500KB.

6. **Portrait-oriented photos**: Very tall images (portrait orientation) can dominate the page. Consider whether a landscape crop would work better, or use CSS to constrain the height.

## Example Output

For a chapter about Minnesota ecoregions, the skill would produce:

**5 images in** `docs/img/chapters/02-ecoregions/`:

| File | Source | Size |
|------|--------|------|
| mn-ecoregion-map.png | EPA (public domain) | 583 KB |
| usda-hardiness-zones-mn.jpg | USDA-ARS (public domain) | 301 KB |
| tallgrass-prairie.jpg | USFWS via Wikimedia (CC BY 2.0) | 383 KB |
| deciduous-forest.jpg | Wikimedia Commons (CC BY-SA 2.0) | 432 KB |
| boreal-forest-bwca.jpg | US Forest Service (public domain) | 113 KB |

**5 insertions** in the chapter markdown, each with alt text, caption, and attribution.

**1 Image Credits section** at the bottom of the chapter consolidating all attributions.
