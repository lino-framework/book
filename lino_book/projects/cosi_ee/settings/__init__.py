# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)


"""
Default settings for an Estonian :ref:`cosi` site.

- `Estonian VAT rates
  <http://www.emta.ee/index.php?id=28460>`_


"""

from __future__ import unicode_literals

from lino_cosi.lib.cosi.settings import *


class Site(Site):
    languages = 'en et'
    # demo_fixtures = 'std all_countries minimal_ledger euvatrates \
    # eesti furniture \
    # demo demo2'.split()
    demo_fixtures = 'std all_countries minimal_ledger \
    eesti furniture \
    demo demo2'.split()

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino_xl.lib.eevat'

    def setup_plugins(self):
        "See :meth:`lino.core.site.Site.setup_plugins`."
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(hide_region=False)
        self.plugins.ledger.configure(use_pcmn=True)
        self.plugins.countries.configure(country_code='EE')
