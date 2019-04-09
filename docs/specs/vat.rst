.. doctest docs/specs/vat.rst
.. _xl.vat:

====================================================
``vat`` : Adding VAT (Value-added tax) functionality
====================================================

.. currentmodule:: lino_xl.lib.vat

The :mod:`lino_xl.lib.vat` plugin adds functionality for handling sales and
purchase invoices in a context where the site operator is subject to
value-added tax (VAT).

.. contents::
   :depth: 1
   :local:

See also
========

Applications using this plugin will probably also install at least one of the
national implementations for their VAT declarations.  Currently we have three
declaration plugins:

- :doc:`bevat` (Belgium standard)
- :doc:`bevats` (Belgium simplified)
- :doc:`eevat` (Estonia)

Accounting applications to be used by site operators who don't care about VAT
might use :mod:`lino_xl.lib.vatless` instead (though this plugin might become
deprecated).  The modules :mod:`lino_xl.lib.vatless` and :mod:`lino_xl.lib.vat`
can theoretically both be installed though obviously this wouldn't make sense.

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.pierre.settings.doctests')
>>> from lino.api.doctest import *

Overview
========

The VAT plugin defines some subtle concepts:

`VAT regimes`_, `VAT classes`_, and `VAT rules`_ decide about the **VAT
rate** to apply for a given operation.

`VAT areas`_ are used to group countries into groups where similar VAT regimes
are available.


VAT regimes
===========

A **VAT regime** must be assigned to each voucher and may optionally be
assigned to each partner.

The *VAT regime of a voucher* influences how the VAT for this voucher is being
handled, e.g. which VAT rates are available and whether and how VAT is to be
declared and paid towards the national VAT office.

The *VAT regime of a partner* is used as the default value for all vouchers
with this partner.  When you define a *default VAT regime* per partner, any new
voucher created for this partner will have this VAT regime.  Existing vouchers
are not changed when you change this field.

The available VAT regimes vary depending on which VAT declaration plugin is
installed.  See also `Available VAT regimes`_. The list below is when no
declaration module is installed, so we have only one default regime.

