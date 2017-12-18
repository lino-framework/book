.. doctest docs/specs/avanti/general.rst
.. _avanti.specs.general:

===============================
General overview of Lino Avanti
===============================

..  doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *

The goal of Lino Avanti is 


.. contents::
  :local:

Miscellaneous
=============

List of demo users:

>>> rt.show(rt.actors.users.Users)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
========== =============== ============ ===========
 Username   User type       First name   Last name
---------- --------------- ------------ -----------
 audrey     Auditor
 laura      Teacher         Laura        Lieblig
 martina    Coordinator
 nathalie   Social worker
 robin      Administrator   Robin        Rood
 rolf       Administrator   Rolf         Rompen
 romain     Administrator   Romain       Raffault
 sandra     Secretary
========== =============== ============ ===========
<BLANKLINE>


>>> dd.plugins.beid.holder_model
<class 'lino_avanti.lib.avanti.models.Client'>

The following checks whether the dashboard displays for user robin:

>>> url = "/"
>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get(url, REMOTE_USER="robin")
>>> res.status_code
200
>>> soup = BeautifulSoup(res.content, "lxml")
>>> links = soup.find_all('a')
>>> len(links)
0
