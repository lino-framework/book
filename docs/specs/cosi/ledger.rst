.. _xl.specs.ledger:
.. _cosi.specs.ledger:
.. _cosi.tested.ledger:

=================================================
The General Ledger: moving money between accounts
=================================================

The :mod:`lino_xl.lib.ledger` plugin defines the "dynamic" part of
general accounting stuff.  You application needs it when you are
moving money between accounts.  You should have read :doc:`accounts`
before reading this document.

.. currentmodule:: lino_xl.lib.ledger

.. to test only this document:

      $ python setup.py test -s tests.SpecsTests.test_ledger
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.pierre.settings.demo')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")
    >>> translation.activate('en')


Table of contents:

.. contents::
   :depth: 1
   :local:


Overview
========

A **ledger** is a book in which the monetary transactions of a
business are posted in the form of debits and credits (from `1
<http://www.thefreedictionary.com/ledger>`__).

In Lino, the ledger is implemented by three database models:

- A :class:`Movement` is an atomic "transfer" on a given date of a
  given *amount* of money out of (or into) a given *account*.  It is
  just a *conceptual* transfer, not a cash or bank transfer.  Moving
  money *out of* an account is called "to debit", moving money *to* an
  account is called "to credit".

- Movements are never created individually but by *registering* a
  :class:`Voucher`.  A voucher is any document which serves as legal
  proof for a **ledger transaction**.  A ledger transaction consists of
  *at least two* movements, and the sum of *debited* money in these
  movements must equal the sum of *credited* money.

  Examples of vouchers include invoices, bank statements, or payment
  orders.

  Vouchers are stored in the database using some subclass of the
  :class:`Voucher` model. Note that the voucher model is never being
  used directly.

- When a voucher is registered, it receives a sequence number in a
  :class:`Journal`.  A journal is a serieas of vouchers, numbered
  sequentially and in chronological order.

There are some secondary models and choicelists:  

- Each ledger movement happens in a given **fiscal year**.
  

And then there are many subtle ways for looking at this data.

- :class:`GeneralAccountsBalance`, :class:`CustomerAccountsBalance` and
  :class:`SupplierAccountsBalance` three reports based on
  :class:`AccountsBalance` and :class:`PartnerAccountsBalance`

- :class:`Debtors` and :class:`Creditors` are tables with one row for
  each partner who has a positive balance (either debit or credit).
  Accessible via :menuselection:`Reports --> Ledger --> Debtors` and
  :menuselection:`Reports --> Ledger --> Creditors`

Models and actors reference
===========================

.. class:: MatchRule

    A **match rule** specifies that a movement into given account can
    be cleared using a given journal.


