#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jeff Langemeier'
SITENAME = 'Imitation Code'
SITESUBTITLE = 'Personal Blog of Jeff Langemeier'
SITEURL = ''

PATH = 'content'
THEME = 'themes/main-style'

TIMEZONE = 'America/Denver'
DEFAULT_DATE_FORMAT = '%d.%b.%Y'

DEFAULT_LANG = 'en'

# Development environment setup
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Plugins
PLUGIN_PATHS = ['../pelican-plugins', ]
PLUGINS = ['render_math', ]

# Blogroll
# LINKS = (('Pelican', '#'),
#          ('Python.org', '#'),
#          ('Jinja2', '#'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('Twitter', '#'),
#           ('LinkedIn', '#'),)

# Menu Items
MENUITEMS = (('Home', ''),
             ('Words', 'archives.html'),
             ('Code', ''),
             ('About', 'pages/about.html'))

# Pagination
DEFAULT_PAGINATION = 5
DEFAULT_ORPHANS = 3
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
}
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Save Locations
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
DRAFT_URL = 'drafts/posts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/posts/{slug}.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
DRAFT_PAGE_URL = 'drafts/pages/{slug}.html'
DRAFT_PAGE_SAVE_AS = 'drafts/pages/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
AUTHORS_SAVE_AS = ''

# Period Archives
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
