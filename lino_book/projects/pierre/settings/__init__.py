# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""
Default settings for a :ref:`cosi` site "à la Pierre".

"""

from __future__ import unicode_literals

from lino_cosi.projects.std.settings import *


class Site(Site):
    languages = 'fr en'
    demo_fixtures = 'std few_countries euvatrates furniture \
    minimal_ledger demo demo_bookings demo2'.split()

    def setup_plugins(self):
        self.plugins.countries.configure(hide_region=False)
        self.plugins.ledger.configure(use_pcmn=True)
        self.plugins.countries.configure(country_code='BE')
        super(Site, self).setup_plugins()

