.. _dev.lets:
.. _lino.tutorial.lets:

=============================
A Local Exchange Trade System
=============================

In this tutorial we imagine a whole Lino project from scratch.  The
fictive application described here is is probably a bit too simple for
a real-life website.  But we *imagine* that this is what our customer
*asked* us to do.  (More about the Lino application development
process in :doc:`/dev/analysis`.)


.. contents::
   :local:


The functional specification
============================


Overview
--------

The fictive application we are going to write is a website of a Local
Exchange Trade System group (`LETS
<http://en.wikipedia.org/wiki/Local_exchange_trading_system>`_). The
members of that site would register the products and services they
want to sell or to buy. The goal is to connect the providers and the
customers.

Database structure
------------------

- **Products** : one row for every product or service. We keep it
  simple and just record the designation for our products. We don't
  even record a price.

- **Members** : the people who use this site to register their offers
  and demands. For each member we record their contact data such as
  place and email.

- An **Offer** is when a given member declares that they want to *sell*
  a given product.

- A **Demand** is when a given member declares that they want to *buy* a
  given product.

- Every member is located in a given **Place**. And in a future
  version we want to add filtering on offers and demands limited to
  the place.

Menu structure
--------------

- **Master**:

  - Products -- show the list of products
  - Members -- show the list of members

- **Market**

  - Offers  -- show the full list of all offers
  - Demands  -- show the full list of all demands


The **main page** (dashboard) should display a list of products
available for exchange.

.. _data_model_diagram:


Graphically representing the database structure
===============================================

Here is a **graphical representation** of the database structure:

.. graphviz:: 

   digraph foo  {

       graph [renderer="neato"]

       node [shape=box]
       node [style=filled]
           node [fontname="times bold", fillcolor=red]  
              Product Member
           node [fontname="times" fillcolor=gold]  Offer  Demand
           node [fontname="times italic" fillcolor=lightblue]  Place

       Product -> Offer[arrowhead="inv"]
       Product -> Demand[arrowhead="inv"]
    
       Offer -> Member[taillabel="provider", labelangle="-90", labeldistance="2"];
       Demand -> Member[taillabel="customer", labelangle="90", labeldistance="2"];
       Member ->  Place;

  }

You shoud do such diagrams by hand, together with the customer.  Above
picture has been realized using `graphviz
<http://www.sphinx-doc.org/en/stable/ext/graphviz.html>`__.  You might
prefer `Dia <http://dia-installer.de/>`_ which renders it as follows:

.. image:: models.png

There are many methodologies for visualizsing a database model (`UML
<https://en.wikipedia.org/wiki/Unified_Modeling_Language>`_, `IDEF1X
<https://en.wikipedia.org/wiki/IDEF1X>`__), and above style is just
our favourite because it is so simple, intuitive and useful.  The
basic rules are:

- Every **node** on the diagram represents a database model.
- Every **arrow** on the diagram represents a `ForeignKey`.  We prefer
  to use the word **pointer** instead of *ForeignKey* when talking with
  a customer because that's more intuitive.

- We display the **name of a pointer** only if it differs from the
  model it points to. For example the arrow from *Offer* to *Product*
  is a FK field called `product`, defined on the *Offer* model. We do
  not display the name `product` on our diagram because that would be
  a waste of place.

The colors of this diagram are a convention for grouping the models
into three "data categories":

- **red** is for **master data** (i.e. relatively stable data)
- **yellow** is for **moving data** (i.e. data which changes
  relatively often)
- **blue** is for **configuration data** (i.e. data which is rather in
  background and accessible only to site administrators)



Note about many-to-many relationships
=====================================

There are two `many-to-many relationships
<https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/>`_
between *Member* and *Product*: 

- A given member can *offer* multiple products, and a given product
  can *be offered* by multiple members. We can call this the
  **providers** of a product.

- A given member can *want* multiple products, and a given product can
  *be wanted* by multiple members. We can call this the **customers** of
  a product.

Using Django's interface for `many-to-many relationships
<https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_many/>`_, 
we can express this as follows::

    providers = models.ManyToManyField(
        'lets.Member', through='lets.Offer', related_name='offered_products')
    customers = models.ManyToManyField(
        'lets.Member', through='lets.Demand', related_name='wanted_products')


Which you can read as follows:

- *Offer* is the "intermediate model" used "to govern the m2m relation
  *Product.providers* / *Member.offered_products*.

- *Demand* is the intermediate model used to govern the m2m relation
  *Product.customers* / *Member.wanted_products*.

A *ManyToManyField* is originally a shortcut for telling Django to
create an automatic, "invisible", additional model, with two
ForeignKey fields.  But in most real-life situations you anyway want
to define what Django calls "`extra fields on many-to-many
relationships
<https://docs.djangoproject.com/en/1.11/topics/db/models/#intermediary-manytomany>`_",
and thus you must explicitly name that "intermediate model" of your
ManyToManyField.  That's why we recommend to always explicitly name
the intermediate models of your m2m relations.



Writing a prototype
===================

With above information you should be ready to write a "first draft" or
"prototype".

For this tutorial we wrote actually *two* prototypes. In the second
variant the members are "polymorphic": they can be either customers or
suppliers, or both. This is an example of multi-table inheritance and
how you can use it with Lino's :class:`Polymorphic
<lino.mixins.polymorphic.Polymorphic>` mixin.

=============================== ===============================
code                            specs
=============================== ===============================
:mod:`lino_book.projects.lets1` :doc:`/specs/projects/lets1`
:mod:`lino_book.projects.lets2` :doc:`/specs/projects/lets2`
=============================== ===============================
  
Note the difference between "code" and "specs". The **code** directory
contains runnable Python code and maybe application-specific
configuration files. A copy of this would be needed on a production
site.  The **specs** is a Sphinx documentation tree and contains
mainly :file:`.rst` files. These are not needed on a production site.

Please explore these projects and try to get them running.  If you
have installed a Lino Development environment, you can simply do::

  $ go lets1
  $ python manage.py prep
  $ python manage.py runserver

And point your browser to http://127.0.0.1:8000/


Form layouts
============

Note the `detail_layout` attributes of certain tables.  They define
the **layout** of the **detail window** for these database models (a
detail window is what Lino opens when the user double-clicks on a
given row).


.. textimage:: t3a-3.jpg
    :scale: 50%

    The detail window of a **Product** should show the data fields and
    two slave tables, one showing the the **offers** and another with
    the **demands** for this product.

    Here is the code for this::

        detail_layout = """
        id name
        OffersByProduct DemandsByProduct
        """
    
When seeing the code on the left, you should be able to imagine
something like the picture on the right.



The web interface
=================

Here are some screenshots.

.. image:: a.png
    :scale: 70
    
.. image:: b.png
    :scale: 70
    
.. image:: c.png
    :scale: 70
    
.. image:: d.png
    :scale: 70
    
.. image:: e.png
    :scale: 70
    
.. image:: members_insert.png
    :scale: 30
    
