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
- 41 plugins
- 81 models
- 20 user roles
- 5 user types
- 311 views
- 23 dialog actions
<BLANKLINE>
