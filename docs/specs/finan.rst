.. _cosi.specs.finan:

===============================
Financial vouchers in Lino Così
===============================

.. to test only this document:

      $ python setup.py test -s tests.DocsTests.test_ledger
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_cosi.projects.std.settings.demo')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")
    >>> translation.activate('en')

This document describes what we call **financial vouchers**
(i.e. *simple journal entries*, *bank statements* and *payment
orders*) as implemented by the :mod:`lino_cosi.lib.finan` plugin.  

It is based on the following other specifications:

- :ref:`cosi.specs.accounting`
- :ref:`cosi.specs.ledger`

Table of contents:


.. contents::
   :depth: 1
   :local:
