.. _lino.admin.install:

====================================================
Installing a Lino application on a production server
====================================================

Before setting up a production server you should be familiar with
setting up and running a development server as documented in
:ref:`lino.dev.install`.

On a production server you will do the same, but you must additionally
decide:

- how to organize your repositories and virtual environmens
- which web server to use

These things are common with all Django sites and therefore we
recommend to learn from the Django community.  So this section is far
from being complete and currently not well maintained.

We recommend the method using `mod_wsgi` and `virtualenv` 
as described in the following documents:

- https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/
- https://code.google.com/p/modwsgi/wiki/VirtualEnvironments



Prerequisites
-------------

For a Lino production server you'll need shell access to a Linux 
computer that acts as server.


Debian packages
---------------

Some Debian packages and why you might need them:

libapache2-mod-wsgi
  
    This will automatically install Apache 
    (packages apache2 apache2-doc apache2-mpm-prefork libexpat1...)
    
python-dev python-pip python-virtualenv

    If you host more than one Lino application, then you should 
    use Ian Bicking's virtualenv tool.


tinymce

    If :attr:`lino.Lino.use_tinymce` is `True` (probably yes),
    then Lino's ExtJS UI uses the TinyMCE WYSIWYG text editor.
    
mysqldb-server
mariadb-server

    Needed if you plan to use Django's MySQL backend.
    See :doc:`install_mysql`.


ssl-cert
    
    If you want to run a https server.
    

Install Lino
------------


- Create a virtualenv for your Lino application

- Activate this environment, then type::

    $ pip install lino
    
    
To test whether Lino is installed, you can write::

    $ python -c "print __import__('lino').__version__"
    
Note: third-party Lino applications 
usually depend on Lino, 
so installing such an application will automatically
install Lino.
For example to install :ref:`welfare`, you can just type::
  
    $ pip install lino-welfare


Optional Python packages
------------------------
  
The following Python packages (to be installed using `pip install`) 
are optional and therefore not automatically installed:
  
mysql-python

    Needed if you plan to use Django's MySQL backend.
    See :doc:`install_mysql`.



Create a local Lino project
---------------------------

Every Lino project should have at least its own :file:`settings.py` and 
project directory (the directory containing this file).
Local Lino :file:`settings.py` files on production servers 
are usually rather short. Something like::

  from foo.bar.settings import *
  SITE = Site(globals())
   


Collecting static files
=======================

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
------------------------------

If you plan to use Lino in other languages than English, you must 
manually install language packs for TinyMCE from
http://tinymce.moxiecode.com/i18n/index.php?ctrl=lang&act=download&pr_id=1

Simplified instructions for a language pack containing 
my personal selection (de, fr, nl and et)::

  # cd /usr/share/tinymce/www
  # wget http://tim.saffre-rumma.net/dl/tmp/tinymce_language_pack.zip
  # unzip tinymce_language_pack.zip
  
  
