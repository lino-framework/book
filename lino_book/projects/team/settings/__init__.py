# -*- coding: UTF-8 -*-
# Copyright 2014-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""

.. autosummary::
   :toctree:

   doctests
   demo
   www



"""

from lino_noi.lib.noi.settings import *


class Site(Site):

    workflows_module = 'lino_book.projects.team.workflows'
    
    def get_installed_apps(self):
        # add lino.modlib.restful to the std list of plugins
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.restful'
        # yield 'lino_xl.lib.caldav'
        yield 'lino_xl.lib.mailbox'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        if self.is_installed('extjs'):
            self.plugins.extjs.configure(enter_submits_form=False)
