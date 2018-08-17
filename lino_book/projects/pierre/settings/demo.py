import datetime

from ..settings import *


class Site(Site):
    # project_name = 'cosi_be_fr'
    is_demo_site = True
    # ignore_dates_after = datetime.date(2019, 05, 22)
    the_demo_date = datetime.date(2017,3,12)
    
    demo_fixtures = 'std few_countries minimal_ledger \
    furniture demo demo_bookings payments demo2'.split()

SITE = Site(globals())
DEBUG = True
SITE.plugins.ledger.configure(start_year=2016)
