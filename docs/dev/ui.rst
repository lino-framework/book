.. _dev.ui:

======================
Writing new front ends
======================


Overview
========

ExtJS is the built-in primary front end for Lino. It is stable and won't change
any more.

React has the advantage that your application will me usable from a mobile
device.  React is being used on two production sites, both of which are
"internal", i.e. we are our own customer. We have no customer yet who is ready
to invest into a mobile-friendly front end. They all say that they would want
it, but they don't want to pay extra money for it...

The :ref:`openui5` front end has passed the proof of concept phase, i.e. it is
visible that it works. But it is not ready for production. There is still much
work to do. We have no plans to continue this  front end because we focus on
extjs  and react. But if you are willing to invest your time, then we are glad
to support you as much as possible.


Lino can have many faces
========================

Lino is designed to have *many possible* front ends.  It comes with an
extensible collection of *out-of-the-box* front ends. You can write a Lino
application once and then deploy it via different web interfaces.

There are currently only two realistic choices for the front end:
:mod:`lino.modlib.extjs` (the classic front end based on ExtJS) and the
:ref:`React front end <react>` (the new front end that will replace ExtJS step
by step). The `Demo sites <http://www.lino-framework.org/demos.html>`__ page
shows both front ends for some applications.

The :ref:`React front end <react>` is already used in production on several
sites.  But there are more conservative customers who still prefer the clasic
front end.  Both front ends are currently maintained.



Alternative front ends
======================

There are several proofs of concept for alternative front ends.

- The :ref:`extjs6` front end was almost ready for production but went asleep
  because the ExtJS library is unfortunately no longer free. More precisely its
  free community version is not maintained.

- OpenUI5 is developed by SAP, conceptually quite similar to ExtJS.  We
  developed the :mod:`lino_openui5` front end, which was almost ready for
  production, but stopped this project when we discovered :ref:`react`.

- The :mod:`lino.modlib.bootstrap3` web interface optimized for
  read-only access and publication of complex data (something like
  :ref:`belref`). We acknowledgethat this needs more work before
  becoming really usable.

- One might consider Lino's :class:`TextRenderer
  <lino.core.renderer.TextRenderer>` (used for writing :doc:`tested
  functional specifications </dev/doctests>`) as a special kind of
  front end.

- a more lightweight web interface using some other JS framework than
  ExtJS.  e.g. `Angular <https://angular.io/>`__ or `Vue
  <https://github.com/vuejs/ui>`__

- A console UI using `ncurses
  <https://en.wikipedia.org/wiki/Ncurses>`_ would be nice.  Not much
  commercial benefit, but a cool tools for system administrators.

- We once started working on an interface that uses the :doc:`Qooxdoo
  library </topics/qooxdoo>`.

- A desktop application using `PyQt
  <https://en.wikipedia.org/wiki/PyQt>`_.
  There is a first prototype of the :manage:`qtclient` command.

- Something similar could be done for `wxWidgets
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
