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


>>> rt.show(cal.DailyPlanner)
============= ================ ==========
 Description   external         internal
------------- ---------------- ----------
 *AM*          *08:30 romain*
 *PM*
 *All day*
============= ================ ==========
<BLANKLINE>


In :ref:`tera` we introduce a new calendar entry state "missed".  This
is used because a *missed* appointment may get invoiced while a
*cancelled* appointment not.


>>> rt.show(cal.EntryStates)
======= ============ ============ ======== =================== ======== ============= =========
 value   name         text         Symbol   Edit participants   Stable   Transparent   No auto
------- ------------ ------------ -------- ------------------- -------- ------------- ---------
 10      suggested    Suggested    ?        Yes                 No       No            No
 20      draft        Draft        ☐        Yes                 No       No            No
 50      took_place   Took place   ☑        Yes                 Yes      No            No
 70      cancelled    Cancelled    ☒        No                  Yes      Yes           Yes
 60      missed       Missed                No                  Yes      No            No
======= ============ ============ ======== =================== ======== ============= =========
<BLANKLINE>


>>> rt.show(cal.EntryStates, language="de")
====== ============ =============== ======== ======================= ======== =================== =========
 Wert   name         Text            Symbol   Teilnehmer bearbeiten   Stabil   nicht blockierend   No auto
------ ------------ --------------- -------- ----------------------- -------- ------------------- ---------
 10     suggested    Vorschlag       ?        Ja                      Nein     Nein                Nein
 20     draft        Entwurf         ☐        Ja                      Nein     Nein                Nein
 50     took_place   Stattgefunden   ☑        Ja                      Ja       Nein                Nein
 70     cancelled    Storniert       ☒        Nein                    Ja       Ja                  Ja
 60     missed       Verpasst                 Nein                    Ja       Nein                Nein
====== ============ =============== ======== ======================= ======== =================== =========
<BLANKLINE>
