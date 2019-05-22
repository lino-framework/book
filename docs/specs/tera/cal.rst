.. doctest docs/specs/tera/cal.rst
.. _specs.tera.cal:

=====================
Calendar in Lino Tera
=====================

.. doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models


This document describes the :mod:`lino_tera.lib.cal` plugin which extends
:mod:`lino_xl.lib.cal` for Tera.

.. currentmodule:: lino_tera.lib.cal


The calendar summary view
=========================

Note that the months are listed in reverse chronological order while
the days within a month in normal order.


>>> obj = rt.models.courses.Course.objects.order_by('id').first()
>>> rt.show(cal.EntriesByController, obj)
March 2015: *Tue 10.*☑
February 2015: *Tue 24.*☑ *Tue 10.*☑
January 2015: *Tue 27.*☉ *Tue 13.*☑
Suggested : 0 ,  Scheduled : 0 ,  Took place : 4 ,  Missed : 1 ,  Called off : 0


Missed calendar entries
=======================

In :ref:`tera` we introduce a new calendar entry state "missed" for
entries where the guest missed the appointment without a valid reason.
A *missed* appointment may get invoiced while a *cancelled*
appointment not.

Changed the symbol for a "Cancelled" calendar entry from ☉ to
⚕. Because the symbol ☉ (a sun) is used for "Missed".  The sun reminds
a day on the beach while the ⚕ reminds a drugstore.


>>> rt.show(cal.EntryStates)
======= ============ ============ ============= =================== ======== ============= =========
 value   name         text         Button text   Edit participants   Stable   Transparent   No auto
------- ------------ ------------ ------------- ------------------- -------- ------------- ---------
 10      suggested    Suggested    ?             Yes                 No       No            No
 20      draft        Scheduled    ☐             Yes                 No       No            No
 50      took_place   Took place   ☑             Yes                 Yes      No            No
 60      missed       Missed       ☉             No                  Yes      No            Yes
 70      cancelled    Called off   ⚕             No                  Yes      Yes           Yes
======= ============ ============ ============= =================== ======== ============= =========
<BLANKLINE>


>>> rt.show(cal.EntryStates, language="de")
====== ============ =============== ============= ======================= ======== =================== =========
 Wert   name         Text            Button text   Teilnehmer bearbeiten   Stabil   nicht blockierend   No auto
------ ------------ --------------- ------------- ----------------------- -------- ------------------- ---------
 10     suggested    Vorschlag       ?             Ja                      Nein     Nein                Nein
 20     draft        Geplant         ☐             Ja                      Nein     Nein                Nein
 50     took_place   Stattgefunden   ☑             Ja                      Ja       Nein                Nein
 60     missed       Verpasst        ☉             Nein                    Ja       Nein                Ja
 70     cancelled    Abgesagt        ⚕             Nein                    Ja       Ja                  Ja
====== ============ =============== ============= ======================= ======== =================== =========
<BLANKLINE>


:ref:`tera` uses the :attr:`EntryState.guest_state` attribute.

>>> rt.show(cal.EntryStates, column_names='name text guest_state')
============ ============ =============
 name         text         Guest state
------------ ------------ -------------
 suggested    Suggested
 draft        Scheduled
 took_place   Took place   Present
 missed       Missed       Missing
 cancelled    Called off   Excused
============ ============ =============
<BLANKLINE>


Guest workflow
==============

>>> rt.show(cal.GuestStates, language="de")
====== ========= ============== ============== =============
 Wert   name      Nachträglich   Text           Button text
------ --------- -------------- -------------- -------------
 10     invited   Nein           Eingeladen     ?
 40     present   Ja             Anwesend       ☑
 50     missing   Ja             Fehlt          ☉
 60     excused   Nein           Entschuldigt   ⚕
====== ========= ============== ============== =============
<BLANKLINE>

>>> show_workflow(cal.GuestStates.workflow_actions, language="de")
============= ============== ============== ============== =========================
 Action name   Verbose name   Help text      Target state   Required states
------------- -------------- -------------- -------------- -------------------------
 wf1           ☑              Anwesend       Anwesend       invited
 wf2           ☉              Fehlt          Fehlt          invited
 wf3           ⚕              Entschuldigt   Entschuldigt   invited
 wf4           ?              Eingeladen     Eingeladen     missing present excused
============= ============== ============== ============== =========================

Calendar entry types
====================


>>> rt.show(cal.EventTypes)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== ======================== ================== ======================== ================ ============= ===================== =================
 Reference   Designation              Designation (de)   Designation (fr)         Planner column   Appointment   Automatic presences   Locks all rooms
----------- ------------------------ ------------------ ------------------------ ---------------- ------------- --------------------- -----------------
             Group meeting            Gruppengespräch    Group meeting                             Yes           No                    No
             Holidays                 Feiertage          Jours fériés             External         No            No                    Yes
             Individual appointment   Einzelgespräch     Individual appointment                    Yes           Yes                   No
             Internal                 Intern             Interne                  Internal         Yes           No                    No
             Meeting                  Versammlung        Réunion                  External         Yes           No                    No
=========== ======================== ================== ======================== ================ ============= ===================== =================
<BLANKLINE>



Daily planner
=============

>>> rt.show(cal.DailyPlanner)
============ ========== =======================================
 Time range   External   Internal
------------ ---------- ---------------------------------------
 *All day*
 *AM*
 *PM*                    *13:30 Robin Rood Breakfast Internal*
============ ========== =======================================
<BLANKLINE>


My appointments
===============

The *My appointments* table also shows in the dashboard when it has no
data to display.

>>> rt.login("elmar").show_dashboard()
... #doctest:  +REPORT_UDIFF
-----------------------------------------------
My appointments **New** `⏏ <My appointments>`__
-----------------------------------------------
<BLANKLINE>
No data to display
-----------------------------------
Daily planner `⏏ <Daily planner>`__
-----------------------------------
<BLANKLINE>
============ ========== ==================================================
 Time range   External   Internal
------------ ---------- --------------------------------------------------
 *All day*
 *AM*
 *PM*                    `13:30 Robin Rood Breakfast Internal <Detail>`__
============ ========== ==================================================
<BLANKLINE>



.. class:: Event

    .. attribute:: amount

        The amount perceived during this appointment.

