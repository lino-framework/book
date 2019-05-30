.. doctest docs/specs/b2c.rst
.. _xl.specs.b2c:

============================
``b2c``: BankToCustomer SEPA
============================

.. currentmodule:: lino_xl.lib.b2c


This document describes the functionality implemented by the
:mod:`lino_xl.lib.b2c` module.

.. contents::
   :local:
   :depth: 2


.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.max.settings.doctests')
>>> from lino.api.doctest import *

See the specs of :ref:`welfare` for examples.

Dependencies
============

The plugin is inactive as long as
:attr:`import_statements_path <lino_xl.lib.b2c.Plugin.import_statements_path>`
is not set.



User interface
==============

>>> ses = rt.login('robin')

>>> ses.show_menu_path(system.SiteConfig.import_b2c)
Accounting --> Import SEPA


Database models
===============

.. class:: Account

    Django model used to represent an imported bank account.

.. class:: Statement

    Django model used to represent aa statement of an imported bank account.

.. class:: Transaction


    Django model used to represent a transaction of an imported bank account.



Views reference
===============

.. class:: Accounts
.. class:: Statements
.. class:: StatementsByAccount
.. class:: TransactionsByStatement

.. class:: ImportStatements