.. class:: Movement

    Represents an accounting movement in the ledger.

    .. attribute:: value_date

        The date at which this movement is to be entered into the
        ledger.  This is usually the voucher's :attr:`entry_date
        <lino_xl.lib.ledger.models.Voucher.entry_date>`, except
        e.g. for bank statements where each item can have its own
        value date.

    .. attribute:: voucher

        Pointer to the :class:`Voucher` who caused this movement.

    .. attribute:: partner

        Pointer to the partner involved in this movement. This may be
        blank.

    .. attribute:: seqno

        Sequential number within a voucher.

    .. attribute:: account

        Pointer to the :class:`Account` that is being moved by this movement.

    .. attribute:: amount
    .. attribute:: dc

    .. attribute:: match

        Pointer to the :class:`Movement` that is being cleared by this
        movement.

    .. attribute:: cleared

        Whether

    .. attribute:: voucher_partner

        A virtual field which returns the *partner of the voucher*.
        For incoming invoices this is the supplier, for outgoing
        invoices this is the customer, for financial vouchers this is
        empty.

    .. attribute:: voucher_link

        A virtual field which shows a link to the voucher.

    .. attribute:: match_link

        A virtual field which shows a clickable variant of the match
        string. Clicking it will open a table with all movements
        having that match.

           
.. class:: Voucher
           
    A Voucher is a document that represents a monetary transaction.

    It is *not* abstract so that :class:`Movement` can have a ForeignKey
    to a Voucher.

    A voucher is never instantiated using this base model but using
    one of its subclasses. Examples of subclassed are sales.Invoice,
    vat.AccountInvoice (or vatless.AccountInvoice), finan.Statement
    etc...
    
    Subclasses must define a field `state`.

    .. attribute:: journal

        The journal into which this voucher has been booked. This is a
        mandatory pointer to a :class:`Journal` instance.

    .. attribute:: number

        The sequence number of this voucher in the :attr:`journal`.

        The voucher number is automatically assigned when the voucher
        is saved for the first time.  The voucher number depends on
        whether :attr:`yearly_numbering` is enabled or not.

        There might be surprising numbering if two users create
        vouchers in a same journal at the same time.

    .. attribute:: entry_date

        The date of the journal entry, i.e. when this voucher has been
        journalized or booked.

    .. attribute:: voucher_date

        The date on the voucher, i.e. when this voucher has been
        issued by its emitter.

    .. attribute:: accounting_period

        The accounting period and fiscal year to which this entry is
        to be assigned to. The default value is determined from
        :attr:`entry_date`.

    .. attribute:: narration

        A short explanation which ascertains the subject matter of
        this journal entry.

    .. attribute:: number_with_year



           
.. class:: PaymentTerm
           
    The payment term of an invoice is a convention on how the invoice
    should be paid.

    The following fields define the default value for `due_date`:

    .. attribute:: days

        Number of days to add to :attr:`voucher_date`.

    .. attribute:: months

        Number of months to add to :attr:`voucher_date`.

    .. attribute:: end_of_month

        Whether to move :attr:`voucher_date` to the end of month.

    .. attribute:: printed_text

        Used in :xfile:`sales/VatProductInvoice/trailer.html` as
        follows::

            {% if obj.payment_term.printed_text %}
            {{parse(obj.payment_term.printed_text)}}
            {% else %}
            {{_("Payment terms")}} : {{obj.payment_term}}
            {% endif %}

    The :attr:`printed_text` field is important when using
    **prepayments** or other more complex payment terms.  Lino uses a
    rather simple approach to handle prepayment invoices: only the
    global amount and the final due date is stored in the database,
    all intermediate amounts and due dates are just generated in the
    printable document. You just define one :class:`PaymentTerm
    <lino_xl.lib.ledger.models.PaymentTerm>` row for each prepayment
    formula and configure your :attr:`printed_text` field. For
    example::

        Prepayment <b>30%</b> 
        ({{(obj.total_incl*30)/100}} {{obj.currency}})
        due on <b>{{fds(obj.due_date)}}</b>, remaining 
        {{obj.total_incl - (obj.total_incl*30)/100}} {{obj.currency}}
        due 10 days before delivery.

.. class:: AccountingPeriod

    An **accounting period** is the smallest time slice to be observed
    (declare) in accounting reports. Usually it corresponds to one
    *month*. Except for some small companies which declare per
    quarter.

    For each period it is possible to specify the exact dates during
    which it is allowed to register vouchers into this period, and
    also its "state": whether it is "closed" or not.

    .. attribute:: start_date
    .. attribute:: end_date
    .. attribute:: state
    .. attribute:: year
    .. attribute:: ref
    

    """
           
.. class:: Journal

    A **journal** is a named sequence of numbered *vouchers*.

    **Fields:**

    .. attribute:: ref
    .. attribute:: trade_type

        Pointer to :class:`TradeTypes`.

    .. attribute:: voucher_type

        Pointer to an item of :class:`VoucherTypes`.

    .. attribute:: journal_group

        Pointer to an item of :class:`JournalGroups`.

    .. attribute:: yearly_numbering

        Whether the
        :attr:`number<lino_xl.lib.ledger.models.Voucher.number>` of
        vouchers should restart at 1 every year.

    .. attribute:: force_sequence

    .. attribute:: account
    .. attribute:: printed_name
    .. attribute:: dc

        The primary booking direction.

        In a journal of *sales invoices* this should be *Debit*
        (checked), because a positive invoice total should be
        *debited* from the customer's account.

        In a journal of *purchase invoices* this should be *Credit*
        (not checked), because a positive invoice total should be
        *credited* from the supplier's account.

        In a journal of *bank statements* this should be *Debit*
        (checked), because a positive balance change should be
        *debited* from the bank's general account.

        In a journal of *payment orders* this should be *Credit* (not
        checked), because a positive total means an "expense" and
        should be *credited* from the journal's general account.

        In all financial vouchers, the amount of every item increases
        the total if its direction is opposite of the primary
        direction.

    .. attribute:: auto_check_clearings

        Whether to automatically check and update the 'cleared' status
        of involved transactions when (de)registering a voucher of
        this journal.

        This can be temporarily disabled e.g. by batch actions in
        order to save time.

    .. attribute:: template

        See :attr:`PrintableType.template
        <lino.mixins.printable.PrintableType.template>`.

    
          
.. class:: Journals

   The default table showing all instances of :class:`Journal`.

.. class:: ByJournal

   Mixin for journal-based tables of vouchers.
           
.. class:: Vouchers

    The base table for all tables working on :class:`Voucher`.
               
.. class:: ExpectedMovements

    A virtual table of :class:`DueMovement` rows, showing
    all "expected" "movements (payments)".

    Subclasses are :class:`DebtsByAccount` and :class:`DebtsByPartner`.

    Also subclassed by
    :class:`lino_xl.lib.finan.SuggestionsByVoucher`.

    .. attribute:: date_until
    .. attribute:: trade_type
    .. attribute:: from_journal
    .. attribute:: for_journal
    .. attribute:: account
    .. attribute:: partner
    .. attribute:: project
    .. attribute:: show_sepa

           
.. class:: DebtsByAccount

    The :class:`ExpectedMovements` accessible by clicking the "Debts"
    action button on an account.

.. class:: DebtsByPartner

    This is the table being printed in a Payment Reminder.  Usually
    this table has one row per sales invoice which is not fully paid.
    But several invoices ("debts") may be grouped by match.  If the
    partner has purchase invoices, these are deduced from the balance.

    This table is accessible by clicking the "Debts" action button on
    a Partner.


.. class:: PartnerVouchers    

    Base class for tables of partner vouchers.

    .. attribute:: cleared

        - Yes : show only completely cleared vouchers.
        - No : show only vouchers with at least one open partner movement.
        - empty: don't care about movements.


.. class:: AccountsBalance

    A virtual table, the base class for different reports that show a
    list of accounts with the following columns:

      ref description old_d old_c during_d during_c new_d new_c

    Subclasses are :class:'GeneralAccountsBalance`,
    :class:'CustomerAccountsBalance` and
    :class:'SupplierAccountsBalance`.

