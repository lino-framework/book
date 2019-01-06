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
lino_tera.lib.contacts


.. class:: Partner

    .. attribute:: pf_residence

        The residence used to determine the fee for invoicing.

    .. attribute:: pf_income

        The income category used to determine the fee for invoicing.

    .. attribute:: pf_composition

        The family composition used to determine the fee for invoicing.

