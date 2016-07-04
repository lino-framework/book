# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)

"""Database models for `lino_book.projects.dumps`.

"""

from django.db import models
from lino.api import _
from lino.mixins import BabelNamed


class Foo(BabelNamed):

    class Meta(object):
        app_label = 'dumps'
        verbose_name = _("Foo")
        verbose_name_plural = _("Foos")

    last_visit = models.DateTimeField(_("Last visit"), editable=False)

    
