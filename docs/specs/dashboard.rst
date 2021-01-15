.. doctest docs/specs/dashboard.rst
.. _specs.dashboard:

======================================
``dashboard`` : customizable dashboard
======================================

.. currentmodule:: lino.modlib.dashboard

The :mod:`lino.modlib.dashboard` plugin adds functionality for letting the users
customize their :term:`dashboard`.

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.noi1e.settings.doctests')
>>> from lino.api.doctest import *

Which means that code snippets in this document are tested using the
:mod:`lino_book.projects.noi1e` demo project.

What are dashboard items?
=========================

A **dashboard item** is an actor that can appear directly in the main window.

As the :term:`application developer` you define the list of available *dashboard
items* for your application. This list is *hard-coded* per application and
*applies to all users*. But Lino respects view permissions, i.e. an item will
appear only if the user has permission to see it. For each dashboard item you
can specify certain options to influence how Lino renders them. For example they
usually don't appear if the table contains no data.

How to define your application's dashboard items:

- override the
  :meth:`get_dashboard_items
  <lino.core.site.Site.get_dashboard_items>`
  of your :class:`Site <lino.core.site.Site>` class.

- override the :meth:`get_dashboard_items
  <lino.core.plugin.Plugin.get_dashboard_items>` of your :class:`Plugin
  <lino.core.plugin.Plugin>` classes.

Independently of how you define the dashboard items for your application, you
can additionally opt to install the :mod:`lino.modlib.dashboard` plugin.


List of available dashboard items
=================================

The list of available dashboard items exists also without this plugin.

>>> user = rt.models.users.User.objects.get(username="robin")
>>> pprint(list(settings.SITE.get_dashboard_items(user)))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
[lino_xl.lib.cal.ui.MyTasks,
 lino.core.dashboard.ActorItem(cal.MyEntries,header_level=2,min_count=None),
 lino_xl.lib.cal.ui.MyOverdueAppointments,
 lino_xl.lib.cal.ui.MyUnconfirmedAppointments,
 lino_xl.lib.cal.ui.MyPresences,
 lino_xl.lib.calview.ui.DailyPlanner,
 lino.modlib.comments.ui.RecentComments,
 lino_xl.lib.tickets.ui.MyTickets,
 lino_xl.lib.tickets.ui.MySites,
 lino_xl.lib.tickets.ui.TicketsToTriage,
 lino_xl.lib.tickets.ui.MyTicketsToWork,
 lino_xl.lib.tickets.ui.TicketsNeedingMyFeedback,
 lino_xl.lib.tickets.ui.MyTicketsNeedingFeedback,
 lino_xl.lib.working.ui.WorkedHours,
 lino.modlib.notify.models.MyMessages,
 lino_xl.lib.groups.models.MyGroups,
 lino_xl.lib.ledger.ui.JournalsOverview]

Note that in practice you would probably prefer to not use above list directly,
but rather its "processed" form, stored in the user's preferences:

>>> pprint(user.get_preferences().dashboard_items)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
[lino.core.dashboard.ActorItem(cal.MyTasks,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(cal.MyEntries,header_level=2,min_count=None),
 lino.core.dashboard.ActorItem(cal.MyOverdueAppointments,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(cal.MyUnconfirmedAppointments,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(cal.MyPresences,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(calview.DailyPlanner,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(comments.RecentComments,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(tickets.MyTickets,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(tickets.MySites,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(tickets.TicketsToTriage,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(tickets.MyTicketsToWork,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(tickets.TicketsNeedingMyFeedback,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(tickets.MyTicketsNeedingFeedback,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(working.WorkedHours,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(notify.MyMessages,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(groups.MyGroups,header_level=2,min_count=1),
 lino.core.dashboard.ActorItem(ledger.JournalsOverview,header_level=2,min_count=1)]

As long as a user didn't populate their dashboard, the list is empty and they
will get all the dashboard items provided by the application.

.. figure:: /specs/noi/dashboard1.png
   :width: 80 %

   Dashboard preferences (empty)

Click the :guilabel:`⚡` button in order to populate the table.


.. figure:: /specs/noi/dashboard2.png
   :width: 80 %

   Dashboard preferences (populated)

Now you can hide individual items and change their order.
