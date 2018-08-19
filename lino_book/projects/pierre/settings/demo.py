import datetime

from ..settings import *


class Site(Site):
    is_demo_site = True
    # ignore_dates_after = datetime.date(2019, 05, 22)
    the_demo_date = datetime.date(2017,3,12)
    
SITE = Site(globals())
DEBUG = True
SITE.plugins.ledger.configure(start_year=2016)
