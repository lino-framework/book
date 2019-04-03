.. doctest docs/dev/quantities.rst
b.. _book.dev.quantities:

==========
Quantities
==========

.. currentmodule: lino.utils.quantities

This document explains the :mod:`lino.utils.quantities` module and
how their usage by Lino's extended database fields
:class:`DurationField <lino.core.fields.DurationField>` and
:class:`QuantityField <lino.core.fields.QuantityField>`.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.pierre.settings.demo')
>>> from lino.api.doctest import *
>>> from lino.utils.quantities import parse, DEC2HOUR, Duration, Percentage, Quantity
>>> import datetime
>>> from decimal import Decimal




Overview
========

A **quantity** is a subclass of `Decimal` used to expresses a quantity for
business documents.  There are three types of quantities:

- A **duration** is a quantity expressed in ``hh:mm`` format.
- A **percentage** is a quantity expressed in ``x%`` format.
- A **fraction** is a quantity expressed as ``x/y`` format.

All quantities are stored in the database as text.


The :func:`parse` function decides which subclass of quantity to use. It is
used internally by :class:`QuantityField`.

>>> parse('1')
Decimal('1')
>>> parse('1:15')
Duration('1:15')
>>> parse('33%')
Percentage('33%')


.. class:: Quantity

    The base class for all *quantities*.

.. class:: Duration

    The class to represent a **duration**.

.. class:: Percentage

    The class to represent a **percentage**.

.. class:: Fraction

    The class to represent a **fraction**. (Not yet implemented)




Durations
=========

A :class:`Duration` expresses a duration in `hours:minutes`.

>>> print(Duration('1'))
1:00
>>> print(Duration('2.5'))
2:30
>>> print(Duration('2.50'))
2:30

>>> print(Duration('1:00'))
1:00
>>> print(Duration('1:30'))
1:30
>>> print(Duration('1:55'))
1:55

>>> print(Duration('1:45') * 2)
3:30
>>> print(Duration('1:55') * 2)
3:50

>>> print(Duration('0:45') / 3)
0:15

>>> print(Duration('0:49') / 10)
0:05

>>> print(Duration('1:30') * 2)
3:00
>>> print(Duration('0:03') * 10)
0:30
>>> print(Duration('0:01') * 60)
1:00
>>> print(Duration('0:01') * 6000)
100:00

>>> print(Duration('1:55') + Duration('0:05'))
2:00
>>> print(Duration('1:55') + Duration('0:10'))
2:05

>>> print(Duration('1:55') - Duration('0:10'))
1:45
>>> print(Duration('1:05') - Duration('0:10'))
0:55
>>> print(Duration('8:30') + Duration('1:00'))
9:30

>>> print(Duration(datetime.timedelta(0)))
0:00
>>> print(Duration(datetime.timedelta(0, hours=10)))
10:00
>>> print(Duration(datetime.timedelta(0, minutes=10)))
0:10

A duration can be more than 24 hours, and in that case (unlike
:class:`datetime.datetime`) it is still represented using
`hhhh.mm`:

>>> print(Duration(datetime.timedelta(hours=25)))
25:00

>>> print(Duration(datetime.timedelta(days=128)))
3072:00

>>> print(Duration(datetime.timedelta(0, minutes=24*60+5)))
24:05

>>> print(Duration(datetime.timedelta(1, minutes=5)))
24:05

You can add a duration to a datetime:

>>> datetime.datetime(2019, 4, 3, 23, 45) + Duration("0:30")
datetime.datetime(2019, 4, 4, 0, 15)

Or substract it from a datetime:

>>> datetime.datetime(2019, 4, 3, 0, 15) - Duration("0:30")
datetime.datetime(2019, 4, 2, 23, 45)

Also when the duration is longer than a day:

>>> datetime.datetime(2019, 4, 3, 16, 53) + Duration("36:00")
datetime.datetime(2019, 4, 5, 4, 53)


Difference between DurationField and TimeField
==============================================

A :class:`lino.core.fields.DurationField` might look similar to a
:class:`lino.core.fields.TimeField` or a standard Django :class:`TimeField`.
But keep in mind:

A DurationField is to store a **number of hours (and minutes)** while a time
field contains the time part of a timestamp.  A duration can be more than 24
hours, it can be negative.

You cannot instantiate from :class:`datetime.time` object:

