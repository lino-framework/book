.. doctest docs/dev/models.rst
   
.. _dev.models:

======================
Introduction to models
======================

.. contents::
    :depth: 1
    :local:


Lino applications fully use Django's ORM.  In Django, every *database
table* is described by a subclass of :class:`Model`.  Every row of the
table is an *instance* of that class.

The models of an application are defined in a file named
:xfile:`models.py`.  Here is the :xfile:`models.py` file we are going
to use in this tutorial:

.. literalinclude:: ../../lino_book/projects/tables/models.py

This file is defined in the :mod:`lino_book.projects.tables` demo
project.  You can try the code snippets on this page from within a
Django shell in that project::

  $ go tables
  $ python manage.py shell

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.tables.settings')
    >>> from lino.api.doctest import *

    
.. initialize the database:

    
    >>> from atelier.sheller import Sheller
    >>> shell = Sheller(settings.SITE.project_dir)
    >>> shell('python manage.py prep --noinput')
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
    `initdb demo` started on database .../default.db.
    Operations to perform:
      Synchronize unmigrated apps: about, bootstrap3, extjs, jinja, lino, staticfiles, tables
      Apply all migrations: (none)
    Synchronizing apps without migrations:
      Creating tables...
        Creating table tables_author
        Creating table tables_book
        Running deferred SQL...
    Running migrations:
      No migrations to apply.
    Loading data from .../fixtures/demo.py
    Installed 7 object(s) from 1 fixture(s)


Accessing the database
======================
    
We import our two models:

>>> from lino_book.projects.tables.models import Author, Book

Every :class:`Model` has a class attribute :attr:`objects` which is
used for operations that *access the database*.

For example you can *count* how many rows are stored in the database.

>>> Author.objects.count()
3

Or you can loop over them:

>>> for a in Author.objects.all():
...     print(a)
Adams, Douglas
Camus, Albert
Huttner, Hannes


You can create a new row by saying:

>>> obj = Author(first_name="Joe", last_name="Doe")

That row is not yet stored in the database, but you can already use
it.  For example you can access the individual fields:

>>> print(obj.first_name)
Joe
>>> print(obj.last_name)
Doe

For example it has a :meth:`__str__` method:

>>> print(obj)
Doe, Joe

You can change the value of a field:

>>> obj.last_name = "Woe"

>>> print(obj)
Woe, Joe


In order to store our object to the database, we call its :meth:`save`
method::

>>> obj.full_clean()  # see later
>>> obj.save()

Our database now knows a new author, Joe Woe:

>>> Author.objects.count()
4
>>> for a in Author.objects.all():
...     print(a)
Adams, Douglas
Camus, Albert
Huttner, Hannes
Woe, Joe


The :meth:`all` method of the :attr:`objects` of a :class:`Model`
returns what Django calls a **queryset**.  A queryset is a volatile
Python object which describes an ``SQL SELECT`` statement. You can see
the SQL if you want:

>>> qs = Author.objects.all()
>>> print(qs.query)
SELECT "tables_author"."id", "tables_author"."first_name", "tables_author"."last_name", "tables_author"."country" FROM "tables_author"

>>> qs = Author.objects.filter(first_name="Joe")
>>> print(qs.query)
SELECT "tables_author"."id", "tables_author"."first_name", "tables_author"."last_name", "tables_author"."country" FROM "tables_author" WHERE "tables_author"."first_name" = Joe

>>> qs.count()
1
>>> qs
<QuerySet [Author #4 ('Woe, Joe')]>

Before going on we tidy up by removing Joe Woe from our demo database:

>>> obj.delete()
>>> Author.objects.count()
3


Validating data
===============

You should always call the :meth:`full_clean` method of an object
before actually calling its :meth:`save` method.  Django does not do
this automatically because they wanted to leave this decision to the
developer.

For example, we did not specify that the :attr:`last_name` of an
author may be empty.  So Django will complain if we try to create an
author without last_name:

>>> author = Author(first_name="Joe")
>>> author.full_clean()
Traceback (most recent call last):
...
ValidationError: {'last_name': [u'This field cannot be blank.']}

Note that Django complains only when we call :meth:`full_clean`.

Note that the :attr:`country` field is declared with `blank=True`, so
this field is optional.

The :class:`ValidationError` is a special kind of exception which
contains a dictionary that can contain one error message for every
field. In the Book model we have three mandatory fields: the
:attr:`title`, the :attr:`price` and the year of publication
(:attr:`published`).  Giving only a title is not enough:

>>> book = Book(title="Foo")
>>> book.full_clean()
Traceback (most recent call last):
...
ValidationError: {'price': [u'This field cannot be null.'], 'published': [u'This field cannot be null.']}


The Book model also shows how you can define custom validation rules
that may depend on complex conditions which involve more than one
field.

>>> book = Book(title="Foo", published=2001, price='4.2')
>>> book.full_clean()
Traceback (most recent call last):
...
ValidationError: [u'A book from 2001 for only $4.20!']


Going deeper
============

Tim Kholod wrote a nice introduction for beginners: `The simple way to
understand Django models <https://arevej.me/django-models/>`__

If you want to know more about Django's way to access the database
using models, read the Django documentation about
`Models and databases
<https://docs.djangoproject.com/en/2.1/topics/db/>`__.


