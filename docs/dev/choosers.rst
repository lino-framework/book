.. _dev.choosers:

========================
Introduction to choosers
========================


The :mod:`lino_book.projects.chooser` demo project.

>>> from lino import startup
>>> startup('lino_book.projects.chooser.settings')
>>> from lino.api.doctest import *


>>> be = chooser.Country.objects.get(name="Belgium")
>>> fr = chooser.Country.objects.get(name="France")


You instantiate a chooser by specifying a model and a fieldname.
The fieldname must be the name of a field that has been defined in your model.
A chooser for a field FOO on a model will look whether the model defines a class method FOO_choices().

Situation 1
===========

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


Situation 2
===========

How to use a Chooser on a field with choices:

>>> food = chooser.Contact.get_chooser_for_field('food')

>>> [str(o) for o in food.get_choices()]
['Potato', 'Vegetable', 'Meat', 'Fish']

>>> [str(o) for o in food.get_choices(year_in_school='FR')]
['Potato']

>>> [str(o) for o in food.get_choices(year_in_school='SR')]
['Potato', 'Vegetable', 'Meat', 'Fish']


Special cases
=============

Note that `Chooser.get_choices()` ignores any unused keyword arguments:

>>> [str(o) for o in city.get_choices(country=be,foo=1,bar=True,baz='7')]
['Brussels', 'Eupen', 'Gent']




Examples of choosers on a ChoiceListField are

- :attr:`lino_xl.lib.countries.Place.type`
- :attr:`lino_xl.lib.contacts.Partner.vat_regime`




