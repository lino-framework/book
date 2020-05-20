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

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.doctests')
>>> from lino.api.doctest import *


Overview
========

.. glossary::

  product

    Something you can trade (e.g. sell, buy, rent) in an item of a :term:`trade
    document`. Mostly a name and a price. It can be material (a good) or
    immaterial (a service).

    The :mod:`lino_xl.lib.sales` plugins injects a :attr:`sales_price` field to
    the product model.

    Products can be grouped into :term:`categories <product category>`, and every
    product must be of a given :term:`product type`.

  product category

    A group of products that fit together.

    The list of product categories of a site can be modified by its :term:`end
    users <end user>` (provided they have access rights).

  product type

    A name for the nature or type of a set of products.

    Used for example to differentiate between "Services" and "Goods".

    The detail layout of a product can vary depending on its type, but not
    depending on its category.

    Every application has its specific list of product types.
    This list can be locally modified by the :term:`site maintainer`.

    Rule of thumb: product **categories** can get edited by end users while
    product **types** are hard-coded by the application developer.

  price factor

    A property of a partner that may influence the price of certain products.

    The list of price factors is meant to be defined by the :term:`application
    developer`. Changing it locally would also require changes in the some
    layouts.  Changes to this list may require a database migration because
    every price factor causes a field to be injected to the
    :class:`lino_xl.lib.contats.Partner` model.

  price rules

    A set of rules that specify which product to use for a given :term:`price
    selector` and a given set of price factors.

  price selector

    A database object used to specify "what is being sold" in price rules.

    In :ref:`voga` and :ref:`presto` we use  the :term:`calendar entry type` as
    price selector,  in :ref:`noi` the :class:`lino_xl.lib.working.SessionType`.


Products
========


.. class:: Product

    Django model to represent a *product*.

    .. attribute:: description

        The description of this product.

        This is a BabelField, so there will be one field for every language
        defined in :attr:`lino.core.site.Site.languages`.

    .. attribute:: product_type

        The type of this product.

        This field may not be blank and must be an item of :class:`ProductTypes`.

        The default value is set by the actor used for creating the product.
        Some product actors don't have a default product type, in that case the
        default value is :attr:`ProductTypes.default`.

    .. attribute:: cat

        The category of this product.

        This is a pointer to :class:`ProductCat`, but the selection list is
        limited to thos categories having the same :attr:`product_type`.

    .. attribute:: delivery_unit

        Pointer to :class:`DeliveryUnits`

    .. attribute:: vat_class

        The VAT class.  Injected by :mod:`lino_xl.lib.vat`. If that plugin is
        not installed, :attr:`vat_class` is a dummy field.


    .. method:: get_ruled_price(self, partner, selector)

        Return the product to use for this partner and this selector according
        to the :term:`price rules`.


.. class:: Products

  Base class for all tables of products.


>>> rt.show(products.Products, )
==== ================================================================ ================================================================ ================================================================ ================= ===============
 ID   Bezeichnung                                                      Bezeichnung (fr)                                                 Bezeichnung (en)                                                 Kategorie         Verkaufspreis
---- ---------------------------------------------------------------- ---------------------------------------------------------------- ---------------------------------------------------------------- ----------------- ---------------
 9    Bildbearbeitung und Unterhalt Website                            Traitement d'images et maintenance site existant                 Image processing and website content maintenance                 Website-Hosting   25,00
 10   Book                                                             Book                                                             Book                                                             Sonstige          29,90
 6    EDV Konsultierung & Unterhaltsarbeiten                           ICT Consultation & maintenance                                   IT consultation & maintenance                                    Website-Hosting   30,00
 8    Programmierung                                                   Programmation                                                    Programming                                                      Website-Hosting   40,00
 7    Server software installation, configuration and administration   Server software installation, configuration and administration   Server software installation, configuration and administration   Website-Hosting   35,00
 11   Stamp                                                            Stamp                                                            Stamp                                                            Sonstige          1,40
 2    Stuhl aus Holz                                                   Chaise en bois                                                   Wooden chair                                                     Möbel             99,99
 4    Stuhl aus Metall                                                 Chaise en métal                                                  Metal chair                                                      Möbel             79,99
 1    Tisch aus Holz                                                   Table en bois                                                    Wooden table                                                     Möbel             199,99
 3    Tisch aus Metall                                                 Table en métal                                                   Metal table                                                      Möbel             129,99
 5    Website-Hosting 1MB/Monat                                        Hébergement 1MB/mois                                             Website hosting 1MB/month                                        Website-Hosting   3,99
                                                                                                                                                                                                                           **675,25**
==== ================================================================ ================================================================ ================================================================ ================= ===============
<BLANKLINE>


Product categories
==================

**Product categories** can be used to group products into "categories".
Categories can be edited by the user via
:menuselection:`Configure --> Products --> Categories`
or
:menuselection:`Configure --> Sales --> Categories`.

>>> show_menu_path(products.ProductCats)
Konfigurierung --> Verkauf --> Produktkategorien


.. class:: ProductCat

    Django model to represent a *product category*.

    .. attribute:: product_type

        The product type to apply to products of this category.


    >>> rt.show(products.ProductCats)
    ==== ================= =============================== ================== ============== =============
     ID   Bezeichnung       Bezeichnung (fr)                Bezeichnung (en)   Product type   description
    ---- ----------------- ------------------------------- ------------------ -------------- -------------
     1    Möbel             Meubles                         Furniture          Produkte
     2    Website-Hosting   Hébergement de sites Internet   Website Hosting    Produkte
     3    Sonstige          Autre                           Other              Produkte
    ==== ================= =============================== ================== ============== =============
    <BLANKLINE>


Product types
=============

Products can be differentiated by their "type".
Types cannot be edited by the
user.  But every product type can have a layout on its own.
Every product type has its own menu entry.


.. class:: ProductType

    .. attribute:: text

        The verbose name of this product type.

        This string is used for the menu entries in :menuselection:`Configure
        --> Products`.

    .. attribute:: table_name

        The name of the table to use for displaying a list of products with this type.

.. class:: ProductTypes

    The list of *product types*.

    It should contain at least one item whose name is :attr:`default`.

    For each item of this list the plugin adds one menu entry to the
    :menuselection:`Configure` menu.

    .. attribute:: default

    The product type to be set on new products when they are created in an
    actor that doesn't have a default product type.



    >>> rt.show(products.ProductTypes)
    ====== ========= ========== ===================
     Wert   name      Text       Table name
    ------ --------- ---------- -------------------
     100    default   Produkte   products.Products
    ====== ========= ========== ===================
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


Price rules
===========

Price rules can be used to define which products are available for a given
partner, and optionally to find a default product for a given :term:`price
selector`.

.. class:: PriceFactors

    The choicelist of :term:`price factors <price factor>`.

    This list is empty by default.  See :ref:`tera` or :ref:`presto` for
    examples of applications that use price factors.

    >>> rt.show(products.PriceFactors)
    Keine Daten anzuzeigen

.. class:: PriceRule

  .. attribute:: seqno

    The sequence number of this rule. Lino loops over price rules in this order
    and returns the first one that applies.

  .. attribute:: product

    The product to use for getting the price when this rule applies.

  .. attribute:: selector

    Either `None` or an additional selector for this price rule.

    When given, this must be an instance of :attr:`lino_xl.lib.products.Plugin.price_selector`.

  Every price rule also has one automatic field for each price factor.


.. class:: PriceRules

    The list of price rules.

    >>> rt.show(products.PriceRules)
    Keine Daten anzuzeigen
