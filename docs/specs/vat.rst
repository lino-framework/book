.. _xl.vat:

=============================
VAT (Value-added tax)
=============================

.. to run only this test:

    $ doctest docs/specs/vat.rst
    
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

See also :class:`lino_xl.lib.vat.Plugin` for configuration options.

The :mod:`lino_xl.lib.vat.utils` module contains some utility
functions.

Code snippets in this document are based on the
:mod:`lino_book.projects.apc` demo.

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *


Related plugins
===============

Installing this plugin will automatically install
:mod:`lino_xl.lib.countries` :mod:`lino_xl.lib.ledger`.

>>> dd.plugins.vat.needs_plugins     
['lino_xl.lib.countries', 'lino_xl.lib.ledger']

Site operators outside the European Union are likely to use
:mod:`lino_xl.lib.vatless` instead.

The modules :mod:`lino_xl.lib.vatless` and :mod:`lino_xl.lib.vat` can
theoretically both be installed though obviously this wouldn't make
sense.

Applications using this plugin will probably also install one of the
national implementations for their VAT declarations
(:mod:`lino_xl.lib.bevat`, :mod:`lino_xl.lib.bevats`, ...)



Fixtures
========

The demo fixtures :mod:`novat <lino_xl.lib.vat.fixtures.novat>` and
:mod:`euvatrates <lino_xl.lib.vat.fixtures.euvatrates>` are mutually
exclusive (should not be used both) and must be loaded before any
`demo` fixture (because otherwise :mod:`lino_xl.lib.vat.fixtures.demo`
would not find any VAT regimes to assign to partners).


Intracom
========

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
 *SLS 2*                Rumma & Ko OÜ               EE100588749   Innergemeinschaftlich   1 685,80            354,02       2 039,82
 *SLS 10*               Bernd Brechts Bücherladen                 Innergemeinschaftlich   1 322,25            277,67       1 599,92
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
 *PRC 2*                 Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   116,78              24,52        141,30
 *PRC 9*                 Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,35              24,65        142,00
 *PRC 16*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   118,52              24,88        143,40
 *PRC 23*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,44              24,66        142,10
 *PRC 30*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   115,87              24,33        140,20
 *PRC 37*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   116,78              24,52        141,30
 *PRC 44*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,35              24,65        142,00
 *PRC 51*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   118,52              24,88        143,40
 *PRC 58*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,44              24,66        142,10
 *PRC 65*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   115,87              24,33        140,20
 *PRC 72*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   116,78              24,52        141,30
 *PRC 79*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,35              24,65        142,00
 *PRC 86*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   119,67              25,13        144,80
 *PRC 93*                Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   118,59              24,91        143,50
 *PRC 100*               Rumma & Ko OÜ   EE100588749   Innergemeinschaftlich   117,03              24,57        141,60
 **Total (15 Zeilen)**                                                         **1 761,34**        **369,86**   **2 131,20**
======================= =============== ============= ======================= =================== ============ ===================
<BLANKLINE>

.. class:: IntracomInvoices

    Common base class for :class:`IntracomSales` and
    :class:`IntracomPurchases`



Models and actors reference
===========================


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
        only for documents with :attr:`VatTotal.auto_compute_totals` set
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
    
    Accessible via :menuselection:`Configure --> VAT --> VAT rules`.

    >>> show_menu_path(vat.VatRules)
    Konfigurierung --> MwSt. --> MwSt-Regeln
    
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

    All three total fields are
    :class:`lino.core.fields.PriceField` instances.
    When
    :attr:`auto_compute_totals` is `True`, they
    are all disabled, 
    otherwise
    only :attr:`total_vat`
    is disabled
    when :attr:`VatRule.can_edit` is `False`.

    .. attribute:: auto_compute_totals = False
                   
        Set this to `True` on subclasses who compute their totals
        automatically, i.e. the fields :attr:`total_base`,
        :attr:`total_vat` and :attr:`total_incl` are disabled.  This is
        set to `True` for :class:`lino_xl.lib.sales.SalesDocument`.
                  
    .. method:: get_trade_type

        Subclasses of VatTotal must implement this method.

    .. method:: get_vat_rule

        Return the VAT rule for this voucher or voucher item. Called
        when user edits a total field in the document header when
        :attr:`auto_compute_totals` is False.


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

    .. attribute:: partner

       Mandatory field to be defined in another class.

    .. attribute:: refresh_after_item_edit

        The total fields of an invoice are currently not automatically
        updated each time an item is modified.  Users must click the
        Save or the Register button to see the invoices totals.

        One idea is to have
        :meth:`lino_xl.lib.vat.models.VatItemBase.after_ui_save`
        insert a `refresh_all=True` (into the response to the PUT or
        POST coming from Lino.GridPanel.on_afteredit).
        
        This has the disadvantage that the cell cursor moves to the
        upper left corner after each cell edit.  We can see how this
        feels by setting :attr:`refresh_after_item_edit` to `True`.

    .. attribute:: vat_regime

        The VAT regime to be used in this document.  A pointer to
        :class:`VatRegimes`.

           
.. class:: VatItemBase
           
    Model mixin for items of a :class:`VatTotal`.

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

    Model mixin for items of a :class:`VatTotal`, adds `unit_price`
    and `qty`.

    .. attribute:: unit_price
                   
    .. attribute:: qty

    Abstract Base class for :class:`lino_xl.lib.sales.InvoiceItem` and
    :class:`lino_xl.lib.sales.OrderItem`, i.e. the lines of invoices
    *with* unit prices and quantities.


                
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
        
        >>> vat.VatAreas.get_for_country('NL')
        <VatAreas.eu:20>
   
        >>> vat.VatAreas.get_for_country('BE')
        <VatAreas.national:10>
    
        >>> vat.VatAreas.get_for_country('')
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
           
.. autoclass:: lino_xl.lib.vat.mixins.VatDeclaration

.. class:: DeclarationField
           
.. autoclass:: lino_xl.lib.vat.choicelists.DeclarationField
           
