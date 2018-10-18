.. _hosting.testing:

======================
Testing sites
======================

This document explains why and how to set up and use a separate
"testing" site and managing releases on bigger Lino production sites
with many users.  See also :doc:`/admin/upgrade` for one-step upgrades
on smaller sites.  See :doc:`/dev/datamig` for technical background
information.


.. contents::
  :local:

What is a testing site?
=======================


A testing site is a copy of a production site as it would look using
the newest version of Lino.  It is made available to end-users so they
can preview and test their coming version before an upgrade.

The primary goal of such a setup is to help the local Lino community
to discuss about new features and to reduce stress caused by
unexpected results after an upgrade.


General infrastructure
======================

A testing site is implemented as a subdomain with its own project
directory, Python environment and database.

You give your project directories **neutral code names** that are like
"anna", "berta", "claudia"... (not "old", "new", "testlino" or
"prod").

Keep all your projects under a common root directory,
e.g. :file:`/usr/local/lino`.

In that directory you have the real project directories ("anna",
"berta", "claudia"), and two symbolic links ``prod`` and ``testing``.

You will have **two vhosts on your web server**, one for production
and one for testing.  Each vhost should refer to their project
directory using the symbolic links so that you can switch easily which
project is being served as which site.


Setting up a testing site
=========================

Each time the site owner asked for an upgrade, you start by setting up
a new testing site.

- Copy the current production project directory to a new directory.

- Remove the :xfile:`env` in the copy and create a new virtualenv.  
  
- Create a file :xfile:`restore2testing.py` in the production snapshot
  as a copy of the :xfile:`restore.py` file.
  
- Run :xfile:`pull.sh`
- Run :xfile:`initdb_from_prod.sh` and adapt
  :xfile:`restore2testing.py` where needed.
- Add a vhost to make the testing site accessible to end-users
- Setup a web page for release notes which serves as a roadmap to you
  and the users.


Synchronizing the testing site
==============================

During the preparation phase you run every night a script that
synchoronizes the testing site, i.e. migrates the production data to
the testing site::

    $ go testing
    $ ./initdb_from_prod.sh
    
Upgrade attempts
================

When you and the users agree that testing seems ready for production,
you announce a date and time for an **upgrade attempt**.

An upgrade attempt lasts an agreed lapse of time (e.g. one hour).

As the hosting provider you make sure that the testing site has been
synchronized from the production site.

During the upgrade attempt users must test whether everything works as
expected.  They must be aware that their changes during this time
might get lost in case they decide to cancel the attempt, and that
they will remain if the attempt succeeds.


Scripts
=======

.. xfile:: restore2testing.py

The file :xfile:`restore2testing.py` is in the :xfile:`snapshot` of
your production project and used by the
:xfile:`initdb_from_prod.sh` script.  You create it as a copy
of the :xfile:`restore.py` file.  You will modify it as needed and
maintain it until the testing site has become production.

.. xfile:: initdb_from_prod.sh

The :xfile:`initdb_from_prod.sh` script creates a snapshot of
production and then restores that snapshot to testing. It also mirrors
media files from prod to testing.
           

.. literalinclude:: initdb_from_prod.sh

