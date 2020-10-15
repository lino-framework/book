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
>>> from lino_xl.lib.ledger.choicelists import DC


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
    ======= ================= ================================= ================== ======== ===================================== ========
     value   name              text                              Sheet type         D/C      Sheet item                            Mirror
    ------- ----------------- --------------------------------- ------------------ -------- ------------------------------------- --------
     1       assets            Assets                            Balance sheet      Debit    (1) Assets
     10                        Current assets                    Balance sheet      Debit    (10) Current assets
     1000    customers         Customers receivable              Balance sheet      Debit    (1000) Customers receivable
     1010                      Taxes receivable                  Balance sheet      Debit    (1010) Taxes receivable               2010
     1020                      Cash and cash equivalents         Balance sheet      Debit    (1020) Cash and cash equivalents      2020
     1030                      Current transfers                 Balance sheet      Debit    (1030) Current transfers              2030
     1090                      Other current assets              Balance sheet      Debit    (1090) Other current assets           2090
     11                        Non-current assets                Balance sheet      Debit    (11) Non-current assets
     2       passiva           Passiva                           Balance sheet      Credit   (2) Passiva
     20      liabilities       Liabilities                       Balance sheet      Credit   (20) Liabilities
     2000    suppliers         Suppliers payable                 Balance sheet      Credit   (2000) Suppliers payable
     2010    taxes             Taxes payable                     Balance sheet      Credit   (2010) Taxes payable                  1010
     2020    banks             Banks                             Balance sheet      Credit   (2020) Banks                          1020
     2030    transfers         Current transfers                 Balance sheet      Credit   (2030) Current transfers              1030
     2090    other             Other liabilities                 Balance sheet      Credit   (2090) Other liabilities              1090
     21      capital           Own capital                       Balance sheet      Credit   (21) Own capital
     2150    net_income_loss   Net income (loss)                 Balance sheet      Credit   (2150) Net income (loss)
     4       com_ass_lia       Commercial assets & liabilities   Balance sheet      Credit   (4) Commercial assets & liabilities
     5       fin_ass_lia       Financial assets & liabilities    Balance sheet      Credit   (5) Financial assets & liabilities
     6       expenses          Expenses                          Income statement   Debit    (6) Expenses
     60      op_costs          Operation costs                   Income statement   Debit    (60) Operation costs
     6000    costofsales       Cost of sales                     Income statement   Debit    (6000) Cost of sales
     6010    operating         Operating expenses                Income statement   Debit    (6010) Operating expenses
     6020    otherexpenses     Other expenses                    Income statement   Debit    (6020) Other expenses
     62      wages             Wages                             Income statement   Debit    (62) Wages
     6900    net_income        Net income                        Income statement   Debit    (6900) Net income                     7900
     7       revenues          Revenues                          Income statement   Credit   (7) Revenues
     7000    sales             Net sales                         Income statement   Credit   (7000) Net sales
     7900    net_loss          Net loss                          Income statement   Credit   (7900) Net loss                       6900
    ======= ================= ================================= ================== ======== ===================================== ========
    <BLANKLINE>


    Every item of this list is an instance of :class:`CommonItem`.

.. class:: CommonItem

    .. attribute:: value

         Corresponds to the :attr:`ref` field in :class:`Item`

    .. attribute:: dc
    .. attribute:: sheet


