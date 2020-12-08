.. doctest docs/specs/noi/as_pdf.rst
.. _noi.specs.as_pdf:

=================
Printing tables
=================

This document just tests the print to pdf function.


.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst


>>> from lino import startup
>>> startup('lino_book.projects.noi1e.settings.demo')
>>> from lino.api.doctest import *


>>> # rt.login('robin').show('tickets.ActiveTickets')

>>> settings.SITE.appy_params.update(raiseOnError=True)
>>> test_client.force_login(rt.login('robin').user)
>>> def mytest(k):
...     url = 'http://127.0.0.1:8000/api/{0}?an=as_pdf'.format(k)
...     res = test_client.get(url, REMOTE_USER='robin')
...     assert res.status_code == 200, "Request to {} got status code {}".format(url, res.status_code)
...     result = json.loads(res.content)
...     assert result['success']
...     print(result['open_url'])

>>> mytest("tickets/ActiveTickets")
/media/cache/appypdf/127.0.0.1/tickets.ActiveTickets.pdf

>>> mytest("tickets/AllTickets")
/media/cache/appypdf/127.0.0.1/tickets.AllTickets.pdf
