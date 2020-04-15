===========================
Configuring e-mail settings
===========================

A :term:`Lino site` may want to send emails to the outside world in the
following situations:

- When a exception happens on the server code, we want to inform the :term:`site
  maintainer`.

- The Lino application (:mod:`lino.modlib.notify`) may decide to send
  notification mails to site users
- An :term:`end user` may use the outbox plugin to explicitly write emails.


Here are the Django settings for sending emails.

.. setting:: ADMINS

  The list of the site administrators

.. setting:: EMAIL_HOST

  The SMTP host that will accept outgoing mails from this site.

  See also https://docs.djangoproject.com/en/3.0/ref/settings/#email-host

.. setting:: EMAIL_HOST_USER

  The user name to use when connecting to the :setting:`EMAIL_HOST`

  See also https://docs.djangoproject.com/en/3.0/ref/settings/#email-host-user

.. setting:: EMAIL_HOST_PASSWORD

  The password to use when connecting as :setting:`EMAIL_HOST_USER` to the :setting:`EMAIL_HOST`

  See also https://docs.djangoproject.com/en/3.0/ref/settings/#email-host-password

.. setting:: SERVER_EMAIL

  The address to use as sender in outgoing mails to the admins

.. setting:: DEFAULT_FROM_EMAIL

  Default value for sender of outgoing emails
  when application code doesn't specify it.

.. setting:: EMAIL_SUBJECT_PREFIX

  The subject prefix to use for emails to the :setting:`ADMINS`.

  See `Django docs
  <https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-EMAIL_SUBJECT_PREFIX>`__

  Lino also uses this in :mod:`lino.modlib.notify`.
