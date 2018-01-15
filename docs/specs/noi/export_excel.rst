.. _noi.specs.export_excel:

================================
Exporting to Excel from Lino Noi
================================

This just tests whether certain tables are exportable to Excel.  For
more explanations see :ref:`lino.specs.export_excel` of :ref:`book`.


.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_noi_export_excel
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *



>>> url = "/api/working/Sessions?an=export_excel"
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200

