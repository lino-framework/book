.. _lino.admin:

=====================
Administrator's Guide
=====================

This document is for :doc:`system administrators </team/sysadm>` who
set up or maintain a server which hosts one or several Lino
applications.

Theoretically this document contains everything you need to know. As
long as there is a difference between theory and practice you are
likely to get free support by the Lino Team.

The approaches described in this document are not mandatory. Hosting a
Lino application is technically the same as hosting a `Django
<https://www.djangoproject.com/>`_ project. If you are already hosting
Django projects, then you might prefer to use your existing system of
approaches.  But even experienced Django hosters might find
interesting tricks or inspiration for their system by reading how we
do it.


Installation
------------

.. toctree::
    :maxdepth: 2

    install
    media
    mysql_install
    config_dirs
    xl
    oood

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
    mailbox
    django_tests
    apache_webdav
    using
    webdav
    install_shell_scripts
    linod
    virtualenv
    tim2lino
    mysql_tune
    du
    

.. toctree::
    :hidden:
       
    djangosite_local
    mass_hosting
