.. _lino.hosting:
.. _lino.hosters:
.. _lino.admin:

===================
Administrator Guide
===================


This part of the documentation is for :term:`server administrators <server
administrator>`  who set up or maintain a server which hosts one or several Lino
production sites.

The approaches described in this document are not mandatory. Hosting a
Lino site is technically the same as hosting a `Django
<https://www.djangoproject.com/>`_ project.  If you are already
hosting Django projects, you might prefer to use your existing system
of approaches.  But even experienced Django hosters might find
interesting tricks or inspiration for their system by reading how we
recommend to do it.


.. contents::
    :depth: 1
    :local:


Installation
============

See :ref:`getlino.install.admin`.

About hosting Lino
==================

.. toctree::
   :maxdepth: 2

   about
   workflow
   preview


Maintenance
===========

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
    datamig
    djangomig


Printing
==================

.. toctree::
    :maxdepth: 2

    printing
    using_appy_pod
    excerpts
    appy_templates

Other
==================

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



Installation (obsolete)
=======================

This section is obsolete as these things are now done automatically  in
:ref:`getlino.install.contrib`.

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



.. toctree::
    :hidden:

    djangosite_local
    mass_hosting
    /davlink/index
    /eidreader/index
    /java/index
