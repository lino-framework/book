.. _xl.specs.ledger:
.. _cosi.specs.ledger:
.. _cosi.tested.ledger:

===========================
General Ledger in Lino Così
===========================

.. to test only this document:

      $ python setup.py test -s tests.SpecsTests.test_ledger
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.pierre.settings.demo')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")
    >>> translation.activate('en')

This document describes the concepts of general accounting as
implemented by the :mod:`lino_xl.lib.ledger` plugin.

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
<lino_xl.lib.ledger.models.Movement>` model.


.. _cosi.specs.ledger.vouchers:

Vouchers
========

A **voucher** is any document which serves as legal proof for a ledger
transaction. Examples of vouchers include invoices, bank statements,
or payment orders.

Vouchers are stored in the database using the :class:`ledger.voucher
<lino_xl.lib.ledger.models.Voucher>` model. But note that the
voucher model is not being used directly.


.. _cosi.specs.ledger.journals:

Journals
========

A **journal** is a named sequence of numbered *vouchers*.

Journals are stored in the database using the :class:`ledger.Journal
<lino_xl.lib.ledger.models.Journal>` model.


>>> ses.show(ledger.Journals,
...     column_names="ref name trade_type account dc")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== ===================== =============================== ============ ================================ ===========================
 Reference   Designation           Designation (en)                Trade type   Account                          Primary booking direction
----------- --------------------- ------------------------------- ------------ -------------------------------- ---------------------------
 SLS         Factures vente        Sales invoices                  Sales                                         Debit
 SLC         Sales credit notes    Sales credit notes              Sales                                         Credit
 PRC         Factures achat        Purchase invoices               Purchases                                     Credit
 PMO         Payment Orders        Payment Orders                  Purchases    (5810) Payment Orders Bestbank   Credit
 CSH         Caisse                Cash                                         (5700) Cash                      Debit
 BNK         Bestbank              Bestbank                                     (5500) Bestbank                  Debit
 MSC         Opérations diverses   Miscellaneous Journal Entries                (5700) Cash                      Debit
=========== ===================== =============================== ============ ================================ ===========================
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

See :class:`lino_xl.lib.ledger.choicelists.TradeTypes` for technical
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

**Debtors** are partners who received credit from us and therefore are
in debt towards us. The most common debtors are customers,
i.e. partners who received a sales invoice from us and did not yet pay
that invoice.

>>> ses.show(ledger.Debtors, column_names="partner partner_id balance")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
======================= ========== ===============
 Partner                 ID         Balance
----------------------- ---------- ---------------
 Bastiaensen Laurent     116        880,00
 Altenberg Hans          114        5 341,45
 Ausdemwald Alfons       115        1 204,81
 Chantraine Marc         119        4 134,71
 Evertz Bernd            125        1 665,81
 Evers Eberhart          126        1 049,90
 Arens Andreas           112        4 599,77
 Emonts Daniel           127        3 989,85
 Dericum Daniel          120        3 959,70
 Hilgers Henri           133        1 060,00
 ...
 Radermacher Hans        159        525,00
 da Vinci David          164        639,92
 di Rupo Didier          163        3 599,71
 Radermecker Rik         172        2 039,82
 van Veen Vincent        165        465,96
 Eierschal Emil          174        959,81
 Östges Otto             167        770,00
 Jeanémart Jérôme        180        990,00
 Martelaer Mark          171        2 999,85
 Dubois Robin            178        1 199,85
 Denon Denis             179        279,90
 Brecht Bernd            176        535,00
 Keller Karl             177        3 319,78
 **Total (42 rows)**     **6180**   **95 304,60**
======================= ========== ===============
<BLANKLINE>

Partner 116 from above list has two open sales invoices, totalling to
880,00:

>>> obj = contacts.Partner.objects.get(pk=116)
>>> ses.show(ledger.DebtsByPartner, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==================== ============ ===================== ==========
 Due date             Balance      Debts                 Payments
-------------------- ------------ --------------------- ----------
 09/01/2016           280,00       `SLS 4 <Detail>`__
 07/11/2016           600,00       `SLS 50 <Detail>`__
 **Total (2 rows)**   **880,00**
==================== ============ ===================== ==========
<BLANKLINE>

**Creditors** are partners hwo gave us credit. The most common
creditors are providers, i.e. partners who send us a purchase invoice
(which we did not yet pay).

>>> ses.show(ledger.Creditors, column_names="partner partner_id balance")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==================== ========= ===============
 Partner              ID        Balance
-------------------- --------- ---------------
 AS Express Post      181       617,70
 AS Matsalu Veevärk   182       2 131,20
 Eesti Energia AS     183       75 828,90
 **Total (3 rows)**   **546**   **78 577,80**
==================== ========= ===============
<BLANKLINE>

Partner 181 from above list has many open purchases invoices,
totalling to 617,70:

>>> obj = contacts.Partner.objects.get(pk=181)
>>> ses.show(ledger.DebtsByPartner, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
===================== ============= ======= =====================
 Due date              Balance       Debts   Payments
--------------------- ------------- ------- ---------------------
 02/01/2016            -40,00                `PRC 1 <Detail>`__
 07/05/2016            -41,30                `PRC 6 <Detail>`__
 15/03/2016            -40,60                `PRC 11 <Detail>`__
 03/05/2016            -42,50                `PRC 16 <Detail>`__
 07/07/2016            -41,10                `PRC 21 <Detail>`__
 13/06/2016            -40,00                `PRC 26 <Detail>`__
 31/07/2016            -41,30                `PRC 31 <Detail>`__
 01/09/2016            -40,60                `PRC 36 <Detail>`__
 07/09/2016            -42,50                `PRC 41 <Detail>`__
 03/01/2017            -41,10                `PRC 46 <Detail>`__
 13/11/2016            -40,00                `PRC 51 <Detail>`__
 07/01/2017            -41,30                `PRC 56 <Detail>`__
 07/03/2017            -41,00                `PRC 61 <Detail>`__
 11/02/2017            -42,90                `PRC 66 <Detail>`__
 31/03/2017            -41,50                `PRC 71 <Detail>`__
 **Total (15 rows)**   **-617,70**
===================== ============= ======= =====================
<BLANKLINE>

Note that the numbers are negative in above table. A purchase invoice
is a *credit* received from the provider, and we asked a list of
*debts* by partner.


Fiscal years
============

Each ledger movement happens in a given **fiscal year**.  Lino has a
table with **fiscal years**.

In a default configuration there is one fiscal year for each calendar
year between :attr:`start_year
<lino_xl.lib.ledger.Plugin.start_year>` and ":func:`today
<lino.core.site.Site.today>` plus 5 years".

>>> dd.plugins.ledger.start_year
2016

>>> dd.today()
datetime.date(2017, 3, 12)

>>> dd.today().year + 5
2022

>>> rt.show(ledger.FiscalYears)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= ====== ======
 value   name   text
------- ------ ------
 16             2016
 17             2017
 18             2018
 19             2019
 20             2020
 21             2021
 22             2022
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
 2016-01     01/01/2016   31/01/2016   2016          Open
 2016-02     01/02/2016   29/02/2016   2016          Open
 2016-03     01/03/2016   31/03/2016   2016          Open
 2016-04     01/04/2016   30/04/2016   2016          Open
 2016-05     01/05/2016   31/05/2016   2016          Open
 2016-06     01/06/2016   30/06/2016   2016          Open
 2016-07     01/07/2016   31/07/2016   2016          Open
 2016-08     01/08/2016   31/08/2016   2016          Open
 2016-09     01/09/2016   30/09/2016   2016          Open
 2016-10     01/10/2016   31/10/2016   2016          Open
 2016-11     01/11/2016   30/11/2016   2016          Open
 2016-12     01/12/2016   31/12/2016   2016          Open
 2017-01     01/01/2017   31/01/2017   2017          Open
 2017-02     01/02/2017   28/02/2017   2017          Open
 2017-03     01/03/2017   31/03/2017   2017          Open
=========== ============ ============ ============= ======= ========
<BLANKLINE>

The *reference* of a new accounting period is computed by applying the
voucher's entry date to the template defined in the
:attr:`date_to_period_tpl
<lino_xl.lib.ledger.models.AccountingPeriod.get_for_date>` setting.  
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
  

Payment terms
=============

>>> rt.show('ledger.PaymentTerms')
==================== ======================================= ======================================= ======== ========= ==============
 Reference            Designation                             Designation (en)                        Months   Days      End of month
-------------------- --------------------------------------- --------------------------------------- -------- --------- --------------
 07                   Payment seven days after invoice date   Payment seven days after invoice date   0        7         No
 10                   Payment ten days after invoice date     Payment ten days after invoice date     0        10        No
 30                   Payment 30 days after invoice date      Payment 30 days after invoice date      0        30        No
 60                   Payment 60 days after invoice date      Payment 60 days after invoice date      0        60        No
 90                   Payment 90 days after invoice date      Payment 90 days after invoice date      0        90        No
 EOM                  Payment end of month                    Payment end of month                    0        0         Yes
 P30                  Prepayment 30%                          Prepayment 30%                          0        30        No
 PIA                  Payment in advance                      Payment in advance                      0        0         No
 **Total (8 rows)**                                                                                   **0**    **227**
==================== ======================================= ======================================= ======== ========= ==============
<BLANKLINE>


