# -*- coding: UTF-8 -*-
# Copyright 2013-2018 Luc Saffre
# License: BSD (see file COPYING for details)


from __future__ import unicode_literals

from lino.projects.std.settings import *


class Site(Site):

    title = "Lino Events"
    verbose_name = "Lino Events"

    demo_fixtures = 'demo vor'.split()

    languages = 'de fr nl'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.system'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.events'


SITE = Site(globals())

DEBUG = True
