# -*- coding: UTF-8 -*-
# Copyright 2014-2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""

.. autosummary::
   :toctree:

   doctests
   demo
   www



"""

from lino_riche.lib.riche.settings import *


class Site(Site):
    
    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps` for Lino
        riche.

        """
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.restful'
        # yield 'lino_xl.lib.caldav'
