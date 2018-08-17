.. _xl.specs.accounts:


========
Accounts
========

.. how to test this document:

    $ doctest docs/specs/accounts.rst

    Doctest initialization:

    >>> import lino
    >>> lino.startup('lino_book.projects.pierre.settings.demo')
    >>> from lino.api.doctest import *


The :mod:`lino_xl.lib.accounts` plugin defines the "static" part of
accounting stuff: it adds an account chart (consisting of accounts and
account groups) to your application.

Table of contents:

.. contents::
   :depth: 1
   :local:

.. currentmodule:: lino_xl.lib.accounts


Accounts
========

.. class:: Account

    An **account** is the most abstract representation for "something
    where you can place money and retrieve it later".

    An account always has a given balance which can be negative or
    positive.

    In applications which use the :mod:`ledger <lino_xl.lib.ledger>`
    plugin, accounts are used as the target of ledger movements.


    .. attribute:: name

        The multilingual designation of this account, as the users see
        it.


    .. attribute:: group

        The *account group* to which this account belongs.  Points to
        an instance of :class:`Group`.  If this field is empty, the
        account won't appear in certain reports.
    
    .. attribute:: seqno

        The sequence number of this account within its :attr:`group`.
    
    .. attribute:: ref

        An optional unique name which can be used to reference a given
        account.

    .. attribute:: type

        The *account type* of this account.  This points to an item of
        :class:`CommonAccounts`.
    
    .. attribute:: needs_partner

        Whether bookings to this account need a partner specified.

        For payment orders this causes the contra entry of financial
        documents to be detailed or not (i.e. one contra entry for
        every item or a single contra entry per voucher.

    .. attribute:: default_amount

        The default amount to book in bank statements or journal
        entries when this account has been selected manually. The
        default booking direction is that of the :attr:`type`.
           
    .. attribute:: purchases_allowed
    .. attribute:: sales_allowed
    .. attribute:: wages_allowed
    .. attribute:: FOO_allowed

        These checkboxes indicate whether this account can be used on
        an item of a purchases (or sales or wages or FOO)
        invoice. There is one such checkbox for every trade type
        (:class:`TradeTypes <lino_xl.lib.ledger.TradeTypes>`).  They
        exist only when the :mod:`ledger <lino_xl.lib.ledger>` plugin
        is installed as well.  See also the
        :meth:`get_allowed_accounts
        <lino_xl.lib.ledger.Journal.get_allowed_accounts>` method.

    .. attribute:: needs_ana
                   
        Whether transactions on this account require the user to also
        specify an analytic account.

        This file exists only when :mod:`lino_xl.lib.ana` is
        installed as well.
        
    .. attribute:: ana_account
           
        Which analytic account to suggest for transactions on this
        account.

        This file exists only when :mod:`lino_xl.lib.ana` is
        installed as well.
        

Account groups
==============

.. class:: Group
           
    A group of accounts.

.. class:: Groups
           
    The global table of all account groups.
           

The balance of an account
=========================

The **balance** of an account is the amount of money in that account.

An accounting balance is either Debit or Credit.  We represent this
internally as a boolean, but define two names `DEBIT` and `CREDIT`:

>>> from lino_xl.lib.accounts.utils import DEBIT, CREDIT, DCLABELS
>>> from lino_xl.lib.accounts.utils import Balance
>>> DEBIT
True
>>> CREDIT
False

A negative value on one side of the balance is automatically taken
from away the other side.

>>> Balance(10, -2)
Balance(12,0)


.. class:: Balance
           
    Light-weight object to represent a balance, i.e. an amount
    together with its booking direction (debit or credit).

    Attributes:

    .. attribute:: d

        The amount of this balance when it is debiting, otherwise zero.

    .. attribute:: c

        The amount of this balance when it is crediting, otherwise zero.

       

Account types
=============


.. class:: AccountTypes

    The global list of **account types** or *top-level
    accounts*. 

    >>> rt.show(accounts.AccountTypes, language="en")
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    ======= ============= ============= ======== ===============
     value   name          text          D/C      Sheet
    ------- ------------- ------------- -------- ---------------
     A       assets        Assets        Debit    BalanceSheet
     L       liabilities   Liabilities   Credit   BalanceSheet
     C       capital       Capital       Credit   BalanceSheet
     I       incomes       Incomes       Credit   EarningsSheet
     E       expenses      Expenses      Debit    EarningsSheet
    ======= ============= ============= ======== ===============
    <BLANKLINE>

    Every item of this list is an instance of :class:`AccountType`.           

.. class:: AccountType
           
    The base class for items of ::class:`AccountTypes`.

    .. attribute:: dc
    .. attribute:: sheet

Every account type has its own Python class as well.

.. class:: Assets(AccountType)
.. class:: Liabilities(AccountType)
.. class:: Capital(AccountType)
.. class:: Income(AccountType)
.. class:: Expenses(AccountType)


The basic `Accounting Equation
<https://en.wikipedia.org/wiki/Accounting_equation>`_ states:

  Assets = Liabilities + Capital
 
And the expanded accounting equation is:

    Assets + Expenses = Liabilities + Equity + Revenue
    
    
Accounts on the left side of the equation (Assets and Expenses) are
normally DEBITed and have DEBIT balances.  That's what the :attr:`dc
<AccountType.dc>` attribute means:

>>> translation.activate('en')

>>> print(DCLABELS[accounts.AccountTypes.assets.dc])
Debit
>>> print(DCLABELS[accounts.AccountTypes.expenses.dc])
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

>>> for t in accounts.AccountTypes.get_list_items():
... #doctest: +NORMALIZE_WHITESPACE
...     print("%-12s|%-15s|%-6s" % (t.name, t, DCLABELS[t.dc]))
assets      |Assets         |Debit 
liabilities |Liabilities    |Credit
capital     |Capital        |Credit
incomes     |Incomes        |Credit
expenses    |Expenses       |Debit


Common accounts
===============

The `accounts` plugin defines a choicelist of **common accounts**
which are used to reference the database object for certain accounts
which have a special meaning.

Here is the standard list of common accounts in a :ref:`cosi`
application:

>>> rt.show(accounts.CommonAccounts, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= ========================= ========================= ============== =========== ================================
 value   name                      text                      Account type   Clearable   Account
------- ------------------------- ------------------------- -------------- ----------- --------------------------------
 4000    customers                 Customers                 Assets         Yes         (4000) Customers
 4300    pending_po                Pending Payment Orders    Assets         Yes         (4300) Pending Payment Orders
 4400    suppliers                 Suppliers                 Liabilities    Yes         (4400) Suppliers
 4500    employees                 Employees                 Liabilities    Yes
 4600    tax_offices               Tax Offices               Liabilities    Yes         (4600) Tax Offices
 4510    vat_due                   VAT due                   Liabilities    No          (4510) VAT due
 4511    vat_returnable            VAT returnable            Liabilities    No          (4511) VAT returnable
 4512    vat_deductible            VAT deductible            Liabilities    No          (4512) VAT deductible
 4513    due_taxes                 VAT declared              Liabilities    No          (4513) VAT declared
 4900    waiting                   Waiting                   Liabilities    Yes         (4900) Waiting     
 5500    best_bank                 BestBank                  Assets         No          (5500) BestBank
 5700    cash                      Cash                      Assets         No          (5700) Cash
 6040    purchase_of_goods         Purchase of goods         Expenses       No          (6040) Purchase of goods
 6010    purchase_of_services      Purchase of services      Expenses       No          (6010) Purchase of services
 6020    purchase_of_investments   Purchase of investments   Expenses       No          (6020) Purchase of investments
 6300    wages                     Wages                     Expenses       No
 7000    sales                     Sales                     Incomes        No          (7000) Sales
======= ========================= ========================= ============== =========== ================================
<BLANKLINE>

Lino applications can add specific items to that list or potentially
redefine it completely

.. class:: CommonAccounts

    The global list of common accounts.

    This is a :class:`lino.core.choicelists.ChoiceList`.
    Every item is an instance of :class:`CommonAccount`.

.. class:: CommonAccount
           
    The base class for items of ::class:`CommonAccounts`.
    It defines two additional attributes:

    .. attribute:: clearable
    .. attribute:: needs_partner



The :class:`Sheet` class
========================

It has a hard-coded list of the Sheets used in annual accounting
reports.

The class :class:`Sheet` represents the basic financial statements
which every accounting package should implement.

Lino currently defines three types of financial statements and defines
one class for each of them.

These classes are not meant to be instantiated, they are just Lino's
suggestion for a standardized vocabulary.

>>> from lino_xl.lib.accounts.choicelists import Sheet
>>> print(Sheet.objects)
(<class 'lino_xl.lib.accounts.choicelists.BalanceSheet'>, <class 'lino_xl.lib.accounts.choicelists.EarningsSheet'>)

The `verbose_name` is what users see. It is a lazily translated
string, so we must call `unicode()` to see it:

>>> for s in Sheet.objects:
...     print(s.verbose_name)
Balance sheet
Profit & Loss statement

French users will see:

>>> from django.utils import translation
>>> with translation.override('fr'):
...     for s in Sheet.objects:
...         print(str(s.verbose_name))
Bilan
Compte de résultats


The :meth:`Sheet.account_types` method.

Assets, Liabilities and Capital are listed in the Balance Sheet.
Income and Expenses are listed in the Profit & Loss statement.

>>> from lino_xl.lib.accounts.choicelists import BalanceSheet, EarningsSheet
>>> print(BalanceSheet.account_types())
[<AccountTypes.assets:A>, <AccountTypes.liabilities:L>, <AccountTypes.capital:C>]

>>> print(EarningsSheet.account_types())
[<AccountTypes.incomes:I>, <AccountTypes.expenses:E>]



Account sheets
==============

.. class:: Sheet
           
    Base class for a financial statement.
           
.. class:: BalanceSheet

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

           
.. class:: EarningsSheet
    https://en.wikipedia.org/wiki/Statement_of_comprehensive_income#Requirements_of_IFRS
           

.. class:: CashFlowSheet

.. class:: AccountsBalanceSheet



Database fields
===============

.. class:: DebitOrCreditField

    A field that stores the "direction" of a movement, i.e. either
    :data:`DEBIT` or :data:`CREDIT`.

          
.. class:: DebitOrCreditStoreField

    This is used as `lino_atomizer_class` for :class:`DebitOrCreditField`.


Plugin attributes
=================

.. class:: Plugin

           
    .. attribute:: ref_length

    The `max_length` of the `Reference` field of an account.
    
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


