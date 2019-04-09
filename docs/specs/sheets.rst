.. doctest docs/specs/sheets.rst
.. _xl.specs.sheets:

===============================================
``sheets`` : Balance sheet and Income statement
===============================================

.. currentmodule:: lino_xl.lib.sheets
                   
The :mod:`lino_xl.lib.sheets` plugin adds an annual financial report: three
types of account balances (general, partner and analytical) as well as the
*Balance sheet* and the *Income statement*.

You should have read :doc:`ledger` before reading this document.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.demo')
>>> from lino.api.doctest import *
>>> ses = rt.login("robin")
>>> translation.activate('en')
>>> from lino_xl.lib.ledger.utils import DCLABELS




.. class:: SheetTypes
           
    The global list of **sheet types** . 

    >>> rt.show(sheets.SheetTypes, language="en")
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    ======= ========= ==================
     value   name      text
    ------- --------- ------------------
     B       balance   Balance sheet
     R       results   Income statement
    ======= ========= ==================
    <BLANKLINE>

    .. attribute:: balance

        A **balance sheet** or *statement of financial position* is a
        summary of the financial balances of an organisation.

        Assets, liabilities and ownership equity are listed as of a
        specific date, such as the end of its financial year.  A balance
        sheet is often described as a "snapshot of a company's financial
        condition".  Of the four basic financial statements, the balance
        sheet is the only statement which applies to a single point in
        time of a business' calendar year.

        A standard company balance sheet has three parts: assets,
        liabilities and ownership equity. The main categories of assets
        are usually listed first, and typically in order of
        liquidity. Assets are followed by the liabilities. The difference
        between the assets and the liabilities is known as equity or the
        net assets or the net worth or capital of the company and
        according to the accounting equation, net worth must equal assets
        minus liabilities.

        https://en.wikipedia.org/wiki/Balance_sheet

    .. attribute:: results
           
        https://en.wikipedia.org/wiki/Statement_of_comprehensive_income#Requirements_of_IFRS
           
    
.. class:: CommonItems

    The global list of **common sheet items** . 

    >>> rt.show(sheets.CommonItems, language="en")
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    ======= ================= =========================== ================== ======== ==================================
     value   name              text                        Sheet type         D/C      Sheet item
    ------- ----------------- --------------------------- ------------------ -------- ----------------------------------
     1       assets            Assets                      Balance sheet      Debit    (1) Assets
     10                        Current assets              Balance sheet      Debit    (10) Current assets
     1000    customers         Customers receivable        Balance sheet      Debit    (1000) Customers receivable
     1010                      Taxes receivable            Balance sheet      Debit    (1010) Taxes receivable
     1020                      Cash and cash equivalents   Balance sheet      Debit    (1020) Cash and cash equivalents
     1030                      Current transfers           Balance sheet      Debit    (1030) Current transfers
     1090                      Other current assets        Balance sheet      Debit    (1090) Other current assets
     11                        Non-current assets          Balance sheet      Debit    (11) Non-current assets
     2       passiva           Passiva                     Balance sheet      Credit   (2) Passiva
     20      liabilities       Liabilities                 Balance sheet      Credit   (20) Liabilities
     2000    suppliers         Suppliers payable           Balance sheet      Credit   (2000) Suppliers payable
     2010    taxes             Taxes payable               Balance sheet      Credit   (2010) Taxes payable
     2020    banks             Banks                       Balance sheet      Credit   (2020) Banks
     2030    transfers         Current transfers           Balance sheet      Credit   (2030) Current transfers
     2090    other             Other liabilities           Balance sheet      Credit   (2090) Other liabilities
     21      capital           Own capital                 Balance sheet      Credit   (21) Own capital
     2150    net_income_loss   Net income (loss)           Balance sheet      Credit   (2150) Net income (loss)
     6       expenses          Expenses                    Income statement   Debit    (6) Expenses
     6000    costofsales       Cost of sales               Income statement   Debit    (6000) Cost of sales
     6100    operating         Operating expenses          Income statement   Debit    (6100) Operating expenses
     6200    otherexpenses     Other expenses              Income statement   Debit    (6200) Other expenses
     6900    net_income        Net income                  Income statement   Debit    (6900) Net income
     7       revenues          Revenues                    Income statement   Credit   (7) Revenues
     7000    sales             Net sales                   Income statement   Credit   (7000) Net sales
     7900    net_loss          Net loss                    Income statement   Credit   (7900) Net loss
    ======= ================= =========================== ================== ======== ==================================
    <BLANKLINE>
    

    Every item of this list is an instance of :class:`CommonItem`.

