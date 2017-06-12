.. _lino.admin.install:

====================================================
Installing a Lino application on a production server
====================================================

Here is a system of files and conventions which we suggest to use when
hosting a Lino production site.  It suits well for having multiple
sites on a same machine.

Prerequisites
=============

You need shell access to a **Linux server**, i.e. a virtual or
physical machine with a Linux operating system running in a network.

We recommend a **stable Debian** as operating system.  If you prefer
some other Linux distribution, that should be no problem. There will
be some differences, but you probably know them.  You need a **web
server**, **Python 2**, some database (e.g. **MySQL** or
**PostGreSQL**) running on that server.

If your customers want want to access their Lino from outside of their
intranet, then you need to setup a **domain name** and configure
Apache to use secure HTTP.


Lino directory structure
========================

There are many ways to setup a django/lino wsgi application. For this
guide we shall be using apache2, mysql, a site-wide lino settings file,
and a virtual python environment for each site.

The recommenced directory structure is the following::

    /usr/local/src/
    └── lino
        ├── __init__.py
        ├── lino_local.py # Site-wide settings
        └── lino_sites/
            ├── __init__.py
            ├── prj1 # Site directory
            │   ├── __init__.py
            │   ├── env/ # Virtual environment
            │   │   ├─── bin
            │   │   └─── ...
            │   ├── repositories/ # Lino git-repositories
            │   │   ├─── lino
            │   │   ├─── xl
            │   │   ├─── django
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

It is possible to use symbolic links for site directories or the virtual
environment, in order to manage user permissions or have several sites
working on the same virtual environment.

However please note, if you choose the use the example configuration
files contained in this guide. Ensure that the above directory structure
is maintained.

System users
============

Create one or several users who will be the *maintainers* of this
site::

    $ sudo adduser joe

Maintainers must be members of the `sudo` and `www-data` groups::
  
    $ sudo adduser joe sudo
    $ sudo adduser joe www-data

They must have a umask 002 or 007::

    $ nano /home/joe/.bashrc
  
.. rubric:: Notes

- `useradd` is a native binary compiled with the system, while
  `adduser` is a perl script which uses `useradd` in back-end.


Installing Lino
===============

First create the lino_sites folder.::

    $ sudo mkdir -p /usr/local/src/lino/lino_sites/

Create the site folder for your site, in this example we shall use *prj1*::

    $ sudo mkdir /usr/local/src/lino/lino_sites/prj1
    $ cd /usr/local/src/lino/lino_sites/prj1

Follow the instructions in :doc:`/dev/install` for installing a
*development* version of Lino inside of our new prj1 *site-folder*.


More Debian packages
====================

Some Debian packages and why you might need them::

    $ sudo apt-get install apache2 libapache2-mod-wsgi

This will automatically install Apache 
(packages apache2 apache2-doc apache2-mpm-prefork libexpat1...)

Select your database backend::

    $ sudo apt-get install mysql-server

or::

    $ sudo apt-get install mariadb-server

Install the python dependencies::

    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install python-dev
    $ sudo apt-get install libffi-dev libssl-dev
    $ pip install mysqlclient

For more info on how to setup a user and database see; :doc:`mysql_install`.

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

- a empty :xfile:`__init__.py` file making it able for apache to import your settings::

    $ touch /usr/local/src/lino/lino_sites/prj1/__init__.py

- a file :xfile:`settings.py` **Note:** Replace the 'prj1' in this file with the name of the site-folder:

    .. literalinclude:: mypy/prj1/settings.py

- a file :xfile:`manage.py`:

    .. literalinclude:: mypy/prj1/manage.py

- a file :xfile:`wsgi.py`. **Note:** Replace the 'prj1' in this file with the name of the site-folder:

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


Collecting static files
=======================

.. .(Needs revision)

One part of your cache directory are the static files.  When your
:envvar:`LINO_CACHE_ROOT` is set, you should run Django's
:manage:`collectstatic` command::

    $ cd /usr/local/src/lino/lino_sites/prj1/
    $ python manage.py collectstatic

The output should be something like this::

    You have requested to collect static files at the destination
    location as specified in your settings:

        /usr/local/src/lino/lino_sites/prj1/static/

    This will overwrite existing files!
    Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: yes

    4688 static files copied to '/usr/local/src/lino/lino_sites/prj1/static/', 0 unmodified.


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

The following is an example of a apache config for our prj1 site.

This example is setup for a single lino-site, if you plan to host more
then one lino-site we advise you to move your static files to
/usr/local/src/lino/static/ and updating the config.


  .. literalinclude:: mypy/prj1/apache2/apache.conf


Do the following in order to active the site with apache::

    $ sudo nano /etc/apache2/sites-available/prj1.conf
    $ sudo a2ensite prj1.conf
    $ sudo a2dissite 000-default
    $ sudo a2enmod wsgi
    $ sudo service apache2 restart

Apache also needs write access to the media folder of each site.::

    $ sudo chown www-data /usr/local/src/lino/lino_sites/prj1/media/

Now you should be able to navigate to your domain and see a barebones
lino-app.


From here
=========

<<<<<<< HEAD
From here you should edit your settings.py file to either import a
=======
From here you should edit your settings.py file to import a
>>>>>>> 47a770715a9d490c7e51bb3b712dc876ab59445a
different settings.py from another repo.

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

