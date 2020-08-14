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

The models of an application are always defined in a file named
:xfile:`models.py`.  Here is the :xfile:`models.py` file we are going to use in
this tutorial:

.. literalinclude:: /../../book/lino_book/projects/tables/models.py

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

For example you can *count* how many authors are stored in our database.

>>> Author.objects.count()
3

Or you can loop over them:

>>> for a in Author.objects.all():
...     print(a)
Adams, Douglas
Camus, Albert
Huttner, Hannes


You can create a new author by saying:

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
>>> author.full_clean() #doctest: +NORMALIZE_WHITESPACE +IGNORE_EXCEPTION_DETAIL +ELLIPSIS
Traceback (most recent call last):
...
ValidationError: {'last_name': [u'This field cannot be blank.']}

Note that Django complains only when we call :meth:`full_clean` (not already
when instantiating the model).

Note that the :attr:`country` field is declared with `blank=True`, so
this field is optional.

The :class:`ValidationError` is a special kind of exception, which
contains a dictionary that can contain one error message for every
field. In the Book model we have three mandatory fields: the
:attr:`title`, the :attr:`price` and the year of publication
(:attr:`published`).  Giving only a title is not enough:

>>> book = Book(title="Foo")
>>> book.full_clean() #doctest: +NORMALIZE_WHITESPACE +IGNORE_EXCEPTION_DETAIL +ELLIPSIS
Traceback (most recent call last):
...
ValidationError: {'price': [u'This field cannot be null.'], 'published': [u'This field cannot be null.']}


The :class:`Book` model also shows how you can define custom validation rules
that may depend on complex conditions which involve more than one
field.

>>> book = Book(title="Foo", published=2001, price='4.2')
>>> book.full_clean() #doctest: +NORMALIZE_WHITESPACE +IGNORE_EXCEPTION_DETAIL +ELLIPSIS
Traceback (most recent call last):
...
ValidationError: [u'A book from 2001 for only $4.20!']


More about Django models
========================

Tim Kholod wrote a nice introduction for beginners: `The simple way to
understand Django models <https://arevej.me/django-models/>`__

If you want to know more about Django's way to access the database
using models, read the Django documentation about
`Models and databases
<https://docs.djangoproject.com/en/3.1//topics/db/>`__.


Lino extends the Django model
=============================

Lino adds a series of features to Django's `Model
<https://docs.djangoproject.com/en/3.1/ref/models/class/>`_ class.   In a Lino
application you will define your models as subclasses of
:class:`lino.core.model.Model` (usually referred as :class:`dd.Model`), which is
a subclass of Django's :class:`django.db.models.Model` class.

When a Lino application imports plain Django Model classes, Lino will "extend"
these by adding the attributes and methods defined here to these classes.

.. currentmodule:: lino.core.model

Standard virtual fields
=======================

Lino adds some virtual fields that you can use in your layouts:

.. attribute:: Model.overview

    A fragment of HTML describing this object in a customizable story of
    paragraphs.

    Customizable using :meth:`Model.get_overview_elems`.

.. attribute:: Model.detail_link

    A virtual field which displays this database row as a clickable link
    which opens the detail window.  Functionally equivalent to a double
    click, but more intuitive in some places.

.. attribute:: Model.workflow_buttons

    A virtual field that displays the **workflow actions** for this row.  This
    is a compact but intuitive representation of the current workflow state,
    using a series of clickable actions.

Field-specific customization hooks
==================================

You can optionally define some field-specific customization hooks. `FOO` in this
section is the name of a database field defined on the same model (or on a
parent).

.. method:: Model.FOO_changed

  Called when field FOO of an instance of this model has been
  modified through the user interface.

  Example::

    def city_changed(self, ar):
        print("User {} changed city of {} to {}!".format(
            ar.get_user(), self, self.city))

  Note: If you want to know the old value when reacting to a change,
  consider writing :meth:`Model.after_ui_save` instead.

.. method:: Model.FOO_choices

  Return a queryset or list of allowed choices for field FOO.

  For every field named "FOO", if the model has a method called
  "FOO_choices" (which must be decorated by :func:`dd.chooser`),
  then this method will be installed as a chooser for this
  field.

  Example of a context-sensitive chooser method::

    country = dd.ForeignKey(
        'countries.Country', blank=True, null=True)
    city = dd.ForeignKey(
        'countries.City', blank=True, null=True)

    @chooser()
    def city_choices(cls,country):
        if country is not None:
            return country.place_set.order_by('name')
        return cls.city.field.remote_field.model.objects.order_by('name')


.. method:: Model.create_FOO_choice

  For every field named "FOO" for which a chooser exists, if the model
  also has a method called "create_FOO_choice", then this chooser will be
  a :term:`learning chooser`. That is, users can enter text into the
  combobox, and Lino will create a new database object from it.

  This works only if FOO is (1) a foreign key and (2) has a chooser.
  See also :term:`learning foreign key`.

.. method:: Model.get_choices_text(self, request, actor, field)

  Return the text to be displayed when an instance of this model
  is being used as a choice in a combobox of a ForeignKey field
  pointing to this model.
  `request` is the web request,
  `actor` is the requesting actor.

  The default behaviour is to simply return `str(self)`.

  A usage example is :class:`lino_xl.lib.countries.Place`.


.. method:: Model.disable_delete(self, ar=None)

  Decide whether this :term:`database object` may be deleted.  Return `None` if
  it is okay to delete this object, otherwise a nonempty translatable string
  with a message that explains in user language why this object cannot be
  deleted.

  The argument `ar` contains the :term:`action request` that is trying to
  delete. `ar` is possibly `None` when this is being called from a script or
  batch process.

  The default behaviour checks whether there are any related objects which would
  not get cascade-deleted and thus produce a database integrity error.

  You can override this method e.g. for defining additional conditions.
  Example::

    def disable_delete(self, ar=None):
        msg = super(MyModel, self).disable_delete(ar)
        if msg is not None:
            return msg
        if self.is_imported:
            return _("Cannot delete imported records.")

  When overriding, be careful to not skip the `super` method unless you know
  what you want.

  Note that :class:`lino.mixins.polymorphic.Polymorphic` overrides this.


How your model behaves in regard to other models:

- :attr:`Model.allow_cascaded_copy`
- :attr:`Model.allow_cascaded_delete`

Customize what happens when an instance is created:

- :attr:`Model.submit_insert`
- :attr:`Model.on_create`
- :attr:`Model.before_ui_save`
- :attr:`Model.after_ui_save`
- :attr:`Model.after_ui_create`
- :attr:`Model.get_row_permission`

Some methods you will use but not override:

- :attr:`Model.get_data_elem`
- :attr:`Model.add_param_filter`
- :attr:`Model.define_action`
- :attr:`Model.hide_elements`
