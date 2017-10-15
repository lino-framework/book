.. _noi.specs.bs3:

=====================================================
A read-only interface to Team using generic Bootstrap
=====================================================

.. How to test just this document:

    $ doctest docs/specs/noi/bs3.rst
    
    doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.bs3.settings.demo')
    >>> from lino.api.doctest import *


This document specifies the read-only public interface of Lino Noi.
implemented in :mod:`lino_book.projects.bs3`.

Provides readonly anonymous access to the data of
:mod:`lino_book.projects.team`, using the :mod:`lino.modlib.bootstrap3`
user interface. See also :mod:`lino_book.projects.public`

This does not use :mod:`lino.modlib.extjs` at all.


.. contents::
  :local:

.. The following was used to reproduce :ticket:`960`:

    >>> res = test_client.get('/tickets/Ticket/13')
    >>> res.status_code
    200


Tickets are rendered using plain bootstrap HTML:

>>> res = test_client.get('/')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, "lxml")
>>> links = soup.find_all('a')
>>> len(links)
24
>>> print(links[0].get('href'))
/?ul=de
>>> print(links[1].get('href'))
/?ul=fr
>>> print(links[2].get('href'))
#

>>> res = test_client.get('/tickets/Ticket/13')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, "lxml")


>>> links = soup.find_all('a')
>>> len(links)
28
>>> print(links[0].get('href'))
/?ul=en

>>> print(soup.get_text(' ', strip=True))
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF +ELLIPSIS
All tickets Sign in — Home en de fr Tickets All tickets Site About #13 (Bar cannot foo) << < > >> State: Sleeping 
<BLANKLINE>
<BLANKLINE>
(last update ...) Created ... by Luc Topic: Lino Core Site: welket Linking to #1 and to blog . This is Lino Noi ... using ...