>>> print(Duration(datetime.time(hour=1, minute=28)))
Traceback (most recent call last):
...
ValueError: Cannot convert datetime.time(1, 28) to Duration



Computing with durations
========================

>>> print(Duration('2:30') * 3)
7:30

>>> print(Duration('2:30') * 100)
250:00

>>> print(Duration('0:20') * 3)
1:00

>>> print(Duration('0:20') * 100)
33:20


Formatting
==========

>>> print(Duration("0.33334"))
0:20
>>> print(Duration("2.50"))
2:30

Decimal separator
=================

Both period and comma are accepted as decimal separator:

>>> parse('1.5')
Decimal('1.5')
>>> parse('1,5')
Decimal('1.5')

But you may not use both at the same time:

>>> parse('1,000.50')
Traceback (most recent call last):
...
Exception: Invalid decimal value '1,000.50'


Durations and invoices
========================

The *quantity* field of invoices (:attr:`lino_xl.lib.vat.QtyProductItem.qty`)
is a :class:`dd.QuantityField <lino.core.fields.QuantityField>`).  This is
handy when invoicing services per hour.  For example when you have a hourly
rate of 60€ and worked 20 minutes, you can write '0:20' as quantity and don't
need to convert this to a decimal value ('0.33'):

>>> hourly_rate = Decimal('60.00')

>>> print(hourly_rate * Duration('0:20'))
20.00000000000000000000000000

>>> print(hourly_rate * Decimal('0.33'))
19.8000

And as you can see, you save 20 cents.  You might work around the rounding
problem by adding decimal places to the quantity field, but this is ugly and
remains a workaround:

>>> print(hourly_rate * Decimal('0.333'))
19.98000

>>> print(hourly_rate * Decimal('0.3333'))
19.998000



Percentages
===========

>>> Percentage('10')
Percentage('10%')

>>> Percentage('10%')
Percentage('10%')

Multiplying a decimal with a percentage yields a decimal:

>>> 100 * Percentage('33%')
Decimal('33.00')

>>> Decimal("100.00") * Percentage("33%")
Decimal('33.0000')


Multiplying a percentage with a decimal yields a percentage:

>>> Percentage('5%') * 3
Percentage('15.00%')

When adding decimals to a percentage, the decimal must have its real value, not
the number of percents:

>>> Percentage('5%') + Decimal('0.03')
Percentage('8.00%')





Discounts
=========

For the following examples we need an invoice item. We don't want to
modify our demo data, so we are not going to save it.

>>> Invoice = rt.models.sales.VatProductInvoice
>>> Item = rt.models.sales.InvoiceItem
>>> Product = rt.models.products.Product
>>> from lino.utils.quantities import Quantity, Percentage, Decimal
>>> # show_fields(Item, all=True)

Pick an existing voucher and product:

>>> voucher = Invoice.objects.all().first()
>>> product = Product.objects.get(pk=1)
>>> product.sales_price
Decimal('199.99')

When you set a product on an invoice item, the `qty` becomes 1 and the
amount is updated.

>>> i = Item(voucher=voucher, product=product)
>>> i.product_changed()
>>> i.total_incl
Decimal('199.99')
>>> i.qty
Decimal('1')

You can manually change the quantity to 2, which will update the total
price:

>>> i.qty = Quantity("2")
>>> i.qty_changed()
>>> i.total_incl
Decimal('399.98')

You can give a discount:

>>> i.discount = Decimal("10")
>>> i.discount_changed()
>>> i.total_incl
Decimal('359.98')

Note that :class:`PercentageField <lino.core.fields.PercentageField>` doesn't
use :mod:`lino.utils.quantities` for historical reasons.  This field is
currently just a thin wrapper around :class:`DecimalField`, and Lino adds a
percent sign when printing it.  One day we might change this (:ticket:`2941`).

You can manually set the quantity to 0:

>>> i.qty = Quantity("0")
>>> i.qty_changed()
>>> i.total_incl
Decimal('0.00')

Note that the qty field is nullable and can be `None`, which means "no
value".  This makes sense e.g. in lines without any product:

>>> i = Item(voucher=voucher)
>>> print(repr(i.qty))
None
>>> i.reset_totals()
>>> i.set_amount(None, Decimal("100"))
>>> i.total_incl
Decimal('100.00')

>>> print(repr(i.qty))
None


Utilities
=========

>>> DEC2HOUR
Decimal('0.01666666666666666666666666667')

