# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

from .demo import *
SITE = Site(globals())
DATABASES['default']['NAME'] = ':memory:'
