.. _specs.projects.min:

=========================
The Lino Minimal projects
=========================


The demo projects :mod:`lino_book.projects.min1` to :mod:`min9
<lino_book.projects.min9>` are a series of **minimalistic
applications** used by a number of tests and tutorials.

- :mod:`min1` is a minimalistic application for managing your
  contacts.  It uses just the :mod:`contacts <lino_xl.lib.contacts>`
  plugin and its dependencies.  See :doc:`/specs/contacts`.
  
- :mod:`min2` adds calendar functionality. See :doc:`/specs/cal`.
  Some features are:
  
    - Warn about Unconfirmed and Overdue appointments
    - Link calendar entries to your contacts
    - Manage invitations to your events  
    - Manage presences of your guests to your events
    - Export data to `.xlsx` file.
  
  
- :mod:`min3` replaces the single phone, gsm and email fields by
  multiple contact details (the :mod:`phones <lino_xl.lib.phones>`
  plugin)
  
- :mod:`min9` is an attempt to use as many plugins as possible.


