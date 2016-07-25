.. _lino.dev.initdb:

===============================
Introduction to Python fixtures
===============================

.. to run only this test:
  $ python setup.py test -s tests.DocsTests.test_initdb

This section gives a first introduction into Lino's innovative way of
providing application-specific demo data.

The :manage:`initdb` and :manage:`initdb_demo` commands
-------------------------------------------------------

Remember that we told you (in :ref:`lino.tutorial.hello`) to "prepare
your database" by running the command::

  $ python manage.py initdb_demo
  
The :xfile:`manage.py` Python script is the standard Django interface
for running a so-called **administrative task** (if you did't know
that, please read `django-admin.py and manage.py
<https://docs.djangoproject.com/en/1.9/ref/django-admin/>`_).

The :manage:`initdb_demo` command which we use here is a `custom
django-admin command
<https://docs.djangoproject.com/en/1.6/howto/custom-management-commands/>`_
provided by Lino.  It does nothing else than to call :manage:`initdb`
with the so-called *demo fixtures* as argument. So now you'll ask:
what is the :manage:`initdb` command, and what are demo fixtures?

The :manage:`initdb` command
----------------------------

The :manage:`initdb` command performs three actions in one:

- it flushes the database specified in your :xfile:`settings.py`,
  i.e. issues a ``DROP TABLE`` for every table used by your application.
 
- then runs Django's `migrate` command to re-create all tables,

- and finally runs Django's `loaddata` command to load the specified
  fixtures.

So the above line is functionally equivalent to the following plain
Django commands::

  $ python manage.py flush
  $ python manage.py migrate
  $ python manage.py loaddata std demo demo2
  
The main difference is that :manage:`initdb` doesn't ask you to type
"yes" followed by :kbd:`RETURN` in order to confirm that you really
want it.  Yes, removing all tables may sound dangerous, but it *is*
actually what we want quite often: when we just want to quickly try
this application, or when we are developing a prototype and made some
changes to the database structure.  We assume that nobody will ever
let a Lino application and some other application share the same
database.

.. _demo_fixtures:

What are demo fixtures?
=======================

Note the three arguments ``std demo demo2`` to both the
:manage:`loaddata` and :manage:`initdb` commands above.  These are
names of so-called *fixtures*.

A **fixture**, in Django, is a portion of data (a collection of data
records in one or several tables) which can be loaded into a database.
Read more about fixtures in the `Providing initial data for models
<https://docs.djangoproject.com/en/1.9/howto/initial-data/>`_ article
of the Django documentation.

Lino adds the concept of **demo fixtures**. These are a predefined set
of fixture names to be specified by the application developer.  

This is done via the :attr:`demo_fixtures
<lino.core.site.Site.demo_fixtures>` attribute.  The `min1` app has
the following value for this attribute:

>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.demo')
>>> from django.conf import settings
>>> settings.SITE.demo_fixtures
'std demo demo2'

This just means that the :manage:`initdb_demo` command (at least in a
:mod:`lino_book.projects.min1` application) is equivalent to::
  
  $ python manage.py initdb std demo demo2

The difference is that with :manage:`initdb_demo`, you don't need to
know the list of demo fixtures, which can be long and difficult to
remember, and (more importantly) which can change when an application
evolves.  System administrators usually don't *want* to know such
details. As a future application developer you can learn more about
them in :ref:`lino.tutorial.writing_fixtures`.

