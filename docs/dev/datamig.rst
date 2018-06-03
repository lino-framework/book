.. _lino.datamig:

=========================
Data migrations à la Lino
=========================

As the maintainer of a database application that is being used on one
or several production sites you must care about how these production
sites will migrate their data.

Data migration is a complex topic. Django needed until version 1.7
before they adapted a default method to automating these tasks (see
`Migrations
<https://docs.djangoproject.com/en/1.11/topics/migrations/>`_).

Lino suggests to use :doc:`Python dumps <dump2py>` as a different
approach for doing database migrations.

Advantages of Lino migrations:

- They make the process of deploying applications and upgrading
  production sites simpler and more transparent.  As the responsible
  adminstrator of a Lino production site, you will simply :doc:`write
  a Python dump </dev/dump2py>` *before* upgrading (using the old
  version), and then load that dump *after* upgrading (with the new
  version). See :doc:`/admin/upgrade` for details.

- They work also when you use Lino's :doc:`inject_field
  <inject_field>` or :ref:`BabelField <mldbc>` features.

- They can help in situations where you would need a magician. For
  example your users accidentally deleted a bunch of data from their
  database and they don't have a recent backup.
  See :doc:`repair` for an example.

Despite these advantages you might still want to use the Django
approach because Lino migrations have one inevitable **disadvantage**:
they are slower than :manage:`migrate`. Users must stop working in
your application during that time.  There are systems where half an
hour downtime for an upgrade is not acceptable.  Rule of thumb: If
your application uses either the :doc:`inject_field <inject_field>` or
:ref:`BabelField <mldbc>` features (or if it uses a plugin which uses
them), then Django migrations won't work.  If your site *does* need to
use Django migrations, then you cannot use :doc:`inject_field
<inject_field>` and :ref:`BabelField <mldbc>`.


General strategy for managing data migrations
=============================================

There are two ways for managing data migrations: either by locally
modifying the :xfile:`restore.py` script or by writing a migrator.


Locally modifying the :xfile:`restore.py` script
------------------------------------------------

Locally modifying a :xfile:`restore.py` script is the natural way when
there is only one production site that needs to migrate and when the
application maintainer is also the site administrator. It is a common
situation when a new customer project has gone into production but is
being used only on that customer's site.

Certain schema changes will migrate automatically: new models, new
fields (when they have a default value), `unique` constraints, ...

If there were unhandled schema changes, you will get error messages
during the restore.  And then you can just change the
:xfile:`restore.py` script and try again.  You can run the
:xfile:`restore.py` script as often as needed until there are no more
errors.

The code of the :xfile:`restore.py` script is optimized for easily
applying most database schema changes.  For example if a model or
field has been removed, you can just comment out one line in that
script.

TODO: write detailed docs


Writing a migrator
------------------

When your application runs on more than one production site, you will
prefer writing a migrator.

TODO: write detailed docs


