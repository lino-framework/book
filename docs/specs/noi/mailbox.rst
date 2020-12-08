.. _noi.specs.mailbox:

====================
Lino Noi and mailbox
====================


.. How to test just this document:

    $ python setup.py test -s tests.SpecsTests.test_mailbox
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.noi1e.settings.demo')
    >>> from lino.api.doctest import *

TODO: write some explanations...

>>> rt.show('mailbox.Messages', column_names="subject from_header to_header")
================================================= ========================================= ================
 Subject                                           From header                               To header
------------------------------------------------- ----------------------------------------- ----------------
 Re: Tonis in Vigala                               Tanel Saimre <tanel.saimre@example.com>   Luc Saffre
 Tonis in Vigala                                   Luc Saffre <luc.saffre@example.com>       Tanel Saimre
 parameters crash course by example                Luc Saffre <luc.saffre@example.com>       Tonis Piip
 Next hangout                                      Luc Saffre <luc.saffre@example.com>       Khchine Hamza
 with attachments                                  tonis <tonis@Pluto>                       team@localhost
 Re: Furnitures company                            "Stephanie.c" <stephanie.c@bigao-f.com>
 *****SPAM***** re: buy more instagram followers   "STEVEN" <medinaluca1@gmail.com>
================================================= ========================================= ================
<BLANKLINE>
