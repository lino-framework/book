.. doctest docs/specs/vat.rst
.. _xl.vat:

====================================================
``vat`` : Adding VAT (Value-added tax) functionality
====================================================

.. currentmodule:: lino_xl.lib.vat

The :mod:`lino_xl.lib.vat` plug-in adds functionality for handling sales and
purchase invoices in a context where the :term:`site operator` is subject to
value-added tax (VAT).  It provides a framework for handling VAT declarations.
When using this plugin, you will probably also install one of the `national VAT
implementations`_.


.. contents::
   :depth: 1
   :local:


.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.pierre.settings.doctests')
>>> from lino.api.doctest import *


Overview
========

The VAT plug in defines the following concepts:

.. glossary::

  VAT regime

    Specifies how the VAT for this voucher is being handled, e.g. which VAT
    rates are available and whether and how and when VAT is to be declared and
    paid to the national VAT office.  See `VAT regimes`_.

  VAT class

    The nature of a trade object to be differentiated in the VAT declaration.

    For example most countries differentiate between "goods" and "services".
    Other common VAT classes are "investments" or "vehicles".

    The list of available VAT classes is defined by your national VAT plugin.
    For example in Estonia the VAT office wants to know, in one field of your
    declaration, how much money you spend for buying "vehicles" and in another
    field how much you spent for "real estate" objects, while in Belgium both
    vehicles and real estate objects are considered together as "investments".

  VAT rules

    A set of rules that defines which VAT rate to apply and which account to use
    for a given combination of regime, class and trade type. The available VAT
    rules vary depending on which VAT declaration plugin is installed.

  VAT declaration

    A :term:`ledger voucher` that expresses the fact that the :term:`site
    operator` submitted a VAT declaration to their tax office.

  VAT area

    A group of countries having same :term:`VAT rules <VAT rule>` in the country
    of the :term:`site operator`.  See `VAT areas`_.




National VAT implementations
============================

Applications using this plug-in must specify the **national implementations**
for their VAT declarations by setting the :attr:`declaration_plugin
<lino_xl.lib.vat.Plugin.declaration_plugin>` plugin attribute.

Currently we have three declaration plug-ins:

- :doc:`bevat`
- :doc:`bevats`
- :doc:`eevat`

Accounting applications to be used by site operators who don't care about VAT
might use :mod:`lino_xl.lib.vatless` instead (though this plug-in might become
deprecated).  The modules :mod:`lino_xl.lib.vatless` and :mod:`lino_xl.lib.vat`
can theoretically both be installed though obviously this wouldn't make sense.




VAT regimes
===========

A :term:`VAT regime` must be assigned to each voucher and may optionally be
assigned to each partner.

The *VAT regime of a partner* is used as the default value for all vouchers
with this partner.  When you define a *default VAT regime* per partner, any new
voucher created for this partner will have this VAT regime.  Existing vouchers
are not changed when you change this field.

The available VAT regimes vary depending on which VAT declaration plugin is
installed.  See also `Available VAT regimes`_. When no declaration module is
installed, we have only one default regime.

