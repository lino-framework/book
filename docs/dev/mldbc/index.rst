.. doctest docs/dev/mldbc/mo
.. _mldbc_tutorial:

=============================
Multilingual database content
=============================

..  doctest init:
    >>> from lino import startup
    >>> startup('lino_book.projects.mldbc.settings')
    >>> from lino.api.doctest import *
    >>> Product = rt.models.mldbc.Product


One feature of Lino is its built-in support for :ref:`single-table
multilingual database content <mldbc>`.  This tutorial explains what
it is.

Note that we are **not** talking about Internationalization (i18n) here.
*Internationalization* is when the :term:`front end` can speak different
languages. Lino has nothing to add to the existing Django techniques about
`Internationalization <https://docs.djangoproject.com/en/2.2/topics/i18n/>`__,
that's why we deliberately didn't add :mod:`lino.modlib.users` and front end
translation in this tutorial.


When to use BabelFields
-----------------------

Imagine a Canadian company which wants to print catalogs and price
offers in an English and a French version, depending on the customer's
preferred language.  They don't want to maintain different product
tables because it is one company, one accounting, and prices are the
same in French and in English.  They need a Products table like this:

  +------------------+------------------+-------------+-------+----+
  | Designation (en) | Designation (fr) | Category    | Price | ID |
  +==================+==================+=============+=======+====+
  | Chair            | Chaise           | Accessories | 29.95 | 1  |
  +------------------+------------------+-------------+-------+----+
  | Table            | Table            | Accessories | 89.95 | 2  |
  +------------------+------------------+-------------+-------+----+
  | Monitor          | Écran            | Hardware    | 19.95 | 3  |
  +------------------+------------------+-------------+-------+----+
  | Mouse            | Souris           | Accessories |  2.95 | 4  |
  +------------------+------------------+-------------+-------+----+
  | Keyboard         | Clavier          | Accessories |  4.95 | 5  |
  +------------------+------------------+-------------+-------+----+

Now imagine that your application is being used not only in Canada but also in
the United States.  Your US customers don't want to have a "useless" column for
the French designation of their products.

This is where you want multi-lingual database content. In that case you would
simply

- use :class:`BabelCharField <lino.utils.mldbc.fields.BabelCharField>`
  instead of Django's :class:`CharField` for every translatable field and

- set the :attr:`languages <lino.core.site.Site.languages>` attribute to
  ``"en"`` for your US customer and to ``"en fr"`` for your Canadian customer.

An example
==========

If you have installed a :term:`contributor environment` (see
:ref:`contrib.install`), then you can run the following examples on your
computer.


Go to :mod:`lino_book.projects.mldbc`::

   $ go mldbc

Make sure that the demo database is initialized::

   $ python manage.py prep


Using the shell
---------------

Now open the interactive Django shell::

  $ python manage.py shell

You can print a catalog in different languages:

>>> print(', '.join([str(p) for p in Product.objects.all()]))
Chair, Table, Monitor, Mouse, Keyboard, Consultation

>>> from django.utils import translation
>>> with translation.override('fr'):
...     print(', '.join([str(p) for p in Product.objects.all()]))
Chaise, Table, Ecran, Souris, Clavier, Consultation

Here is how we got the above table:

>>> from lino.api import rt
>>> rt.show(mldbc.Products)
==================== ================== ============= ============
 Designation          Designation (fr)   Category      Price
-------------------- ------------------ ------------- ------------
 Chair                Chaise             Accessories   29,95
 Table                Table              Accessories   89,95
 Monitor              Ecran              Hardware      19,95
 Mouse                Souris             Accessories   2,95
 Keyboard             Clavier            Accessories   4,95
 Consultation         Consultation       Service       59,95
 **Total (6 rows)**                                    **207,70**
==================== ================== ============= ============
<BLANKLINE>



Using the web interface
-----------------------

.. code-block:: bash

  $ go mldbc
  $ python manage.py prep
  $ python manage.py runserver
  Analyzing Tables...
  Analyze 0 slave tables...
  Discovering choosers for model fields...
  Analyzing Tables...
  Analyze 0 slave tables...
  Discovering choosers for model fields...
  Watching for file changes with StatReloader
  Performing system checks...

  System check identified no issues (0 silenced).
  November 05, 2019 - 07:32:06
  Django version 2.2.6, using settings 'lino_book.projects.mldbc.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.


Screenshots
-----------

The screenshots on the left have been taken on a server with
``languages = ['en']``,
those on the right on a server with
``languages = ['de','fr']``.


.. image:: babel1a.jpg
    :scale: 50

.. image:: babel1b.jpg
    :scale: 50

.. image:: babel2a.jpg
    :scale: 50

.. image:: babel2b.jpg
    :scale: 50

.. image:: babel3a.jpg
    :scale: 50

.. image:: babel3b.jpg
    :scale: 50


The :xfile:`settings.py` file
-----------------------------

.. literalinclude:: /../../book/lino_book/projects/mldbc/settings.py

This is where you specify the :setting:`languages` setting.


The :xfile:`models.py` file
---------------------------

.. literalinclude:: /../../book/lino_book/projects/mldbc/models.py

Note that this is the first time we use a
:class:`dd.ChoiceList <lino.core.choicelists.ChoiceList>`
they deserve another tutorial on their own.


The `demo` fixture
------------------

.. literalinclude:: /../../book/lino_book/projects/mldbc/fixtures/demo.py

Note how the application developer doesn't know which :attr:`languages
<lino.core.site.Site.languages>` will be set at runtime.

Of course the fixture above supposes a single person who knows
all the languages, but that's just because we are simplifying.
In reality you can do it as sophisticated as you want,
reading the content from different sources.

BabelFields and migrations
==========================

BabelFields cause the database structure to change when a :term:`site
maintainer` locally changes the :attr:`languages
<lino.core.site.Site.languages>` setting of a :term:`Lino site`.

That's why the :term:`application carrier` cannot provide Django migrations for
their product.
See :doc:`/dev/datamig` and :doc:`/specs/migrate`.


Related work
------------

- `django-datatrans <https://pypi.python.org/pypi/django-datatrans>`_ (Jef Geskens)
- `django-localeurl <https://pypi.python.org/pypi/django-localeurl>`_ (Carl Meyer)
- `django-transmeta <https://pypi.python.org/pypi/django-transmeta>`_ (Marc Garcia, Manuel Saelices, Pablo Martin)

TODO: write comparisons about these
