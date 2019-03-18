.. _user.install:

===============
Installing Lino
===============

This document explains how to install Lino on your machine in order to write
applications.  If you prefer using the latest version, then you should rather
follow :doc:`/dev/install`. For deploying Lino applications on a production
site you will read :doc:`/admin/install`.

Basically you open a terminal and type::

    $ virtualenv env
    $ . env/bin/activate
    $ pip install lino_cosi

Then create a local project::
    
    $ mkdir mylino
    $ touch mylino/__init__.py
    $ nano mylino/settings.py

Add the following  content to your :xfile:`settings.py` file::

    from lino_cosi.lib.cosi.settings import *
    SITE = Site(globals())
    DEBUG = True

Tell Django and Python to use your settings::

    $ export DJANGO_SETTINGS_MODULE=mylino.settings
    $ export PYTHONPATH=.

Then initialize and populate the demo database::
  
    $ django-admin prep

And finally we launch a development server::
  
    $ django-admin runserver

    

