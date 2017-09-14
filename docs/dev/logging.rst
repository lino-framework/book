.. _lino.logging:

========================
How to configure logging
========================


- :attr:`lino.core.site.Site.logger_filename`
- :attr:`lino.core.site.Site.history_aware_logging`
- :attr:`lino.core.site.Site.log_each_action_request`
- :attr:`lino.core.site.Site.auto_configure_logger_names`

- :meth:`lino.core.site.Site.setup_logging`

- On my development machine I have a `runserver` script which does::

    set LINO_LOGLEVEL=DEBUG
    python manage.py runserver  
  

  
Showing SQL statements
======================

:meth:`lino.core.site.Site.setup_logging` sets the level for the
`django.db.backends
<https://docs.djangoproject.com/en/1.11/topics/logging/#django-db-backends>`__
handler to WARNING.

A similar thing happens for the `schedule` handler.

TODO: how to override or change these hard-coded logger configurations?


The main logger file
====================
      
.. xfile:: lino.log
.. xfile:: system.log

    The name of Lino's main logger file Default value is
    :xfile:`lino.log`. Until 20160729 it was :xfile:`system.log`.


Setting the log level via the environment
=========================================


.. envvar:: LINO_LOGLEVEL

If an environment variable :envvar:`LINO_LOGLEVEL` is set, then it
should contain the log level to use for both console and file
handlers. It should be one of `INFO`, `DEBUG` etc.


