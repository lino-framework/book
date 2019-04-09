import datetime

from ..settings import *


class Site(Site):
    # project_name = 'cosi_et'
    is_demo_site = True
    # ignore_dates_after = datetime.date(2019, 05, 22)
    the_demo_date = datetime.date(2017, 3, 12)

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('ledger', 'start_year', 2015)

SITE = Site(globals())
DEBUG = True

