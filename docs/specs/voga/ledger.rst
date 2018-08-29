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
 SLS         Sales invoices                  Verkaufsrechnungen        Factures vente            Sales                                                 Credit
 SLC         Sales credit notes              Gutschriften Verkauf      Sales credit notes        Sales                                                 Debit
 PRC         Purchase invoices               Einkaufsrechnungen        Factures achat            Purchases                                             Debit
 PMO         Bestbank Payment Orders         Bestbank Payment Orders   Bestbank Payment Orders   Bank payment orders   (4300) Pending Payment Orders   Debit
 CSH         Cash                            Kasse                     Caisse                                          (5700) Cash                     Credit
 BNK         Bestbank                        Bestbank                  Bestbank                                        (5500) BestBank                 Credit
 MSC         Miscellaneous Journal Entries   Diverse Buchungen         Opérations diverses                             (5700) Cash                     Credit
 VAT         VAT declarations                MwSt.-Erklärungen         Déclarations TVA          Taxes                 (4513) VAT declared             Debit
=========== =============================== ========================= ========================= ===================== =============================== ===========================
<BLANKLINE>


>>> rt.show(ledger.Accounts)
=========== ========================= =============================== ============================
 Reference   Designation               Designation (de)                Designation (fr)
----------- ------------------------- ------------------------------- ----------------------------
 1000        Net income (loss)         Net income (loss)               Net income (loss)
 4000        Customers                 Kunden                          Clients
 4300        Pending Payment Orders    Offene Zahlungsaufträge         Ordres de paiement ouverts
 4400        Suppliers                 Lieferanten                     Fournisseurs
 4500        Employees                 Angestellte                     Employés
 4510        VAT due                   Geschuldete Mehrwertsteuer      TVA dûe
 4511        VAT returnable            Rückzahlbare Mehrwertsteuer     TVA à retourner
 4512        VAT deductible            Abziehbare Mehrwertsteuer       TVA déductible
 4513        VAT declared              Deklarierte Mehrwertsteuer      TVA déclarée
 4600        Tax Offices               Steuerämter                     Tax Offices
 4900        Waiting account           Wartekonto                      Waiting account
 5500        BestBank                  BestBank                        BestBank
 5700        Cash                      Kasse                           Caisse
 6010        Purchase of services      Einkäufe von Dienstleistungen   Achats de services
 6020        Purchase of investments   Investierungskäufe              Achats d'investissement
 6040        Purchase of goods         Wareneinkäufe                   Achats de marchandises
 6300        Wages                     Löhne und Gehälter              Salaires
 6900        Net income                Net income                      Net income
 7000        Sales                     Verkauf                         Ventes
 7310        Membership fees           Membership fees                 Membership fees
 7900        Net loss                  Net loss                        Net loss
=========== ========================= =============================== ============================
<BLANKLINE>
