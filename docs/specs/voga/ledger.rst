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
=========== ============================ ============================ ============================ ===================== =============================== ===========================
 Reference   Designation                  Designation (de)             Designation (fr)             Trade type            Account                         Primary booking direction
----------- ---------------------------- ---------------------------- ---------------------------- --------------------- ------------------------------- ---------------------------
 SLS         Sales invoices               Verkaufsrechnungen           Factures vente               Sales                                                 Credit
 SLC         Sales credit notes           Gutschriften Verkauf         Sales credit notes           Sales                                                 Debit
 PRC         Purchase invoices            Einkaufsrechnungen           Factures achat               Purchases                                             Debit
 PMO         Bestbank Payment Orders      Bestbank Payment Orders      Bestbank Payment Orders      Bank payment orders   (4300) Pending Payment Orders   Debit
 CSH         Cash                         Kasse                        Caisse                                             (5700) Cash                     Credit
 BNK         Bestbank                     Bestbank                     Bestbank                                           (5500) BestBank                 Credit
 MSC         Miscellaneous transactions   Miscellaneous transactions   Miscellaneous transactions                         (5700) Cash                     Credit
 SAL         Salaries                     Salaries                     Salaries                                           (5700) Cash                     Credit
 VAT         VAT declarations             MwSt.-Erklärungen            Déclarations TVA             Taxes                 (4513) VAT declared             Debit
=========== ============================ ============================ ============================ ===================== =============================== ===========================
<BLANKLINE>


>>> rt.show(ledger.Accounts)
======================================= =============== =========== ===========
 Description                             Needs partner   Clearable   Reference
--------------------------------------- --------------- ----------- -----------
 1000 Net income (loss)                  Yes             Yes         1000
 **4 Commercial assets & liabilities**   No              No          4
 4000 Customers                          Yes             Yes         4000
 4300 Pending Payment Orders             Yes             Yes         4300
 4400 Suppliers                          Yes             Yes         4400
 4500 Employees                          Yes             Yes         4500
 4510 VAT due                            No              No          4510
 4511 VAT returnable                     No              No          4511
 4512 VAT deductible                     No              No          4512
 4513 VAT declared                       No              No          4513
 4550 Internal clearings                 Yes             Yes         4550
 4600 Tax Offices                        Yes             Yes         4600
 4900 Waiting account                    Yes             Yes         4900
 **5 Financial assets & liabilities**    No              No          5
 5500 BestBank                           No              No          5500
 5700 Cash                               No              No          5700
 **6 Expenses**                          No              No          6
 ** 60 Operation costs**                 No              No          60
 6010 Purchase of services               No              No          6010
 6020 Purchase of investments            No              No          6020
 6040 Purchase of goods                  No              No          6040
 ** 61 Wages**                           No              No          61
 6300 Wages                              No              No          6300
 6900 Net income                         No              No          6900
 **7 Revenues**                          No              No          7
 7000 Sales                              No              No          7000
 7310 Membership fees                    Yes             No          7310
 7900 Net loss                           No              No          7900
======================================= =============== =========== ===========
<BLANKLINE>
