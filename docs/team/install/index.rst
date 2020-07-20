.. _getlino.install.contrib:
.. _contrib.install:

=========================================
Setting up a Lino contributor environment
=========================================

We assume you have already :doc:`installed a developer environment
</dev/install/index>` and that you now want to extend your it into a
:term:`contributor environment`.

The main new thing is that as a contributor you have a local clone of the Lino
code repositories because you are going to do local modifications and submit
pull requests.  Getlino does the tedious work of cloning and installing them
into your virtualenv as editable (with `pip install -e`).

Run getlino to clone Lino repositories
======================================

Run :cmd:`getlino` with the following options::

  $ getlino configure --clone --devtools --redis

For details see the documentation about :ref:`getlino`.

TODO: This won't uninstall Lino packages that were previously installed from
PyPI in non-editable mode (when you were still a developer environment). So you
must probably pip uninstall them manually.

Note that getlino overrides only the configuration values you specified at the
command line, otherwise it uses those you specified during
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
