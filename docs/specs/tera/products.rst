.. _specs.tera.products:

=======
Tariffs
=======


.. to run only this test:

    $ doctest docs/specs/tera/products.rst
    
    doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models


This document describes how we extend and use the
:mod:`lino_xl.lib.products` plugin in Tera.


>>> rt.show(products.Products)
==== ==================== ==================== ==================== ========== ===========
 ID   Designation          Designation (de)     Designation (fr)     Category   VAT Class
---- -------------------- -------------------- -------------------- ---------- -----------
 1    Group therapy        Group therapy        Group therapy
 2    Individual therapy   Individual therapy   Individual therapy
 3    Other                Sonstige             Autre
==== ==================== ==================== ==================== ========== ===========
<BLANKLINE>


Reference
=========


.. class:: Product
           
    Adds two fields

    .. attribute:: number_of_events

        Number of calendar events paid per invoicing.

    .. attribute:: min_asset

        Minimum quantity required to trigger an invoice.
    

