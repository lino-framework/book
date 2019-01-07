.. doctest docs/specs/tera/contacts.rst
.. _tera.specs.contacts:

=========
Contacts
=========

This document specifies how the :mod:`lino_tera.lib.contacts` plugin is
being used in :ref:`tera`.


.. contents::
  :local:


.. currentmodule:: lino_tera.lib.contacts
                   

.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *

>>> dd.plugins.contacts
lino_tera.lib.contacts (extends_models=['Person'])



.. class:: Partner

    .. attribute:: pf_residence

        The residence used to determine the fee for invoicing.

        >>> rt.show(courses.Residences)
        ======= ======== =========
         value   name     text
        ------- -------- ---------
         10      inside   Inside
         20      ouside   Outside
        ======= ======== =========
        <BLANKLINE>

    .. attribute:: pf_income

        The income category used to determine the fee for invoicing.

        >>> rt.show(courses.IncomeCategories)
        ======= ====== ======
         value   name   text
        ------- ------ ------
         10             A
         20             B
         30             C
         40             D
         50             E
        ======= ====== ======
        <BLANKLINE>

    .. attribute:: pf_composition

        The family composition used to determine the fee for invoicing.

        >>> rt.show(courses.HouseholdCompositions)
        ======= =============== ====================================
         value   name            text
        ------- --------------- ------------------------------------
         10      no_child        No participant below 18
         20      one_child       One participant below 18
         30      more_children   More than one participant below 18
        ======= =============== ====================================
        <BLANKLINE>
