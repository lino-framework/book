.. _getlino:

=======================
The ``getlino`` package
=======================

The :mod:`getlino` package greatly helps with installing Lino to your computer.
But it is still work in progress, so use it only for testing purposes.

If you just want to quickly try a Lino, read :doc:`/dev/quick/install`.

Installing getlino
==================

You must install getlino into the system-wide Python::

   $ sudo pip3 install getlino

You might prefer the development version::

   $ sudo pip3 install -e git+https://github.com/lino-framework/getlino.git#egg=getlino

Or, if you have installed a development environment, you can install your own
local clone::

   $ cd ~/repositories
   $ git clone git@github.com:lino-framework/getlino.git
   $ sudo pip3 install -e getlino


Turn a virgin Debian system into a Lino production server
=========================================================

You simply run :cmd:`getlino configure` as root::

   $ sudo getlino.py configure

This will ask you some questions about the general layout of this Lino server.
You can answer ENTER to each of them if your don't care.

You can also instruct getlino to not ask any question::

   $ sudo getlino.py configure --batch

But please use the ``--batch`` option only when you really know that you want
it (e.g. in a Dockerfile).

Your answers will be stored in the system-wide getlino config file, and the
server will be configured according to your config file.

Now install a first site::

   $ sudo -H getlino.py startsite appname prjname [options]

The ``-H`` option instructs :cmd:`sudo` to use your home directory for caching
its downloads.  You will appreciate this when you run the command a second
time.

The script will ask you some questions:

- appname is the Lino application to run

- prjname is the internal name, it must be unique for this Lino server. We
  recommend lower-case only and no "-" or "_", maybe a number.  Examples:  foo,
  foo2, mysite, first,

Notes
=====

When you maintain a Lino server, then you don't want to decide for each new
site which database engine to use. You decide this once for all during
:cmd:`getlino configure`. In general, `apt-get install` is called only during
:cmd:`getlino configure`, never during :cmd:`getlino startsite`. If you have a
server with some mysql sites and exceptionally want to install a site with
postgres, you simply call :cmd:`getlino configure` before calling
:cmd:`getlino startsite`.


Install a Lino development environment
======================================

Install getlino into your default Python environment, then run :cmd:`getlino
configure`::

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
      --admin-name TEXT               The full name of the server administrator
      --admin-email TEXT              The email address of the server administrator
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


.. _ss:

The ``startsite`` template
==========================

The `cookiecutter-startsite
<https://github.com/lino-framework/cookiecutter-startsite>`__ project contains
a cookiecutter template used by :cmd:`getlino startsite`.