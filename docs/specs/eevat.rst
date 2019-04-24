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
| 5     | Rate 0.20                                             |
|       | When Sales, Intra-community, EU, Normal VAT rate      |
|       | Book to VAT due                                       |
|       | Returnable to VAT returnable                          |
+-------+-------------------------------------------------------+
| 6     | Rate 0.09                                             |
|       | When Sales, Intra-community, EU, Reduced VAT rate     |
|       | Book to VAT due                                       |
|       | Returnable to VAT returnable                          |
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
==================== =========================== ================ ================= ================= ============== =================
 Invoice              Partner                     VAT id           VAT regime        Total excl. VAT   VAT            Total incl. VAT
-------------------- --------------------------- ---------------- ----------------- ----------------- -------------- -----------------
 *SLS 4/2015*         Bäckerei Mießen             BE7336627818     Intra-community   233,33            46,67          280,00
 *SLS 7/2015*         Donderweer BV               NL211892074B01   Intra-community   999,88            199,97         1 199,85
 *SLS 10/2015*        Bernd Brechts Bücherladen   DE529665130      Intra-community   1 333,27          266,65         1 599,92
 *SLS 13/2015*        Auto École Verte            FR74229232671    Intra-community   437,50            87,50          525,00
 *SLS 47/2016*        Bäckerei Mießen             BE7336627818     Intra-community   500,00            100,00         600,00
 *SLS 50/2016*        Donderweer BV               NL211892074B01   Intra-community   388,30            77,66          465,96
 *SLS 53/2016*        Bernd Brechts Bücherladen   DE529665130      Intra-community   1 699,85          339,97         2 039,82
 *SLS 57/2016*        Auto École Verte            FR74229232671    Intra-community   2 766,48          553,30         3 319,78
 **Total (8 rows)**                                                                  **8 358,61**      **1 671,72**   **10 030,33**
==================== =========================== ================ ================= ================= ============== =================
<BLANKLINE>


TODO: the following table should not be empty. some bug in the demo fixtures?

>>> rt.show(vat.IntracomPurchases)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ================= ================ ================= ================= ============== =================
 Invoice               Partner           VAT id           VAT regime        Total excl. VAT   VAT            Total incl. VAT
