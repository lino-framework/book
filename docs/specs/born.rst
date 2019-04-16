.. doctest docs/specs/born.rst
.. _lino.specs.born:

==================
The ``Born`` mixin
==================

.. currentmodule:: lino.mixins.human

This document explains the :class:`lino.mixins.human.Born` model mixin which
defines a database field :attr:`Born.birth_date` and a virtual field
:attr:`Born.age`.


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst
             
>>> import lino
>>> lino.startup('lino_book.projects.human.settings')
>>> from lino.api.doctest import *
>>> from django.db.models import Q
>>> from lino_book.projects.human.models import Person
>>> from lino.modlib.system.choicelists import Genders
>>> from django.utils import translation


This tutorial uses the same demo database as :doc:`human` (see there for more
explanations).


The age of a human
==================

For the following examples, we will set :attr:`the_demo_date
<lino.core.site.Site.the_demo_date>` in order to have reproducible test cases.
At the end of this page we will need to restore the demo date to its original
value, which is `None`:

>>> print(settings.SITE.the_demo_date)
None

We define a utility function for our tests:

>>> def test(birth_date, today):
...    settings.SITE.the_demo_date = i2d(today)
...    p = Person(birth_date=birth_date)
...    p.full_clean()
...    print(p.age)
...    settings.SITE.the_demo_date = None

Here we go.

A person born on April 5, 2002 was 16 years old on June 11, 2018:

>>> test("2002-04-05", 20180611)
16 years

When you get 16 years old tomorrow, then today you are still 15:

>>> test("2002-04-05", 20180404)
15 years

You start being 16 on your birthday.

>>> test("2002-04-05", 20180405)
16 years

For **children younger than 5 years** Lino adds the number of months:

>>> test("2018-03-01", 20180611)
0 years 3 months

Lino respects the **singular forms**:

>>> test("2017-05-01", 20180611)
1 year 1 month


Incomplete birth dates
======================

The birth date is an instance of :class:`lino.utils.IncompleteDate`. Yes, there
are people who don't know their exact birth date.

>>> test("2002-05-00", 20180611)
±16 years

>>> test("2002-00-00", 20180611)
±15 years

If you say only your birth day but not the year, then we don't know your age:

>>> test("0000-06-01", 20180611)
unknown

Other languages
===============

The age is **translated text**:

>>> with translation.override('de'):
...    test("2018-03-01", 20180611)
0 Jahre 3 Monate

>>> with translation.override('de'):
...    test("2017-05-01", 20180611)
1 Jahr 1 Monat

>>> with translation.override('fr'):
...    test("2017-05-01", 20180611)
1 an 1 mois

>>> with translation.override('fr'):
...    test("0000-05-01", 20180611)
inconnu

The leap year bug
=================

In April 2019 Steve reported :ticket:`2946`: Lino was saying 35 years as age of a
person whose birth date was 10.04.1984 when today is 04.04.2019. Which is wrong.
The person will get 35 only in 6 days.  So today she is 34:

>>> test("1984-04-10", 20190404)
34 years

It is now correct since the bug is fixed.  We added some more test cases

>>> test("2002-04-05", 20180403)
15 years
>>> test("2002-04-05", 20180402)
15 years
>>> test("2002-04-05", 20180401)
15 years
>>> test("2002-04-05", 20180331)
15 years

The explanation was that each leap year caused one day of difference. In our
case the leap years were 2004, 2008 and 2012 and 2016, so Lino starts saying 16
4 days before your birthday:


