.. _dev.choosers:

================
Chooser examples
================

:ref:`lino.dev.combo`

Examples in this document use the :mod:`lino_book.projects.chooser` demo
project.

>>> from lino import startup
>>> startup('lino_book.projects.chooser.settings')
>>> from lino.api.doctest import *


>>> be = chooser.Country.objects.get(name="Belgium")
>>> fr = chooser.Country.objects.get(name="France")


You instantiate a chooser by specifying a model and a fieldname.
The fieldname must be the name of a field that has been defined in your model.
A chooser for a field FOO on a model will look whether the model defines a class method FOO_choices().

Choosers on ForeignKey fields
=============================

A Contact has ForeignKey fields to Country and City.
In an entry form for a Contact you want only the cities of that country when selecting a city.

How to use a Chooser on a ForeignKey:

>>> from lino.core.utils import get_field
>>> city = chooser.Contact.get_chooser_for_field('city')
>>> [str(o) for o in city.get_choices(country=be)]
['Brussels', 'Eupen', 'Gent']

>>> [str(o) for o in city.get_choices(country=fr)]
['Bordeaux', 'Paris']

>>> [str(o) for o in city.get_choices()]
['Bordeaux', 'Brussels', 'Eupen', 'Gent', 'Narva', 'Paris', 'Tallinn', 'Tartu']

There is no method `country_choices`, so `Contact.country` has no Chooser:

>>> print(chooser.Contact.get_chooser_for_field('country'))
None


Char field choosers
===================

How to make and use a chooser on a char-field, to limit the valid values:

.. literalinclude:: /../../book/lino_book/projects/chooser/food.py

>>> food = chooser.Contact.get_chooser_for_field('food')

>>> [str(o) for o in food.get_choices()]
['Potato', 'Vegetable', 'Meat', 'Fish']

>>> [str(o) for o in food.get_choices(year_in_school='FR')]
['Potato']

>>> [str(o) for o in food.get_choices(year_in_school='SO')]
['Potato', 'Vegetable']

Choosers that depend on current user
====================================

Sometimes you require the current user to determine the choices for a field.
To do this include a "ar" parameter to your chooser method:

.. literalinclude:: /../../book/lino_book/projects/chooser/ar_chooser.py

>>> ses = rt.login("robin")
... #doctest: +SKIP
>>> [str(o) for o in food.get_choices(ar=ses)]
... #doctest: +SKIP
['Potato', 'Vegetable']

Not that this example doesn't work in our choices demo as there are no users.
This tests assumes that the user model has a year_in_school field.

This use case would be required if users are submitting what food they want
to eat during the week on a separate table.

Learning foreignkey fields
==========================

.. glossary::

  Learning foreignkey field

    The :term:`application developer` can turn any foreign key field that has a
    chooser into a learning foreign key by defining a :meth:`create_FOO_choice`
    method on the model.

Examples:

The :attr:`city <lino_xl.lib.countries.CountryCity.city>` field of the address
of a :class:`lino_xl.lib.countries.CountryCity` (e.g. of a partner). When you
specify a country and then discover that the city does not yet exist, you simply
leave the "invalid" city name in the combobox (Lino accepts it) and save the
partner. Lino will then silently create a city of that name.


Or the :attr:`lino_xl.lib.contacts.Role.person` field.  You can see the new
feature in every application with contacts.  For example
:mod:`lino_book.projects.min1`. In the detail of a company, you have the
:class:`RolesByCompany <lino_xl.lib.contacts.RolesByCompany>` slave table. In
the Person column of that table you can type the name of a person that does
not yet exist in the database.  Lino will create it silently, and you can then
click on the pointer to edit more information.

You can disable a :term:`learning foreignkey field` by setting the
:attr:`lino.core.model.Model.disable_create_choice` model attribute to `True`.


Special cases
=============

Note that `Chooser.get_choices()` ignores any unused keyword arguments:

>>> [str(o) for o in city.get_choices(country=be, foo=1, bar=True, baz='7')]
['Brussels', 'Eupen', 'Gent']


Examples of choosers on a ChoiceListField are

- :attr:`lino_xl.lib.countries.Place.type`
- :attr:`lino_xl.lib.contacts.Partner.vat_regime`
