.. _noi.specs.public:

=================================================================
Experimental interface to Team using Bootstrap and self-made URLs
=================================================================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_noi_public
    Or:
    $ python -m doctest docs/specs/noi/public.rst
   
    doctest init:

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

Public tickets
==============

This is currently the only table publicly available.

The demo database contains the following data:

>>> rt.show(tickets.PublicTickets)
... #doctest: +REPORT_UDIFF
================================================================================== ============= =========== ==========
 Description                                                                        Ticket type   Topic       Priority
---------------------------------------------------------------------------------- ------------- ----------- ----------
 `#115 (☉ Ticket 115) <Detail>`__  by *Luc*, assigned to *Luc*                      Bugfix        Lino Voga   Normal
 `#107 (☉ Ticket 107) <Detail>`__  by *Mathieu*, assigned to *Luc*                  Enhancement   Lino Voga   Normal
 `#91 (☉ Ticket 91) <Detail>`__  by *Luc*, assigned to *Luc*                        Bugfix        Lino Voga   Normal
 `#83 (☉ Ticket 83) <Detail>`__  by *Mathieu*, assigned to *Luc*                    Enhancement   Lino Voga   Normal
 `#75 (☉ Ticket 75) <Detail>`__  by *Jean*, assigned to *Luc*                       Upgrade       Lino Voga   Normal
 `#67 (☉ Ticket 67) <Detail>`__  by *Luc*, assigned to *Luc*                        Bugfix        Lino Voga   Normal
 `#51 (☉ Ticket 51) <Detail>`__  by *Jean*, assigned to *Luc*                       Upgrade       Lino Voga   Normal
 `#43 (☉ Ticket 43) <Detail>`__  by *Luc*, assigned to *Luc*                        Bugfix        Lino Voga   Normal
 `#35 (☉ Ticket 35) <Detail>`__  by *Mathieu*, assigned to *Luc*                    Enhancement   Lino Voga   Normal
 `#27 (☉ Ticket 27) <Detail>`__  by *Jean*, assigned to *Luc*                       Upgrade       Lino Voga   Normal
 `#11 (☉ Class-based Foos and Bars?) <Detail>`__  by *Mathieu*, assigned to *Luc*   Enhancement   Lino Voga   Normal
================================================================================== ============= =========== ==========
<BLANKLINE>


The home page:

>>> res = test_client.get('/')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, 'lxml')
>>> links = soup.find_all('a')
>>> len(links)
28
>>> print(links[0].get('href'))
/?ul=de
>>> print(links[1].get('href'))
/?ul=fr
>>> print(links[2].get('href'))
/ticket/115


>>> res = test_client.get('/ticket/13/')
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, 'lxml')
>>> print(soup.get_text(' ', strip=True))
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF +ELLIPSIS
Home en de fr #13 Bar cannot foo State: Sleeping
<BLANKLINE>
<BLANKLINE>
(last update ...) Created ... by Luc Topic: Lino Welfare Linking to [ticket 1] and to
 [url http://luc.lino-framework.org/blog/2015/0923.html blog]. This is Lino Noi ... using ...
