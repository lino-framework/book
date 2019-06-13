.. _lino.hosting:
.. _lino.hosters:
.. _lino.admin:

=====================
Administrator's Guide
=====================

This part of the documentation is for system administrators who set up
or maintain a server which hosts one or several Lino production sites.

A **Lino system administrator** is a person who installs Lino
applications in order to make them available on a web server.  They
take care of the maintenance and security of those servers. They might
do this either in a single company as their system administrator or
for a hosting provider.

Typical requirements for a Lino system administrator are:

- Lino is written in Python. You don't need profound knowledge of the
  language, but you are going to install Python packages (using `pip
  <https://pip.pypa.io/en/stable/>`__ into virtual environments (using
  `virtualenv <https://virtualenv.pypa.io/en/stable/index.html>`__).

- Previous experience with hosting `Django
  <https://www.djangoproject.com/>`_ applications is useful.


The approaches described in this document are not mandatory. Hosting a
Lino site is technically the same as hosting a `Django
<https://www.djangoproject.com/>`_ project.  If you are already
hosting Django projects, you might prefer to use your existing system
of approaches.  But even experienced Django hosters might find
interesting tricks or inspiration for their system by reading how we
recommend to do it.

About hosting Lino
------------------

.. toctree::
   :maxdepth: 2

   about
   workflow
   preview



Installation
------------

.. toctree::
    :maxdepth: 2

    install
    media
    mysql_install
    pgsql_install
    config_dirs
    xl
    oood
    linod
    monit
    notify
    security
    cron

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
    virtualenv
    tim2lino
    mysql_tune
    du
    startsite

    
 
    

.. toctree::
    :hidden:
       
    djangosite_local
    mass_hosting
    datamig
    /davlink/index
    /eidreader/index
    /java/index
