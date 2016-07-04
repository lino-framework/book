"""Default settings for a :mod:`lino_book.projects.dump` site.

This module instantiates a :setting:`SITE` variable and thus is
designed to be used directly as a :setting:`DJANGO_SETTINGS_MODULE`.

"""

from ..settings import *
from lino.utils import i2d


class Site(Site):
    languages = "en de fr"

    the_demo_date = i2d(20160702)

SITE = Site(globals())
# SECRET_KEY = "20227"  # see :djangoticket:`20227`
DEBUG = True

