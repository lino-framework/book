.. doctest docs/specs/calview.rst
.. _book.specs.calview:

================================
``calview`` : Calendar view
================================

.. currentmodule:: lino_xl.lib.calview

The :mod:`lino_xl.lib.calview` plugin adds a calendar view.

.. contents::
  :local:


.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.avanti1.settings.demo')
>>> from lino.api.doctest import *


Calendar views
==============

.. class:: CalendarView

    Base class for all calendar views (daily, weekly and monthly).

.. class:: DailyView

    Shows a calendar navigator with a configurable daily view.

.. class:: WeeklyView

    Shows a calendar navigator with a configurable weekly view.

.. class:: MonthlyView

    Shows a calendar navigator with a configurable monthly view.



The daily planner
=================

The daily planner is a table that shows an overview on all events of a day.

>>> rt.show(calview.DailyPlanner)
============ =================================================== ==========
 Time range   External                                            Internal
------------ --------------------------------------------------- ----------
 *All day*    *Rolf Rompen Absent for private reasons Absences*
 *AM*         *08:30 Romain Raffault Rencontre Meeting*
 *PM*
============ =================================================== ==========
<BLANKLINE>


.. class:: DailyPlanner

    The virtual table used to render the daily planner.


.. >>> dd.today()
   datetime.date(2017, 2, 15)


.. class:: PlannerColumns

    A choicelist that defines the columns to appear in the daily
    planner. This list can be modified locally.


A default configuration has two columns in the daily planner:

>>> rt.show(calview.PlannerColumns)
======= ========== ==========
 value   name       text
------- ---------- ----------
 10      external   External
 20      internal   Internal
======= ========== ==========
<BLANKLINE>


.. class:: DailyPlannerRow

    A database object that represents one row of the :term:`daily planner`.
    The default configuration has "AM", "PM" and "All day".

>>> rt.show(calview.DailyPlannerRows)
===== ============= ================== ================== ============ ==========
 No.   Designation   Designation (de)   Designation (fr)   Start time   End time
----- ------------- ------------------ ------------------ ------------ ----------
 1     AM            Vormittags         Avant-midi                      12:00:00
 2     PM            Nachmittags        Après-midi         12:00:00
===== ============= ================== ================== ============ ==========
<BLANKLINE>



.. Tested translations:

    >>> # settings.SITE.languages

    >>> with translation.override('de'):
    ...     rt.show(calview.DailyPlanner, header_level=1)
    ===========
    Tagesplaner
    ===========
    =============== =================================================== ========
     Zeitabschnitt   Extern                                              Intern
    --------------- --------------------------------------------------- --------
     *Ganztags*      *Rolf Rompen Absent for private reasons Absences*
     *Vormittags*    *08:30 Romain Raffault Rencontre Versammlung*
     *Nachmittags*
    =============== =================================================== ========
    <BLANKLINE>

    >>> rt.show(calview.DailyPlanner, language="fr", header_level=1)
    =======================
    Planificateur quotidien
    =======================
    =================== =================================================== =========
     Time range          Externe                                             Interne
    ------------------- --------------------------------------------------- ---------
     *Journée entière*   *Rolf Rompen Absent for private reasons Absences*
     *Avant-midi*        *08:30 Romain Raffault Rencontre Réunion*
     *Après-midi*
    =================== =================================================== =========
    <BLANKLINE>

    >>> print(cal.Event.update_guests.help_text)
    Populate or update the list of participants for this calendar
    entry according to the suggestions.

    >>> with translation.override('de'):
    ...     print(str(cal.Event.update_guests.help_text))
    ... #doctest: +NORMALIZE_WHITESPACE +REPORT_CDIFF
    Teilnehmerliste für diesen Kalendereintrag füllen entsprechend der Vorschläge.

    >>> cal.Event.update_guests.help_text.__class__
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
    <class 'django.utils.functional...__proxy__'>