.. class:: CommonItem

    .. attribute:: value
                   
         Corresponds to the :attr:`ref` field in :class:`Item`
         
    .. attribute:: dc
    .. attribute:: sheet

    
.. class:: Item

    In this table the uer can configure their local list of items for
    both sheet types.
           
    >>> rt.show(sheets.Items, language="en")
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    =========== =========================== =========================== =========================== ================== =================== ===========================
     Reference   Designation                 Designation (de)            Designation (fr)            Sheet type         Booking direction   Common sheet item
    ----------- --------------------------- --------------------------- --------------------------- ------------------ ------------------- ---------------------------
     1           Assets                      Vermögen                    Actifs                      Balance sheet      Debit               Assets
     10          Current assets              Current assets              Current assets              Balance sheet      Debit               Current assets
     1000        Customers receivable        Customers receivable        Customers receivable        Balance sheet      Debit               Customers receivable
     1010        Taxes receivable            Taxes receivable            Taxes receivable            Balance sheet      Debit               Taxes receivable
     1020        Cash and cash equivalents   Cash and cash equivalents   Cash and cash equivalents   Balance sheet      Debit               Cash and cash equivalents
     1030        Current transfers           Current transfers           Current transfers           Balance sheet      Debit               Current transfers
     1090        Other current assets        Other current assets        Other current assets        Balance sheet      Debit               Other current assets
     11          Non-current assets          Non-current assets          Non-current assets          Balance sheet      Debit               Non-current assets
     2           Passiva                     Passiva                     Passiva                     Balance sheet      Credit              Passiva
     20          Liabilities                 Verpflichtungen             Passifs                     Balance sheet      Credit              Liabilities
     2000        Suppliers payable           Suppliers payable           Suppliers payable           Balance sheet      Credit              Suppliers payable
     2010        Taxes payable               Taxes payable               Taxes payable               Balance sheet      Credit              Taxes payable
     2020        Banks                       Banks                       Banks                       Balance sheet      Credit              Banks
     2030        Current transfers           Current transfers           Current transfers           Balance sheet      Credit              Current transfers
     2090        Other liabilities           Other liabilities           Other liabilities           Balance sheet      Credit              Other liabilities
     21          Own capital                 Own capital                 Own capital                 Balance sheet      Credit              Own capital
     2150        Net income (loss)           Net income (loss)           Net income (loss)           Balance sheet      Credit              Net income (loss)
     6           Expenses                    Ausgaben                    Dépenses                    Income statement   Debit               Expenses
     6000        Cost of sales               Cost of sales               Cost of sales               Income statement   Debit               Cost of sales
     6100        Operating expenses          Operating expenses          Operating expenses          Income statement   Debit               Operating expenses
     6200        Other expenses              Other expenses              Other expenses              Income statement   Debit               Other expenses
     6900        Net income                  Net income                  Net income                  Income statement   Debit               Net income
     7           Revenues                    Revenues                    Revenues                    Income statement   Credit              Revenues
     7000        Net sales                   Net sales                   Net sales                   Income statement   Credit              Net sales
     7900        Net loss                    Net loss                    Net loss                    Income statement   Credit              Net loss
    =========== =========================== =========================== =========================== ================== =================== ===========================
    <BLANKLINE>
    

    In the demo database this list is an unchanged copy of :class:`CommonItems`.

The Accounting Report
=====================
    
.. class:: Report
.. class:: AccountEntry
.. class:: PartnerEntry
.. class:: AnaAccountEntry
.. class:: ItemEntry

    An **entry** is the computed value of given *item* for a given
    report.
    
