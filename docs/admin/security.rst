.. _lino.admin.security:

=============================
Security of Lino applications
=============================

When your Lino site is publicly accessible via Internet you should
care about potential security issues.

Checklist
=========

- Make sure that :setting:`DEBUG` is set to `False`.

- Make sure that :attr:`use_ipdict <lino.core.site.Site.use_ipdict>` is
  set to `True` in order to prevent brute force attacks.

- Activate `Clickjacking protection`_ (see below).


Clickjacking protection
=======================

To prevent clickjacking attacks (at least in modern browsers), you can
activate Django's built-in `Clickjacking protection
<https://docs.djangoproject.com/en/1.11/ref/clickjacking/>`__.

To activate clickjacking protection, you simply add the following line
to the end of your :xfile:`settings.py` file::

    MIDDLEWARE_CLASSES += (
        'django.middleware.clickjacking.XFrameOptionsMiddleware',)

Note that you must to this *after* initializing the :setting:`SITE`
because Lino sets the :setting:`MIDDLEWARE_CLASSES` setting during
site initialization.
