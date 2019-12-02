import datetime

from ..settings import *

class Site(Site):
    project_name = 'apc'
    is_demo_site = True
    # ignore_dates_after = datetime.date(2019, 5, 22)
    the_demo_date = datetime.date(2015, 3, 12)

    # default_ui = "lino.modlib.extjs"
    # default_ui = "lino_react.react"

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('ledger', 'start_year', 2014)


SITE = Site(globals())

DEBUG = True
