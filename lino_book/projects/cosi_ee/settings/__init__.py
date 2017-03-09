# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""
Default settings for an Estonian :ref:`cosi` site.

- `Estonian VAT rates
  <http://www.emta.ee/index.php?id=28460>`_


"""

from __future__ import unicode_literals

from lino_cosi.projects.std.settings import *


class Site(Site):
    "The base for all Estonian Lino Cosi Sites."
    languages = 'en et'
    demo_fixtures = 'std all_countries euvatrates eesti furniture \
    minimal_ledger demo demo2'.split()

    def setup_plugins(self):
        "See :meth:`lino.core.site.Site.setup_plugins`."
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(hide_region=False)
        self.plugins.ledger.configure(use_pcmn=True)
        self.plugins.countries.configure(country_code='EE')
