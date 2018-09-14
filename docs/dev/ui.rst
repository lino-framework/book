.. _dev.ui:

==================
The user interface
==================

The ExtJS user interface is stable and quite usable once you accept a
few known oddnesses.  Its most serious limitation is that it is not
very usable on mobile devices.  But more than hundred users use it
every day, and most of them love it.  Which doesn't mean that they
never complain about certain known oddnesses.  Don't forget that
complaining is actaally one facet of love.

Alternatives
============

There are several proofs of concept for alternative user interfaces.

- The :ref:`extjs6` is almost ready for production.  But it is
  currently asleep because the ExtJS library is unfortunately no
  longer free. More precisely its free community version is not
  maintained.
  
- The :ref:`OpenUI5 <specs.openui5>` project is almost ready for
  production.  OpenUI5 is developed by SAP, conceptually quite similar
  to ExtJS.
  
- The :mod:`lino.modlib.bootstrap3` web interface optimized for
  read-only access and publication of complex data (something like
  :ref:`belref`). We acknowledgethat this needs more work before
  becoming really usable.
  
- :ref:`noi` is an example of an application which is deployed using
  two public UIs.

- One might consider Lino's :class:`TextRenderer
  <lino.core.renderer.TextRenderer>` (used for writing :doc:`tested
  functional specifications </dev/doctests>`) as a special kind of
  user interface.

- a more lightweight web interface using some other JS framework than
  ExtJS
  
- A console UI using `ncurses
  <https://en.wikipedia.org/wiki/Ncurses>`_ would be nice.  Not much
  commercial benefit, but a cool tools for system administrators.
  
- We once started working on an interface that uses the :doc:`Qooxdoo
  library </topics/qooxdoo>`.
  
- A desktop application using `PyQt
  <https://en.wikipedia.org/wiki/PyQt>`_.
  There is a first prototype of the :manage:`qtclient` command.

  Something similar could be done for `wxWidgets
  <https://en.wikipedia.org/wiki/WxWidgets>`_.
  
- Support OData to provide an XML or JSON based HTTP interface.

  

Elements of a user interface
============================

In :doc:`/about/ui` we say that Lino separates business logic and user
interface.  That's a noble goal, but the question is *where exactly*
you are going to separate.  The actual challenge is the API between
them.

Lino has a rather high-level API because we target a rather wide range
of possible interfaces.  That API is still evolving and not yet very
well documented, but the basics seem to have stabilized.  Some general
elements of every Lino application are:

- the **main menu** : a hierarchical representation of the
  application's functions.  In multi-user applications the main menu
  changes depending on the user permissions.

- a highly customizable **grid widget** for rendering tabular data in
  an editable way.  This description is used for **

- form input using **detail windows** which can contain :ref:`slave
  tables <slave_tables>`, custom panels, ...

- Context-sensitive ComboBoxes with dynamic data store.

- Keyboard navigation for areas are where manual data entry is needed.

- WYSIWYG rich text editor

- Support for multi-lingual database content

- Unlike some desktop applications Lino does *not* reimplement an
  internal method to open several windows: users simply open several
  browser windows.


