.. doctest docs/dev/remote_fields.rst
.. _dev.remote_fields:

=============
Remote fields
=============

This page explains a concept we call **remote fields**.

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q
>>> translation.activate("en")


Django has lookups that span relationships
==========================================

Let's say you want to see your sales invoices to clients in Eupen.

For this you can do the following:

>>> eupen = countries.Place.objects.get(name="Eupen")
>>> qs = sales.VatProductInvoice.objects.filter(partner__city=eupen)
>>> qs.count()
44

Above code is equivalent (but much more efficient) to the following code:

>>> len([invoice for invoice in sales.VatProductInvoice.objects.all()
...    if invoice.partner.city == eupen])
44

This is plain Django knowledge, documented in `Lookups that span relationships
<https://docs.djangoproject.com/en/3.0/topics/db/queries/#lookups-that-span-relationships>`__.


Lino extends this idea by allowing to also specify layout elements using this
syntax.

For example if you want, in your :class:`sales.Invoices` table, a column showing
the city of the partner of each invoice,  you can simply specify
``partner__city`` as a field name in your :attr:`column_names
<lino.core.actors.tables.AbstractTable.column_names>`.

>>> rt.show(sales.Invoices,
...   column_names="id partner partner__city total_incl", limit=5)
===== ================== ============= ==============
 ID    Partner            Locality      Total to pay
----- ------------------ ------------- --------------
 177   da Vinci David     4730 Raeren   1 110,16
 176   da Vinci David     4730 Raeren   535,00
 175   di Rupo Didier     4730 Raeren   280,00
 174   Radermacher Jean   4730 Raeren   679,81
 173   Radermacher Inge   4730 Raeren   2 039,82
                                        **4 644,79**
===== ================== ============= ==============
<BLANKLINE>

.. glossary::

  remote field

    A virtual field created automatically on the fly by pointing to a field in a
    related object.

    A remote field is a chain of subfields to be walked through for each row.

    The intermediate subfields of a remote field must be pointers (either
    ForeignKey or OneToOneField). The last subfield is called the :term:`leaf
    field`.

    A remote field is an instance of :class:`lino.core.fields.RemoteField`.

  leaf field

    The last subfield of a remote field.
    This field determines the return type of the remote field itself.


You can use remote fields also in a :term:`detail layout`. When all their
intermeditate subfields are OneToOneField, they are editable. For example the
:term:`detail layout` of partners in :ref:`voga` has a field
``salesrule__paper_type`` where you can set the paper type to be used for this
partner in new invoices.  In this case, :attr:`Partner.salesrule` is a
OneToOneField pointing to the one and only
:class:`lino_xl.lib.invoicing.SalesRule` instance for this partner.

.. Theoretically also in
   an :term:`insert layout`, though we have no usage example for this.

You can also use remote fields as :term:`actor parameters <actor parameter>`. This is useful mostly
when the :term:`leaf field` is either a ForeignKey or a ChoiceListField. For
example, :meth:`lino_xl.lib.orders.Order.get_simple_parameters` defines
``journal__room`` as :term:`simple actor parameter`::

  class Order(...):

      @classmethod
      def get_simple_parameters(cls):
          for f in super(Order, cls).get_simple_parameters():
              yield f
          yield 'journal__room'


You can even use a remote field pointing to a :term:`virtual field` as
:term:`actor parameter`,  But that virtual field must have a :attr:`return_type
<lino.core.fields.VirtualField.return_type>` of ForeignKey, and you must also
write a :meth:`lino.core.model.Model.setup_parameters` method on your model that
defines this field. That's because remote fields are kind of volatile fields
that get created on the fly when a layout asks for them. In :ref:`presto` we
have a usage example where we add a parameter field ``project__municipality`` to
tables on the :class:`cal.Event` model.  That why we extend the
:class:`cal.Event` model::



    from lino.core.fields import make_remote_field

    @classmethod
    def setup_parameters(cls, params):
        super(Event, cls).setup_parameters(params)
        params['project__municipality'] = make_remote_field(cls, 'project__municipality')

    @classmethod
    def get_request_queryset(cls, ar, **filter):
        qs = super(Event, cls).get_request_queryset(ar, **filter)
        pv = ar.param_values
        if pv.project__municipality:
            places = pv.project__municipality.whole_clan()
            qs = qs.filter(project__isnull=False, project__city__in=places)
        return qs


catch_layout_exceptions
=======================

Some general documentation about :attr:`catch_layout_exceptions`.

This setting tells Lino what to do when it encounters a wrong field name in a
layout specification.  It will anyway raise an Exception, but the difference is
the content of the error message.

The default value for this setting is True.
In that case the error message reports only a summary of the
original exception and tells you in which layout it happens.
Because that's your application code and probably the place where
the bug is hidden.

>>> settings.SITE.catch_layout_exceptions
True

For example:

>>> rt.show(sales.Invoices,
...   column_names="id partner foo total_incl")
Traceback (most recent call last):
  ...
Exception: lino.core.layouts.ColumnsLayout on lino_xl.lib.sales.models.Invoices has no data element 'foo'


>>> rt.show(sales.Invoices,
...   column_names="id partner partner__foo total_incl")
Traceback (most recent call last):
  ...
Exception: lino.core.layouts.ColumnsLayout on lino_xl.lib.sales.models.Invoices has no data element 'partner__foo'


>>> settings.SITE.catch_layout_exceptions = False
>>> rt.show(sales.Invoices,
...   column_names="id partner partner__foo total_incl")  #doctest: +SKIP
Traceback (most recent call last):
  ...
Exception: Invalid RemoteField contacts.Partner.partner__foo (no field foo in contacts.Partner)

Skipped because after 20200430 there is no longer a difference in the exception
message.


..  When you mistakenly specify "partner.city" instead of "partner__city", Lino
    raises an exception:

    >>> rt.show(sales.Invoices,
    ...   column_names="id partner partner.city total_incl")
    Traceback (most recent call last):
      ...
    Exception: lino.core.layouts.ColumnsLayout on lino_xl.lib.sales.models.Invoices has no data element 'partner.city'


Notes
=====

Note that Lino's remote fields have nothing to do with
Django's :attr:`remote_field` of a ForeignKey field.