.. class:: Item

    In this table the user can configure their local list of items for
    both sheet types.

    The default table is populated from :class:`CommonItems`.

    >>> rt.show(sheets.Items, language="en")
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    =========== ================================= =================================================== ================================= ================== =================== =================================
     Reference   Designation                       Designation (de)                                    Designation (fr)                  Sheet type         Booking direction   Common sheet item
    ----------- --------------------------------- --------------------------------------------------- --------------------------------- ------------------ ------------------- ---------------------------------
     1           Assets                            Vermögen                                            Actifs                            Balance sheet      Debit               Assets
     10          Current assets                    Current assets                                      Current assets                    Balance sheet      Debit               Current assets
     1000        Customers receivable              Customers receivable                                Customers receivable              Balance sheet      Debit               Customers receivable
     1010        Taxes receivable                  Taxes receivable                                    Taxes receivable                  Balance sheet      Debit               Taxes receivable
     1020        Cash and cash equivalents         Cash and cash equivalents                           Cash and cash equivalents         Balance sheet      Debit               Cash and cash equivalents
     1030        Current transfers                 Current transfers                                   Current transfers                 Balance sheet      Debit               Current transfers
     1090        Other current assets              Other current assets                                Other current assets              Balance sheet      Debit               Other current assets
     11          Non-current assets                Non-current assets                                  Non-current assets                Balance sheet      Debit               Non-current assets
     2           Passiva                           Passiva                                             Passiva                           Balance sheet      Credit              Passiva
     20          Liabilities                       Verpflichtungen                                     Passifs                           Balance sheet      Credit              Liabilities
     2000        Suppliers payable                 Suppliers payable                                   Suppliers payable                 Balance sheet      Credit              Suppliers payable
     2010        Taxes payable                     Taxes payable                                       Taxes payable                     Balance sheet      Credit              Taxes payable
     2020        Banks                             Banks                                               Banks                             Balance sheet      Credit              Banks
     2030        Current transfers                 Current transfers                                   Current transfers                 Balance sheet      Credit              Current transfers
     2090        Other liabilities                 Other liabilities                                   Other liabilities                 Balance sheet      Credit              Other liabilities
     21          Own capital                       Own capital                                         Own capital                       Balance sheet      Credit              Own capital
     2150        Net income (loss)                 Net income (loss)                                   Net income (loss)                 Balance sheet      Credit              Net income (loss)
     4           Commercial assets & liabilities   Kommerzielle Vermögenswerte und Verbindlichkeiten   Commercial assets & liabilities   Balance sheet      Credit              Commercial assets & liabilities
     5           Financial assets & liabilities    Finanzielle Vermögenswerte und Verbindlichkeiten    Financial assets & liabilities    Balance sheet      Credit              Financial assets & liabilities
     6           Expenses                          Ausgaben                                            Dépenses                          Income statement   Debit               Expenses
     60          Operation costs                   Diplome                                             Operation costs                   Income statement   Debit               Operation costs
     6000        Cost of sales                     Cost of sales                                       Cost of sales                     Income statement   Debit               Cost of sales
     6010        Operating expenses                Operating expenses                                  Operating expenses                Income statement   Debit               Operating expenses
     6020        Other expenses                    Other expenses                                      Other expenses                    Income statement   Debit               Other expenses
     62          Wages                             Löhne und Gehälter                                  Salaires                          Income statement   Debit               Wages
     6900        Net income                        Net income                                          Net income                        Income statement   Debit               Net income
     7           Revenues                          Einnahmen                                           Revenus                           Income statement   Credit              Revenues
     7000        Net sales                         Net sales                                           Net sales                         Income statement   Credit              Net sales
     7900        Net loss                          Net loss                                            Net loss                          Income statement   Credit              Net loss
    =========== ================================= =================================================== ================================= ================== =================== =================================
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
>>> print(rpt.start_period)
2015-01
>>> print(rpt.end_period)
2015-12
>>> rpt.run_update_plan(rt.login('robin'))  # temporary 20200927
>>> rt.show(sheets.ResultsEntriesByReport, rpt)  # doctest: -SKIP
========================= =========== ===========
 Description               Expenses    Revenues
------------------------- ----------- -----------
 **6 Expenses**            26 115,45
 ** 60 Operation costs**   26 115,45
 6000 Cost of sales        6 285,79
 6010 Operating expenses   16 261,89
 6020 Other expenses       3 567,77
 **7 Revenues**                        21 050,00
 7000 Net sales                        21 050,00
========================= =========== ===========
<BLANKLINE>


>>> ses = rt.login("robin")
>>> ses.show_story(rpt.get_story(ses), header_level=2)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
------------------------
General account balances
------------------------
============================== ================ ================ =============== ===============
 Account                        Balance before   Debit            Credit          Balance after
