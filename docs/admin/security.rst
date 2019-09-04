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

- Set the :attr:`use_security_features
  <lino.core.site.Site.use_security_features>` attribute to `True` in
  order to activate general security features.

- Consider enabling `HTTP Strict Transport Security
  <https://docs.djangoproject.com/en/2.2/ref/middleware/#http-strict-transport-security>`__ by setting
  :setting:`SECURE_HSTS_SECONDS` to a non-zero integer value.

- If you want users to sign in each time after having closed their
  browser sessions, set `SESSION_EXPIRE_AT_BROWSER_CLOSE
  <https://docs.djangoproject.com/en/2.2/ref/settings/#session-expire-at-browser-close>`__
  to `True`.

Notes
=====

Lino does not yet support CSRF protection (:ticket:`2389`).

See also
========

- https://docs.djangoproject.com/en/2.2/topics/security/
