.. _lino.tutorial.tables:

=========================
An introduction to Tables
=========================


Models, tables and views
========================

In a Lino application you don't write only your *models* in Python,
but also something we call **tables**.  While your *models* describe
how data is to be structured in the database, *tables* describe how
data is to be presented to users in tabular form.

Roughly speaking, Lino's "tables" are the equivalent of what Django
calls "views". With Lino you don't need to write views because Lino
writes them for you. (To be complete, tables correspond only to one
class of Django's views, sometimes referred to as "tabular" or "list"
views. The other class of views are "detail" views, for which you are
going to define *Layouts*, but we'll talk about these later.)

The fact that you can define more than one Table per model is a
fundamental difference from Django's concept of the `ModelAdmin` class
and `Model._meta` options.



An example
==========

The files we are going to use in this tutorial are already on your
hard disk, you can use the project directly from your repository::

    $ cd ~/repositories/book/docs/tutorials/tables

So this tutorial does not require you to create anything. Just follow
the instructions and learn. You may modify the code inside your local
copy of the repository and later undo your changes by using ``git
checkout``.

Here is the :xfile:`models.py` file :

.. literalinclude:: models.py

Here is the data we use to fill our database:

.. literalinclude:: fixtures/demo.py
  
.. 
    >>> from __future__ import print_function
    >>> from lino.utils.dpy import load_fixture_from_module

Let's initialize our database with this fixture::

  $ python manage.py initdb_demo

.. 
    >>> import tables.fixtures.demo as m
    >>> load_fixture_from_module(m)


What is a table?
================

A table, in general, is a rectangular thing divided into rows and
columns, used to display data.

For example, here is how the "Authors" table of our database might
look in a printed document:

============ =========== =========
 First name   Last name   Country
------------ ----------- ---------
 Douglas      Adams       UK
 Albert       Camus       FR
 Hannes       Huttner     DE
============ =========== =========

A table is usually about a given **database model**. The :attr:`model
<lino.core.dbtables.Table.model>` attribute of a Table is mandatory.
For every database model there should be at least one table. Lino will
generate a default table for models for which there is no table at
all.  Note that there may be *more than one table* for a given model.

The **columns** of a table correspond to the *fields* of your database
model. Every column has a **header** which is the `verbose_name` of
that field. The values in a column are of same **data type** for each
row. So Lino knows all these things. Only one information is missing:
the :attr:`column_names <lino.core.tables.AbstractTable.column_names>`
attribute defines *which* columns are to be listed, and in which
order. It is a simple string with a space-separated list of field
names.

The **rows** of a table can be **sorted** and **filtered**. These are
things which are done in Django on a QuerySet.  Lino doesn't reinvent
the wheel here and just forwards them to their corresponding Django
methods: :attr:`order_by <lino.core.tables.AbstractTable.order_by>`,
:attr:`filter <lino.core.tables.AbstractTable.filter>` and
:attr:`exclude <lino.core.tables.AbstractTable.exclude>`.

Tables can hold information which goes beyond a model or a
queryset. For example we set :attr:`hide_sums
<lino.core.tables.AbstractTable.hide_sums>` to `True` on the ``Books``
table because otherwise Lino would display a sum for the "published"
column.



Designing your tables
=====================

There is another file named :xfile:`desktop.py` which describes the
tables we are going to use in this tutorial:

.. literalinclude:: desktop.py

Database *models* are usually named in *singular* form, tables in
*plural* form.

Tables may inherit from other tables (e.g. ``BooksByAuthor``)

The recommended place for defining tables is in a separate file
:file:`desktop.py`.  You might define your tables together with the
models in your :file:`models.py` file, but in that case your
application has no chance to support :ref:`responsive design
<lino.dev.design>`.

A table is the pythonic definition of a tabular view.  As a rule of
thumb you can say that you need one table for every *grid view* used
in your application. Each table is a subclass of :class:`dd.Table
<lino.core.dbtables.Table>`.

To define tables, you simply need to declare their classes.  Lino
discovers and analyzes them when it initializes.  Tables never get
instantiated.

Each table class must have at least one class attribute :attr:`model
<lino.core.dbtables.Table.model>` which points to the model on which
this table will "work". Every row of a table represents an instance of
its model. (This is true only for *database* tables. Lino also has
*virtual* tables, we will talk about them in a :doc:`later tutorial
</tutorials/vtables/index>`).

Since tables are normal Python classes they can use inheritance.  In
our code `BooksByAuthor` inherits from `Books`.  That's why we don't
need to explicitly specify a `model` attribute for `BooksByAuthor`.

`BooksByAuthor` is an example of a **slave table**.  `BooksByAuthor`
means: the table of `Books` of a given `Author`.  This given Author is
called the "master" of these Books.  We also say that a slave table
*depends* on its master.

Lino manages this dependency almost automatically.  The application
developer just needs to specify a class attribute :attr:`master_key
<lino.core.tables.AbstractTable.master_key>`.  This attribute, when
set, must be a string containing the name of a `ForeignKey` field
which must exist in the Table's model.

A table can defined attributes like :attr:`filter
<lino.core.tables.AbstractTable.filter>` and :attr:`order_by
<lino.core.tables.AbstractTable.order_by>` which you know from Django's
`QuerySet API
<https://docs.djangoproject.com/en/1.9/ref/models/querysets/>`_.

A table is like a grid widget, 
it has attributes like :attr:`column_names
<lino.core.tables.AbstractTable.column_names>` which describe how to
display it to the user.

But the table is even more than the definition of a grid widget.  It
also has attributes like :attr:`detail_layout
<lino.core.actors.Actor.detail_layout>` which tells it how to display
a single record in a form view.

Try also to work through the API docs, 
knowing that
:class:`lino.core.dbtables.Table` 
inherits from
:class:`lino.core.tables.AbstractTable` 
who inherits from
:class:`lino.core.actors.Actor`.


Using tables without a web server
=================================

An important thing with tables is that they are independent of any
user interface. You define them once, and you can use them on the
console, in a script, in a unit test, in a web interface or in a GUI
window.

At this point of our tutorial, we cannot yet fire up a web browser
(because we need to explain a few more concepts like menus and layouts
before we can do that), but we can already play with our data using
Django's console shell::

  $ python manage.py shell

And please note that the following code snippets are tested as part of
Lino's test suite. Writing test cases is an important part of software
development. Writing test cases might look less funny than developing
cool widgets, but actually these are part of analyzing and describing
how your users want their data to be structured.  Which is the more
important part of software development.

The first thing you do in a :manage:`shell` session is to import
everything from :mod:`lino.api.shell`:

>>> from lino.api.shell import *

This imports especially a name ``rt`` which points to the
:mod:`lino.api.rt` module.  ``rt`` stands for "run time" and it
exposes Lino's runtime API.  In our first session we are going to use
the :meth:`show <lino.api.rt.show>` method and the :meth:`actors
<lino.core.site.Site.actors>` object.

>>> rt.show(rt.actors.tables.Authors)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
============ =========== =========
 First name   Last name   Country
------------ ----------- ---------
 Douglas      Adams       UK
 Albert       Camus       FR
 Hannes       Huttner     DE
============ =========== =========
<BLANKLINE>

So here is, our ``Authors`` table, in a testable console format!

And here is the ``Books`` table:

>>> rt.show(rt.actors.tables.Books)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
================= ====================================== ===========
 author            Title                                  Published
----------------- -------------------------------------- -----------
 Adams, Douglas    Last chance to see...                  1990
 Adams, Douglas    The Hitchhiker's Guide to the Galaxy   1978
 Huttner, Hannes   Das Blaue vom Himmel                   1975
 Camus, Albert     L'etranger                             1957
================= ====================================== ===========
<BLANKLINE>

These were so-called **master tables**.  We can also show the content
of **slave tables**:

>>> adams = tables.Author.objects.get(last_name="Adams")
>>> rt.show(rt.actors.tables.BooksByAuthor, adams)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== ======================================
 Published   Title
----------- --------------------------------------
 1978        The Hitchhiker's Guide to the Galaxy
 1990        Last chance to see...
=========== ======================================
<BLANKLINE>




Defining a web interface
========================

Before starting the web interface of our application, let's have a
look at the last piece of the user interface, the menu definition:

.. literalinclude:: __init__.py


Exercise
========

Start your development server and your browser, and have a look at the
application::

  $ python manage.py runserver

Explore the application and try to extend it: change things in the
code and see what happens.


Summary
=======

Tables are Python class objects which describe tabular data views in
an abstract way, i.e. independently of the user interface.