------------------------------ ---------------- ---------------- --------------- ---------------
 4000 Customers                 0.00 CR          21 172,95        18 497,91       2675.04 DB
 4100 Suppliers                 0.00 CR          22 332,12        27 904,40       5572.28 CR
 4300 Pending Payment Orders    0.00 CR          22 448,65        22 448,65       0 CR
 4500 Tax Offices               0.00 CR          116,53           116,53          0 CR
 4510 VAT due                   0.00 CR          116,53           170,39          53.86 CR
 4520 VAT deductible            0.00 CR          1 899,34                         1899.34 DB
 5500 BestBank                  0.00 CR          6 187,46         2 253,77        3933.69 DB
 6010 Purchase of services      0.00 CR          16 261,89                        16261.89 DB
 6020 Purchase of investments   0.00 CR          3 567,77                         3567.77 DB
 6040 Purchase of goods         0.00 CR          6 285,79                         6285.79 DB
 7000 Sales                     0.00 CR          1 440,00         2 730,00        1290.00 CR
 7010 Sales on therapies        0.00 CR                           19 760,00       19760.00 CR
 **Total (12 rows)**                             **101 829,03**   **93 881,65**
============================== ================ ================ =============== ===============
<BLANKLINE>
--------------------------
Analytic accounts balances
--------------------------
====================== ================ =============== ======== ===============
 Account                Balance before   Debit           Credit   Balance after
---------------------- ---------------- --------------- -------- ---------------
 1100 Wages             0.00 CR          531,36                   531.36 DB
 1200 Transport         0.00 CR          1 434,63                 1434.63 DB
 1300 Training          0.00 CR          3 128,42                 3128.42 DB
 1400 Other costs       0.00 CR          650,08                   650.08 DB
 2100 Secretary wages   0.00 CR          1 520,72                 1520.72 DB
 2110 Manager wages     0.00 CR          4 336,29                 4336.29 DB
 2200 Transport         0.00 CR          3 671,17                 3671.17 DB
 2300 Training          0.00 CR          552,64                   552.64 DB
 3000 Investment        0.00 CR          1 200,31                 1200.31 DB
 4100 Wages             0.00 CR          3 555,20                 3555.20 DB
 4200 Transport         0.00 CR          481,78                   481.78 DB
 4300 Training          0.00 CR          501,50                   501.50 DB
 5100 Wages             0.00 CR          1 359,79                 1359.79 DB
 5200 Transport         0.00 CR          2 942,07                 2942.07 DB
 5300 Other costs       0.00 CR          249,49                   249.49 DB
 **Total (15 rows)**                     **26 115,45**
====================== ================ =============== ======== ===============
<BLANKLINE>
------------------------
Partner balances (Sales)
------------------------
================================================ ================ =============== =============== ===============
 Partner                                          Balance before   Debit           Credit          Balance after
