.. _lino.admin.install:

====================================================
Installing a Lino application on a production server
====================================================

.. _pip: http://www.pip-installer.org/en/latest/
.. _virtualenv: https://pypi.python.org/pypi/virtualenv

Here is a system of files and conventions which we suggest to use when
hosting a Lino production site.  It suits well for having multiple
sites on a same machine.

There are many ways to setup a Django/Lino application. For this guide
we shall be using apache2, mysql, a site-wide Lino settings file, and
a virtual Python environment for each site.


Prerequisites
=============

You need shell access to a **Linux server**, i.e. a virtual or
physical machine with a Linux operating system running in a network.

We recommend a **stable Debian** as operating system.  If you prefer
some other Linux distribution, that should be no problem. There will
be some differences, but you probably know them.  You need a **web
server**, **Python 2**, some database (e.g. **MySQL** or
**PostGreSQL**) running on that server.

If your customers want to access their Lino from outside of their
intranet, then you need to setup a **domain name** and configure
Apache to use secure HTTP.


System requirements
===================

.. include:: /include/system_req.rst


System users
============

Before you do anything on your server, create one or several users who
will be the *maintainers* of this site::

    $ sudo adduser joe

Maintainers must be members of the `sudo` and `www-data` groups::
  
    $ sudo adduser joe sudo
    $ sudo adduser joe www-data

.. rubric:: Notes

- `useradd` is a native binary compiled with the system, while
  `adduser` is a perl script which uses `useradd` in back-end.

All maintainers must have a umask `002` or `007` (not `022` or `077`
as is the default value). Edit either the file :file:`~/.bashrc` of
each user or the file :file:`/etc/bash.bashrc` (site-wide for all
users) and add the following line at the end::

    umask 002
 
.. rubric:: Notes
            
- The umask is used to mask (disable) certain file permissions from
  any new file created by a given user. See :doc:`umask` for more
  detailed information.
  

Lino directory structure
========================

At the end of this document you will have the following recommenced
directory structure on your Lino production server::

    /usr/local/src/
    └── lino
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

This structure is recommended even if you have only one Lino site on
your server because you never know whether the customer some day
change their mind and ask e.g. for a test site as well.

It is possible to use symbolic links for the :file:`env` and
:file:`repositories` in order to have several sites working on the
same virtual environment.

.. However please note, if you choose the use the example
   configuration files contained in this guide. Ensure that the above
   directory structure is maintained.


Create a project directory
==========================

First create the main :file:`prod_sites` folder::

    $ sudo mkdir -p /usr/local/src/lino/prod_sites/
    $ cd /usr/local/src/lino/prod_sites/

Create the project folder for your first site, in this example we
shall use :file:`prj1`::

    $ mkdir prj1
    $ cd prj1


Set up a Python environment
===========================

Create a new Python environment in you project directory::

        $ sudo apt install virtualenv
        $ virtualenv --python=python2 env

*Activate* this environment by typing::

        $ . env/bin/activate

Afterwards update the new environment's pip and setuptools to the
latest version::

        $ pip install -U pip
        $ pip install -U setuptools
    

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
  

    
Get the sources
===============

Create a directory :file:`repositories` to hold your working copies of
version-controlled software projects and then clone these projects.

  $ go prj1
  $ mkdir repositories
  $ cd repositories
  $ git clone https://github.com/lino-framework/lino.git
  $ git clone https://github.com/lino-framework/xl.git
  $ git clone https://github.com/lino-framework/MYAPP.git

Replace ``MYAPP`` by the name of the Lino application
you want to install.

The `lino` repository contains general Lino core code.  The `xl`
repository contains the :ref:`Lino extension library <xl>` used by
most Lino applications.

Now you are ready to "install" Lino, i.e. to tell your Python
environment where the source file are, so that you can import them
from within any Python program::

  $ pip install -e lino
  $ pip install -e xl
  $ pip install -e MYAPP


More Debian packages
====================

Some Debian packages and why you might need them::

    $ sudo apt-get install apache2 libapache2-mod-wsgi

This will automatically install Apache 
(packages apache2 apache2-doc apache2-mpm-prefork libexpat1...)

Select your database backend::

    $ sudo apt install mysql-server

Install the python dependencies::

    $ sudo apt install libmysqlclient-dev
    $ sudo apt install python-dev
    $ sudo apt install libffi-dev libssl-dev
    $ pip install mysqlclient

For more info on how to setup a user and database see
:doc:`mysql_install`.

.. _lino.admin.site_module:

    
Configuring site-wide default settings
======================================

Lino applications (unlike Django projects) have a hook for specifying
site-wide default values for their Django settings.

As root, in your :file:`/usr/local/src/lino` the directory create a
empty :xfile:`__init__.py` file::

  $ sudo touch /usr/local/src/lino/__init__.py

In that directory, create our :file:`lino_local.py` file that contains
the site-wide configuration::
  
  $ sudo nano /usr/local/src/lino/lino_local.py

Paste the following content into that file:

.. literalinclude:: mypy/lino_local.py

Adapt that content to your site.

This will be your :xfile:`lino_local.py` file.

More about this in :ref:`lino.site_module`.


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
<https://docs.djangoproject.com/en/1.9/topics/install/#get-your-database-running>`__



Activate file logging
=====================

To activate logging to a file, you simply add a symbolic link named
:xfile:`log` which points to the actual location::

    $ sudo mkdir -p /var/log/lino/
    $ sudo chown :www-data /var/log/lino/
    $ sudo chmod g+ws /var/log/lino/
    $ sudo mkdir /var/log/lino/prj1/
    $ cd ~/mypy/prj1/
    $ ln -s /var/log/lino/prj1/ log/

Create two empty directories :xfile:`media` and :xfile:`config`::

    $ mkdir media
    $ mkdir config


Initialize the database
=======================

::
     $ go prj1
     $ python manage.py prep

     
Collecting static files
=======================

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


Setting up Apache2
==================

The following is an example of a apache config for our :file:`prj1`
site.

This example is setup for a single Lino site, if you plan to host more
than one Lino site we advise you to move your static files to
:file:`/usr/local/src/lino/static/` and to update the config
accordingly.


  .. literalinclude:: mypy/prj1/apache2/apache.conf

Do the following in order to activate the site with Apache::

    $ sudo nano /etc/apache2/sites-available/prj1.conf
    $ sudo a2ensite prj1.conf
    $ sudo a2dissite 000-default
    $ sudo a2enmod wsgi
    $ sudo service apache2 restart

Apache also needs write access to the media folder of each site.::

    $ sudo chown www-data /usr/local/src/lino/prod_sites/prj1/media/

Now you should be able to navigate to your domain and see a barebones
lino-app.


From here
=========

From here you should edit your settings.py file to import a different
:xfile:`settings.py` module from another repo.

Return to the index for more information :doc:`mysql_install`.

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

