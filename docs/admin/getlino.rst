.. doctest docs/admin/getlino.rst
.. _getlino:

=======================
The ``getlino`` package
=======================

The :mod:`getlino` package greatly helps with installing Lino to your computer.
But it is still work in progress, so use it only for testing purposes. If you
just want to quickly try a Lino, read :doc:`/dev/quick/install`.

To install a production server, you need a Debian machine and a user account
which has permission to run ``sudo``.

You can also use getlino to simply configure a development environment. In that
case you don't need root privileges.


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



The :cmd:`getlino configure` command
====================================

.. program:: getlino configure


You simply run :cmd:`getlino configure` as root::

   $ sudo getlino configure

This will ask you some questions about the general layout of this Lino server.
You can answer ENTER to each of them if your don't care.

On a development server you will probably specify your default work virtual
environment as :option:`--shared-env`.

You can also instruct getlino to not ask any question::

   $ sudo getlino configure --batch

You should use the :option:`--batch` option only when you really know that you want
it (e.g. in a Dockerfile).

Your answers will be stored in the system-wide getlino config file, and the
server will be configured according to your config file.


.. command:: getlino configure

    Configure this machine as a :term:`Lino server`.  This is required before
    you can run :cmd:`startsite`.

    potentially includes
    the installation of system packages and their configuration.

    Create or update a Lino server configuration file and then set up this
    machine to become a Lino production server according to the configuration
    file.

    Options:

    .. option:: --batch

        Run in batch mode, i.e. without asking any questions.
        Assume yes to all questions.

    .. option:: --asroot

        Whether you have root permissions and want to install system packages.

    .. option:: --shared-env

        Full path to your default virtualenv.

    .. option:: --repositories-root PATH

        Full path to your shared repositories root.  This is where getlino
        should clone repositories of packages to be used in editable mode
        ("development version").

        If this is empty and a site requests a development version, this will
        be stored in a directory below the virtualenv dir.

    .. option:: --projects-root

        The root directory for sites on this server.

        This will be added to the :envvar:`PYTHONPATH` of every Lino process
        (namely in :xfile:`manage.py` and :xfile:`wsgi.py`).

        The :envvar:`PYTHONPATH` is needed because the :xfile:`settings.py` of
        a site says ``from lino_local.settings import *``, and the
        :xfile:`manage.py` sets :setting:`DJANGO_SETTINGS_MODULE` to
        ``'lino_local.mysite1.settings'``.


    .. option:: --webdav

        Whether new sites should have webdav.

    .. option:: --env-link

        Name of subdir or link to virtualenv.

    .. option:: --local-prefix

        The local prefix.

    .. option:: --repositories-link

        Name of subdir or link to repositories.

    .. option:: --server-domain NAME

        Fully qualified domain name of this server.  Default is 'localhost'.

    .. option:: --https

        Whether this server provides secure http.

        This option will cause getlino to install certbot.

        When you use this option, you must have your domain name
        (:option:`--server-domain`) registered so that it points to the server.
        If your server has a dynamic IP address, you may use some dynamic DNS
        service like `FreedomBox
        <https://wiki.debian.org/FreedomBox/Manual/DynamicDNS>`__or `dynu.com
        <https://www.dynu.com/DynamicDNS/IPUpdateClient/Linux>`__.


..
  --projects-root TEXT            Base directory for Lino sites
  --local-prefix TEXT             Prefix for for local server-wide importable
                                  packages
  --shared-env TEXT               Directory with shared virtualenv
  --repositories-root TEXT        Base directory for shared code repositories
  --webdav / --no-webdav          Whether to enable webdav on new sites.
  --backups-root TEXT             Base directory for backups
  --log-root TEXT                 Base directory for log files
  --usergroup TEXT                User group for files to be shared with the
                                  web server
  --supervisor-dir TEXT           Directory for supervisor config files
  --db-engine [postgresql|mysql|sqlite3]
                                  Default database engine for new sites.
  --db-port TEXT                  Default database port for new sites.
  --db-host TEXT                  Default database host name for new sites.
  --env-link TEXT                 link to virtualenv (relative to project dir)
  --repos-link TEXT               link to code repositories (relative to
                                  virtualenv)
  --appy / --no-appy              Whether this server provides appypod and
                                  LibreOffice
  --redis / --no-redis            Whether this server provides redis
  --devtools / --no-devtools      Whether this server provides developer tools
                                  (build docs and run tests)
  --server-domain TEXT            Domain name of this server
  --https / --no-https            Whether this server uses secure http
  --monit / --no-monit            Whether this server uses monit
  --admin-name TEXT               The full name of the server administrator
  --admin-email TEXT              The email address of the server
                                  administrator
  --time-zone TEXT                The TIME_ZONE to set on new sites
  --help                          Show this message and exit.





The :cmd:`getlino startsite` command
====================================

.. program:: getlino startsite

Usage::

   $ sudo -H getlino startsite appname prjname [options]

The ``-H`` option instructs :cmd:`sudo` to use your home directory for caching
its downloads.  You will appreciate this when you run the command a second
time.

The script will ask you some questions:

- appname is the Lino application to run

- prjname is the internal name, it must be unique for this Lino server. We
  recommend lower-case only and no "-" or "_", maybe a number.  Examples:  foo,
  foo2, mysite, first,


.. command:: getlino startsite

    Create a new Lino site.

    Usage: getlino startsite [OPTIONS] APPNAME PRJNAME

    Arguments:

    APPNAME : The application to run on the new site.

    SITENAME : The name for the new site.

    .. option:: --batch

        Don't ask anything. Assume yes to all questions.

    .. option:: --asroot

        Whether you have root permissions and want to install system packages.

    .. option:: --dev-repos

        A space-separated list of repositories for which this site uses the
        development version (i.e. not the PyPI release).

        Usage example::

            $ getlino startsite avanti mysite --dev-repos "lino xl"



.. _ss:

The ``startsite`` template
==========================

The `cookiecutter-startsite
<https://github.com/lino-framework/cookiecutter-startsite>`__ project contains
a cookiecutter template used by :cmd:`getlino startsite`.




Notes
=====

When you maintain a Lino server, then you don't want to decide for each new
site which database engine to use. You decide this once for all during
:cmd:`getlino configure`. In general, `apt-get install` is called only during
:cmd:`getlino configure`, never during :cmd:`getlino startsite`. If you have a
server with some mysql sites and exceptionally want to install a site with
postgres, you simply call :cmd:`getlino configure` before calling
:cmd:`getlino startsite`.





Combining getlino and Docker
============================

(needs revision)

The `getlino <https://github.com/lino-framework/getlino>`__ repository contains a
:xfile:`Dockerfile` which you

To create and run the docker image, you need to the run the following command:

docker build -t getlino .

This will create the docker image and use the current getlino.py script (It
will not install getlino from pip servers ) , so be sure the also update your
getlino.py local file.




