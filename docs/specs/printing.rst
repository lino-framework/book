==================
Printing documents
==================

.. How to test only this document:

     $ py.test -k test_printing
     $ python setup.py test -s tests.SpecsTests.test_printing

   Initialize doctest:

    >>> from lino import startup
    >>> startup('lino_book.projects.max.settings.doctests')
    Your plugins.clocking.ticket_model (<class 'lino_xl.lib.contacts.models.Partner'>) is not workable
    >>> from lino.api.shell import *
    >>> from lino.api.doctest import *

The Extended Library adds a series of plugins related to printing:

- :mod:`lino_xl.lib.excerpts`.
- :mod:`lino_xl.lib.appy_pod`.
- :mod:`lino_xl.lib.wkhtmltopdf`.


>>> rt.show(printing.BuildMethods)  #doctest: +NORMALIZE_WHITESPACE
============= ============= ======================
 value         name          text
------------- ------------- ----------------------
 latex         latex         LatexBuildMethod
 pisa          pisa          PisaBuildMethod
 rtf           rtf           RtfBuildMethod
 weasy2html    weasy2html    WeasyHtmlBuildMethod
 weasy2pdf     weasy2pdf     WeasyPdfBuildMethod
 wkhtmltopdf   wkhtmltopdf   WkBuildMethod
 appyodt       appyodt       AppyOdtBuildMethod
 appydoc       appydoc       AppyDocBuildMethod
 appypdf       appypdf       AppyPdfBuildMethod
 appyrtf       appyrtf       AppyRtfBuildMethod
============= ============= ======================
<BLANKLINE>


Printing a normal pdf table
===========================

>>> settings.SITE.appy_params.update(raiseOnError=True)
>>> url = 'http://127.0.0.1:8000/api/contacts/Partners?an=as_pdf'
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> print(result['success'])
True
>>> print(result['open_url'])
/media/cache/appypdf/127.0.0.1/contacts.Partners.pdf



Printing address labels
=======================

>>> settings.SITE.appy_params.update(raiseOnError=True)
>>> url = 'http://127.0.0.1:8000/api/contacts/Partners?an=print_labels'
>>> res = test_client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> print(result['success'])
True
>>> print(result['open_url'])
/media/cache/appypdf/127.0.0.1/contacts.Partners.pdf


