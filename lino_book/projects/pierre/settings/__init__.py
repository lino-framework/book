# -*- coding: UTF-8 -*-
# Copyright 2014-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


"""
Default settings for a :ref:`cosi` site "à la Pierre".

"""

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

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        # yield ('vat', 'declaration_plugin', 'lino_xl.lib.bevat')
        yield ('countries', 'hide_region', True)
        yield ('countries', 'country_code', 'BE')
        yield ('ledger', 'use_pcmn', True)
        # yield ('ledger', 'worker_model', 'contacts.Person')
