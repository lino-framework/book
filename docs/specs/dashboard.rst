.. doctest docs/specs/dashboard.rst
.. _specs.dashboard:

====================================
The ``lino.modlib.dashboard`` plugin
====================================

>>> import lino
>>> lino.startup('lino_book.projects.team.settings.doctests')
>>> from lino.api.doctest import *
>>> from django.db.models import Q

As explained in :doc:`/dev/admin_main` you can define a sequence of
*dashboard items* for your application.  Lino renders these dashboard
items quite intelligently: they don't appear if the table contains no
data or if the user has no permission to see it.  But the *dashboard
items* of an application are *hard-coded* and *apply to all users*.
If this is a problem for you, you can install the
:mod:`lino.modlib.dashboard` plugin.


.. currentmodule:: lino.modlib.dashboard

.. contents:: Table of Contents
 :local:
 :depth: 2

List of available dashboard items
=================================

>>> user = rt.models.users.User.objects.get(username="robin")         
>>> pprint(list(settings.SITE.get_dashboard_items(user)))
[lino_xl.lib.cal.ui.MyTasks,
 lino_xl.lib.cal.ui.MyEntries,
 lino_xl.lib.cal.ui.MyOverdueAppointments,
 lino_xl.lib.cal.ui.MyUnconfirmedAppointments,
 lino.modlib.comments.ui.RecentComments,
 lino_xl.lib.tickets.ui.MyTickets,
 lino_xl.lib.tickets.ui.MySitesDashboard,
 lino_xl.lib.tickets.ui.TicketsToTriage,
 lino_xl.lib.tickets.ui.MyTicketsToWork,
 lino_xl.lib.working.ui.WorkedHours,
 lino.modlib.notify.models.MyMessages]

 
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
