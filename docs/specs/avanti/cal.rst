.. _avanti.specs.cal:

=================================
Calendar functions in Lino Avanti
=================================

.. How to test just this document:

    $ python setup.py test -s tests.SpecsTests.test_avanti_cal
    
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

>>> show_choices("martina", base + '?query=') #doctest: +ELLIPSIS
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
