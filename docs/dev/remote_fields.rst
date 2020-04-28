.. doctest docs/dev/remote_fields.rst
.. _dev.remote_fields:

=============
Remote fields
=============

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

This is plain Django, documented in `Lookups that span relationships
<https://docs.djangoproject.com/en/3.0/topics/db/queries/#lookups-that-span-relationships>`__.

Lino extends this idea by allowing to specify layout elements using this syntax.

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

Usage examples in parameter layouts:

- :meth:`lino_xl.lib.orders.Order.get_simple_parameters` defines 'journal__room'
  as actor parameter.

- :ref:`presto` adds a parameter field ``project__municipality`` to its
  :class:`cal.AllEntries` table


catch_layout_exceptions
=======================

Some general documentation about :attr:`catch_layout_exceptions`.

This setting tells Lino what to do when it encounters a wrong
field name in a layout specification.  It will anyway raise an
Exception, but the difference is is the content of the error message.

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
Exception: lino.core.layouts.ColumnsLayout on lino_xl.lib.sales.models.Invoices has no data element 'partner__foo (Invalid RemoteField contacts.Partner.partner__foo (no field foo in contacts.Partner))'


>>> settings.SITE.catch_layout_exceptions = False
>>> rt.show(sales.Invoices,
...   column_names="id partner partner__foo total_incl")
Traceback (most recent call last):
  ...
Exception: Invalid RemoteField contacts.Partner.partner__foo (no field foo in contacts.Partner)


When you mistakenly specify "partner.city" instead of "partner__city", Lino
raises an exception:

>>> rt.show(sales.Invoices,
...   column_names="id partner partner.city total_incl")
Traceback (most recent call last):
  ...
Exception: lino.core.layouts.ColumnsLayout on lino_xl.lib.sales.models.Invoices has no data element 'partner.city'


Notes
=====

Note that Lino's :class:`lino.core.fields.RemoteField` has nothing to do with
Django's :attr:`remote_field` of a FK field.
