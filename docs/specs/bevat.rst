.. doctest docs/specs/bevat.rst
.. _xl.bevat:

====================================
``bevat`` : Belgian VAT declarations
====================================

.. currentmodule:: lino_xl.lib.bevat

The :mod:`lino_xl.lib.bevat` plugin adds functionality for handling **Belgian
VAT declarations**.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *


Dependencies
============

Installing this plugin will automatically install :mod:`lino_xl.lib.vat`.

>>> dd.plugins.bevat.needs_plugins
['lino_xl.lib.vat']


Models and actors reference
===========================

.. class:: Declaration

    Django model to represent a Belgian :term:`VAT declaration`.



VAT rules
=========

>>> rt.show(vat.VatRules, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
+-------+---------------------------------------------------------------------+
| value | Description                                                         |
+=======+=====================================================================+
| 1     | VAT rule 1:                                                         |
|       | if (Purchases, National, Services) then                             |
|       | apply 0.21 %                                                        |
|       | and book to VAT deductible                                          |
+-------+---------------------------------------------------------------------+
| 2     | VAT rule 2:                                                         |
|       | if (Purchases, Intra-community, EU, Services) then                  |
|       | apply 0.21 %                                                        |
|       | and book to VAT deductible                                          |
|       | (return to VAT returnable)                                          |
+-------+---------------------------------------------------------------------+
| 3     | VAT rule 3:                                                         |
|       | if (Sales, Services) then                                           |
|       | apply 0.21 %                                                        |
|       | and book to VAT due                                                 |
+-------+---------------------------------------------------------------------+
| 4     | VAT rule 4:                                                         |
|       | if (Purchases, National, Goods at normal VAT rate) then             |
|       | apply 0.21 %                                                        |
|       | and book to VAT deductible                                          |
+-------+---------------------------------------------------------------------+
| 5     | VAT rule 5:                                                         |
|       | if (Purchases, Intra-community, EU, Goods at normal VAT rate) then  |
|       | apply 0.21 %                                                        |
|       | and book to VAT deductible                                          |
|       | (return to VAT returnable)                                          |
+-------+---------------------------------------------------------------------+
| 6     | VAT rule 6:                                                         |
|       | if (Sales, Goods at normal VAT rate) then                           |
|       | apply 0.21 %                                                        |
|       | and book to VAT due                                                 |
+-------+---------------------------------------------------------------------+
| 7     | VAT rule 7:                                                         |
|       | if (Purchases, National, Goods at reduced VAT rate) then            |
|       | apply 0.07 %                                                        |
|       | and book to VAT deductible                                          |
+-------+---------------------------------------------------------------------+
| 8     | VAT rule 8:                                                         |
|       | if (Purchases, Intra-community, EU, Goods at reduced VAT rate) then |
|       | apply 0.07 %                                                        |
|       | and book to VAT deductible                                          |
|       | (return to VAT returnable)                                          |
+-------+---------------------------------------------------------------------+
| 9     | VAT rule 9:                                                         |
|       | if (Sales, Goods at reduced VAT rate) then                          |
|       | apply 0.07 %                                                        |
|       | and book to VAT due                                                 |
+-------+---------------------------------------------------------------------+
| 10    | VAT rule 10:                                                        |
|       | apply 0 %                                                           |
|       | and book to None                                                    |
+-------+---------------------------------------------------------------------+
<BLANKLINE>


VAT declaration
===============

.. class:: DeclarationFields

    The list of fields in a VAT declaration.

>>> rt.show(bevat.DeclarationFields)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
+------+------+------+-------------------------------------------------+
| Wert | name | Text | Beschreibung                                    |
+======+======+======+=================================================+
| 00   | F00  | [00] | Verkauf |br|                                    |
|      |      |      | columns 00 |br|                                 |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 01   | F01  | [01] | Verkauf |br|                                    |
|      |      |      | columns 01 |br|                                 |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 02   | F02  | [02] | Sales 12% |br|                                  |
|      |      |      | columns 02 |br|                                 |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 03   | F03  | [03] | Sales 20% |br|                                  |
|      |      |      | columns 03 |br|                                 |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 44   | F44  | [44] | Sales located inside EU |br|                    |
|      |      |      | columns 00 01 02 03 |br|                        |
|      |      |      | regimes inside |br|                             |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 45   | F45  | [45] | Vertragspartner |br|                            |
|      |      |      | columns 00 01 02 03 |br|                        |
|      |      |      | regimes cocontractor |br|                       |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 46   | F46  | [46] | Sales intracom and ABC |br|                     |
|      |      |      | columns 00 01 02 03 |br|                        |
|      |      |      | regimes intracom |br|                           |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 47   | F47  | [47] | Verkauf |br|                                    |
|      |      |      | columns 00 01 02 03 |br|                        |
|      |      |      | regimes intracom |br|                           |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 48   | F48  | [48] | CN sales 48 |br|                                |
|      |      |      | columns 00 01 02 03 |br|                        |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 49   | F49  | [49] | CN sales 49 |br|                                |
|      |      |      | columns 00 01 02 03 |br|                        |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 81   | F81  | [81] | Lebenslauf |br|                                 |
|      |      |      | columns 81 |br|                                 |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 82   | F82  | [82] | Dienstleistungen |br|                           |
|      |      |      | columns 82 |br|                                 |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 83   | F83  | [83] | Investierungen |br|                             |
|      |      |      | columns 83 |br|                                 |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 84   | F84  | [84] | CN purchases on operations in 86 and 88 |br|    |
|      |      |      | columns 81 82 83 |br|                           |
|      |      |      | regimes intracom |br|                           |
|      |      |      | MvtDeclarationField Kredit only |br|            |
+------+------+------+-------------------------------------------------+
| 85   | F85  | [85] | CN purchases on other operations |br|           |
|      |      |      | columns 81 82 83 |br|                           |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 86   | F86  | [86] | IC purchases and ABC sales |br|                 |
|      |      |      | columns 81 82 83 |br|                           |
|      |      |      | regimes intracom |br|                           |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 87   | F87  | [87] | Other purchases in Belgium |br|                 |
|      |      |      | columns 81 82 83 |br|                           |
|      |      |      | regimes cocontractor |br|                       |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 88   | F88  | [88] | IC services |br|                                |
|      |      |      | columns 81 82 83 |br|                           |
|      |      |      | regimes delayed |br|                            |
|      |      |      | MvtDeclarationField Debit |br|                  |
+------+------+------+-------------------------------------------------+
| 54   | F54  | [54] | Due VAT for 01, 02 and 03 |br|                  |
|      |      |      | columns 54 |br|                                 |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 55   | F55  | [55] | Due VAT for 86 and 88 |br|                      |
|      |      |      | columns 54 |br|                                 |
|      |      |      | regimes intracom |br|                           |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 56   | F56  | [56] | Due VAT for 87 except those covered by 57 |br|  |
|      |      |      | columns 54 |br|                                 |
|      |      |      | regimes cocontractor |br|                       |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 57   | F57  | [57] | Due VAT for 87 except those covered by 57 |br|  |
|      |      |      | columns 54 |br|                                 |
|      |      |      | regimes delayed |br|                            |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| 61   | F61  | [61] | Diverse Buchungen |br|                          |
|      |      |      | WritableDeclarationField Kredit |br|            |
+------+------+------+-------------------------------------------------+
| XX   | FXX  | [XX] | Total of due taxes |br|                         |
|      |      |      | SumDeclarationField Kredit |br|                 |
|      |      |      | Sum of F54 F55 F56 F57 |br|                     |
+------+------+------+-------------------------------------------------+
| 59   | F59  | [59] | Deductible VAT from purchase invoices |br|      |
|      |      |      | columns 59 |br|                                 |
|      |      |      | MvtDeclarationField Kredit |br|                 |
|      |      |      | Sum of F81 F82 F83 |br|                         |
+------+------+------+-------------------------------------------------+
| 62   | F62  | [62] | Diverse Buchungen |br|                          |
|      |      |      | WritableDeclarationField Kredit |br|            |
+------+------+------+-------------------------------------------------+
| 64   | F64  | [64] | VAT on sales CN |br|                            |
|      |      |      | columns 59 |br|                                 |
|      |      |      | MvtDeclarationField Kredit |br|                 |
+------+------+------+-------------------------------------------------+
| YY   | FYY  | [YY] | Total of deductible taxes |br|                  |
|      |      |      | SumDeclarationField Kredit |br|                 |
|      |      |      | Sum of F59 F62 F64 |br|                         |
+------+------+------+-------------------------------------------------+
| 72   | F72  | [72] | Total to pay (+) or to return (-) |br|          |
|      |      |      | SumDeclarationField Debit |br|                  |
|      |      |      | Sum of FXX FYY |br|                             |
+------+------+------+-------------------------------------------------+
<BLANKLINE>



External references
===================

- `165-625-directives-2016.pdf
  <https://finances.belgium.be/sites/default/files/downloads/165-625-directives-2016.pdf>`__

- `finances.belgium.be
  <https://finances.belgium.be/fr/entreprises/tva/declaration/declaration_periodique>`__
