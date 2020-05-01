.. doctest docs/dev/layouts/index.rst
.. _layouts:

=======================
Introduction to layouts
=======================

.. currentmodule:: lino.core.layouts

A **layout** is a description of how to visually arrange the fields and
other data elements in an entry form or a table.

Layouts are one of Lino's important features, which it adds to the Django
framework.  They provide a way to design forms using the Python language and
independently of the chosen :term:`front end`.


.. contents::
    :depth: 2
    :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lets1.settings')
>>> from lino.api.doctest import *
>>> ses = rt.login('robin')



The columns of a table
======================

The simplest occurrence of layouts is the :attr:`column_names
<lino.core.tables.AbstractTable.column_names>` attribute of a table,
used to define which fields should be displayed as the columns of that
table.

Code example (from :doc:`/dev/lets/index`)::

    class Products(dd.Table):
        ...
        column_names = 'id name providers customers'
        ...

Result:

.. image:: products.png
  :scale: 40 %



The layout of a detail window
=============================

Another frequent usage of layouts is the :term:`detail window`, i.e. the window
used to display one table row at a time.

You define a detail window by setting the :attr:`detail_layout
<lino.core.actors.Actor.detail_layout>` attribute of a table.  For
example::


    class Members(dd.Table):
        ...
        detail_layout = """
        id name place email
        OffersByMember DemandsByMember
        """

Result:

.. image:: ../lets/b.png
  :scale: 50 %

Note that the names ``id``, ``name``, ``place`` and ``email`` in the
above example represent **single-line** entry fields while
``OffersByMember`` and ``DemandsByMember`` refer to **multi-line**
panels containing a grid.


The insert window
=================

**Insert windows** are similar to detail windows, but they are used on
rows that do not yet exist.  The most visible difference is their
default size: while detail windows usually take the full screen,
insert windows usually are modular pop-up windows.

You define an insert window by setting the :attr:`insert_layout
<lino.core.actors.Actor.insert_layout>` attribute of a table.  For
example::

    class Members(dd.Table):
        ...
        insert_layout = """
        name place
        email
        """

Result:

.. image:: ../lets/members_insert.png
  :scale: 50 %




Where layouts are being used
============================

Until now we have seen that the following attributes of your tables
contain layouts:

- :attr:`column_names <lino.core.tables.AbstractTable.column_names>`
  contains an instance of  :class:`ColumnsLayout`
- :attr:`detail_layout <lino.core.actors.Actor.detail_layout>`
  contains an instance of :class:`DetailLayout`
- :attr:`insert_layout <lino.core.actors.Actor.insert_layout>`
  contains an instance of :class:`InsertLayout`

There are two other places where Lino uses layouts:

- The *parameter panel* of a table, specified as the
  :attr:`params_layout <lino.core.actors.Actor.params_layout>` attribute
  and containing an instance of :class:`ParamsLayout`.  See :doc:`/dev/parameters`.

- The optional *action dialog* of a custom action, specified as the
  :attr:`params_layout <lino.core.actions.Action.params_layout>`
  attribute of an action and containing an instance of
  :class:`ActionParamsLayout`). See :doc:`/dev/action_parameters`.

Data elements
=============

The **data elements** of a normal layout (:class:`ColumnsLayout`,
:class:`DetailLayout` or :class:`InsertLayout`), can be:

- database fields
- virtual fields
- :term:`slave tables <slave table>`
- panels_ (see below)

:class:`ParamsLayout` are special but similar: their data elements
refer to the :term:`actor parameters <actor parameter>`.

And the data elements of an :class:`ActionParamsLayout`
refer to the :term:`action parameters <action parameter>`.



The template string
====================

For simple layouts it is enough to specify them just as a string
template, as in the examples above.  Lino will automatically convert
such string templates into instances of :class:`ColumnsLayout`,
:class:`DetailLayout`, :class:`InsertLayout`, :class:`ParamsLayout` or
:class:`ActionParamsLayout`.

A layout template is a string containing words, where each word is the
name of a *data element*.


Panels
======

A Layout consists of *panels*.
Every layout has at least one panel whose name is ``main``.

When a :attr:`detail_layout <lino.core.actors.Actor.detail_layout>` is
a string, then Lino replaces this by a :class:`DetailLayout` instance
whose `main` panel is that string.



Writing layouts as classes
==========================

In more complex situations it may be preferrable or even necessary to
define your own layout class.

You do this by subclassing :class:`DetaiLayout`.  For example::

  class PartnerDetail(dd.DetailLayout):

      main = """
      id name
      description contact
      """

      contact = """
      phone
      email
      url
      """

  class Partners(dd.Table):
      ...
      detail_layout = PartnerDetail()




Each panel is a class attribute defined on your subclass, containing a
string value to be used as template describing the content of that
panel.

It can define more panels whose names may be chosen by the application
developer (just don't chose the name :attr:`window_size` which has a
special meaning, and don't start your panel names with an underscore
because these are reserved for internal use).


Panels are **either horizontal or vertical**, depending on whether
their template contains at least one newline character or not.

Indentation doesn't matter.

If the `main` panel of a :class:`FormLayout` is horizontal,
ExtJS will render the Layout using as a tabbed main panel.
If you want a horizontal main panel instead, just insert
a newline somewhere in your main's template. Example::


  class NoteLayout(dd.FormLayout):
      left = """
      date type subject
      person company
      body
      """

      right = """
      uploads.UploadsByController
      cal.TasksByController
      """

      # the following will create a tabbed main panel:

      main = "left:60 right:30"

      # to avoid a tabbed main panel, specify:
      main = """
      left:60 right:30
      """


Glossary
========

.. glossary::

  detail layout

    The layout of a :term:`detail window`.
    See `The layout of a detail window`_

  column layout

    The string that specifies how `The columns of a table`_ are laid out.

See also
========

- :doc:`/tutorials/layouts`
- :ref:`lino.tutorial.polls`.
- :mod:`lino.core.layouts`
