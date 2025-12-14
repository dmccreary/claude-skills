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