------------------------------------------------ ---------------- --------------- --------------- ---------------
 `Altenberg Hans <Detail>`__                      0.00 CR          1 086,20        846,20          240.00 DB
 `Arens Andreas <Detail>`__                       0.00 CR          540,00          540,00          0 CR
 `Arens Annette <Detail>`__                       0.00 CR          1 332,83        1 332,80        0.03 DB
 `Ausdemwald Alfons <Detail>`__                   0.00 CR          620,00          620,00          0 CR
 `Auto École Verte <Detail>`__                    0.00 CR          500,00          500,00          0 CR
 `Bastiaensen Laurent <Detail>`__                 0.00 CR          711,20          570,20          141.00 DB
 `Bernd Brechts Bücherladen <Detail>`__           0.00 CR          620,00          620,00          0 CR
 `Bäckerei Ausdemwald <Detail>`__                 0.00 CR          360,00          360,00          0 CR
 `Bäckerei Mießen <Detail>`__                     0.00 CR          440,00          440,00          0 CR
 `Bäckerei Schmitz <Detail>`__                    0.00 CR          160,00          160,00          0 CR
 `Chantraine Marc <Detail>`__                     0.00 CR          1 190,00        540,00          650.00 DB
 `Charlier Ulrike <Detail>`__                     0.00 CR          1 020,60        540,60          480.00 DB
 `Collard Charlotte <Detail>`__                   0.00 CR          840,00          540,00          300.00 DB
 `Demeulenaere Dorothée <Detail>`__               0.00 CR          1 523,80        843,80          680.00 DB
 `Denon Denis <Detail>`__                         0.00 CR          1 620,00        1 620,00        0 CR
 `Dericum Daniel <Detail>`__                      0.00 CR          160,00                          160.00 DB
 `Dobbelstein-Demeulenaere Dorothée <Detail>`__   0.00 CR          540,00          540,00          0 CR
 `Donderweer BV <Detail>`__                       0.00 CR          320,00          320,00          0 CR
 `Emonts Erich <Detail>`__                        0.00 CR          255,00          255,00          0 CR
 `Emontspool Erwin <Detail>`__                    0.00 CR          630,60          630,60          0 CR
 `Garage Mergelsberg <Detail>`__                  0.00 CR          605,00          605,00          0 CR
 `Groteclaes Gregory <Detail>`__                  0.00 CR          301,10          301,00          0.10 DB
 `Hans Flott & Co <Detail>`__                     0.00 CR          350,00          350,00          0 CR
 `Hilgers Henri <Detail>`__                       0.00 CR          540,00          540,00          0 CR
 `Jonas Josef <Detail>`__                         0.00 CR          240,70          240,70          0 CR
 `Kaivers Karl <Detail>`__                        0.00 CR          541,20          541,20          0 CR
 `Leffin Electronics <Detail>`__                  0.00 CR          100,00          100,00          0 CR
 `Malmendier Marc <Detail>`__                     0.00 CR          300,46          298,75          1.71 DB
 `Martelaer Mark <Detail>`__                      0.00 CR          630,00          630,00          0 CR
 `Moulin Rouge <Detail>`__                        0.00 CR          450,00          427,50          22.50 DB
 `Radermacher Daniela <Detail>`__                 0.00 CR          285,96          286,20          0.24 CR
 `Radermacher Edgard <Detail>`__                  0.00 CR          540,00          540,00          0 CR
 `Radermecker Rik <Detail>`__                     0.00 CR          241,10          241,10          0 CR
 `Reinhards Baumschule <Detail>`__                0.00 CR          280,00          280,00          0 CR
 `Rumma & Ko OÜ <Detail>`__                       0.00 CR          450,00          450,00          0 CR
 `Van Achter NV <Detail>`__                       0.00 CR          306,00          306,00          0 CR
 `da Vinci David <Detail>`__                      0.00 CR          541,20          541,26          0.06 CR
 **Total (37 rows)**                                               **21 172,95**   **18 497,91**
================================================ ================ =============== =============== ===============
<BLANKLINE>
----------------------------
Partner balances (Purchases)
----------------------------
=============================================== ================ =============== =============== ===============
 Partner                                         Balance before   Debit           Credit          Balance after
----------------------------------------------- ---------------- --------------- --------------- ---------------
 `Bäckerei Ausdemwald <Detail>`__                0.00 CR          568,80          709,00          140.20 CR
 `Bäckerei Mießen <Detail>`__                    0.00 CR          2 407,80        3 010,00        602.20 CR
 `Bäckerei Schmitz <Detail>`__                   0.00 CR          4 802,60        6 005,00        1202.40 CR
 `Donderweer BV <Detail>`__                      0.00 CR          567,00          709,00          142.00 CR
 `Garage Mergelsberg <Detail>`__                 0.00 CR          12 970,32       16 210,90       3240.58 CR
 `Rumma & Ko OÜ <Detail>`__                      0.00 CR          163,00          205,50          42.50 CR
 `Tough Thorough Thought Therapies <Detail>`__   0.00 CR          50,00           50,00           0 CR
 `Van Achter NV <Detail>`__                      0.00 CR          802,60          1 005,00        202.40 CR
 **Total (8 rows)**                                               **22 332,12**   **27 904,40**
=============================================== ================ =============== =============== ===============
<BLANKLINE>
------------------------
Partner balances (Wages)
------------------------
No data to display
------------------------
Partner balances (Taxes)
------------------------
=============================================== ================ ============ ============ ===============
 Partner                                         Balance before   Debit        Credit       Balance after
----------------------------------------------- ---------------- ------------ ------------ ---------------
 `Mehrwertsteuer-Kontrollamt Eupen <Detail>`__   0.00 CR          116,53       116,53       0 CR
 **Total (1 rows)**                                               **116,53**   **116,53**
