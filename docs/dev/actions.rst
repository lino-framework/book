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

Actions are always linked to a given :term:`actor`.  Each actor has its list of
actions.

**Standard actions** are installed more or less automatically on every table
when Lino starts up.  They are defined in :mod:`lino.core.actions`.

Application developers can define new :doc:`custom_actions`, or also
override standard actions with their own custom actions.

Some action attributes include:

- label : the text to place on the button or menu item
- help_text : the text to appear as tooltip when the mouse is over
  that button
- handler function : the function to call when the action is invoked
- permission requirements : for whom and under which conditions this
  action is available


Some standard actions
=====================

.. class:: ShowTable

  Open a window with a tabular grid editor on this table.  The grid editor is
  that main widget of that window (otherwise it would be a slave table).

  Most items of the main menu are :class:`ShowTable` actions.

.. class:: ShowDetail

  Open the :term:`detail window` on a table actor.

.. class:: ShowInsert

  Open an insert window on this actor.
  A new row will be inserted only when this window gets submitted,
  which is a separate action named :class:`SubmitInsert`.

.. class:: SubmitInsert

  Create a new database row using the data specified in the insert
  window.  Called when the :guilabel:`Create` button of an insert window was
  clicked.

  Most database models share the same action instance of this, which is stored
  in the :attr:`submit_insert <lino.core.model.Model.submit_insert>` class
  attribute.

.. _window_actions:

Window actions
==============

Some actions do nothing but opening a new window on the client. We call them
:term:`window actions <window action>`.

Examples of window actions are :class:`ShowTable`, :class:`ShowDetail` and
:class:`ShowInsert`.

This behaviour is specified by the :attr:`opens_a_window` attribute.

.. attribute:: Action.opens_a_window

Specifies whether this action opens a window.  It is up to the :term:`front end`
to actually render that window.

Another class of actions also open a window, but that window is not their main
purpose.  For example the Merge action always opens a dialog window with
miscellaneous parameters, and the action itself will execute only when the user
confirms that dialog window.  These actions are called **parameter actions**.


Or the :class:`DeleteSelected` action is visible in the toolbars of
the grid and the detail windows and in the context menu on a grid row.



- :class:`DeleteSelected`, :class:`SubmitDetail` and
  :class:`SubmitInsert` send an AJAX request which causes something to
  happen on the server.


Read-only actions
=================

.. attribute:: Action.readonly

A read-only action is an action that doesn't cause any change in the current
data object. A read-only action has its :attr:`readonly <Action.readonly>`
attribute set to `True`.

For example the `lino.modlib.printing.DirectPrintAction` action is read-only.
Also :class:`ShowInsert` is read-only because it does not modify the *current*
data object.  Otherwise it would be disabled on a registered invoice.

Setting :attr:`readonly <Action.readonly>` to `False` will (1) disable the
action for `readonly` user types or when :attr:`lino.core.site.Site.readonly` is
True, and (2) will cause it to be logged when :attr:`log_each_action_request
<lino.core.site.Site.log_each_action_request>` is set to `True`.

Note that when a read-only action actually *does* modify the object, Lino won't
"notice" it.

Discussion

Maybe we should change the name :attr:`readonly` to :attr:`modifying` or
:attr:`writing` (and set the default value `False`).  Because that would look
more intuitive for the application developer.  Or --maybe better but probably
with even more consequences-- the default value should be `False`.  Because
being read-only, for actions, is a kind of "privilege": they don't get logged,
they also exist for read-only users...  It would be more "secure" when the
developer must explicitly "say something" in order to grant that privilege.

Another subtlety is the fact that this attribute is used by
:class:`lino.modlib.users.UserAuthored`.  For example the
:class:`StartTicketSession <lino_xl.lib.working.StartTicketSession>` action in
:ref:`noi` is declared :attr:`readonly` because we want Workers who are not
Triagers to see this action even if they are not the author (reporter) of a
ticket.  In this use case the attribute name should rather be
`requires_authorship`.

Action instances
================

A same action instance can be shared by many actors.  For example the
:class:`DeleteSelected` action exists only as one instance shared among all
actors that use it.

Other actions can exist as different instances even on a same actor. For example
the :class:`lino.modlib.printing.DirectPrintAction`.


Instance actions
================

.. glossary::

  instance action

    An action that has been bound to a given :term:`database object`.

A :term:`window action` exists only as long as the Python representation of the
:term:`database object` exists.


The default action of an actor
==============================

Each actor has a **default action**. The default action for :class:`Table
<lino.core.dbtables.Table>` is :class:`ShowTable`. That's why you can define a
menu item by simply naming the table.

For example in the :meth:`setup_menu
<lino.core.plugin.Site.setup_menu>` method in the :ref:`Polls tutorial
<lino.tutorial.polls>`) we say::

    def setup_menu(self, user_type, main):
        super(Site, self).setup_menu(user_type, main)
        m = main.add_menu("polls", "Polls")
        m.add_action('polls.Questions')
        m.add_action('polls.Choices')

(Above snippet is from :file:`lino_book/projects/polls/mysite/settings.py`)

The :meth:`add_action <lino.core.menus.Menu.add_action>` method of
Lino's :class:`lino.core.menus.Menu` is smart enough to understand
that if you specify a Table, you mean in fact that table's default
action.
