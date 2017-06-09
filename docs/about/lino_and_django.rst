Lino and Django
===============

From the hoster's and system manager's point of view, Lino
applications are just Django projects.  The difference with plain
Django projects is that Lino applications have an **out-of-the box
user interface**.

For the application developer this means that certain design choices
have been made for you.  You don't not need to write any URLconf,
HTML, CSS nor Javascript.

But Lino is more than a user interface. In fact the current user
interface is not even the only choice [#ui]_.  This section summarizes
the differences between Lino and Django.


- Lino adds the concept of an central :doc:`application object
  </dev/application>` while Django is a radically decentralized
  approach. I believe that without such a central place it is not
  possible --or at least not fun and not efficient-- to maintain
  complex software projects.

- Lino is a replacement for `Django's admin interface
  <http://docs.djangoproject.com/en/dev/ref/contrib/admin>`__.  I
  believe that `django.contrib.admin` is not a usable base for
  representing a desktop-style application.  It has obviously not been
  designed to write complete database applications.
 
- Lino also replaces `django.contrib.auth
  <https://docs.djangoproject.com/en/dev/ref/contrib/auth/>`__ by
  :mod:`lino.modlib.auth`.  I believe that `django.contrib.auth` is
  not suitable for defining and maintaining complex permission systems
  because it lacks the concepts of user roles and functional groups.
  
- Lino doesn't use `django.forms
  <https://docs.djangoproject.com/en/dev/ref/forms/>`__ because I
  believe that this API is "somehow hooked into the wrong place" and
  forces application developers to write redundant code. Lino replaces
  Django's forms by the concept of :doc:`layouts </dev/layouts>`.
  
- Lino suggests (but doesn't enfore) to use its own system for
  :doc:`/dev/datamig` migrations instead of Django's default
  `Migrations
  <https://docs.djangoproject.com/en/dev/topics/migrations/>`_ system.
  
- Lino prefers Jinja2 templates over the `default Django engine
  <https://docs.djangoproject.com/en/dev/topics/templates/>`_ to
  generate its own stuff.  For the plain Django part of your
  application you can use the system of your choice.

- Actions, Choosers, ChoiceLists, Workflows, multi-lingual database
  content, generating printable documents, ...

- Higher level solutions for common features like
  :mod:`lino.modlib.changes`, `lino_xl.lib.excerpts`, ...


.. rubric:: Footnotes

.. [#ui] See :doc:`ui`. 

