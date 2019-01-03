.. doctest docs/specs/noi/cal.rst
.. _noi.specs.cal:

=======================================
``cal`` : Calendar functionality in Noi
=======================================

.. currentmodule:: lino_noi.lib.cal

The :mod:`lino_noi.lib.cal` adds calendar functionality.

.. contents::
  :local:



.. include:: /include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *


>>> cal.Days
lino_noi.lib.cal.models.Days

>>> print(cal.Days.column_names)
detail_link worked_tickets  vc0:5 vc1:5 vc2:5 vc3:5 *

>>> cal.Days.get_data_elem('detail_link')
lino_noi.lib.cal.models.Days.detail_link

>>> ses = rt.login('jean')
>>> cal.Task(user=ses.get_user())
Task(user=107,priority=<Priorities.normal:30>,state=<TaskStates.todo:10>)
