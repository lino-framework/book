.. _voga.tested.general:

=======
General
=======

.. To run only this test::

    $ python setup.py test -s tests.DocsTests.test_general

    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *

