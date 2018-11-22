# -*- coding: UTF-8 -*-
"""
The base settings module for :mod:`lino_book.projects.roger`.
"""

from __future__ import unicode_literals
from __future__ import print_function

from lino_voga.lib.voga.settings import *


class Site(Site):
    default_ui = 'lino_openui5.openui5'

    title = "Lino Voga à la Roger"
    languages = "en de fr"

    # demo_fixtures = """std few_countries minimal_ledger euvatrates
    # demo voga demo_bookings payments demo2 checkdata""".split()
    demo_fixtures = """std few_countries minimal_ledger 
    demo voga demo_bookings payments demo2 checkdata""".split()

    def setup_plugins(self):
        """
        Change the default value of certain plugin settings.
       
        """
        super(Site, self).setup_plugins()
        self.plugins.countries.configure(hide_region=True)
        self.plugins.countries.configure(country_code='BE')
        self.plugins.ledger.configure(start_year=2014)
        self.plugins.ledger.configure(use_pcmn=True)

    def get_apps_modifiers(self, **kw):
        kw = super(Site, self).get_apps_modifiers(**kw)
        # alternative implementations:
        kw.update(courses='lino_voga.lib.roger.courses')
        return kw
