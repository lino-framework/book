.. doctest docs/specs/voga/checkdata.rst
.. _voga.specs.checkdata:

=======================================
Checking for data problems in Lino Voga
=======================================

Lino Voga offers some functionality for managing data problems.

See also :ref:`book.specs.checkdata`.

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.edmund.settings.doctests')
>>> from lino.api.doctest import *


Data checkers available in Lino Voga
====================================

In the web interface you can select :menuselection:`Explorer -->
System --> Data checkers` to see a table of all available
checkers.

.. 
    >>> show_menu_path(checkdata.Checkers)
    Explorer --> System --> Data checkers
    

>>> rt.show(checkdata.Checkers)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=================================== ===============================================
 value                               text
----------------------------------- -----------------------------------------------
 beid.SSINChecker                    Check for invalid SSINs
 cal.ConflictingEventsChecker        Check for conflicting calendar entries
 cal.EventGuestChecker               Entries without participants
 cal.LongEntryChecker                Too long-lasting calendar entries
 cal.ObsoleteEventTypeChecker        Obsolete generated calendar entries
 countries.PlaceChecker              Check data of geographical places.
 finan.FinancialVoucherItemChecker   Check for invalid account/partner combination
 ledger.VoucherChecker               Check integrity of ledger vouchers
 printing.CachedPrintableChecker     Check for missing target files
 sepa.BankAccountChecker             Check for partner mismatches in bank accounts
 system.BleachChecker                Find unbleached html content
 vat.VatColumnsChecker               Check VAT columns configuration.
=================================== ===============================================
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
