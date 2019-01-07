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


>>> cal.LastWeek
lino_xl.lib.cal.ui.LastWeek

>>> ses = rt.login('jean')
>>> cal.Task(user=ses.get_user())
Task(user=107,priority=<Priorities.normal:30>,state=<TaskStates.todo:10>)
