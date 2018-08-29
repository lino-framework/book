.. doctest docs/specs/sheets.rst
.. _xl.specs.sheets:

==================================
Balance sheet and Income statement
==================================

.. currentmodule:: lino_xl.lib.sheets
                   
The :mod:`lino_xl.lib.sheets` plugin adds two important parts of the
annual financial reports: the *Balance sheet* and the *Income
statement*.

You should have read :doc:`accounts`
and :doc:`ledger` before reading this document.

Examples in this document use the :mod:`lino_book.projects.lydia`
demo project.

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.demo')
>>> from lino.api.doctest import *
>>> ses = rt.login("robin")
>>> translation.activate('en')
>>> from lino_xl.lib.accounts.utils import DCLABELS


Table of contents:

.. contents::
   :depth: 1
   :local:



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
    ======= ================= =========================== ================== ======== ================================
     value   name              text                        Sheet type         D/C      Sheet item
    ------- ----------------- --------------------------- ------------------ -------- --------------------------------
     1       assets            Assets                      Balance sheet      Debit    1 Assets
     10                        Current assets              Balance sheet      Debit    10 Current assets
     1000    customers         Customers receivable        Balance sheet      Debit    1000 Customers receivable
     1010                      Taxes receivable            Balance sheet      Debit    1010 Taxes receivable
     1020                      Cash and cash equivalents   Balance sheet      Debit    1020 Cash and cash equivalents
     1030                      Current transfers           Balance sheet      Debit    1030 Current transfers
     1090                      Other current assets        Balance sheet      Debit    1090 Other current assets
     11                        Non-current assets          Balance sheet      Debit    11 Non-current assets
     2       passiva           Passiva                     Balance sheet      Credit   2 Passiva
     20      liabilities       Liabilities                 Balance sheet      Credit   20 Liabilities
     2000    suppliers         Suppliers payable           Balance sheet      Credit   2000 Suppliers payable
     2010    taxes             Taxes payable               Balance sheet      Credit   2010 Taxes payable
     2020    banks             Banks                       Balance sheet      Credit   2020 Banks
     2030    transfers         Current transfers           Balance sheet      Credit   2030 Current transfers
     2090    other             Other liabilities           Balance sheet      Credit   2090 Other liabilities
     21      capital           Own capital                 Balance sheet      Credit   21 Own capital
     2150    net_income_loss   Net income (loss)           Balance sheet      Credit   2150 Net income (loss)
     6       expenses          Expenses                    Income statement   Debit    6 Expenses
     6000    costofsales       Cost of sales               Income statement   Debit    6000 Cost of sales
     6100    operating         Operating expenses          Income statement   Debit    6100 Operating expenses
     6200    otherexpenses     Other expenses              Income statement   Debit    6200 Other expenses
     6900    net_income        Net income                  Income statement   Debit    6900 Net income
     7       revenues          Revenues                    Income statement   Credit   7 Revenues
     7000    sales             Net sales                   Income statement   Credit   7000 Net sales
     7900    net_loss          Net loss                    Income statement   Credit   7900 Net loss
    ======= ================= =========================== ================== ======== ================================
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
    ==== =========== =========================== =========================== =========================== =================== ================== =========================== ========
     ID   Reference   Designation                 Designation (de)            Designation (fr)            Booking direction   Sheet type         Common sheet item           Mirror
    ---- ----------- --------------------------- --------------------------- --------------------------- ------------------- ------------------ --------------------------- --------
     1    1           Assets                      Vermögen                    Actifs                      Debit               Balance sheet      Assets
     2    10          Current assets              Current assets              Current assets              Debit               Balance sheet      Current assets
     3    1000        Customers receivable        Customers receivable        Customers receivable        Debit               Balance sheet      Customers receivable
     ...
     25   7900        Net loss                    Net loss                    Net loss                    Credit              Income statement   Net loss                    6900
    ==== =========== =========================== =========================== =========================== =================== ================== =========================== ========
    <BLANKLINE>

    In the demo database this list is an unchanged copy of :class:`CommonItems`.
    
.. class:: Entry

    An **entry** is the computed value of given *item* for a given
    *fiscal year*.
           
    >>> rt.show(sheets.Entries, language="en")
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    ============= =========================== =================== ===========
     Fiscal year   Sheet item                  Booking direction   Value
    ------------- --------------------------- ------------------- -----------
     2015          1 Assets                    Debit               4 663,25
     2015          10 Current assets           Debit               4 663,25
     2015          1000 Customers receivable   Debit               4 663,25
     2015          2 Passiva                   Credit              13 836,75
     2015          20 Liabilities              Credit              23 191,15
     2015          2000 Suppliers payable      Credit              5 512,50
     2015          2010 Taxes payable          Credit              297,46
     2015          2020 Banks                  Credit              4 586,75
     2015          2030 Current transfers      Credit              12 794,44
     2015          21 Own capital              Credit              -9 354,40
     2015          2150 Net income (loss)      Credit              -9 354,40
     2015          6 Expenses                  Debit               27 854,40
     2015          6000 Cost of sales          Debit               6 714,00
     2015          6100 Operating expenses     Debit               17 620,40
     2015          6200 Other expenses         Debit               3 520,00
     2015          7 Revenues                  Credit              27 854,40
     2015          7000 Net sales              Credit              18 500,00
     2015          7900 Net loss               Credit              9 354,40
    ============= =========================== =================== ===========
    <BLANKLINE>
    

The Accounting Equation
=======================

The basic `Accounting Equation
<https://en.wikipedia.org/wiki/Accounting_equation>`_ states:

  Assets = Liabilities + Capital
 
And the expanded accounting equation is:

    Assets + Expenses = Liabilities + Equity + Revenue

>>> year = ledger.FiscalYear.get_by_ref('2015')
>>> def val(ci):
...     e = sheets.Entry.objects.get(master=year, item=ci.get_object())
...     return e.value

>>> assets = val(sheets.CommonItems.assets)
>>> liabilities = val(sheets.CommonItems.liabilities)
>>> capital = val(sheets.CommonItems.capital)
>>> passiva = val(sheets.CommonItems.passiva)
>>> expenses = val(sheets.CommonItems.expenses)
>>> revenues = val(sheets.CommonItems.revenues)

>>> print(assets)
4663.25
>>> print(liabilities)
23191.15
>>> print(capital)
-9354.40
>>> print(liabilities+capital)
13836.75
>>> print(passiva)
13836.75
>>> print(expenses)
27854.40
>>> print(revenues)
27854.40
    
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




Don't read me
=============


>>> th = rt.models.sheets.BalanceByYear.get_handle()
>>> th  #doctest: +ELLIPSIS
<lino.core.tables.TableHandle object at ...>

>>> ll = th.get_list_layout()
>>> ll.layout._datasource is rt.models.sheets.BalanceByYear
True

>>> cols = th.get_columns()
>>> el = cols[0]
>>> print(el.field.name)
description
>>> print(el.name)
description
>>> print(el.width)
None
>>> el.preferred_width
50

