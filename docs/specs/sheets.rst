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
     7           Revenues                    Einnahmen                   Revenues                    Income statement   Credit              Revenues
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
 **1 Assets**                                               21 072,13   18 718,13                  2 354,00
 ** 10 Current assets**                                     21 072,13   18 718,13                  2 354,00
 1000 Customers receivable                                  21 072,13   18 718,13                  2 354,00
 **2 Passiva**                                              45 566,00   55 718,39   10 152,39
 ** 20 Liabilities**                                        45 566,00   55 718,39   10 152,39
 2000 Suppliers payable                                     22 282,12   27 854,40   5 572,28
 2010 Taxes payable                                         3 551,55    575,62                     2 975,93
 2020 Banks                                                 3 021,29    5 006,25    1 984,96
 2030 Current transfers                                     16 711,04   22 282,12   5 571,08
 **6 Expenses**                                             24 878,47                              24 878,47
 6000 Cost of sales                                         6 777,94                               6 777,94
 6100 Operating expenses                                    14 753,13                              14 753,13
 6200 Other expenses                                        3 347,40                               3 347,40
 **7 Revenues**                                             1 440,00    22 490,00   21 050,00
 7000 Net sales                                             1 440,00    22 490,00   21 050,00
=========================== ============== =============== =========== =========== ============== =============
<BLANKLINE>



>>> ses = rt.login("robin")
>>> ses.show_story(rpt.get_story(ses))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======================================= ============== =============== =========== =========== ============== =============
 Description                             Debit before   Credit before   Debit       Credit      Credit after   Debit after
--------------------------------------- -------------- --------------- ----------- ----------- -------------- -------------
 **4 Commercial assets & liabilities**                                  63 616,84   69 430,27   5 813,43
 4000 Customers                                                         21 072,13   18 718,13                  2 354,00
 4300 Pending Payment Orders                                            16 711,04   22 282,12   5 571,08
 4400 Suppliers                                                         22 282,12   27 854,40   5 572,28
 4510 VAT due                                                           215,69      359,93      144,24
 4512 VAT deductible                                                    3 335,86                               3 335,86
 4600 Tax Offices                                                                   215,69      215,69
 **5 Financial assets & liabilities**                                   3 021,29    5 006,25    1 984,96
 5500 BestBank                                                          3 021,29    5 006,25    1 984,96
 **6 Expenses**                                                         24 878,47                              24 878,47
 ** 60 Operation costs**                                                24 878,47                              24 878,47
 6010 Purchase of services                                              14 753,13                              14 753,13
 6020 Purchase of investments                                           3 347,40                               3 347,40
 6040 Purchase of goods                                                 6 777,94                               6 777,94
 **7 Revenues**                                                         1 440,00    22 490,00   21 050,00
 7000 Sales                                                             1 440,00    2 730,00    1 290,00
 7010 Sales on therapies                                                            19 760,00   19 760,00
======================================= ============== =============== =========== =========== ============== =============
<BLANKLINE>
============================ ============== =============== ========== ======== ============== =============
 Description                  Debit before   Credit before   Debit      Credit   Credit after   Debit after
---------------------------- -------------- --------------- ---------- -------- -------------- -------------
 **1 Operation costs**                                       5 650,27                           5 650,27
 1100 Wages                                                  502,66                             502,66
 1200 Transport                                              1 438,58                           1 438,58
 1300 Training                                               3 135,75                           3 135,75
 1400 Other costs                                            573,28                             573,28
 **2 Administrative costs**                                  9 260,64                           9 260,64
 2100 Secretary wages                                        1 672,64                           1 672,64
 2110 Manager wages                                          4 020,87                           4 020,87
 2200 Transport                                              3 086,97                           3 086,97
 2300 Training                                               480,16                             480,16
 **3 Investments**                                           1 434,36                           1 434,36
 3000 Investment                                             1 434,36                           1 434,36
 **4 Project 1**                                             3 958,28                           3 958,28
 4100 Wages                                                  3 073,46                           3 073,46
 4200 Transport                                              440,15                             440,15
 4300 Training                                               444,67                             444,67
 **5 Project 2**                                             4 574,92                           4 574,92
 5100 Wages                                                  1 359,79                           1 359,79
 5200 Transport                                              2 970,24                           2 970,24
 5300 Other costs                                            244,89                             244,89
============================ ============== =============== ========== ======== ============== =============
<BLANKLINE>
==================================================== ============== =============== ========== ========== ============== =============
 Description                                          Debit before   Credit before   Debit      Credit     Credit after   Debit after
