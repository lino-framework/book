from lino_book.projects.belref.settings import *
SITE = Site(
    globals(), title=Site.verbose_name + " demo",
    default_ui='lino.modlib.bootstrap3')
DEBUG = True
# the following line should always be commented out in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'
