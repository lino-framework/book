.. _hosting.preview:

======================
Preview sites
======================

This document explains why and how to set up and use a separate preview site
and manage releases for bigger Lino production sites with many users.  See also
:doc:`/admin/upgrade` for one-step upgrades on smaller sites.  See
:doc:`/dev/datamig` for technical background information.


.. contents::
  :local:

What is a preview site?
=======================

A preview site is a copy of a production site as it would look using
the newest version of Lino.  It is made available to end-users so they
can preview and test their coming version before an upgrade.

The primary goal of such a setup is to help the local Lino community
to discuss about new features and to reduce stress caused by
unexpected results after an upgrade.


General infrastructure
======================

A preview site is implemented as a subdomain with its own project
directory, Python environment and database.

You give your project directories **neutral code names** that are like
"anna", "berta", "claudia"... (not "old", "new", "testlino" or
"prod").

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

Each time the site owner asked for an upgrade, you start by setting up
a new preview site.

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

