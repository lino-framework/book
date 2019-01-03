# -*- coding: UTF-8 -*-
# Copyright 2016-2018 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

import datetime

from ..settings import *


class Site(Site):
    the_demo_date = datetime.date(2015, 5, 23)
    languages = "en de fr"
    use_ipdict = True

    # legacy_data_path = '...'

    # def get_installed_apps(self):
    #     yield super(Site, self).get_installed_apps()
    #     yield 'lino_xl.lib.tim2lino'

SITE = Site(globals())
DEBUG = True


# SITE.plugins.tim2lino.configure(
#     languages='de fr',
#     timloader_module='lino_xl.lib.tim2lino.spzloader',
#     dbf_table_ext='.FOX',
#     #use_dbf_py=True,
#     use_dbfread=True)


# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'
