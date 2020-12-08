.. doctest docs/specs/noi/suggesters.rst
.. _specs.noi.suggesters:

======================
Suggesters in Lino Noi
======================


Compare the :fixture:`demo2` fixture of :mod:`lino.modlib.comments`.

.. contents::
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.noi1e.settings.doctests')
>>> from lino.api.doctest import *


>>> mp = settings.SITE.plugins.memo.parser
>>> sorted(mp.suggesters.keys())
['#', '@']

>>> print(mp.parse("This comment refers to #11 and @robin."))
This comment refers to #11 and @robin.

Nothing has been replaced! Why? Because the parser replaces the suggested
expressions only when an action request is known.  The current action request
is usually given in the context.

>>> ses = rt.login('robin')
>>> print(mp.parse("This comment refers to #11 and @robin.", ar=ses))
This comment refers to <a href="Detail" title="#11 (&#9737; Class-based Foos and Bars?)">#11</a> and <a href="Detail" title="Robin Rood">@robin</a>.

>>> print(mp.parse("This comment refers to #robin and @11.", ar=ses))
This comment refers to #robin and @11.

>>> print(mp.parse("This comment refers to # and @.", ar=ses))
This comment refers to # and @.
