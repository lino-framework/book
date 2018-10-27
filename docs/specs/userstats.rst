.. doctest docs/specs/userstats.rst
.. _specs.userstats:

===============
User statistics
===============

.. doctest init:
   
   >>> import lino
   >>> lino.startup('lino_book.projects.team.settings.doctests')
   >>> from lino.api.doctest import *

.. currentmodule:: lino_xl.lib.userstats   

The :mod:`lino_xl.lib.userstats` plugin adds functionality for getting
statistical data about the system users.  For the moment this shows
nothing more and nothing less than the **number of active users for
every month**.

The plugin adds a database model :class:`UserStat` and a menu entry
:menuselection:`Explorer --> System --> User statistics` which shows
all user statistic entries.

The numbers are updated together with all other :doc:`summaries`.

.. contents::
  :local:

Example
=======

>>> rt.show('userstats.UserStats')
===================== ======= ==============
 Year                  Month   Active users
--------------------- ------- --------------
 2013                  1       7
 2013                  2       7
 2013                  3       7
 2013                  4       7
 2013                  5       7
 2013                  6       7
 2013                  7       7
 2013                  8       7
 2013                  9       7
 2013                  10      7
 2013                  11      7
 2013                  12      7
 2014                  1       7
 2014                  2       7
 2014                  3       7
 2014                  4       7
 2014                  5       7
 2014                  6       7
 2014                  7       7
 2014                  8       7
 2014                  9       7
 2014                  10      7
 2014                  11      7
 2014                  12      7
 2015                  1       7
 2015                  2       7
 2015                  3       7
 2015                  4       7
 2015                  5       7
 2015                  6       7
 2015                  7       7
 2015                  8       7
 2015                  9       7
 2015                  10      7
 2015                  11      7
 2015                  12      7
 **Total (36 rows)**           **252**
===================== ======= ==============
<BLANKLINE>


.. currentmodule:: lino_xl.lib.userstats

Models
======

.. class:: UserStats
.. class:: UserStat

    A :class:`Summary <lino.modlib.summaries.Summary>` on
    :class:`SiteConfig <lino.modlib.system.SiteConfig>`.


    .. attribute:: year
    .. attribute:: month
    .. attribute:: master
    .. attribute:: active_users

        The number of active users. A user is considered active if
        their :attr:`start_date <lino.modlib.users.User.start_date>`
        is either empty or before the first day of this month or year,
        and if their :attr:`end_date
        <lino.modlib.users.User.end_date>` is either empty or
        after the first day of this month or year.
