.. _noi.specs.faculties:

================================
Faculties management in Lino Noi
================================


.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_faculties
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.noi1e.settings.demo')
    >>> from lino.api.doctest import *


Lino Noi no longer has a notion of **faculties** and **competences**
which might be useful in bigger teams for assigning a ticket to a
worker.  See :ref:`care` which has does more usage of them.