>>> rt.show(vat.VatRegimes, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
======= ======== ======== ========== ==============
 value   name     text     VAT area   Needs VAT id
------- -------- -------- ---------- --------------
 10      normal   Normal              No
======= ======== ======== ========== ==============
<BLANKLINE>

Note that the :term:`VAT regime` has nothing to do with the :term:`trade type`.
For example, when a partner has the regime "Intra-community", this regime is
used for both sales and purchase invoices with this partner.  The difference
between sales and purchases is defined by the `VAT rules`_, not by the regime.

.. class:: VatRegime

    Base class for the items of :class:`VatRegimes`.  Each VAT regime is an
    instance of this and has two properties:

    .. attribute:: vat_area

        In which :term:`VAT area` this regime is available.

    .. attribute:: item_vat

        Whether unit prices are VAT included or not.
        No longer used. See :attr:`Plugin.item_vat` instead.


    .. attribute:: needs_vat_id

        Whether this VAT regime requires that partner to have a
        :attr:`vat_id`.

.. class:: VatRegimes

    The global list of *VAT regimes*.  Each item of this list is an instance of
    :class:`VatRegime`.

    Three VAT regimes are considered standard minimum:

    .. attribute:: normal
    .. attribute:: subject
    .. attribute:: intracom

    Two additional regimes are defined in :mod:`lino_xl.lib.bevat`:

    .. attribute:: de
    .. attribute:: lu


VAT classes
===========

A :term:`VAT class` is assigned to each item of an invoice.  The VAT class can
influence the available VAT rates. You can sell or purchase a same product to
different partners using different VAT regimes.

>>> rt.show(vat.VatClasses, language="en")
======= ============= ===========================
 value   name          text
------- ------------- ---------------------------
 010     goods         Goods at normal VAT rate
 020     reduced       Goods at reduced VAT rate
 030     exempt        Goods exempt from VAT
 100     services      Services
 200     investments   Investments
 210     real_estate   Real estate
 220     vehicles      Vehicles
======= ============= ===========================
<BLANKLINE>


A VAT class is a direct or indirect property of a trade object (e.g. a Product)
and influences the VAT rate to be used.  It does not contain the actual rate
because this still varies depending on your country, the time and type of the
operation, and possibly other factors.


.. class:: VatClasses

    The global list of VAT classes.

    Default classes are:

    .. attribute:: exempt

    .. attribute:: reduced

    .. attribute:: normal


VAT rules
=========

When no national declaration module is installed, we have only one default
:term:`VAT rule` with no condition and zero rate.

>>> rt.show(vat.VatRules, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
+-------+------------------+
| value | Description      |
+=======+==================+
| 1     | VAT rule 1:      |
|       | apply 0 %        |
|       | and book to None |
+-------+------------------+
<BLANKLINE>


.. class:: VatRule

    A rule which defines how VAT is to be handled for a given invoice
    item.

    Example data see :mod:`lino_xl.lib.vat.fixtures.euvatrates`.

    Database fields:

    .. attribute:: seqno

       The sequence number.

    .. attribute:: country
    .. attribute:: vat_class

    .. attribute:: vat_regime

        The regime for which this rule applies.

        Pointer to :class:`VatRegimes`.

    .. attribute:: rate

        The VAT rate to be applied. Note that a VAT rate of 20 percent is
        stored as `0.20` (not `20`).

    .. attribute:: vat_account

        The general account where VAT is to be booked.

    .. attribute:: vat_returnable

        Whether VAT is returnable. Returnable VAT does not increase the total
        amount of the voucher, it causes an additional movement into the
        :attr:`vat_returnable_account`. See `About returnable VAT`_.

    .. attribute:: vat_returnable_account

        Where to book returnable VAT. If this field is empty and
        :attr:`vat_returnable` is `True`, then VAT will be added to the base
        account. See `About returnable VAT`_.


    .. classmethod:: get_vat_rule(cls, trade_type, vat_regime,
                     vat_class=None, country=None, date=None)

        Return the VAT rule to be applied for the given criteria.

        Lino loops through all rules (ordered by their :attr:`seqno`)
        and returns the first object which matches.

.. class:: VatRules

    The table of all :class:`VatRule` objects.

    This table is accessible via :menuselection:`Explorer --> VAT --> VAT rules`.

    >>> show_menu_path(vat.VatRules, language='en')
    Explorer --> VAT --> VAT rules

    This table is filled by



VAT areas
=========

When your business is located, e.g. in Belgium and you buy goods or services
from France, Germany and the Netherlands,  then these countries are called
"intra community". Certain VAT rules apply for all intra-community countries.
We don't want to repeat them for each country. That's why we have VAT areas.

A :term:`VAT area` is a group of countries for which same VAT rules apply in
the country of the :term:`site operator` .

     are used to group countries into groups where similar VAT regimes
  are available.

    See :class:`VatAreas`.


>>> rt.show(vat.VatAreas, language="en")
======= =============== ===============
 value   name            text
------- --------------- ---------------
 10      national        National
 20      eu              EU
 30      international   International
======= =============== ===============
<BLANKLINE>


The plugin property :attr:`eu_country_codes
<lino_xl.lib.vat.Plugin.eu_country_codes>` defines which countries are
considered part of the EU.

So the :attr:`country <lino_xl.lib.contacts.Partner.country>` field of a
partner indirectly influences which `VAT regimes`_ are available this partner.

Available VAT regimes
=====================

The declaration plugin controls which VAT regimes are available for selection
on a partner or on a voucher.

The list of available VAT regimes for a partner depends on the VAT area and on
whether the partner has a VAT id or not.

.. function:: get_vat_regime_choices(country=None, vat_id=None):

    Used for the choosers of the :attr:`vat_regime` field of a partner and a
    voucher.


.. class:: VatAreas

    The global list of VAT areas.

    .. classmethod:: get_for_country(cls, country)

        Return the VatArea instance for this country.

Why differentiate between VAT regimes and VAT classes?
======================================================

You might ask why we use two sets of categories for specifying the VAT rate.
Some other accounting programs do not have two different categories for the
subtle difference between "exempt from VAT" and "VAT 0%", they have just a
category "VAT rate" which you can set per invoice item (and a default value per
provider).

The problem with this simplified vision is that at least for Belgian VAT
declarations there is a big difference between having 0% of VAT because the
provider is a private person and having 0% of VAT because you are buying post
stamps or flight tickets (which are exempt from VAT).

Another thing to consider is that in Lino we want to be able to have partners
who are both a provider and a customer.  Their VAT regime remains the same for
both trade types (sales and purchase) while the default VAT class to use in
invoice items depends on the account or the product.

.. Consider e.g. an invoice from an airline company where you buy tickets (VAT 0%)
   and some additional service (VAT 20%). Or an invoice from some other company
   where you buy post stamps (0%), books (9%) and additional service (20%).


Account invoices
===================

An :term:`account invoice` is an invoice for which the user enters just the bare
accounts and amounts. The :mod:`lino_xl.lib.vat` plugin defines a VAT-capable
implementation of :term:`account invoices <account invoice>`. They are typically
used to store incoming purchase invoices, and they do no not usually produce a
printable document.

If you also need products, quantities and discounts, use a journal having
:class:`VatProductInvoice <lino_xl.lib.sales.VatProductInvoice>` as voucher type
instead.

Account invoices are typically used to store incoming purchase invoices, but
exceptions in both directions are possible: (1) purchase invoices can be stored
using :class:`VatProductInvoice <lino_xl.lib.sales.VatProductInvoice>` if stock
management is important, or (2) outgoing sales invoice can be stored as
:class:`VatAccountInvoice` because they have been created using some external
tool and are entered into Lino just for the general ledger.

It is one of the most basic voucher types, which can be used even in  accounting
applications that don't have :mod:`lino_xl.lib.sales`.


There are two database models:

.. class:: VatAccountInvoice

    Django model for storing :term:`account invoices <account invoice>`.

.. class:: InvoiceItem

    Django model for representing items of an :term:`account invoice`.

There are several views:

.. class:: Invoices

    The table of all :class:`VatAccountInvoice` objects.

.. class:: InvoicesByJournal

    Shows all invoices of a given journal (whose :attr:`voucher_type
    <lino_xl.lib.ledger.Journal.voucher_type>` must be
    :class:`VatAccountInvoice`)

.. class:: PrintableInvoicesByJournal

    Purchase journal

.. class:: InvoiceDetail

    The detail layout used by :class:`Invoices`.

.. class:: ItemsByInvoice

.. class:: VouchersByPartner



Utilites
========


The :mod:`lino_xl.lib.vat.utils` module contains some utility functions.


>>> from lino_xl.lib.vat.utils import add_vat, remove_vat

>>> add_vat(100, 21)
121.0

>>> remove_vat(121, 21)
100.0

>>> add_vat(10, 21)
12.1

>>> add_vat(1, 21)
1.21



Showing the invoices covered by a VAT declaration
=================================================

The plugin defines two tables that show the invoices covered by a VAT
declaration, IOW the invoices that have contributed to the numbers in the
declaration.


.. class:: SalesByDeclaration

    Show a list of all sales invoices whose VAT regime is Intra-Community.

.. class:: PurchasesByDeclaration

    Show a list of all purchase invoices whose VAT regime is Intra-Community.

.. class:: VatInvoices

    Common base class for :class:`SalesByDeclaration` and
    :class:`PurchasesByDeclaration`



Intracom sales and purchases
============================

The plugin defines two reports accessible via the
:menuselection:`Reports --> Accounting` menu and integrated in the
printout of a VAT declaration:


.. class:: IntracomSales

    Show a list of all sales invoices whose VAT regime is Intra-Community.

.. class:: IntracomPurchases

    Show a list of all purchase invoices whose VAT regime is Intra-Community.

.. class:: IntracomInvoices

    Common base class for :class:`IntracomSales` and
    :class:`IntracomPurchases`

These reports are empty when you have no national declaration plugin installed:

>>> rt.show(vat.IntracomSales, language='en')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
No data to display

>>> rt.show(vat.IntracomPurchases, language='en')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
No data to display



Model mixins
============

.. class:: VatTotal

    Model mixin which defines the database fields :attr:`total_incl`,
    :attr:`total_base` and :attr:`total_vat` and some related behaviour.

    Used for both the voucher (:class:`VatDocument`) and for each item
    (:class:`VatItemBase`).

    .. attribute:: total_incl

        The amount VAT *included*.

    .. attribute:: total_base

        The amount VAT *excluded*.

    .. attribute:: total_vat

        The amount of VAT.

    All three total fields are :class:`lino.core.fields.PriceField`
    instances.

    The fields are editable by default, but implementing models can call
    :func:`lino.core.fields.update_field` to change this behaviour. A model that
    sets all fields to non-editable should also set :attr:`edit_totals` to
    `False`.

    .. method:: get_trade_type

        Subclasses of VatTotal must implement this method.

    .. method:: get_vat_rule

        Return the VAT rule for this voucher or voucher item. Called
        when user edits a total field in the document header when
        :attr:`edit_totals` is True.


    .. method:: total_base_changed

        Called when user has edited the :attr:`total_base` field.  If
        total_base has been set to blank, then Lino fills it using
        :meth:`reset_totals`. If user has entered a value, compute
        :attr:`total_vat` and :attr:`total_incl` from this value using
        the vat rate. If there is no VatRule, :attr:`total_incl` and
        :attr:`total_vat` are set to None.

        If there are rounding differences, :attr:`total_vat` will get
        them.

    .. method:: total_vat_changed

        Called when user has edited the `total_vat` field.  If it has been
        set to blank, then Lino fills it using
        :meth:`reset_totals`. If user has entered a value, compute
        :attr:`total_incl`. If there is no VatRule, `total_incl` is
        set to None.

    .. method:: total_incl_changed

        Called when user has edited the `total_incl` field.  If total_incl
        has been set to blank, then Lino fills it using
        :meth:`reset_totals`. If user enters a value, compute
        :attr:`total_base` and :attr:`total_vat` from this value using
        the vat rate. If there is no VatRule, `total_incl` should be
        disabled, so this method will never be called.

        If there are rounding differences, `total_vat` will get them.


.. class:: VatDocument

    Abstract base class for invoices, offers and other vouchers.

    Inherited by :class:`VatAccountInvoice` as well as in other
    plugins (e.g. :class:`lino_xl.lib.sales.VatProductInvoice` and
    :class:`lino_xl.lib.ana.AnaAccountInvoice`).

    Models that inherit this mixin can set the following class
    attribute:

    .. attribute:: edit_totals

        Whether the user usually wants to edit the total amount or
        not.

        The total fields of an invoice are not automatically updated
        each time an item is modified.  Users must click the Σ
        ("Compute sums") button (or Save or the Register button) to
        see the invoice's totals.


    Inherits the following database fields from :class:`VatTotal`:

    .. attribute:: total_base
    .. attribute:: total_vat
    .. attribute:: total_incl

    Adds the following database fields:

    .. attribute:: project

       Pointer to a :attr:`lino_xl.lib.ledger.Plugin.project_model`.

    .. attribute:: partner

       Mandatory field to be defined in the implementing class.

    .. attribute:: items_edited

       An automatically managed boolean field which says whether the
       user has manually edited the items of this document.  If this
       is False and :attr:`edit_totals` is True, Lino will
       automatically update the only invoice item according to
       :attr:`partner` and :attr:`vat_regime` and :attr:`total_incl`.

    .. attribute:: vat_regime

        The VAT regime to be used in this document.

        A pointer to :class:`VatRegimes`.


    Adds an action:

    .. attribute:: compute_sums

        Calls :class:`ComputeSums` for this document.


.. class:: ComputeSums

    Compute the sum fields of a :class:`VatDocument` based on its
    items.

    Represented by a "Σ" button.


.. class:: VatItemBase

    Model mixin for items of a :class:`VatDocument`.

    Abstract Base class for
    :class:`lino_xl.lib.ledger.InvoiceItem`, i.e. the lines of
    invoices *without* unit prices and quantities.

    Subclasses must define a field called "voucher" which must be a
    ForeignKey with related_name="items" to the "owning document",
    which in turn must be a subclass of :class:`VatDocument`).

    .. attribute:: vat_class

        The VAT class to be applied for this item. A pointer to
        :class:`VatClasses`.

    .. method:: get_vat_rule(self, tt)

        Return the `VatRule` which applies for this item.

        `tt` is the trade type (which is the same for each item of a
        voucher, that's why we expect the caller to provide it).

        This basically calls the class method
        :meth:`VatRule.get_vat_rule` with
        appropriate arguments.

        When selling certain products ("automated digital services")
        in the EU, you have to pay VAT in the buyer's country at that
        country's VAT rate.  See e.g.  `How can I comply with VAT
        obligations?
        <https://ec.europa.eu/growth/tools-databases/dem/watify/selling-online/how-can-i-comply-vat-obligations>`_.

        TODO: Add a new attribute `VatClass.buyers_country` or a
        checkbox `Product.buyers_country` or some other way to specify
        this.


.. class:: QtyVatItemBase


    Model mixin for items of a :class:`VatTotal`.  Extends
    :class:`VatItemBase` by adding :attr:`unit_price` and :attr:`qty`.

    Abstract Base class for :class:`lino_xl.lib.sales.InvoiceItem` and
    :class:`lino_xl.lib.sales.OrderItem`, i.e. invoice items *with*
    unit prices and quantities.

    .. attribute:: unit_price

        The unit price for this item.

    .. attribute:: qty

    Changing the :attr:`unit_price` ot the :attr:`qty` will
    automatically reset the total amount of this item: the value
    `unit_price * qty` will be stored in :attr:`total_incl` if
    :attr:`VatRegime.item_vat` is `True`, otherwise in
    :attr:`total_base`.



VAT columns
===========

.. class:: VatColumns

    The global list of VAT columns.

    The VAT column of a ledger account indicates where the movements
    on this account are to be collected in VAT declarations.


VAT declarations
================

A **VAT declaration** is a voucher that expresses that a corporation declares to
its government how much sales and purchases they've done during a given period.

A VAT declaration is a computed summary of ledger movements in an **observed
period** or range of periods.  The voucher itself is a ledger voucher that
generates new movements in its own **period of declration**, which is different
from the observed period range.


.. class:: VatDeclaration

    Abstract base class for VAT declarations.

    Inherits from
    :class:`lino_xl.lib.sepa.Payable`
    :class:`lino_xl.lib.ledger.Voucher`
    :class:`lino_xl.lib.excerpts.Certifiable`
    :class:`lino_xl.lib.ledger.PeriodRange`

    .. attribute:: accounting_period

    .. method:: get_payable_sums_dict

        Implements
        :meth:`lino_xl.lib.sepa.Payable.get_payable_sums_dict`.

        As a side effect this updates values in the computed fields of
        this declaration.


Declaration fields
==================

Defining the declaration fields is responsibility of each national
implementation plugin. But every individual field in every VAT declaration of
every country is an instance of one of the following three classes:

.. class:: MvtDeclarationField

  A declaration field to be computed by analyzing the *ledger movements*.

.. class:: WritableDeclarationField

  A declaration field to be entered manually by the end user.

.. class:: SumDeclarationField

  A declaration field that computes the sum of its *observed fields*.


All these three declaration field classes have a common ancestor
:class:`DeclarationField`.

.. class:: DeclarationField

    Base class for all declaration fields.

    It is not instantiated directly but by using one of its subclasses

    .. attribute:: editable

      Whether the value of this field is to be manually entered by the end user.

      Most fields are not editable, i.e. computed.

    .. attribute:: both_dc

      Whether the value of this field is to be manually entered by the end user.

    .. attribute:: fieldnames

       An optional space-separated list of names of *observed fields*, i.e.
       other declaration fields to be observed by this field.   If a field name
       is prefixed by a "-", the observed field will additionally be *inverted*.

       This is used only by sum fields.  The values of all observed fields will
       be added, except inverted fields whose value will be subtracted.

       Note that the booking direction (D or C) of the observed fields is
       ignored when computing the sum.

    .. attribute:: vat_regimes
    .. attribute:: vat_classes
    .. attribute:: vat_columns

    .. attribute:: exclude_vat_regimes
    .. attribute:: exclude_vat_classes
    .. attribute:: exclude_vat_columns


    .. attribute:: is_payable

        Whether the value of this field represents an amount to be paid to the
        tax office.


.. class:: DeclarationFieldsBase

  .. method:: add_mvt_field
  .. method:: add_sum_field
  .. method:: add_writable_field

Configuration
=============

See also :class:`lino_xl.lib.vat.Plugin` for configuration options.


Fill invoice items based on voucher's total
===========================================

In a VatAccountInvoice, end users may edit the total amount of the invoice in
order to have Lino assist them for filling invoice items based on this amount.


Manually editing the VAT amount of invoice items
================================================

End users can manually edit any amount of an invoice item.

When you enter a :attr:`total_incl <InvoiceItem.total_incl>`, Lino automatically
computes the :attr:`total_base <InvoiceItem.total_base>`  and :attr:`total_vat
<InvoiceItem.total_vat>`. But when entering data from a legacy system, you may
want to manually specify a different VAT amount.

Example
=======

An electricity invoice of 94,88 €.  Only 35% of the total amount is
deductible.

- Manually enter 94.88 in :attr:`VatProductInvoice.total_incl`. Lino fills one
  invoice item. The general account of this item is either the provider's
  :attr:`purchase_account` or (if that field is empty)
  :attr:`lino_xl.lib.ledger.CommonAccounts.waiting`.

- Change the amount of the invoice item (:attr:`total_incl
  <InvoiceItem.total_incl>`) from 94.88 to 33.22 (94.88 * 0.35).
  Lino automatically sets :attr:`total_base
  <InvoiceItem.total_base>` to 27.68 € (33.22 / 1.20) and :attr:`total_vat
  <InvoiceItem.total_vat>` to 5.54 (33.22 - 27.68).

- Add a second line and manually set :attr:`InvoiceItem.account` to ``600020``
  (Non deducible costs).   Lino automatically fills the remaining amount (94.88
  - 33.22 = 61.66) into the :attr:`InvoiceItem.total_incl` field and computes
  the other amounts of that line. Since account ``600020`` has :attr:`vat_class`
  set to :attr:`exempt<lino_xl.lib.vat.VatClasses.exempt>`, the other amounts
  are set to blank.


About returnable VAT
====================

.. glossary::

  returnable VAT

    A VAT amount in an invoice that is not to be paid to (or by) the
    partner but must be declared in the VAT declaration.

    Returnable VAT, unlike normal VAT, does not increase the total amount of the
    voucher but causes an additional movement into the account configured as
    "VAT returnable" (a :term:`common account`).

    See also :attr:`vat_returnable_account <VatRule.vat_returnable_account>`.

The VAT columns checker
=======================

.. class:: VatColumnsChecker

  Check VAT columns configuration.

This is an unbound data checker
(:attr:`lino.modlib.checkdata.Checker.model` is `None`), i.e. the messages aren't bound to a particular
database object.
