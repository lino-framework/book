.. doctest docs/dev/combo/index.rst
.. _lino.dev.combo:

===========================
Introduction to Combo boxes
===========================

A **combo box** is a widget used to edit a field that can have a number of
choices.  See also :doc:`/dev/radiobuttons`.

This unit uses the :mod:`lino_book.projects.combo` project to show how
to define dynamic lists of choices for a combobox field in a Lino
application.


All related fields and choice lists are rendered in lino using a combo box.
This component allows for a selection of a single choice from a dropdown.
It also supports tying of a query to filter the choices.


.. contents::
    :depth: 1
    :local:


Filtering results
=================

Filtering is done via setting :attr:`Model.quick_search_fields`, or by overriding
:meth:`Model.quick_search_filter`.


Context-sensitive Comboboxes
============================

More examples and info can be seen here :ref:`dev.choosers`

The challenge is old: when you have two fields on a model (here
`country` and `city` on the `Person` model) and you want the choices
for one of these field (here `city`) to depend on the value of the
other field (here `country`), then you need a hack because Django has
no built-in API for producing this behaviour.

The Lino solution is you simply define the following function on the
`Person` model::

    @dd.chooser()
    def city_choices(cls, country):
        return rt.models.combo.City.objects.filter(country=country)

Lino finds all choosers at startup that are decorated with the
:func:`dd.chooser <lino.utils.chooser>` decorator (which turns it into
a "chooser" object) and has a name of the form.

Lino matches it to the field using the fieldname in`<fieldname>_choices``.
Lino matches the context related fields by positional argument named the
same as other fields.
`ar` is also a valid argument name for the chooser. The value will be the
action request used in the API call. The request object can be used to

Then Lino then does the dirty work of generating appropriate JavaScript
and HTML code and the views which respond to the AJAX calls.


.. _learning_combos:

Learning Comboboxes
-------------------

When the model also defines a method ``create_<fieldname>_choice``, then the
chooser will become "learning": the ComboBox will be told to accept
also new values, and the server will handle these cases accordingly.

In the example application you can create new cities by simply typing
them into the combobox. ::

    class Person(dd.Model):
        ...
        def create_city_choice(self, text):
            """
            Called when an unknown city name was given.
            Try to auto-create it.
            """
            if self.country is not None:
                return rt.models.countries.Place.lookup_or_create(
                    'name', text, country=self.country)

            raise ValidationError(
                "Cannot auto-create city %r if country is empty", text)



Screenshots
===========

.. image:: 1.png

.. image:: 2.png

.. image:: 3.png


Other files
===========

Here is the :xfile:`models.py` file :

.. literalinclude:: /../../book/lino_book/projects/combo/models.py

Here are the other files used in this unit.

The :xfile:`desktop.py` file specifies a table for every model:

.. literalinclude:: /../../book/lino_book/projects/combo/desktop.py

The :xfile:`__init__.py` file specifies how the tables are organized
in the main menu:

.. literalinclude:: /../../book/lino_book/projects/combo/__init__.py

Here is the project's :xfile:`settings.py` file :

.. literalinclude:: /../../book/lino_book/projects/combo/settings.py

And finally the :file:`fixtures/demo.py` file contains the data we use
to fill our database:

.. literalinclude:: /../../book/lino_book/projects/combo/fixtures/demo.py


Exercise
========

The files we are going to use in this tutorial are already on your
hard disk in the :mod:`lino_book.projects.combo` package.

Start your development server and your browser, and have a look at the
application::

  $ go combo
  $ python manage.py runserver

Explore the application and try to extend it: change things in the
code and see what happens.


Discussion
==========

This is inspired by Vitor Freitas' blog post `How to
Implement Dependent/Chained Dropdown List with Django
<https://simpleisbetterthancomplex.com/tutorial/2018/01/29/how-to-implement-dependent-or-chained-dropdown-list-with-django.html>`__.


.. TODO: document chooser options and choosers on other fields than
   foreign keys.
   TODO: compare with `django-ajax-selects
   <https://github.com/crucialfelix/django-ajax-selects>`_

Doctests
========

The remaining samples are here in order to test the project.

>>> from lino import startup
>>> startup('lino_book.projects.combo.settings')
>>> from lino.api.doctest import *

>>> rt.show('combo.Cities')
==== ========= ==========
 ID   Country   name
---- --------- ----------
 1    Belgium   Eupen
 2    Belgium   Brussels
 3    Belgium   Gent
 4    Belgium   Raeren
 5    Belgium   Namur
 6    Estonia   Tallinn
 7    Estonia   Tartu
 8    Estonia   Vigala
==== ========= ==========
<BLANKLINE>
