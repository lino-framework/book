.. doctest docs/specs/holidays.rst
.. _xl.specs.holidays:

=================
Defining holidays
=================


Some initialization:

>>> from lino import startup
>>> startup('lino_book.projects.min9.settings.demo')
>>> from lino.api.doctest import *
>>> settings.SITE.verbose_client_info_message = True
>>> from lino.api import rt, _
>>> from atelier.utils import i2d
>>> RecurrentEvent = cal.RecurrentEvent
>>> Recurrencies = cal.Recurrencies


Recurrent event rules
=====================

Here are the standard holidays, defined as recurrent event rules
:class:`RecurrentEvent <lino.modlib.cal.RecurrentEvent>` by
:mod:`lino.modlib.cal.fixtures.std`:

>>> rt.show(cal.RecurrentEvents)
============ ========== ============================ ======================== =================================== ==================== =====================
 Start date   End Date   Designation                  Designation (et)         Designation (fr)                    Recurrency           Calendar entry type
------------ ---------- ---------------------------- ------------------------ ----------------------------------- -------------------- ---------------------
 01/01/2013              New Year's Day               Uusaasta                 Jour de l'an                        yearly               Holidays
 11/02/2013              Rosenmontag                  Rosenmontag              Lundi de carnaval                   Relative to Easter   Holidays
 13/02/2013              Ash Wednesday                Ash Wednesday            Mercredi des Cendres                Relative to Easter   Holidays
 29/03/2013              Good Friday                  Good Friday              Vendredi Saint                      Relative to Easter   Holidays
 31/03/2013              Easter sunday                Easter sunday            Pâques                              Relative to Easter   Holidays
 01/04/2013              Easter monday                Easter monday            Lundi de Pâques                     Relative to Easter   Holidays
 01/05/2013              International Workers' Day   kevadpüha                Premier Mai                         yearly               Holidays
 09/05/2013              Ascension of Jesus           Ascension of Jesus       Ascension                           Relative to Easter   Holidays
 20/05/2013              Pentecost                    Pentecost                Pentecôte                           Relative to Easter   Holidays
 21/07/2013              National Day                 Belgia riigipüha         Fête nationale                      yearly               Holidays
 15/08/2013              Assumption of Mary           Assumption of Mary       Assomption de Marie                 yearly               Holidays
 31/10/2013              All Souls' Day               All Souls' Day           Commémoration des fidèles défunts   yearly               Holidays
 01/11/2013              All Saints' Day              All Saints' Day          Toussaint                           yearly               Holidays
 11/11/2013              Armistice with Germany       Armistice with Germany   Armistice                           yearly               Holidays
 25/12/2013              Christmas                    Esimene Jõulupüha        Noël                                yearly               Holidays
============ ========== ============================ ======================== =================================== ==================== =====================
<BLANKLINE>

Relative to Easter
==================

Certain yearly events don't have a fixed day of the year but move
together with the Easter day.  They are also known as `moveable feasts
<https://en.wikipedia.org/wiki/Moveable_feast_%28observance_practice%29>`_.

Let's look at one of them, Ash Wednesday::

>>> ash = RecurrentEvent.objects.get(name="Ash Wednesday")

.. the following doesn't yet work:

    >>> # screenshot(ash, 'ash.png')

    followed by a .. image:: ash.png directive.


The :mod:`lino.modlib.cal.fixtures.std` fixture generates
automatically all Ash Wednesdays for a range of years:

>>> rt.show(cal.EntriesByController, master_instance=ash, nosummary=True)
==================== =================== ================= ======== ================== =====================
 When                 Short description   Workflow          No.      Responsible user   Calendar entry type
-------------------- ------------------- ----------------- -------- ------------------ ---------------------
 Wed 06/03/2019       Ash Wednesday       **? Suggested**   7                           Holidays
 Wed 14/02/2018       Ash Wednesday       **? Suggested**   6                           Holidays
 Wed 01/03/2017       Ash Wednesday       **? Suggested**   5                           Holidays
 Wed 10/02/2016       Ash Wednesday       **? Suggested**   4                           Holidays
 Wed 18/02/2015       Ash Wednesday       **? Suggested**   3                           Holidays
 Wed 05/03/2014       Ash Wednesday       **? Suggested**   2                           Holidays
 **Total (6 rows)**                                         **27**
==================== =================== ================= ======== ================== =====================
<BLANKLINE>

Actually the user sees just the summary:

>>> rt.show(cal.EntriesByController, master_instance=ash)
March 2019: *Wed 06.*?
February 2018: *Wed 14.*?
March 2017: *Wed 01.*?
February 2016: *Wed 10.*?
February 2015: *Wed 18.*?
March 2014: *Wed 05.*?
Suggested : 6 ,  Draft : 0 ,  Published : 0 ,  Took place : 0 ,  Cancelled : 0

That range of years depends on some configuration variables:

- :attr:`ignore_dates_before <lino.modlib.cal.Plugin.ignore_dates_before>`
- :attr:`ignore_dates_after <lino.modlib.cal.Plugin.ignore_dates_after>`
- :attr:`lino.modlib.system.SiteConfig.max_auto_events`
- :attr:`the_demo_date <lino.core.site.Site.the_demo_date>`

>>> dd.plugins.cal.ignore_dates_before
>>> dd.plugins.cal.ignore_dates_after
datetime.date(2019, 10, 23)
>>> settings.SITE.site_config.max_auto_events
72
>>> settings.SITE.the_demo_date
datetime.date(2014, 10, 23)

Manually creating moving feasts
===============================

Event rules for moving feasts have their :attr:`every_unit
<lino.modlib.cal.models.RecurrentEvent.every_unit>` field set to
:attr:`easter <lino.modlib.cal.choicelists.Recurrencies.easter>`.

Lino then computes the offset (number of days) your :attr:`start_date`
and the easter date of the start year, and generates subsequent events
by moving their date so that the offset remains the same.

Lino uses the `easter()
<https://labix.org/python-dateutil#head-8863c4fc47132b106fcb00b9153e3ac0ab486a0d>`_
function of `dateutil` for getting the Easter date.

>>> from dateutil.easter import easter
>>> easter(2015)
datetime.date(2015, 4, 5)



Adding a local moving feast
===========================

.. verify that no events have actually been saved:
   >>> cal.Event.objects.count()
   171

We can add our own local custom holidays which depend on easter.

We create a *recurrent event rule* for it, specifying :attr:`easter
<lino.modlib.cal.choicelists.Recurrencies.easter>`.  in their
:attr:`every_unit <lino.modlib.cal.RecurrentEvent.every_unit>`
field.

>>> holidays = cal.EventType.objects.get(**dd.str2kw('name', _("Holidays")))
>>> obj = RecurrentEvent(name="Karneval in Kettenis",
...     every_unit=Recurrencies.easter,
...     start_date=i2d(20160209), event_type=holidays)
>>> obj.full_clean()
>>> obj.find_start_date(i2d(20160209))
datetime.date(2016, 2, 9)

>>> ar = rt.login()
>>> wanted, unwanted = obj.get_wanted_auto_events(ar)
>>> len(wanted)
4
>>> print(ar.response['info_message'])
Generating events between 2016-02-09 and 2019-10-23 (max. 72).
Reached upper date limit 2019-10-23 for 4

.. Note that owner_type in below snippet depends on whether the database has
   been prepared under Py2 or Py3

>>> wanted[1]  #doctest: +ELLIPSIS
Event(start_date=2016-02-09,owner_type=...,summary='Karneval in Kettenis',auto_type=1,priority=<Priorities.normal:30>,event_type=2,state=<EntryStates.suggested:10>)

.. verify that no events have actually been saved:
   >>> cal.Event.objects.count()
   171
