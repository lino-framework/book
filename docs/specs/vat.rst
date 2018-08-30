.. doctest docs/specs/vat.rst
.. _xl.vat:

=============================
VAT (Value-added tax)
=============================

Table of contents:

.. contents::
   :depth: 1
   :local:

Overview
========

.. currentmodule:: lino_xl.lib.vat

The :mod:`lino_xl.lib.vat` plugin adds functionality for handling
incoming and outgoing invoices in a context where the site operator is
subject to value-added tax (VAT).

Applications to be used only outside the European Union might use
:mod:`lino_xl.lib.vatless` instead.  Though this plugin might become
deprecated.  The modules :mod:`lino_xl.lib.vatless` and
:mod:`lino_xl.lib.vat` can theoretically both be installed though
obviously this wouldn't make sense.

Applications using this plugin will probably also install one of the
national implementations for their VAT declarations
(:mod:`lino_xl.lib.bevat`, :mod:`lino_xl.lib.bevats`, ...)

See also :class:`lino_xl.lib.vat.Plugin` for configuration options
and the :mod:`lino_xl.lib.vat.utils` module contains some utility
functions.



Code snippets in this document are based on the
:mod:`lino_book.projects.apc` demo.

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *


Dependencies
============

Installing this plugin will automatically install
:mod:`lino_xl.lib.countries` :mod:`lino_xl.lib.ledger`.

>>> dd.plugins.vat.needs_plugins     
['lino_xl.lib.countries', 'lino_xl.lib.ledger']


Fixtures
========

The demo fixtures :mod:`novat <lino_xl.lib.vat.fixtures.novat>` and
:mod:`euvatrates <lino_xl.lib.vat.fixtures.euvatrates>` are mutually
exclusive (should not be used both) and must be loaded before any
`demo` fixture (because otherwise :mod:`lino_xl.lib.vat.fixtures.demo`
would not find any VAT regimes to assign to partners).


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




Intracom sales and purchases
============================

The plugin defines two reports accessible via the
:menuselection:`Reports --> Accounting` menu and integrated in the
printout of a VAT declaration:

.. class:: IntracomSales
           
    Show a list of all sales invoices whose :attr:`vat_regime` is
    intra-Community.
    
>>> rt.show(vat.IntracomSales)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
====================== =========================== ============= ======================= =================== ============ ===================
 Rechnung               Partner                     MwSt.-Nr.     MwSt.-Regime            Total zzgl. MwSt.   MwSt.        Total inkl. MwSt.
---------------------- --------------------------- ------------- ----------------------- ------------------- ------------ -------------------
 *SLS 2/2014*           Rumma & Ko OÜ               EE100588749   Innergemeinschaftlich   1 685,80            354,02       2 039,82
 *SLS 10/2014*          Bernd Brechts Bücherladen                 Innergemeinschaftlich   1 322,25            277,67       1 599,92
 **Total (2 Zeilen)**                                                                     **3 008,05**        **631,69**   **3 639,74**
====================== =========================== ============= ======================= =================== ============ ===================
<BLANKLINE>

.. class:: IntracomPurchases

    Show a list of all purchase invoices whose :attr:`vat_regime` is
    intra-Community.
    
>>> rt.show(vat.IntracomPurchases)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
======================= =============== ============= ======================= =================== ============ ===================
 Rechnung                Partner         MwSt.-Nr.     MwSt.-Regime            Total zzgl. MwSt.   MwSt.        Total inkl. MwSt.
----------------------- --------------- ------------- ----------------------- ------------------- ------------ -------------------
 *PRC 2/2014*            Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   116,78              24,52        141,30
 *PRC 2/2015*            Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   119,67              25,13        144,80
 *PRC 9/2014*            Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,35              24,65        142,00
 *PRC 9/2015*            Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   118,59              24,91        143,50
 *PRC 16/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   118,52              24,88        143,40
 *PRC 16/2015*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,03              24,57        141,60
 *PRC 23/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,44              24,66        142,10
 *PRC 30/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   115,87              24,33        140,20
 *PRC 37/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   116,78              24,52        141,30
 *PRC 44/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,35              24,65        142,00
 *PRC 51/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   118,52              24,88        143,40
 *PRC 58/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,44              24,66        142,10
 *PRC 65/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   115,87              24,33        140,20
 *PRC 72/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   116,78              24,52        141,30
 *PRC 79/2014*           Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,35              24,65        142,00
 **Total (15 Zeilen)**                                                         **1 761,34**        **369,86**   **2 131,20**
======================= =============== ============= ======================= =================== ============ ===================
<BLANKLINE>

.. class:: IntracomInvoices

    Common base class for :class:`IntracomSales` and
    :class:`IntracomPurchases`



VAT rules
=========


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

        The regime for which this rule applies. Pointer to
        :class:`VatRegimes <lino_xl.lib.vat.choicelists.VatRegimes>`.
    
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
    
    Accessible via :menuselection:`Explorer --> VAT --> VAT rules`.

    >>> show_menu_path(vat.VatRules)
    Explorer --> MwSt. --> MwSt-Regeln


>>> vat.VatRules.get_vat_rule(vat.VatAreas.national, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.normal).rate
Decimal('0.21')

>>> vat.VatRules.get_vat_rule(vat.VatAreas.international, ledger.TradeTypes.sales, vat.VatRegimes.normal, vat.VatClasses.normal).rate
Decimal('0.21')



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

        The VAT regime to be used in this document.  A pointer to
        :class:`VatRegimes`.


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



                
Choicelists
===========

.. class:: VatAreas

    The global list of VAT areas.

    A VAT area is a geographical area of countries for which same VAT
    rules apply.

    >>> rt.show(vat.VatAreas)
    ====== =============== ===============
     Wert   name            Text
    ------ --------------- ---------------
     10     national        National
     20     eu              EU
     30     international   International
    ====== =============== ===============
    <BLANKLINE>
    

    .. classmethod:: get_for_country(cls, country)
                     
        Return the VatArea instance for this country.

        >>> print(dd.plugins.countries.country_code)
        BE
        
        >>> vat.VatAreas.get_for_country(countries.Country(isocode='NL'))
        <VatAreas.eu:20>
   
        >>> vat.VatAreas.get_for_country(countries.Country(isocode='BE'))
        <VatAreas.national:10>
    
        >>> vat.VatAreas.get_for_country(countries.Country(isocode='US'))
        <VatAreas.international:30>

.. class:: VatClasses

    The global list of VAT classes.

    A VAT class is a direct or indirect property of a trade object
    (e.g. a Product) which determines the VAT *rate* to be used.  It
    does not contain the actual rate because this still varies
    depending on your country, the time and type of the operation, and
    possibly other factors.

    Default classes are:

    .. attribute:: exempt

    .. attribute:: reduced

    .. attribute:: normal


.. class:: VatColumns

                   
    The global list of VAT columns.

    The VAT column of a ledger account indicates where the movements
    on this account are to be collected in VAT declarations.
    

.. class:: VatRegime
           
    Base class for choices of :class:`VatRegimes`.
    
    The **VAT regime** of an invoice determines how the VAT is being
    handled, i.e. whether and how it is to be paid.
    
    You can define a *default VAT regime* per partner.
    
    The VAT regime does not depend on the *trade type*.

    .. attribute:: item_vat
                   
        Whether unit prices are VAT included or not.

.. class:: VatRegimes

    The global list of *VAT regimes*.  Each item is an instance of
    :class:`VatRegime`.

    Three regimes are considered standard minimum:

    .. attribute:: normal
    .. attribute:: subject
    .. attribute:: intracom
                   

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
           
