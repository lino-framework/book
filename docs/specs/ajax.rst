.. doctest docs/specs/ajax.rst
.. _book.specs.ajax:
.. _cosi.tested.bel_de:

===========================================
Refusing permission to an anonymous request
===========================================

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.apc.settings.sestests')
    >>> from lino.api.doctest import *



This document reproduces a unicode error which occurred when Lino
tried to say "As Anonymous you have no permission to run this action."
in German (where the internationalized text contains non-ascii
characters.

The error was::

  UnicodeEncodeError at /api/sales/InvoicesByJournal
  'ascii' codec can't encode character u'\xfc' in position 64: ordinal not in range(128)

We cannot use the `doctests` settings because the situation happens
only with session-based authentication.


This document uses :mod:`lino_book.projects.apc`:

>>> print(settings.SETTINGS_MODULE)
lino_book.projects.apc.settings.sestests

>>> print(settings.SITE.default_user)
None
>>> print(settings.SITE.user_model)
<class 'lino.modlib.users.models.User'>
>>> print(settings.SITE.remote_user_header)
None
>>> print(settings.SITE.get_auth_method())
session
>>> print('\n'.join(settings.MIDDLEWARE))
django.middleware.common.CommonMiddleware
django.middleware.locale.LocaleMiddleware
django.contrib.sessions.middleware.SessionMiddleware
lino.core.auth.middleware.AuthenticationMiddleware
lino.core.auth.middleware.WithUserMiddleware
lino.core.auth.middleware.DeviceTypeMiddleware
lino.utils.ajax.AjaxExceptionResponse

>>> 'django.contrib.sessions' in settings.INSTALLED_APPS
True

Some client logs in and gets some data:

>>> test_client.force_login(rt.login('rolf').user)

The user uses the main menu to open sales.InvoicesByJournal, which
will do the following AJAX call to get its data:

>>> url = '/api/sales/InvoicesByJournal'
>>> url += "?start=0&limit=25&fmt=json&rp=ext-comp-1135"
>>> url += "&pv=1&pv=&pv=&pv=&pv=&mt=24&mk=1"
>>> res = test_client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
>>> res.status_code
200
>>> r = json.loads(res.content.decode())
>>> print(json.dumps(sorted(r.keys())))
["count", "no_data_text", "param_values", "rows", "success", "title"]
>>> len(r['rows'])
25

Now imagine that the user gets a break and leaves her browser open,
the server meanwhile did a dump and a reload. So the sessions have
been removed:

>>> x = sessions.Session.objects.all().delete()

The user comes back and resizes her browser window, or some other
action which will trigger a refresh.  The same URL will now return a
400 (Bad request) response:

>>> import logging
>>> logger = logging.getLogger("django.request")
>>> logger.setLevel(logging.CRITICAL)

>>> res = test_client.get(url)  #doctest: +ELLIPSIS
>>> res.status_code
403
>>> soup = BeautifulSoup(res.content, 'lxml')
>>> # print(soup.body.prettify())
>>> divs = soup.body.find_all('div')
>>> len(divs)
6
>>> print(divs[3].get_text().strip())
Zugriff verweigert
You have no permission to see this resource.


The above URL is usually issued as an AJAX call.

Lino recognizes AJAX calls
by the extra HTTP header `HTTP_X_REQUESTED_WITH`
having the value ``XMLHttpRequest``.
For this simulation
we must say this explicitly to Django's test client.

>>> res = test_client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

When an exception like the above occurs during an AJAX call, Lino's
reponse has different format which is defined by the
:mod:`lino.utils.ajax` middleware. It sets the status code to 400 (Bad
Request) which means "The request could not be understood by the
server due to malformed syntax. The client SHOULD NOT repeat the
request without modifications." (`w3.org
<https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10>`__)

>>> res.status_code
400
>>> print(res.content.decode())
PermissionDenied: As 000 (Anonym) you have no permission to run this action.
