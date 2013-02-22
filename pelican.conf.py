#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"Science and Civilization"
SITEURL = 'http://markbetnel.com/scicivS2013'

TIMEZONE = 'America/New_York'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

# Blogroll
LINKS =  (
    ('Stanford Encyclopedia of Philosophy', 'http://plato.stanford.edu/')	
        )

# Social widget
SOCIAL = (
         ('HomeworkFeed', SITEURL + '/feeds/homework.atom.xml'),
         ('LessonsFeed', SITEURL + '/feeds/lessons.atom.xml'),
	 ('QuizzesFeed', SITEURL + '/feeds/quizzes.atom.xml')
	 )

DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    
