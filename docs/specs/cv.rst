.. doctest docs/specs/cv.rst
.. _lino.tested.cv:

==================================
Career module (tested)
==================================


.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.max.settings.demo')
    >>> from lino.api.doctest import *

.. contents:: 
   :local:
   :depth: 2


>>> UserTypes = rt.models.users.UserTypes
>>> AllLanguageKnowledges = rt.models.cv.AllLanguageKnowledges

>>> rt.show(UserTypes)
======= =========== =============== =====================================
 value   name        text            User role
------- ----------- --------------- -------------------------------------
 000     anonymous   Anonymous       lino.core.roles.UserRole
 100     user        User            lino_xl.lib.xl.user_types.SiteUser
 900     admin       Administrator   lino_xl.lib.xl.user_types.SiteAdmin
======= =========== =============== =====================================
<BLANKLINE>

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
