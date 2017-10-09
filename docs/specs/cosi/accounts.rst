.. _xl.specs.accounts:


=====================
The `accounts` plugin
=====================

.. how to test this document:

    $ doctest docs/specs/cosi/accounts.rst

    Doctest initialization:

    >>> import lino
    >>> lino.startup('lino_book.projects.pierre.settings.demo')
    >>> from lino.api.doctest import *


The :mod:`lino_xl.lib.accounts` plugin defines the "static" part of
accounting stuff.

.. currentmodule:: lino_xl.lib.accounts



Debit and Credit
================

An accounting balance is either Debit or Credit.  We represent this
internally as a boolean, but define two names `DEBIT` and `CREDIT`:

>>> from lino_xl.lib.accounts.models import *
>>> DEBIT
True
>>> CREDIT
False


Common accounts
===============

Lino has a list of **common accounts** or "top-level accounts", defined
in :class:`CommonAccounts`.

>>> rt.show(accounts.CommonAccounts, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= ========================= ========================= ======== ===============
 value   name                      text                      D/C      Sheet
------- ------------------------- ------------------------- -------- ---------------
 A       assets                    Assets                    Debit    BalanceSheet
 L       liabilities               Liabilities               Credit   BalanceSheet
 C       capital                   Capital                   Credit   BalanceSheet
 I       incomes                   Incomes                   Credit   EarningsSheet
 E       expenses                  Expenses                  Debit    EarningsSheet
 55      bank_accounts             Bank accounts             Debit    BalanceSheet
 4000    customers                 Customers                 Debit    BalanceSheet
 4400    suppliers                 Suppliers                 Credit   BalanceSheet
 4600    tax_offices               Tax Offices               Credit   BalanceSheet
 4500    employees                 Employees                 Credit   BalanceSheet
 4700    pending_po                Pending Payment Orders    Debit    BalanceSheet
 4510    vat_due                   VAT Due                   Credit   BalanceSheet
 4511    vat_returnable            VAT Returnable            Credit   BalanceSheet
 4512    vat_deductible            VAT Deductible            Credit   BalanceSheet
 4513    due_taxes                 VAT Declared              Credit   BalanceSheet
 5500    best_bank                 BestBank                  Debit    BalanceSheet
 5700    cash                      BestBank                  Debit    BalanceSheet
 6040    purchase_of_goods         Purchase of goods         Debit    EarningsSheet
 6010    purchase_of_services      Purchase of services      Debit    EarningsSheet
 6020    purchase_of_investments   Purchase of investments   Debit    EarningsSheet
 6300    wages                     Wages                     Debit    EarningsSheet
 7000    sales                     Sales                     Credit   EarningsSheet
 7310    membership_fee            Membership Fees           Credit   EarningsSheet
======= ========================= ========================= ======== ===============
<BLANKLINE>

Each item in above list is defined as a Python class as well.

.. class:: CommonAccount
           
    The base class for all **common accounts**.

The five basic account types are:    
           
.. class:: Assets
.. class:: Liabilities
.. class:: Capital
.. class:: Income
.. class:: Expenses

A **bank account** is a subclass of an asset:

.. class:: BankAccounts

   A subclass of :class:`Assets`.
           
.. class:: CommonAccounts

    The global list of common accounts. See :class:`CommonAccount`.


The same in French and German:

>>> rt.show(accounts.CommonAccounts, language="fr")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= ========================= ========================= ======== ===============
 value   name                      text                      D/C      Sheet
------- ------------------------- ------------------------- -------- ---------------
 A       assets                    Actifs                    Débit    BalanceSheet
 L       liabilities               Passifs                   Crédit   BalanceSheet
 C       capital                   Capital                   Crédit   BalanceSheet
 I       incomes                   Revenus                   Crédit   EarningsSheet
 E       expenses                  Dépenses                  Débit    EarningsSheet
 55      bank_accounts             Comptes en banque         Débit    BalanceSheet
 4000    customers                 Customers                 Débit    BalanceSheet
 4400    suppliers                 Suppliers                 Crédit   BalanceSheet
 4600    tax_offices               Tax Offices               Crédit   BalanceSheet
 4500    employees                 Employees                 Crédit   BalanceSheet
 4700    pending_po                Pending Payment Orders    Débit    BalanceSheet
 4510    vat_due                   VAT Due                   Crédit   BalanceSheet
 4511    vat_returnable            VAT Returnable            Crédit   BalanceSheet
 4512    vat_deductible            VAT Deductible            Crédit   BalanceSheet
 4513    due_taxes                 VAT Declared              Crédit   BalanceSheet
 5500    best_bank                 BestBank                  Débit    BalanceSheet
 5700    cash                      BestBank                  Débit    BalanceSheet
 6040    purchase_of_goods         Purchase of goods         Débit    EarningsSheet
 6010    purchase_of_services      Purchase of services      Débit    EarningsSheet
 6020    purchase_of_investments   Purchase of investments   Débit    EarningsSheet
 6300    wages                     Salaires                  Débit    EarningsSheet
 7000    sales                     Sales                     Crédit   EarningsSheet
 7310    membership_fee            Membership Fees           Crédit   EarningsSheet
======= ========================= ========================= ======== ===============
<BLANKLINE>

>>> rt.show(accounts.CommonAccounts, language="de")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
====== ========================= ========================= ======== ===============
 Wert   name                      Text                      D/C      Sheet
------ ------------------------- ------------------------- -------- ---------------
 A      assets                    Vermögen                  Débit    BalanceSheet
 L      liabilities               Verpflichtungen           Kredit   BalanceSheet
 C      capital                   Kapital                   Kredit   BalanceSheet
 I      incomes                   Einkünfte                 Kredit   EarningsSheet
 E      expenses                  Ausgaben                  Débit    EarningsSheet
 55     bank_accounts             Bankkonten                Débit    BalanceSheet
 4000   customers                 Customers                 Débit    BalanceSheet
 4400   suppliers                 Suppliers                 Kredit   BalanceSheet
 4600   tax_offices               Tax Offices               Kredit   BalanceSheet
 4500   employees                 Employees                 Kredit   BalanceSheet
 4700   pending_po                Pending Payment Orders    Débit    BalanceSheet
 4510   vat_due                   VAT Due                   Kredit   BalanceSheet
 4511   vat_returnable            VAT Returnable            Kredit   BalanceSheet
 4512   vat_deductible            VAT Deductible            Kredit   BalanceSheet
 4513   due_taxes                 VAT Declared              Kredit   BalanceSheet
 5500   best_bank                 BestBank                  Débit    BalanceSheet
 5700   cash                      BestBank                  Débit    BalanceSheet
 6040   purchase_of_goods         Purchase of goods         Débit    EarningsSheet
 6010   purchase_of_services      Purchase of services      Débit    EarningsSheet
 6020   purchase_of_investments   Purchase of investments   Débit    EarningsSheet
 6300   wages                     Löhne und Gehälter        Débit    EarningsSheet
 7000   sales                     Verkauf                   Kredit   EarningsSheet
 7310   membership_fee            Membership Fees           Kredit   EarningsSheet
====== ========================= ========================= ======== ===============
<BLANKLINE>


.. 
  >>> translation.activate('en')



The basic `Accounting Equation
<https://en.wikipedia.org/wiki/Accounting_equation>`_ states:

  Assets = Liabilities + Capital
 
And the expanded accounting equation is:

    Assets + Expenses = Liabilities + Equity + Revenue
    

Accounts on the left side of the equation (Assets and Expenses) are
normally DEBITed and have DEBIT balances.  That's what the :attr:`dc
<CommonAccount.dc>` attribute means:

>>> print(unicode(DCLABELS[CommonAccounts.assets.dc]))
Debit
>>> print(unicode(DCLABELS[CommonAccounts.expenses.dc]))
Debit

>>> from lino_xl.lib.accounts.choicelists import Assets
>>> print isinstance(CommonAccounts.bank_accounts, Assets)
True


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
  
The equivalent in Python is:

>>> for t in CommonAccounts.filter(top_level=True):
... #doctest: +NORMALIZE_WHITESPACE
...     print "%-12s|%-15s|%-6s" % (t.name, unicode(t), DCLABELS[t.dc])
assets      |Assets         |Debit 
liabilities |Liabilities    |Credit
capital     |Capital        |Credit
incomes     |Incomes        |Credit
expenses    |Expenses       |Debit 


The :class:`Sheet` class
------------------------

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
(<class 'lino_xl.lib.accounts.choicelists.BalanceSheet'>, <class 'lino_xl.lib.accounts.choicelists.EarningsSheet'>, <class 'lino_xl.lib.accounts.choicelists.CashFlowSheet'>)

The `verbose_name` is what users see. It is a lazily translated
string, so we must call `unicode()` to see it:

>>> for s in Sheet.objects:
...     print(s.verbose_name)
Balance sheet
Profit & Loss statement
Cash flow statement

French users will see:

>>> from django.utils import translation
>>> with translation.override('fr'):
...     for s in Sheet.objects:
...         print unicode(s.verbose_name)
Bilan
Compte de résultats
Tableau de financement


The :meth:`Sheet.account_types` method.

Assets, Liabilities and Capital are listed in the Balance Sheet.
Income and Expenses are listed in the Profit & Loss statement.

>>> from lino_xl.lib.accounts.choicelists import BalanceSheet, EarningsSheet, CashFlowSheet
>>> print(BalanceSheet.account_types())
[<CommonAccounts.assets:A>, <CommonAccounts.liabilities:L>, <CommonAccounts.capital:C>]

>>> print(EarningsSheet.account_types())
[<CommonAccounts.incomes:I>, <CommonAccounts.expenses:E>]

>>> print(CashFlowSheet.account_types())
[]



TODO
----

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

           

Account groups
==============

.. class:: Group
           
    A group of accounts.

.. class:: Groups
           
    The global table of all account groups.
           
Utilities
=========

.. class:: Sheet
           
    Base class for a financial statement.
           
.. class:: Balance
           
    Light-weight object to represent a balance, i.e. an amount
    together with its booking direction (debit or credit).

    Attributes:

    .. attribute:: d

        The amount of this balance when it is debiting, otherwise zero.

    .. attribute:: c

        The amount of this balance when it is crediting, otherwise zero.


Account sheets
==============

.. class:: BalanceSheet

    In financial accounting, a balance sheet or statement of financial
    position is a summary of the financial balances of an
    organisation.

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
