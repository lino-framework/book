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
=========== ========================= =============================== ============================ =================================
 Reference   Designation               Designation (de)                Designation (fr)             Account Group
----------- ------------------------- ------------------------------- ---------------------------- ---------------------------------
 4000        Customers                 Kunden                          Clients                      Commercial assets & liabilities
 4300        Pending Payment Orders    Offene Zahlungsaufträge         Ordres de paiement ouverts   Other assets & liabilities
 4400        Suppliers                 Lieferanten                     Fournisseurs                 Commercial assets & liabilities
 4510        VAT due                   Geschuldete Mehrwertsteuer      TVA dûe                      Tax office
 4511        VAT returnable            Rückzahlbare Mehrwertsteuer     TVA à retourner              Tax office
 4512        VAT deductible            Abziehbare Mehrwertsteuer       TVA déductible               Tax office
 4513        VAT declared              Deklarierte Mehrwertsteuer      TVA déclarée                 Tax office
 4600        Tax Offices               Steuerämter                     Tax Offices                  Tax office
 4900        Waiting account           Wartekonto                      Waiting account              Other assets & liabilities
 5500        BestBank                  BestBank                        BestBank                     Banks
 5700        Cash                      Kasse                           Caisse                       Banks
 6010        Purchase of services      Einkäufe von Dienstleistungen   Achats de services           Expenses
 6020        Purchase of investments   Investierungskäufe              Achats d'investissement      Expenses
 6040        Purchase of goods         Wareneinkäufe                   Achats de marchandises       Expenses
 7000        Sales                     Verkauf                         Ventes                       Revenues
 7310        Membership fees           Membership fees                 Membership fees              Revenues
=========== ========================= =============================== ============================ =================================
<BLANKLINE>
