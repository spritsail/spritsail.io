#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)

AUTHOR = 'Spritsail Team'
SITENAME = 'Spritsail.io'
SITEDESCRIPTION = 'Docker images done tiny'
SITEURL = 'https://spritsail.io'
RELATIVE_URLS = False

# plugins
PLUGIN_PATHS = ['/pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = '/fh5co-marble'
TIMEZONE = 'Europe/London'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# content paths
PATH = 'content'
STATIC_PATHS = ['assets']
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
EXTRA_PATH_METADATA = {'assets/favicon.ico': {'path': 'favicon.ico'}}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'pymdownx.github': {},
    },
    'output_format': 'html5',
}


# logo path, needs to be stored in PATH Setting
LOGO = '/assets/logo.png'

# special content
HERO = [
  {
    'image': '/assets/home/background-1.jpg',
    # for multilanguage support, create a simple dict
    'title': 'Spritsail',
    'text': 'We develop and maintain the smallest Docker images possible',
    'links': [
      {
        'icon': 'icon-github',
        'url': 'https://github.com/spritsail',
        'text': 'Github'
      }
    ]
  }, {
    'image': '/assets/home/background-1.jpg',
    'title': 'Spritsail',
    'text': 'Check us out on Docker Hub',
    'links': [
      {
        'icon': 'icon-stack',
        'url': 'https://hub.docker.com/r/spritsail',
        'text': 'Docker Hub'
      }
    ]
  }
]

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/spritsail'),
)

ABOUT = {
  'image': '/assets/home/email.png',
  'mail': 'hello@spritsail.io',
  # keep it a string if you dont need multiple languages
  'text': 'Something else not covered here, or want to request a new image? Drop us an email.',
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
]

DEFAULT_METADATA = {
  'status': 'draft'
}

DELETE_OUTPUT_DIRECTPRY = True

# setup disqus
DISQUS_SHORTNAME = 'gitcd-dev'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page
