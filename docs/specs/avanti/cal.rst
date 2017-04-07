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
ABAD Aabdeen (114)
ABBAS Aabid (115)
ABBASI Aaisha (118)
ABDALLA Aadil (120)
...

>>> show_choices("audrey", base + '?query=') #doctest: +ELLIPSIS
<br/>
Aabdeen (114) from Eupen
Aabid (115) from Eupen
Aaisha (118) from Eupen
Aadil (120) from Eupen
Aaish (127) from Eupen
Aakif (128) from Eupen
...

>>> show_choices("martina", base + '?query=') #doctest: +ELLIPSIS
<br/>
Aabdeen (114) from Eupen
Aabid (115) from Eupen
Aaisha (118) from Eupen
Aadil (120) from Eupen
Aaish (127) from Eupen
Aakif (128) from Eupen
...

