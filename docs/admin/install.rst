.. _lino.admin.install:

====================================================
Installing a Lino application on a production server
====================================================

Here is a system of files and conventions which we suggest to use when
hosting a Lino production site.  It suits well for having multiple
sites on a same machine.

Prerequisites
=============

You need shell access to a Linux box, i.e. a virtual or physical
machine with a Linux operating system.

If your customers want want to access their Lino from outside of their
intranet, then you need to setup a public domain or subdomain and
configure Apache to use secure HTTP.

We recommend a **stable Debian** as operating system.  If you prefer
some other Linux distribution, that should be no problem. There will
be some differences, but you probably know them.

You need a **web server**, **Python 2**, some database
(e.g. **MySQL**) running on that server.


Debian packages
===============

Some Debian packages and why you might need them:

libapache2-mod-wsgi
  
    This will automatically install Apache 
    (packages apache2 apache2-doc apache2-mpm-prefork libexpat1...)
    
mysqldb-server
mariadb-server

    Needed if you plan to use Django's MySQL backend.
    See :doc:`install_mysql`.

ssl-cert
    
    If you want to run a https server.

.. _lino.admin.site_module:

    
Configuring site-wide default settings
======================================

Lino applications (unlike Django projects) have a hook for specifying
site-wide default values for their Django settings.

As root, create a directory :file:`/usr/local/src/lino` containing an
empty :xfile:`__init__.py` file::

  $ sudo mkdir /usr/local/src/lino
  $ sudo touch /usr/local/src/lino/__init__.py

In that directory, still as root, create a file named
:file:`lino_local.py`::
  
  $ sudo nano /usr/local/src/lino/lino_local.py

Paste the following content into that file:

.. literalinclude:: mypy/lino_local.py

Adapt that content to your site.

This will be your :xfile:`lino_local.py` file.

More about this in :ref:`lino.site_module`.


Users and projects
==================

When hosting Lino projects, you may

- create a new Linux user for every project
- define a single user who manages multiple projects
- use a mixture of both

Every user should create a directory which will be the root for all
Lino projects.  We suggest to call it :file:`~/mypy`.  So our project
directories will be :file:`~/mypy/prj1`, :file:`~/mypy/prj2` etc.

Project directories
===================

Every new project directory must have at least three files:

- a file :xfile:`settings.py`:

  .. literalinclude:: mypy/prj1/settings.py
                      
- a file :xfile:`manage.py`:

  .. literalinclude:: mypy/prj1/manage.py

- a file :xfile:`wsgi.py` :

  .. literalinclude:: mypy/prj1/wsgi.py

Note that :xfile:`manage.py` and :xfile:`wsgi.py` have the same
content for every project. Once you have a first project running, you
can add new projects by copying the directory of some existing
project.

Which database backend to use
=============================

Our example assumes you are using Django's **MySQL** backend.  For
other backends, adapt your :setting:`DATABASES` accordingly.

The database backend of your choice is not automatically installed.
If you plan to use Django's MySQL backend, see :doc:`install_mysql`.

Follow the Django documentation at `Get your database running
<https://docs.djangoproject.com/en/1.9/topics/install/#get-your-database-running>`__


Create a virtualenv
===================

Create the virtualenv for the project::

    $ cd ~/mypy/prj1
    $ virtualenv env
    $ a env/bin/activate
    $ pip install lino-voga

Above example assumes that you want to run :ref:`voga` on that site.
Of course you have other choices, for example:

    - `lino-voga` for :ref:`voga`
    - `lino-cosi` for :ref:`cosi`
    - `lino-noi` for :ref:`noi`  or :ref:`care`
    - `lino-presto` for :ref:`presto` or :ref:`psico`
    - `lino-welfare` for :ref:`welfare`

And of course you must then write your :xfile:`settings.py` as
documented by these projects.

We recommend the convention of having in each project a subdirectory
named :xfile:`env` which contains the virtualenv. On systems with
shared virtualenvs,  :xfile:`env`  might be a symbolic link.


Activate file logging
=====================

To activate logging to a file, you simply add a symbolic link named
:xfile:`log` which points to the actual location::

  $ ln -s /vat/log/lino/prj1 log
 
Create two empty directores :xfile:`media` and :xfile:`config`::

  $ mkdir media
  $ mkdir config

 

Collecting static files
=======================

(Needs revision)

One part of your cache directory are the static files.  When your
:envvar:`LINO_CACHE_ROOT` is set, you should run Django's
:manage:`collectstatic` command::

    $ cd ~/repositories/book/lino_book/projects/polly
    $ python manage.py collectstatic

The output should be something like this::

    You have requested to collect static files at the destination
    location as specified in your settings:

        /home/myname/virtualenvs/a/lino_cache/collectstatic

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes

    4688 static files copied to '/home/myname/virtualenvs/a/lino_cache/collectstatic', 0 unmodified.

Note that you can chose an arbitrary project directory (any subdir
below :mod:`lino_book.projects` should do it) for running
:manage:`collectstatic`, it does not need to be :mod:`polly
<lino_book.projects.polly>`. That's because all Lino applications have
the same set of staticfiles.

You need to do this only for your first local Lino project because
static files are the same for every Lino application.  (There are
exceptions to this rule, but we can ignore them for the moment.)
  
 
  
Install TinyMCE language packs
==============================

(Needs revision)

If you plan to use Lino in other languages than English, you must 
manually install language packs for TinyMCE from
http://tinymce.moxiecode.com/i18n/index.php?ctrl=lang&act=download&pr_id=1

Simplified instructions for a language pack containing 
my personal selection (de, fr, nl and et)::

  # cd /usr/share/tinymce/www
  # wget http://tim.saffre-rumma.net/dl/tmp/tinymce_language_pack.zip
  # unzip tinymce_language_pack.zip
  
  
