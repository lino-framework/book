.. _book.specs.help_texts:

======================
Help texts
======================

TODO: Write explanations between the examples.

..  To test only this document:

    $ python setup.py test -s tests.SpecsTests.test_help_texts

    doctest initialization:

    >>> import lino
    >>> lino.startup('lino_book.projects.min2.settings.doctests')
    >>> from lino.api.doctest import *

.. contents::
   :local:
   :depth: 2


>>> from lino.api import _
>>> from lino.utils.jsgen import py2js
>>> x = dict(tooltip=_("""This is a "foo", IOW a bar."""))
>>> print(py2js(x))
{ "tooltip": "This is a \"foo\", IOW a bar." }
