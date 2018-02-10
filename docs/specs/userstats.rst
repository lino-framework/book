.. doctest docs/specs/userstats.rst
.. _specs.userstats:

===============
User statistics
===============

.. doctest init:
   
   >>> import lino
   >>> lino.startup('lino_book.projects.team.settings.doctests')
   >>> from lino.api.doctest import *
   >>> from django.db.models import Q

The :mod:`lino_xl.lib.userstats` plugin adds functionality for
gettings statistical data about the system users.  For the moment this
computes the number of active users for every month.


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

>>> # rt.models.userstats.UserStat.__mro__
>>> # rt.models.userstats.UserStat._widget_options
>>> # cols = rt.models.userstats.UserStats.get_handle().get_columns()
>>> # cols[0].name
>>> # cols[0].hide_sum
