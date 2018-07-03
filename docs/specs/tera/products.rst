.. doctest docs/specs/tera/products.rst
.. _specs.tera.products:

====================
Tariffs in Lino Tera
====================


.. doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models


This document describes how we extend and use the
:mod:`lino_xl.lib.products` plugin in Tera.


>>> rt.show(products.Products)
==== ==================== ==================== ==================== ============= ====================================== ==========
 ID   Designation          Designation (de)     Designation (fr)     Sales price   Sales Base account                     Category
---- -------------------- -------------------- -------------------- ------------- -------------------------------------- ----------
 1    Group therapy        Group therapy        Group therapy        30,00
 2    Individual therapy   Individual therapy   Individual therapy   60,00         (7010) Sales on individual therapies
 3    Other                Sonstige             Autre                35,00
                                                                     **125,00**
==== ==================== ==================== ==================== ============= ====================================== ==========
<BLANKLINE>


Reference
=========


.. class:: Product
           
    Lino Tera has two specific fields:

    .. attribute:: number_of_events

        Number of calendar events paid per invoicing.

    .. attribute:: min_asset

        Minimum quantity required to trigger an invoice.

    Other interesting fields are:
    
    .. attribute:: sales_account

                   


