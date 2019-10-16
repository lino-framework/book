.. doctest docs/specs/ssin.rst
.. _xl.specs.ssin:

==================================================
``ssin`` : Belgian national identification numbers
==================================================

The :mod:`lino.utils.ssin` module defines some utilities for
manipulating *Belgian national identification numbers*.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> # lino.startup('lino.projects.std.settings_test')
>>> startup('lino_book.projects.min1.settings.doctests')
>>> from lino.api.doctest import *

Which means that code examples in this document use the
:mod:`lino_book.projects.min1` demo project.

We will also use some additional Python modules:

>>> import datetime

Overview
=========

Belgians call their national identification number **INSZ**
("identificatienummer van de sociale zekerheid) in Dutch, **NISS**
("No. d'identification de Sécurité Sociale") in French or **INSS**
("Identifizierungsnummer der Sozialen Sicherheit") in German.  We use
the English abbreviation **SSIN** ("Social Security Identification
Number"), though some sources also speak about **INSS**
("Identification Number Social Security").

See also

- the Wikipedia articles about `Belgian national identification
  numbers
  <http://en.wikipedia.org/wiki/National_identification_number#Belgium>`__,
  `Numéro de registre national
  <http://fr.wikipedia.org/wiki/Num%C3%A9ro_de_registre_national>`_
  and `Rijksregisternummer
  <http://nl.wikipedia.org/wiki/Rijksregisternummer>`_

- http://www.ibz.rrn.fgov.be/fileadmin/user_upload/Registre/Acces_RN/RRNS003_F_IV.pdf
- http://www.simplification.fgov.be/doc/1206617650-4990.pdf


.. currentmodule:: lino.utils.ssin

Formatting
==========

The module defines the functions :func:`format_ssin` and
:func:`new_format_ssin`.

>>> from lino.utils.ssin import Genders
>>> from lino.utils.ssin import format_ssin, new_format_ssin

An officialy obsolete but still used format for printing a Belgian
SSIN is ``YYMMDDx123-97``, where ``YYMMDD`` is the birth date, ``x``
indicates the century (``*`` for the 19th, a *space* for the 20th and
a ``=`` for the 21st century), ``123`` is a sequential number for
persons born the same day (odd numbers for men and even numbers for
women), and ``97`` is a check digit (remainder of previous digits
divided by 97).

Validation
==========

The module defines two validator functions, :func:`is_valid_ssin` and
:func:`ssin_validator`.

>>> from lino.utils.ssin import ssin_validator, is_valid_ssin

The difference between them is that one returns True or False while
the other raises a ValidationError to be used in Django forms.  The
message of this ValidationError depends on the user language.

>>> ssin_validator('123') #doctest: +NORMALIZE_WHITESPACE +IGNORE_EXCEPTION_DETAIL +ELLIPSIS
Traceback (most recent call last):
...
ValidationError: [u'Invalid SSIN 123 : A formatted SSIN must have 13 positions']

>>> is_valid_ssin('123')
False


Generating fictive SSIN
=======================

The module also defines a function :func:`generate_ssin` is mainly
used to generate fictive demo data.  For example, here is the national
number of the 25th boy born in Belgium on June 1st, 1968:

Examples:

>>> from lino.utils.ssin import generate_ssin

>>> n = generate_ssin(datetime.date(1968, 6, 1), Genders.male, 53)
>>> print(n)
680601 053-29
>>> ssin_validator(n)

The sequence number is optional and the default value depends on
the gender.  For boys it is 1, for girls 2.

>>> n = generate_ssin(datetime.date(2002, 4, 5),Genders.female)
>>> print(n)
020405 002=44
>>> ssin_validator(n)

>>> n = generate_ssin(datetime.date(1968, 7, 21), Genders.male, 13)
>>> print(n)
680721 013-58
>>> ssin_validator(n)


SSIN for incomplete birth date
==============================

Here is the SSIN of a person with incomplete birth date:

>>> from lino.utils import IncompleteDate
>>> n = generate_ssin(IncompleteDate(1995, 0, 0), Genders.male, 153)
>>> print (n)
950000 153-96
>>> ssin_validator(n)


No need for special characters?
===============================

In 1983 Belgians discovered that the formatting with a special
character to indicate the century is not absolutely required since the
national register no longer cared about people born before 1900, and
now the century can be deduced by trying the check digits.

>>> format_ssin('68060105329')
'680601 053-29'

In order to say whether the person is born in 19xx or 20xx, we need to
look at the check digits.

For example, the 25th boy born on June 1st in **1912** will get
another check-digit than a similar boy exactly 100 years later (in
**2012**):

>>> format_ssin('12060105317')
'120601 053-17'

>>> format_ssin('12060105346')
'120601 053=46'

Question to mathematicians: is it sure that there is no combination of
birth date and sequence number for which the check digits are the
same?
