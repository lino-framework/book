.. _avanti.specs.cal:

=================================
Calendar functions in Lino Avanti
=================================

.. How to test just this document:

    $ doctest docs/specs/avanti/cal.rst
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *


.. contents::
  :local:

>>> base = '/choices/cal/Guests/partner'
>>> show_choices("rolf", base + '?query=') #doctest: +ELLIPSIS
<br/>
ABAD Aábdeen (114)
ABBAS Aábid (115)
ABBASI Aáishá (118)
ABDALLA Aádil (120)
...

>>> show_choices("audrey", base + '?query=') #doctest: +ELLIPSIS
<br/>
Aábdeen (114) from Eupen
Aábid (115) from Eupen
Aáishá (118) from Eupen
Aádil (120) from Eupen
Aáish (127) from Eupen
Aákif (128) from Eupen
...


>>> rt.show(cal.GuestStates)
======= ========= ============ ========= ========
 value   name      Afterwards   text      Symbol
------- --------- ------------ --------- --------
 10      invited   No           Invited   ?
 40      present   Yes          Present   ☑
 50      absent    Yes          Absent    ☉
 60      excused   No           Excused   ⚕
======= ========= ============ ========= ========
<BLANKLINE>


>>> rt.show(cal.EntryStates)
======= ============ ============ ======== =================== ======== ============= =========
 value   name         text         Symbol   Edit participants   Stable   Transparent   No auto
------- ------------ ------------ -------- ------------------- -------- ------------- ---------
 10      suggested    Suggested    ?        Yes                 No       No            No
 20      draft        Draft        ☐        Yes                 No       No            No
 50      took_place   Took place   ☑        Yes                 Yes      No            No
 70      cancelled    Cancelled    ☒        No                  Yes      Yes           Yes
======= ============ ============ ======== =================== ======== ============= =========
<BLANKLINE>


:class:`GuestsByPartner` shows only presences on entries which took
place, and it sorts them chronologically:

>>> obj = avanti.Client.objects.get(pk=115)
>>> rt.show(cal.GuestsByPartner, obj)
*16.01.☑*, *17.01.⚕*, *19.01.☑*, *20.01.☑*, *23.01.⚕*, *24.01.☑*, *26.01.?*, *27.01.☑*, *30.01.⚕*, *31.01.☑*, *02.02.☑*, *03.02.⚕*, *06.02.☑*, *07.02.☑*, *09.02.?*, *10.02.?*, *13.02.?*, *14.02.?*, *16.02.?*, *17.02.?*, *20.02.?*, *21.02.?*, *23.02.?*, *24.02.?*
