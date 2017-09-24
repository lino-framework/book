.. _avanti.specs.db:

=================================
Database structure of Lino Avanti
=================================

.. To run only this test::

    $ doctest docs/specs/avanti/db.rst

    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

This document describes the database structure.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP



>>> print(analyzer.show_complexity_factors())
- 39 plugins
- 77 models
- 281 views
- 7 user types
- 11 dialog actions
<BLANKLINE>

