.. doctest docs/specs/voga/ledger.rst
.. _voga.specs.ledger:

Ledger
=======

doctest init:

>>> from lino import startup
>>> startup('lino_book.projects.roger.settings.doctests')
>>> from lino.api.doctest import *


Journals
--------

>>> ses = settings.SITE.login('robin')
>>> ses.show(ledger.Journals, column_names="ref name trade_type account dc")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== ============================ ============================ ============================ ===================== =============================== ===========================
 Reference   Designation                  Designation (de)             Designation (fr)             Trade type            Account                         Primary booking direction
----------- ---------------------------- ---------------------------- ---------------------------- --------------------- ------------------------------- ---------------------------
 SLS         Sales invoices               Verkaufsrechnungen           Factures vente               Sales                                                 Credit
 SLC         Sales credit notes           Gutschriften Verkauf         Notes de crédit vente        Sales                                                 Debit
 PRC         Purchase invoices            Einkaufsrechnungen           Factures achat               Purchases                                             Debit
 PMO         Bestbank Payment Orders      Zahlungsaufträge             Ordre de paiement Bestbank   Bank payment orders   (4300) Pending Payment Orders   Credit
 CSH         Cash book                    Kassenbuch                   Livre de caisse                                    (5700) Cash                     Credit
 BNK         Bestbank                     Bestbank                     Bestbank                                           (5500) BestBank                 Credit
 MSC         Miscellaneous transactions   Miscellaneous transactions   Opérations diverses                                (5700) Cash                     Credit
 PRE         Preliminary transactions     Preliminary transactions     Preliminary transactions                           (5700) Cash                     Credit
 SAL         Paychecks                    Lohnscheine                  Fiches de paie                                     (5700) Cash                     Debit
 VAT         VAT declarations             MwSt.-Erklärungen            Déclarations TVA             Taxes                 (4513) VAT declared             Debit
=========== ============================ ============================ ============================ ===================== =============================== ===========================
<BLANKLINE>


>>> rt.show(ledger.Accounts)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
============================== =============== =========== ===========
 Description                    Needs partner   Clearable   Reference
------------------------------ --------------- ----------- -----------
 1000 Net income (loss)         Yes             Yes         1000
 4000 Customers                 Yes             Yes         4000
 4100 Suppliers                 Yes             Yes         4100
 4200 Employees                 Yes             Yes         4200
 4300 Pending Payment Orders    Yes             Yes         4300
 4500 Tax Offices               Yes             Yes         4500
 4510 VAT due                   No              No          4510
 4513 VAT declared              No              No          4513
 4520 VAT deductible            No              No          4520
 4530 VAT returnable            No              No          4530
 4800 Internal clearings        Yes             Yes         4800
 4900 Waiting account           Yes             Yes         4900
 5500 BestBank                  No              No          5500
 5700 Cash                      No              No          5700
 6010 Purchase of services      No              No          6010
 6020 Purchase of investments   No              No          6020
 6040 Purchase of goods         No              No          6040
 6300 Wages                     No              No          6300
 6900 Net income                No              No          6900
 7000 Sales                     No              No          7000
 7310 Membership fees           Yes             No          7310
============================== =============== =========== ===========
<BLANKLINE>
