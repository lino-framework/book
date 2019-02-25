.. _dev.ui:

======================
Writing new front ends
======================

Lino can have many faces
========================

Lino is designed to have *many possible* front ends.  It comes with an
extensible collection of *out-of-the-box* front ends. You can write a Lino
application once and then deploy it via different interfaces.

A real-world example for this is :ref:`noi` which can be deployed using two
public UIs.  Inspect the :mod:`lino_book.projects.team` and
:mod:`lino_book.projects.bs3` demo projects.


Alternative front ends
======================

There are several proofs of concept for alternative front ends.

- The :ref:`extjs6` front end is almost ready for production.  But it is
  currently asleep because the ExtJS library is unfortunately no
  longer free. More precisely its free community version is not
  maintained.
  
- The :ref:`React front end <react>`  is almost ready for production.

- The :ref:`OpenUI5 <specs.openui5>` project is almost ready for
  production.  OpenUI5 is developed by SAP, conceptually quite similar
  to ExtJS.
  
- The :mod:`lino.modlib.bootstrap3` web interface optimized for
  read-only access and publication of complex data (something like
  :ref:`belref`). We acknowledgethat this needs more work before
  becoming really usable.
  
- One might consider Lino's :class:`TextRenderer
  <lino.core.renderer.TextRenderer>` (used for writing :doc:`tested
  functional specifications </dev/doctests>`) as a special kind of
  front end.

- a more lightweight web interface using some other JS framework than
  ExtJS.  e.g. `Anular <https://angular.io/>`__ or `Vue
  <https://github.com/vuejs/ui>`__
  
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

  

Elements of a front end
=======================

In :doc:`/dev/about/ui` we say that Lino separates business logic and front
end.  That's a noble goal, but the question is *where exactly* you are going to
separate.  The actual challenge is the API between them.

The general elements of every Lino application are:

- the **main menu** : a hierarchical representation of the
  application's functions.  In multi-user applications the main menu
  changes depending on the user permissions.

- a highly customizable **grid widget** for rendering tabular data.

- form input using **detail windows** which can contain :ref:`slave
  tables <slave_tables>`, custom panels, ...