>>> rt.show(vat.VatRegimes, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
======= ======== ======== ========== ============== ==========
 value   name     text     VAT area   Needs VAT id   item VAT
------- -------- -------- ---------- -------------- ----------
 10      normal   Normal              No             Yes
======= ======== ======== ========== ============== ==========
<BLANKLINE>

Note that the VAT regime does not depend on the *trade type*.  For example,
when a partner has the regime "Intra-community", this regime is used for both
sales and purchase invoices with this partner.  The difference between sales
and purchases is defined by the `VAT rules`_, not by the regime.

.. class:: VatRegime

    Base class for the items of :class:`VatRegimes`.  Each VAT regime is an
    instance of this and has two properties:

    .. attribute:: vat_area

        In which *VAT area* this regime is available.  See :class:`VatAreas`.

    .. attribute:: item_vat

        Whether unit prices are VAT included or not.

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

A **VAT class** is assigned to each product and to each item of a simple
account invoice.  The VAT class specifies how that product or invoice item
behaves regarding to VAT, especially it influences the available rates. You can
sell or purchase a same product to different partners using different VAT
regimes.

>>> rt.show(vat.VatClasses, language="en")
======= ========= ==================
 value   name      text
------- --------- ------------------
 0       exempt    Exempt from VAT
 1       reduced   Reduced VAT rate
 2       normal    Normal VAT rate
======= ========= ==================
<BLANKLINE>

A VAT class is a direct or indirect property of a trade object (e.g. a Product)
which

determines the VAT *rate* to be used.  It does not contain the actual
rate because this still varies depending on your country, the time and type of
the operation, and possibly other factors.


.. class:: VatClasses

    The global list of VAT classes.

    Default classes are:

    .. attribute:: exempt

    .. attribute:: reduced

    .. attribute:: normal


VAT rules
=========

A **VAT rule** defines which VAT rate to apply and which account to use for a
given combination of regime, class and trade type.

The available VAT rules vary depending on which VAT declaration plugin is
installed. The list below is when no declaration module is installed, so we
have only one default rule with no condition and zero rate.

>>> rt.show(vat.VatRules, language="en")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
+-------+--------------+
| value | Description  |
+=======+==============+
| 1     | Rate 0       |
|       | Book to None |
+-------+--------------+
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

    .. attribute:: can_edit

        Whether the VAT amount can be modified by the user. This applies
        only for documents with :attr:`VatDocument.edit_totals` set
        to `False`.

    .. attribute:: vat_account

        The general account where VAT is to be booked.

    .. attribute:: vat_returnable

        Whether VAT is "returnable" (i.e. not to be paid to or by the
        partner). Returnable VAT, unlike normal VAT, does not increase
        the total amount of the voucher and causes an additional
        movement into the :attr:`vat_returnable_account`.

    .. attribute:: vat_returnable_account

        Where to book returnable VAT. If VAT is returnable and this
        field is empty, then VAT will be added to the base account.


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



VAT areas
=========

A **VAT area** is a group of countries for which same VAT rules apply in the
the country of the site owner.

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


Simple account invoices
=======================
    
.. class:: VatAccountInvoice
                   
    An invoice for which the user enters just the bare accounts and
    amounts (not products, quantities, discounts).

    An account invoice does not usually produce a printable
    document. This model is typically used to store incoming purchase
    invoices, but exceptions in both directions are possible: (1)
    purchase invoices can be stored using `purchases.Invoice` if stock
    management is important, or (2) outgoing sales invoice can have
    been created using some external tool and are entered into Lino
    just for the general ledger.


.. class:: Invoices
           
    The table of all :class:`VatAccountInvoice` objects.

.. class:: InvoicesByJournal
           
    Shows all invoices of a given journal (whose
    :attr:`voucher_type <lino_xl.lib.ledger.models.Journal.voucher_type>`
    must be :class:`VatAccountInvoice`)

.. class:: PrintableInvoicesByJournal
           
    Purchase journal

.. class:: InvoiceDetail
           
    The detail layout used by :class:`Invoices`.    

.. class:: InvoiceItem
           
    An item of a :class:`VatAccountInvoice`.


.. class:: ItemsByInvoice

.. class:: VouchersByPartner           



Utilites
========

>>> from lino_xl.lib.vat.utils import add_vat, remove_vat

>>> add_vat(100, 21)
121.0

>>> remove_vat(121, 21)
100.0

>>> add_vat(10, 21)
12.1

>>> add_vat(1, 21)
1.21




Intracom sales and purchases
============================

The plugin defines two reports accessible via the
:menuselection:`Reports --> Accounting` menu and integrated in the
printout of a VAT declaration:

.. TODO:  why do the tables span all periods?

.. class:: IntracomSales
           
    Show a list of all sales invoices whose VAT regime is Intra-Community.
    
.. class:: IntracomPurchases

    Show a list of all purchase invoices whose VAT regime is Intra-Community.

.. class:: IntracomInvoices

    Common base class for :class:`IntracomSales` and
    :class:`IntracomPurchases`

>>> rt.show(vat.IntracomSales, language='en')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
No data to display

>>> rt.show(vat.IntracomPurchases, language='en')
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
No data to display



Model mixins
============

.. class:: VatTotal

    Model mixin which defines the fields :attr:`total_incl`,
    :attr:`total_base` and :attr:`total_vat`.

    Used for both the document header (:class:`VatDocument`) and for
    each item (:class:`VatItemBase`).

    .. attribute:: total_incl
    
        The amount VAT *included*.

    .. attribute:: total_base

        The amount VAT *excluded*.

    .. attribute:: total_vat

        The amount of VAT.

    All three total fields are :class:`lino.core.fields.PriceField`
    instances.  When :attr:`edit_totals` is `False`, they are all
    disabled, otherwise only :attr:`total_vat` is disabled when
    :attr:`VatRule.can_edit` is `False`.

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

.. class:: VatDeclaration

    Abstract base class for VAT declarations.

    A **VAT declaration** is when a company declares to its government
    how much sales and purchases they've done during a given period.

    A VAT declaration is a computed summary of ledger movements in an
    **observed period**, but it is also itself a ledger voucher which
    generates new movements in its own period.

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
           
.. class:: DeclarationField

    Base class for all fields of VAT declarations.

    .. attribute:: both_dc
    .. attribute:: editable
    .. attribute:: fieldnames

       An optional space-separated list of names of other declaration
       fields to be observed by this field.
                   
    .. attribute:: vat_regimes
    .. attribute:: vat_classes
    .. attribute:: vat_columns
                   
    .. attribute:: exclude_vat_regimes
    .. attribute:: exclude_vat_classes
    .. attribute:: exclude_vat_columns
    .. attribute:: is_payable
    

.. class:: DeclarationFieldsBase           
           
Configuration
=============

See also :class:`lino_xl.lib.vat.Plugin` for configuration options
and the :mod:`lino_xl.lib.vat.utils` module contains some utility
functions.



