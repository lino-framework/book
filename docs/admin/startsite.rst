.. _lino.admin.startsite:

====================================================
The ``startsite`` script
====================================================


.. xfile:: startsite.sh

The :xfile:`startsite.sh` script is used during :doc:`install`
to setup a new Lino production site on a server.

The script is meant as template for a script to be adapted to your system.

Usage
=====

::

  $ wget https://raw.githubusercontent.com/lino-framework/lino/master/bash/startsite.sh
  $ nano startsite.sh

Edit the config section of the file to adapt it to your system-wide server
preferences.

  $ sudo chmod a+x startsite.sh
  $ sudo mv startsite.sh /usr/local/bin


The remaining sections of this page just describe what the script does.
You don't need to read them unless something goes wrong.

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

Create a new Python environment in your project directory::

        $ sudo apt install virtualenv
        $ virtualenv --python=python2 env

*Activate* this environment by typing::

        $ . env/bin/activate

Afterwards update the new environment's pip and setuptools to the
latest version::

        $ pip install -U pip
        $ pip install -U setuptools
    


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

    $ sudo apt install apache2 libapache2-mod-wsgi

This will automatically install Apache 
(packages apache2 apache2-doc apache2-mpm-prefork libexpat1...)

If MySQL is your database backend::

    $ sudo apt install mysql-server
    $ sudo apt install libmysqlclient-dev
    $ sudo apt install python-dev
    $ sudo apt install libffi-dev libssl-dev

Install the mysql client into your project's virtualenv::
  
    $ pip install mysqlclient

If you prefer PostgreSQL::

    $ sudo apt install postgresql
    
Install the PostgreSQL client into your project's virtualenv::
  
    $ pip install psycopg2

For more info on how to setup a user and database see
:doc:`mysql_install` and :doc:`pgsql_install`.
     

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
<https://docs.djangoproject.com/en/1.11/topics/install/#get-your-database-running>`__


Activate file logging
=====================

See :doc:`/admin/logging`.



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


Install TinyMCE language packs
==============================

(Needs revision)

If you plan to use Lino in other languages than English, you must 
manually install language packs for TinyMCE from
http://tinymce.moxiecode.com/i18n/index.php?ctrl=lang&act=download&pr_id=1

Simplified instructions for a language pack containing 
my personal selection (de, fr, nl and et)::

  # cd /usr/share/tinymce/www
  # wget http://tim.lino-framework.org/dl/tmp/tinymce_language_pack.zip
  # unzip tinymce_language_pack.zip

