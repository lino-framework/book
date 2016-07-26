.. _lino.tutorial.writing_fixtures:
.. _lino.tutorial.dpy:

================================
Writing your own Python fixtures
================================

.. to test just this doc:

    $ python setup.py test -s tests.DocsTests.test_dumpy

   doctest init::

    >>> from atelier.sheller import Sheller
    >>> shell = Sheller(".")


This tutorial shows how to use :doc:`the Python serializer
</topics/dpy>` for writing and loading demonstration data samples for
application prototypes and test suites.

We suppose that you have folled the :ref:`lino.tutorial.hello`
tutorial.


.. contents::
    :depth: 1
    :local:

Introduction
============

You know that a *fixture* is a collection of data records in one or
several tables which can be loaded into a database.  Django's
`Providing initial data for models
<https://docs.djangoproject.com/en/1.9/howto/initial-data/>`__ article
says that "fixtures can be written as XML, YAML, or JSON documents".
Well, Lino adds another format to this list: Python.

Here is a fictive minimal example of a Python fixture::

  from myapp.models import Foo
  def objects():
      yield Foo(name="First")
      yield Foo(name="Second")

A Python fixture is a normal Python module, stored in a file ending
with :file:`.py` and designed to being imported and exectued during
Django's :manage:`loaddata` command.  It is furthermore expected to
contain a function named ``objects`` which must take no parameters and
which must return (or yield) a list of database objects.


Good to know
============

Here are some standard Django admin commands that you should know.

.. management_command:: shell

    Start an interactive Python session using your project settings.
    See the `Django documentation
    <https://docs.djangoproject.com/en/1.9/ref/django-admin/#shell>`__

.. management_command:: dumpdata

    Output all data in the database (or some tables) to a serialized
    stream. The default will write to `stdout`, but you usually
    redirect this into a file.  See the `Django documentation
    <https://docs.djangoproject.com/en/1.9/ref/django-admin/#dumpdata>`__
    
    You might theoretically use :manage:`dumpdata` for writing a
    Python fixture, but Lino's preferred equivalent is
    :manage:`dump2py`.

.. management_command:: flush

    Removes all data from the database and re-executes any
    post-synchronization handlers. The table of which migrations have
    been applied is not cleared.  See the `Django documentation
    <https://docs.djangoproject.com/en/1.9/ref/django-admin/#flush>`__
    
.. management_command:: loaddata

    Loads the contents of the named fixtures into the database.
    See the `Django documentation
    <https://docs.djangoproject.com/en/1.9/ref/django-admin/#loaddata>`__.
    
    Both :manage:`loaddata` and :manage:`initdb` can be used to load
    fixtures into a database.  The difference is that :manage:`loaddata`
    *adds* data to your database while :manage:`initdb` first clears
    (initializes) your database.


Writing your own fixture
========================

Create a directory named :xfile:`fixtures` in your local project
directory (the one you created in :ref:`lino.tutorial.hello`)::

   $ cd ~/projects/mysite
   $ mkdir fixtures

Create an empty file :xfile:`__init__.py` in that directory to mark is
as a package::

   $ touch fixtures/__init__.py
   
Create a file `dumpy1.py` in that directory with the following
content, but don't hesitate to put your real name and data, this is
your local file.

.. literalinclude:: fixtures/dumpy1.py
    :linenos:

Initialize your database using this fixture::

  $ python manage.py initdb dumpy1

The output should be as follows:

>>> shell("python manage.py initdb dumpy1 --noinput")
... #doctest: +ELLIPSIS +REPORT_UDIFF +NORMALIZE_WHITESPACE
Operations to perform:
  Synchronize unmigrated apps: gfks, about, jinja, office, countries, staticfiles, contacts, system, xl, printing, lino_startup, cal, users, extjs, export_excel, bootstrap3
  Apply all migrations: contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Creating table system_siteconfig
    Creating table users_user
    Creating table users_authority
    Creating table countries_country
    Creating table countries_place
    Creating table contacts_partner
    Creating table contacts_person
    Creating table contacts_companytype
    Creating table contacts_company
    Creating table contacts_roletype
    Creating table contacts_role
    Creating table gfks_helptext
    Creating table cal_remotecalendar
    Creating table cal_room
    Creating table cal_priority
    Creating table cal_eventtype
    Creating table cal_guestrole
    Creating table cal_calendar
    Creating table cal_subscription
    Creating table cal_task
    Creating table cal_recurrentevent
    Creating table cal_event
    Creating table cal_guest
    Running deferred SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying sessions.0001_initial... OK
