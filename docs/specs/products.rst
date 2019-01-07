.. doctest docs/specs/products.rst
.. _specs.products:

===================================================
``products`` : defining the things you sell and buy
===================================================

.. currentmodule:: lino_xl.lib.products
                   
The :mod:`lino_xl.lib.products` plugin adds functionality for managing
"products".

.. contents::
   :depth: 1
   :local:

.. include:: /include/tested.rst
             
>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *



Reference
=========


.. class:: Product

    A product is something you can sell or buy.  The :mod:`lino_xl.lib.sales`
    plugins injects a `sales_price` field.

    .. attribute:: description

        The description of this product.

        This is a BabelField, so there will be one field for every language
        defined in :attr:`lino.core.site.Site.languages`.

    .. attribute:: cat

        Pointer to :class:`ProductCat`

    .. attribute:: delivery_unit

        Pointer to :class:`DeliveryUnits`

    .. attribute:: vat_class

        The VAT class.  Injected by :mod:`lino_xl.lib.vat`. If that plugin is
        not installed, :attr:`vat_class` is a dummy field.



    >>> rt.show(products.Products)
    ==== ================================================================ ================================================================ ================================================================ ================= ===============
     ID   Bezeichnung                                                      Bezeichnung (fr)                                                 Bezeichnung (en)                                                 Kategorie         Verkaufspreis
    ---- ---------------------------------------------------------------- ---------------------------------------------------------------- ---------------------------------------------------------------- ----------------- ---------------
     9    Bildbearbeitung und Unterhalt Website                            Traitement d'images et maintenance site existant                 Image processing and website content maintenance                 Website-Hosting   25,00
     6    EDV Konsultierung & Unterhaltsarbeiten                           ICT Consultation & maintenance                                   IT consultation & maintenance                                    Website-Hosting   30,00
     8    Programmierung                                                   Programmation                                                    Programming                                                      Website-Hosting   40,00
     7    Server software installation, configuration and administration   Server software installation, configuration and administration   Server software installation, configuration and administration   Website-Hosting   35,00
     2    Stuhl aus Holz                                                   Chaise en bois                                                   Wooden chair                                                     Möbel             99,99
     4    Stuhl aus Metall                                                 Chaise en métal                                                  Metal chair                                                      Möbel             79,99
     1    Tisch aus Holz                                                   Table en bois                                                    Wooden table                                                     Möbel             199,99
     3    Tisch aus Metall                                                 Table en métal                                                   Metal table                                                      Möbel             129,99
     5    Website-Hosting 1MB/Monat                                        Hébergement 1MB/mois                                             Website hosting 1MB/month                                        Website-Hosting   3,99
                                                                                                                                                                                                                               **643,95**
    ==== ================================================================ ================================================================ ================================================================ ================= ===============
    <BLANKLINE>


.. class:: ProductCat

    Can be used to group products into "categories".  Categories can be edited by the user.
   
    >>> rt.show(products.ProductCats)
    ==== ================= =============================== ================== =============
     ID   Bezeichnung       Bezeichnung (fr)                Bezeichnung (en)   description
    ---- ----------------- ------------------------------- ------------------ -------------
     1    Möbel             Meubles                         Furniture
     2    Website-Hosting   Hébergement de sites Internet   Website Hosting
    ==== ================= =============================== ================== =============
    <BLANKLINE>

.. class:: ProductTypes

    Can be used to group products into "types".  Types cannot be edited by the
    user.  But every product type can have a layout on its own.


    >>> rt.show(products.ProductTypes)
    ====== ========= ==========
     Wert   name      Text
    ------ --------- ----------
     100    default   Produkte
    ====== ========= ==========
    <BLANKLINE>


.. class:: DeliveryUnits

    The list of possible delivery units of a product.

    >>> rt.show(products.DeliveryUnits)
    ====== ======= =======
     Wert   name    Text
    ------ ------- -------
     10     hour    Hour
     20     piece   Piece
     30     kg      Kg
    ====== ======= =======
    <BLANKLINE>
