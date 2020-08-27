.. _lino.hosting:
.. _lino.hosters:
.. _lino.admin:

===================
Hosting Guide
===================

This part of the documentation is for :term:`server administrators <server
administrator>` who set up or maintain a server that hosts one or several Lino
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

Running Lino on a full server
=============================

.. toctree::
    :maxdepth: 1

    root
    install
    install_demo
    appy
    backup
    dbengine
    email
    multiple_frontends
    certbot
    security
    cron
    mail/index

Running Lino on PythonAnywhere
==============================

.. toctree::
    :maxdepth: 1

    pyanywhere

Maintenance
===========

.. toctree::
    :maxdepth: 1

    settings
    snapshot
    reload_services
    upgrade
    env
    shell_scripts
    bash_aliases
    logging
    new_site
    djangomig
    preview
    move
    datamig


Printing
==================

.. toctree::
    :maxdepth: 1

    printing
    using_appy_pod
    excerpts
    appy_templates
    config_dirs

Other
==================

.. toctree::
    :maxdepth: 1

    pythonpath
    linod
    monit
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
    oood
    notify
    mirror




.. toctree::
    :hidden:

    djangosite_local
    mass_hosting
    /davlink/index
    /eidreader/index
    /java/index
    attic
    media
    xl
