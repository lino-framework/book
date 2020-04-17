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
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
+-------+-------------------------------------------------------------------------+
| value | Description                                                             |
+=======+=========================================================================+
| 1     | VAT rule 1:                                                             |
|       | if (Exempt) then                                                        |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 2     | VAT rule 2:                                                             |
|       | if (Outside EU) then                                                    |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 3     | VAT rule 3:                                                             |
|       | if (Purchases, Intra-community, EU, Services) then                      |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 4     | VAT rule 4:                                                             |
|       | if (Sales, Intra-community, EU, Services) then                          |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 5     | VAT rule 5:                                                             |
|       | if (Purchases, Co-contractor, National, Services) then                  |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 6     | VAT rule 6:                                                             |
|       | if (Sales, Co-contractor, National, Services) then                      |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 7     | VAT rule 7:                                                             |
|       | if (Purchases, Intra-community, EU, Goods at normal VAT rate) then      |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 8     | VAT rule 8:                                                             |
|       | if (Sales, Intra-community, EU, Goods at normal VAT rate) then          |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 9     | VAT rule 9:                                                             |
|       | if (Purchases, Co-contractor, National, Goods at normal VAT rate) then  |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 10    | VAT rule 10:                                                            |
|       | if (Sales, Co-contractor, National, Goods at normal VAT rate) then      |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 11    | VAT rule 11:                                                            |
|       | if (Purchases, Intra-community, EU, Real estate) then                   |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 12    | VAT rule 12:                                                            |
|       | if (Sales, Intra-community, EU, Real estate) then                       |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 13    | VAT rule 13:                                                            |
|       | if (Purchases, Co-contractor, National, Real estate) then               |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 14    | VAT rule 14:                                                            |
|       | if (Sales, Co-contractor, National, Real estate) then                   |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 15    | VAT rule 15:                                                            |
|       | if (Purchases, Intra-community, EU, Vehicles) then                      |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 16    | VAT rule 16:                                                            |
|       | if (Sales, Intra-community, EU, Vehicles) then                          |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 17    | VAT rule 17:                                                            |
|       | if (Purchases, Co-contractor, National, Vehicles) then                  |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 18    | VAT rule 18:                                                            |
|       | if (Sales, Co-contractor, National, Vehicles) then                      |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 19    | VAT rule 19:                                                            |
|       | if (Purchases, Intra-community, EU, Goods at reduced VAT rate) then     |
|       | apply 0.09 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 20    | VAT rule 20:                                                            |
|       | if (Sales, Intra-community, EU, Goods at reduced VAT rate) then         |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 21    | VAT rule 21:                                                            |
|       | if (Purchases, Co-contractor, National, Goods at reduced VAT rate) then |
|       | apply 0.09 %                                                            |
|       | and book to VAT deductible                                              |
|       | (return to VAT returnable)                                              |
+-------+-------------------------------------------------------------------------+
| 22    | VAT rule 22:                                                            |
|       | if (Sales, Co-contractor, National, Goods at reduced VAT rate) then     |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+
| 23    | VAT rule 23:                                                            |
|       | if (Purchases, National, Services) then                                 |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 24    | VAT rule 24:                                                            |
|       | if (Sales, Services) then                                               |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 25    | VAT rule 25:                                                            |
|       | if (Purchases, National, Goods at normal VAT rate) then                 |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 26    | VAT rule 26:                                                            |
|       | if (Sales, Goods at normal VAT rate) then                               |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 27    | VAT rule 27:                                                            |
|       | if (Purchases, National, Real estate) then                              |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 28    | VAT rule 28:                                                            |
|       | if (Sales, Real estate) then                                            |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 29    | VAT rule 29:                                                            |
|       | if (Purchases, National, Vehicles) then                                 |
|       | apply 0.20 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 30    | VAT rule 30:                                                            |
|       | if (Sales, Vehicles) then                                               |
|       | apply 0.20 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 31    | VAT rule 31:                                                            |
|       | if (Purchases, National, Goods at reduced VAT rate) then                |
|       | apply 0.09 %                                                            |
|       | and book to VAT deductible                                              |
+-------+-------------------------------------------------------------------------+
| 32    | VAT rule 32:                                                            |
|       | if (Sales, Goods at reduced VAT rate) then                              |
|       | apply 0.09 %                                                            |
|       | and book to VAT due                                                     |
+-------+-------------------------------------------------------------------------+
| 33    | VAT rule 33:                                                            |
|       | apply 0 %                                                               |
|       | and book to None                                                        |
+-------+-------------------------------------------------------------------------+

