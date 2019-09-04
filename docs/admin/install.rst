.. _lino.admin.install:

====================================================
Installing a Lino application on a production server
====================================================

This page is obsolete.
Read http://getlino.lino-framework.org/ instead.

.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv

Here is a system of files and conventions which we suggest to use when
hosting a Lino production site.  It suits well for having multiple
sites on a same machine.

There are many ways to setup a Django/Lino application. For this guide
we shall be using apache2, mysql, a site-wide Lino settings file, and
a virtual Python environment for each site.


System requirements
===================

.. include:: /include/system_req.rst


System users
============

Before you do anything on your server, create one or several users who
will be the :term:`server administrator`::

    $ sudo adduser joe

Server administrators must be members of the `sudo` and `www-data` groups::

    $ sudo adduser joe sudo
    $ sudo adduser joe www-data

.. rubric:: Notes

- `useradd` is a native binary compiled with the system, while
  `adduser` is a perl script which uses `useradd` in back-end.

All maintainers must have a umask `002` or `007` (not `022` or `077`
as is the default value).

Edit either the file :file:`~/.bashrc` of each user or the file
:file:`/etc/bash.bashrc` (site-wide for all users) and add the following line at
the end::

    umask 002

.. Add one line to your :file:`/etc/apache2/envvars` file::

    umask 002

The umask is used to mask (disable) certain file permissions from
any new file created by a given user. See :doc:`umask` for more
detailed information.



Lino directory structure
========================

At the end of this document you will have the following recommenced
directory structure on your Lino production server::

    /usr/local/lino/
    ├── __init__.py
    ├── lino_local.py # Site-wide settings
    └── prod_sites/
        ├── __init__.py
        ├── prj1 # Site directory
        │   ├── __init__.py
        │   ├── env/ # Virtual environment
        │   │   ├─── bin
        │   │   └─── ...
        │   ├── repositories/ # Lino git-repositories
        │   │   ├─── lino
        │   │   ├─── xl
        │   │   ├─── noi
        │   │   └─── ...
        │   ├── log/ -> /var/log/lino/prj1/
        │   ├── manage.py
        │   ├── media/
        │   ├── settings.py # Site specific settings
        │   ├── static/
        │   ├── wsgi.py
        │   └── ...
        └── prj2
            ├─── ...
                └─── ...

This structure is recommended even if you have only one Lino site on your server
because you never know whether the customer some day change their mind and ask
e.g. for a :term:`preview site` as well.

It is possible to use symbolic links for the :file:`env` and
:file:`repositories` in order to have several sites working on the same virtual
environment.


Some useful additions to your shell
===================================

Add the following to your system-wide :file:`/etc/bash.bashrc`:

.. literalinclude:: bash_aliases

If you want :ref:`log2syslog`, then add also this:

.. literalinclude:: log2syslog

After these changes you must close and reopen your terminal to
activate them. You can now do the following to quickly cd to a project
directory and activate its Python environment::

  $ go prj1
  $ a

Project directories
===================

Every new project directory must have at least four files:

- an empty :xfile:`__init__.py` file making it able for apache to
  import your settings::

    $ touch /usr/local/src/lino/prod_sites/prj1/__init__.py

- a file :xfile:`settings.py` **Note:** Replace the 'prj1' in this
  file with the name of the project:

    .. literalinclude:: mypy/prj1/settings.py

- a file :xfile:`manage.py`:

    .. literalinclude:: mypy/prj1/manage.py

- a file :xfile:`wsgi.py`. **Note:** Replace the 'prj1' in this file
  with the name of the project:

    .. literalinclude:: mypy/prj1/wsgi.py



.. Note that :xfile:`manage.py` and :xfile:`wsgi.py` have the same content for every
   project. Once you have a first project running, you can add new
   projects by copying the directory of some existing project.

We recommend the convention of having in each project a symbolic link
named :xfile:`env` which points to the virtualenv.


Which database backend to use
=============================

Our example assumes you are using Django's **MySQL** backend.  For
other backends, adapt your :setting:`DATABASES` accordingly.

The database backend of your choice is not automatically installed.
If you plan to use Django's MySQL backend, see :doc:`mysql_install`.

Follow the Django documentation at `Get your database running
<https://docs.djangoproject.com/en/2.2/topics/install/#get-your-database-running>`__


Initialize the database
=======================

::
     $ go prj1
     $ python manage.py prep


Collecting static files
=======================

Create two empty directories :xfile:`media` and :xfile:`config`::

    $ mkdir media
    $ mkdir config

.. .(Needs revision)

One part of your cache directory are the static files.  When your
:envvar:`LINO_CACHE_ROOT` is set, you should run Django's
:manage:`collectstatic` command::

    $ cd /usr/local/src/lino/prod_sites/prj1/
    $ python manage.py collectstatic

The output should be something like this::

    You have requested to collect static files at the destination
    location as specified in your settings:

        /usr/local/src/lino/prod_sites/prj1/static/

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes

    4688 static files copied to '/usr/local/src/lino/prod_sites/prj1/static/', 0 unmodified.


..  Note that you can chose an arbitrary project directory (any subdir
    below :mod:`lino_book.projects` should do it) for running
    :manage:`collectstatic`, it does not need to be :mod:`polly
    <lino_book.projects.polly>`. That's because all Lino applications have
    the same set of staticfiles.

.. You need to do this only for your first local Lino project because
   static files are the same for every Lino application.  (There are
   exceptions to this rule, but we can ignore them for the moment.)



From here
=========

From here you may edit your :xfile:`settings.py` file to import a different
settings module from another repo.

Return to the index for more information :doc:`mysql_install`.
