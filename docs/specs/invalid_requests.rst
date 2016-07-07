.. _invalid_requests:
.. _lino.specs.invalid_requests:

Answering to invalid requests
=============================

.. to run only this test:

    $ python setup.py test -s tests.SpecsTests.test_invalid_requests
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.min1.settings.doctests')
    >>> from lino.api.doctest import *


We are going to send some invalid AJAX requests to
:class:`lino_xl.lib.contacts.models.RolesByPerson`, a slave table on
person.

>>> contacts.RolesByPerson.master
<class 'lino_xl.lib.contacts.models.Person'>

Simulate an AJAX request:

>>> headers = dict(HTTP_X_REQUESTED_WITH='XMLHttpRequest')
>>> headers.update(REMOTE_USER='robin')

Here is a valid request:

>>> url = "/api/contacts/RolesByPerson?fmt=json&start=0&limit=15&mt=8&mk=114"
>>> res = test_client.get(url, **headers)
>>> print(res.status_code)
200
>>> d = AttrDict(json.loads(res.content))
>>> d.count
1
>>> print(d.title)
Contact for of Mr Hans Altenberg


Specifying an *invalid primary key* for the master (5114 in the
example below) will internally raise an `ObjectDoesNotExist`
exception, which in turn will cause an `HttpResponseBadRequest`
response (i.e. status code 400):

>>> url = "/api/contacts/RolesByPerson?fmt=json&start=0&limit=15&mt=8&mk=114114"
>>> res = test_client.get(url, **headers)
>>> print(res.status_code)
400

Since RolesByPerson has a known master class (i.e. Person), the ``mt``
url parameter is *ignored*: an invalid value for ``mt`` does *not*
raise an exception:

>>> url = "/api/contacts/RolesByPerson?fmt=json&start=0&limit=15&mt=8888&mk=114"
>>> res = test_client.get(url, **headers)
>>> print(res.status_code)
200

