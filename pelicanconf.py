#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yinhe Zhang'
SITENAME = u'Galaxy of Yinhe'
SITEURL = ''

SITESUBTITLE = u"Part Of Cosmos" 

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('My Love', 'http://elaine-zhang.cn/'),
    )

#MENUITEMS = (
#    ('My Love', 'http://elaine-zhang.cn/'),
#    )

# Social widget
SOCIAL = (
    ('github', 'https://github.com/crickzhang1'),
    ('google-plus', 'http://plus.google.com/108537760578691322012?prsrc=3'),
    ('weibo', 'http://weibo.com/silveryzhang'),
    ('rss', 'feeds/all.atom.xml'),
    )

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True

SUMMARY_MAX_LENGTH = 32

DISPLAY_PAGES_ON_MENU = True

DISPLAY_CATEGORIES_ON_MENU = True

#ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_DATE_FORMAT = '%H:%M, %a %d %B %Y'

STATIC_PATHS = ['img', 'extra/CNAME', 'extra/README.md']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/README.md': {'path': 'README.md'},
    }
ARTICLE_EXCLUDES = ('pages','extra', 'img')

DISQUS_SITENAME = "crickzhang1"
GITHUB_URL = 'http://github.com/crickzhang1/'

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

#THEME = "notmyidea"
THEME = "pure-single"

# Theme `pure` specific
COVER_IMG_URL = "https://raw.githubusercontent.com/crickzhang1/static_res/master/img/bg.jpg"
PROFILE_IMG_URL = "https://raw.githubusercontent.com/crickzhang1/static_res/master/img/profile-yh.jpg"
TAGLINE = "Part Of COSMOS"
COPYRIGHT_YEARS = "2012-2014"
