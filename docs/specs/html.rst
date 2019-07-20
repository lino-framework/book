.. doctest docs/specs/html.rst
.. _lino.specs.html:

===============
Generating HTML
===============

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.polly.settings.demo')
    >>> from lino.api.doctest import *

This describes some Lino-specific usage of the
:mod:`etgen.html` module.


.. contents::
   :depth: 1
   :local:


>>> from etgen.html import E

>>> txt = "foo"
>>> txt = E.b(txt)
>>> ar = rt.login('robin', renderer=settings.SITE.kernel.default_renderer)
>>> obj = ar.user
>>> e = ar.obj2html(obj, txt)
>>> print(tostring(e))
<a href="/api/users/Users/1"><b>foo</b></a>


