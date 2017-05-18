# -*- coding: UTF-8 -*-
# Copyright 2016 Luc Saffre
# License: BSD (see file COPYING for details)

import datetime

from ..settings import *


class Site(Site):
    the_demo_date = datetime.date(2015, 5, 23)
    languages = "en de fr"


SITE = Site(globals())
DEBUG = True

# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
