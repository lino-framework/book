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


>>> rt.show(cal.GuestStates)
======= ========= ============ ========= =============
 value   name      Afterwards   text      Button text
------- --------- ------------ --------- -------------
 10      invited   No           Invited   ?
 40      present   Yes          Present   ☑
 50      absent    Yes          Absent    ☉
 60      excused   No           Excused   ⚕
======= ========= ============ ========= =============
<BLANKLINE>


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


:class:`GuestsByPartner` shows all presences except those in more than
one week and sorts them chronologically:

>>> obj = avanti.Client.objects.get(pk=115)
>>> rt.show(cal.GuestsByPartner, obj)
*16.01.*☑, *17.01.*☑, *19.01.*☑, *20.01.*☑, *23.01.*☑, *24.01.*☑, *26.01.*☒, *27.01.*☑, *30.01.*☑, *31.01.*☑, *02.02.*☑, *03.02.*☑, *06.02.*☑, *07.02.*☑, *09.02.*?, *10.02.*?, *13.02.*?, *14.02.*?, *16.02.*?, *17.02.*?, *20.02.*?, *21.02.*?



