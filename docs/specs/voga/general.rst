.. doctest docs/specs/voga/general.rst
.. _voga.tested.general:

=======
General
=======

doctest init:

>>> import lino
>>> lino.startup('lino_book.projects.voga1.settings')
>>> from lino.api.doctest import *


>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 42 plugins
- 83 models
- 6 user types
- 313 views
- 24 dialog actions
<BLANKLINE>
