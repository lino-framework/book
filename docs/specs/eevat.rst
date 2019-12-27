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
 40      tax_free       Tax-free                          No             Yes
 50      outside        Outside EU        International   No             Yes
 60      exempt         Exempt                            No             No
======= ============== ================= =============== ============== ==========
<BLANKLINE>


VAT rules
=========

>>> rt.show(vat.VatRules, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
+-------+-------------------------------------------------------------------------+
| value | Description                                                             |
+=======+=========================================================================+
| 1     | VAT rule 1:                                                             |
|       | if (Exempt) then                                                        |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 2     | VAT rule 2:                                                             |
|       | if (Purchases, Intra-community, EU, Services) then                      |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 3     | VAT rule 3:                                                             |
|       | if (Sales, Intra-community, EU, Services) then                          |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 4     | VAT rule 4:                                                             |
|       | if (Purchases, Co-contractor, National, Services) then                  |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 5     | VAT rule 5:                                                             |
|       | if (Sales, Co-contractor, National, Services) then                      |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 6     | VAT rule 6:                                                             |
|       | if (Purchases, Intra-community, EU, Goods at normal VAT rate) then      |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 7     | VAT rule 7:                                                             |
|       | if (Sales, Intra-community, EU, Goods at normal VAT rate) then          |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 8     | VAT rule 8:                                                             |
|       | if (Purchases, Co-contractor, National, Goods at normal VAT rate) then  |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 9     | VAT rule 9:                                                             |
|       | if (Sales, Co-contractor, National, Goods at normal VAT rate) then      |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 10    | VAT rule 10:                                                            |
|       | if (Purchases, Intra-community, EU, Real estate) then                   |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 11    | VAT rule 11:                                                            |
|       | if (Sales, Intra-community, EU, Real estate) then                       |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 12    | VAT rule 12:                                                            |
|       | if (Purchases, Co-contractor, National, Real estate) then               |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 13    | VAT rule 13:                                                            |
|       | if (Sales, Co-contractor, National, Real estate) then                   |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 14    | VAT rule 14:                                                            |
|       | if (Purchases, Intra-community, EU, Vehicles) then                      |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 15    | VAT rule 15:                                                            |
|       | if (Sales, Intra-community, EU, Vehicles) then                          |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 16    | VAT rule 16:                                                            |
|       | if (Purchases, Co-contractor, National, Vehicles) then                  |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 17    | VAT rule 17:                                                            |
|       | if (Sales, Co-contractor, National, Vehicles) then                      |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 18    | VAT rule 18:                                                            |
|       | if (Purchases, Intra-community, EU, Goods at reduced VAT rate) then     |
|       | apply 0.09 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 19    | VAT rule 19:                                                            |
|       | if (Sales, Intra-community, EU, Goods at reduced VAT rate) then         |
|       | apply 0.09 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 20    | VAT rule 20:                                                            |
|       | if (Purchases, Co-contractor, National, Goods at reduced VAT rate) then |
|       | apply 0.09 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 21    | VAT rule 21:                                                            |
|       | if (Sales, Co-contractor, National, Goods at reduced VAT rate) then     |
|       | apply 0.09 %                                                            |
|       | and book to VAT due                                                     |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 22    | VAT rule 22:                                                            |
|       | if (Purchases, National, Services) then                                 |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 23    | VAT rule 23:                                                            |
|       | if (Sales, Services) then                                               |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 24    | VAT rule 24:                                                            |
|       | if (Purchases, National, Goods at normal VAT rate) then                 |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 25    | VAT rule 25:                                                            |
|       | if (Sales, Goods at normal VAT rate) then                               |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 26    | VAT rule 26:                                                            |
|       | if (Purchases, National, Real estate) then                              |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 27    | VAT rule 27:                                                            |
|       | if (Sales, Real estate) then                                            |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 28    | VAT rule 28:                                                            |
|       | if (Purchases, National, Vehicles) then                                 |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 29    | VAT rule 29:                                                            |
|       | if (Sales, Vehicles) then                                               |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 30    | VAT rule 30:                                                            |
|       | if (Purchases, National, Goods at reduced VAT rate) then                |
|       | apply 0.09 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 31    | VAT rule 31:                                                            |
|       | if (Sales, Goods at reduced VAT rate) then                              |
|       | apply 0.09 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 32    | VAT rule 32:                                                            |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
<BLANKLINE>


For example here is the rule that applies when selling a normal product to a
private person:

>>> rule = vat.VatRules.get_vat_rule(vat.VatAreas.national, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.goods)

The Estonian VAT rate is 20%:

>>> rule.rate
Decimal('0.20')
>>> rule.vat_account
<CommonAccounts.vat_due:4510>
>>> rule.vat_account.get_object()
Account #7 ('(4510) VAT due')

This VAT is not returnable:

>>> rule.vat_returnable
False
>>> rule.vat_returnable_account

>>> vat.VatRules.get_vat_rule(vat.VatAreas.international, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.goods).rate
Decimal('0.20')

Note that returnable VAT is used only in purchase invoices, not in sales.  In a
sales invoice to an intracom partner, there is simply no VAT to be generated.
IOW even for services and good for which national customers must pay VAT
(because their VAT class is normal or reduced but not exempt), the VAT rule
specifies a rate of 0.



VAT declaration
===============

.. class:: DeclarationFields

    The list of fields in a VAT declaration.

>>> rt.show(eevat.DeclarationFields)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| value | name | text  | Description                                                                                                                                                                                        |
+=======+======+=======+====================================================================================================================================================================================================+
| 1     | F1   | [1]   | 20% määraga maksustatavad toimingud ja tehingud |br|                                                                                                                                               |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes !cocontractor !exempt !intracom !tax_free |br|                                                                                                                                             |
|       |      |       | classes goods services |br|                                                                                                                                                                        |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2     | F2   | [2]   | 9% määraga maksustatavad toimingud ja tehingud |br|                                                                                                                                                |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes !cocontractor !exempt !intracom !tax_free |br|                                                                                                                                             |
|       |      |       | classes reduced |br|                                                                                                                                                                               |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3     | F3   | [3]   | 0% määraga maksustatavad toimingud ja tehingud, sh |br|                                                                                                                                            |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes cocontractor exempt intracom tax_free |br|                                                                                                                                                 |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 31    | F31  | [31]  | 1) kauba ühendusesisene käive ja teise liikmesriigi maksukohustuslasele / piiratud maksukohustuslasele osutatud teenuste käive kokku, sh |br|                                                      |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes cocontractor intracom |br|                                                                                                                                                                 |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 311   | F311 | [311] | 1) kauba ühendusesisene käive |br|                                                                                                                                                                 |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes intracom |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 32    | F32  | [32]  | 2) kauba eksport, sh |br|                                                                                                                                                                          |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes exempt tax_free |br|                                                                                                                                                                       |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 321   | F321 | [321] | 1) käibemaksutagastusega müük reisijale |br|                                                                                                                                                       |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes tax_free |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4     | F4   | [4]   | Käibemaks kokku (20% lahtrist 1 + 9% lahtrist 2) |br|                                                                                                                                              |
|       |      |       | columns 40 |br|                                                                                                                                                                                    |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 41    | F41  | [41]  | Impordilt tasumisele kuuluv käibemaks |br|                                                                                                                                                         |
|       |      |       | columns 41 |br|                                                                                                                                                                                    |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 5     | F5   | [5]   | Kokku sisendkäibemaksusumma, mis on seadusega lubatud maha arvata, sh |br|                                                                                                                         |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 51    | F51  | [51]  | 1) impordilt tasutud või tasumisele kuuluv käibemaks |br|                                                                                                                                          |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | regimes intracom |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 52    | F52  | [52]  | 2) põhivara soetamiselt tasutud või tasumisele kuuluv käibemaks |br|                                                                                                                               |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | classes real_estate |br|                                                                                                                                                                           |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 53    | F53  | [53]  | 3) ettevõtluses (100%) kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks |br|                          |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | classes vehicles |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 54    | F54  | [54]  | 4) osaliselt ettevõtluses kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks |br|                       |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | classes vehicles |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6     | F6   | [6]   | Kauba ühendusesisene soetamine ja teise liikmesriigi maksukohustuslaselt saadud teenused kokku, sh |br|                                                                                            |
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 61    | F61  | [61]  | 1) kauba ühendusesisene soetamine |br|                                                                                                                                                             |
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | regimes intracom |br|                                                                                                                                                                              |
|       |      |       | classes goods |br|                                                                                                                                                                                 |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 7     | F7   | [7]   | Muu kauba soetamine ja teenuse saamine, mida maksustatakse käibemaksuga, sh |br|                                                                                                                   |
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | regimes !intracom |br|                                                                                                                                                                             |
|       |      |       | classes !goods |br|                                                                                                                                                                                |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 71    | F71  | [71]  | 1) erikorra alusel maksustatava kinnisasja, metallijäätmete, väärismetalli ja metalltoodete soetamine (KMS § 41¹) |br|                                                                             |
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | regimes !intracom |br|                                                                                                                                                                             |
|       |      |       | classes !goods |br|                                                                                                                                                                                |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8     | F8   | [8]   | Maksuvaba käive |br|                                                                                                                                                                               |
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | classes exempt |br|                                                                                                                                                                                |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 9     | F9   | [9]   | Erikorra alusel maksustatava kinnisasja, metallijäätmete, väärismetalli ja metalltoodete käive (KMS § 411) ning teises liikmesriigis paigaldatava või kokkupandava kauba maksustatav väärtus |br|  |
|       |      |       | columns 61 |br|                                                                                                                                                                                    |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 10    | F10  | [10]  | Täpsustused (-) |br|                                                                                                                                                                               |
|       |      |       | WritableDeclarationField Credit |br|                                                                                                                                                               |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 11    | F11  | [11]  | Täpsustused (+) |br|                                                                                                                                                                               |
|       |      |       | WritableDeclarationField Debit |br|                                                                                                                                                                |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 13    | F13  | [13]  | Tasumisele kuuluv(+) või enammakstud (-) käibemaks (lahter 4 + lahter 41 - lahter 5 + lahter 10 - lahter 11) |br|                                                                                  |
|       |      |       | SumDeclarationField Credit |br|                                                                                                                                                                    |
|       |      |       | = F4 + F41 + F5 + F10 + F11 |br|                                                                                                                                                                   |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
<BLANKLINE>


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
[<VatRegimes.normal:10>, <VatRegimes.subject:20>, <VatRegimes.cocontractor:25>, <VatRegimes.tax_free:40>, <VatRegimes.exempt:60>]