The normal Estonian VAT rate is 20%.  For example here is the rule that applies
when selling a normal product to a private person:

>>> rule = vat.VatRules.get_vat_rule(vat.VatAreas.national, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.goods)
>>> rule.rate
Decimal('0.20')
>>> rule.vat_account
<CommonAccounts.vat_due:4510>
>>> rule.vat_account.get_object()
Account #7 ('(4510) VAT due')
>>> rule.vat_returnable_account is None
True

Or selling a normal product to a company outside of Europe:

>>> rule = vat.VatRules.get_vat_rule(vat.VatAreas.international, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.goods)
>>> rule.rate
Decimal('0.20')
>>> rule.vat_account
<CommonAccounts.vat_due:4510>
>>> rule.vat_returnable_account is None
True

Or selling a normal product to a company in another country of the European Union:

>>> rule = vat.VatRules.get_vat_rule(vat.VatAreas.eu, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.goods)
>>> rule.rate
Decimal('0.20')
>>> rule.vat_account
<CommonAccounts.vat_due:4510>
>>> rule.vat_returnable_account is None
True

Note that returnable VAT is used only in purchase invoices, not in sales.  In a
sales invoice to an intra-community partner, there is simply no VAT to be
generated. IOW even for services and goods for which national customers must pay
VAT (because their VAT class is normal or reduced but not exempt), the VAT rule
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
| 1a    | F1a  | [1a]  | 20% määraga maksustatavad müügid |br|                                                                                                                                                              |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes normal subject |br|                                                                                                                                                                        |
|       |      |       | classes goods services |br|                                                                                                                                                                        |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1b    | F1b  | [1b]  | 20% määraga maksustatavad ostud liikmesriigi maksukohustuslaselt |br|                                                                                                                              |
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | regimes intracom |br|                                                                                                                                                                              |
|       |      |       | classes goods services |br|                                                                                                                                                                        |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1     | F1   | [1]   | 20% määraga maksustatavad toimingud ja tehingud |br|                                                                                                                                               |
|       |      |       | SumDeclarationField Credit |br|                                                                                                                                                                    |
|       |      |       | = 1a + 1b |br|                                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2a    | F2a  | [2a]  | 9% määraga maksustatavad müügid |br|                                                                                                                                                               |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes normal subject |br|                                                                                                                                                                        |
|       |      |       | classes reduced |br|                                                                                                                                                                               |
|       |      |       | MvtDeclarationField Credit |br|                                                                                                                                                                    |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2b    | F2b  | [2b]  | 9% määraga maksustatavad ostud liikmesriigi maksukohustuslaselt |br|                                                                                                                               |
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | regimes intracom |br|                                                                                                                                                                              |
|       |      |       | classes reduced |br|                                                                                                                                                                               |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2     | F2   | [2]   | 9% määraga maksustatavad toimingud ja tehingud |br|                                                                                                                                                |
|       |      |       | SumDeclarationField Credit |br|                                                                                                                                                                    |
|       |      |       | = 2a + 2b |br|                                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 3     | F3   | [3]   | 0% määraga maksustatavad toimingud ja tehingud, sh |br|                                                                                                                                            |
|       |      |       | columns 10 |br|                                                                                                                                                                                    |
|       |      |       | regimes !normal !subject |br|                                                                                                                                                                      |
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
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 51    | F51  | [51]  | 1) impordilt tasutud või tasumisele kuuluv käibemaks |br|                                                                                                                                          |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | regimes intracom |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 52    | F52  | [52]  | 2) põhivara soetamiselt tasutud või tasumisele kuuluv käibemaks |br|                                                                                                                               |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | classes real_estate |br|                                                                                                                                                                           |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 53    | F53  | [53]  | 3) ettevõtluses (100%) kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks |br|                          |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | classes vehicles |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
+-------+------+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 54    | F54  | [54]  | 4) osaliselt ettevõtluses kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks |br|                       |
|       |      |       | columns 50 |br|                                                                                                                                                                                    |
|       |      |       | classes vehicles |br|                                                                                                                                                                              |
|       |      |       | MvtDeclarationField Debit |br|                                                                                                                                                                     |
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
|       |      |       | columns 60 |br|                                                                                                                                                                                    |
|       |      |       | classes !goods !real_estate !services !vehicles |br|                                                                                                                                               |
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
|       |      |       | = 4 + 41 - 5 + 10 - 11 |br|                                                                                                                                                                        |
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
===================== =========================== ================ ================= ================= ===== ===============
 Invoice               Partner                     VAT id           VAT regime        Total excl. VAT   VAT   Total to pay
