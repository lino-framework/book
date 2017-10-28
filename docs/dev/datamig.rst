.. _lino.datamig:

=========================
Data migrations à la Lino
=========================

Overview
========

Data migration is a complex topic. Django needed until version 1.7
before they dared to suggest a default method to automating these
tasks (see `Migrations
<https://docs.djangoproject.com/en/1.11/topics/migrations/>`_).

Lino includes a system for managing database migrations which takes a
rather different approach than what Django does.

Advantages of Lino migrations:

- They help making the whole process of developing applications (which
  includes testing, maintaining and documenting) more natural and
  easier to manage.

- They work also when you use the :doc:`inject_field` and :ref:`mldbc`
  features.

Lino suggests to *not use* Django migrations. At least if you want to
use either the :doc:`inject_field <inject_field>` or :ref:`BabelField
<mldbc>` features. If your application uses them (or if it uses a
plugin which uses them), then Django migrations won't work.

You might still want to use the Django approach because Lino
migrations have one inevitable **disadvantage**: they are slower than
:manage:`migrate`. Users must stop working in your application during
that time.  There are systems where half an hour downtime for an
upgrade is not acceptable.

If you *do* need to use Django migrations in your Lino application,
then you cannot use :doc:`inject_field <inject_field>` and
:ref:`BabelField <mldbc>`.


General strategy for handling data migrations
=============================================

The basic idea is that you :doc:`write a Python dump </dev/dump2py>`
with the old version (*before* upgrading), and that you load that dump
with the new version (*after* upgrading).

- When you upgrade on a production site, always make a Python dump
  (using :manage:`dump2py`) of your database **before** the upgrade.

- **After** the upgrade, reinitialize your database from that dump by
  running the :xfile:`restore.py` script.

Certain schema changes will migrate automatically: new models, new
fields (when they have a default value), `unique` constraints, ...

If there were unhandled schema changes, you will get error messages.
This is no reason to panic. Just change your code and try again.  You
can run the :xfile:`restore.py` script as often as needed until there
are no more errors.

There are two ways for correcting your code: either by locally
modifying your :xfile:`restore.py` script or by writing a migrator.


Modifying :xfile:`restore.py` script
====================================

Locally modifying a :xfile:`restore.py` script is the natural way when
there is only one production site who needs to be migrated. It is a
common situation when a new customer project has gone into production
but is being used only on that customer's site.

Look at the code of your :xfile:`restore.py` script.

For example if a model or field has been removed, you can just comment
out one line in that script.

See also :doc:`dump2py`.


Writing a migrator
==================

(Not finished)

- Increase your version number
- 

