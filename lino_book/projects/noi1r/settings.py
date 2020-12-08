# -*- coding: UTF-8 -*-
# Copyright 2015-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino_book.projects.noi1e.settings.demo import *

class Site(Site):
    default_ui = 'lino_react.react'
    title = "Noi React demo"

    if False:
        use_websockets = True
        def get_installed_apps(self):
            yield super(Site, self).get_installed_apps()
            yield 'lino.modlib.chat'


x = DATABASES, SECRET_KEY
# the following will set new values for DATABASES and SECRET_KEY, which we are
# going to restore from those we imported previously.
SITE = Site(globals())
DATABASES, SECRET_KEY = x

# from django.utils.log import DEFAULT_LOGGING
# from pprint import pprint
# pprint(DEFAULT_LOGGING)
