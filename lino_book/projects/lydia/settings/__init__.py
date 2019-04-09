# -*- coding: UTF-8 -*-
# Copyright 2017-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""
The settings package.

.. autosummary::
   :toctree:

   demo
   doctests
   memory



"""

from __future__ import print_function
from __future__ import unicode_literals

from lino_tera.lib.tera.settings import *


class Site(Site):

    verbose_name = "Lino Tera for Lydia"
   
    demo_fixtures = 'std minimal_ledger demo demo_bookings payments demo2'.split()

    languages = 'en de fr'
    
# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