--------------------- --------------------------- ---------------- ----------------- ----------------- ----- ---------------
 *SLS 3/2018*          Bäckerei Ausdemwald         BE2206624259     Intra-community   679,81                  679,81
 *SLS 4/2018*          Bäckerei Mießen             BE7336627818     Intra-community   280,00                  280,00
 *SLS 5/2018*          Bäckerei Schmitz            BE8204648930     Intra-community   535,00                  535,00
 *SLS 6/2018*          Garage Mergelsberg          BE4498652125     Intra-community   1 110,16                1 110,16
 *SLS 7/2018*          Donderweer BV               NL211892074B01   Intra-community   1 499,85                1 499,85
 *SLS 8/2018*          Van Achter NV               NL634943207B01   Intra-community   1 939,82                1 939,82
 *SLS 9/2018*          Hans Flott & Co             DE141548977      Intra-community   815,96                  815,96
 *SLS 10/2018*         Bernd Brechts Bücherladen   DE529665130      Intra-community   320,00                  320,00
 *SLS 11/2018*         Reinhards Baumschule        DE575791208      Intra-community   548,50                  548,50
 *SLS 12/2018*         Moulin Rouge                FR14406028064    Intra-community   2 013,88                2 013,88
 *SLS 13/2018*         Auto École Verte            FR74229232671    Intra-community   1 949,85                1 949,85
 **Total (11 rows)**                                                                  **11 692,83**           **11 692,83**
===================== =========================== ================ ================= ================= ===== ===============
<BLANKLINE>


>>> rt.show(vat.IntracomPurchases)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ===================== ================ ================= ================= ===== ===============
 Invoice               Partner               VAT id           VAT regime        Total excl. VAT   VAT   Total to pay