>>> rpt = sheets.Report.objects.get(pk=1)
>>> rt.show(sheets.ItemEntriesByReport, rpt)
=========================== ============== =============== =========== =========== ============== =============
 Description                 Debit before   Credit before   Debit       Credit      Credit after   Debit after
--------------------------- -------------- --------------- ----------- ----------- -------------- -------------
 **1 Assets**                                               13 195,76   10 361,07                  2 834,69
 ** 10 Current assets**                                     13 195,76   10 361,07                  2 834,69
 1000 Customers receivable                                  13 195,76   10 361,07                  2 834,69
 **2 Passiva**                                              30 393,54   55 597,39   25 203,85
 ** 20 Liabilities**                                        30 393,54   55 597,39   25 203,85
 2000 Suppliers payable                                     22 044,44   27 556,94   5 512,50
 2010 Taxes payable                                         3 514,10    475,70                     3 038,40
 2020 Banks                                                             5 520,31    5 520,31
 2030 Current transfers                                     4 835,00    22 044,44   17 209,44
 **6 Expenses**                                             24 518,54                              24 518,54
 6000 Cost of sales                                         6 714,00                               6 714,00
 6100 Operating expenses                                    14 668,19                              14 668,19
 6200 Other expenses                                        3 136,35                               3 136,35
 **7 Revenues**                                             480,00      13 670,00   13 190,00
 7000 Net sales                                             480,00      13 670,00   13 190,00
=========================== ============== =============== =========== =========== ============== =============
<BLANKLINE>



>>> ses = rt.login("robin")
>>> ses.show_story(rpt.get_story(ses))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======================================= ============== =============== =========== =========== ============== =============
 Description                             Debit before   Credit before   Debit       Credit      Credit after   Debit after
--------------------------------------- -------------- --------------- ----------- ----------- -------------- -------------
 **4 Commercial assets & liabilities**                                  43 589,30   60 438,15   16 848,85
 4000 Customers                                                         13 195,76   10 361,07                  2 834,69
 4300 Pending Payment Orders                                            4 835,00    22 044,44   17 209,44
 4400 Suppliers                                                         22 044,44   27 556,94   5 512,50
 4510 VAT due                                                           178,24      297,46      119,22
 4512 VAT deductible                                                    3 335,86                               3 335,86
 4600 Tax Offices                                                                   178,24      178,24
 **5 Financial assets & liabilities**                                               5 520,31    5 520,31
 5500 BestBank                                                                      5 520,31    5 520,31
 **6 Expenses**                                                         24 518,54                              24 518,54
 ** 60 Operation costs**                                                24 518,54                              24 518,54
 6010 Purchase of services                                              14 668,19                              14 668,19
 6020 Purchase of investments                                           3 136,35                               3 136,35
 6040 Purchase of goods                                                 6 714,00                               6 714,00
 **7 Revenues**                                                         480,00      13 670,00   13 190,00
 7000 Sales                                                             480,00      2 730,00    2 250,00
 7010 Sales on therapies                                                            10 940,00   10 940,00
======================================= ============== =============== =========== =========== ============== =============
<BLANKLINE>
============================ ============== =============== ========== ======== ============== =============
 Description                  Debit before   Credit before   Debit      Credit   Credit after   Debit after
---------------------------- -------------- --------------- ---------- -------- -------------- -------------
 **1 Operation costs**                                       5 578,62                           5 578,62
 1100 Wages                                                  490,10                             490,10
 1200 Transport                                              1 421,70                           1 421,70
 1300 Training                                               3 093,54                           3 093,54
 1400 Other costs                                            573,28                             573,28
 **2 Administrative costs**                                  9 175,90                           9 175,90
 2100 Secretary wages                                        1 659,56                           1 659,56
 2110 Manager wages                                          4 004,11                           4 004,11
 2200 Transport                                              3 044,86                           3 044,86
 2300 Training                                               467,37                             467,37
 **3 Investments**                                           1 404,50                           1 404,50
 3000 Investment                                             1 404,50                           1 404,50
 **4 Project 1**                                             3 843,84                           3 843,84
 4100 Wages                                                  3 013,68                           3 013,68
 4200 Transport                                              398,17                             398,17
 4300 Training                                               431,99                             431,99
 **5 Project 2**                                             4 515,68                           4 515,68
 5100 Wages                                                  1 342,80                           1 342,80
 5200 Transport                                              2 927,99                           2 927,99
 5300 Other costs                                            244,89                             244,89