>>> nl = countries.Country(isocode='NL')
>>> vat.VatAreas.get_for_country(nl)
<VatAreas.eu:20>
>>> list(rt.models.vat.get_vat_regime_choices(nl))
[<VatRegimes.normal:10>, <VatRegimes.intracom:30>, <VatRegimes.tax_free:40>, <VatRegimes.exempt:60>]

>>> us = countries.Country(isocode='US')
>>> vat.VatAreas.get_for_country(countries.Country(isocode='US'))
<VatAreas.international:30>
>>> list(rt.models.vat.get_vat_regime_choices(us))
[<VatRegimes.normal:10>, <VatRegimes.tax_free:40>, <VatRegimes.outside:50>, <VatRegimes.exempt:60>]


Intracom
========


>>> rt.show(vat.IntracomSales)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF +ELLIPSIS
==================== ================= ================ ================= ================= ===== ==============
 Invoice              Partner           VAT id           VAT regime        Total excl. VAT   VAT   Total to pay
-------------------- ----------------- ---------------- ----------------- ----------------- ----- --------------
 *SLS 4/2018*         Bäckerei Mießen   BE7336627818     Intra-community   280,00                  280,00
 *SLS 8/2018*         Van Achter NV     NL634943207B01   Intra-community   1 939,82                1 939,82
 *SLS 12/2018*        Moulin Rouge      FR14406028064    Intra-community   2 013,88                2 013,88
 **Total (3 rows)**                                                        **4 233,70**            **4 233,70**