Installed 2 object(s) from 1 fixture(s)

Let's use the :manage:`show` command to see whether our data has been
imported::

    $ python manage.py show users.Users

The output should be as follows:

>>> shell("python manage.py show users.Users")
... #doctest: +ELLIPSIS
========== ============== ============ ===========
 Username   User Profile   First name   Last name
---------- -------------- ------------ -----------
 jdupond                   Jean         Dupond
 pbommel                   Piet         Bommel
========== ============== ============ ===========

  
.. _tutorial.instantiator:

The ``Instantiator`` class
==========================

Since `.py` fixtures are normal Python modules, there are no more
limits to our phantasy when creating new objects.  A first thing that
drops into mind is: there should be a more "compact" way to create
many records of a same table.

A quick generic method for for writing more compact fixtures this is
the :class:`Instantiator <lino.utils.instantiator.Instantiator>`
class.  Here is the same fixture in a more compact way using an
instantiator:

.. literalinclude:: fixtures/dumpy2.py
    :linenos:


Not that the name ``User`` in that file refers to the :meth:`build
<lino.utils.instantiator.Instantiator.build>` method of an
:class:`Instantiator <lino.utils.instantiator.Instantiator>` instance.

The :class:`Instantiator <lino.utils.instantiator.Instantiator>` class
is just a little utility. It helps us to eliminate some lines of the
code, nothing more (and nothing less). Compare the two source files on
this page and imagine you want to maintain these fixtures. For example
add a third user, or add a new field for every user.  Which one will
be easier to maintain?


Python fixtures are intelligent
===============================

Python fixtures are a powerful tool.  You can use them to generate
random and massive amount of data. Look for example at the source code
of the following fixtures:

- :mod:`lino_xl.lib.notes.fixtures.demo`.

- :mod:`lino.modlib.users.fixtures.demo_users`

- :mod:`lino_xl.lib.countries.fixtures.few_countries`

- :mod:`lino_xl.lib.countries.fixtures.all_countries`

- :mod:`lino_xl.lib.countries.fixtures.few_cities`
- :mod:`lino_xl.lib.countries.fixtures.all_cities`
- :mod:`lino_xl.lib.countries.fixtures.be`

- :mod:`lino.modlib.languages.fixtures.few_languages`
- :mod:`lino.modlib.languages.fixtures.all_languages`

Play with them by trying your own combinations::

  $ python manage.py initdb std all_countries be few_languages props demo 
  $ python manage.py initdb std few_languages few_countries few_cities demo 
  ...

Exercise
========

- Get inspired by these examples and extend your 
  :file:`dumpy2.py` fixture.

- Publish your code somewhere (e.g. in a blog or on GitHub) so that we
  can refer to it here and others can learn from it.


Python fixtures are modularizable
=================================

Lino encourages fine-grained modularity of your fixtures because as an
application developer your can use the :attr:`demo_fixtures
<lino.core.site.Site.demo_fixtures>` setting in order to specify a
**default set** of fixture names to be loaded.  Check the
:ref:`demo_fixtures` section in case you didn't know this.


Python fixtures don't like relative imports
===========================================

There is one (minor) limitation to your phantasy when writing Python
fixtures: you cannot use relative imports in a Python
fixture.  See `here
<http://stackoverflow.com/questions/4907054/loading-each-py-file-in-a-path-imp-load-module-complains-about-relative-impor>`__



Conclusion
==========

Python fixtures are an important tool for application developers
because

- they are more flexible than json or xml fixtures and easy to adapt 
  when your database structure changes.
  
- they provide a simple and modular way to deploy demo data for your
  application