---------------------------------------------------- -------------- --------------- ---------- ---------- -------------- -------------
 `Mr Hans Altenberg <Detail>`__                                                      1 085,40   1 085,40
 `Mr Andreas Arens <Detail>`__                                                       540,00     540,00
 `Mrs Annette Arens <Detail>`__                                                      1 330,00   1 307,00                  23,00
 `Mr Alfons Ausdemwald <Detail>`__                                                   620,38     620,38
 `Auto École Verte <Detail>`__                                                       500,00     500,00
 `Mr Laurent Bastiaensen <Detail>`__                                                 711,20     711,20
 `Bernd Brechts Bücherladen <Detail>`__                                              620,00     620,00
 `Bäckerei Ausdemwald <Detail>`__                                                    360,00     360,00
 `Bäckerei Mießen <Detail>`__                                                        440,00     440,00
 `Bäckerei Schmitz <Detail>`__                                                       160,00     160,00
 `Mr Marc Chantraine <Detail>`__                                                     1 190,00   540,00                    650,00
 `Mrs Ulrike Charlier <Detail>`__                                                    1 020,60   540,60                    480,00
 `Mrs Charlotte Collard <Detail>`__                                                  840,00     540,00                    300,00
 `Mrs Dorothée Demeulenaere <Detail>`__                                              1 524,30   844,30                    680,00
 `Mr Denis Denon <Detail>`__                                                         1 621,20   1 621,20
 `Mr Daniel Dericum <Detail>`__                                                      160,00                               160,00
 `Mrs Dorothée Dobbelstein-Demeulenaere <Detail>`__                                  540,00     538,50                    1,50
 `Donderweer BV <Detail>`__                                                          320,00     320,00
 `Mr Erich Emonts <Detail>`__                                                        255,10     255,10
 `Mr Erwin Emontspool <Detail>`__                                                    630,00     570,00                    60,00
 `Garage Mergelsberg <Detail>`__                                                     605,00     605,00
 `Mr Gregory Groteclaes <Detail>`__                                                  301,10     301,10
 `Hans Flott & Co <Detail>`__                                                        357,00     357,00
 `Mr Henri Hilgers <Detail>`__                                                       540,00     540,00
 `Mr Josef Jonas <Detail>`__                                                         240,70     240,45                    0,25
 `Mr Karl Kaivers <Detail>`__                                                        541,20     541,20
 `Mr Marc Malmendier <Detail>`__                                                     300,00     300,00
 `Mr Mark Martelaer <Detail>`__                                                      630,00     631,20     1,20
 `Moulin Rouge <Detail>`__                                                           450,00     450,00
 `Mrs Daniela Radermacher <Detail>`__                                                286,21     286,21
 `Mr Edgard Radermacher <Detail>`__                                                  540,84     541,20     0,36
 `Mr Rik Radermecker <Detail>`__                                                     240,70     240,70
 `Reinhards Baumschule <Detail>`__                                                   280,00     280,00
 `Rumma & Ko OÜ <Detail>`__                                                          450,00     450,00
 `Van Achter NV <Detail>`__                                                          300,00     300,09     0,09
 `Mr David da Vinci <Detail>`__                                                      541,20     540,30                    0,90
==================================================== ============== =============== ========== ========== ============== =============
<BLANKLINE>
================================== ============== =============== =========== =========== ============== =============
 Description                        Debit before   Credit before   Debit       Credit      Credit after   Debit after
---------------------------------- -------------- --------------- ----------- ----------- -------------- -------------
 `Bäckerei Ausdemwald <Detail>`__                                  568,80      709,00      140,20
 `Bäckerei Mießen <Detail>`__                                      2 407,80    3 010,00    602,20
 `Bäckerei Schmitz <Detail>`__                                     4 802,60    6 005,00    1 202,40
 `Donderweer BV <Detail>`__                                        567,00      709,00      142,00
 `Garage Mergelsberg <Detail>`__                                   12 970,32   16 210,90   3 240,58
 `Rumma & Ko OÜ <Detail>`__                                        163,00      205,50      42,50
 `Van Achter NV <Detail>`__                                        802,60      1 005,00    202,40
================================== ============== =============== =========== =========== ============== =============
<BLANKLINE>
No data to display
=============================================== ============== =============== ======= ======== ============== =============
 Description                                     Debit before   Credit before   Debit   Credit   Credit after   Debit after
----------------------------------------------- -------------- --------------- ------- -------- -------------- -------------
 `Mehrwertsteuer-Kontrollamt Eupen <Detail>`__                                          215,69   215,69
=============================================== ============== =============== ======= ======== ============== =============
<BLANKLINE>
No data to display
======================= ============== =============== =========== =========== ============== =============
 Description             Debit before   Credit before   Debit       Credit      Credit after   Debit after
----------------------- -------------- --------------- ----------- ----------- -------------- -------------
 `Bestbank <Detail>`__                                  16 711,04   22 282,12   5 571,08
======================= ============== =============== =========== =========== ============== =============
<BLANKLINE>
=========================== =========== ==========
 Description                 Activa      Passiva
--------------------------- ----------- ----------
 **1 Assets**                            2 354,00
 ** 10 Current assets**                  2 354,00
 1000 Customers receivable               2 354,00
 **2 Passiva**               10 152,39
 ** 20 Liabilities**         10 152,39
 2000 Suppliers payable      5 572,28
 2010 Taxes payable
 2020 Banks                  1 984,96
 2030 Current transfers      5 571,08
=========================== =========== ==========
<BLANKLINE>
========================= =========== ===========
 Description               Expenses    Revenues
------------------------- ----------- -----------
 **6 Expenses**            24 878,47
 6000 Cost of sales        6 777,94
 6100 Operating expenses   14 753,13
 6200 Other expenses       3 347,40
 **7 Revenues**                        21 050,00
 7000 Net sales                        21 050,00
========================= =========== ===========
<BLANKLINE>


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
2354.00
>>> print(liabilities)
10152.39
>>> print(capital)  #doctest: +SKIP
-9354.40
>>> print(liabilities+capital)  #doctest: +SKIP
13836.75
>>> print(passiva)  #doctest: +SKIP
13836.75
>>> print(expenses)
24878.47
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