=============================================== ================ ============ ============ ===============
<BLANKLINE>
----------------------------
Partner balances (Clearings)
----------------------------
No data to display
--------------------------------------
Partner balances (Bank payment orders)
--------------------------------------
======================= ================ =============== =============== ===============
 Partner                 Balance before   Debit           Credit          Balance after
----------------------- ---------------- --------------- --------------- ---------------
 `Bestbank <Detail>`__   0.00 CR          22 448,65       22 448,65       0 CR
 **Total (1 rows)**                       **22 448,65**   **22 448,65**
======================= ================ =============== =============== ===============
<BLANKLINE>
-------------
Balance sheet
-------------
================================ ========== ==========
 Description                      Activa     Passiva
-------------------------------- ---------- ----------
 **1 Assets**                                8 454,21
 ** 10 Current assets**                      8 454,21
 1000 Customers receivable                   2 675,04
 1010 Taxes receivable                       1 845,48
 1020 Cash and cash equivalents              3 933,69
 **2 Passiva**                    5 572,28
 ** 20 Liabilities**              5 572,28
 2000 Suppliers payable           5 572,28
 2030 Current transfers
================================ ========== ==========
<BLANKLINE>
----------------
Income statement
----------------
========================= =========== ===========
 Description               Expenses    Revenues
------------------------- ----------- -----------
 **6 Expenses**            26 115,45
 ** 60 Operation costs**   26 115,45
 6000 Cost of sales        6 285,79
 6010 Operating expenses   16 261,89
 6020 Other expenses       3 567,77
 **7 Revenues**                        21 050,00
 7000 Net sales                        21 050,00
========================= =========== ===========
<BLANKLINE>

======================================= ============== =============== =========== =========== ============== =============
 Account                                 Debit before   Credit before   Debit       Credit      Credit after   Debit after
--------------------------------------- -------------- --------------- ----------- ----------- -------------- -------------
 **4 Commercial assets & liabilities**                                  68 086,12   69 137,88   1 051,76
 4000 Customers                                                         21 172,95   18 497,91                  2 675,04
 4100 Suppliers                                                         22 332,12   27 904,40   5 572,28
 4300 Pending Payment Orders                                            22 448,65   22 448,65
 4500 Tax Offices                                                       116,53      116,53
 4510 VAT due                                                           116,53      170,39      53,86
 4520 VAT deductible                                                    1 899,34                               1 899,34
 **5 Financial assets & liabilities**                                   6 187,46    2 253,77                   3 933,69
 5500 BestBank                                                          6 187,46    2 253,77                   3 933,69
 **6 Expenses**                                                         26 115,45                              26 115,45
 ** 60 Operation costs**                                                26 115,45                              26 115,45
 6010 Purchase of services                                              16 261,89                              16 261,89
 6020 Purchase of investments                                           3 567,77                               3 567,77
 6040 Purchase of goods                                                 6 285,79                               6 285,79
 **7 Revenues**                                                         1 440,00    22 490,00   21 050,00
 7000 Sales                                                             1 440,00    2 730,00    1 290,00
 7010 Sales on therapies                                                            19 760,00   19 760,00
======================================= ============== =============== =========== =========== ============== =============
<BLANKLINE>
============================ ============== =============== =========== ======== ============== =============
 Account                      Debit before   Credit before   Debit       Credit   Credit after   Debit after
---------------------------- -------------- --------------- ----------- -------- -------------- -------------
 **1 Operation costs**                                       5 744,49                            5 744,49
 1100 Wages                                                  531,36                              531,36
 1200 Transport                                              1 434,63                            1 434,63
 1300 Training                                               3 128,42                            3 128,42
 1400 Other costs                                            650,08                              650,08
 **2 Administrative costs**                                  10 080,82                           10 080,82
 2100 Secretary wages                                        1 520,72                            1 520,72
 2110 Manager wages                                          4 336,29                            4 336,29
 2200 Transport                                              3 671,17                            3 671,17
 2300 Training                                               552,64                              552,64
 **3 Investments**                                           1 200,31                            1 200,31
 3000 Investment                                             1 200,31                            1 200,31
 **4 Project 1**                                             4 538,48                            4 538,48
 4100 Wages                                                  3 555,20                            3 555,20
 4200 Transport                                              481,78                              481,78
 4300 Training                                               501,50                              501,50
 **5 Project 2**                                             4 551,35                            4 551,35
 5100 Wages                                                  1 359,79                            1 359,79
 5200 Transport                                              2 942,07                            2 942,07
 5300 Other costs                                            249,49                              249,49
