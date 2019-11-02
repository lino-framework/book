.. doctest docs/specs/dashboard.rst
.. _specs.dashboard:

======================================
``dashboard`` : customizable dashboard
======================================

.. currentmodule:: lino.modlib.dashboard

The :mod:`lino.modlib.dashboard` plugin adds functionality for letting the
users customize their dashboard.

As explained in :doc:`/dev/admin_main` you can define a sequence of
*dashboard items* for your application.  Lino renders these dashboard
items quite intelligently: they don't appear if the table contains no
data or if the user has no permission to see it.  But the *dashboard
items* of an application are *hard-coded* and *apply to all users*.


.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.team.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q

Which means that code snippets in this document are tested using the
:mod:`lino_book.projects.team` demo project.


List of available dashboard items
=================================

>>> user = rt.models.users.User.objects.get(username="robin")
>>> pprint(list(settings.SITE.get_dashboard_items(user)))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
[lino_xl.lib.cal.ui.MyTasks,
 <class 'lino.core.dashboard.ActorItem'>(cal.MyEntries,header_level=2,min_count=None),
 lino_xl.lib.cal.ui.MyOverdueAppointments,
 lino_xl.lib.cal.ui.MyUnconfirmedAppointments,
 lino_xl.lib.cal.ui.DailyPlanner,
 lino.modlib.comments.ui.RecentComments,
 lino_xl.lib.tickets.ui.MyTickets,
 lino_xl.lib.tickets.ui.MySites,
 lino_xl.lib.tickets.ui.TicketsToTriage,
 lino_xl.lib.tickets.ui.MyTicketsToWork,
 lino_xl.lib.tickets.ui.TicketsNeedingMyFeedback,
 lino_xl.lib.tickets.ui.MyTicketsNeedingFeedback,
 lino_xl.lib.working.ui.WorkedHours,
 lino.modlib.notify.models.MyMessages,
 lino_xl.lib.groups.models.MyGroups]


As long as a user didn't populate their dashboard, the list ist empty
and they will get all the dashboard items provided by the application.

.. figure:: /specs/noi/dashboard1.png
   :width: 80 %

   Dashboard preferences (empty)

Click the :guilabel:`⚡` button in order to populate the table.


.. figure:: /specs/noi/dashboard2.png
   :width: 80 %

   Dashboard preferences (populated)

Now you can hide individual items and change their order.