============================ ============== =============== ========== ======== ============== =============
<BLANKLINE>
==================================================== ============== =============== ======== ======== ============== =============
 Description                                          Debit before   Credit before   Debit    Credit   Credit after   Debit after
---------------------------------------------------- -------------- --------------- -------- -------- -------------- -------------
 `Mr Hans Altenberg <Detail>`__                                                      925,00   925,00
 `Mr Andreas Arens <Detail>`__                                                       180,00   180,00
 `Mrs Annette Arens <Detail>`__                                                      750,00   290,00                  460,00
 `Mr Alfons Ausdemwald <Detail>`__                                                   460,00   346,00                  114,00
 `Auto École Verte <Detail>`__                                                       500,00   500,00
 `Mr Laurent Bastiaensen <Detail>`__                                                 550,00   559,40   9,40
 `Bernd Brechts Bücherladen <Detail>`__                                              620,00   620,00
 `Bäckerei Ausdemwald <Detail>`__                                                    360,00   360,00
 `Bäckerei Mießen <Detail>`__                                                        440,00   440,00
 `Bäckerei Schmitz <Detail>`__                                                       160,00   160,00
 `Mr Marc Chantraine <Detail>`__                                                     830,00   180,00                  650,00
 `Mrs Ulrike Charlier <Detail>`__                                                    660,00   180,00                  480,00
 `Mrs Charlotte Collard <Detail>`__                                                  480,00   180,00                  300,00
 `Mrs Dorothée Demeulenaere <Detail>`__                                              960,50   280,50                  680,00
 `Mr Denis Denon <Detail>`__                                                         543,60   543,60
 `Mr Daniel Dericum <Detail>`__                                                      160,00                           160,00
 `Mrs Dorothée Dobbelstein-Demeulenaere <Detail>`__                                  180,60   180,60
 `Donderweer BV <Detail>`__                                                          320,00   320,00
 `Mr Erich Emonts <Detail>`__                                                        85,00    85,00
 `Mr Erwin Emontspool <Detail>`__                                                    210,00   210,00
 `Garage Mergelsberg <Detail>`__                                                     605,00   605,00
 `Mr Gregory Groteclaes <Detail>`__                                                  100,00   100,00
 `Hans Flott & Co <Detail>`__                                                        350,00   350,00
 `Mr Henri Hilgers <Detail>`__                                                       180,36   180,36
 `Mr Josef Jonas <Detail>`__                                                         80,70    80,70
 `Mr Karl Kaivers <Detail>`__                                                        180,00   180,00
 `Mr Marc Malmendier <Detail>`__                                                     100,00   99,91                   0,09
 `Mr Mark Martelaer <Detail>`__                                                      210,00   210,00
 `Moulin Rouge <Detail>`__                                                           450,00   450,00
 `Mrs Daniela Radermacher <Detail>`__                                                95,00    95,00
 `Mr Edgard Radermacher <Detail>`__                                                  180,00   180,00
 `Mr Rik Radermecker <Detail>`__                                                     80,00    80,00
 `Reinhards Baumschule <Detail>`__                                                   280,00   280,00
 `Rumma & Ko OÜ <Detail>`__                                                          450,00   450,00
 `Van Achter NV <Detail>`__                                                          300,00   300,00
 `Mr David da Vinci <Detail>`__                                                      180,00   180,00
==================================================== ============== =============== ======== ======== ============== =============
<BLANKLINE>
================================== ============== =============== =========== =========== ============== =============
 Description                        Debit before   Credit before   Debit       Credit      Credit after   Debit after
