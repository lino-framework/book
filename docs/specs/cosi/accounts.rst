.. _xl.specs.accounts:


=====================
The `accounts` plugin
=====================

.. how to test this document:

    $ python setup.py test -s tests.SpecsTests.test_accounting

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


Account types
=============

Lino has a list of **account types** or "top-level accounts", defined
in :class:`AccountTypes`.

>>> rt.show(ledger.AccountTypes, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= =============== =============== ======== ===============
 value   name            text            D/C      Sheet
------- --------------- --------------- -------- ---------------
 A       assets          Assets          Debit    BalanceSheet
 L       liabilities     Liabilities     Credit   BalanceSheet
 I       incomes         Incomes         Credit   EarningsSheet
 E       expenses        Expenses        Debit    EarningsSheet
 C       capital         Capital         Credit   BalanceSheet
 B       bank_accounts   Bank accounts   Debit    BalanceSheet
======= =============== =============== ======== ===============
<BLANKLINE>

Each item in above list is defined as a Python class as well.

.. class:: AccountType
           
    The base class for all **account types**.

The five basic account types are:    
           
.. class:: Assets
.. class:: Liabilities
.. class:: Capital
.. class:: Income
.. class:: Expenses

A **bank account** is a subclass of an asset:

.. class:: BankAccounts

   A subclass of :class:`Assets`.
           
.. class:: AccountTypes

    The global list of account types. See :class:`AccountType`.


The same in French and German:

>>> rt.show(ledger.AccountTypes, language="fr")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= =============== =================== ======== ===============
 value   name            text                D/C      Sheet
------- --------------- ------------------- -------- ---------------
 A       assets          Actifs              Débit    BalanceSheet
 L       liabilities     Passifs             Crédit   BalanceSheet
 I       incomes         Revenus             Crédit   EarningsSheet
 E       expenses        Dépenses            Débit    EarningsSheet
 C       capital         Capital             Crédit   BalanceSheet
 B       bank_accounts   Comptes en banque   Débit    BalanceSheet
======= =============== =================== ======== ===============
<BLANKLINE>

>>> rt.show(ledger.AccountTypes, language="de")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
====== =============== ================= ======== ===============
 Wert   name            Text              D/C      Sheet
------ --------------- ----------------- -------- ---------------
 A      assets          Vermögen          Débit    BalanceSheet
 L      liabilities     Verpflichtungen   Kredit   BalanceSheet
 I      incomes         Einkünfte         Kredit   EarningsSheet
 E      expenses        Ausgaben          Débit    EarningsSheet
 C      capital         Kapital           Kredit   BalanceSheet
 B      bank_accounts   Bankkonten        Débit    BalanceSheet
====== =============== ================= ======== ===============
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
<AccountType.dc>` attribute means:

>>> print(unicode(DCLABELS[AccountTypes.assets.dc]))
Debit
>>> print(unicode(DCLABELS[AccountTypes.expenses.dc]))
Debit

>>> print isinstance(AccountTypes.bank_accounts,Assets)
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

>>> for t in AccountTypes.filter(top_level=True):
... #doctest: +NORMALIZE_WHITESPACE
...     print "%-12s|%-15s|%-6s" % (t.name, unicode(t), DCLABELS[t.dc])
assets      |Assets         |Debit
liabilities |Liabilities    |Credit
incomes     |Incomes        |Credit
expenses    |Expenses       |Debit
capital     |Capital        |Credit


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

>>> print Sheet.objects
(<class 'lino_xl.lib.accounts.choicelists.BalanceSheet'>, <class 'lino_xl.lib.accounts.choicelists.EarningsSheet'>, <class 'lino_xl.lib.accounts.choicelists.CashFlowSheet'>)

The `verbose_name` is what users see. It is a lazily translated
string, so we must call `unicode()` to see it:

>>> for s in Sheet.objects:
...     print(unicode(s.verbose_name))
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

>>> print(BalanceSheet.account_types())
[<AccountTypes.assets:A>, <AccountTypes.liabilities:L>, <AccountTypes.capital:C>]

>>> print(EarningsSheet.account_types())
[<AccountTypes.incomes:I>, <AccountTypes.expenses:E>]

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
        :class:`AccountTypes
        <lino_xl.lib.accounts.choicelists.AccountTypes>`.
    
    .. attribute:: needs_partner

        Whether bookings to this account need a partner specified.

        This causes the contra entry of financial documents to be
        detailed (i.e. one for every item) or not (i.e. a single
        contra entry per voucher, without project nor partner).

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
