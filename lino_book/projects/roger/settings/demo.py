import datetime

from ..settings import *


class Site(Site):
    is_demo_site = True
    the_demo_date = datetime.date(2015, 5, 22)
    # ignore_dates_after = datetime.date(2019, 05, 22)
    use_java = False
    # use_ipdict = True


SITE = Site(globals())
DEBUG = True

# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