==================== ================= ================ ================= ================= ===== ==============
<BLANKLINE>


>>> rt.show(vat.IntracomPurchases)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ================= ============== ================= ================= ===== ===============
 Invoice               Partner           VAT id         VAT regime        Total excl. VAT   VAT   Total to pay
--------------------- ----------------- -------------- ----------------- ----------------- ----- ---------------
 *PRC 4/2018*          Bäckerei Mießen   BE7336627818   Intra-community   1 199,90                1 199,90
 *PRC 4/2019*          Bäckerei Mießen   BE7336627818   Intra-community   1 213,00                1 213,00
 *PRC 11/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 200,50                1 200,50
 *PRC 11/2019*         Bäckerei Mießen   BE7336627818   Intra-community   1 213,20                1 213,20
 *PRC 18/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 201,00                1 201,00
 *PRC 18/2019*         Bäckerei Mießen   BE7336627818   Intra-community   1 214,40                1 214,40
 *PRC 25/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 201,20                1 201,20
 *PRC 25/2019*         Bäckerei Mießen   BE7336627818   Intra-community   1 211,90                1 211,90
 *PRC 32/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 202,40                1 202,40
 *PRC 32/2019*         Bäckerei Mießen   BE7336627818   Intra-community   1 212,50                1 212,50
 *PRC 39/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 199,90                1 199,90
 *PRC 39/2019*         Bäckerei Mießen   BE7336627818   Intra-community   1 213,00                1 213,00
 *PRC 46/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 200,50                1 200,50
 *PRC 53/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 201,00                1 201,00
 *PRC 60/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 201,20                1 201,20
 *PRC 67/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 202,40                1 202,40
 *PRC 74/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 199,90                1 199,90
 *PRC 81/2018*         Bäckerei Mießen   BE7336627818   Intra-community   1 200,50                1 200,50
 **Total (18 rows)**                                                      **21 688,40**           **21 688,40**
