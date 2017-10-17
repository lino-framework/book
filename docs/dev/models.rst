.. doctest docs/dev/models.rst
   
.. _dev.models:

==================================
An introduction to Django models
==================================

.. contents::
    :depth: 1
    :local:


Lino applications fully use Django's ORM.

In this tutorial we are going to use the
:mod:`lino_book.projects.tables` demo application:

>>> from lino import startup
>>> startup('lino_book.projects.tables.settings')
>>> from lino.api.doctest import *
    

In Django, any subclass of :class:`Model` describes a *database
table*.  Every row of the table is an *instance* of its corresponding
*model*.  You can create a new row by saying::

Models are defined in a file whose name should be :xfile:`models.py`.

Here is our :xfile:`models.py` file:

.. literalinclude:: ../../lino_book/projects/tables/models.py


.. initialize the database:

    >>> from atelier.sheller import Sheller
    >>> shell = Sheller(settings.SITE.project_dir)
    >>> shell('python manage.py prep --noinput')
    `initdb demo` started on database /media/dell1tb/work/book/lino_book/projects/tables/default.db.
    Operations to perform:
      Synchronize unmigrated apps: about, bootstrap3, extjs, jinja, lino_startup, staticfiles, tables
      Apply all migrations: (none)
    Synchronizing apps without migrations:
      Creating tables...
        Creating table tables_author
        Creating table tables_book
        Running deferred SQL...
    Running migrations:
      No migrations to apply.
    Loading data from /media/dell1tb/work/book/lino_book/projects/tables/fixtures/demo.py
    Installed 7 object(s) from 1 fixture(s)


In a Lino application you can now say:                    

>>> from lino_book.projects.tables.models import Author
>>> obj = Author(first_name="Joe", last_name="Doe")

That row is not yet stored in the database, but you can use it.

For example you can access the individual fields:

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


The :attr:`objects` class attribute of a model
is used for certain
operations which require a *queryset*.


>>> Author.objects.count()
3

>>> Author.objects.all()
<QuerySet [Author #1 ('Adams, Douglas'), Author #2 ('Camus, Albert'), Author #3 ('Huttner, Hannes')]>


>>> obj.save()
>>> Author.objects.all()
<QuerySet [Author #1 ('Adams, Douglas'), Author #2 ('Camus, Albert'), Author #3 ('Huttner, Hannes'), Author #4 ('Woe, Joe')]>


>>> qs = Author.objects.filter(first_name="Joe")

>>> qs.count()
1
>>> qs
<QuerySet [Author #4 ('Woe, Joe')]>


The :attr:`_meta`


>>> obj.delete()
>>> Author.objects.count()
3
  
 

Tim Kholod wrote a nice introduction for beginners: `The simple way to
understand Django models <https://arevej.me/django-models/>`__
