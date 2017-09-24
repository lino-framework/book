.. _lino.dev.initdb:

===============================
Initializing the demo databases
===============================

.. to run only this test:
   $ doctest docs/dev/initdb.rst

This document describes Lino's innovative way of providing
application-specific demo data.


Standard Django admin commands
==============================

Here are some standard Django admin commands that you should know.

.. management_command:: dumpdata

    Output all data in the database (or some tables) to a serialized
    stream. The default will write to `stdout`, but you usually
    redirect this into a file.  See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#dumpdata>`__
    
    You might theoretically use :manage:`dumpdata` for writing a
    Python fixture, but Lino's preferred equivalent is
    :manage:`dump2py`.

.. management_command:: flush

    Removes all data from the database and re-executes any
    post-synchronization handlers. The migrations history is not
    cleared.  If you would rather start from an empty database and
    re-run all migrations, you should drop and recreate the database
    and then run :manage:`migrate` instead.  See the `Django
    documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#flush>`__
    
    
.. management_command:: loaddata

    Loads the contents of the named fixtures into the database.
    See the `Django documentation
    <https://docs.djangoproject.com/en/1.11/ref/django-admin/#loaddata>`__.
    
    Both :manage:`loaddata` and :manage:`initdb` can be used to load
    fixtures into a database.  The difference is that :manage:`loaddata`
    *adds* data to your database while :manage:`initdb` first clears
    (initializes) your database.



The :manage:`initdb` and :manage:`prep` commands
-------------------------------------------------------

Remember that we told you (in :ref:`lino.tutorial.hello`) to "prepare
your database" by running the command::

  $ python manage.py prep
  
The :manage:`prep` command which we use here is a `custom
django-admin command
<https://docs.djangoproject.com/en/1.9/howto/custom-management-commands/>`_
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

Note the three arguments ``std demo demo2`` to the :manage:`loaddata`
command above.  These are names of *fixtures*.

A **fixture**, in Django, is a portion of data (a collection of data
records in one or several tables) which can be loaded into a database.
Fixtures can be defined by several files in different directories.
Read more about this in the `Django documentation
<https://docs.djangoproject.com/en/1.9/howto/initial-data/>`_.

Lino adds the concept of **demo fixtures**. These are a predefined set
of fixture names to be specified by the application developer via the
:attr:`demo_fixtures <lino.core.site.Site.demo_fixtures>` attribute.
The `min1` application has the following value for this attribute:

>>> from lino import startup
>>> startup('lino_book.projects.min1.settings.demo')
>>> from django.conf import settings
>>> settings.SITE.demo_fixtures
'std demo demo2'

This means that the :manage:`prep` command (in a
:mod:`lino_book.projects.min1` application) is equivalent to::
  
  $ python manage.py initdb std demo demo2

The difference is that with :manage:`prep`, you don't need to
know the list of demo fixtures, which can be long and difficult to
remember, and (more importantly) which can change when an application
evolves.  System administrators usually don't *want* to know such
details. As a future application developer you can learn more about
them in :ref:`lino.tutorial.writing_fixtures`.

