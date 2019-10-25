.. _getlino.install.contrib:
.. _contrib.install:

=========================================
Setting up a Lino contributor environment
=========================================

We assume you have already :doc:`/dev/install/index`. and that you decided to
extend your developer environment into a :term:`contributor environment`. As a
contributor you have a local clone of the Lino code repositories because you are
going to do local modifications and submit pull requests.


Run getlino to clone Lino repositories
======================================

.. program:: getlino configure

Run :cmd:`getlino configure` with :option:`--clone` and :option:`--devtools`::

  $ getlino configure --clone --devtools

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



Set up a simulated production server
====================================

For testing nginx-specific issues you might want to run a "simulated" production
server that unlike a real production server uses your local repositories but
otherwise runs as a series of real nginx and wsgi and :manage:`linod` processes.

Set shared permissions in your default :term:`virtualenv`::

      $ sudo chown root:www-data .
      $ sudo chmod g+ws .

Otherwise it might happen that nginx compiles a :xfile:``.pyc` file that you
cannot modify afterwards.

Run :cmd:`getlino configure` and :cmd:`getlino startsite` as root (remember
:ref:`getlino.install.prod` for details)::

   $ sudo env PATH=$PATH getlino configure
   $ sudo env PATH=$PATH getlino startsite noi first

Point your browser to http://first.localhost

.. rubric:: Pitfalls

  When using nginx and you want to restart it, you must restart *supervisor*
  (not nginx) because the wsgi process of the site is running there. nginx
  itself usually doesn't need to be restarted.
