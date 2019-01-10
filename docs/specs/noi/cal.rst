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


Don't read me
=============

Verify the window actions of some actors (:ticket:`2784`):

>>> for ba in rt.models.cal.MyEntries.get_actions():
...     if ba.action.is_window_action():
...         print(ba)
<BoundAction(cal.MyEntries, <lino.core.actions.ShowInsert insert ('New')>)>
<BoundAction(cal.MyEntries, <lino.core.actions.ShowDetail detail ('Detail')>)>
<BoundAction(cal.MyEntries, <lino.core.actions.ShowTable grid>)>


