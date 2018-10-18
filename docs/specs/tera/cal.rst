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
 20      draft        Draft        ☐             Yes                 No       No            No
 50      took_place   Took place   ☑             Yes                 Yes      No            No
 70      cancelled    Cancelled    ⚕             No                  Yes      Yes           Yes
 60      missed       Missed       ☉             No                  Yes      No            Yes
======= ============ ============ ============= =================== ======== ============= =========
<BLANKLINE>


>>> rt.show(cal.EntryStates, language="de")
====== ============ =============== ============= ======================= ======== =================== =========
 Wert   name         Text            Button text   Teilnehmer bearbeiten   Stabil   nicht blockierend   No auto
------ ------------ --------------- ------------- ----------------------- -------- ------------------- ---------
 10     suggested    Vorschlag       ?             Ja                      Nein     Nein                Nein
 20     draft        Entwurf         ☐             Ja                      Nein     Nein                Nein
 50     took_place   Stattgefunden   ☑             Ja                      Ja       Nein                Nein
 70     cancelled    Storniert       ⚕             Nein                    Ja       Ja                  Ja
 60     missed       Verpasst        ☉             Nein                    Ja       Nein                Ja
====== ============ =============== ============= ======================= ======== =================== =========
<BLANKLINE>

Lino Tera uses the :attr:`EntryState.guest_state` attribute 

>>> rt.show(cal.EntryStates, column_names='name text guest_state')
============ ============ =============
 name         text         Guest state
------------ ------------ -------------
 suggested    Suggested
 draft        Draft
 took_place   Took place   Present
 cancelled    Cancelled    Excused
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
 50     missing   Ja             Missing        ☉
 60     excused   Nein           Entschuldigt   ⚕
====== ========= ============== ============== =============
<BLANKLINE>

>>> show_workflow(cal.GuestStates.workflow_actions, language="de")
============= ============== ============== ============== =========================
 Action name   Verbose name   Help text      Target state   Required states
------------- -------------- -------------- -------------- -------------------------
 wf1           ☑              Anwesend       Anwesend       invited
 wf2           ☉              Missing        Missing        invited
 wf3           ⚕              Entschuldigt   Entschuldigt   invited
 wf4           ?              Eingeladen     Eingeladen     missing present excused
============= ============== ============== ============== =========================

Calendar entry types
====================


>>> rt.show(cal.EventTypes)
======================== ======================== ======================== ================ ============= ==================== =================
 Designation              Designation (de)         Designation (fr)         Planner column   Appointment   Force guest states   Locks all rooms
------------------------ ------------------------ ------------------------ ---------------- ------------- -------------------- -----------------
 Holidays                 Feiertage                Jours fériés             External         No            No                   Yes
 Meeting                  Versammlung              Réunion                  External         Yes           No                   No
 Internal                 Intern                   Interne                  Internal         Yes           No                   No
 Individual appointment   Individual appointment   Individual appointment                    Yes           Yes                  No
 Group meeting            Group meeting            Group meeting                             Yes           No                   No
======================== ======================== ======================== ================ ============= ==================== =================
<BLANKLINE>



Daily planner
=============

>>> rt.show(cal.DailyPlanner)
=========== ========== ===============
 Activity    External   Internal
----------- ---------- ---------------
 *AM*
 *PM*                   *13:30 robin*
 *All day*
=========== ========== ===============
<BLANKLINE>


