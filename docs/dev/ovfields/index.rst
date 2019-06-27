.. doctest docs/dev/ovfields/index.rst
.. _dev.ovfields:

=========================
Overriding virtual fields
=========================

While it is okay to override a database field by a virtual field, the opposite
is not true.  To avoid this pitfall, Lino raises a ChangedAPI exception when
this happens.

It is not allowed to override a virtual field inherited from a parent by a
database field. Django doesn't know about Lino's virtual fields and doesn't
complain, but when you then try to get the value of the database field, Python
will call the virtual field method and give you this value.

The :mod:`lino_book.projects.ovfields` demo application shows this by defining
the following database model:

.. literalinclude:: /../../book/lino_book/projects/ovfields/models.py


>>> from lino import startup
>>> startup('lino_book.projects.ovfields.settings')
Traceback (most recent call last):
  ...
lino.core.exceptions.ChangedAPI: CharField field ovfields.MyModel.foo hidden by virtual field of same name.
