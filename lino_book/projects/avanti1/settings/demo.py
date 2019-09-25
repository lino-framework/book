# -*- coding: UTF-8 -*-
# Copyright 2017-2019 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)
"""Defines and instantiates a demo version of a Lino Avanti Site."""

import datetime

from ..settings import *


class Site(Site):

    the_demo_date = datetime.date(2017, 2, 15)
    languages = "en de fr"


SITE = Site(globals())

DEBUG = True

# the following line should not be active in a checked-in version
#~ DATABASES['default']['NAME'] = ':memory:'

# SITE.eidreader_timeout = 25
