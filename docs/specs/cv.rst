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
