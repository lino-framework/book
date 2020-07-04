.. _getlino.install.contrib:
.. _contrib.install:

=========================================
Setting up a Lino contributor environment
=========================================

We assume you have already :doc:`/dev/install/index` and that you decided to
extend your developer environment into a :term:`contributor environment`. As a
contributor you have a local clone of the Lino code repositories because you are
going to do local modifications and submit pull requests.


Run getlino to clone Lino repositories
======================================

Run :cmd:`getlino` with the following options::

  $ getlino configure --clone --devtools --redis

For details see the documentation about :ref:`getlino`.

Note that getlino uses the configuration values you specified during
:doc:`/dev/install/index`.

Try one of the demo projects::

  $ cd ~/lino/env/repositories/book/lino_book/projects/team
  $ python manage.py prep
  $ python manage.py runserver

Point your browser to http://localhost:8000

Note that :manage:`prep` is needed only once per demo project in order to create
the database.


Running your first Lino site
============================

You can now ``cd`` to any subdir of :mod:`lino_book.projects` and run
a development server.  Before starting a web server on a project for
the first time, you must initialize its database using the
:manage:`prep` command::

    $ cd ~/repositories/book/lino_book/projects/min1
    $ python manage.py prep
    $ python manage.py runserver


Exercises
=========

#.  Sign in and play around.

#.  Create some persons and organizations. Don't enter lots of data
    because we are going to throw it away soon.
