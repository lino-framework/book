# -*- coding: UTF-8 -*-
# Copyright 2014-2019 Rumma & Ko Ltd
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

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('vat', 'declaration_plugin', 'lino_xl.lib.bevat')
        yield ('countries', 'hide_region', True)
        yield ('countries', 'country_code', 'BE')
        yield ('ledger', 'use_pcmn', True)
        yield ('ledger', 'worker_model', 'contacts.Person')
