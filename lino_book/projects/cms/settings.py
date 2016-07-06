# -*- coding: UTF-8 -*-
# Copyright 2012-2015 Luc Saffre
# License: BSD (see file COPYING for details)

"""The Django settings module for Lino CMS.

"""

from django.utils.translation import ugettext_lazy as _

from lino.projects.std.settings import *


class Site(Site):

    verbose_name = "Lino CMS"
    version = "0.1"
    author = 'Luc Saffre'
    author_email = 'luc@lino-framework.org'

    default_ui = 'lino_xl.lib.pages'

    languages = 'en de fr'

    project_model = 'tickets.Project'

    sidebar_width = 3

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.gfks'
        yield 'lino.modlib.extjs'
        yield 'lino.modlib.bootstrap3'
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_xl.lib.contacts'
        #~ yield 'lino_xl.lib.outbox'
        yield 'lino_xl.lib.blogs'
        # yield 'lino.modlib.tickets'
        yield 'lino_xl.lib.pages'
        yield 'lino_book.projects.cms'


SITE = Site(globals())
