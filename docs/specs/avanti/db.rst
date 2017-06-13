.. _avanti.specs.db:

=================================
Database structure of Lino Avanti
=================================

.. To run only this test::

    $ python setup.py test -s tests.SpecsTests.test_avanti_db

    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

This document describes the database structure.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP



>>> print(analyzer.show_complexity_factors())
- 38 plugins
- 76 models
- 275 views
- 7 user types
- 10 dialog actions
<BLANKLINE>

