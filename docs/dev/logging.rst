.. _dev.logging:

==========================================
About logging in a development environment
==========================================

See also :doc:`/admin/logging`.

On my development machine I have a `runserver` script which does::

    set LINO_LOGLEVEL=DEBUG
    python manage.py runserver  
  

  
Showing SQL statements
======================

:meth:`lino.core.site.Site.setup_logging` sets the level for the
`django.db.backends
<https://docs.djangoproject.com/en/2.2/topics/logging/#django-db-backends>`__
handler to WARNING.

A similar thing happens for the `schedule` handler.

TODO: how to override or change these hard-coded logger configurations?


