.. doctest docs/specs/cv.rst
.. _lino.tested.cv:

==================================
The Career plugin
==================================

The :mod:`lino_xl.lib.cv` plugin adds functionality to manage
career-related information about a client which can be used for
example to generate a CV.

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.max.settings.demo')
    >>> from lino.api.doctest import *

.. contents:: 
   :local:
   :depth: 2


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
