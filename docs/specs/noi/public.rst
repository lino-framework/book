.. doctest docs/specs/noi/public.rst
.. _noi.specs.public:

=================================================================
Experimental interface to Team using Bootstrap and self-made URLs
=================================================================

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.public.settings.demo')
    >>> from lino.api.doctest import *

This document describes the :mod:`lino_book.projects.public` variant of
:ref:`noi` which provides readonly anonymous access to the data of
:mod:`lino_book.projects.team` using the :mod:`lino_noi.lib.public`
user interface.

The :mod:`lino_noi.lib.public` user interface is yet another way of
providing read-only anonymous access.  But it is experimental,
currently we recommend :ref:`noi.specs.bs3`


.. contents::
  :local:

The home page:

>>> res = test_client.get('/')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, 'lxml')
>>> links = soup.find_all('a')
>>> len(links)
134
>>> print(links[0].get('href'))
/?ul=de
>>> print(links[1].get('href'))
/?ul=fr
>>> print(links[2].get('href'))
/ticket/116


>>> res = test_client.get('/ticket/13/')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, 'lxml')
>>> print(soup.get_text(' ', strip=True))
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF +ELLIPSIS
Home en de fr #13 Bar cannot foo State: Sleeping
<BLANKLINE>
<BLANKLINE>
(last update ...) Created ... by Rolf Rompen Linking to [ticket 1] and to
 [url http://luc.lino-framework.org/blog/2015/0923.html blog]. This is Lino Noi ... using ...
