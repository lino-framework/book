import datetime

from ..settings import *


class Site(Site):
    # project_name = 'cosi_et'
    is_demo_site = True
    # ignore_dates_after = datetime.date(2019, 05, 22)
    the_demo_date = datetime.date(2019, 6, 12)
    # default_ui = 'lino_react.react'

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('ledger', 'start_year', 2018)

SITE = Site(globals())
DEBUG = True
