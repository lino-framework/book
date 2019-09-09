.. _lino.tutorial.auto_create:

================================================
`lookup_or_create` and the `auto_create` signal
================================================

.. This document is part of the test suite.  To test only this
   document, run::

     $ cd lino_book/projects/auto_create
     $ python manage.py test

This document describes and tests the
:meth:`lookup_or_create <lino.core.model.Model.lookup_or_create>`
method and the
:attr:`auto_create <lino.core.signals.auto_create>` signal.
I wrote it primarily to reproduce and test the
"NameError / global name 'dd' is not defined"
on :blogref:`20130311`.

We define a single simple model and a handler for the auto_create signal:

.. literalinclude:: models.py

>>> from lino_book.projects.auto_create.models import Tag

..
  20190909 : for some reason (maybe inside Django) we have to define the
  receiver in the models.py file

Manually create a Tag:

>>> Tag(name="Foo").save()

A first call to `lookup_or_create`:

>>> Tag.lookup_or_create("name", "Foo")
Tag #1 ('Foo')

The signal was not emitted here because the Foo tag existed before.

>>> print(Tag.lookup_or_create("name", "Bar"))
My handler was called with Bar
Bar

>>> print(list(Tag.objects.all()))
[Tag #1 ('Foo'), Tag #2 ('Bar')]

Voilà, that's all for the moment.