============================ ============== =============== =========== ======== ============== =============
<BLANKLINE>
================================================ ============== =============== ========== ========== ============== =============
 Partner                                          Debit before   Credit before   Debit      Credit     Credit after   Debit after
------------------------------------------------ -------------- --------------- ---------- ---------- -------------- -------------
 `Altenberg Hans <Detail>`__                                                     1 086,20   846,20                    240,00
 `Arens Andreas <Detail>`__                                                      540,00     540,00
 `Arens Annette <Detail>`__                                                      1 332,83   1 332,80                  0,03
 `Ausdemwald Alfons <Detail>`__                                                  620,00     620,00
 `Auto École Verte <Detail>`__                                                   500,00     500,00
 `Bastiaensen Laurent <Detail>`__                                                711,20     570,20                    141,00
 `Bernd Brechts Bücherladen <Detail>`__                                          620,00     620,00
 `Bäckerei Ausdemwald <Detail>`__                                                360,00     360,00
 `Bäckerei Mießen <Detail>`__                                                    440,00     440,00
 `Bäckerei Schmitz <Detail>`__                                                   160,00     160,00
 `Chantraine Marc <Detail>`__                                                    1 190,00   540,00                    650,00
 `Charlier Ulrike <Detail>`__                                                    1 020,60   540,60                    480,00
 `Collard Charlotte <Detail>`__                                                  840,00     540,00                    300,00
 `Demeulenaere Dorothée <Detail>`__                                              1 523,80   843,80                    680,00
 `Denon Denis <Detail>`__                                                        1 620,00   1 620,00
 `Dericum Daniel <Detail>`__                                                     160,00                               160,00
 `Dobbelstein-Demeulenaere Dorothée <Detail>`__                                  540,00     540,00
 `Donderweer BV <Detail>`__                                                      320,00     320,00
 `Emonts Erich <Detail>`__                                                       255,00     255,00
 `Emontspool Erwin <Detail>`__                                                   630,60     630,60
 `Garage Mergelsberg <Detail>`__                                                 605,00     605,00
 `Groteclaes Gregory <Detail>`__                                                 301,10     301,00                    0,10
 `Hans Flott & Co <Detail>`__                                                    350,00     350,00
 `Hilgers Henri <Detail>`__                                                      540,00     540,00
 `Jonas Josef <Detail>`__                                                        240,70     240,70
 `Kaivers Karl <Detail>`__                                                       541,20     541,20
 `Leffin Electronics <Detail>`__                                                 100,00     100,00
 `Malmendier Marc <Detail>`__                                                    300,46     298,75                    1,71
 `Martelaer Mark <Detail>`__                                                     630,00     630,00
 `Moulin Rouge <Detail>`__                                                       450,00     427,50                    22,50
 `Radermacher Daniela <Detail>`__                                                285,96     286,20     0,24
 `Radermacher Edgard <Detail>`__                                                 540,00     540,00
 `Radermecker Rik <Detail>`__                                                    241,10     241,10
 `Reinhards Baumschule <Detail>`__                                               280,00     280,00
 `Rumma & Ko OÜ <Detail>`__                                                      450,00     450,00
 `Van Achter NV <Detail>`__                                                      306,00     306,00
 `da Vinci David <Detail>`__                                                     541,20     541,26     0,06
================================================ ============== =============== ========== ========== ============== =============
<BLANKLINE>
=============================================== ============== =============== =========== =========== ============== =============
 Partner                                         Debit before   Credit before   Debit       Credit      Credit after   Debit after
----------------------------------------------- -------------- --------------- ----------- ----------- -------------- -------------
 `Bäckerei Ausdemwald <Detail>`__                                               568,80      709,00      140,20
 `Bäckerei Mießen <Detail>`__                                                   2 407,80    3 010,00    602,20
 `Bäckerei Schmitz <Detail>`__                                                  4 802,60    6 005,00    1 202,40
 `Donderweer BV <Detail>`__                                                     567,00      709,00      142,00
 `Garage Mergelsberg <Detail>`__                                                12 970,32   16 210,90   3 240,58
 `Rumma & Ko OÜ <Detail>`__                                                     163,00      205,50      42,50
 `Tough Thorough Thought Therapies <Detail>`__                                  50,00       50,00
 `Van Achter NV <Detail>`__                                                     802,60      1 005,00    202,40
