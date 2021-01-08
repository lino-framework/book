# -*- coding: UTF-8 -*-
# Copyright 2017-2020 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The settings package.

.. autosummary::
   :toctree:

   demo
   doctests
   memory



"""

from lino_tera.lib.tera.settings import *


class Site(Site):

    # title = "lino_book.projects.lydia"

    demo_fixtures = 'std minimal_ledger demo demo_bookings payments demo2'.split()

    languages = 'en de fr'

# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
