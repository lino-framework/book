# don't forget to import the default workflows:
from lino_noi.lib.noi.workflows import *

from django.conf import settings
from lino.modlib.about.choicelists import TimeZones
TimeZones.clear()
add = TimeZones.add_item
add('01', settings.TIME_ZONE or 'UTC', 'default')
add('02', "Europe/Tallinn")
add('03', "Europe/Brussels")
add('04', "Africa/Tunis")
