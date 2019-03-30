.. doctest docs/specs/tera/products.rst
.. _specs.tera.products:

=========================
``products`` in Lino Tera
=========================

The :mod:`lino_xl.lib.products` plugin is called "Fees" in Lino Tera
because here we don't produce anything, we just sell services.


.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *


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


Price rules
===========

Price rules are used in Lino Tera to define the "tarification table"

.. class:: PriceFactors

    A choicelist of "price factors".

    This list is empty by default.  Applications can define their specific
    price factors.  Every price factor causes a field to be injected to the
    :class:`lino_xl.lib.contats.Partner` model.

    >>> rt.show(products.PriceFactors)
    ======= ============= =======================
     value   name          text
    ------- ------------- -----------------------
     10      residence     Residence
     20      income        Income category
     30      composition   Household composition
    ======= ============= =======================
    <BLANKLINE>

.. class:: PriceRules

    The list of price rules.

    >>> rt.show(products.PriceRules)
    ===== =========== ================= ==================================== ======================== ====================
     No.   Residence   Income category   Household composition                Service type             Fee
    ----- ----------- ----------------- ------------------------------------ ------------------------ --------------------
     1                                   More than one participant below 18   Individual appointment   Individual therapy
     2                                                                        Group meeting            Group therapy
     3                                                                        Individual appointment   Individual therapy
    ===== =========== ================= ==================================== ======================== ====================
    <BLANKLINE>
