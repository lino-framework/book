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
+-------+------------------------------------------------------------+
| value | Description                                                |
+=======+============================================================+
| 1     | VAT rule 1:                                                |
|       | if (Purchases, National, Normal VAT rate) then             |
|       | apply 0.20 %                                               |
|       | and book to VAT deductible                                 |
+-------+------------------------------------------------------------+
| 2     | VAT rule 2:                                                |
|       | if (Purchases, National, Reduced VAT rate) then            |
|       | apply 0.09 %                                               |
|       | and book to VAT deductible                                 |
+-------+------------------------------------------------------------+
| 3     | VAT rule 3:                                                |
|       | if (Purchases, Intra-community, EU, Normal VAT rate) then  |
|       | apply 0.20 %                                               |
|       | and book to VAT deductible                                 |
|       | (return to VAT returnable)                                 |
+-------+------------------------------------------------------------+
| 4     | VAT rule 4:                                                |
|       | if (Purchases, Intra-community, EU, Reduced VAT rate) then |
|       | apply 0.09 %                                               |
|       | and book to VAT deductible                                 |
|       | (return to VAT returnable)                                 |
+-------+------------------------------------------------------------+
| 5     | VAT rule 5:                                                |
|       | if (Sales, Intra-community, EU, Normal VAT rate) then      |
|       | apply 0.00 %                                               |
|       | and book to None                                           |
+-------+------------------------------------------------------------+
| 6     | VAT rule 6:                                                |
|       | if (Sales, Intra-community, EU, Reduced VAT rate) then     |
|       | apply 0.00 %                                               |
|       | and book to None                                           |
+-------+------------------------------------------------------------+
| 7     | VAT rule 7:                                                |
|       | if (Sales, Reduced VAT rate) then                          |
|       | apply 0.09 %                                               |
|       | and book to VAT due                                        |
+-------+------------------------------------------------------------+
| 8     | VAT rule 8:                                                |
|       | if (Sales, Normal VAT rate) then                           |
|       | apply 0.20 %                                               |
|       | and book to VAT due                                        |
+-------+------------------------------------------------------------+
| 9     | VAT rule 9:                                                |
|       | apply 0 %                                                  |
|       | and book to None                                           |
+-------+------------------------------------------------------------+
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

>>> list(rt.models.vat.get_vat_regime_choices(ee))
[<VatRegimes.normal:10>, <VatRegimes.subject:20>, <VatRegimes.cocontractor:25>, <VatRegimes.exempt:60>]

>>> nl = countries.Country(isocode='NL')
>>> vat.VatAreas.get_for_country(nl)
<VatAreas.eu:20>
>>> list(rt.models.vat.get_vat_regime_choices(nl))
[<VatRegimes.normal:10>, <VatRegimes.intracom:30>, <VatRegimes.exempt:60>]

