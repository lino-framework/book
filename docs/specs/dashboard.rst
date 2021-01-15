.. doctest docs/specs/dashboard.rst
.. _specs.dashboard:

======================================
``dashboard`` : customizable dashboard
======================================

.. currentmodule:: lino.modlib.dashboard

The :mod:`lino.modlib.dashboard` plugin adds functionality for letting the users
customize their :term:`dashboard`.

As long as a user didn't populate their dashboard, the list is empty and they
will get all the dashboard items provided by the application.

.. figure:: /specs/noi/dashboard1.png
   :width: 80 %

   Dashboard preferences (empty)

Click the :guilabel:`⚡` button in order to populate the table.


.. figure:: /specs/noi/dashboard2.png
   :width: 80 %

   Dashboard preferences (populated)

Now you can hide individual items and change their order.
