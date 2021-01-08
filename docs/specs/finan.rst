.. doctest docs/specs/finan.rst
.. _xl.specs.finan:
.. _specs.cosi.finan:

==============================
``finan`` : Financial vouchers
==============================

This document describes the :mod:`lino_xl.lib.finan` plugin, which introduces
concepts like :term:`financial voucher` and :term:`booking suggestion`.


.. contents::
   :depth: 1
   :local:

.. currentmodule:: lino_xl.lib.finan


.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *
>>> ses = rt.login("robin")
>>> translation.activate('en')

This document is based on the following other specifications:

- :ref:`cosi.specs.accounting`
- :ref:`cosi.specs.ledger`

Vocabulary
==========

There are three kinds of financial vouchers:

.. glossary::

  bank statement

    A :term:`ledger voucher` received from your bank and which reports the
    transactions that occurred on a given bank account during a given period.

    See `Bank statements`_.

  payment order

    A voucher you send to your bank asking them to execute a series of payments
    (outgoing transactions) to third-party partners from a given bank account.

    See `Payment orders`_.

  journal entry

    A voucher where you declare that you move money around internally, for your
    own accounting.

    French: "operations diverse".

    See `Journal entries`_.

  financial voucher

    General term for the voucher types :term:`bank statement`, :term:`payment
    order` and :term:`journal entry`.  They have certain things in common, but
    use different database models because certain things differ.

  expected movement

    A :term:`ledger movement` that did not yet happen but is expected to happen.
    For example the payment of an invoice.

  booking suggestion

    A suggestion to add an :term:`expected movement` to a :term:`financial voucher`.
    See `Booking suggestions`_.


Payment orders
==============

To configure a journal of :term:`payment orders <payment order>`, you set the
following fields:

- :attr:`voucher_type <lino_xl.lib.ledger.Journal.voucher_type>` should be
  :attr:`lino_xl.lib.ledger.VoucherTypes.bank_po`

- :attr:`partner <lino_xl.lib.ledger.Journal.partner>` ("Organization") should
  point to your bank.

- :attr:`dc <lino_xl.lib.ledger.Journal.dc>` (Primary booking direction) should
  be DEBIT because each item should debit (not credit) the partner's account.

- :attr:`account <lino_xl.lib.ledger.Journal.account>` should be the
  :term:`ledger account` marked as :attr:`CommonAccounts.pending_po
  <lino_xl.lib.ledger.CommonAccounts.pending_po>`.

A payment order clears the invoices it asks to pay.  Which means for example
that a supplier might tell you that some invoice isn't yet paid, although your
MovementsByPartner says that it is paid. The explanation for this difference is
simply that the payment order hasn't yet been executed by your or their bank.