>>> us = countries.Country(isocode='US')
>>> vat.VatAreas.get_for_country(countries.Country(isocode='US'))
<VatAreas.international:30>
>>> list(rt.models.vat.get_vat_regime_choices(us))
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
 *PRC 4/2015*          Bäckerei Mießen   BE7336627818     Intra-community   1 199,90                1 199,90
 *PRC 4/2016*          Bäckerei Mießen   BE7336627818     Intra-community   1 213,00                1 213,00
 *PRC 4/2017*          Bäckerei Mießen   BE7336627818     Intra-community   1 226,40                1 226,40
 *PRC 7/2015*          Donderweer BV     NL211892074B01   Intra-community   199,90                  199,90
 *PRC 7/2016*          Donderweer BV     NL211892074B01   Intra-community   203,00                  203,00
 *PRC 7/2017*          Donderweer BV     NL211892074B01   Intra-community   206,40                  206,40
 *PRC 11/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 200,50                1 200,50
 *PRC 11/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 213,20                1 213,20
 *PRC 11/2017*         Bäckerei Mießen   BE7336627818     Intra-community   1 223,90                1 223,90
 *PRC 14/2015*         Donderweer BV     NL211892074B01   Intra-community   200,50                  200,50
 *PRC 14/2016*         Donderweer BV     NL211892074B01   Intra-community   203,20                  203,20
 *PRC 14/2017*         Donderweer BV     NL211892074B01   Intra-community   203,90                  203,90
 *PRC 18/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 201,00                1 201,00
 *PRC 18/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 214,40                1 214,40
 *PRC 18/2017*         Bäckerei Mießen   BE7336627818     Intra-community   1 224,50                1 224,50
 *PRC 21/2015*         Donderweer BV     NL211892074B01   Intra-community   201,00                  201,00
 *PRC 21/2016*         Donderweer BV     NL211892074B01   Intra-community   204,40                  204,40
 *PRC 21/2017*         Donderweer BV     NL211892074B01   Intra-community   204,50                  204,50
 *PRC 25/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 201,20                1 201,20
 *PRC 25/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 211,90                1 211,90
 *PRC 28/2015*         Donderweer BV     NL211892074B01   Intra-community   201,20                  201,20
 *PRC 28/2016*         Donderweer BV     NL211892074B01   Intra-community   201,90                  201,90
 *PRC 32/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 202,40                1 202,40
 *PRC 32/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 212,50                1 212,50
 *PRC 35/2015*         Donderweer BV     NL211892074B01   Intra-community   202,40                  202,40
 *PRC 35/2016*         Donderweer BV     NL211892074B01   Intra-community   202,50                  202,50
 *PRC 39/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 199,90                1 199,90
 *PRC 39/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 213,00                1 213,00
 *PRC 42/2015*         Donderweer BV     NL211892074B01   Intra-community   199,90                  199,90
 *PRC 42/2016*         Donderweer BV     NL211892074B01   Intra-community   203,00                  203,00
 *PRC 46/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 200,50                1 200,50
 *PRC 46/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 213,20                1 213,20
 *PRC 49/2015*         Donderweer BV     NL211892074B01   Intra-community   200,50                  200,50
 *PRC 49/2016*         Donderweer BV     NL211892074B01   Intra-community   203,20                  203,20
 *PRC 53/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 201,00                1 201,00
 *PRC 53/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 214,40                1 214,40
 *PRC 56/2015*         Donderweer BV     NL211892074B01   Intra-community   201,00                  201,00
 *PRC 56/2016*         Donderweer BV     NL211892074B01   Intra-community   204,40                  204,40
 *PRC 60/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 201,20                1 201,20
 *PRC 60/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 211,90                1 211,90
 *PRC 63/2015*         Donderweer BV     NL211892074B01   Intra-community   201,20                  201,20
 *PRC 63/2016*         Donderweer BV     NL211892074B01   Intra-community   201,90                  201,90
 *PRC 67/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 202,40                1 202,40
 *PRC 67/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 212,50                1 212,50
 *PRC 70/2015*         Donderweer BV     NL211892074B01   Intra-community   202,40                  202,40
 *PRC 70/2016*         Donderweer BV     NL211892074B01   Intra-community   202,50                  202,50
 *PRC 74/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 199,90                1 199,90
 *PRC 74/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 213,00                1 213,00
 *PRC 77/2015*         Donderweer BV     NL211892074B01   Intra-community   199,90                  199,90
 *PRC 77/2016*         Donderweer BV     NL211892074B01   Intra-community   203,00                  203,00
 *PRC 81/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 200,50                1 200,50
 *PRC 81/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 213,20                1 213,20
 *PRC 84/2015*         Donderweer BV     NL211892074B01   Intra-community   200,50                  200,50
 *PRC 84/2016*         Donderweer BV     NL211892074B01   Intra-community   203,20                  203,20
 **Total (54 rows)**                                                        **38 102,80**           **38 102,80**
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
================================ ============= ================= ================= ===== ==============
 Account                          Description   VAT class         Total excl. VAT   VAT   Total to pay
-------------------------------- ------------- ----------------- ----------------- ----- --------------
 (6020) Purchase of investments                 Normal VAT rate   204,50                  204,50
 **Total (1 rows)**                                               **204,50**              **204,50**
================================ ============= ================= ================= ===== ==============
<BLANKLINE>


>>> rt.show('ledger.MovementsByVoucher', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
================================ =============== ============ ============ ================= =========
 Account                          Partner         Debit        Credit       Match             Cleared
-------------------------------- --------------- ------------ ------------ ----------------- ---------
 (4400) Suppliers                 Donderweer BV                204,50       **PRC 21/2017**   No
 (4511) VAT returnable                            40,90                                       Yes
 (4512) VAT deductible                                         40,90                          Yes
 (6020) Purchase of investments                   204,50                                      Yes
                                                  **245,40**   **245,40**
================================ =============== ============ ============ ================= =========
<BLANKLINE>

>>> print(invoice.total_base)
204.50
>>> print(invoice.total_vat)
0.00
>>> print(invoice.total_incl)
204.50

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
