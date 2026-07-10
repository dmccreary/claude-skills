"""MkDocs hook that overrides og:image and twitter:image with a page's
`image:` frontmatter value.

Behavior:
    - If the page has `image:` in its frontmatter, og:image and
      twitter:image are set to site_url + image (absolute URL).
    - If the page has no `image:`, the hook is a no-op. All meta tags
      emitted by mkdocs-material (and by the social plugin, if enabled)
      pass through unchanged.

The cover image (img/cover.png) is therefore used ONLY for pages that
declare it explicitly -- typically docs/index.md. There is no site-wide
default. When the mkdocs-material[imaging] social plugin is enabled, its
auto-generated /assets/images/social/<page>.png card is what crawlers see
for every page that does NOT declare `image:`. A page that DOES declare
`image:` always wins over the generated card.

Loaded via the `hooks:` entry in mkdocs.yml, not as a plugin -- this
avoids collisions with other projects that also install a package
called `social_override` or a top-level module called `plugins`.
"""

import re


def on_post_page(html, page, config, **kwargs):
    image = (page.meta or {}).get("image")
    if not image:
        return html

    site_url = config.get("site_url") or ""
    if not site_url:
        return html

    if image.startswith(("http://", "https://")):
        image_url = image
    else:
        image_url = site_url.rstrip("/") + "/" + image.lstrip("/")

    og_tag = f'<meta property="og:image" content="{image_url}">'
    og_pattern = re.compile(
        r'<meta\s+property="og:image"\s+content="[^"]*"[^>]*>'
    )
    if og_pattern.search(html):
        html = og_pattern.sub(og_tag, html, count=1)
    else:
        html = html.replace("</head>", f"  {og_tag}\n</head>", 1)

    tw_tag = f'<meta name="twitter:image" content="{image_url}">'
    tw_pattern = re.compile(
        r'<meta\s+(?:property|name)="twitter:image"\s+content="[^"]*"[^>]*>'
    )
    if tw_pattern.search(html):
        html = tw_pattern.sub(tw_tag, html, count=1)
    else:
        html = html.replace("</head>", f"  {tw_tag}\n</head>", 1)

    return html
