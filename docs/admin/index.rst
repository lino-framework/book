.. _lino.hosting:
.. _lino.hosters:
.. _lino.admin:

===================
Hosting Guide
===================

This part of the documentation is for :term:`server administrators <server
administrator>` who set up or maintain a server that hosts one or several Lino
:term:`production sites <production site>`.

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

Setting up a new Lino server
============================

.. toctree::
    :maxdepth: 1

    root
    install
    install_demo
    backup

Configuring a Lino site
=======================

.. toctree::
    :maxdepth: 1

    dbengine
    email
    multiple_frontends
    certbot
    security
    cron
    settings
    snapshot
    env
    logging
    linod
    pythonpath
    permissions
    umask


Maintenance
===========

.. toctree::
    :maxdepth: 1

    reload_services
    upgrade
    shell_scripts
    djangomig
    preview
    move
    appy

Monitoring and diagnostics
==========================

.. toctree::
    :maxdepth: 1

    server_diag
    du
    ram
    monit


Printing
==================

.. toctree::
    :maxdepth: 1

    printing
    appy_templates
    config_dirs

Other
==================

.. toctree::
    :maxdepth: 1

    apache_http_auth
    mailbox
    django_tests
    apache_webdav
    using
    webdav
    virtualenv
    tim2lino
    mysql_tune
    startsite
    oood
    notify
    mirror
    mail/index
    choicelists




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
    pyanywhere
    new_site
    excerpts
    using_appy_pod
    bash_aliases
    datamig
