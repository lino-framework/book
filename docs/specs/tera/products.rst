.. doctest docs/specs/tera/products.rst
.. _specs.tera.products:

====================
Fees in Lino Tera
====================

The :mod:`lino_xl.lib.products` plugin is called "Fees" in Lino Tera
because here we don't produce anything, we just sell services.


.. doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models



.. currentmodule:: lino_tera.lib.products     

Fees in the demo database
=========================

>>> rt.show(products.Products)
==== ==================== ================== ==================== ============= =========================== =============
 ID   Designation          Designation (de)   Designation (fr)     Sales price   Sales account               Category
---- -------------------- ------------------ -------------------- ------------- --------------------------- -------------
 1    Group therapy        Gruppentherapie    Group therapy        30,00         (7010) Sales on therapies   Fees
 2    Individual therapy   Einzeltherapie     Individual therapy   60,00         (7010) Sales on therapies   Fees
 3    Other                Sonstige           Autre                35,00
 4    Prepayment           Anzahlung          Prepayment                                                     Prepayments
                                                                   **125,00**
==== ==================== ================== ==================== ============= =========================== =============
<BLANKLINE>


