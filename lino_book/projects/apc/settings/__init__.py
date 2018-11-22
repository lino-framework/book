# -*- coding: UTF-8 -*-
# Copyright 2014-2016 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
Default settings for a :ref:`cosi` "à la APC".

"""

from __future__ import unicode_literals

from lino_cosi.lib.cosi.settings import *


class Site(Site):
    languages = 'de fr en'
    # demo_fixtures = 'std few_countries minimal_ledger euvatrates \
    # furniture \
    # demo demo_bookings payments demo2'.split()
    demo_fixtures = 'std few_countries minimal_ledger \
    furniture \
    demo demo_bookings payments demo2'.split()

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(hide_region=False)
        self.plugins.ledger.configure(use_pcmn=True)
        self.plugins.countries.configure(country_code='BE')

