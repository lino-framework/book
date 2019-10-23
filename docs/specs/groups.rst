.. doctest docs/specs/groups.rst
.. _specs.groups:

=========================================
``groups`` : user groups
=========================================

.. currentmodule:: lino_xl.lib.groups

The :mod:`lino_xl.lib.groups` plugin adds the notions of :term:`users groups
<users group>` and :term:`user memberships <user membership>`.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.team.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q


Overview
========

.. glossary::

  Users group

    A named entity that holds a list of :term:`user memberships <user
    membership>`.

  User membership

    The fact that a given user is member of a given :term:`users group`.

Application developers can add a panel "Memberships"
(:class:`MembershipsByUser`) to the  detail window of
:class:`lino.modlib.users.User`.



In :ref:`noi` the verbose name of "Group" is changed to "Team".

>>> dd.plugins.groups.menu_group
'system'

>>> print(dd.plugins.groups.verbose_name)
Teams

>>> show_menu_path(groups.Groups)
Configure --> System --> Teams


Groups
======

>>> rt.show(groups.Groups)
=========== ================ ================== ================== ==============
 Reference   Designation      Designation (de)   Designation (fr)   Team manager
----------- ---------------- ------------------ ------------------ --------------
             Developers       Developers         Developers
             Managers         Managers           Managers
             Front-end team   Front-end team     Front-end team
=========== ================ ================== ================== ==============
<BLANKLINE>

.. class:: Group

    Django model representing a :term:`users group`.

    .. attribute:: ref

        The reference.

        See :attr:`lino.mixins.ref.StructuredReferrable.ref`

    .. attribute:: name

        The designation in different languages.

    .. attribute:: user

        The owner of the group


.. class:: Groups

  Shows all groups.

.. class:: Membership

    Django model representing a :term:`user membership`.

    .. attribute:: user
    .. attribute:: group
    .. attribute:: remark
