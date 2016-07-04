# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)
"""
This is the base for all settings of lino_book.projects.dumps

.. autosummary::
   :toctree:

   demo


"""

from lino.projects.std.settings import *


class Site(Site):
    title = "Lino Dumps"

    demo_fixtures = 'demo'

    def get_installed_apps(self):
        yield super(Site, self).get_installed_apps()

        yield 'lino_book.projects.dumps'
