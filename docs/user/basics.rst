===========
Lino basics
===========

Not finished. We are working on it.

Many Lino applications require you to **sign in** using a username and
password.

When you signed into a Lino application, you see the **home screen**.
This includes the **main menu**, some **welcome messages**, a series
of **quick links** and your **dashboard**.

The **dashboard** is a sequence of widgets, usually tables, which
display some data from your database.  Many Lino applications allow
you to configure that dashboard in your *user settings*.

You can edit your **user settings** by selecting :guilabel:`My
settings` from the User menu in the upper right corner.  Some
application also provide a quick link :guilabel:`[My settings]`.

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

While a grid window displays all the rows of some table, a **detail
window** displays one row at a time.

 
Many Lino applications have a menu command :menuselection:`Configure
--> System --> Site parameters`, usually available only to system
administrators.