===================== ================= ============== ================= ================= ===== ===============
<BLANKLINE>


External references
===================

- https://www.emta.ee/et/ariklient/tulu-kulu-kaive-kasum/kaibemaksuseaduse-selgitused/maksustamisperiood-ja
- https://www.riigiteataja.ee/aktilisa/1060/1201/7010/Lisa%201.pdf#
- https://www.emta.ee/et/ariklient/tulu-kulu-kaive-kasum/kaibedeklaratsiooni-esitamine/kaibedeklaratsiooni-tehniline

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
 40     tax_free       Tax-free                                Nein           Ja
 50     outside        Außerhalb EU            International   Nein           Ja
 60     exempt         Befreit von MwSt.                       Nein           Nein
====== ============== ======================= =============== ============== ==========
<BLANKLINE>


>>> rt.show(vat.VatClasses, language="et")
======= ============= ===========================
 value   nimi          text
------- ------------- ---------------------------
 010     goods         Goods at normal VAT rate
 020     reduced       Goods at reduced VAT rate
 030     exempt        Goods exempt from VAT
 100     services      Teenused
 200     investments   Investeeringud
 210     real_estate   Real estate
 220     vehicles      Vehicles
======= ============= ===========================
<BLANKLINE>

>>> rt.show(vat.VatAreas, language="et")
======= =============== ===============
 value   nimi            text
------- --------------- ---------------
 10      national        National
 20      eu              EU
 30      international   International
======= =============== ===============
<BLANKLINE>


Returnable VAT
==============

A purchases invoice with :term:`Returnable VAT`:

