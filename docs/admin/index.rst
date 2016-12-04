.. _lino.admin:

=====================
Administrator's Guide
=====================

This document is for :doc:`system administrators </team/sysadm>` who
set up or maintain a server which hosts one or several Lino
applications.

If you are already hosting Django projects, then you might prefer to
use your existing system.  Hosting a Lino application is technically
the same as hosting a `Django <https://www.djangoproject.com/>`_
project, so this guide is not mandatory. But even experienced Django
hosters might find interesting tricks or inspiration for their system
by reading how we do it.


Installation
------------

.. toctree::
    :maxdepth: 2

    install
    media
    install_mysql
    config_dirs
    xl

Maintenance
-----------

.. toctree::
    :maxdepth: 2

    upgrade
    datamig
    env
    shell_scripts
    bash_aliases
   

Java applets included with Lino
-------------------------------

.. toctree::
   :maxdepth: 2

   /davlink/index
   /eidreader/index
   /java/index


Printing
--------

.. toctree::
    :maxdepth: 2
   
    printing
    using_appy_pod
    excerpts
    appy_templates

Howto
-----

.. toctree::
    :maxdepth: 2
   
    settings
    snapshot

Other
-----

.. toctree::
    :maxdepth: 2
   
    pythonpath
   
    permissions
    apache_http_auth
    django_tests
    apache_webdav
    using
    webdav
    install_shell_scripts
    oood
    linod
    virtualenv
    tim2lino
    mysql_tune
    du
    testing
    

.. toctree::
    :hidden:
       
    djangosite_local
    mass_hosting
