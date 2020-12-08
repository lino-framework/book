.. _noi.specs.stars:

=================
Stars in Lino Noi
=================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_stars
    Or:
    $ python -m atelier.doctest_utf8 docs/specs/noi/stars.rst

    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.noi1e.settings.demo')
    >>> from lino.api.doctest import *
    >>> from pprint import pprint

This document specifies how stars are implemented in
:mod:`lino_xl.lib.stars` (as used by Lino Noi).

.. contents::
  :local:


Stars are used in to indicate that the user want to be notified on changes to database object.
There are 3 ways that a object can be starred. Not stared, inheriting a star, and directly stared.

The user will only be notified on object which they have either inherited a star or been directly stared.


>>> ses = rt.login('robin')
>>> ses.selected_rows.append(rt.models.tickets.Site.objects.all()[0])
>>> pprint(set(ses.selected_rows[0].get_children_starrable()))
... #doctest: +REPORT_UDIFF +SKIP

