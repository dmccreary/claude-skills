#!/bin/bash

# Script to install social_override plugin for mkdocs-material
# Run this from the root directory of your project

# Create directories
echo "Creating plugin directories..."
mkdir -p plugins

# Create __init__.py
echo "Creating plugins/__init__.py..."
cat > plugins/__init__.py << 'EOL'
from .social_override import SocialOverridePlugin
EOL

# Create social_override.py
echo "Creating plugins/social_override.py..."
cat > plugins/social_override.py << 'EOL'
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
EOL

# Create setup.py
echo "Creating setup.py..."
cat > setup.py << 'EOL'
from setuptools import setup, find_packages

setup(
    name='social_override',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'social_override = plugins.social_override:SocialOverridePlugin',
        ]
    }
)
EOL

# Install the plugin
echo "Installing the social_override plugin..."
pip install -e .

# Update mkdocs.yml
echo "Please add 'social_override' to your plugins section in mkdocs.yml:"
echo ""
echo "plugins:"
echo "  - search"
echo "  - social"
echo "  - social_override"
echo ""
echo "Installation complete!"
