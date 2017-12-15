# -*- coding: UTF-8 -*-
# Copyright 2016-2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""The demo fixture for this tutorial.
"""
from __future__ import unicode_literals

# import pytz
from datetime import datetime
from django.conf import settings
from django.utils.timezone import make_aware
from lino.api import dd, _
from lino_book.projects.dumps.models import Foo


if settings.USE_TZ:
    # mytz = pytz.timezone(settings.TIME_ZONE)
    def dt(*args):
        return make_aware(datetime(*args))
        # return make_aware(datetime(*args), timezone=mytz)
else:
    def dt(*args):
        return datetime(*args)


def objects():
    yield Foo(
        name="First", name_de="Erster", name_fr="Premier",
        last_visit=dt(2016, 7, 2, 23, 55, 12))
    yield Foo(
        last_visit=dt(2016, 7, 3, 0, 10, 23),
        **dd.str2kw('name', _("January")))
    yield Foo(
        last_visit=dt(2016, 10, 30, 4, 34, 0),
        **dd.babelkw('name', en="Three", de="Drei",
                     fr="Trois", et="Kolm"))
    # on the last sunday of october, at 3am all clocks are turned back
    # by one hour to 2am again. So on that day when you say 2:34 in a
    # naive timestamp


