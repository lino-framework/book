.. _cosi.specs.ledger:
.. _cosi.tested.ledger:

===========================
General Ledger in Lino Così
===========================

.. to test only this document:

      $ python setup.py test -s tests.DocsTests.test_ledger
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_cosi.projects.std.settings.demo')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")
    >>> translation.activate('en')

This document describes the concepts of general accounting as
implemented by the :mod:`lino_cosi.lib.ledger` plugin.

This document is based on the following other specification:

- :ref:`cosi.specs.accounting`

Table of contents:

.. contents::
   :depth: 1
   :local:


What is a ledger?
=================

A ledger is a book in which the monetary transactions of a business
are posted in the form of debits and credits (from `1
<http://www.thefreedictionary.com/ledger>`__).

In Lino, the ledger is a central table of Movements_, owned by
Vouchers_ which are grouped into Journals_.


.. _cosi.specs.ledger.movements:

Movements
=========

Movements are stored in the database using the :class:`ledger.Movement
<lino_cosi.lib.ledger.models.Movement>` model.


.. _cosi.specs.ledger.vouchers:

Vouchers
========

A **voucher** is any document which serves as legal proof for a ledger
transaction. Examples of vouchers include invoices, bank statements,
or payment orders.

Vouchers are stored in the database using the :class:`ledger.voucher
<lino_cosi.lib.ledger.models.Voucher>` model. But note that the
voucher model is not being used directly.


.. _cosi.specs.ledger.journals:

Journals
========

A **journal** is a named sequence of numbered *vouchers*.

Journals are stored in the database using the :class:`ledger.Journal
<lino_cosi.lib.ledger.models.Journal>` model.


>>> ses.show(ledger.Journals,
...     column_names="ref name trade_type account dc")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== =============================== ===================== ====================== ============ ================================ ===========================
 Reference   Designation                     Designation (fr)      Designation (de)       Trade type   Account                          Primary booking direction
----------- ------------------------------- --------------------- ---------------------- ------------ -------------------------------- ---------------------------
 SLS         Sales invoices                  Factures vente        Verkaufsrechnungen     Sales                                         Debit
 SLC         Sales credit notes              Sales credit notes    Gutschriften Verkauf   Sales                                         Credit
 PRC         Purchase invoices               Factures achat        Einkaufsrechnungen     Purchases                                     Credit
 PMO         Payment Orders                  Payment Orders        Zahlungsaufträge       Purchases    (5810) Payment Orders Bestbank   Credit
 CSH         Cash                            Caisse                Kasse                               (5700) Cash                      Debit
 BNK         Bestbank                        Bestbank              Bestbank                            (5500) Bestbank                  Debit
 MSC         Miscellaneous Journal Entries   Opérations diverses   Diverse Buchungen                   (5700) Cash                      Debit
=========== =============================== ===================== ====================== ============ ================================ ===========================
<BLANKLINE>






Trade types
===========

This plugin introduces the concept of **trade types**.

The default list of trade types is:

>>> rt.show(ledger.TradeTypes)
======= =========== ===========
 value   name        text
------- ----------- -----------
 S       sales       Sales
 P       purchases   Purchases
 W       wages       Wages
 C       clearings   Clearings
======= =========== ===========
<BLANKLINE>

Your application might have a different list.  You can see the
actually configured list for your site via :menuselection:`Explorer
--> Accounting --> Trade types`.

See :class:`lino_cosi.lib.ledger.choicelists.TradeTypes` for technical
details.


Match rules
===========

A **match rule** specifies that a movement into given account can be
*cleared* using a given journal.

>>> ses.show(ledger.MatchRules)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
==== ================== =====================================
 ID   Account            Journal
---- ------------------ -------------------------------------
 1    (4000) Customers   Sales invoices (SLS)
 2    (4000) Customers   Sales credit notes (SLC)
 3    (4400) Suppliers   Purchase invoices (PRC)
 4    (4000) Customers   Payment Orders (PMO)
 5    (4400) Suppliers   Payment Orders (PMO)
 6    (4000) Customers   Cash (CSH)
 7    (4400) Suppliers   Cash (CSH)
 8    (4000) Customers   Bestbank (BNK)
 9    (4400) Suppliers   Bestbank (BNK)
 10   (4000) Customers   Miscellaneous Journal Entries (MSC)
 11   (4400) Suppliers   Miscellaneous Journal Entries (MSC)
==== ================== =====================================
<BLANKLINE>


For example a payment order can be used to pay an open suppliers
invoice or (less frequently) to send back money that a customer had
paid too much.

>>> jnl = ledger.Journal.objects.get(ref="PMO")
>>> jnl
Journal #4 ('Payment Orders (PMO)')

>>> rt.show(ledger.MatchRulesByJournal, jnl)
==================
 Account
