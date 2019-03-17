# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


"""
Default settings for a :ref:`cosi` site "à la Pierre".

"""

from __future__ import unicode_literals

from lino_cosi.lib.cosi.settings import *


class Site(Site):
    languages = 'fr en'
    # demo_fixtures = 'std few_countries minimal_ledger euvatrates \
    # furniture demo demo_bookings demo2'.split()
    demo_fixtures = 'std few_countries minimal_ledger \
    furniture demo demo_bookings demo2'.split()

    #def get_installed_apps(self):
    #    yield super(Site, self).get_installed_apps()
    #    yield 'lino_xl.lib.bevat'

    def setup_plugins(self):
        self.plugins.countries.configure(hide_region=False)
        self.plugins.ledger.configure(use_pcmn=True)
        self.plugins.countries.configure(country_code='BE')
        super(Site, self).setup_plugins()

