#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Antoine Charlet'
SITENAME = 'Deep Disgression'
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/in/antoinecharlet'),)

DEFAULT_PAGINATION = 3
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

STATIC_PATHS = ['images', 'pdfs']

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# THEME SETTINGS
THEME = './themes/attila'

ABOUT_PAGE = '/pages/about.html'
GITHUB_USERNAME = 'charlet-antoine'
STACKOVERFLOW_ADDRESS = 'https://stackoverflow.com/users/4616183/antoine-charlet'
AUTHOR_BLOG = 'http://charlet-antoine.github.io'
AUTHOR_CV = 'https://www.linkedin.com/in/antoinecharlet'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ENABLE_MATHJAX = True

# Path to the folder containing the plugins
PLUGIN_PATHS = ['pelican-plugins']
# Enabled plugins
PLUGINS = ['pelican-ipynb.markup', 'sitemap',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook']

MARKUP = ('md', 'ipynb')

IGNORE_FILES = [".ipynb_checkpoints"]  
IPYNB_USE_METACELL = True

DELETE_OUTPUT_DIRECTORY = False



HOME_COVER = 'https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/8/b/3/8b30e81545_85864_645-fractal-canonique.jpg'
COLOR_SCHEME_CSS = 'github.css'

DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']
