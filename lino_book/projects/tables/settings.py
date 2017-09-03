from lino.projects.std.settings import *
# SITE = Site(globals(), 'tables', anonymous_user_type = '900')    
SITE = Site(globals(), 'lino_book.projects.tables')
SITE.demo_fixtures = ['demo']

DEBUG = True
