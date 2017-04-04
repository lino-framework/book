.. _specs.cosi.finan:

===============================
Financial vouchers in Lino Così
===============================

.. to test only this document:

      $ python setup.py test -s tests.SpecsTests.test_finan
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.pierre.settings.doctests')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")
    >>> translation.activate('en')

This document describes what we call **financial vouchers**
(i.e. *simple journal entries*, *bank statements* and *payment
orders*) as implemented by the :mod:`lino_xl.lib.finan` plugin.  

It is based on the following other specifications:

- :ref:`cosi.specs.accounting`
- :ref:`cosi.specs.ledger`

Table of contents:


.. contents::
   :depth: 1
   :local:
