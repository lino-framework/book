.. doctest docs/specs/invoicing.rst
.. _cosi.specs.invoicing:

===================
Generating invoices
===================

The :mod:`lino_xl.lib.invoicing` plugin adds functionality for
**invoicing**, i.e. automatically generating invoices from data in the
database.

This document describes some general aspects of invoicing and how
applications can handle this topic.
See also

- :doc:`/specs/voga/invoicing`
- :doc:`sales`
- :doc:`accounting`

The examples in this document have been tested using the :mod:`pierre
<lino_book.projects.pierre>` demo project.

>>> from lino import startup
>>> startup('lino_book.projects.pierre.settings.demo')
>>> from lino.api.doctest import *
>>> ses = rt.login("robin")
>>> translation.activate('en')


.. contents::
   :depth: 1
   :local:


Manually editing automatically generated invoices
=================================================

Resetting title and description of a generated invoice item
===========================================================

When the user sets `title` of an automatically generated invoice
item to an empty string, then Lino restores the default value for
both title and description



.. class:: SalesRule
           
   .. attribute:: partner
   .. attribute:: invoice_recipient
   .. attribute:: paper_type
                  
.. class:: SalesRules
           
.. class:: Plan

    An **invoicing plan** is a rather temporary database object which
    represents the plan of a given user to have Lino generate a series
    of invoices.

    .. attribute:: user
    .. attribute:: journal

        The journal where to create invoices.  When this field is
        empty, you can fill the plan with suggestions but cannot
        execute the plan.

    .. attribute:: max_date
    .. attribute:: today
    .. attribute:: partner

    .. attribute:: update_plan
    .. attribute:: execute_plan

        Execute this plan, i.e. create an invoice for each selected
        suggestion.

    .. method:: start_plan(user, **options)
           
        Start an invoicing plan for the given `user` on the database
        object defined by `k` and `v`. Where `k` is the name of the
        field used to select the plan (e.g. `'partner'` or
        `'journal'`) and `v` is the value for that field.

        This will either create a new plan, or check whether the
        currently existing plan for this user was for the same
        database object. If it was for another object, then clear all
        items.

    .. method:: fill_plan(ar)
                
        Add items to this plan, one for each invoice to generate.

        This also groups the invoiceables by their invoiceable
        partner.

        Note a case we had (20171007) : One enrolment for Alfons whose
        invoice_recipient points to Erna, a second enrolment for Erna
        directly. The first enrolment returned Erna as Partner, the
        second returned Erna as Pupil, so they were not grouped.

.. class:: Item

    The items of an invoicing plan are called **suggestions**.

    .. attribute:: plan
    .. attribute:: partner
    .. attribute:: preview
    
        A textual preview of the invoiceable items to be included in
        the invoice.


    .. attribute:: amount
    .. attribute:: invoice

        The invoice that has been generated. This field is empty for
        new items. When an item has been executed, this field points
        to the generated invoice.

    .. attribute:: workflow_buttons

    The following fields are maybe not important:

    .. attribute:: first_date
    .. attribute:: last_date
    .. attribute:: number_of_invoiceables

    .. method:: create_invoice(ar):
           
        Create the invoice corresponding to this item of the plan.


.. class:: Plans
.. class:: MyPlans
.. class:: AllPlans
.. class:: Items
.. class:: ItemsByPlan
.. class:: InvoicingsByInvoiceable

The ``Invoiceable`` model mixin
===============================

.. class:: Invoiceable

    Mixin for things that are "invoiceable", i.e. for which a customer
    is going to receive an invoice.

    Subclasses must implement the following:

    .. method:: get_invoiceables_for_plan(cls, plan, partner=None)
                
        Yield a sequence of invoiceables (of this class) for the given
        plan.  If a `partner` is given, use it as an additional filter
        condition.

    .. attribute:: incoiceable_date_field

       The name of the field which holds the invoiceable date.  Must
       be set by subclasses.
       

    .. method:: get_invoiceable_product(self, plan)

        To be implemented by subclasses.  Return the product to put
        into the invoice item.
                
    .. method:: get_invoiceable_qty(self)
                
        To be implemented by subclasses.  Return the quantity to put
        into the invoice item.


    .. method:: get_invoiceable_title(self, invoice=None)

        Return the title to put into the invoice item.  May be
        overridden by subclasses.

    The mixin adds the following methods to the model:
        
    .. attribute:: invoicings

        A simple `GenericRelation
        <https://docs.djangoproject.com/ja/1.9/ref/contrib/contenttypes/#reverse-generic-relations>`_
        to all invoice items pointing to this enrolment.

        This is preferred over :meth:`get_invoicings`.

           
    .. method:: get_invoicings(**kwargs)

        Get a queryset with the invoicings which point to this
        enrolment.

        This is deprecated. Preferred way is to use
        :attr:`invoicings`.

                
Actions
=======

.. class:: StartInvoicing

    Base for :class:`StartInvoicingForJournal` and
    :class:`StartInvoicingForPartner`.

.. class:: StartInvoicingForJournal
           
    Start an invoicing plan for this journal.

    This is installed onto the VouchersByJournal table of the
    VoucherType for the configured :attr:`voucher_model
    <lino_xl.lib.invoicing.Plugin.voucher_model>` as
    `start_invoicing`.

           
.. class:: StartInvoicingForPartner
           
    Start an invoicing plan for this partner.

    This is installed onto the :class:`contacts.Partner
    <lino_xl.lib.contacts.Partner>` model as `start_invoicing`.

    
.. class:: UpdatePlan

    Build a new list of suggestions.    
    This will remove all current suggestions.
           
           
.. class:: ExecutePlan
           
   Execute this invoicing plan.
   Create an invoice for each selected suggestion.

           
.. class:: ExecuteItem
           
    Create an invoice for this suggestion.

.. class:: ToggleSelection
    
    Invert selection status for all suggestions.
           
