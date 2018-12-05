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
==================== ================== ==================== ========== ============= ===========================
 Designation          Designation (de)   Designation (fr)     Flatrate   Sales price   Sales account
-------------------- ------------------ -------------------- ---------- ------------- ---------------------------
 Group therapy        Gruppentherapie    Group therapy                   30,00         (7010) Sales on therapies
 Individual therapy   Einzeltherapie     Individual therapy              60,00         (7010) Sales on therapies
 Other                Sonstige           Autre                           35,00
 **Total (3 rows)**                                                      **125,00**
==================== ================== ==================== ========== ============= ===========================
<BLANKLINE>