.. class:: GeneralAccountsBalance

    An :class:`AccountsBalance` for general accounts.           

.. class:: PartnerAccountsBalance
           
    An :class:`AccountsBalance` for partner accounts.

.. class:: CustomerAccountsBalance
           
    A :class:`PartnerAccountsBalance` for the TradeType "sales".
    
.. class:: SuppliersAccountsBalance

    A :class:`PartnerAccountsBalance` for the TradeType "purchases".

.. class:: DebtorsCreditors

    Abstract base class for different tables showing a list of
    partners with the following columns:

      partner due_date balance actions

.. class:: Debtors

    Shows partners who have some debt against us.
    Inherits from :class:`DebtorsCreditors`.

.. class:: Creditors

    Shows partners who give us some form of credit.
    Inherits from :class:`DebtorsCreditors`.

           


.. _cosi.specs.ledger.movements:


.. _cosi.specs.ledger.vouchers:


.. _cosi.specs.ledger.journals:

Journals
========

>>> ses.show(ledger.Journals,
...     column_names="ref name trade_type account dc")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== ===================== =============================== ============ ================================ ===========================
 Reference   Designation           Designation (en)                Trade type   Account                          Primary booking direction
----------- --------------------- ------------------------------- ------------ -------------------------------- ---------------------------
 SLS         Factures vente        Sales invoices                  Sales                                         Debit
 SLC         Sales credit notes    Sales credit notes              Sales                                         Credit
 PRC         Factures achat        Purchase invoices               Purchases                                     Credit
 PMO         Payment Orders        Payment Orders                  Purchases    (5810) Payment Orders Bestbank   Credit
 CSH         Caisse                Cash                                         (5700) Cash                      Debit
 BNK         Bestbank              Bestbank                                     (5500) Bestbank                  Debit
 MSC         Opérations diverses   Miscellaneous Journal Entries                (5700) Cash                      Debit
 VAT         Déclarations TVA      VAT declarations                             (4513) VAT to declare            Debit
=========== ===================== =============================== ============ ================================ ===========================
<BLANKLINE>