---------------------------------- -------------- --------------- ----------- ----------- -------------- -------------
 `Bäckerei Ausdemwald <Detail>`__                                  568,80      709,00      140,20
 `Bäckerei Mießen <Detail>`__                                      2 407,80    3 010,00    602,20
 `Bäckerei Schmitz <Detail>`__                                     4 802,60    6 005,00    1 202,40
 `Donderweer BV <Detail>`__                                        468,61      585,96      117,35
 `Garage Mergelsberg <Detail>`__                                   12 970,32   16 210,90   3 240,58
 `Rumma & Ko OÜ <Detail>`__                                        163,00      205,50      42,50
 `Van Achter NV <Detail>`__                                        663,31      830,58      167,27
================================== ============== =============== =========== =========== ============== =============
<BLANKLINE>
No data to display
=============================================== ============== =============== ======= ======== ============== =============
 Description                                     Debit before   Credit before   Debit   Credit   Credit after   Debit after
----------------------------------------------- -------------- --------------- ------- -------- -------------- -------------
 `Mehrwertsteuer-Kontrollamt Eupen <Detail>`__                                          178,24   178,24
=============================================== ============== =============== ======= ======== ============== =============
<BLANKLINE>
No data to display
No data to display
=========================== =========== ==========
 Description                 Activa      Passiva
--------------------------- ----------- ----------
 **1 Assets**                            2 834,69
 ** 10 Current assets**                  2 834,69
 1000 Customers receivable               2 834,69
 **2 Passiva**               25 203,85
 ** 20 Liabilities**         25 203,85
 2000 Suppliers payable      5 512,50
 2010 Taxes payable
 2020 Banks                  5 520,31
 2030 Current transfers      17 209,44
=========================== =========== ==========
<BLANKLINE>
========================= =========== ===========
 Description               Expenses    Revenues
------------------------- ----------- -----------
 **6 Expenses**            24 518,54
 6000 Cost of sales        6 714,00
 6100 Operating expenses   14 668,19
 6200 Other expenses       3 136,35
 **7 Revenues**                        13 190,00
 7000 Net sales                        13 190,00
========================= =========== ===========
<BLANKLINE>






TODO: merge column headers "Debit before" and "Credit before" etc.


The Accounting Equation
=======================

The basic `Accounting Equation
<https://en.wikipedia.org/wiki/Accounting_equation>`_ states:

  Assets = Liabilities + Capital
 
And the expanded accounting equation is:

    Assets + Expenses = Liabilities + Equity + Revenue

>>> rpt = sheets.Report.objects.get(pk=1)
>>> def val(ci):
...     try:
...         e = sheets.ItemEntry.objects.get(report=rpt, item=ci.get_object())
...     except sheets.ItemEntry.DoesNotExist:
...         return 0
...     return e.new_balance().value(e.item.dc)

TODO: the following tests are skipped, we must first automatically generate the
profit/loss booking so that the expenses and revenues are balanced.

>>> assets = val(sheets.CommonItems.assets)
>>> liabilities = val(sheets.CommonItems.liabilities)
>>> capital = val(sheets.CommonItems.capital)
>>> passiva = val(sheets.CommonItems.passiva)
>>> expenses = val(sheets.CommonItems.expenses)
>>> revenues = val(sheets.CommonItems.revenues)

>>> print(assets)
2834.69
>>> print(liabilities)
25203.85
>>> print(capital)  #doctest: +SKIP
-9354.40
>>> print(liabilities+capital)  #doctest: +SKIP
13836.75
>>> print(passiva)  #doctest: +SKIP
13836.75
>>> print(expenses)
24518.54
>>> print(revenues)  #doctest: +SKIP
24518.54
    
Accounts on the left side of the equation (Assets and Expenses) are
normally DEBITed and have DEBIT balances.  That's what the :attr:`dc
<CommonItem.dc>` attribute means:

>>> translation.activate('en')

>>> print(DCLABELS[sheets.CommonItems.assets.dc])
Debit
>>> print(DCLABELS[sheets.CommonItems.expenses.dc])
Debit

`Wikipedia <http://en.wikipedia.org/wiki/Debits_and_credits>`_ gives a
Summary table of standard increasing and decreasing attributes for the
five accounting elements:

