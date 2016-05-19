.. _book.specs.cal:

=================
Calendar
=================


.. How to test just this document

   $ python setup.py test -s tests.SpecsTests.test_cal

Some initialization:

>>> from lino import startup
>>> startup('lino_book.projects.min2.settings.demo')
>>> from lino.api.doctest import *


See also :mod:`lino_xl.lib.cal.utils`.


Duration units
==============

>>> from lino_xl.lib.cal.choicelists import DurationUnits
>>> start_date = i2d(20111026)
>>> DurationUnits.months.add_duration(start_date, 2)
datetime.date(2011, 12, 26)

>>> from lino.utils import i2d
>>> start_date = i2d(20111026)
>>> DurationUnits.months.add_duration(start_date, 2)
datetime.date(2011, 12, 26)
>>> DurationUnits.months.add_duration(start_date, -2)
datetime.date(2011, 8, 26)

>>> start_date = i2d(20110131)
>>> DurationUnits.months.add_duration(start_date, 1)
datetime.date(2011, 2, 28)
>>> DurationUnits.months.add_duration(start_date, -1)
datetime.date(2010, 12, 31)
>>> DurationUnits.months.add_duration(start_date, -2)
datetime.date(2010, 11, 30)

>>> start_date = i2d(20140401)
>>> DurationUnits.months.add_duration(start_date, 3)
datetime.date(2014, 7, 1)
>>> DurationUnits.years.add_duration(start_date, 1)
datetime.date(2015, 4, 1)


Recurrencies
============

>>> from lino_xl.lib.cal.choicelists import Recurrencies
>>> start_date = i2d(20160327)
>>> Recurrencies.easter.add_duration(start_date, 1)
datetime.date(2017, 4, 16)


Conflicting events
==================

The demo datebase contains two appointments on All Souls' Day:

>>> obj = cal.Event.objects.get(id=30)
>>> print(obj)
Event #30 All Souls' Day (31.10.2014)

>>> rt.show(cal.ConflictingEvents, obj)
============ ============ ========== ========= ====== ==================
 Start date   Start time   End Time   Project   Room   Responsible user
------------ ------------ ---------- --------- ------ ------------------
 31/10/2014   09:40:00     11:40:00                    Robin Rood
 31/10/2014   11:10:00     12:40:00                    Rando Roosi
============ ============ ========== ========= ====== ==================
<BLANKLINE>
