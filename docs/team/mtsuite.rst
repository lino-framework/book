.. _team.mt:

===============================================
The manual testing suite for the Lino framework
===============================================

This documents contains instructions for a Lino :term:`contributing developer`
who is responsible for :term:`manual testing` of the framework.

It assumes that you have installed a contributor environment as described in
:doc:`/team/install/index`.

Run :manage:`runserver` in the :mod:`lino_book.projects.min9` demo project and
sign in as robin.


.. _team.mt.addresses:

Multiple addresses
========================================

Here are some tests for the :mod:`lino_xl.lib.addresses` plugin.

For each of the following items, open the `Manage addresses` window, do what the
items says, then close the window and check that the partner's :attr:`overview`
field has been updated correctly:

- edit the primary address (the partner's address should change accordingly)

- make another address primary (the partner's address should change accordingly)

- edit a non-primary address (should *not* update the partner)

- uncheck the primary checkbox of the primary address (so that there is no
  primary address, which means that the partner's address should become empty)

Directly edit the address fields of a partner. The primary address should get
updated accordingly.