=============================================== ============== =============== =========== =========== ============== =============
<BLANKLINE>
No data to display
=============================================== ============== =============== ======== ======== ============== =============
 Partner                                         Debit before   Credit before   Debit    Credit   Credit after   Debit after
----------------------------------------------- -------------- --------------- -------- -------- -------------- -------------
 `Mehrwertsteuer-Kontrollamt Eupen <Detail>`__                                  116,53   116,53
=============================================== ============== =============== ======== ======== ============== =============
<BLANKLINE>
No data to display
======================= ============== =============== =========== =========== ============== =============
 Partner                 Debit before   Credit before   Debit       Credit      Credit after   Debit after
----------------------- -------------- --------------- ----------- ----------- -------------- -------------
 `Bestbank <Detail>`__                                  22 448,65   22 448,65
======================= ============== =============== =========== =========== ============== =============
<BLANKLINE>
=========================== ========== ==========
 Description                 Activa     Passiva
--------------------------- ---------- ----------
 **1 Assets**                           2 675,04
 ** 10 Current assets**                 2 675,04
 1000 Customers receivable              2 675,04
 **2 Passiva**
 ** 20 Liabilities**
 2000 Suppliers payable      5 572,28
 2010 Taxes payable
 2020 Banks
 2030 Current transfers
=========================== ========== ==========
<BLANKLINE>
========================= =========== ===========
 Description               Expenses    Revenues
------------------------- ----------- -----------
 **6 Expenses**            26 115,45
 6000 Cost of sales        6 285,79
 6100 Operating expenses   16 261,89
 6200 Other expenses       3 567,77
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
>>> def getval(ci):
...     try:
...         e = sheets.ItemEntry.objects.get(report=rpt, item=ci.get_object())
...     except sheets.ItemEntry.DoesNotExist:
...         return 0
...     return e.new_balance().value(e.item.dc)

TODO: the following tests aren't yet very meaningful, we must first
automatically generate the profit/loss booking (:ticket:`3476`) so that the
expenses and revenues are balanced.

>>> assets = getval(sheets.CommonItems.assets)
>>> liabilities = getval(sheets.CommonItems.liabilities)
>>> capital = getval(sheets.CommonItems.capital)
>>> passiva = getval(sheets.CommonItems.passiva)
>>> expenses = getval(sheets.CommonItems.expenses)
>>> revenues = getval(sheets.CommonItems.revenues)

>>> print(assets)
8454.21
>>> print(liabilities)
5572.28
>>> print(capital)  #doctest: +SKIP
-9354.40
>>> print(liabilities+capital)  #doctest: +SKIP
13836.75
>>> print(passiva)  #doctest: +SKIP
13836.75
>>> print(expenses)
26115.45
>>> print(revenues)  #doctest: +SKIP
24518.54

Accounts on the left side of the equation (Assets and Expenses) are
normally DEBITed and have DEBIT balances.  That's what the :attr:`dc
<CommonItem.dc>` attribute means:

>>> translation.activate('en')

>>> print(sheets.CommonItems.assets.dc)
Debit
>>> print(sheets.CommonItems.expenses.dc)
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
...     print("%-2s|%-15s|%-6s" % (t.value, t, t.dc))
1 |Assets         |Debit
10|Current assets |Debit
11|Non-current assets|Debit
2 |Passiva        |Credit
20|Liabilities    |Credit
21|Own capital    |Credit
4 |Commercial assets & liabilities|Credit
5 |Financial assets & liabilities|Credit
6 |Expenses       |Debit
60|Operation costs|Debit
62|Wages          |Debit
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


>>> t = rt.models.sheets.BalanceEntriesByReport
>>> th = t.get_handle()
>>> th  #doctest: +ELLIPSIS
<lino.core.tables.TableHandle object at ...>

>>> ll = th.get_list_layout()
>>> ll.layout._datasource is t
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
