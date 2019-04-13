.. _lino.tutorial.writing_fixtures:
.. _lino.tutorial.dpy:

================================
Writing Python fixtures
================================

.. to test just this doc:

    $ doctest docs/dev/pyfixtures/index.rst

   doctest init::

    >>> from atelier.sheller import Sheller
    >>> shell = Sheller('docs/dev/pyfixtures')


This tutorial shows how to use :doc:`the Python serializer
</topics/dpy>` for writing and loading demonstration data samples for
application prototypes and test suites.

We suppose that you have followed the :ref:`lino.tutorial.hello`
tutorial.


.. contents::
    :depth: 1
    :local:

Introduction
============

You know that a *fixture* is a collection of data records in one or
several tables which can be loaded into a database.  Django's
`Providing initial data for models
<https://docs.djangoproject.com/en/1.11/howto/initial-data/>`__ article
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

Writing your own fixture
========================

Create a directory named :xfile:`fixtures` in your local project
directory (the one you created in :ref:`lino.tutorial.hello`)::

   $ cd ~/projects/hello
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
`initdb dumpy1` started on database .../default.db.
Operations to perform:
  Synchronize unmigrated apps: about, bootstrap3, cal, checkdata, contacts, countries, export_excel, extjs, gfks, jinja, lino, office, printing, staticfiles, system, users, xl
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
    Creating table checkdata_problem
    Creating table cal_dailyplannerrow
    Creating table cal_remotecalendar
    Creating table cal_room
    Creating table cal_eventtype
    Creating table cal_guestrole
    Creating table cal_calendar
    Creating table cal_subscription
    Creating table cal_task
    Creating table cal_eventpolicy
    Creating table cal_recurrentevent
    Creating table cal_event
    Creating table cal_guest
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying sessions.0001_initial... OK
Loading data from .../docs/dev/pyfixtures/fixtures/dumpy1.py
Installed 2 object(s) from 1 fixture(s)

Let's use the :manage:`show` command to see whether our data has been
imported::

    $ python manage.py show users.Users

The output should be as follows:

>>> shell("python manage.py show users.Users")
... #doctest: +ELLIPSIS
========== =========== ============ ===========
 Username   User type   First name   Last name
---------- ----------- ------------ -----------
 jdupond                Jean         Dupond
 pbommel                Piet         Bommel
========== =========== ============ ===========

  
.. _tutorial.instantiator:

The ``Instantiator`` class
==========================

Since `.py` fixtures are normal Python modules, there are no more
limits to our phantasy when creating new objects.  A first thing that
might drop into our mind is that there should be a more "compact" way
to create many records of a same table.

A quick generic method for writing more compact fixtures this is the
:class:`Instantiator <lino.utils.instantiator.Instantiator>` class.
Here is the same fixture using an instantiator:

.. literalinclude:: fixtures/dumpy2.py
    :linenos:


Note that the name ``User`` in that file refers to the :meth:`build
<lino.utils.instantiator.Instantiator.build>` method of an
:class:`Instantiator <lino.utils.instantiator.Instantiator>` instance,
not to some User model.

The :class:`Instantiator <lino.utils.instantiator.Instantiator>` class
is just a little utility. It helps us to eliminate some lines of the
code, nothing more (and nothing less). Compare the two source files on
this page and imagine you want to maintain these fixtures. For example
add a third user, or add a new field for every user.  Which one will
be easier to maintain?


Python fixtures are intelligent
===============================

Note the difference between "intelligent" and "dumped" fixtures: An
**intelligent fixture** is written by a human and used to provide demo
data to a Lino application (see :doc:`/dev/pyfixtures/index`).  A **dumped
fixture** is generated by the :command:`dumpdata` or
:command:`dump2py` command and looks much less readable because it is
optimized to allow automated database migrations.
  
Python fixtures are a powerful tool.  You can use them to generate
demo data in many different ways. Look for example at the source code
of the following fixtures:

- :mod:`lino_xl.lib.notes.fixtures.demo`.

- :mod:`lino.modlib.users.fixtures.demo_users`

- :mod:`lino_xl.lib.countries.fixtures.few_countries`

- :mod:`lino_xl.lib.countries.fixtures.all_countries`

- :mod:`lino_xl.lib.countries.fixtures.few_cities`
- :mod:`lino_xl.lib.countries.fixtures.all_cities`
- :mod:`lino_xl.lib.countries.fixtures.be`
- :mod:`lino_xl.lib.countries.fixtures.eesti`

- :mod:`lino.modlib.languages.fixtures.few_languages`
- :mod:`lino.modlib.languages.fixtures.all_languages`

Play with them by trying your own combinations::

  $ python manage.py initdb std all_countries be few_languages props demo 
  $ python manage.py initdb std few_languages few_countries few_cities demo 
  ...

Exercise
========

- Get inspired by the examples above and extend your :file:`dumpy2.py`
  fixture.

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

