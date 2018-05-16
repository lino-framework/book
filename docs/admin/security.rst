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

- Make sure that :attr:`use_security_features
  <lino.core.site.Site.use_security_features>` is set to `True` in
  order to activate general security features.

- Consider enabling `HTTP Strict Transport Security
  <https://docs.djangoproject.com/en/1.11/ref/middleware/#http-strict-transport-security>`__ by setting
  :setting:`SECURE_HSTS_SECONDS` to a non-zero integer value.

