# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import datetime

from lino_voga.lib.voga.settings import *


class Site(Site):

    title = "Lino Voga à la Edmund"
    languages = "en et"

    # demo_fixtures = """std
    # few_countries few_cities
    # minimal_ledger euvatrates
    # demo voga demo2""".split()
    demo_fixtures = """std
    minimal_ledger
    demo voga demo2""".split()

    # ignore_dates_before = None
    the_demo_date = datetime.date(2014, 9, 26)
    # ignore_dates_after = datetime.date(2019, 05, 22)

    def setup_plugins(self):
        """
        Change the default value of certain plugin settings.
       
        """
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(country_code='EE')
        self.plugins.ledger.configure(start_year=2014)
