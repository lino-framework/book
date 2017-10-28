.. _voga.specs.ledger:

Ledger
=======

.. how to test just this document:

    $ doctest docs/specs/voga/ledger.rst

    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *


Journals
--------

>>> ses = settings.SITE.login('robin')
>>> ses.show(ledger.Journals, column_names="ref name trade_type account dc")
=========== =============================== ========================= ========================= ===================== =============================== ===========================
 Reference   Designation                     Designation (de)          Designation (fr)          Trade type            Account                         Primary booking direction
----------- ------------------------------- ------------------------- ------------------------- --------------------- ------------------------------- ---------------------------
 SLS         Sales invoices                  Verkaufsrechnungen        Factures vente            Sales                                                 Debit
 SLC         Sales credit notes              Gutschriften Verkauf      Sales credit notes        Sales                                                 Credit
 PRC         Purchase invoices               Einkaufsrechnungen        Factures achat            Purchases                                             Credit
 PMO         Bestbank Payment Orders         Bestbank Payment Orders   Bestbank Payment Orders   Bank payment orders   (4300) Pending Payment Orders   Credit
 CSH         Cash                            Kasse                     Caisse                                          (5700) Cash                     Debit
 BNK         Bestbank                        Bestbank                  Bestbank                                        (5500) BestBank                 Debit
 MSC         Miscellaneous Journal Entries   Diverse Buchungen         Opérations diverses                             (5700) Cash                     Debit
 VAT         VAT declarations                MwSt.-Erklärungen         Déclarations TVA          Taxes                 (4513) VAT declared             Credit
=========== =============================== ========================= ========================= ===================== =============================== ===========================
<BLANKLINE>


>>> rt.show(accounts.Accounts)
=========== ========================= =============================== ========================= ==========================
 Reference   Designation               Designation (de)                Designation (fr)          Account Group
----------- ------------------------- ------------------------------- ------------------------- --------------------------
 4000        Customers                 Kunden                          Customers                 Commercial receivable(?)
 4300        Pending Payment Orders    Offene Zahlungsaufträge         Pending Payment Orders    Commercial receivable(?)
 4400        Suppliers                 Lieferanten                     Suppliers                 Commercial receivable(?)
 4510        VAT due                   Geschuldete Mehrwertsteuer      VAT due                   VAT to pay
 4511        VAT returnable            Rückzahlbare Mehrwertsteuer     VAT returnable            VAT to pay
 4512        VAT deductible            Abziehbare Mehrwertsteuer       VAT deductible            VAT to pay
 4513        VAT declared              Deklarierte Mehrwertsteuer      VAT declared              Commercial receivable(?)
 4600        Tax Offices               Steuerämter                     Tax Offices               Commercial receivable(?)
 5500        BestBank                  BestBank                        BestBank                  Banks
 5700        Cash                      Kasse                           Caisse                    Banks
 6010        Purchase of services      Einkäufe von Dienstleistungen   Purchase of services      Expenses
 6020        Purchase of investments   Investierungskäufe              Purchase of investments   Expenses
 6040        Purchase of goods         Wareneinkäufe                   Purchase of goods         Expenses
 7000        Sales                     Verkauf                         Sales                     Revenues
 7310        Membership fees           Membership fees                 Membership fees           Revenues
=========== ========================= =============================== ========================= ==========================
<BLANKLINE>

