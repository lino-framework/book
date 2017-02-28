.. _cosi.specs.invoicing:

===================
Generating invoices
===================

.. to test only this document:

      $ python setup.py test -s tests.DocsTests.test_invoicing
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_cosi.projects.std.settings.demo')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")
    >>> translation.activate('en')

This document describes some general aspects of how Lino Così and
derived applications can handle **invoicing**, i.e. automatically
generating invoices from data in the database.

:mod:`lino_cosi.lib.invoicing`

- :ref:`cosi.specs.sales`
- :ref:`cosi.specs.accounting`


.. contents::
   :depth: 1
   :local:


Manually editing automatically generated invoices
=================================================

Resetting title and description of a generated invoice item
===========================================================

When the user sets `title` of an automatically generated invoice
item to an empty string, then Lino restores the default value for
both title and description



