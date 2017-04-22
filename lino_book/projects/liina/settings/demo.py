# import os ; print "20161219 %s (pid:%s)" % (__name__, os.getpid())

import datetime

from ..settings import *


class Site(Site):
    the_demo_date = datetime.date(2017, 3, 16)
    languages = "en et"

    # default_ui = 'lino_extjs6.extjs6'
    
    # default_ui = 'lino.modlib.bootstrap3'
    # default_user = 'anonymous'
    
SITE = Site(globals())
# print "20161219 b"
DEBUG = True

# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