--------------------- --------------------- ---------------- ----------------- ----------------- ----- ---------------
 *PRC 3/2018*          Bäckerei Ausdemwald   BE2206624259     Intra-community   603,60                  603,60
 *PRC 4/2018*          Bäckerei Mießen       BE7336627818     Intra-community   1 199,90                1 199,90
 *PRC 5/2018*          Bäckerei Schmitz      BE8204648930     Intra-community   3 241,68                3 241,68
 *PRC 6/2018*          Garage Mergelsberg    BE4498652125     Intra-community   143,40                  143,40
 *PRC 7/2018*          Donderweer BV         NL211892074B01   Intra-community   199,90                  199,90
 *PRC 10/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   602,30                  602,30
 *PRC 11/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 200,50                1 200,50
 *PRC 12/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 242,38                3 242,38
 *PRC 13/2018*         Garage Mergelsberg    BE4498652125     Intra-community   142,10                  142,10
 *PRC 14/2018*         Donderweer BV         NL211892074B01   Intra-community   200,50                  200,50
 *PRC 17/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   600,40                  600,40
 *PRC 18/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 201,00                1 201,00
 *PRC 19/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 243,78                3 243,78
 *PRC 20/2018*         Garage Mergelsberg    BE4498652125     Intra-community   140,20                  140,20
 *PRC 21/2018*         Donderweer BV         NL211892074B01   Intra-community   201,00                  201,00
 *PRC 24/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   601,50                  601,50
 *PRC 25/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 201,20                1 201,20
 *PRC 26/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 242,48                3 242,48
 *PRC 27/2018*         Garage Mergelsberg    BE4498652125     Intra-community   141,30                  141,30
 *PRC 28/2018*         Donderweer BV         NL211892074B01   Intra-community   201,20                  201,20
 *PRC 31/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   602,20                  602,20
 *PRC 32/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 202,40                1 202,40
 *PRC 33/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 240,58                3 240,58
 *PRC 34/2018*         Garage Mergelsberg    BE4498652125     Intra-community   142,00                  142,00
 *PRC 35/2018*         Donderweer BV         NL211892074B01   Intra-community   202,40                  202,40
 *PRC 38/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   603,60                  603,60
 *PRC 39/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 199,90                1 199,90
 *PRC 40/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 241,68                3 241,68
 *PRC 41/2018*         Garage Mergelsberg    BE4498652125     Intra-community   143,40                  143,40
 *PRC 42/2018*         Donderweer BV         NL211892074B01   Intra-community   199,90                  199,90
 *PRC 45/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   602,30                  602,30
 *PRC 46/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 200,50                1 200,50
 *PRC 47/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 242,38                3 242,38
 *PRC 48/2018*         Garage Mergelsberg    BE4498652125     Intra-community   142,10                  142,10
 *PRC 49/2018*         Donderweer BV         NL211892074B01   Intra-community   200,50                  200,50
 *PRC 52/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   600,40                  600,40
 *PRC 53/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 201,00                1 201,00
 *PRC 54/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 243,78                3 243,78
 *PRC 55/2018*         Garage Mergelsberg    BE4498652125     Intra-community   140,20                  140,20
 *PRC 56/2018*         Donderweer BV         NL211892074B01   Intra-community   201,00                  201,00
 *PRC 59/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   601,50                  601,50
 *PRC 60/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 201,20                1 201,20
 *PRC 61/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 242,48                3 242,48
 *PRC 62/2018*         Garage Mergelsberg    BE4498652125     Intra-community   141,30                  141,30
 *PRC 63/2018*         Donderweer BV         NL211892074B01   Intra-community   201,20                  201,20
 *PRC 66/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   602,20                  602,20
 *PRC 67/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 202,40                1 202,40
 *PRC 68/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 240,58                3 240,58
 *PRC 69/2018*         Garage Mergelsberg    BE4498652125     Intra-community   142,00                  142,00
 *PRC 70/2018*         Donderweer BV         NL211892074B01   Intra-community   202,40                  202,40
 *PRC 73/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   603,60                  603,60
 *PRC 74/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 199,90                1 199,90
 *PRC 75/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 241,68                3 241,68
 *PRC 76/2018*         Garage Mergelsberg    BE4498652125     Intra-community   143,40                  143,40
 *PRC 77/2018*         Donderweer BV         NL211892074B01   Intra-community   199,90                  199,90
 *PRC 80/2018*         Bäckerei Ausdemwald   BE2206624259     Intra-community   602,30                  602,30
 *PRC 81/2018*         Bäckerei Mießen       BE7336627818     Intra-community   1 200,50                1 200,50
 *PRC 82/2018*         Bäckerei Schmitz      BE8204648930     Intra-community   3 242,38                3 242,38
 *PRC 83/2018*         Garage Mergelsberg    BE4498652125     Intra-community   142,10                  142,10
 *PRC 84/2018*         Donderweer BV         NL211892074B01   Intra-community   200,50                  200,50
 *PRC 3/2019*          Bäckerei Ausdemwald   BE2206624259     Intra-community   606,40                  606,40
 *PRC 4/2019*          Bäckerei Mießen       BE7336627818     Intra-community   1 213,00                1 213,00
 *PRC 5/2019*          Bäckerei Schmitz      BE8204648930     Intra-community   3 276,18                3 276,18
 *PRC 6/2019*          Garage Mergelsberg    BE4498652125     Intra-community   141,60                  141,60
 *PRC 7/2019*          Donderweer BV         NL211892074B01   Intra-community   203,00                  203,00
 *PRC 10/2019*         Bäckerei Ausdemwald   BE2206624259     Intra-community   607,50                  607,50
 *PRC 11/2019*         Bäckerei Mießen       BE7336627818     Intra-community   1 213,20                1 213,20
 *PRC 12/2019*         Bäckerei Schmitz      BE8204648930     Intra-community   3 274,88                3 274,88
 *PRC 13/2019*         Garage Mergelsberg    BE4498652125     Intra-community   142,70                  142,70
 *PRC 14/2019*         Donderweer BV         NL211892074B01   Intra-community   203,20                  203,20
 *PRC 17/2019*         Bäckerei Ausdemwald   BE2206624259     Intra-community   608,20                  608,20
 *PRC 18/2019*         Bäckerei Mießen       BE7336627818     Intra-community   1 214,40                1 214,40
 *PRC 19/2019*         Bäckerei Schmitz      BE8204648930     Intra-community   3 272,98                3 272,98
 *PRC 20/2019*         Garage Mergelsberg    BE4498652125     Intra-community   143,40                  143,40
 *PRC 21/2019*         Donderweer BV         NL211892074B01   Intra-community   204,40                  204,40
 *PRC 24/2019*         Bäckerei Ausdemwald   BE2206624259     Intra-community   609,60                  609,60
 *PRC 25/2019*         Bäckerei Mießen       BE7336627818     Intra-community   1 211,90                1 211,90
 *PRC 26/2019*         Bäckerei Schmitz      BE8204648930     Intra-community   3 274,08                3 274,08
 *PRC 27/2019*         Garage Mergelsberg    BE4498652125     Intra-community   144,80                  144,80
 *PRC 28/2019*         Donderweer BV         NL211892074B01   Intra-community   201,90                  201,90
 *PRC 31/2019*         Bäckerei Ausdemwald   BE2206624259     Intra-community   608,30                  608,30
 *PRC 32/2019*         Bäckerei Mießen       BE7336627818     Intra-community   1 212,50                1 212,50
 *PRC 33/2019*         Bäckerei Schmitz      BE8204648930     Intra-community   3 274,78                3 274,78
 *PRC 34/2019*         Garage Mergelsberg    BE4498652125     Intra-community   143,50                  143,50
 *PRC 35/2019*         Donderweer BV         NL211892074B01   Intra-community   202,50                  202,50
 *PRC 38/2019*         Bäckerei Ausdemwald   BE2206624259     Intra-community   606,40                  606,40
 *PRC 39/2019*         Bäckerei Mießen       BE7336627818     Intra-community   1 213,00                1 213,00
 *PRC 40/2019*         Bäckerei Schmitz      BE8204648930     Intra-community   3 276,18                3 276,18
 *PRC 41/2019*         Garage Mergelsberg    BE4498652125     Intra-community   141,60                  141,60
 *PRC 42/2019*         Donderweer BV         NL211892074B01   Intra-community   203,00                  203,00
 **Total (90 rows)**                                                            **97 305,14**           **97 305,14**
