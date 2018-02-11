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
 2013                  1       6
 2013                  2       6
 2013                  3       6
 2013                  4       6
 2013                  5       6
 2013                  6       6
 2013                  7       6
 2013                  8       6
 2013                  9       6
 2013                  10      6
 2013                  11      6
 2013                  12      6
 2014                  1       6
 2014                  2       6
 2014                  3       6
 2014                  4       6
 2014                  5       6
 2014                  6       6
 2014                  7       6
 2014                  8       6
 2014                  9       6
 2014                  10      6
 2014                  11      6
 2014                  12      6
 2015                  1       6
 2015                  2       6
 2015                  3       6
 2015                  4       6
 2015                  5       6
 2015                  6       6
 2015                  7       6
 2015                  8       6
 2015                  9       6
 2015                  10      6
 2015                  11      6
 2015                  12      6
 **Total (36 rows)**           **216**
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
