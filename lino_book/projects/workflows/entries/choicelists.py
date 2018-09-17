# -*- coding: UTF-8 -*-
## Copyright 2013-2018 Rumma & Ko Ltd
## This file is part of the Lino project.

from __future__ import unicode_literals

from lino.api import dd, _


class EntryStates(dd.Workflow):
    pass
    
add = EntryStates.add_item
add('10', _("New"), 'new', button_text="☐")
add('20', _("Started"), 'started', button_text="⚒")
add('30', _("Done"), 'done', button_text="☑")
add('40', _("Sleeping"), 'sleeping', button_text="☾")
add('50', _("Cancelled"), 'cancelled', button_text="☒")

