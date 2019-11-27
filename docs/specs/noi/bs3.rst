.. doctest docs/specs/noi/bs3.rst
.. _noi.specs.bs3:

=====================================================
A read-only interface to Team using generic Bootstrap
=====================================================

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.bs3.settings.demo')
    >>> from lino.api.doctest import *


This document specifies the read-only public interface of Lino Noi.
implemented in :mod:`lino_book.projects.bs3`.

Provides readonly anonymous access to the data of
:mod:`lino_book.projects.team`, using the :mod:`lino.modlib.bootstrap3`
front end. See also :mod:`lino_book.projects.public`

This does not use :mod:`lino.modlib.extjs` at all.


.. contents::
  :local:

.. The following was used to reproduce :ticket:`960`:

    >>> res = test_client.get('/tickets/Ticket/15')
    >>> res.status_code
    200


Tickets are rendered using plain bootstrap HTML:

>>> res = test_client.get('/')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, "lxml")
>>> links = soup.find_all('a')
>>> len(links)
65
>>> print(links[0].get('href'))
/?ul=de
>>> print(links[1].get('href'))
/?ul=fr
>>> print(links[2].get('href'))
#

>>> res = test_client.get('/tickets/Ticket/15')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, "lxml")


>>> links = soup.find_all('a')
>>> len(links)
32
>>> print(links[0].get('href'))
/?ul=en

>>> print(soup.get_text(' ', strip=True))
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF +ELLIPSIS
Tickets Sign in — Home en de fr Tickets All tickets Office Recent comments Site About #15 (Bars have no foo) << < > >> State: Closed
<BLANKLINE>
<BLANKLINE>
(last update ...) Created ... by Jean Site: pypi Styled comment pasted ... This is Lino Noi ... using ...
