.. doctest docs/specs/voga/voga.rst
.. _voga.tested.voga:

Voga
=======

..  doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.utils.translation import get_language

    >>> print([lng.name for lng in settings.SITE.languages])
    ['en', 'de', 'fr']


A web request
-------------

The following snippet reproduces a one-day bug on calendar events
whose **time** fields are empty.  Fixed 2013-06-04 in
:func:`lino.modlib.cal.utils.when_text`.

>>> print(get_language())
en
>>> client = Client()
>>> d = settings.SITE.demo_date().replace(month=12,day=25)
>>> d = d.strftime(settings.SITE.date_format_strftime)
>>> print(d)
25.12.2015
>>> url = '/api/cal/MyEntries?start=0&limit=16&fmt=json&pv=%s&pv=%s&pv=&pv=&pv=&pv=&pv=&pv=&pv=' % (d,d)
>>> client.force_login(rt.login('robin').user)
>>> res = client.get(url, REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> print(result.keys())
[u'count', u'rows', u'no_data_text', u'success', u'title', u'param_values']


Printable documents
-------------------

We take a sales invoice, clear the cache, ask Lino to print it and 
check whether we get the expected response.

>>> ses = rt.login("robin")
>>> translation.activate('en')
>>> obj = sales.VatProductInvoice.objects.get(journal__ref="SLS", number=11)

>>> obj.printed_by is None
True

>>> obj.clear_cache()
>>> rv = ses.run(obj.do_print)  #doctest: +ELLIPSIS
appy.pod render .../lino_xl/lib/sales/config/sales/VatProductInvoice/Default.odt -> .../media/cache/appypdf/sales.VatProductInvoice-135.pdf (language='en',params={'raiseOnError': True, 'ooPort': 8100, 'pythonWithUnoPath': ...}

>>> print(rv['success']) 
True
>>> print(rv['open_url'])  #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
/media/cache/appypdf/sales.VatProductInvoice-135.pdf
>>> print(rv['message']) #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
Your printable document (filename sales.VatProductInvoice-135.pdf)
should now open in a new browser window. If it doesn't, please consult
<a href="http://www.lino-framework.org/help/print.html"
target="_blank">the documentation</a> or ask your system
administrator.

Note that we must clear the print cache because leaving the excerpt
there would break a test case in :doc:`db_roger`.

>>> obj.clear_cache()

Same for a calendar Event.  This is mainly to see whether the
templates directory has been inherited.  Note that the first few dozen
events have no `user` and would currently fail to print.

>>> obj = cal.Event.objects.get(pk=100)
>>> obj.clear_cache()
>>> rv = ses.run(obj.do_print) #doctest: +ELLIPSIS
appy.pod render .../lino_xl/lib/cal/config/cal/Event/Default.odt -> .../media/cache/appypdf/cal.Event-100.pdf (language='en',params={'raiseOnError': True, 'ooPort': 8100, 'pythonWithUnoPath': ...}

>>> print(rv['success'])
True
>>> print(rv['message']) #doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
Your printable document (filename cal.Event-100.pdf) should now open
in a new browser window. If it doesn't, please consult <a
href="http://www.lino-framework.org/help/print.html"
target="_blank">the documentation</a> or ask your system
administrator.

Note that this test should fail if you run the test suite without a 
LibreOffice server running.


