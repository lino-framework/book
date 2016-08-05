Jargon
=============



.. _pk:

primary key
-----------

The **primary key** of a database table (which we call "Model" in
Lino) is one of it fields which holds the unique identification of
each row.  This field is often not shown to the user.

.. _gfk:

GenericForeignKey
-----------------

See `Django docs
<https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey>`_

.. _ise:

Internal Server Error
---------------------

When an exception occurs that is not catched, then Lino behaves like 
any Django application and return a HTTP return code 500.


.. _admin:

System administrator
--------------------

A system administrator is a person who installs an existing Lino application.
He or she doesn't need to write Python code except for the :xfile:`settings.py` 
file.

.. _dev:

Lino application developer
--------------------------

A Lino application developer is a Python programmer who uses Lino while 
writing his own application.


.. _install_requires:

install_requires
----------------

See http://python-packaging.readthedocs.io/en/latest/dependencies.html



.. _book:

The Lino Book
-------------

The Lino Book is a repository used for educational and testing
purposes.  It contains the big Sphinx documentation tree about the
Lino framework (published on http://www.lino-framework.org/).

It contains also the :mod:`lino_book` Python package which contains
nothing but a set of example Lino applications.

The code repositories for :mod:`lino` and :mod:`lino_xl` (the Python
packages) have no documentation tree on their own, their documentation
and many tests are done in :ref:`book`.


