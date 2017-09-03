from lino_book.projects.polly.settings import *


class Site(Site):

    user_types_module = 'lino_book.projects.myroles.myroles'

SITE = Site(globals())

# SECRET_KEY = 123
# DEBUG = True
