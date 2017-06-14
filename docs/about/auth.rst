.. _about.auth:

================================
Lino has its own user management
================================

Lino replaces Django's `django.contrib.auth
<https://docs.djangoproject.com/en/dev/topics/auth/>`_ plugin by its
own plugin :mod:`lino.modlib.users`.

Django's permission system is not suitable for developing complex
applications because maintaining permissions becomes a hell when you
develop an application which runs on different sites. Also it provides
no means for defining instance-specific permissions and has no
built-in concept of user types.
