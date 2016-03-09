# coding: utf8
#!/usr/bin/env python
from __future__ import unicode_literals
from datetime import date
import locale
from os import path
from glob import glob

LOCALE = 'en_AU.UTF-8'
AUTHOR = 'Kevin Murray'
SITENAME = '𝜥'
SITEURL = ''
SITE_DOMAIN = 'www.kdmurray.id.au'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en_AU.UTF-8'
THEME = './theme_built-texts/'

COPYRIGHT_FROM = 2013
COPYRIGHT_UNTIL = date.today().year

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
STATIC_PATHS = ['images', 'static']
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
}

# Blogroll
LINKS =  (('Where I Work', 'http://borevitzlab.anu.edu.au/'),
         )

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/kdmurray91'),
    ('GitHub', 'https://github.com/kdmurray91'),
)

DEFAULT_PAGINATION = 10

# Use filsystem folders for categories
INDEX_SAVE_AS = 'blog/index.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

PATH = 'content'
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']
MARKUP = (('rst', 'html'))
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
ARCHIVES_SAVE_AS = 'blog/archives.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
TAGS_SAVE_AS = 'blog/tags.html'
DAY_ARCHIVE_SAVE_AS = False
AUTHORS_SAVE_AS = False

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.+)(\..*)?'

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = [
    'better_figures_and_images',
    'assets',
    'related_posts',
    'extract_toc',
    'post_stats',
    'multi_part'
]

RESPONSIVE_IMAGES = True
RELATED_POSTS_MAX = 4

def suffix(d, wrap=True):
    tmp = 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
    if wrap:
        return '<span class="day_suffix">' + tmp + '</span>'
    else:
        return tmp

def tagsort(tags):
  return sorted(tags,lambda a,b:len(b[1])-len(a[1]))

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def month_name(month_number):
    import calendar
    return calendar.month_name[month_number]

def archive_date_format(date):
    return custom_strftime('{S} %B, %Y', date)

def sidebar_date_format(date):
    return custom_strftime('%a {S} %B, %Y', date)

def dump(thing):
    return vars(thing)

# Which custom Jinja filters to enable
JINJA_FILTERS = {
    "month_name": month_name,
    "archive_date_format": archive_date_format,
    "sidebar_date_format": sidebar_date_format,
    "tagsort": tagsort,
    "dump": dump,
}