===================== ===================== ================ ================= ================= ===== ===============
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
 Wert   name           Text                    MWSt-Zone       Needs VAT id   item VAT
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
======= ============= ============================
 value   nimi          text
------- ------------- ----------------------------
 010     goods         Kaup tavalise KM määraga
 020     reduced       Kaup vähendatud KM määraga
 030     exempt        Kaup ilma käibemaksuta
 100     services      Teenused
 200     investments   Investeeringud
 210     real_estate   Kinnisvara
 220     vehicles      Sõidukid
======= ============= ============================
<BLANKLINE>


>>> rt.show(vat.VatAreas, language="et")
======= =============== ==============
 value   nimi            text
------- --------------- --------------
 10      national        Riiklik
 20      eu              Euroopa Liit
 30      international   Liiduväline
======= =============== ==============
<BLANKLINE>


Returnable VAT
==============

A purchases invoice with :term:`returnable VAT`:

>>> invoice = vat.VatAccountInvoice.objects.filter(vat_regime=vat.VatRegimes.intracom).first()
>>> print(invoice)
PRC 3/2018
>>> rt.show('vat.ItemsByInvoice', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
================================ ============= ============= ================= ===== ==============
 Account                          Description   VAT class     Total excl. VAT   VAT   Total to pay
-------------------------------- ------------- ------------- ----------------- ----- --------------
 (6010) Purchase of services                    Services      201,20                  201,20
 (6020) Purchase of investments                 Investments   402,40                  402,40
 **Total (2 rows)**                                           **603,60**              **603,60**
================================ ============= ============= ================= ===== ==============
<BLANKLINE>



>>> rt.show('vat.MovementsByVoucher', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
================================ ===================== ============ ============ ============= ================ =========
 Account                          Partner               Debit        Credit       VAT class     Match            Cleared
-------------------------------- --------------------- ------------ ------------ ------------- ---------------- ---------
 (4100) Suppliers                 Bäckerei Ausdemwald                603,60                     **PRC 3/2018**   Yes
 (4520) VAT deductible                                  40,24                     Services                       Yes
 (4530) VAT returnable                                               40,24        Services                       Yes
 (6010) Purchase of services                            201,20                    Services                       Yes
 (6020) Purchase of investments                         402,40                    Investments                    Yes
                                                        **643,84**   **643,84**
================================ ===================== ============ ============ ============= ================ =========
<BLANKLINE>


>>> print(invoice.total_base)
603.60
>>> print(invoice.total_vat)
0.00
>>> print(invoice.total_incl)
603.60

Note that above is for purchases only. Intra-Community *sales* invoices have no
:term:`returnable VAT` because they don't have any VAT at all:

>>> invoice = rt.models.sales.VatProductInvoice.objects.get(number=4, accounting_period__year__ref='2018')
>>> invoice.vat_regime
<VatRegimes.intracom:30>

>>> rt.show('vat.MovementsByVoucher', invoice)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
================== ================= ============ ============ =========== ================ =========
 Account            Partner           Debit        Credit       VAT class   Match            Cleared
------------------ ----------------- ------------ ------------ ----------- ---------------- ---------
 (4000) Customers   Bäckerei Mießen   280,00                                **SLS 4/2018**   Yes
 (7000) Sales                                      280,00       Services                     Yes
                                      **280,00**   **280,00**
================== ================= ============ ============ =========== ================ =========
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
 *PRC 29/2019*        Bestbank              EE4391498123     Subject to VAT    37,61             3,39        41,00
 *PRC 30/2019*        Rumma & Ko OÜ         EE100588749      Subject to VAT    129,75            13,65       143,40
 *PRC 31/2019*        Bäckerei Ausdemwald   BE2206624259     Intra-community   608,30                        608,30
 *PRC 32/2019*        Bäckerei Mießen       BE7336627818     Intra-community   1 212,50                      1 212,50
 *PRC 33/2019*        Bäckerei Schmitz      BE8204648930     Intra-community   3 274,78                      3 274,78
 *PRC 34/2019*        Garage Mergelsberg    BE4498652125     Intra-community   143,50                        143,50
 *PRC 35/2019*        Donderweer BV         NL211892074B01   Intra-community   202,50                        202,50
 **Total (7 rows)**                                                            **5 608,94**      **17,04**   **5 625,98**
==================== ===================== ================ ================= ================= =========== ==============
<BLANKLINE>

>>> rt.show(vat.SalesByDeclaration, master_instance=obj)
==================== ==================== ======== ================ ================= ============ ==============
 Invoice              Partner              VAT id   VAT regime       Total excl. VAT   VAT          Total to pay
-------------------- -------------------- -------- ---------------- ----------------- ------------ --------------
 *SLS 21/2019*        Dmitriev Eva-Liisa            Private person   1 680,57          333,31       2 013,88
 *SLS 22/2019*        Nikitin Einar                 Private person   1 624,88          324,97       1 949,85
 *SLS 23/2019*        Mölder Elmar                  Private person   693,18            138,64       831,82
 *SLS 24/2019*        Jegorov Eve                   Private person   870,83            174,17       1 045,00
 **Total (4 rows)**                                                  **4 869,46**      **971,09**   **5 840,55**
==================== ==================== ======== ================ ================= ============ ==============
<BLANKLINE>


Here is the content of the fields in the detail of that declaration:

>>> obj.print_declared_values()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
[1a] 20% määraga maksustatavad müügid : 4855.46
[1] 20% määraga maksustatavad toimingud ja tehingud : 4855.46
[4] Käibemaks kokku (20% lahtrist 1 + 9% lahtrist 2) : 971.09
[41] Impordilt tasumisele kuuluv käibemaks : -989.77
[5] Kokku sisendkäibemaksusumma, mis on seadusega lubatud maha arvata, sh : 1006.81
[51] 1) impordilt tasutud või tasumisele kuuluv käibemaks : 989.77
[52] 2) põhivara soetamiselt tasutud või tasumisele kuuluv käibemaks : 80.78
[53] 3) ettevõtluses (100%) kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks : 242.50
[54] 4) osaliselt ettevõtluses kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks : 242.50
[6] Kauba ühendusesisene soetamine ja teise liikmesriigi maksukohustuslaselt saadud teenused kokku, sh : 1343.65
[7] Muu kauba soetamine ja teenuse saamine, mida maksustatakse käibemaksuga, sh : 68.25
[71] 1) erikorra alusel maksustatava kinnisasja, metallijäätmete, väärismetalli ja metalltoodete soetamine (KMS § 41¹) : 68.25
[8] Maksuvaba käive : 62.90
[9] Erikorra alusel maksustatava kinnisasja, metallijäätmete, väärismetalli ja metalltoodete käive (KMS § 411) ning teises liikmesriigis paigaldatava või kokkupandava kauba maksustatav väärtus : 62.90
[13] Tasumisele kuuluv(+) või enammakstud (-) käibemaks (lahter 4 + lahter 41 - lahter 5 + lahter 10 - lahter 11) : -1025.49


