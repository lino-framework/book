# -*- coding: UTF-8 -*-
# Copyright 2012-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""The Django settings module for Lino CMS.

"""

from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino CMS"
    version = "0.1"
    author = 'Rumma & Ko OÜ'
    author_email = 'luc@lino-framework.org'
    use_auth = False

    default_ui = 'lino_react.react'
    # default_ui = 'lino.modlib.extjs'
    # default_ui = 'lino.modlib.publisher'
    # default_ui = 'lino.modlib.bootstrap3'
    # default_ui = 'lino_openui5.openui5'
    # default_ui = 'lino_xl.lib.pages'

    languages = 'en de fr'

    # project_model = 'tickets.Project'

    demo_fixtures = ['std', 'demo', 'demo2', 'checkdata']
    # demo_fixtures = ['std', 'demo', 'demo2', 'intro']

    sidebar_width = 3

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        yield 'lino.modlib.extjs'
        yield 'lino.modlib.memo'
        yield 'lino.modlib.checkdata'  # fill body_preview during prep
        # yield 'lino.modlib.bootstrap3'
        yield 'lino.modlib.users'
        yield 'lino.modlib.publisher'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.contacts'
        #~ yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.blogs'
        # yield 'lino.modlib.tickets'
        yield 'lino_xl.lib.pages'
        # yield 'lino_book.projects.cms'

    # def get_plugin_configs(self):
    #     yield super(Site, self).get_plugin_configs()
    #     if self.default_ui == 'lino.modlib.bootstrap3':
    #         yield ('bootstrap3', 'url_prefix', None)
