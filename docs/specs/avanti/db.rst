.. doctest docs/specs/avanti/db.rst
.. _avanti.specs.db:

=================================
Database structure of Lino Avanti
=================================

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

This document describes the database structure.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP



>>> print(analyzer.show_complexity_factors())
- 39 plugins
- 79 models
- 29 user roles
- 8 user types
- 289 views
- 89 dialog actions
<BLANKLINE>

