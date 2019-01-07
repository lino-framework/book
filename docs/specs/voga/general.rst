.. doctest docs/specs/voga/general.rst
.. _voga.tested.general:

=======
General
=======

doctest init:

>>> import lino
>>> lino.startup('lino_book.projects.roger.settings.doctests')
>>> from lino.api.doctest import *


>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 41 plugins
- 80 models
- 21 user roles
- 5 user types
- 308 views
- 23 dialog actions
<BLANKLINE>
