.. doctest docs/specs/noi/cal.rst
.. _noi.specs.cal:

=======================================
``cal`` : Calendar functionality in Noi
=======================================

.. currentmodule:: lino_noi.lib.cal

The :mod:`lino_noi.lib.cal` adds calendar functionality.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.noi1e.settings.demo')
>>> from lino.api.doctest import *

>>> ses = rt.login('jean')
>>> cal.Task(user=ses.get_user())
Task(user=187,priority=<xl.Priorities.normal:30>,state=<cal.TaskStates.todo:10>)


Don't read me
=============

Verify the window actions of some actors (:ticket:`2784`):

>>> for ba in rt.models.cal.MyEntries.get_actions():
...     if ba.action.is_window_action():
...         ba
<BoundAction(cal.MyEntries, <lino.core.actions.ShowInsert insert ('New')>)>
<BoundAction(cal.MyEntries, <lino.core.actions.ShowDetail detail ('Detail')>)>
<BoundAction(cal.MyEntries, <lino.core.actions.ShowTable grid>)>
