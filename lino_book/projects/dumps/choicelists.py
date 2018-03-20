# -*- coding: UTF-8 -*-
# Copyright 2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from lino.api import dd, _

class Bars(dd.ChoiceList):
    verbose_name = _("Bar")
    verbose_name_plural = _("Bars")

add = Bars.add_item
add('10', _("Sale"), 'sale')
add('20', _("Purchase"), 'purchase')
add('30', _("Profit"), 'profit')
add('40', _("Loss"), 'loss')

    
