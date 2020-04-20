.. _dev.actions:

=======================
Introduction to actions
=======================

This section tries to explain everything you need to know about actions.

.. contents::
    :depth: 1
    :local:


.. currentmodule:: lino.core.actions


Overview
========

Actions are always linked to an **actor**.  Each actor has its list of actions.

**Standard actions** are installed automatically on every table when Lino starts
up.  They are defined in :mod:`lino.core.actions`.

Application developers can define new :doc:`custom_actions`, or also
override standard actions with their own custom actions.

Some action attributes include:

- label : the text to place on the button or menu item
- help_text : the text to appear as tooltip when the mouse is over
  that button
- handler function : the function to call when the action is invoked
- permission requirements : for whom and under which conditions this
  action is available

.. _window_actions:

Window actions
==============

Some actions cause a new window to open on the client, others don't.
This is specified by the :attr:`opens_a_window` attribute.

For example the :class:`ShowTable` action opens a window showing a
tabular grid view of its actor.  Most items of the main menu are
:class:`ShowTable` actions.

Or the :class:`DeleteSelected` action is visible in the toolbars of
the grid and the detail windows and in the context menu on a grid row.

For example

- :class:`ShowTable`, :class:`ShowDetail`, :class:`ShowInsert` open a
  window

- :class:`DeleteSelected`, :class:`SubmitDetail` and
  :class:`SubmitInsert` send an AJAX request which causes something to
  happen on the server.


Readonly actions
================

See :attr:`Action.readonly`.

Actions and actors
==================

A same action instance can be shared by many actors.  For example the
:class:`DeleteSelected` action is


The default action of an actor
==============================

Each actor has a **default action**. The default action for
:class:`Table <lino.core.dbtables.Table>` is :class:`ShowTable`.
That's why you can define a menu item by simply naming the actor.

For example in the :meth:`setup_menu
<lino.core.plugin.Site.setup_menu>` method in the :ref:`Polls tutorial
<lino.tutorial.polls>`) you say::

    def setup_menu(site, ui, user_type, main):
        m = main.add_menu("polls", "Polls")
        m.add_action('polls.Questions')
        m.add_action('polls.Choices')


The :meth:`add_action <lino.core.menus.Menu.add_action>` method of
Lino's :class:`lino.core.menus.Menu` is smart enough to understand
that if you specify a Table, you mean in fact that table's default
action.
