.. doctest docs/specs/voga/checkdata.rst
.. _voga.specs.checkdata:

=======================================
Checking for data problems in Lino Voga
=======================================

..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.edmund.settings.doctests')
    >>> from lino.api.doctest import *


Lino Voga offers some functionality for managing data
problems.

See also :ref:`book.specs.checkdata`.

Data checkers available in Lino Voga
====================================

In the web interface you can select :menuselection:`Explorer -->
System --> Data checkers` to see a table of all available
checkers.

.. 
    >>> show_menu_path(checkdata.Checkers)
    Explorer --> System --> Data checkers
    

>>> rt.show(checkdata.Checkers)
================================= ===============================================
 value                             text
--------------------------------- -----------------------------------------------
 printing.CachedPrintableChecker   Check for missing target files
 countries.PlaceChecker            Check data of geographical places.
 ledger.VoucherChecker             Check integrity of ledger movements
 sepa.BankAccountChecker           Check for partner mismatches in bank accounts
 beid.BeIdCardHolderChecker        Check for invalid SSINs
 cal.EventGuestChecker             Entries without participants
 cal.ConflictingEventsChecker      Check for conflicting calendar entries
 cal.ObsoleteEventTypeChecker      Obsolete event type of generated entries
 cal.LongEntryChecker              Too long-lasting calendar entries
================================= ===============================================
<BLANKLINE>


Showing all problems
====================

In the web interface you can select :menuselection:`Explorer -->
System --> Data problems` to see them.

..
    >>> show_menu_path(checkdata.AllProblems)
    Explorer --> System --> Data problems


>>> rt.show(checkdata.AllProblems)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
No data to display
