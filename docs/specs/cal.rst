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

When generating automatic calendar events, Lino supports the following
date recurrenies:

>>> rt.show(cal.Recurrencies)
======= ============= ====================
 value   name          text
------- ------------- --------------------
 O       once          once
 D       daily         daily
 W       weekly        weekly
 M       monthly       monthly
 Y       yearly        yearly
 P       per_weekday   per weekday
 E       easter        Relative to Easter
======= ============= ====================
<BLANKLINE>

Addding a duration unit

>>> start_date = i2d(20160327)
>>> cal.Recurrencies.once.add_duration(start_date, 1)
Traceback (most recent call last):
...
Exception: Invalid DurationUnit once

>>> cal.Recurrencies.daily.add_duration(start_date, 1)
datetime.date(2016, 3, 28)

>>> cal.Recurrencies.weekly.add_duration(start_date, 1)
datetime.date(2016, 4, 3)

>>> cal.Recurrencies.monthly.add_duration(start_date, 1)
datetime.date(2016, 4, 27)

>>> cal.Recurrencies.yearly.add_duration(start_date, 1)
datetime.date(2017, 3, 27)

>>> cal.Recurrencies.easter.add_duration(start_date, 1)
datetime.date(2017, 4, 16)


Recurrent events
================

In :mod:`lino_book.projects.min2` we have a database model
:class:`RecurrentEvent <lino_xl.lib.cal.models.RecurrentEvent>` used
to generate holidays.  See also :ref:`xl.specs.holidays`.

We are going to use this model for demonstrating some more features
(which it inherits from :class:`RecurrenceSet
<lino_xl.lib.cal.mixins.RecurrenceSet>` and an :class:`EventGenerator
<lino_xl.lib.cal.mixins.EventGenerator>`)


>>> list(rt.models_by_base(cal.RecurrenceSet))
[<class 'lino_xl.lib.cal.models.RecurrentEvent'>]

>>> list(rt.models_by_base(cal.EventGenerator))
[<class 'lino_xl.lib.cal.models.RecurrentEvent'>]

>>> obj = cal.RecurrentEvent(start_date=i2d(20160628))
>>> obj.tuesday = True
>>> obj.every_unit = cal.Recurrencies.weekly
>>> print(obj.weekdays_text)
Every Tuesday

>>> obj.every
1

>>> obj.every = 2
>>> print(obj.weekdays_text)
Every 2nd Tuesday

>>> obj.every_unit = cal.Recurrencies.monthly
>>> print(obj.weekdays_text)
Every 2nd month


>>> rt.show(cal.EventTypes, column_names="id name")
==== ============= ================== ==================
 ID   Designation   Designation (et)   Designation (fr)
---- ------------- ------------------ ------------------
 1    Holidays      Holidays           Jours fériés
 2    Meeting       Meeting            Réunion
==== ============= ================== ==================
<BLANKLINE>

>>> obj.event_type = cal.EventType.objects.get(id=1)
>>> obj.max_events = 5

>>> ses = rt.login('robin')
>>> wanted, unwanted = obj.get_wanted_auto_events(ses)
>>> for num, e in wanted.items():
...     print(dd.fds(e.start_date))
28/06/2016
30/08/2016
01/11/2016
03/01/2017
07/03/2017

Note that above dates are not exactly every 2 months because 

- they are only on Tuesdays
- Lino also avoids conflicts with existing events

>>> cal.Event.objects.order_by('start_date')[0]
Event #1 ("Event #1 New Year's Day (01.01.2013)")

>>> obj.monday = True
>>> obj.wednesday = True
>>> obj.thursday = True
>>> obj.friday = True
>>> obj.saturday = True
>>> obj.sunday = True
>>> obj.start_date=i2d(20120628)
>>> wanted, unwanted = obj.get_wanted_auto_events(ses)
>>> for num, e in wanted.items():
...     print(dd.fds(e.start_date))
28/06/2012
28/08/2012
28/10/2012
28/12/2012
28/02/2013




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
 31/10/2014   09:40:00     11:40:00                    Romain Raffault
 31/10/2014   08:30:00     09:30:00                    Rando Roosi
============ ============ ========== ========= ====== ==================
<BLANKLINE>

