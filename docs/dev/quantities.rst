.. doctest docs/dev/quantities.rst
.. _book.dev.quantities:


=====================
Quantities
=====================

.. Doctest initialization:

    >>> import lino
    >>> lino.startup('lino_book.projects.pierre.settings.demo')
    >>> from lino.api.doctest import *


Table of contents:

.. contents::
   :depth: 1
   :local:

     
:mod:`lino.utils.quantities`.
:mod:`lino_xl.lib.sales`

>>> Invoice = rt.models.sales.VatProductInvoice
>>> Item = rt.models.sales.InvoiceItem
>>> Product = rt.models.products.Product
>>> from lino.utils.quantities import Quantity, Percentage, Decimal
>>> # show_fields(Item, all=True)

>>> voucher = Invoice.objects.all().first()
>>> product = Product.objects.get(pk=1)
>>> product.sales_price
Decimal('199.99')


>>> i = Item(voucher=voucher, product=product)
>>> i.product_changed()
>>> i.total_incl
Decimal('199.99')
>>> print(repr(i.qty))
Decimal('1')

>>> i.qty = Quantity("2")
>>> i.qty_changed()
>>> i.total_incl
Decimal('399.98')

>>> i.discount = Percentage("10")
>>> i.discount_changed()
>>> i.total_incl
Decimal('359.98')

>>> i.qty = Quantity("0")
>>> i.qty_changed()
>>> i.total_incl
Decimal('0.00')


The qty field is nullable and can be `None`, which means "no value".
This makes sense e.g. in lines without any product:

>>> i = Item(voucher=voucher)
>>> print(repr(i.qty))
None
>>> i.reset_totals()
>>> i.set_amount(None, Decimal("100"))
>>> i.total_incl
Decimal('100.00')

>>> print(repr(i.qty))
None
