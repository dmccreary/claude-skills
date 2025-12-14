from mkdocs.plugins import BasePlugin
import re

class SocialOverridePlugin(BasePlugin):
    def on_page_context(self, context, page, config, **kwargs):
        """Save custom image path from page metadata if it exists"""
        if page.meta and 'image' in page.meta:
            page.custom_image = page.meta['image']
        return context
    
    def on_post_page(self, html, page, config, **kwargs):
        """Replace social plugin meta tags with our custom image"""
        # Only process pages with custom image
        if not hasattr(page, 'custom_image'):
            return html
        
        # Build the full URL for the custom image
        site_url = config['site_url'].rstrip('/')
        image_path = '/' + page.custom_image.lstrip('/')
        full_image_url = site_url + image_path
        
        # Find and replace OpenGraph image tags
        og_tags = re.findall(r'<meta\s+property="og:image"[^>]*?>', html)
        for tag in og_tags:
            if '/assets/images/social/' in tag:
                new_tag = f'<meta property="og:image" content="{full_image_url}">'
                html = html.replace(tag, new_tag)
        
        # Find and replace Twitter image tags
        twitter_tags = re.findall(r'<meta\s+name="twitter:image"[^>]*?>', html)
        for tag in twitter_tags:
            if '/assets/images/social/' in tag:
                new_tag = f'<meta name="twitter:image" content="{full_image_url}">'
                html = html.replace(tag, new_tag)
        
        return html

# Make the plugin available to MkDocs
def get_plugin():
    return SocialOverridePlugin()