--------------------- ----------------- ---------------- ----------------- ----------------- -------------- -----------------
 *PRC 4/2015*          Bäckerei Mießen   BE7336627818     Intra-community   999,92            199,98         1 199,90
 *PRC 4/2016*          Bäckerei Mießen   BE7336627818     Intra-community   1 010,83          202,17         1 213,00
 *PRC 4/2017*          Bäckerei Mießen   BE7336627818     Intra-community   1 022,00          204,40         1 226,40
 *PRC 7/2015*          Donderweer BV     NL211892074B01   Intra-community   166,58            33,32          199,90
 *PRC 7/2016*          Donderweer BV     NL211892074B01   Intra-community   169,17            33,83          203,00
 *PRC 7/2017*          Donderweer BV     NL211892074B01   Intra-community   172,00            34,40          206,40
 *PRC 11/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,42          200,08         1 200,50
 *PRC 11/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 011,00          202,20         1 213,20
 *PRC 11/2017*         Bäckerei Mießen   BE7336627818     Intra-community   1 019,92          203,98         1 223,90
 *PRC 14/2015*         Donderweer BV     NL211892074B01   Intra-community   167,08            33,42          200,50
 *PRC 14/2016*         Donderweer BV     NL211892074B01   Intra-community   169,33            33,87          203,20
 *PRC 14/2017*         Donderweer BV     NL211892074B01   Intra-community   169,92            33,98          203,90
 *PRC 18/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,83          200,17         1 201,00
 *PRC 18/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 012,00          202,40         1 214,40
 *PRC 18/2017*         Bäckerei Mießen   BE7336627818     Intra-community   1 020,42          204,08         1 224,50
 *PRC 21/2015*         Donderweer BV     NL211892074B01   Intra-community   167,50            33,50          201,00
 *PRC 21/2016*         Donderweer BV     NL211892074B01   Intra-community   170,33            34,07          204,40
 *PRC 21/2017*         Donderweer BV     NL211892074B01   Intra-community   170,42            34,08          204,50
 *PRC 25/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 001,00          200,20         1 201,20
 *PRC 25/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 009,92          201,98         1 211,90
 *PRC 28/2015*         Donderweer BV     NL211892074B01   Intra-community   167,67            33,53          201,20
 *PRC 28/2016*         Donderweer BV     NL211892074B01   Intra-community   168,25            33,65          201,90
 *PRC 32/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 002,00          200,40         1 202,40
 *PRC 32/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,42          202,08         1 212,50
 *PRC 35/2015*         Donderweer BV     NL211892074B01   Intra-community   168,67            33,73          202,40
 *PRC 35/2016*         Donderweer BV     NL211892074B01   Intra-community   168,75            33,75          202,50
 *PRC 39/2015*         Bäckerei Mießen   BE7336627818     Intra-community   999,92            199,98         1 199,90
 *PRC 39/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,83          202,17         1 213,00
 *PRC 42/2015*         Donderweer BV     NL211892074B01   Intra-community   166,58            33,32          199,90
 *PRC 42/2016*         Donderweer BV     NL211892074B01   Intra-community   169,17            33,83          203,00
 *PRC 46/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,42          200,08         1 200,50
 *PRC 46/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 011,00          202,20         1 213,20
 *PRC 49/2015*         Donderweer BV     NL211892074B01   Intra-community   167,08            33,42          200,50
 *PRC 49/2016*         Donderweer BV     NL211892074B01   Intra-community   169,33            33,87          203,20
 *PRC 53/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,83          200,17         1 201,00
 *PRC 53/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 012,00          202,40         1 214,40
 *PRC 56/2015*         Donderweer BV     NL211892074B01   Intra-community   167,50            33,50          201,00
 *PRC 56/2016*         Donderweer BV     NL211892074B01   Intra-community   170,33            34,07          204,40
 *PRC 60/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 001,00          200,20         1 201,20
 *PRC 60/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 009,92          201,98         1 211,90
 *PRC 63/2015*         Donderweer BV     NL211892074B01   Intra-community   167,67            33,53          201,20
 *PRC 63/2016*         Donderweer BV     NL211892074B01   Intra-community   168,25            33,65          201,90
 *PRC 67/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 002,00          200,40         1 202,40
 *PRC 67/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,42          202,08         1 212,50
 *PRC 70/2015*         Donderweer BV     NL211892074B01   Intra-community   168,67            33,73          202,40
 *PRC 70/2016*         Donderweer BV     NL211892074B01   Intra-community   168,75            33,75          202,50
 *PRC 74/2015*         Bäckerei Mießen   BE7336627818     Intra-community   999,92            199,98         1 199,90
 *PRC 74/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 010,83          202,17         1 213,00
 *PRC 77/2015*         Donderweer BV     NL211892074B01   Intra-community   166,58            33,32          199,90
 *PRC 77/2016*         Donderweer BV     NL211892074B01   Intra-community   169,17            33,83          203,00
 *PRC 81/2015*         Bäckerei Mießen   BE7336627818     Intra-community   1 000,42          200,08         1 200,50
 *PRC 81/2016*         Bäckerei Mießen   BE7336627818     Intra-community   1 011,00          202,20         1 213,20
 *PRC 84/2015*         Donderweer BV     NL211892074B01   Intra-community   167,08            33,42          200,50
 *PRC 84/2016*         Donderweer BV     NL211892074B01   Intra-community   169,33            33,87          203,20
 **Total (54 rows)**                                                        **31 752,35**     **6 350,45**   **38 102,80**
===================== ================= ================ ================= ================= ============== =================
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


