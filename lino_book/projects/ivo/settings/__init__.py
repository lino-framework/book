# -*- coding: UTF-8 -*-
"""
The base settings module for :mod:`lino_book.projects.ivo`.
"""

from lino_voga.lib.voga.settings import *


class Site(Site):

    default_ui = 'lino_react.react'

    title = "Lino Voga for Ivo"
    languages = "en et"

    workflows_module = 'lino_xl.lib.courses.workflows.doodle'

    demo_fixtures = """std minimal_ledger
    demo tantsukool demo_bookings payments demo2 checkdata""".split()

    # def get_installed_apps(self):
    #     yield super(Site, self).get_installed_apps()
    #     yield 'lino.modlib.publisher'
    #
    
    def get_apps_modifiers(self, **kw):
        kw = super(Site, self).get_apps_modifiers(**kw)
        # alternative implementations:
        kw.update(courses='lino_voga.lib.roger.courses')
        return kw

    def get_plugin_configs(self):
        yield super(Site, self).get_plugin_configs()
        yield ('countries', 'hide_region', True)
        yield ('countries', 'country_code', 'EE')
        yield ('vat', 'declaration_plugin', 'lino_xl.lib.eevat')
        # yield ('ledger', 'use_pcmn', True)
        yield ('ledger', 'start_year', 2020)
        # yield ('react', 'url_prefix', 'admin')
        # yield ('react', 'force_url_prefix', True)
