=====
Attic
=====

This section contains some older texts that need revision.

Lino directory structure
========================

TODO: review

At the end of this document you will have the following recommenced
directory structure on your Lino production server::

    /usr/local/lino/
    │
    ├── shared/
    │   ├── settings.py   # shared Django settings
    │   ├── master/ # a shared virtualenv named "master"
    │   │   ├── repositories/ # git repositories used by master
    │   │   │   ├─── lino
    │   │   │   ├─── xl
    │   │   │   ├─── noi
    │   │   │   └─── ...
    │   └── ...
    └── lino_local/
        ├── __init__.py
        ├── prj1 # project directory of site "prj1"
        │   ├── __init__.py
        │   ├── settings.py  # Site specific settings
        │   ├── env/ # either a link to some shared virtualenv, or a subdir with a site-specific virtualenv
        │   ├── log/ -> /var/log/lino/prj1/
        │   ├── manage.py
        │   ├── media/
        │   ├── static/
        │   ├── wsgi.py
        │   └── ...
        └── prj2
            ├─── ...
            └─── ...

This structure is recommended even if you have only one Lino site on your server
because you never know whether the :term:`site operator` some day change their
mind and ask e.g. for a :term:`preview site` as well.

It is possible to use symbolic links for the :file:`env` and
:file:`repositories` in order to have several sites working on the same virtual
environment.


Project directories
===================

The following is done automatically by getlino.

Every new project directory must have at least four files:

- an empty :xfile:`__init__.py` file so that Python processes can
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

We recommend the convention of having in each project a symbolic link
named :xfile:`env` which points to the virtualenv.


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




Which database backend to use
=============================

Our example assumes you are using Django's **MySQL** backend.  For
other backends, adapt your :setting:`DATABASES` accordingly.

The database backend of your choice is not automatically installed.
If you plan to use Django's MySQL backend, see :doc:`mysql_install`.

Follow the Django documentation at `Get your database running
<https://docs.djangoproject.com/en/2.2/topics/install/#get-your-database-running>`__




How to install mysql on your site::

    $ sudo apt install mysql-server
    $ sudo apt install libmysqlclient-dev
    $ sudo apt install python-dev
    $ sudo apt install libffi-dev libssl-dev
    $ sudo apt install mysql-server

    $ sudo mysql_secure_installation

.. Install the mysql client into your project's virtualenv::

    $ pip install mysqlclient

  Note that we recommended `mysql-python` before but modified this to
  `mysqlclient` in accordance with `Django
  <https://docs.djangoproject.com/en/2.2/ref/databases/#mysql-db-api-drivers>`__.