>>> invoice = vat.VatAccountInvoice.objects.filter(vat_regime=vat.VatRegimes.intracom).first()
>>> print(invoice)
PRC 4/2018
>>> rt.show('vat.ItemsByInvoice', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
========================== ============= ============= ================= ===== ==============
 Account                    Description   VAT class     Total excl. VAT   VAT   Total to pay
-------------------------- ------------- ------------- ----------------- ----- --------------
 (6040) Purchase of goods                 Real estate   1 199,90                1 199,90
 **Total (1 rows)**                                     **1 199,90**            **1 199,90**
========================== ============= ============= ================= ===== ==============
<BLANKLINE>


>>> rt.show('vat.MovementsByVoucher', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
========================== ================= ============== ============== ============= ================ =========
 Account                    Partner           Debit          Credit         VAT class     Match            Cleared
-------------------------- ----------------- -------------- -------------- ------------- ---------------- ---------
 (4100) Suppliers           Bäckerei Mießen                  1 199,90                     **PRC 4/2018**   Yes
 (4520) VAT deductible                                       239,98         Real estate                    Yes
 (4530) VAT returnable                        239,98                        Real estate                    Yes
 (6040) Purchase of goods                     1 199,90                      Real estate                    Yes
                                              **1 439,88**   **1 439,88**
========================== ================= ============== ============== ============= ================ =========
<BLANKLINE>


>>> print(invoice.total_base)
1199.90
>>> print(invoice.total_vat)
0.00
>>> print(invoice.total_incl)
1199.90

Note that above is for purchases only. Intracom *sales* invoices have no
:term:`returnable VAT` because they don't have any VAT at all:

>>> invoice = rt.models.sales.VatProductInvoice.objects.get(number=4, accounting_period__year__ref='2018')
>>> invoice.vat_regime
<VatRegimes.intracom:30>

>>> rt.show('vat.MovementsByVoucher', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
======================= ================= ============ ============ =========== ================ =========
 Account                 Partner           Debit        Credit       VAT class   Match            Cleared
----------------------- ----------------- ------------ ------------ ----------- ---------------- ---------
 (4000) Customers        Bäckerei Mießen   280,00                                **SLS 4/2018**   Yes
 (4510) VAT due                            56,00                     Services                     Yes
 (4530) VAT returnable                                  56,00        Services                     Yes
 (7000) Sales                                           280,00       Services                     Yes
                                           **336,00**   **336,00**
======================= ================= ============ ============ =========== ================ =========
<BLANKLINE>


>>> print(invoice.total_base)
280.00
>>> print(invoice.total_vat)
0.00
>>> print(invoice.total_incl)
280.00


Invoices covered by a declaration
=================================

The detail view of a VAT declarations has two slave tables that show the
invoices covered by this declaration.

>>> obj = eevat.Declaration.objects.get(accounting_period__ref="2019-05")
>>> print(obj)
VAT 5/2019

>>> rt.show(vat.PurchasesByDeclaration, master_instance=obj)
==================== ===================== ================ ================= ================= =========== ==============
 Invoice              Partner               VAT id           VAT regime        Total excl. VAT   VAT         Total to pay
-------------------- --------------------- ---------------- ----------------- ----------------- ----------- --------------
 *PRC 29/2019*        Bestbank              EE4391498123     Private person    37,61             3,39        41,00
 *PRC 30/2019*        Rumma & Ko OÜ         EE100588749      Subject to VAT    129,75            13,65       143,40
 *PRC 31/2019*        Bäckerei Ausdemwald   BE2206624259     Private person    608,30                        608,30
 *PRC 32/2019*        Bäckerei Mießen       BE7336627818     Intra-community   1 212,50                      1 212,50
 *PRC 33/2019*        Bäckerei Schmitz      BE8204648930     Tax-free          3 274,78                      3 274,78
 *PRC 34/2019*        Garage Mergelsberg    BE4498652125     Exempt            143,50                        143,50
 *PRC 35/2019*        Donderweer BV         NL211892074B01   Private person    202,50                        202,50
 **Total (7 rows)**                                                            **5 608,94**      **17,04**   **5 625,98**
==================== ===================== ================ ================= ================= =========== ==============
<BLANKLINE>

>>> rt.show(vat.SalesByDeclaration, master_instance=obj)
==================== ==================== ======== ================ ================= ============ ==============
 Invoice              Partner              VAT id   VAT regime       Total excl. VAT   VAT          Total to pay
-------------------- -------------------- -------- ---------------- ----------------- ------------ --------------
 *SLS 21/2019*        Dmitriev Eva-Liisa            Private person   1 680,57          333,31       2 013,88
 *SLS 22/2019*        Nikitin Einar                 Tax-free         1 624,88          324,97       1 949,85
 *SLS 23/2019*        Mölder Elmar                  Exempt           831,82                         831,82
 *SLS 24/2019*        Jegorov Eve                   Private person   870,83            174,17       1 045,00
 **Total (4 rows)**                                                  **5 008,10**      **832,45**   **5 840,55**
==================== ==================== ======== ================ ================= ============ ==============
<BLANKLINE>


Here is the content of the fields in the detail of that declaration:

>>> obj.print_declared_values()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
[1] 20% määraga maksustatavad toimingud ja tehingud : 2537.40
[3] 0% määraga maksustatavad toimingud ja tehingud, sh : 2456.70
[32] 2) kauba eksport, sh : 2456.70
[321] 1) käibemaksutagastusega müük reisijale : 1624.88
[4] Käibemaks kokku (20% lahtrist 1 + 9% lahtrist 2) : 832.45
[41] Impordilt tasumisele kuuluv käibemaks : 242.50
[5] Kokku sisendkäibemaksusumma, mis on seadusega lubatud maha arvata, sh : 225.46
[51] 1) impordilt tasutud või tasumisele kuuluv käibemaks : 242.50
[53] 3) ettevõtluses (100%) kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks : 242.50
[54] 4) osaliselt ettevõtluses kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks : 242.50
[6] Kauba ühendusesisene soetamine ja teise liikmesriigi maksukohustuslaselt saadud teenused kokku, sh : 1343.65
[7] Muu kauba soetamine ja teenuse saamine, mida maksustatakse käibemaksuga, sh : 131.15
[71] 1) erikorra alusel maksustatava kinnisasja, metallijäätmete, väärismetalli ja metalltoodete soetamine (KMS § 41¹) : 131.15
[8] Maksuvaba käive : 62.90
[9] Erikorra alusel maksustatava kinnisasja, metallijäätmete, väärismetalli ja metalltoodete käive (KMS § 411) ning teises liikmesriigis paigaldatava või kokkupandava kauba maksustatav väärtus : 3555.69
[13] Tasumisele kuuluv(+) või enammakstud (-) käibemaks (lahter 4 + lahter 41 - lahter 5 + lahter 10 - lahter 11) : 815.41

