.. doctest docs/specs/voga/checkdata.rst
.. _voga.specs.checkdata:

=======================================
Checking for data problems in Lino Voga
=======================================

Lino Voga uses the :ref:`checkdata <book.specs.checkdata>` plugin for managing
data problem messages.


.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.roger.settings.doctests')
>>> from lino.api.doctest import *


Data checkers available in Lino Voga
====================================

In the web interface you can select :menuselection:`Explorer -->
System --> Data checkers` to see a table of all available
checkers.

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
 courses.MemberChecker               Check membership payments
 finan.FinancialVoucherItemChecker   Check for invalid account/partner combination
 ledger.VoucherChecker               Check integrity of ledger vouchers
 memo.PreviewableChecker             Check for previewables needing update
 printing.CachedPrintableChecker     Check for missing target files
 sepa.BankAccountChecker             Check for partner mismatches in bank accounts
 system.BleachChecker                Find unbleached html content
 vat.VatColumnsChecker               Check VAT columns configuration.
=================================== ===============================================
<BLANKLINE>

More information about each checker in the corresponding plugin specs  (e.g.
:class:`beid.SSINChecker <lino_xl.lib.beid.SSINChecker>` is defined in
:mod:`lino_xl.lib.beid` and hence documented in :doc:`/specs/beid`)

Showing all data problem messages
=================================

In the web interface you can select :menuselection:`Explorer -->
System --> Data problems` to see them.

..
    >>> show_menu_path(checkdata.AllProblems)
    Explorer --> System --> Data problems


>>> rt.show(checkdata.AllProblems)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
============= =========================================== ============================================================== ========================================
 Responsible   Database object                             Message                                                        Checker
------------- ------------------------------------------- -------------------------------------------------------------- ----------------------------------------
 Robin Rood    *Recurring event #4 Assumption of Mary*     Event conflicts with Activity #1 001  1.                       Check for conflicting calendar entries
 Robin Rood    *Recurring event #11 Ascension of Jesus*    Event conflicts with Mittagessen (14.05.2015 11:10).           Check for conflicting calendar entries
 Robin Rood    *Recurring event #12 Pentecost*             Event conflicts with 4 other events.                           Check for conflicting calendar entries
 Rolf Rompen   *Mittagessen (14.05.2015 11:10)*            Event conflicts with Recurring event #11 Ascension of Jesus.   Check for conflicting calendar entries
 Robin Rood    *First meeting (25.05.2015 13:30)*          Event conflicts with Recurring event #12 Pentecost.            Check for conflicting calendar entries
 Robin Rood    *Absent for private reasons (25.05.2015)*   Event conflicts with Recurring event #12 Pentecost.            Check for conflicting calendar entries
 Robin Rood    *Karl Kaivers (ME)*                         Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Laura Laschet (ME)*                        Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Josefine Leffin (MEL)*                     Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Marie-Louise Meier (ME)*                   Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Alfons Radermacher (ME)*                   Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Christian Radermacher (MEL)*               Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Edgard Radermacher (ME)*                   Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Guido Radermacher (ME)*                    Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Hedi Radermacher (ME)*                     Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Jean Radermacher (ME)*                     Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Erna Ärgerlich (ME)*                       Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Jean Dupont (ME)*                          Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Marie-Louise Vandenmeulenbos (MEC)*        Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Bernd Brecht (ME)*                         Member until 2015-12-31, but no payment.                       Check membership payments
 Robin Rood    *Jérôme Jeanémart (ME)*                     Member until 2015-12-31, but no payment.                       Check membership payments
============= =========================================== ============================================================== ========================================
<BLANKLINE>
