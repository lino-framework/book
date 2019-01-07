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

Fees
====

>>> rt.show(products.Products)
==================== ================== ==================== ============= ============= ===========================
 Designation          Designation (de)   Designation (fr)     Flatrate      Sales price   Sales account
-------------------- ------------------ -------------------- ------------- ------------- ---------------------------
 Group therapy        Gruppentherapie    Group therapy        By presence   30,00         (7010) Sales on therapies
 Individual therapy   Einzeltherapie     Individual therapy   By presence   20,00         (7010) Sales on therapies
 Individual therapy   Einzeltherapie     Individual therapy   Maximum 10    20,00         (7010) Sales on therapies
 Other                Sonstige           Autre                              35,00
 **Total (4 rows)**                                                         **105,00**
==================== ================== ==================== ============= ============= ===========================
<BLANKLINE>


Daybooks
========

>>> rt.show(products.Daybooks)
===================== =================== ===================== ===============
 Designation           Designation (de)    Designation (fr)      Sales account
--------------------- ------------------- --------------------- ---------------
 Cash daybook Daniel   Kassenbuch Daniel   Cash daybook Daniel
===================== =================== ===================== ===============
<BLANKLINE>