Trade types
===========

This plugin introduces the concept of **trade types**.

The default list of trade types is:

>>> rt.show(ledger.TradeTypes)
======= =========== ===========
 value   name        text
------- ----------- -----------
 S       sales       Sales
 P       purchases   Purchases
 W       wages       Wages
 C       clearings   Clearings
======= =========== ===========
<BLANKLINE>

Your application might have a different list.  You can see the
actually configured list for your site via :menuselection:`Explorer
--> Accounting --> Trade types`.

See :class:`lino_xl.lib.ledger.choicelists.TradeTypes` for technical
details.


Match rules
===========

A **match rule** specifies that a movement into given account can be
*cleared* using a given journal.

>>> ses.show(ledger.MatchRules)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
==== ================== =====================================
 ID   Account            Journal
---- ------------------ -------------------------------------
 1    (4000) Customers   Sales invoices (SLS)
 2    (4000) Customers   Sales credit notes (SLC)
 3    (4400) Suppliers   Purchase invoices (PRC)
 4    (4000) Customers   Payment Orders (PMO)
 5    (4400) Suppliers   Payment Orders (PMO)
 6    (4000) Customers   Cash (CSH)
 7    (4400) Suppliers   Cash (CSH)
 8    (4000) Customers   Bestbank (BNK)
 9    (4400) Suppliers   Bestbank (BNK)
 10   (4000) Customers   Miscellaneous Journal Entries (MSC)
 11   (4400) Suppliers   Miscellaneous Journal Entries (MSC)
==== ================== =====================================
<BLANKLINE>


For example a payment order can be used to pay an open suppliers
invoice or (less frequently) to send back money that a customer had
paid too much.

>>> jnl = ledger.Journal.objects.get(ref="PMO")
>>> jnl
Journal #4 ('Payment Orders (PMO)')

>>> rt.show(ledger.MatchRulesByJournal, jnl)
==================
 Account
------------------
 (4000) Customers
 (4400) Suppliers
==================
<BLANKLINE>

Or a sales invoice can be used to clear another sales invoice.

>>> jnl = ledger.Journal.objects.get(ref="SLS")
>>> jnl
Journal #1 ('Sales invoices (SLS)')
>>> rt.show(ledger.MatchRulesByJournal, jnl)
==================
 Account
------------------
 (4000) Customers
==================
<BLANKLINE>



Debtors
=======

**Debtors** are partners who received credit from us and therefore are
in debt towards us. The most common debtors are customers,
i.e. partners who received a sales invoice from us and did not yet pay
that invoice.

>>> ses.show(ledger.Debtors, column_names="partner partner_id balance")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE -REPORT_UDIFF
======================= ========== ===============
 Partner                 ID         Balance
----------------------- ---------- ---------------
 Bastiaensen Laurent     116        880,00
 Altenberg Hans          114        5 341,45
 Ausdemwald Alfons       115        1 204,81
 Chantraine Marc         119        5 003,00
 Evertz Bernd            125        1 665,81
 Evers Eberhart          126        1 049,90
 Arens Andreas           112        4 599,77
 Emonts Daniel           127        3 989,85
 Dericum Daniel          120        3 959,70
 Hilgers Henri           133        1 060,00
 Jonas Josef             138        745,86
 Engels Edgar            128        3 639,74
 Kaivers Karl            140        5 349,66
 Groteclaes Gregory      131        1 231,82
 Jansen Jérémy           135        3 919,78
 Jousten Jan             139        3 359,92
 Lambertz Guido          141        3 619,88
 Emonts Erich            149        7 454,49
 Mießen Michael          147        880,00
 Radermacher Edgard      156        1 599,92
 Emontspool Erwin        150        1 839,77
 Radermacher Fritz       157        2 349,81
 Radermacher Christian   154        990,00
 Faymonville Luc         129        3 029,62
 Johnen Johann           137        5 439,48
 Radermacher Guido       158        951,82
 Radermacher Jean        162        600,00
 Malmendier Marc         145        1 204,81
 Radermacher Alfons      152        1 834,19
 Radermacher Hans        159        525,00
 da Vinci David          164        639,92
 di Rupo Didier          163        4 355,65
 Radermecker Rik         172        2 039,82
 van Veen Vincent        165        465,96
 Eierschal Emil          174        1 161,37
 Östges Otto             167        770,00
 Jeanémart Jérôme        180        990,00
 Martelaer Mark          171        2 999,85
 Dubois Robin            178        1 199,85
 Denon Denis             179        279,90
 Brecht Bernd            176        535,00
 Keller Karl             177        3 319,78
 **Total (42 rows)**     **6180**   **98 076,96**
