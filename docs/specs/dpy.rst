.. _dpy:

The Python serializer
=====================

The :mod:`lino.utils.dpy` module defines Lino's **Python serializer
and deserializer**, which is used for :doc:`writing and loading demo
data </dev/pyfixtures/index>`, :doc:`making backups </dev/dump2py>` and
:doc:`migrating </dev/datamig>` databases.

Concept and implementation is one of the important concepts which Lino
adds to a Django project. It is fully the author's work, and we didn't
yet find a similar approach in any other framework [#notnew]_.  In
March 2009 Luc suggested to merge it into Django or make it available
outside of Lino as well (`#10664
<http://code.djangoproject.com/ticket/10664>`__), but that idea is
sleeping since then.

A **serializer** is run by the :manage:`dumpdata` command and writes
data into a file which can be used as a fixture.  A **deserializer**
is run by :manage:`loaddata` and loads fixtures into the database.

Basic idea:

When a Lino application starts up, it sets your `SERIALIZATION_MODULES
<https://docs.djangoproject.com/en/1.11/ref/settings/#serialization-modules>`_
setting to `{"py" : "lino.utils.dpy"}`.  This tells Django to
associate the `.py` ending to the :class:`lino.utils.dpy.Deserializer`
class when loading ("deserializing") fixtures.

This deserializer` expects every Python fixture to define a global
function `objects` which it expects to return (or `yield
<http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained>`_)
the list of model instances to be added to the database.
  
.. rubric:: Footnotes

.. [#notnew] Though the basic idea of using Python language to
    describe data collections is not new.  For example Limodou
    published a Djangosnippet in 2007 which does something similar:
    `db_dump.py - for dumping and loading data from database
    <http://djangosnippets.org/snippets/14/>`_.  Or `Why using
    factories in Django
    <http://eatsomecode.com/why-using-factories-in-django>`__.
