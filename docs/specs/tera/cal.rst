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


This document describes how we use the :mod:`lino_xl.lib.cal` plugin
in Tera.


The calendar summary view
=========================

Note that the months are listed in reverse chronological order while
the days within a month in normal order.


>>> obj = rt.models.courses.Course.objects.order_by('id').first()
>>> rt.show(cal.EntriesByController, obj)
January 2015: *Tue 13.*☑ *Tue 27.*☉
February 2015: *Tue 10.*☑ *Tue 24.*☑
March 2015: *Tue 10.*☑
Suggested : 0 ,  Scheduled : 0 ,  Took place : 4 ,  Called off : 0 ,  Missed : 1


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
 70      cancelled    Called off   ⚕             No                  Yes      Yes           Yes
 60      missed       Missed       ☉             No                  Yes      No            Yes
======= ============ ============ ============= =================== ======== ============= =========
<BLANKLINE>


>>> rt.show(cal.EntryStates, language="de")
====== ============ =============== ============= ======================= ======== =================== =========
 Wert   name         Text            Button text   Teilnehmer bearbeiten   Stabil   nicht blockierend   No auto
------ ------------ --------------- ------------- ----------------------- -------- ------------------- ---------
 10     suggested    Vorschlag       ?             Ja                      Nein     Nein                Nein
 20     draft        Geplant         ☐             Ja                      Nein     Nein                Nein
 50     took_place   Stattgefunden   ☑             Ja                      Ja       Nein                Nein
 70     cancelled    Abgesagt        ⚕             Nein                    Ja       Ja                  Ja
 60     missed       Verpasst        ☉             Nein                    Ja       Nein                Ja
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
 cancelled    Called off   Excused
 missed       Missed       Missing
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
=========== ======================== ================== ======================== ================ ============= ==================== =================
 Reference   Designation              Designation (de)   Designation (fr)         Planner column   Appointment   Force guest states   Locks all rooms
----------- ------------------------ ------------------ ------------------------ ---------------- ------------- -------------------- -----------------
             Group meeting            Gruppengespräch    Group meeting                             Yes           No                   No
             Holidays                 Feiertage          Jours fériés             External         No            No                   Yes
             Individual appointment   Einzelgespräch     Individual appointment                    Yes           Yes                  No
             Internal                 Intern             Interne                  Internal         Yes           No                   No
             Meeting                  Versammlung        Réunion                  External         Yes           No                   No
=========== ======================== ================== ======================== ================ ============= ==================== =================
<BLANKLINE>



Daily planner
=============

>>> rt.show(cal.DailyPlanner)
============ ========== ===============
 Time range   External   Internal
------------ ---------- ---------------
 *AM*
 *PM*                    *13:30 robin*
 *All day*
============ ========== ===============
<BLANKLINE>


