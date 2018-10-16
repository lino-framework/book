.. doctest docs/specs/avanti/cal.rst
.. _avanti.specs.cal:

=================================
Calendar functions in Lino Avanti
=================================

This document describes how the :mod:`lino_xl.lib.cal` is being used
in :ref:`avanti`.

..  doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *


.. contents::
  :local:

.. currentmodule:: lino_avanti.lib.cal

.. class:: Guest

    .. attribute:: absence_reason

        Why the pupil was absent.  Choices for this field are defined
        in :class:`AbsenceReasons`.

Calendar workflow
=================

It's almost :mod:`lino_xl.lib.cal.workflows.voga`, except that we
removed the transition it.

In existing data (until June 2018) they differentiate between
"excused" and "absent".  In August 2018 we decided to no longer do
this differentiation.

>>> rt.show(cal.GuestStates)
======= ========= ============ ========= =============
 value   name      Afterwards   text      Button text
------- --------- ------------ --------- -------------
 10      invited   No           Invited   ?
 40      present   Yes          Present   ☑
 50      missing   Yes          Missing   ☉
 60      excused   No           Excused   ⚕
======= ========= ============ ========= =============
<BLANKLINE>

In Avanti there is a state "exused" but we removed the transition it:

>>> show_workflow(cal.GuestStates.workflow_actions)
============= ============== =========== ============== =========================
 Action name   Verbose name   Help text   Target state   Required states
------------- -------------- ----------- -------------- -------------------------
 wf1           ☑              Present     Present        invited
 wf2           ☉              Missing     Missing        invited
 wf3           ?              Invited     Invited        missing present excused
============= ============== =========== ============== =========================


>>> rt.show(cal.EntryStates)
======= ============ ============ ============= =================== ======== ============= =========
 value   name         text         Button text   Edit participants   Stable   Transparent   No auto
------- ------------ ------------ ------------- ------------------- -------- ------------- ---------
 10      suggested    Suggested    ?             Yes                 No       No            No
 20      draft        Draft        ☐             Yes                 No       No            No
 50      took_place   Took place   ☑             Yes                 Yes      No            No
 70      cancelled    Cancelled    ☒             No                  Yes      Yes           Yes
======= ============ ============ ============= =================== ======== ============= =========
<BLANKLINE>

>>> show_workflow(cal.EntryStates.workflow_actions)
============= ============== ============ ============== ================================
 Action name   Verbose name   Help text    Target state   Required states
------------- -------------- ------------ -------------- --------------------------------
 reset_event   Reset          Draft        Draft          suggested took_place cancelled
 wf2           Took place     Took place   Took place     suggested draft cancelled
 wf3           ☒              Cancelled    Cancelled      suggested draft took_place
============= ============== ============ ============== ================================

     

>>> base = '/choices/cal/Guests/partner'
>>> show_choices("rolf", base + '?query=') #doctest: +ELLIPSIS
<br/>
ABAD Aábdeen (114)
ABBASI Aáishá (118)
ABDALLA Aádil (120)
ABDALLAH Aáish (127)
ABDELLA Aákif (128)
...

>>> show_choices("audrey", base + '?query=') #doctest: +ELLIPSIS
<br/>
(114) from Eupen
(118) from Eupen
(120) from Eupen
(127) from Eupen
(128) from Eupen
(136) from Eupen
...



:class:`GuestsByPartner` shows all presences except those in more than
one week and sorts them chronologically:

>>> obj = avanti.Client.objects.get(pk=115)
>>> rt.show(cal.GuestsByPartner, obj)
January 2017: *Mon 16.*☑ *Tue 17.*☑ *Thu 19.*☑ *Fri 20.*☑ *Mon 23.*☑ *Tue 24.*☑ *Thu 26.*☒ *Fri 27.*☑ *Mon 30.*☑ *Tue 31.*☑
Suggested : 8 ,  Draft : 0 ,  Took place : 13 ,  Cancelled : 1


Absence reasons
===============

In :ref:`avanti` we record and analyze why pupils have been missing.

.. class:: AbsenceReasons

    The table of possible absence reasons.
    
    Accessible via :menuselection:`Configure --> Calendar --> Absence
    reasons`.

    >>> show_menu_path(cal.AbsenceReasons)
    Configure --> Calendar --> Absence reasons

    >>> rt.show(cal.AbsenceReasons)
    ==== ==================== ========================== ====================
     ID   Designation          Designation (de)           Designation (fr)
    ---- -------------------- -------------------------- --------------------
     1    Sickness             Krankheit                  Sickness
     2    Other valid reason   Sonstiger gültiger Grund   Other valid reason
     3    Unknown              Unbekannt                  Inconnu
     4    Unjustified          Unberechtigt               Unjustified
    ==== ==================== ========================== ====================
    <BLANKLINE>
   
   
.. class:: AbsenceReason

   .. attribute:: name

                  
