.. doctest docs/specs/tera/cal.rst
.. _specs.tera.cal:

=====================
Calendar in Lino Tera
=====================


.. doctest init

    >>> from lino import startup
    >>> startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *
    >>> from django.db import models


This document describes how we use the :mod:`lino_xl.lib.cal` plugin
in Tera.


>>> rt.show(cal.DailyPlanner)
============= ================ ==========
 Description   external         internal
------------- ---------------- ----------
 *AM*          *08:30 romain*
 *All day*
 *PM*
============= ================ ==========
<BLANKLINE>