Lino books the **sum of a payment order** into a single counter-movement that
will *debit* your bank's partner account (specified in the :attr:`partner
<Journal.partner>` of the journal).  Your bank becomes a creditor (you owe them
the sum of the payments) and you expect this amount to be cleared by an expense
in a :term:`bank statement` which confirms that the bank executed your payment
order.

>>> rt.show("finan.PaymentOrdersByJournal", ledger.Journal.get_by_ref("PMO"))
===================== ============ =========== =============== ================ =================== ================
 No.                   Entry date   Narration   Total           Execution date   Accounting period   Workflow
--------------------- ------------ ----------- --------------- ---------------- ------------------- ----------------
 2/2015                13/02/2015               6 801,22                         2015-02             **Registered**
 1/2015                13/01/2015               5 626,48                         2015-01             **Registered**
 12/2014               13/12/2014               5 878,16                         2014-12             **Registered**
 11/2014               13/11/2014               6 124,29                         2014-11             **Registered**
 10/2014               13/10/2014               5 877,47                         2014-10             **Registered**
 9/2014                13/09/2014               6 228,18                         2014-09             **Registered**
 8/2014                13/08/2014               5 707,66                         2014-08             **Registered**
 7/2014                13/07/2014               5 944,37                         2014-07             **Registered**
 6/2014                13/06/2014               6 112,07                         2014-06             **Registered**
 5/2014                13/05/2014               6 350,89                         2014-05             **Registered**
 4/2014                13/04/2014               7 061,63                         2014-04             **Registered**
 3/2014                13/03/2014               5 570,88                         2014-03             **Registered**
 2/2014                13/02/2014               5 570,38                         2014-02             **Registered**
 1/2014                13/01/2014               6 793,62                         2014-01             **Registered**
 **Total (14 rows)**                            **85 647,30**
===================== ============ =========== =============== ================ =================== ================
<BLANKLINE>


.. class:: PaymentOrder

    Django model to represent a :term:`payment order`.

    .. attribute:: entry_date

        The date of the ledger entry.

    .. attribute:: execution_date

        The execution date of payment order. If this is empty, Lino
        assumes the :attr:`entry_date` when writing the
        :xfile:`pain_001.xml` file.

    .. attribute:: total

        The total amount. This is automatically computed when you register
        de voucher.


.. class:: PaymentOrderItem

    Django model to represent an individual item of a :term:`payment order`.


.. class:: PaymentOrders

    The base table of all tables on :class:`PaymentOrder`.

.. class:: ItemsByPaymentOrder


Bank statements
===============

>>> rt.show("finan.BankStatementsByJournal", ledger.Journal.get_by_ref("BNK"))
===================== ============ =============== =============== =================== ================
 No.                   Entry date   Old balance     New balance     Accounting period   Workflow
--------------------- ------------ --------------- --------------- ------------------- ----------------
 2/2015                21/02/2015   -2 367,73       -1 723,45       2015-02             **Registered**
 1/2015                21/01/2015   2 518,58        -2 367,73       2015-01             **Registered**
 12/2014               21/12/2014   1 732,80        2 518,58        2014-12             **Registered**
 11/2014               21/11/2014   2 377,98        1 732,80        2014-11             **Registered**
 10/2014               21/10/2014   -2 395,03       2 377,98        2014-10             **Registered**
 9/2014                21/09/2014   -5 619,22       -2 395,03       2014-09             **Registered**
 8/2014                21/08/2014   -2 029,93       -5 619,22       2014-08             **Registered**
 7/2014                21/07/2014   -190,86         -2 029,93       2014-07             **Registered**
 6/2014                21/06/2014   5 846,85        -190,86         2014-06             **Registered**
 5/2014                21/05/2014   -524,23         5 846,85        2014-05             **Registered**
 4/2014                21/04/2014   -2 746,54       -524,23         2014-04             **Registered**
 3/2014                21/03/2014   288,24          -2 746,54       2014-03             **Registered**
 2/2014                21/02/2014   1 196,16        288,24          2014-02             **Registered**
 1/2014                21/01/2014                   1 196,16        2014-01             **Registered**
 **Total (14 rows)**                **-1 912,93**   **-3 636,38**
===================== ============ =============== =============== =================== ================
<BLANKLINE>

.. class:: BankStatement

    Django model to represent a :term:`bank statement`.

    .. attribute:: balance1

        The old (or start) balance.

    .. attribute:: balance2

        The new (or end) balance.

.. class:: BankStatementItem

    Django model to represent an individual item of a :term:`bank statement`.


.. class:: BankStatements

    The base table of all tables on :class:`BankStatement`.


.. class:: ItemsByBankStatement

    Shows the items of a :term:`bank statement`.



Cash journals
=============

Cash journals are technically the same as bank statements.

>>> rt.show("finan.BankStatementsByJournal", ledger.Journal.get_by_ref("CSH"))
No data to display


Journal entries
===============

>>> rt.show("finan.JournalEntriesByJournal", ledger.Journal.get_by_ref("MSC"))
No data to display

>>> rt.show("finan.JournalEntriesByJournal", ledger.Journal.get_by_ref("PRE"))
======== ============ =========== =================== ================
 No.      Entry date   Narration   Accounting period   Workflow
-------- ------------ ----------- ------------------- ----------------
 1/2014   01/01/2014               2014-01             **Registered**
======== ============ =========== =================== ================
<BLANKLINE>


.. class:: JournalEntry

    Django model to represent a :term:`journal entry`.

.. class:: JournalEntryItem

    Django model to represent an individual item of a :term:`journal entry`.

.. class:: JournalEntries

    The base table of all tables on :class:`JournalEntry`.

.. class:: ItemsByJournalEntry

    Shows the items of a journal entry.




Model mixins
============

.. class:: FinancialVoucher

    Base class for all :term:`financial vouchers <financial voucher>`.

    .. attribute:: item_account

        The default value to use when
        :attr:`FinancialVoucherItem.account` of an item is empty.

    .. attribute:: item_remark

        The default value to use when
        :attr:`FinancialVoucherItem.remark` of an item is empty.

    .. attribute:: printed
        See :attr:`lino_xl.lib.excerpts.mixins.Certifiable.printed`


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


In a :term:`bank statement` you might want to specify an individual date for
every item.

.. class:: DatedFinancialVoucher

    A :class:`FinancialVoucher` whose items have a :attr:`date` field.


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

    Base class for the default tables of all financial voucher
    types (:class:`JournalEntries` , :class:`PaymentOrders` and
    :class:`BankStatements`).

.. class:: ItemsByVoucher

    The base table of all tables which display the items of a given
    voucher.


Booking suggestions
===================

In a financial voucher you often book transactions that are actually expected.
When you have booked your invoices, then Lino "knows" that each invoice will
--ideally-- lead to a payment.

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


.. class:: ShowSuggestions

    Show suggested items for this voucher.

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


.. class:: FinancialVoucherItemChecker
