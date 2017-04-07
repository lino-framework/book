.. _avanti.specs.roles:

=========================
User roles in Lino Avanti
=========================

.. To run only this test::

    $ python setup.py test -s tests.SpecsTests.test_avanti_roles

    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

Menus
-----

System administrator
--------------------

Rolf is a system administrator, he has a complete menu.

>>> ses = rt.login('robin') 
>>> ses.user.profile
users.UserTypes.admin:900

>>> ses.show_menu()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP
