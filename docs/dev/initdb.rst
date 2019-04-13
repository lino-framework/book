.. doctest docs/dev/initdb.rst
.. _lino.dev.initdb:

======================
The ``initdb`` command
======================

.. management_command:: initdb

The :manage:`initdb` command is one of Lino's utilities for providing
application-specific demo data.  It performs an initialization of the database,
replacing all data by default data loaded from the specified fixtures.

This command removes *all existing tables* from the database (not only Django
tables), then runs Django's :manage: `migrate` to create all tables, and
finally runs Django's :manage:`loaddata` command to load the specified
fixtures.

For example the command

::

  $ python manage.py initdb std demo demo2

is functionally equivalent to the following plain Django commands::

  $ python manage.py flush
  $ python manage.py migrate
  $ python manage.py loaddata std demo demo2
  
The main difference is that :manage:`initdb` doesn't ask you to type
"yes" followed by :kbd:`RETURN` in order to confirm that you really
want it.  Yes, removing all tables may sound dangerous, but it *is*
actually what we want quite often: when we just want to quickly try
this application, or when we are developing a prototype and made some
changes to the database structure.  We assume that nobody will ever
let a Lino application and some other application share the same
database.

See also the :manage:`prep` command and :doc:`demo_fixtures`.