------------------
 (4000) Customers
 (4400) Suppliers
==================
<BLANKLINE>

Or a sales invoice can be used to clear another sales invoice.

>>> jnl = ledger.Journal.objects.get(ref="SLS")
>>> jnl
Journal #1 ('Sales invoices (SLS)')
>>> rt.show(ledger.MatchRulesByJournal, jnl)
==================
 Account
------------------
 (4000) Customers
==================
<BLANKLINE>



Debtors
=======

**Debtors** are partners who received credit from us and thereefore
are in debt towards us. The most common debtors are customers,
i.e. partners who received a sales invoice from us (and did not yet
pay that invoice).

>>> ses.show(ledger.Debtors, column_names="partner partner_id balance")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
==================== ========= ===============
 Partner              ID        Balance
-------------------- --------- ---------------
 Kaivers Karl         140       2 999,85
 Groteclaes Gregory   131       47,59
 Lambertz Guido       141       2 039,82
 Emonts Erich         149       3 854,78
 Mießen Michael       147       280,00
 Johnen Johann        137       639,92
 Malmendier Marc      145       679,81
 **Total (7 rows)**   **990**   **10 541,77**
==================== ========= ===============
<BLANKLINE>


**Creditors** are partners hwo gave us credit. The most common
creditors are providers, i.e. partners who send us a purchase invoice
(which we did not yet pay).

>>> ses.show(ledger.Creditors, column_names="partner partner_id balance")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==================== ========= ==============
 Partner              ID        Balance
-------------------- --------- --------------
 AS Express Post      181       41,10
 AS Matsalu Veevärk   182       143,40
 Eesti Energia AS     183       5 045,18
 Chantraine Marc      119       1 578,25
 Engels Edgar         128       1 631,92
 Evers Eberhart       126       195,93
 **Total (6 rows)**   **919**   **8 635,78**
==================== ========= ==============
<BLANKLINE>


Partner 149 has 2 open sales invoices:

>>> obj = contacts.Partner.objects.get(pk=149)
>>> ses.show(ledger.DebtsByPartner, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==================== ============== ===================== ==========
 Due date             Balance        Debts                 Payments
-------------------- -------------- --------------------- ----------
 17/05/2015           535,00         `SLS 23 <Detail>`__
 18/05/2015           3 319,78       `SLS 24 <Detail>`__
 **Total (2 rows)**   **3 854,78**
==================== ============== ===================== ==========
<BLANKLINE>



Fiscal years
============

Each ledger movement happens in a given **fiscal year**.  Lino has a
table with **fiscal years**.

In a default configuration there is one fiscal year for each calendar
year between :attr:`start_year
<lino_cosi.lib.ledger.Plugin.start_year>` and ":func:`today
<lino.core.site.Site.today>` plus 5 years".

>>> dd.plugins.ledger.start_year
2015

>>> dd.today().year + 5
2020

>>> rt.show(ledger.FiscalYears)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= ====== ======
 value   name   text
------- ------ ------
 15             2015
 16             2016
 17             2017
 18             2018
 19             2019
 20             2020
======= ====== ======
<BLANKLINE>


Accounting periods
==================

Each ledger movement happens in a given **accounting period**.  
An accounting period usually corresponds to a month of the calendar.
Accounting periods are automatically created the first time they are
needed by some operation.


>>> rt.show(ledger.AccountingPeriods)
=========== ============ ============ ============= ======= ========
 Reference   Start date   End date     Fiscal Year   State   Remark
----------- ------------ ------------ ------------- ------- --------
 2015-01     01/01/2015   31/01/2015   2015          Open
 2015-02     01/02/2015   28/02/2015   2015          Open
 2015-03     01/03/2015   31/03/2015   2015          Open
 2015-04     01/04/2015   30/04/2015   2015          Open
 2015-05     01/05/2015   31/05/2015   2015          Open
=========== ============ ============ ============= ======= ========
<BLANKLINE>

The *reference* of a new accounting period is computed by applying the
voucher's entry date to the template defined in the
:attr:`date_to_period_tpl
<lino_cosi.lib.ledger.models.AccountingPeriod.get_for_date>` setting.  
The default implementation leads to the following references:

>>> print(ledger.AccountingPeriod.get_ref_for_date(i2d(19940202)))
1994-02
>>> print(ledger.AccountingPeriod.get_ref_for_date(i2d(20150228)))
2015-02
>>> print(ledger.AccountingPeriod.get_ref_for_date(i2d(20150401)))
2015-04

You may manually create other accounting periods. For example

- `2015-00` might stand for a fictive "opening" period before January
  2015 and after December 2014.

- `2015-13` might stand for January 2016 in a company which is
  changing their fiscal year from "January-December" to "July-June".



