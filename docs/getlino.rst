.. _getlino:

=======================
The ``getlino`` package
=======================

The :mod:`getlino` package is still work in progress, so use it only for
testing purposes. When finished, it will help to install Lino to your computer.

If you just want to quickly try a Lino, read :doc:`/dev/quick/install`.


Configure a virgin Debian system as a Lino production server
============================================================

Get root permissions, install getlino into the system-wide Python, then run
:cmd:`getlino configure`::

   $ sudo pip3 install getlino
   $ sudo getlino configure

This will ask you some questions about the general layout of this Lino server.
You can answer ENTER if your don't care. You can also instruct getlino to not
ask any question::

   $ sudo getlino configure --batch

Your answers will be stored in the system-wide getlino config file, and the
server will be configured according to your config file.

Now install a first site (this time you don't need to be root anymore)::

   $ getlino startsite appname prjname [options]

The script will ask you some questions:

- appname is the Lino application to run

- prjname is the internal name, it must be unique for this Lino server. We
  recommend lower-case only and no "-" or "_", maybe a number.  Examples:  foo,
  foo2, mysite, first,




Install a Lino development environment
======================================

Install getlino into your default Python environment, then run :cmd:`getlino
setup`::

   $ . path/to/virtualenv/bin/activate
   $ sudo pip3 install getlino
   $ sudo getlino configure




Combining getlino and Docker
============================



The `getlino <https://github.com/lino-framework/getlino>`__ repository contains a
:xfile:`Dockerfile` which you

To create and run the docker image, you need to the run the following command:

docker build -t getlino .

This will create the docker image and use the current getlino.py script (It
will not install getlino from pip servers ) , so be sure the also update your
getlino.py local file.



.. command:: getlino configure

::

    Usage: getlino.py configure [OPTIONS]

          Edit and/or create a configuration file and     set up this machine to
          become a Lino production server     according to the configuration
          file.

    Options:
      --batch / --no-batch            Whether to run in batch mode, i.e. without
                                      asking any questions.  Don't use this on a
                                      machine that is already being used.
      --projects-root TEXT            Base directory for Lino sites
      --backups-root TEXT             Base directory for backups
      --log-root TEXT                 Base directory for log files
      --usergroup TEXT                User group for files to be shared with the
                                      web server
      --supervisor-dir TEXT           Directory for supervisor config files
      --db-engine [pgsql|mysql|sqlite]
                                      Default database engine for new sites.
      --env-dir TEXT                  Default virtualenv directory for new sites
      --repos-dir TEXT                Default repositories directory for new sites
      --appy / --no-appy              Whether this server provides appypod and
                                      LibreOffice
      --redis / --no-redis            Whether this server provides redis
      --devtools / --no-devtools      Whether this server provides developer tools
                                      (build docs and run tests)
      --admin-name TEXT               The full name of the server maintainer
      --admin-email TEXT              The email address of the server maintainer
      --help                          Show this message and exit.


.. command:: getlino startsite

::

    Usage: getlino.py startsite [OPTIONS] APPNAME PRJNAME

      Create a new Lino site.

      Arguments:

      APPNAME : The application to run on the new site.

      PRJNAME : The project name for the new site.

    Options:
      --batch / --no-batch  Whether to run in batch mode, i.e. without asking any
                            questions.  Don't use this on a machine that is
                            already being used.
      --dev / --no-dev      Whether to use development version of the application
      --server_url TEXT     The URL where this site is published
      --help                Show this message and exit.
