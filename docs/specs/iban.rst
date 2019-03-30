.. doctest docs/specs/iban.rst
.. _specs.iban:

===================
Adding IBAN numbers
===================

This document describes the concepts implemented by the
:mod:`lino_xl.lib.sepa` plugin.

.. contents::
   :depth: 1
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.apc.settings.demo')
>>> from lino.api.doctest import *

The following snippet tests whether all the fictuve IBAN samples are
detected as valid by `localflavor`:

>>> from lino_xl.lib.sepa.fixtures.sample_ibans import IBANS
>>> from django.core.exceptions import ValidationError
>>> from localflavor.generic.validators import IBANValidator
>>> validate = IBANValidator()
>>> for i, iban in enumerate(IBANS):
...     try:
...         validate(iban)
...     except ValidationError as e:
...         print("{0}: {1} : {2}".format(i, iban, e))


