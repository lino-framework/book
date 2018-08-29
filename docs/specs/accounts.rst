.. doctest docs/specs/accounts.rst
.. _xl.specs.accounts:


========
Accounts
========

.. Doctest initialization:

    >>> import lino
    >>> lino.startup('lino_book.projects.pierre.settings.demo')
    >>> from lino.api.doctest import *


The :mod:`lino_xl.lib.accounts` plugin adds some basic notions of
accounting: the :class:`Account` model and a choicelist
:class:`CommonAccounts`.  The plugin is normally used together with
the :mod:`lino_xl.lib.ledger` plugin.

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
        
    .. attribute:: sheet_item

        Pointer to the item of the balance sheet or income statement
        that will report the movements of this account.

        This file is a dummy field when :mod:`lino_xl.lib.sheets` is
        not installed.



Common accounts
===============

The `accounts` plugin defines a choicelist of **common accounts**
which are used to reference the database object for certain accounts
which have a special meaning.

.. class:: CommonAccounts

    The global list of common accounts.

    This is a :class:`lino.core.choicelists.ChoiceList`.
    Every item is an instance of :class:`CommonAccount`.

.. class:: CommonAccount
           
    The base class for items of ::class:`CommonAccounts`.
    It defines two additional attributes:

    .. attribute:: clearable
    .. attribute:: needs_partner



Here is the standard list of common accounts in a :ref:`cosi`
application:

>>> rt.show(accounts.CommonAccounts, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= ========================= ========================= =========== ================================
 value   name                      text                      Clearable   Account
------- ------------------------- ------------------------- ----------- --------------------------------
 1000    net_income_loss           Net income (loss)         Yes         (1000) Net income (loss)
 4000    customers                 Customers                 Yes         (4000) Customers
 4300    pending_po                Pending Payment Orders    Yes         (4300) Pending Payment Orders
 4400    suppliers                 Suppliers                 Yes         (4400) Suppliers
 4500    employees                 Employees                 Yes         (4500) Employees
 4600    tax_offices               Tax Offices               Yes         (4600) Tax Offices
 4510    vat_due                   VAT due                   No          (4510) VAT due
 4511    vat_returnable            VAT returnable            No          (4511) VAT returnable
 4512    vat_deductible            VAT deductible            No          (4512) VAT deductible
 4513    due_taxes                 VAT declared              No          (4513) VAT declared
 4900    waiting                   Waiting account           Yes         (4900) Waiting account
 5500    best_bank                 BestBank                  No          (5500) BestBank
 5700    cash                      Cash                      No          (5700) Cash
 6040    purchase_of_goods         Purchase of goods         No          (6040) Purchase of goods
 6010    purchase_of_services      Purchase of services      No          (6010) Purchase of services
 6020    purchase_of_investments   Purchase of investments   No          (6020) Purchase of investments
 6300    wages                     Wages                     No          (6300) Wages
 6900    net_income                Net income                No          (6900) Net income
 7000    sales                     Sales                     No          (7000) Sales
 7900    net_loss                  Net loss                  No          (7900) Net loss
======= ========================= ========================= =========== ================================
<BLANKLINE>

Lino applications can add specific items to that list or potentially
redefine it completely


Debit and credit
================
        
The balance of an account
=========================

The **balance** of an account is the amount of money in that account.

An account balance is either Debit or Credit.  We represent this
internally as a boolean, but define two names `DEBIT` and `CREDIT`:

>>> from lino_xl.lib.accounts.utils import DEBIT, CREDIT
>>> from lino_xl.lib.accounts.utils import Balance
>>> DEBIT
True
>>> CREDIT
False

.. class:: Balance
           
    Light-weight object to represent a balance, i.e. an amount
    together with its booking direction (debit or credit).

    Attributes:

    .. attribute:: d

        The amount of this balance when it is debiting, otherwise zero.

    .. attribute:: c

        The amount of this balance when it is crediting, otherwise zero.

       
A negative value on one side of the balance is automatically moved to
the other side.

>>> Balance(10, -2)
Balance(12,0)



Database fields
===============

.. class:: DebitOrCreditField

    A field that stores the "direction" of a movement, i.e. either
    :data:`DEBIT` or :data:`CREDIT`.

          
.. class:: DebitOrCreditStoreField

    This is used as `lino_atomizer_class` for :class:`DebitOrCreditField`.


Plugin attributes
=================

See :class:`lino_xl.lib.accounts.Plugin`.

          

