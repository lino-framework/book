.. _lino.admin:

=====================
Administrator's Guide
=====================

This part of the documentation is for **system administrators** who
set up or maintain a server which hosts one or several Lino production
sites. Non-programmers will prefer to read :doc:`/about/index`,
developers :doc:`/dev/index`

The approaches described in this document are not mandatory. Hosting a
Lino site is technically the same as hosting a `Django
<https://www.djangoproject.com/>`_ project.  If you are already
hosting Django projects, you might prefer to use your existing system
of approaches.  But even experienced Django hosters might find
interesting tricks or inspiration for their system by reading how we
recommend to do it.


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
    notify

Maintenance
-----------

.. toctree::
    :maxdepth: 2
   
    settings
    snapshot
    reload_services
    upgrade
    env
    shell_scripts
    bash_aliases
    logging
    new_site
   

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

Other
-----

.. toctree::
    :maxdepth: 2
   
    pythonpath
   
    permissions
    umask
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
    datamig
