.. _specs.office:

====================================
``office`` : Adding an "Office" menu
====================================

.. currentmodule:: lino_xl.lib.office

The :mod:`lino.modlib.office` plugin is just a menu hook for several other
plugins.  It also defines some `user roles`_ shared by these plugins.

Here is a list of plugins that consider themselves office stuff:

- :doc:`cal`
- :doc:`contacts`
- :doc:`human`
- :doc:`countries`
- :doc:`notes`
- :doc:`printing`
- :doc:`phones`
- :doc:`excerpts`
- :doc:`printing`
- :doc:`weasyprint`
- :doc:`uploads`
- :doc:`holidays`

User roles
==========

.. class:: OfficeUser

    Has access to office functionality like calendar, notes and
    uploads.


.. class:: OfficeOperator

    Can manage office functionality for other users (but not for
    himself).

    An office operator can create their own notes and uploads, but no
    calendar entries.

    For example the `lino_xl.lib.cal.OverdueAppointments` table
    requires :class:`OfficeStaff` and is *not* available for
    :class:`OfficeOperator`.


.. class:: OfficeStaff

    Can manage configuration of office functionality.