======================= ========== ===============
<BLANKLINE>

Partner 116 from above list has two open sales invoices, totalling to
880,00:

>>> obj = contacts.Partner.objects.get(pk=116)
>>> ses.show(ledger.DebtsByPartner, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==================== ============ ===================== ==========
 Due date             Balance      Debts                 Payments
-------------------- ------------ --------------------- ----------
 09/01/2016           280,00       `SLS 4 <Detail>`__
 07/11/2016           600,00       `SLS 50 <Detail>`__
 **Total (2 rows)**   **880,00**
==================== ============ ===================== ==========
<BLANKLINE>

**Creditors** are partners hwo gave us credit. The most common
creditors are providers, i.e. partners who send us a purchase invoice
(which we did not yet pay).

>>> ses.show(ledger.Creditors, column_names="partner partner_id balance")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==================== ========= ===============
 Partner              ID        Balance
-------------------- --------- ---------------
 AS Express Post      181       510,48
 AS Matsalu Veevärk   182       2 131,20
 Eesti Energia AS     183       75 828,90
 **Total (3 rows)**   **546**   **78 470,58**
==================== ========= ===============
<BLANKLINE>

Partner 181 from above list has 15 open purchases invoices, totalling
to 510,48:

>>> obj = contacts.Partner.objects.get(pk=181)
>>> ses.show(ledger.DebtsByPartner, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
===================== ============= ======= =====================
 Due date              Balance       Debts   Payments
--------------------- ------------- ------- ---------------------
 02/01/2016            -33,06                `PRC 1 <Detail>`__
 07/05/2016            -34,13                `PRC 6 <Detail>`__
 15/03/2016            -33,55                `PRC 11 <Detail>`__
 03/05/2016            -35,12                `PRC 16 <Detail>`__
 07/07/2016            -33,97                `PRC 21 <Detail>`__
 13/06/2016            -33,06                `PRC 26 <Detail>`__
 31/07/2016            -34,13                `PRC 31 <Detail>`__
 01/09/2016            -33,55                `PRC 36 <Detail>`__
 07/09/2016            -35,12                `PRC 41 <Detail>`__
 03/01/2017            -33,97                `PRC 46 <Detail>`__
 13/11/2016            -33,06                `PRC 51 <Detail>`__
 07/01/2017            -34,13                `PRC 56 <Detail>`__
 07/03/2017            -33,88                `PRC 61 <Detail>`__
 11/02/2017            -35,45                `PRC 66 <Detail>`__
 31/03/2017            -34,30                `PRC 71 <Detail>`__
 **Total (15 rows)**   **-510,48**
===================== ============= ======= =====================
<BLANKLINE>

Note that the numbers are negative in above table. A purchase invoice
is a *credit* received from the provider, and we asked a list of
*debts* by partner.


Fiscal years
============

Lino has a table with **fiscal years**.

.. class:: FiscalYears

    A choicelist with the fiscal years available in this database.

    The default value for this list is 5 years starting from
    :attr:`start_year <lino_xl.lib.ledger.Plugin.start_year>`.

    If the fiscal year of your company is the same as the calendar
    year, then the default entries in this should do.  Otherwise you
    can override this in your
    :attr:`workflows_module <lino.core.site.Site.workflows_module>`.


In a default configuration there is one fiscal year for each calendar
year between :attr:`start_year
<lino_xl.lib.ledger.Plugin.start_year>` and ":func:`today
<lino.core.site.Site.today>` plus 5 years".

>>> dd.plugins.ledger.start_year
2016

>>> dd.today()
datetime.date(2017, 3, 12)

>>> dd.today().year + 5
2022

>>> rt.show(ledger.FiscalYears)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
======= ====== ======
 value   name   text
------- ------ ------
 16             2016
 17             2017
 18             2018
 19             2019
 20             2020
 21             2021
 22             2022
======= ====== ======
<BLANKLINE>


Accounting periods
==================

Each ledger movement happens in a given **accounting period**.  
An accounting period usually corresponds to a month of the calendar.
Accounting periods are automatically created the first time they are
needed by some operation.


>>> rt.show(ledger.AccountingPeriods)
=========== ============ ============ ============= ======= ========
 Reference   Start date   End date     Fiscal Year   State   Remark
----------- ------------ ------------ ------------- ------- --------
 2016-01     01/01/2016   31/01/2016   2016          Open
 2016-02     01/02/2016   29/02/2016   2016          Open
 2016-03     01/03/2016   31/03/2016   2016          Open
 2016-04     01/04/2016   30/04/2016   2016          Open
 2016-05     01/05/2016   31/05/2016   2016          Open
 2016-06     01/06/2016   30/06/2016   2016          Open
 2016-07     01/07/2016   31/07/2016   2016          Open
 2016-08     01/08/2016   31/08/2016   2016          Open
 2016-09     01/09/2016   30/09/2016   2016          Open
 2016-10     01/10/2016   31/10/2016   2016          Open
 2016-11     01/11/2016   30/11/2016   2016          Open
 2016-12     01/12/2016   31/12/2016   2016          Open
 2017-01     01/01/2017   31/01/2017   2017          Open
 2017-02     01/02/2017   28/02/2017   2017          Open
 2017-03     01/03/2017   31/03/2017   2017          Open
=========== ============ ============ ============= ======= ========
<BLANKLINE>

The *reference* of a new accounting period is computed by applying the
voucher's entry date to the template defined in the
:attr:`date_to_period_tpl
<lino_xl.lib.ledger.models.AccountingPeriod.get_for_date>` setting.  
The default implementation leads to the following references:

>>> print(ledger.AccountingPeriod.get_ref_for_date(i2d(19940202)))
1994-02
>>> print(ledger.AccountingPeriod.get_ref_for_date(i2d(20150228)))
2015-02
>>> print(ledger.AccountingPeriod.get_ref_for_date(i2d(20150401)))
2015-04

You may manually create other accounting periods. For example

- `2015-00` might stand for a fictive "opening" period before January
  2015 and after December 2014.

- `2015-13` might stand for January 2016 in a company which is
  changing their fiscal year from "January-December" to "July-June".
  

Payment terms
=============

>>> rt.show('ledger.PaymentTerms')
==================== ======================================= ======================================= ======== ========= ==============
 Reference            Designation                             Designation (en)                        Months   Days      End of month
-------------------- --------------------------------------- --------------------------------------- -------- --------- --------------
 07                   Payment seven days after invoice date   Payment seven days after invoice date   0        7         No
 10                   Payment ten days after invoice date     Payment ten days after invoice date     0        10        No
 30                   Payment 30 days after invoice date      Payment 30 days after invoice date      0        30        No
 60                   Payment 60 days after invoice date      Payment 60 days after invoice date      0        60        No
 90                   Payment 90 days after invoice date      Payment 90 days after invoice date      0        90        No
 EOM                  Payment end of month                    Payment end of month                    0        0         Yes
 P30                  Prepayment 30%                          Prepayment 30%                          0        30        No
 PIA                  Payment in advance                      Payment in advance                      0        0         No
 **Total (8 rows)**                                                                                   **0**    **227**
==================== ======================================= ======================================= ======== ========= ==============
<BLANKLINE>




Journal groups
==============

.. class:: JournalGroups

    The list of possible journal groups.

    This list is used to build the main menu. For each journal group
    there will be a menu item in the main menu.

    Journals whose :attr:`journal_group <Journal.journal_group>` is
    empty will not be available through the main user menu.

    The default configuration has the following journal groups:

    .. attribute:: sales

        For sales journals.

    .. attribute:: purchases

        For purchases journals.

    .. attribute:: wages

        For wages journals.

    .. attribute:: financial

        For financial journals (bank statements and cash reports)

           
.. class:: PeriodStates

    The list of possible states of an accounting period.
    
    .. attribute:: open
                   
    .. attribute:: closed


.. class:: VoucherTypes
           
    A list of the voucher types available in this application. Items
    are instances of :class:VoucherType`.

    The :attr:`voucher_type <lino_xl.lib.ledger.Journal.voucher_type>`
    field of a journal points to an item of this.


           
.. class:: VoucherType
           
    Base class for all items of :class:`VoucherTypes`.
    
    The **voucher type** defines the database model used to store
    vouchers of this type (:attr:`model`).

    But it can be more complex: actually the voucher type is defined
    by its :attr:`table_class`, i.e. application developers can define
    more than one *voucher type* per model by providing alternative
    tables (views) for it.

    Every Lino Cosi application has its own global list of voucher
    types defined in the :class:`VoucherTypes` choicelist.

    .. attribute:: model

        The database model used to store vouchers of this type.
        A subclass of :class:`lino_xl.lib.ledger.models.Voucher``.

    .. attribute:: table_class

        Must be a table on :attr:`model` and with `master_key` set to
        the
        :attr:`journal<lino_xl.lib.ledger.models.Voucher.journal>`.

              

.. class:: VoucherState
           
    Base class for items of :class:`VoucherStates`.

    .. attribute:: editable
                   
        Whether a voucher in this state is editable.
        
    
.. class:: VoucherStates
           
    The list of possible states of a voucher.

    In a default configuration, vouchers can be :attr:`draft`,
    :attr:`registered`, :attr:`cancelled` or :attr:`signed`.

    .. attribute:: draft

        *Draft* vouchers can be modified but are not yet visible as movements
        in the ledger.

    .. attribute:: registered

        *Registered* vouchers cannot be modified, but are visible as
        movements in the ledger.

    .. attribute:: cancelled

        *Cancelled* is similar to *Draft*, except that you cannot edit the
        fields. This is used for invoices which have been sent, but the
        customer signaled that they doen't agree. Instead of writing a
        credit nota, you can decide to just cancel the invoice.

    .. attribute:: signed

        The *Signed* state is similar to *registered*, but cannot usually be
        deregistered anymore. This state is not visible in the default
        configuration. In order to make it usable, you must define a custom
        workflow for :class:`lino_xl.lib.ledger.VoucherStates`.


           
.. class:: TradeTypes
           
    A choicelist with the *trade types* defined for this application.

    The **trade type** is one of the basic properties of every ledger
    operation which involves an external partner.  Every partner
    movement belongs to one and only one trade type.

    The default configuration defines the following trade types:

    .. attribute:: sales

        A sale transaction is when you write an invoice to a customer
        and then expect the customer to pay it.

    .. attribute:: purchases

        A purchase transaction is when you get an invoice from a
        provider who expects you to pay it.


    .. attribute:: wages

        A wage transaction is when you write a payroll (declare the
        fact that you owe some wage to an employee) and later pay it
        (e.g. via a payment order).


    .. attribute:: clearings

        A clearing transaction is when an employee declares that he
        paid some invoice for you, and later you pay that money back
        to his account.


.. class:: TradeType
           
    Base class for the choices of :class:`TradeTypes`.

    .. attribute:: dc

        The default booking direction.

    .. attribute:: price_field

        The name and label of the `price` field to be defined on the
        :class:`Product <lino.modlib.products.models.Product>`
        database model.

        With Lino Così you can define one price field per trade type.

    .. attribute:: partner_account_field

        The name and label of the :guilabel:`Partner account` field to
        be defined for this trade type on the :class:`SiteConfig
        <lino.modlib.system.models.SiteConfig>` database model.

    .. attribute:: base_account_field

        The name and label of the :guilabel:`Base account` field to
        be defined for this trade type on the :class:`SiteConfig
        <lino.modlib.system.models.SiteConfig>` database model.


    .. attribute:: vat_account_field

        The name and label of the :guilabel:`VAT account` field to be
        defined for this trade type on the :class:`SiteConfig
        <lino.modlib.system.models.SiteConfig>` database model.

Model mixins
============


.. class:: SequencedVoucherItem

   A :class:`VoucherItem` which also inherits from
   :class:`lino.mixins.sequenced.Sequenced`.


.. class:: AccountVoucherItem


    Abstract base class for voucher items which point to an account.
    
    This is also a :class:`SequencedVoucherItem`.
    
    This is subclassed by
    :class:`lino_xl.lib.vat.models.InvoiceItem`
    and
    :class:`lino_xl.lib.vatless.models.InvoiceItem`.
           
    It defines the :attr:`account` field and some related methods.

    .. attribute:: account

        ForeignKey pointing to the account (:class:`accounts.Account
        <lino_xl.lib.accounts.models.Account>`) that is to be moved.

   

.. class:: VoucherItem
           
    Base class for items of a voucher.

    Subclasses must define the following fields:

    .. attribute:: voucher

        Pointer to the voucher which contains this item.  Non
        nullable.  The voucher must be a subclass of
        :class:`ledger.Voucher<lino_xl.lib.ledger.models.Voucher>`.
        The `related_name` must be `'items'`.
    

    .. attribute:: title

        The title of this voucher.

        Currently (because of :djangoticket:`19465`), this field is
        not implemented here but in the subclasses:

        :class:`lino_xl.lib.vat.models.AccountInvoice`
        :class:`lino_xl.lib.vat.models.InvoiceItem`

           
.. class:: Matching

    Model mixin for database objects that are considered *matching
    transactions*.  A **matching transaction** is a transaction that
    points to some other movement which it "clears" at least partially.

    A movement is cleared when its amount equals the sum of all
    matching movements.

    Adds a field :attr:`match` and a chooser for it.  Requires a field
    `partner`.  The default implementation of the chooser for
    :attr:`match` requires a `journal`.

    Base class for :class:`lino_xl.lib.vat.AccountInvoice`
    (and e.g. `lino_xl.lib.sales.Invoice`, `lino_xl.lib.finan.DocItem`)
    
    .. attribute:: match

       Pointer to the :class:`movement
       <lino.modlib.ledger.models.Movement>` which is being cleared by
       this movement.

.. class:: PartnerRelated
           
    Base class for things that are related to one and only one trade
    partner. This is base class for both (1) trade document vouchers
    (e.g. invoices or offers) and (2) for the individual entries of
    financial vouchers and ledger movements.

    .. attribute:: partner

        The recipient of this document. A pointer to
        :class:`lino_xl.lib.contacts.models.Partner`.

    .. attribute:: payment_term

        The payment terms to be used in this document.  A pointer to
        :class:`PaymentTerm`.

    .. attribute:: recipient

        Alias for the partner


.. class:: ProjectRelated

    Model mixin for objects that are related to a :attr:`project`.

    .. attribute:: project

        Pointer to the "project". This field exists only if the
        :attr:`project_model <Plugin.project_model>` setting is
        nonempty.


Utilities
=========

.. class:: DueMovement
           
    A volatile object representing a group of matching movements.

    A **due movement** is a movement which a partner should do in
    order to satisfy their debt.  Or which we should do in order to
    satisfy our debt towards a partner.

    The "matching" movements of a given movement are those whose
    `match`, `partner` and `account` fields have the same values.
    
    These movements are themselves grouped into "debts" and "payments".
    A "debt" increases the debt and a "payment" decreases it.
    
    .. attribute:: match

        The common `match` string of these movments

    .. attribute:: dc

        Whether I mean *my* debts and payments (towards that partner)
        or those *of the partner* (towards me).

    .. attribute:: partner

    .. attribute:: account



           

Plugin attributes
=================

.. class:: Plugin

           
    .. attribute:: currency_symbol

        Temporary approach until we add support for multiple
        currencies.

    .. attribute:: use_pcmn
                   
        Whether to use the PCMN notation.

        PCMN stands for "plan compatable minimum normalisé" and is a
        standardized nomenclature for accounts used in France and
        Belgium.

    .. attribute:: project_model

        Leave this to `None` for normal behaviour.  Set this to a
        string of the form `'<app_label>.<ModelName>'` if you want to
        add an additional field `project` to all models which inherit
        from :class:`lino_xl.lib.ledger.ProjectRelated`.

                   
    .. attribute:: intrusive_menu

        Whether the plugin should integrate into the application's
        main menu in an intrusive way.  Intrusive means that the main
        menu gets one top-level item per journal group.

        The default behaviour is `False`, meaning that these items are
        gathered below a single item "Accounting".

                   
    .. attribute:: start_year

        An integer with the calendar year in which this site starts
        working.

        This is used to fill the default list of :class:`FiscalYears`,
        and by certain fixtures for generating demo invoices.

                   
    .. attribute:: fix_y2k
                   
        Whether to use a Y2K compatible representation for fiscal
        years.


    .. attribute:: force_cleared_until

        Force all movements on vouchers with entry_date until the
        given date to be *cleared*.  This is useful e.g. when you want
        to keep legacy invoices in your database but not their
        payments.