============= ===== ======
ACCOUNT TYPE  DEBIT CREDIT
============= ===== ======
Asset         \+    \−
Liability     \−    \+
Income        \−    \+
Expense       \+    \−
Equity        \−     \+      
============= ===== ======
  
The equivalent in Lino is:

>>> for t in sheets.CommonItems.get_list_items():
... #doctest: +NORMALIZE_WHITESPACE
...   if len(t.value) <= 2:
...     print("%-2s|%-15s|%-6s" % (t.value, t, DCLABELS[t.dc]))
1 |Assets         |Debit 
10|Current assets |Debit 
11|Non-current assets|Debit 
2 |Passiva        |Credit
20|Liabilities    |Credit
21|Own capital    |Credit
6 |Expenses       |Debit 
7 |Revenues       |Credit
      


TODO
====

- The Belgian and French `PCMN
  <https://en.wikipedia.org/wiki/French_generally_accepted_accounting_principles>`__
  has 7+1 top-level accounts:

    | CLASSE 0 : Droits & engagements hors bilan
    | CLASSE 1 : Fonds propres, provisions pour risques & charges et Dettes à plus d'un an
    | CLASSE 2 : Frais d'établissement, actifs immobilisés et créances à plus d'un an

  | CLASSE 3 : Stock & commandes en cours d'exécution
    | CLASSE 4 : Créances et dettes à un an au plus
    | CLASSE 5 : Placements de trésorerie et valeurs disponibles
    | CLASSE 6 : Charges
    | CLASSE 7 : Produits
    
  explain the differences and how to solve this.
  
  See also 

  - http://code.gnucash.org/docs/help/acct-types.html
  - http://www.futureaccountant.com/accounting-process/study-notes/financial-accounting-account-types.php
  

- A Liability is Capital acquired from others. 
  Both together is what French accountants call *passif*.
  
  The accounting equation "Assets = Liabilities + Capital" 
  in French is simply:

      Actif = Passif
      
  I found an excellent definition of these two terms at 
  `plancomptable.com <http://www.plancomptable.com/titre-II/titre-II.htm>`_:

  - Un actif est un élément identifiable du patrimoine ayant une 
    valeur économique positive pour l’entité, c’est-à-dire un élément 
    générant une ressource que l’entité contrôle du fait d’événements 
    passés et dont elle attend des avantages économiques futurs.
  
  - Un passif est un élément du patrimoine ayant une valeur 
    économique négative pour l'entité, c'est-à-dire une obligation de 
    l'entité à l'égard d'un tiers dont il est probable ou certain 
    qu'elle provoquera une sortie des ressources au bénéfice de ce 
    tiers, sans contrepartie au moins équivalente attendue de celui-ci. 
  

Some vocabulary

- Provisions pour risques et charges : Gesetzliche Rücklagen.
- Créances et dettes : Kredite, Anleihen, Schulden.

The template of the report
==========================

.. xfile:: ledger/Report/default.weasy.html

   Uses the method :meth:`ar.show_story
   <lino.core.requests.BaseRequest.show_story>`

Don't read me
=============


>>> th = rt.models.sheets.ItemEntriesByReport.get_handle()
>>> th  #doctest: +ELLIPSIS
<lino.core.tables.TableHandle object at ...>

>>> ll = th.get_list_layout()
>>> ll.layout._datasource is rt.models.sheets.ItemEntriesByReport
True

>>> cols = th.get_columns()
>>> el = cols[0]
>>> print(el.field.name)
description
>>> print(el.name)
description
>>> print(el.width)
40
>>> el.preferred_width
30

>>> th = rt.models.sheets.Items.get_handle()
>>> cols = th.get_columns()
>>> el = cols[0]
>>> print(el.field.name)
ref
>>> print(el.width)
4
>>> el.preferred_width
21

TODO: the preferred_width of the ref field should be 4, not 21.
It is a :class:`lino.mixins.ref.StructuredReferrable`
with :attr:`ref_max_length` set to 4.
