.. doctest docs/dev/remote_fields.rst
.. _dev.remote_fields:

=============
Remote fields
=============

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *
>>> translation.activate("en")

Let's say you want to see your sales invoices to clients in Eupen.

In plain Django you can do the following:

>>> eupen = countries.Place.objects.get(name="Eupen")
>>> qs = sales.VatProductInvoice.objects.filter(partner__city=eupen)
>>> qs.count()
44

This is documented in `Lookups that span relationships
<https://docs.djangoproject.com/en/3.0/topics/db/queries/#lookups-that-span-relationships>`__.

Lino extends this idea by allowing to specify layout elements using this syntax.

>>> sales.Invoices.column_names
'id entry_date partner total_incl user *'

>>> from django.db.models import Q
>>> rt.show(sales.Invoices,
...   column_names="id partner partner__city total_incl",
...   filter=Q(partner__city=eupen), limit=5)
===== ==================== ============ ==============
 ID    Partner              Locality     Total to pay
----- -------------------- ------------ --------------
 159   Meier Marie-Louise   4700 Eupen   770,00
 158   Mießen Michael       4700 Eupen   465,96
 157   Meessen Melissa      4700 Eupen   639,92
 156   Malmendier Marc      4700 Eupen   3 599,71
 155   Leffin Josefine      4700 Eupen   310,20
                                         **5 785,79**
===== ==================== ============ ==============
<BLANKLINE>



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
