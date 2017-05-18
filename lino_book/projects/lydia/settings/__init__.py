# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
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

    verbose_name = "Lino for Lydia"
   
    demo_fixtures = 'std demo novat minimal_ledger demo_bookings payments demo2'.split()
    project_model = 'contacts.Person'

    languages = 'en de fr'
    
    # workflows_module = 'lino_xl.lib.tickets.workflows'

    user_types_module = 'lino_tera.lib.tera.user_types'

# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