And these are the movements generated by our declaration:

>>> rt.show('ledger.MovementsByVoucher', obj)
======================= ===================== ============== ============== ================ =========
 Account                 Partner               Debit          Credit         Match            Cleared
----------------------- --------------------- -------------- -------------- ---------------- ---------
 (4500) Tax Offices      Maksu- ja Tolliamet                  954,05         **VAT 5/2019**   Yes
 (4510) VAT due                                971,09                                         Yes
 (4520) VAT deductible                                        1 006,81                        Yes
 (4530) VAT returnable                         989,77                                         Yes
                                               **1 960,86**   **1 960,86**
======================= ===================== ============== ============== ================ =========
<BLANKLINE>


The 2018-11 VAT declaration has values in both fields 1a and 1b:

>>> obj = eevat.Declaration.objects.get(accounting_period__ref="2018-11")
>>> obj.print_declared_values()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
[1a] 20% määraga maksustatavad müügid : 4233.83
[1b] 20% määraga maksustatavad ostud liikmesriigi maksukohustuslaselt : 1199.90
[1] 20% määraga maksustatavad toimingud ja tehingud : 5433.73
[2a] 9% määraga maksustatavad müügid : 274.31
[2] 9% määraga maksustatavad toimingud ja tehingud : 274.31
[4] Käibemaks kokku (20% lahtrist 1 + 9% lahtrist 2) : 871.45
[41] Impordilt tasumisele kuuluv käibemaks : -312.98
[5] Kokku sisendkäibemaksusumma, mis on seadusega lubatud maha arvata, sh : 343.20
[51] 1) impordilt tasutud või tasumisele kuuluv käibemaks : 312.98
[52] 2) põhivara soetamiselt tasutud või tasumisele kuuluv käibemaks : 14.89
[53] 3) ettevõtluses (100%) kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks : 22.29
[54] 4) osaliselt ettevõtluses kasutatava sõiduauto soetamiselt ja sellisesõiduauto tarbeks kaupade soetamiselt ja teenuste saamiselttasutud või tasumisele kuuluv käibemaks : 22.29
[6] Kauba ühendusesisene soetamine ja teise liikmesriigi maksukohustuslaselt saadud teenused kokku, sh : 1328.42
[13] Tasumisele kuuluv(+) või enammakstud (-) käibemaks (lahter 4 + lahter 41 - lahter 5 + lahter 10 - lahter 11) : 215.27

Here again the movements generated by this declaration:

>>> rt.show('ledger.MovementsByVoucher', obj)
======================= ===================== ============== ============== ================= =========
 Account                 Partner               Debit          Credit         Match             Cleared
----------------------- --------------------- -------------- -------------- ----------------- ---------
 (4500) Tax Offices      Maksu- ja Tolliamet                  841,23         **VAT 11/2018**   Yes
 (4510) VAT due                                871,45                                          Yes
 (4520) VAT deductible                                        343,20                           Yes
 (4530) VAT returnable                         312,98                                          Yes
                                               **1 184,43**   **1 184,43**
======================= ===================== ============== ============== ================= =========
<BLANKLINE>
