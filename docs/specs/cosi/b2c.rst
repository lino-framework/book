.. _specs.cosi.b2c:

===============================
B2C in Lino Così
===============================

.. to test only this document:

      $ python setup.py test -s tests.SpecsTests.test_b2c
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.pierre.settings.doctests')
    >>> from lino.api.doctest import *
    >>> ses = rt.login("robin")

This document describes
Bank to Customer (B2C) communication
as implemented by the :mod:`lino_cosi.lib.b2c` plugin.



.. contents::
   :depth: 1
   :local:


Febelfin Bank Transaction Code designations
===========================================

The :mod:`lino_xl.lib.b2c.febelfin` module defines a utility function
:func:`code2desc` which returns the designation of a *bank transaction
code*, as specified by the `XML message for statement Implementation
guidelines
<https://www.febelfin.be/sites/default/files/files/Standard-XML-Statement-v1-en_0.pdf>`_
of the Belgian Federation of Financial Sector.

This function is being used by the :attr:`txcd_text
<lino_xl.lib.b2c.models.Movement.txcd_text>` field of an imported
movement.

Usage examples:

>>> from lino_cosi.lib.b2c.febelfin import code2desc

>>> with translation.override('en'):
...     print(code2desc('0103'))
Standing order

>>> with translation.override('fr'):
...     print(code2desc('0103'))
Ordre permanent

>>> with translation.override('en'):
...     print(code2desc('0150'))
Transfer in your favour

>>> with translation.override('fr'):
...     print(code2desc('0150'))
Virement en votre faveur

>>> with translation.override('en'):
...     print(code2desc('8033'))
Miscellaneous fees and commissions


Did you know that there are 274 different Febelfin bank transaction codes?

>>> from lino_cosi.lib.b2c.febelfin import DESCRIPTIONS
>>> len(DESCRIPTIONS)
274

