# -*- coding: UTF-8 -*-
# Copyright 2017-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
Base settings module for every Teamy site.
"""

from lino.projects.std.settings import *

from lino.api import _

class Site(Site):
    verbose_name = "Lino Chatter"
    description = _("a simple chatting app.")

    demo_fixtures = 'std demo demo2'.split()
    user_types_module = 'lino_xl.lib.xl.user_types'
    use_websockets = True

    languages = 'en'

    default_ui = "lino_react.react"

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.users'
        yield 'lino.modlib.notify'
        yield 'lino_xl.lib.groups'
