.. _hosting.preview:

======================
Preview sites
======================

This document explains why and how to set up and use a separate :term:`preview
site` to manage releases on bigger Lino :term:`production sites <production
site>`.  See also :doc:`/admin/upgrade` for one-step upgrades on smaller sites.
See :doc:`/dev/datamig` for technical background information.


.. contents::
  :local:


General infrastructure
======================

A preview site is a separate :term:`Lino site` with its own subdomain, its own
project directory, Python environment and database. But that data is just a
mirror of another site, usually the :term:`production site`.

A same :term:`site operator` will have a a series of sites, one in "production"
state and maybe another in "preview" state.  Every site has its "life cycle" :
it typically starts as a "preview" site, then becomes the "production" site, and
maybe afterwards remains alive for some time as the "old" site.

Remember that virtual environments cannot change their name. So please give your
project directories neutral names like "mdg1", "mdg2", "mdg3". **Do not** call
them not "preview", "old", "new", "testing" or "prod".

..

  Keep all your projects under a common root directory,
  e.g. :file:`/usr/local/lino`.

  In that directory you have the real project directories ("anna",
  "berta", "claudia"), and two symbolic links ``prod`` and ``preview``.

  You will have **two vhosts on your web server**, one for production
  and one for preview.  Each vhost should refer to their project
  directory using the symbolic links so that you can switch easily which
  project is being served as which site.


Setting up a preview site
=========================

When the :term:`site operator` asks for an upgrade, you start by setting up a
new preview site.

- Copy the current production project directory to a new directory::

    $ df -h
    $ cp -a afoo bfoo

- In the afoo directory run::

    $ python manage.py dump2py snapshot2preview

  Create a file :xfile:`restore2preview.py` in the production snapshot
  as a copy of the :xfile:`restore.py` file.

- In the bfoo directory:

- Let the :xfile:`log` directory point to a different directory::

      $ rm log
      $ mkdir /var/log/lino/bfoo
      $ ln -s /var/log/lino/bfoo log

- Have a deep look at all the following files in the preview project
  and replace afoo with bfoo where needed:

  :xfile:`settings.py`,
  :xfile:`manage.py`
  :xfile:`wsgi.py`
  :xfile:`pull.sh`
  :xfile:`make_snapshot.sh`
  :xfile:`initdb_from_prod.sh`
  etc

- Remove the :xfile:`env` directory in the copy and create a new
  one with virtualenv.  Activate the new env.
  Run pull.sh to update repositories.
  Install Lino from repositories.

- Create the new database in mysql or pg

- Run :xfile:`pull.sh`

- Run collectstatic

- Run :xfile:`initdb_from_prod.sh` and adapt
  :xfile:`restore2preview.py` where needed.
- Add a vhost to make the preview site accessible to end-users
- Setup a web page for release notes which serves as a roadmap to you
  and the users.


Synchronizing the preview site
==============================

During the preparation phase you run every night a script that
synchoronizes the preview site, i.e. migrates the production data to
the preview site::

    $ go preview
    $ ./initdb_from_prod.sh

Upgrade attempts
================

When you and the users agree that preview seems ready for production,
you announce a date and time for an **upgrade attempt**.

An upgrade attempt lasts an agreed lapse of time (e.g. one hour).

As the hosting provider you make sure that the preview site has been
synchronized from the production site.

During the upgrade attempt users must test whether everything works as
expected.  They must be aware that their changes during this time
might get lost in case they decide to cancel the attempt, and that
they will remain if the attempt succeeds.


Scripts
=======

.. xfile:: restore2preview.py

The file :xfile:`restore2preview.py` is in the :xfile:`snapshot` of
your production project and used by the
:xfile:`initdb_from_prod.sh` script.  You create it as a copy
of the :xfile:`restore.py` file.  You will modify it as needed and
maintain it until the preview site has become production.

.. xfile:: initdb_from_prod.sh

The :xfile:`initdb_from_prod.sh` script creates a snapshot of
production and then restores that snapshot to preview. It also mirrors
media files from prod to preview.


.. literalinclude:: initdb_from_prod.sh



Troubleshooting
===============

- rsync: failed to set times on "...": Operation not permitted (1)

  rsync tries to change the timestamps of directories because that helps
  detecting changes.  But that doesn't work when the file owner is different
  from the user who runs the migration script. Because it's not allowed to
  change the timestamp of a file you don't own, even when you have write
  permission. --> That's why we use the ``--omit-dir-times`` option.
