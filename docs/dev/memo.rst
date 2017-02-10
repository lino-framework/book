.. _dev.memo:

===============
The memo parser
===============


.. To run only this test:

   $ python setup.py test -s tests.DocsTests.test_memo

..
    >>> from lino import startup
    >>> startup('lino_noi.projects.team.settings.doctests')
    >>> from lino.api.doctest import *

Lino has a simple built-in markup language called "memo".

See :mod:`lino.utils.memo`.
    
>>> ar = rt.login('robin')
>>> obj = rt.models.tickets.Ticket.objects.get(pk=1)
>>> txt = ar.obj2memo(obj)
>>> print(txt)
[ticket 1] (Föö fails to bar when baz)

>>> print(ar.parse_memo(txt))
<a href="Detail" title="F&#246;&#246; fails to bar when baz">#1</a> (Föö fails to bar when baz)

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_memo_commands())
<BLANKLINE>
- [ticket ...] : Insert a reference to the specified database object.
<BLANKLINE>
  The first argument is mandatory and specifies the
  primary key.
<BLANKLINE>
  If there is more than one argument, all remaining text
  is used as the text of the link.
<BLANKLINE>
