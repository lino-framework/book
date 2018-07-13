.. doctest docs/dev/quantities.rst
.. _book.dev.quantities:

=====================
Quantities
=====================

.. Doctest initialization:

    >>> import lino
    >>> lino.startup('lino_book.projects.pierre.settings.demo')
    >>> from lino.api.doctest import *

  
This document gives some examples about how to use
:mod:`lino.utils.quantities` and :mod:`lino_xl.lib.sales`.

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
>>> print(repr(i.qty))
Decimal('1')

You can manually change the quantity to 2, which will update the total
price:

>>> i.qty = Quantity("2")
>>> i.qty_changed()
>>> i.total_incl
Decimal('399.98')

You can give a discount:

>>> i.discount = Percentage("10")
>>> i.discount_changed()
>>> i.total_incl
Decimal('359.98')

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