Here is another way to see the content of the fields in the detail of that declaration:

>>> # rt.login("robin").show_detail(obj)
>>> print(py2rst(obj))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
(main):
- **Info** (info):
  - (info_1): **Start period** (start_period): 2019-05, **End period** (end_period), **Entry date** (entry_date): 04/05/2019, **Accounting period** (accounting_period): 2019-05
  - **Movements** (MovementsByVoucher): No data to display
- **Values** (values):
  - (values_1): **Partner** (partner): Maksu- ja Tolliamet, **Author** (user): Robin Rood, **Workflow** (workflow_buttons): **Registered**
  - (values_2):
    - (c1): **[1]** (F1): 2 537,40, **[2]** (F2): , **[3]** (F3): 2 456,70, **[31]** (F31): , **[311]** (F311): , **[32]** (F32): 2 456,70, **[321]** (F321): 1 624,88
    - (c2): **[4]** (F4): 832,45, **[41]** (F41): 242,50, **[5]** (F5): 225,46, **[51]** (F51): 242,50, **[52]** (F52): , **[53]** (F53): 242,50, **[54]** (F54): 242,50
    - (c3): **[6]** (F6): 1 343,65, **[61]** (F61): , **[7]** (F7): 131,15, **[71]** (F71): 131,15
    - (c4): **[8]** (F8): 62,90, **[9]** (F9): 3 555,69, **[10]** (F10): , **[11]** (F11): , **[13]** (F13): 815,41
  - (values_3):
    - **VAT sales** (vat.SalesByDeclaration)
    - **VAT purchases** (vat.PurchasesByDeclaration)
- **Declared movements** (vat.MovementsByDeclaration)
<BLANKLINE>
