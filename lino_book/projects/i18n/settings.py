# -*- coding: UTF-8 -*-

from lino_book.projects.min2.settings import *


class Site(Site):
    languages = 'en de fr et nl pt-br'

SITE = Site(globals(), no_local=True)

SECRET_KEY = "20227"  # see :djangoticket:`20227`
