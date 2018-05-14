.. _lino.admin.security:

=============================
Security of Lino applications
=============================



Brute force attacks
===================

To prevent brute force attacks,
:attr:`lino.core.site.Site.use_ipdict` should be set to `True`.


Clickjacking attacks
====================

To prevent clickjacking attacks (at least in modern browsers), you can
activate Django's built-in `Clickjacking protection
<https://docs.djangoproject.com/en/1.11/ref/clickjacking/>`__.

Simply add the following line to the end of your :xfile:`settings.py`
file (it must be **after** initializing the :setting:`SITE`)::

    MIDDLEWARE_CLASSES += (
        'django.middleware.clickjacking.XFrameOptionsMiddleware',)

      
Lino still uses `MIDDLEWARE_CLASSES
<https://docs.djangoproject.com/en/1.11/ref/settings/#middleware-classes>`__
instead of :setting:`MIDDLEWARE`.
We should probably upgrade all Lino
middleware to the new middleware style.
See also 
https://docs.djangoproject.com/en/1.11/topics/http/middleware/#upgrading-middleware


