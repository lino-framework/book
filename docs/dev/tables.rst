.. doctest docs/dev/tables.rst
.. _lino.tutorial.tables:

=========================
Introduction to tables
=========================

..
    >>> from lino import startup
    >>> startup('lino_book.projects.tables.settings')
    >>> from lino.api.doctest import *
    
.. contents::
    :depth: 1
    :local:

What is a table?
================

In a Lino application you don't write only your *models* in Python,
but also something we call **tables**.

While your *models* describe how data is to be *stored in the
database*, *tables* describe how data is to be *presented to users*.

Tables are Python class objects which are never instantiated.

A table describes how to display some data in a tabular way, They do
this in an *abstract* way, i.e. independently of the user interface.
The same table can be used to render data interactively as a grid
panel or on a printable document as a table.

Lino's "tables" are roughly equivalent of Django's "views".  With Lino
you don't need to write views because Lino writes them for you.
Actually a Lino table corresponds only to one class of Django's views,
sometimes referred to as "tabular" or "list" views. The other class of
views are "detail" views, for which you are going to define
:doc:`Layouts <layouts/index>` (we'll talk about these later).


Model tables
============

There can be more than one table for a given model, but each table has
exactly one model as its data source.  That model is specified in the
:attr:`model <lino.core.dbtables.Table.model>` attribute of the table.
For every database model there should be at least one table.  Lino
will generate a default table for models that have no table at all.

.. Note that there may be *more than one table* for a given
   model. That's a fundamental difference from Django's concept of the
   `ModelAdmin` class and `Model._meta` options.

Much information about your table is automatically extracted from the
model: the **columns** correspond to the *fields* of your database
model.  The **header** of every column is the `verbose_name` of its
field.  The values in a column are of same **data type** for each
row. So Lino knows all these things from your models.

The **rows** of a table can be **sorted** and **filtered**. These are
things which are done in Django on a QuerySet.  Lino doesn't reinvent
the wheel here and just forwards them to their corresponding Django
methods: :attr:`order_by <lino.core.tables.AbstractTable.order_by>`,
:attr:`filter <lino.core.tables.AbstractTable.filter>` and
:attr:`exclude <lino.core.tables.AbstractTable.exclude>`.

But here is something you cannot express on a Django model: *which*
columns are to be shown, and their order.  This is defined by the
:attr:`column_names <lino.core.tables.AbstractTable.column_names>`
attribute, a simple string with a space-separated list of field names.

Tables can hold information which goes beyond a model or a
queryset. For example we set :attr:`hide_sums
<lino.core.tables.AbstractTable.hide_sums>` to `True` on the ``Books``
table because otherwise Lino would display a sum for the "published"
column.

.. _slave_tables:

Slave tables
============

A table is called a **slave table** when it "depends" on a master.

For example the `BooksByAuthor` table shows the *books* written by a
given *author.  Or the `ChoicesByQuestion` table in
:ref:`lino.tutorial.polls` shows the *choices* for a given *question*
(its master).  Other examples of slave tables are used in
:ref:`dev.lets` and :doc:`/dev/table_summaries`.
     
A slave table cannot render if we don't define the master.  You cannot
render `BooksByAuthor` if you don't specify for *which* author you
want it.


.. _own_window:

Show a slave table in own window
================================

Slave tables are usually rendered as elements of a detail layout.  The
widget used to render a slave table in a detail window is called a
**slave panel**.

.. |own_window| image:: /user/own_window.png

A slave panel has a special button |own_window| in its upper right
corner used to show that slave table in a separate window.  This
button is important for several functions.

- If the table's display_mode is ``'summary'``, the
  |own_window| button is the only way to see the table as a grid.

- The slave panel shows only 15 rows, even if there are more.

- The slave panel has no pagination toolbar while the separate window
  does.

     

Exercise
========

The files we are going to use in this tutorial are already on your
hard disk in the :mod:`lino_book.projects.tables` package.

Start your development server and your browser, and have a look at the
application::

  $ go tables
  $ python manage.py runserver

Explore the application and try to extend it: change things in the
code and see what happens.


Here is the :xfile:`models.py` file :

.. literalinclude:: ../../lino_book/projects/tables/models.py

The :file:`fixtures/demo.py` file contains the data we use to fill our
database:

.. literalinclude:: ../../lino_book/projects/tables/fixtures/demo.py

  
Designing your tables
=====================

There is another file named :xfile:`desktop.py` which describes the
tables we are going to use in this tutorial:

.. literalinclude:: ../../lino_book/projects/tables/desktop.py

Database *models* are usually named in *singular* form, tables in
*plural* form.

Tables may inherit from other tables (e.g. ``BooksByAuthor`` inherits
from ``Books``: it is basically a list of books, with the difference
that it shows only the books of a given author.

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
*virtual* tables, we will talk about them in a later tutorial.

Since tables are normal Python classes they can use inheritance.  In
our code `BooksByAuthor` inherits from `Books`.  That's why we don't
need to explicitly specify a `model` attribute for `BooksByAuthor`.

`BooksByAuthor` is an example of a :ref:`slave table <slave_tables>`.
It shows the books of a given `Author`.  This given Author is called
the "master" of these Books.  We also say that a slave table *depends*
on its master.

Lino manages this dependency almost automatically.  The application
developer just needs to specify a class attribute :attr:`master_key
<lino.core.tables.AbstractTable.master_key>`.  This attribute, when
set, must be a string containing the name of a `ForeignKey` field
which must exist in the Table's model.

A table can defined attributes like :attr:`filter
<lino.core.tables.AbstractTable.filter>` and :attr:`order_by
<lino.core.tables.AbstractTable.order_by>` which you know from Django's
`QuerySet API
<https://docs.djangoproject.com/en/1.11/ref/models/querysets/>`_.

A table is like a grid widget, 
it has attributes like :attr:`column_names
<lino.core.tables.AbstractTable.column_names>` which describe how to
display it to the user.

But the table is even more than the definition of a grid widget.  It
also has attributes like :attr:`detail_layout
<lino.core.actors.Actor.detail_layout>` which tells it how to display
the detail of a single record in a form view.

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
console, in a script, in a testcase, in a web interface or in a GUI
window.

At this point of our tutorial, we won't yet fire up a web browser
(because we want to explain a few more concepts like menus and layouts
before we can do that), but we can already play with our data using
Django's console shell::

  $ python manage.py shell

The first thing you do in a :manage:`shell` session is to import
everything from :mod:`lino.api.shell`:

>>> from lino.api.shell import *

This imports especially a name ``rt`` which points to the
:mod:`lino.api.rt` module.  ``rt`` stands for "run time" and it
exposes Lino's runtime API.  In our first session we are going to use
the :meth:`show <lino.api.rt.show>` method and the :meth:`actors
<lino.core.site.Site.actors>` object.

>>> rt.show(tables.Authors)
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

>>> rt.show(tables.Books)
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
of :ref:`slave tables <slave_tables>` :

>>> adams = tables.Author.objects.get(last_name="Adams")
>>> rt.show(tables.BooksByAuthor, adams)
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
=========== ======================================
 Published   Title
----------- --------------------------------------
 1978        The Hitchhiker's Guide to the Galaxy
 1990        Last chance to see...
=========== ======================================
<BLANKLINE>


Before going on, please note that the preceding code snippets are
**tested** as part of Lino's test suite.  This means that as a core
developer you can run a command (:cmd:`inv test` in case you are
curious) which will parse the source file of this page, execute every
line that starts with ``>>>`` and verifies that the output is the same
as in this document.  If a single dot changes, the test "fails" and
the developer will find out the reason.

Writing test cases is an important part of software development.  It
might look less funny than developing cool widgets, but actually these
are part of analyzing and describing how your users want their data to
be structured.  Which is the more important part of software
development.



Defining a web interface
========================

The last piece of the user interface is the *menu definition*, located
in the :xfile:`__init__.py` file ot this tutorial:

.. literalinclude:: ../../lino_book/projects/tables/__init__.py

Every plugin of a Lino application can define its own subclass of
:class:`lino.core.plugin.Plugin`, and Lino instantiates these objects
automatically a startup, even before importing your database models.

You might ask "Why can't we just define the menu commands in our
:xfile:`settings.py` or the :xfile:`models.py` files? That question
goes beyond the scope of this tutorial

Note that a plugin corresponds to what Django calls an application.

Read more about plugins in :ref:`dev.plugins`.


.. _remote_master:

Tables with remote master
=========================

The :attr:`master_key` of a :ref:`slave table <slave_tables>` can be a remote field. 

When you have three models A, B and C with A.b being a pointer to B
and B.c being a pointer to C, then you can design a table `CsByA`
which shows the C instances of a given A instance by saying::

    class CsByA(Cs):
        master_key = "c__b"

For example :class:`lino_xl.lib.courses.CoursesByTopic` shows all
courses about a given topic. But a course has no FK `topic`, so you
cannot say ``master_key = 'topic'``. But a course does know its topic
indirectyl because it knows it's course series, and the course series
knows its topic. So you can specify a remote field::

  master_key = 'line__topic'

Other examples

- :class:`lino_avanti.lib.courses.RemindersByPupil`
  
.. :class:`lino_xl.lib.courses.EntriesByTeacher`





Virtual tables
==============

Besides *model-based tables* (used to display data from the database
using its model), Lino has :doc:`virtual tables <vtables>` **virtual
tables** which have no model because they get their rows from
somewhere else than the database.

The **rows** of a virtual table are defined by a method
:meth:`get_data_rows <lino.core.tables.AbstractTable.get_data_rows>`.
In a *model-based table* this method has a default implementation
based on the :attr:`model <lino.core.tables.Table.model>` attribute.

:class:`lino.core.tables.AbstractTable` is the base class for 
:class:`lino.core.tables.Table`  and
:class:`lino.core.tables.VirtualTable` 


