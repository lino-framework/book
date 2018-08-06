.. _user.install:

===============
Installing Lino
===============

Warning: 
**The installation process described below does not yet work.**
Until we are done, you should rather follow the instructions
about :doc:`/dev/install`.

This document explains how to install Lino on your machine in order to
write applications.  If you prefer using the latest version, then you
should rather follow :doc:`/dev/install`.

For deploying Lino applications on a production site you will read
:doc:`/admin/install`.

Basically you open a terminal and type::

    $ virtualenv env
    $ . env/bin/activate
    $ pip install lino_cosi
    
    $ mkdir mylino
    $ nano mylino/settings.py

Copy the following content to your editor::
    
    from lino_cosi.lib.cosi.settings import *
    SITE = Site(globals())

Save your file and continue in the terminal::
    
    $ export DJANGO_SETTINGS_MODULE=mylino.settings
    $ django-admin prep
    $ django-admin runserver

    

