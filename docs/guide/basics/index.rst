.. include:: /shared/include/defs.rst

===========
Lino basics
===========

Not finished. We are working on it.

Entering Lino
=============

Many Lino applications require you to **sign in** using a username and
password.

When you signed into a Lino application, you see the **home screen**.
This includes the :ref:`main menu <main_menu>`, some **welcome
messages**, a series of **quick links** and your :ref:`dashboard
<dashboard>`.

.. _main_menu:

Main menu
=========

The **main menu** is a pull-down menu that you can access in every
Lino window.  Each time you select a command from the main menu, Lino
opens a new window which will be placed over any other open windows.
A window remains open until you close it.  So you have a stack of
windows.

.. _dashboard:

Dashboard
=========

The **dashboard** is a sequence of widgets, usually tables, which
display some data from your database.  Many Lino applications allow
you to configure that dashboard in your *user settings*.

You can edit your **user settings** by selecting :guilabel:`My
settings` from the User menu in the upper right corner.  Some
application also provide a quick link :guilabel:`[My settings]`.

Grid windows
============

Most commands of the main menu open a **grid window**.  A *grid
window* displays some data from your database as a tabular grid where
you can navigate and edit that data.

- Hit :kbd:`Escape` or click the X in the upper right corner of the
  window to close that window and return to the home screen.

- Hit :kbd:`Enter` or **double click** on a row of a grid window opens
  a *detail window* on that row (if that table has a detail view
  defined).
  
- On some cells of a grid you can hit :kbd:`F2` in order to edit that
  cell.

- Note the grid's **toolbar** where you have the quick search field
  and a series of buttons for navigating or running actions.

Detail windows
==============

While a grid window displays multiple rows of some table, a **detail
window** displays one row at a time.


.. _slave_panels:

Slave panels
============

In a detail window you can have **slave panels**.  A slave panel
displays data that is *related* to the current row but stored in a
separate database table.

A slave panel has a special button |eject| in its upper right corner
used to show that slave table in a separate window on its own.  This
is good to know for several reasons:

- If the table's display mode is ``'summary'``, the |eject| button
  is the only way to see that data as a grid.

- The slave panel is meant as a preview, it shows only 15 rows, even
  if there are more.

- The slave panel has no pagination toolbar while the separate window
  does.

Site parameters
===============

 
Many Lino applications have a menu command :menuselection:`Configure
--> System --> Site parameters`, usually available only to system
administrators.
