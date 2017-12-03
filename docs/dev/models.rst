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
table is an *instance* of that :class:`Model` class.  The models of an
application are defined in a file named :xfile:`models.py`.

Here is the
:xfile:`models.py` file
we are going to use        
in this tutorial:

.. literalinclude:: ../../lino_book/projects/tables/models.py

This file is defined in the :mod:`lino_book.projects.tables` demo
project.

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
    
    
Every :class:`Model` has a class attribute :attr:`objects` which is is
used for operations which access the database.

For example you can *count* how many rows are stored in the database.

>>> from lino_book.projects.tables.models import Author
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

Before leaving, we tidy up by removing Joe Woe from our demo database:

>>> obj.delete()
>>> Author.objects.count()
3


Tim Kholod wrote a nice introduction for beginners: `The simple way to
understand Django models <https://arevej.me/django-models/>`__


