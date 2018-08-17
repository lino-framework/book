.. doctest docs/specs/finan.rst
.. _xl.specs.finan:
.. _specs.cosi.finan:

==================
Financial vouchers
==================

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.pierre.settings.doctests')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")
    >>> translation.activate('en')

This document describes what we call **financial vouchers** as
implemented by the :mod:`lino_xl.lib.finan` plugin.

There are three kinds of financial vouchers:

- *bank statements* are these documents you receive from your bank and
  which shows the activities on your account.
 
- A *payment order* is a document where you ask your bank to pay some
  money to somebody else.
  
- a *journal entry* is when you move money around internally, for your
  own acounting. For example...

It is based on the following other specifications:

- :ref:`cosi.specs.accounting`
- :ref:`cosi.specs.ledger`

Table of contents:


.. contents::
   :depth: 1
   :local:



.. currentmodule:: lino_xl.lib.finan


Database models
===============

.. class:: JournalEntry
           
    This is the model for "journal entries" ("operations diverses").

.. class:: BankStatement

    A **bank statement** is a document issued by the bank, which
    reports all transactions which occured on a given account during a
    given period.

    .. attribute:: balance1

        The old (or start) balance.

    .. attribute:: balance2

        The new (or end) balance.

.. class:: PaymentOrder
           
    A **payment order** is when a user instructs a bank to execute a
    series of outgoing transactions from a given bank account.

    .. attribute:: entry_date

        The date of the ledger entry.
        
    .. attribute:: execution_date

        The execution date of payment order. If this is empty, Lino
        assumes the :attr:`entry_date` when writing the 
        :xfile:`pain_001.xml` file.

    .. attribute:: total

        The total amount. This is automatically computed when you register
        de voucher.


.. class:: JournalEntryItem
           
    An item of a :class:`JournalEntry`.

.. class:: BankStatementItem
           
    An item of a :class:`BankStatement`.

.. class:: PaymentOrderItem

    An item of a :class:`PaymentOrder`.
    

Model mixins
============

.. class:: FinancialVoucher    

    Base class for all financial vouchers:
    :class:`Grouper`,
    :class:`JournalEntry`,
    :class:`PaymentOrder` and
    :class:`BankStatement`.

    .. attribute:: item_account

        The default value to use when
        :attr:`FinancialVoucherItem.account` of an item is empty.

    .. attribute:: item_remark

        The default value to use when
        :attr:`FinancialVoucherItem.remark` of an item is empty.

    .. attribute:: printed
        See :attr:`lino_xl.lib.excerpts.mixins.Certifiable.printed`


.. class:: DatedFinancialVoucher
    A :class:`FinancialVoucher` whose items have a :attr:`date` field.

    
.. class:: FinancialVoucherItem
    
    The base class for the items of all types of financial vouchers
    (:class:`FinancialVoucher`).

    .. attribute:: account

        The general account to be used in the primary booking.
        If this is empty, use :attr:`item_account` of the voucher.

    .. attribute:: project

        The "project" related to this transaction. For example in Lino
        Welfare this is the client.

    .. attribute:: partner

        The partner account to be used in the primary booking.
    
        In Lino Welfare this field is optional and used only for
        transactions whose *recipient* is different from the *client*.
        When empty, Lino will book to the **client**
        (i.e. :attr:`project`).

    .. attribute:: amount

        The amount to be booked. If this is empty, then the voucher
        cannot be registered.

    .. attribute:: dc

        The direction of the primary booking to create.

    .. attribute:: remark

        External reference. The description of this transation
        as seen by the external partner.

    .. attribute:: seqno

    .. attribute:: match

        An arbitrary string used to group several movements.

        A reference to the voucher that caused this voucher entry.  For
        example the :attr:`match` of the payment of an invoice points
        to that invoice.


.. class:: DatedFinancialVoucherItem

    A :class:`FinancialVoucherItem` with an additional :attr:`date`
    field.

    .. attribute:: date

        The value date of this item.

           
Plugin configuration
====================

.. class:: Plugin
      

    This :class:`Plugin <lino.core.plugin.Plugin>` class adds some
    entries to the Explorer menu.  It contains the following
    additional attributes:

    .. attribute:: suggest_future_vouchers

        Whether to suggest vouchers whose due_date is in the future.

        The default value is currently `False` because some demo fixtures
        rely on this.  But in most cases this should probably be set to
        `True` because of course a customer can pay an invoice in advance.

        You can specify this for your application::

            def setup_plugins(self):
                self.plugins.finan.suggest_future_vouchers = True
                super(Site, self).setup_plugins()

        Or, as a local system administrator you can also simply set it
        after your :data:`SITE` instantiation::

            SITE = Site(globals())
            ...
            SITE.plugins.finan.suggest_future_vouchers = True

           
Tables
======

.. class:: FinancialVouchers
           
    Base class for the default tables of all other financial voucher
    types (:class:`JournalEntries` , :class:`PaymentOrders` and
    :class:`BankStatements`).

.. class:: JournalEntries
           
.. class:: PaymentOrders
           
    The base table of all tables on :class:`PaymentOrder`.
    
.. class:: BankStatements

    The base table of all tables on :class:`BankStatement`.
           

.. class:: ItemsByVoucher
           
    The base table of all tables which display the items of a given
    voucher.

.. class:: ItemsByJournalEntry
.. class:: ItemsByPaymentOrder
.. class:: ItemsByBankStatement
    
           
.. class:: SuggestionsByVoucher
           
    Shows the suggested items for a given voucher, with a button to
    fill them into the current voucher.

    This is the base class for
    :class:`SuggestionsByJournalEntry`
    :class:`SuggestionsByBankStatement` and
    :class:`SuggestionsByPaymentOrder` who define the class of the
    master_instance (:attr:`master <lino.core.actors.Actor.master>`)

    This is an abstract virtual slave table.

    Every row is a :class:`DueMovement
    <lino_xl.lib.ledger.utils.DueMovement>` object.

.. class:: SuggestionsByJournalEntry
           
    A :class:`SuggestionsByVoucher` table for a :class:`JournalEntry`.
    
.. class:: SuggestionsByPaymentOrder
           
    A :class:`SuggestionsByVoucher` table for a :class:`PaymentOrder`.
    
.. class:: SuggestionsByBankStatement
           
    A :class:`SuggestionsByVoucher` table for a :class:`BankStatement`.
    

.. class:: SuggestionsByVoucherItem    

    Displays the payment suggestions for a given voucher *item*, with
    a button to fill them into the current item (creating additional
    items if more than one suggestion was selected).

    
    
.. class:: SuggestionsByJournalEntryItem

.. class:: SuggestionsByPaymentOrderItem
           
    A :class:`SuggestionsByVoucherItem` table for a
    :class:`PaymentOrderItem`.


.. class:: SuggestionsByBankStatementItem
           
    A :class:`SuggestionsByVoucherItem` table for a
    :class:`BankStatementItem`.

Actions
=======


.. class:: ShowSuggestions
           
    Show suggested items for this voucher.

.. class:: SuggestionsByVoucher

.. class:: FillSuggestionsToVoucher           

    Fill selected suggestions from a SuggestionsByVoucher table into a
    financial voucher.

    This creates one voucher item for each selected row.

.. class:: FillSuggestionsToVoucherItem
           
    Fill the selected suggestions as items to the voucher. The *first*
    selected suggestion does not create a new item but replaces the
    item for which it was called.
    

Template files
==============
    
.. xfile:: pain_001.xml

   Used for writing a SEPA payment initiation.

   :file:`finan/PaymentOrder/pain_001.xml`
        
