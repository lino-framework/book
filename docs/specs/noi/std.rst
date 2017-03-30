.. _noi.specs.std:

================================
The Standard variant of Lino Noi
================================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_std
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *



Overview
========

>>> dd.is_installed('products')
False

>>> dd.plugins.topics
lino_noi.lib.topics

>>> dd.plugins.tickets
lino_noi.lib.tickets

>>> dd.plugins.clocking
lino_noi.lib.clocking


