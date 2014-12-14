#!/usr/bin/env python
from __future__ import unicode_literals
from datetime import date
import locale

LOCALE = 'en_AU.UTF-8'
AUTHOR = 'Kevin Murray'
SITENAME = 'kdm'
SITEURL = '/'#http://www.kdmurray.id.au'
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

# Blogroll
LINKS =  (('Where I Work', 'http://borevitzlab.anu.edu.au/'),
         )

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/kdmurray91'),
    ('GitHub', 'http://github.com/kdmurray91'),
)

DEFAULT_PAGINATION = 10

# Use filsystem folders for categories
INDEX_SAVE_AS = 'blog/index.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

PATH = 'content'
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']
#MARKUP = (('rst', 'html'))
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/index.html'
ARCHIVES_SAVE_AS = 'blog/archive.html'
AUTHOR_SAVE_AS = False

PLUGIN_PATH = './pelican-plugins'
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

RELATIVE_URLS = False

#################################
#
# Custom Jinja Filters
#   see: http://jinja.pocoo.org/docs/templates/#filters
#
#################################

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
