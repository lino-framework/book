import datetime
from lino_voga.lib.voga.settings import *

class Site(Site):
    # default_ui = 'lino_react.react'
    title = "voga1"
    languages = "en"
    is_demo_site = True
    the_demo_date = datetime.date(2020, 10, 22)
    # ignore_dates_after = datetime.date(2019, 05, 22)
    use_java = False
    # use_ipdict = True

SITE = Site(globals())
DEBUG = True
