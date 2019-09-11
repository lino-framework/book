.. doctest docs/specs/eevat.rst
.. _xl.eevat:

=====================================
``eevat`` : Estonian VAT declarations
=====================================

.. currentmodule:: lino_xl.lib.eevat

The :mod:`lino_xl.lib.eevat` plugin adds functionality for handling **Estonian
VAT declarations**.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.cosi_ee.settings.doctests')
>>> from lino.api.doctest import *


Dependencies
============

Installing this plugin will automatically install :mod:`lino_xl.lib.vat`.

>>> dd.plugins.eevat.needs_plugins
['lino_xl.lib.vat']

VAT regimes
===========


>>> rt.show(vat.VatRegimes, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
======= ============== ================= =============== ============== ==========
 value   name           text              VAT area        Needs VAT id   item VAT
------- -------------- ----------------- --------------- -------------- ----------
 10      normal         Private person                    No             Yes
 20      subject        Subject to VAT    National        Yes            Yes
 25      cocontractor   Co-contractor     National        Yes            Yes
 30      intracom       Intra-community   EU              Yes            Yes
 50      outside        Outside EU        International   No             Yes
 60      exempt         Exempt                            No             No
======= ============== ================= =============== ============== ==========
<BLANKLINE>

VAT rules
=========

>>> rt.show(vat.VatRules, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
+-------+-------------------------------------------------------+
| value | Description                                           |
+=======+=======================================================+
| 1     | Rate 0.20                                             |
|       | When Purchases, National, Normal VAT rate             |
|       | Book to VAT deductible                                |
+-------+-------------------------------------------------------+
| 2     | Rate 0.09                                             |
|       | When Purchases, National, Reduced VAT rate            |
|       | Book to VAT deductible                                |
+-------+-------------------------------------------------------+
| 3     | Rate 0.20                                             |
|       | When Purchases, Intra-community, EU, Normal VAT rate  |
|       | Book to VAT deductible                                |
|       | Returnable to VAT returnable                          |
+-------+-------------------------------------------------------+
| 4     | Rate 0.09                                             |
|       | When Purchases, Intra-community, EU, Reduced VAT rate |
|       | Book to VAT deductible                                |
|       | Returnable to VAT returnable                          |
+-------+-------------------------------------------------------+
| 5     | Rate 0.00                                             |
|       | When Sales, Intra-community, EU, Normal VAT rate      |
|       | Book to None                                          |
+-------+-------------------------------------------------------+
| 6     | Rate 0.00                                             |
|       | When Sales, Intra-community, EU, Reduced VAT rate     |
|       | Book to None                                          |
+-------+-------------------------------------------------------+
| 7     | Rate 0.09                                             |
|       | When Sales, Reduced VAT rate                          |
|       | Book to VAT due                                       |
+-------+-------------------------------------------------------+
| 8     | Rate 0.20                                             |
|       | When Sales, Normal VAT rate                           |
|       | Book to VAT due                                       |
+-------+-------------------------------------------------------+
| 9     | Rate 0                                                |
|       | Book to None                                          |
+-------+-------------------------------------------------------+
<BLANKLINE>


For example here is the rule that applies when selling a normal product to a
private person:

>>> rule = vat.VatRules.get_vat_rule(vat.VatAreas.national, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.normal)

The Estonian VAT rate is 20%:

>>> rule.rate
Decimal('0.20')
>>> rule.vat_account
<CommonAccounts.vat_due:4510>
>>> rule.vat_account.get_object()
Account #6 ('(4510) VAT due')

This VAT is not returnable:

>>> rule.vat_returnable
False
>>> rule.vat_returnable_account

>>> vat.VatRules.get_vat_rule(vat.VatAreas.international, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.normal).rate
Decimal('0.20')

Note that returnable VAT is used only in purchase invoices, not in sales.  In a
sales invoice to an intracom partner, there is simply no VAT to be generated.
IOW even for services and good for which national customers must pay VAT
(because their VAT class is normal or reduced but not exempt), the VAT rule
specifies a rate of 0.


Available VAT regimes
=====================

For example, when using :mod:`eevat <lino_xl.lib.eevat>` as declaration plugin,
a partner located in Estonia will be in the "national" area,
a partner located in the Netherlands will be in the "EU" area,
and a partner located in the United States will be in the "International" area.


.. >>> print(dd.plugins.countries.country_code)
   EE

>>> ee = countries.Country(isocode='EE')
>>> vat.VatAreas.get_for_country(ee)
<VatAreas.national:10>
>>> list(rt.models.vat.get_vat_regime_choices(ee, None))
[<VatRegimes.normal:10>, <VatRegimes.exempt:60>]

>>> list(rt.models.vat.get_vat_regime_choices(ee, "EE123456789"))
[<VatRegimes.normal:10>, <VatRegimes.subject:20>, <VatRegimes.cocontractor:25>, <VatRegimes.exempt:60>]

>>> nl = countries.Country(isocode='NL')
>>> vat.VatAreas.get_for_country(nl)
<VatAreas.eu:20>
>>> list(rt.models.vat.get_vat_regime_choices(nl, None))
[<VatRegimes.normal:10>, <VatRegimes.exempt:60>]
>>> list(rt.models.vat.get_vat_regime_choices(nl, "NL123456789"))
[<VatRegimes.normal:10>, <VatRegimes.intracom:30>, <VatRegimes.exempt:60>]

>>> us = countries.Country(isocode='US')
>>> vat.VatAreas.get_for_country(countries.Country(isocode='US'))
<VatAreas.international:30>
>>> list(rt.models.vat.get_vat_regime_choices(us, None))
[<VatRegimes.normal:10>, <VatRegimes.outside:50>, <VatRegimes.exempt:60>]


Intracom
========


>>> rt.show(vat.IntracomSales)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +ELLIPSIS
==================== =========================== ================ ================= ================= ===== ===============
 Invoice              Partner                     VAT id           VAT regime        Total excl. VAT   VAT   Total to pay
-------------------- --------------------------- ---------------- ----------------- ----------------- ----- ---------------
 *SLS 4/2015*         Bäckerei Mießen             BE7336627818     Intra-community   280,00                  280,00
 *SLS 7/2015*         Donderweer BV               NL211892074B01   Intra-community   1 199,85                1 199,85
 *SLS 10/2015*        Bernd Brechts Bücherladen   DE529665130      Intra-community   1 599,92                1 599,92
 *SLS 13/2015*        Auto École Verte            FR74229232671    Intra-community   525,00                  525,00
 *SLS 47/2016*        Bäckerei Mießen             BE7336627818     Intra-community   600,00                  600,00
 *SLS 50/2016*        Donderweer BV               NL211892074B01   Intra-community   465,96                  465,96
 *SLS 53/2016*        Bernd Brechts Bücherladen   DE529665130      Intra-community   2 039,82                2 039,82
 *SLS 57/2016*        Auto École Verte            FR74229232671    Intra-community   3 319,78                3 319,78
 **Total (8 rows)**                                                                  **10 030,33**           **10 030,33**
==================== =========================== ================ ================= ================= ===== ===============
<BLANKLINE>


>>> rt.show(vat.IntracomPurchases)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ================= ================ ================= ================= ===== ===============
 Invoice               Partner           VAT id           VAT regime        Total excl. VAT   VAT   Total to pay
--------------------- ----------------- ---------------- ----------------- ----------------- ----- ---------------
 *PRC 4/2015*          Bäckerei Mießen   BE7336627818     Intra-community   999,92                  999,92
 *PRC 4/2016*          Bäckerei Mießen   BE7336627818     Intra-community   1 010,83                1 010,83
 *PRC 4/2017*          Bäckerei Mießen   BE7336627818     Intra-community   1 022,00                1 022,00
 *PRC 7/2015*          Donderweer BV     NL211892074B01   Intra-community   166,58                  166,58
 *PRC 7/2016*          Donderweer BV     NL211892074B01   Intra-community   169,17                  169,17
 *PRC 7/2017*          Donderweer BV     NL211892074B01   Intra-community   172,00                  172,00
 *PRC 11/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,42                1 000,42
 *PRC 11/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 011,00                1 011,00
 *PRC 11/2017*         Bäckerei Mießen   BE7336627818     Intra-community   1 019,92                1 019,92
 *PRC 14/2015*         Donderweer BV     NL211892074B01   Intra-community   167,08                  167,08
 *PRC 14/2016*         Donderweer BV     NL211892074B01   Intra-community   169,33                  169,33
 *PRC 14/2017*         Donderweer BV     NL211892074B01   Intra-community   169,92                  169,92
 *PRC 18/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,83                1 000,83
 *PRC 18/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 012,00                1 012,00
 *PRC 18/2017*         Bäckerei Mießen   BE7336627818     Intra-community   1 020,42                1 020,42
 *PRC 21/2015*         Donderweer BV     NL211892074B01   Intra-community   167,50                  167,50
 *PRC 21/2016*         Donderweer BV     NL211892074B01   Intra-community   170,33                  170,33
 *PRC 21/2017*         Donderweer BV     NL211892074B01   Intra-community   170,42                  170,42
 *PRC 25/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 001,00                1 001,00
 *PRC 25/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 009,92                1 009,92
 *PRC 28/2015*         Donderweer BV     NL211892074B01   Intra-community   167,67                  167,67
 *PRC 28/2016*         Donderweer BV     NL211892074B01   Intra-community   168,25                  168,25
 *PRC 32/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 002,00                1 002,00
 *PRC 32/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,42                1 010,42
 *PRC 35/2015*         Donderweer BV     NL211892074B01   Intra-community   168,67                  168,67
 *PRC 35/2016*         Donderweer BV     NL211892074B01   Intra-community   168,75                  168,75
 *PRC 39/2015*         Bäckerei Mießen   BE7336627818     Intra-community   999,92                  999,92
 *PRC 39/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,83                1 010,83
 *PRC 42/2015*         Donderweer BV     NL211892074B01   Intra-community   166,58                  166,58
 *PRC 42/2016*         Donderweer BV     NL211892074B01   Intra-community   169,17                  169,17
 *PRC 46/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,42                1 000,42
 *PRC 46/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 011,00                1 011,00
 *PRC 49/2015*         Donderweer BV     NL211892074B01   Intra-community   167,08                  167,08
 *PRC 49/2016*         Donderweer BV     NL211892074B01   Intra-community   169,33                  169,33
 *PRC 53/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,83                1 000,83
 *PRC 53/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 012,00                1 012,00
 *PRC 56/2015*         Donderweer BV     NL211892074B01   Intra-community   167,50                  167,50
 *PRC 56/2016*         Donderweer BV     NL211892074B01   Intra-community   170,33                  170,33
 *PRC 60/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 001,00                1 001,00
 *PRC 60/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 009,92                1 009,92
 *PRC 63/2015*         Donderweer BV     NL211892074B01   Intra-community   167,67                  167,67
 *PRC 63/2016*         Donderweer BV     NL211892074B01   Intra-community   168,25                  168,25
 *PRC 67/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 002,00                1 002,00
 *PRC 67/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,42                1 010,42
 *PRC 70/2015*         Donderweer BV     NL211892074B01   Intra-community   168,67                  168,67
 *PRC 70/2016*         Donderweer BV     NL211892074B01   Intra-community   168,75                  168,75
 *PRC 74/2015*         Bäckerei Mießen   BE7336627818     Intra-community   999,92                  999,92
 *PRC 74/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,83                1 010,83
 *PRC 77/2015*         Donderweer BV     NL211892074B01   Intra-community   166,58                  166,58
 *PRC 77/2016*         Donderweer BV     NL211892074B01   Intra-community   169,17                  169,17
 *PRC 81/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,42                1 000,42
 *PRC 81/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 011,00                1 011,00
 *PRC 84/2015*         Donderweer BV     NL211892074B01   Intra-community   167,08                  167,08
 *PRC 84/2016*         Donderweer BV     NL211892074B01   Intra-community   169,33                  169,33
 **Total (54 rows)**                                                        **31 752,35**           **31 752,35**
===================== ================= ================ ================= ================= ===== ===============
<BLANKLINE>



External references
===================

- `165-625-directives-2016.pdf
  <https://finances.belgium.be/sites/default/files/downloads/165-625-directives-2016.pdf>`__

- `finances.belgium.be
  <https://finances.belgium.be/fr/entreprises/tva/declaration/declaration_periodique>`__


Other languages
===============


>>> rt.show(vat.VatRegimes, language="de")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
====== ============== ======================= =============== ============== ==========
 Wert   name           Text                    VAT area        Needs VAT id   item VAT
------ -------------- ----------------------- --------------- -------------- ----------
 10     normal         Privatperson                            Nein           Ja
 20     subject        MwSt.-pflichtig         National        Ja             Ja
 25     cocontractor   Vertragspartner         National        Ja             Ja
 30     intracom       Innergemeinschaftlich   EU              Ja             Ja
 50     outside        Außerhalb EU            International   Nein           Ja
 60     exempt         Befreit von MwSt.                       Nein           Nein
====== ============== ======================= =============== ============== ==========
<BLANKLINE>


>>> rt.show(vat.VatClasses, language="de")
====== ========= ====================
 Wert   name      Text
------ --------- --------------------
 0      exempt    Ohne MWSt
 1      reduced   Reduced VAT rate
 2      normal    Normaler MwSt-Satz
====== ========= ====================
<BLANKLINE>

>>> rt.show(vat.VatAreas, language="de")
====== =============== ===============
 Wert   name            Text
------ --------------- ---------------
 10     national        National
 20     eu              EU
 30     international   International
====== =============== ===============
<BLANKLINE>


Returnable VAT
==============

A purchases invoice with :term:`Returnable VAT`:

>>> invoice = rt.models.vat.VatAccountInvoice.objects.get(id=189)
>>> print(invoice)
PRC 21/2017
>>> rt.show('vat.ItemsByInvoice', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
================================ ============= ================= ================= =========== ==============
 Account                          Description   VAT class         Total excl. VAT   VAT         Total to pay
-------------------------------- ------------- ----------------- ----------------- ----------- --------------
 (6020) Purchase of investments                 Normal VAT rate   170,42            34,08       204,50
 **Total (1 rows)**                                               **170,42**        **34,08**   **204,50**
================================ ============= ================= ================= =========== ==============
<BLANKLINE>

>>> rt.show('ledger.MovementsByVoucher', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
================================ =============== ============ ============ ================= =========
 Account                          Partner         Debit        Credit       Match             Cleared
-------------------------------- --------------- ------------ ------------ ----------------- ---------
 (4400) Suppliers                 Donderweer BV                170,42       **PRC 21/2017**   No
 (4511) VAT returnable                            34,08                                       Yes
 (4512) VAT deductible                                         34,08                          Yes
 (6020) Purchase of investments                   170,42                                      Yes
                                                  **204,50**   **204,50**
================================ =============== ============ ============ ================= =========
<BLANKLINE>

>>> print(invoice.total_base)
170.42
>>> print(invoice.total_vat)
0.00
>>> print(invoice.total_incl)
170.42

Note that intracom sales invoices have no :term:`returnable VAT` because they
don't have any VAT at all:

>>> invoice = rt.models.sales.VatProductInvoice.objects.get(id=199)
>>> invoice.vat_regime
<VatRegimes.intracom:30>

>>> rt.show('ledger.MovementsByVoucher', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
================== =========================== ============== ============== ================= =========
 Account            Partner                     Debit          Credit         Match             Cleared
------------------ --------------------------- -------------- -------------- ----------------- ---------
 (4000) Customers   Bernd Brechts Bücherladen   1 599,92                      **SLS 10/2015**   No
 (7000) Sales                                                  1 599,92                         Yes
                                                **1 599,92**   **1 599,92**
================== =========================== ============== ============== ================= =========
<BLANKLINE>

>>> print(invoice.total_base)
1599.92
>>> print(invoice.total_vat)
0.00
>>> print(invoice.total_incl)
1599.92
