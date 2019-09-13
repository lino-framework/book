.. doctest docs/specs/cv.rst
.. _lino.tested.cv:

================================================
``cv`` : Managing career-related data of clients
================================================

.. currentmodule:: lino_xl.lib.cv

The :mod:`lino_xl.lib.cv` plugin adds functionality for managing career-related
information about a client which can be used for example to generate a CV (a
*curriculum vitae*).

.. contents::
   :depth: 1
   :local:


Concepts
========

.. glossary::

  Language knowledge

    The fact that a given person knows a given language at a given degree.

    Database model: :class:`LanguageKnowledge`

- An **education** entry (fr: Éducation, de: Bildung) is when a given
  person has followed lessons in a given *school* for a given
  *period*.  There are two basic types of education: **studies** (fr:
  Études, de: Studium) and **trainings** (fr: Formation, de:
  Ausbildung).

- A **Work experience** (fr: Expérience professionnelle, de:
  Berufserfahrung) is when a given person has worked in a given
  *organisation* for a given *period*.



.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.max.settings.demo')
>>> from lino.api.doctest import *



>>> UserTypes = rt.models.users.UserTypes
>>> AllLanguageKnowledges = rt.models.cv.AllLanguageKnowledges

>>> a = UserTypes.admin
>>> a
users.UserTypes.admin:900

>>> u = UserTypes.user
>>> u
users.UserTypes.user:100

>>> AllLanguageKnowledges.required_roles == {cv.CareerStaff}
True

>>> AllLanguageKnowledges.default_action.get_view_permission(u)
False

>>> AllLanguageKnowledges.default_action.get_view_permission(a)
False



.. class:: LanguageKnowledge

  Django model to represent a :term:`Language knowledge`.

  .. attribute:: person

    The person to which this entry applies.

  .. attribute:: language

    The language to which this entry applies.

  .. attribute:: spoken
  .. attribute:: written
  .. attribute:: spoken_passively
  .. attribute:: written_passively
  .. attribute:: native
  .. attribute:: cef_level

    The CEF level. A pointer to a choice of :class:`CefLevels`

  .. attribute:: has_certificate

    Whether this entry is confirmed by a certificate.

  .. attribute:: entry_date

    When this entry was created.
