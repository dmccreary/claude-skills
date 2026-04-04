# Trim excess padding from around images
# Use when generated mascot images contain too much padding
# This can also be used for non-mascot images
from pathlib import Path
from PIL import Image

root = Path('docs/img/mascot')
THRESH = 10   # alpha ≤ 10 treated as padding
PADDING = 4   # px buffer preserved after crop

for path in sorted(root.glob('*.png')):
    img = Image.open(path).convert('RGBA')
    alpha = img.getchannel('A')
    px = alpha.load()
    w, h = img.size
    min_x, max_x, min_y, max_y = w, -1, h, -1
    for y in range(h):
        for x in range(w):
            if px[x, y] > THRESH:
                min_x = min(min_x, x); max_x = max(max_x, x)
                min_y = min(min_y, y); max_y = max(max_y, y)
    if max_x == -1:
        print(f'skip {path.name}'); continue
    bbox = (max(min_x-PADDING,0), max(min_y-PADDING,0),
            min(max_x+PADDING,w-1)+1, min(max_y+PADDING,h-1)+1)
    cropped = img.crop(bbox)
    if cropped.size != img.size:
        cropped.save(path)
        print(f'cropped {path.name}: {img.size} -> {cropped.size}')
