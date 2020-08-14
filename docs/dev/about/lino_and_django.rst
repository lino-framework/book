===============
Lino and Django
===============

The differences between Lino and plain Django are visible mainly for
the application developer.

A first an most visible difference with plain Django projects is that
your Lino applications have an out-of-the box **front end**.  You
don't not need to write any URLconf, HTML, CSS nor Javascript.

But Lino is more than a front end. In fact the current front end is not even the
only choice [#ui]_.  Here are the **under the hood** differences between Lino
and Django.

- Lino adds the concept of an central :doc:`application object
  </dev/application>` while Django is a radically decentralized approach. We
  believe that without such a central place it is not possible -or at least not
  efficient- to maintain complex software projects.

- Lino is a replacement for `Django's admin interface
  <http://docs.djangoproject.com/en/2.2/ref/contrib/admin>`__ which has
  obviously not been designed as a base for writing and maintaining collections
  of reusable customized database applications.

- Lino replaces Django's database-stored user groups and
  permissions system by a system that uses pure Python code objects.
  This approach is more suitable for defining and maintaining complex
  applications.

- Lino doesn't use `django.forms
  <https://docs.djangoproject.com/en/3.1/ref/forms/>`__ because they
  are not needed.  We believe that this API is "somehow hooked into
  the wrong place" and forces application developers to write
  redundant code. Lino replaces Django's forms by the concept of
  :doc:`layouts </dev/layouts/index>`.

- Lino suggests (but doesn't enfore) to use its own system for
  :doc:`database migrations </dev/datamig>` instead of Django's default
  `Migrations
  <https://docs.djangoproject.com/en/3.1/topics/migrations/>`_ system.

- Lino prefers Jinja2 templates over the `default Django engine
  <https://docs.djangoproject.com/en/3.1/topics/templates/>`_ to
  generate its own stuff.  For the plain Django part of your
  application you can use the system of your choice.

- Lino adds concepts like Actions, Choosers, ChoiceLists, Workflows,
  multi-lingual database content, generating printable documents, ...

- Lino comes with a set of high level features like
  :mod:`lino.modlib.comments`,
  :mod:`lino.modlib.changes`,
  :mod:`lino_xl.lib.excerpts`,
  :mod:`lino.modlib.summaries`, ...


.. rubric:: Footnotes

.. [#ui] See :doc:`ui`.
