# -*- coding: UTF-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

from django.db import models
from lino.api import dd, _
from lino.mixins import BabelDesignated
from .choicelists import Bars

class Foo(BabelDesignated):

    class Meta(object):
        app_label = 'dumps'
    #     verbose_name = _("Foo")
    #     verbose_name_plural = _("Foos")

    last_visit = models.DateTimeField(_("Last visit"), editable=False)
    bar = Bars.field(default='sale')
    
class Foos(dd.Table):
    model = Foo


