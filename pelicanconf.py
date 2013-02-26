#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Crick Zhang'
SITENAME = u"Crickzhang's Blog"
SITEURL = 'http://crickzhang1.github.com/blog'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh_CN.utf8'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Github', 'http://github.com'),)

# Social widget
SOCIAL = (('My Github page', 'https://github.com/crickzhang1'),
          )

DEFAULT_PAGINATION = False

USE_FOLDER_AS_CATEGORY = True

SUMMARY_MAX_LENGTH = 100

DISPLAY_PAGES_ON_MENU = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

DEFAULT_DATE_FORMAT = '%H:%M, %a %d %B %Y'
