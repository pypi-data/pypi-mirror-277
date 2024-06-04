try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'The Core Library for the Spirit of Harmony',
    'author': 'Andrew Shatz',
    'url': r'https://github.com/Great-Strength-Studios/aikicore',
    'download_url': r'https://github.com/Great-Strength-Studios/aikicore',
    'author_email': 'andrew@greatstrength.me',
    'version': '0.2.0-alpha.7',
    'license': 'BSD 3',
    'install_requires': [
        'schematics>=2.1.1',
        'pyyaml>=6.0.1'
    ],
    'packages': [
        'aikicore',
        'aikicore.config',
        'aikicore.data',
        'aikicore.handlers',
        'aikicore.handlers.feature',
        'aikicore.objects',
        'aikicore.services',
        'aikicore.repositories',
        'aikicore.repositories.error_cache',
        'aikicore.repositories.feature',
    ],    
    'scripts': [],
    'name': 'aikicore'
}

setup(**config)