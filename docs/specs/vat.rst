.. _xl.vat:

=============================
VAT (Value-added tax)
=============================

.. to run only this test:

    $ doctest docs/specs/vat.rst
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.apc.settings.doctests')
    >>> from lino.api.doctest import *


Table of contents:

.. contents::
   :depth: 1
   :local:

Overview
========

.. currentmodule:: lino_xl.lib.vat

The :mod:`lino_xl.lib.vat` adds functionality for handling incoming
and outgoing invoices in a context where the site operator is subject
to value-added tax (VAT). Site operators outside the European Union
are likely to use :mod:`lino_xl.lib.vatless` instead.

The modules :mod:`lino_xl.lib.vatless` and :mod:`lino_xl.lib.vat` can
theoretically both be installed though obviously this wouldn't make
sense.

Installing this plugin will automatically install
:mod:`lino_xl.lib.countries` :mod:`lino_xl.lib.ledger`.

>>> dd.plugins.vat.needs_plugins     
['lino_xl.lib.countries', 'lino_xl.lib.ledger']



VAT rules
=========

The demo fixtures :mod:`novat <lino_xl.lib.vat.fixtures.novat>` and
:mod:`euvatrates <lino_xl.lib.vat.fixtures.euvatrates>` are mutually
exclusive (should not be used both) and must be loaded before any
`demo` fixture (because otherwise :mod:`lino_xl.lib.vat.fixtures.demo`
would not find any VAT regimes to assign to partners).


Intracom
========

Two tables accessible via the :menuselection:`Reports --> Accounting`
menu and integrated in the printout of a VAT declaration:

.. class:: IntracomSales
           
    Show a list of all sales invoices whose :attr:`vat_regime` is
    intra-Community.
    
>>> rt.show(vat.IntracomSales)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
====================== ==================== =========== ======================= =================== ============== ===================
 Rechnung               Partner              MwSt.-Nr.   MwSt.-Regime            Total zzgl. MwSt.   MwSt.          Total inkl. MwSt.
---------------------- -------------------- ----------- ----------------------- ------------------- -------------- -------------------
 *SLS 5*                Garage Mergelsberg               Innergemeinschaftlich   442,15              92,85          535,00
 *SLS 17*               Ausdemwald Alfons                Innergemeinschaftlich   385,09              80,87          465,96
 *SLS 29*               Evers Eberhart                   Innergemeinschaftlich   1 942,00            407,81         2 349,81
 *SLS 41*               Johnen Johann                    Innergemeinschaftlich   442,15              92,85          535,00
 *SLS 53*               Meier Marie-Louise               Innergemeinschaftlich   385,09              80,87          465,96
 *SLS 65*               Radermacher Hans                 Innergemeinschaftlich   1 942,00            407,81         2 349,81
 **Total (6 Zeilen)**                                                            **5 538,48**        **1 163,06**   **6 701,54**
====================== ==================== =========== ======================= =================== ============== ===================
<BLANKLINE>

.. class:: IntracomPurchases

    Show a list of all purchase invoices whose :attr:`vat_regime` is
    intra-Community.
    
>>> rt.show(vat.IntracomPurchases)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
======================= ================= =========== ======================= =================== ============ ===================
 Rechnung                Partner           MwSt.-Nr.   MwSt.-Regime            Total zzgl. MwSt.   MwSt.        Total inkl. MwSt.
----------------------- ----------------- ----------- ----------------------- ------------------- ------------ -------------------
 *PRC 1*                 AS Express Post               Innergemeinschaftlich   33,06               6,94         40,00
 *PRC 6*                 AS Express Post               Innergemeinschaftlich   34,13               7,17         41,30
 *PRC 11*                AS Express Post               Innergemeinschaftlich   33,55               7,05         40,60
 *PRC 16*                AS Express Post               Innergemeinschaftlich   35,12               7,38         42,50
 *PRC 21*                AS Express Post               Innergemeinschaftlich   33,97               7,13         41,10
 *PRC 26*                AS Express Post               Innergemeinschaftlich   33,06               6,94         40,00
 *PRC 31*                AS Express Post               Innergemeinschaftlich   34,13               7,17         41,30
 *PRC 36*                AS Express Post               Innergemeinschaftlich   33,55               7,05         40,60
 *PRC 41*                AS Express Post               Innergemeinschaftlich   35,12               7,38         42,50
 *PRC 46*                AS Express Post               Innergemeinschaftlich   33,97               7,13         41,10
 *PRC 51*                AS Express Post               Innergemeinschaftlich   33,06               6,94         40,00
 *PRC 56*                AS Express Post               Innergemeinschaftlich   34,13               7,17         41,30
 *PRC 61*                AS Express Post               Innergemeinschaftlich   33,88               7,12         41,00
 *PRC 66*                AS Express Post               Innergemeinschaftlich   35,45               7,45         42,90
 *PRC 71*                AS Express Post               Innergemeinschaftlich   34,30               7,20         41,50
 **Total (15 Zeilen)**                                                         **510,48**          **107,22**   **617,70**
======================= ================= =========== ======================= =================== ============ ===================
<BLANKLINE>






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

.. class:: InvoiceItem
           
    An item of a :class:`VatAccountInvoice`.

.. class:: IntracomInvoices

    Common base class for :class:`IntracomSales` and
    :class:`IntracomPurchases`
           

Model mixins
============

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
    :class:`lino_xl.lib.ledger.models.InvoiceItem`, i.e. the lines of
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

.. class:: VatDeclaration
           
    Base class for VAT declarations. Currently Lino can do Belgian VAT
    declarations (implemented by :class:`bevat.Declaration
    <lino_xl.lib.bevat.Declaration>` in :mod:`lino_xl.lib.bevat`).


                
Choicelists
===========

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
           
    The VAT regime is a classification of the way how VAT is being
    handled for a given partner, e.g. whether and how it is to be
    paid.
    
    .. attribute:: item_vat
                   
        Whether unit prices are VAT included or not.

.. class:: VatRegimes

    The global list of VAT regimes. Each item is an instance of
    :class:`VatRegime`.

    Three regimes are considered standard minimum:

    .. attribute:: normal
    .. attribute:: subject
    .. attribute:: intracom
                   

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
                   
                   
    
