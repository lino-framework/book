# -*- coding: UTF-8 -*-
"""
The base settings module for :mod:`lino_book.projects.roger`.
"""

from __future__ import unicode_literals
from __future__ import print_function

from lino_voga.lib.voga.settings import *


class Site(Site):

    # default_ui = 'lino_extjs6.extjs6'

    title = "Lino Voga for Roger"
    languages = "en de fr"

    demo_fixtures = """std minimal_ledger 
    demo voga demo_bookings payments demo2 checkdata""".split()

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('countries', 'hide_region', True)
        yield ('countries', 'country_code', 'BE')
        yield ('vat', 'declaration_plugin', 'lino_xl.lib.bevats')
        yield ('ledger', 'use_pcmn', True)
        yield ('ledger', 'start_year', 2014)

    def get_apps_modifiers(self, **kw):
        kw = super(Site, self).get_apps_modifiers(**kw)
        # alternative implementations:
        kw.update(courses='lino_voga.lib.roger.courses')
        return kw
