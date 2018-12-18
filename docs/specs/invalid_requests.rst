.. _invalid_requests:
.. _lino.specs.invalid_requests:

=============================
Answering to invalid requests
=============================

.. to run only this test:

    $ doctest docs/specs/invalid_requests.rst
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.min2.settings.doctests')
    >>> from lino.api.doctest import *


We are going to send some invalid AJAX requests to
:class:`lino_xl.lib.contacts.models.RolesByPerson`, a slave table on
person.

>>> contacts.RolesByPerson.master
<class 'lino_xl.lib.contacts.models.Person'>

Simulate an AJAX request:

>>> headers = dict(HTTP_X_REQUESTED_WITH='XMLHttpRequest')
>>> headers.update(REMOTE_USER='robin')
>>> test_client.force_login(rt.login('robin').user)

Here is a valid request:

>>> url = "/api/contacts/RolesByPerson?fmt=json&start=0&limit=15&mt=8&mk=114"
>>> res = test_client.get(url, **headers)
>>> print(res.status_code)
200
>>> d = AttrDict(json.loads(res.content.decode()))
>>> d.count
1
>>> print(d.title)
Contact for of Mr Hans Altenberg


Specifying an *invalid primary key* for the master (5114 in the
example below) will internally raise an `ObjectDoesNotExist`
exception, which in turn will cause an `HttpResponseBadRequest`
response (i.e. status code 400):

>>> import logging
>>> logger = logging.getLogger("django.request")
>>> logger.setLevel(logging.CRITICAL)

>>> url = "/api/contacts/RolesByPerson?fmt=json&start=0&limit=15&mt=8&mk=114114"
>>> res = test_client.get(url, **headers)
>>> res.status_code
400
>>> print(res.content.decode())
ObjectDoesNotExist: Invalid master key 114114 for contacts.RolesByPerson

Since RolesByPerson has a known master class (i.e. Person), the ``mt``
url parameter is *ignored*: an invalid value for ``mt`` does *not*
raise an exception:

>>> url = "/api/contacts/RolesByPerson?fmt=json&start=0&limit=15&mt=8888&mk=114"
>>> res = test_client.get(url, **headers)
>>> print(res.status_code)
200


Request data not supplied
=========================

After 20170410 the following AJAX request no longer raises a real
exception but continues to log it. Raising an exception had the
disadvantage of having an email sent to the ADMINS which was just
disturbing and not helpful because it had no "request data supplied".
Now the user gets an appropriate message because it receives a status
code 400.

>>> url = '/api/cal/EventsByProject?_dc=1491615952104&fmt=json&rp=ext-comp-1306&start=0&limit=15&mt=13&mk=188'
>>> res = test_client.get(url, **headers)  #doctest: +ELLIPSIS
AjaxExceptionResponse Http404: cal.EventsByProject is not a class
<BLANKLINE>
in request GET /api/cal/EventsByProject?_dc=1491615952104&fmt=json&rp=ext-comp-1306&start=0&limit=15&mt=13&mk=188
TRACEBACK:
...

>>> res.status_code
400
>>> #print(json.loads(res.content)['message'])
>>> print(res.content.decode())
Http404: cal.EventsByProject is not a class
