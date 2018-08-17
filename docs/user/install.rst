.. _user.install:

===============
Installing Lino
===============

**Warning: The installation process described below is currently being
tested. No guarantee.** Until we are done, you should rather follow
the instructions about :doc:`/dev/install`.

This document explains how to install Lino on your machine in order to
write applications.  If you prefer using the latest version, then you
should rather follow :doc:`/dev/install`.

For deploying Lino applications on a production site you will read
:doc:`/admin/install`.

Basically you open a terminal and type::

    $ virtualenv env
    $ . env/bin/activate
    $ pip install lino_cosi

This takes some time.

Now we create a local project::
    
    $ mkdir mylino
    $ touch mylino/__init__.py
    $ touch __init__.py
    $ echo "from lino_cosi.lib.cosi.settings import *" > mylino/settings.py
    $ echo "SITE = Site(globals())" >> mylino/settings.py

Then we initialize and populate the demo database::
  
    $ export DJANGO_SETTINGS_MODULE=mylino.settings
    $ export PYTHONPATH=.
    $ django-admin prep

And finally we launch a development server::
  
    $ django-admin runserver

    

