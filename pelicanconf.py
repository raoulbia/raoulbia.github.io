##!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#AUTHOR = 'raoulbia'
SITENAME = 'code snippets etc.'
SITEURL = 'http://raoulbia.github.io/'

PATH = 'content'

TIMEZONE = 'Europe/Dublin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
#TAGS_URL           = 'tags'
#TAGS_SAVE_AS       = 'tags/index.html'
#AUTHORS_URL        = 'authors'
#AUTHORS_SAVE_AS    = 'authors/index.html'
#CATEGORIES_URL     = 'categories'
#CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_URL       = 'archives'
ARCHIVES_SAVE_AS   = 'archives/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    #('Tags', TAGS_URL, TAGS_SAVE_AS),
    # ('Authors', AUTHORS_URL, AUTHORS_SAVE_AS),
    #('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
# additional menu items
MENUITEMS = (
    ('GitHub', 'https://github.com/raoulbia'),
    # ('StackOverflow', 'https://stackoverflow.com/users/425727/raoulbia')
)


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 2

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# THEME = "./themes/pelican-svbtle"
#THEME = "./pelican-themes/" # if only blue penguin was installed then it will be in the root (no need to specify)
THEME = "pelican-themes/theme/blue-penguin"
STATIC_PATHS = ['img', 'static']
MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup'] #, 'render_math']
IGNORE_FILES = ['.ipynb_checkpoints']
