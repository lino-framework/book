.. doctest docs/dev/admin_main.rst
.. _dev.admin_main:

===============
The main window
===============

This page explains the elements of the :term:`main window` of a Lino
application: :term:`quick links <quick link>`, :term:`welcome messages <welcome
message>` and :term:`dashboard items <dashboard item>`. It also gives some ideas
for customizing it. See `Behind the scenes`_.

.. contents::
  :local:


Vocabulary
==========

.. glossary::

  main window

    The inner content of the home page presented to the user after signing in
    and before opening any other window (:term:`detail window` or :term:`grid
    window`).

  quick link

    A shortcut link in the main window.

    See `Quick links`_ below.

  welcome message

    A short message to inform the :term:`end user` about something after signing
    in.

    Welcome messages are being generated dynamically each time your main window
    is being displayed. Unlike notifications you don't get rid of them by
    marking them as seen.

    See `Welcome messages`_ below.

  dashboard item

    An actor that is rendered directly (inline) into the main window because it
    is considered an important entry point.

  dashboard

    The area of the main window where :term:`dashboard items <dashboard item>`
    are being displayed.

    See `The dashboard`_ below.


.. include:: /../docs/shared/include/tested.rst

Code snippets in this document are tested using the
:mod:`lino_book.projects.noi1e` demo project.

>>> import lino
>>> lino.startup('lino_book.projects.noi1e.settings.doctests')
>>> from lino.api.doctest import *
>>> ar = rt.login("robin")
>>> user = ar.get_user()


Quick links
===========

As the :term:`application developer` you define quick links by overriding the
:meth:`setup_quicklinks <lino.core.site.Site.setup_quicklinks>` methods of your
:class:`Site <lino.core.site.Site>` class.

For example the :mod:`lino.modlib.about` plugin says::

  class Plugin(Plugin):

      def get_quicklinks(site, user):
          yield 'about.SiteSearch'

Or the the :mod:`lino_noi.lib.noi.settings` module says::

  class Site(Site):
      ...
      def setup_quicklinks(self, user, tb):
          super(Site, self).setup_quicklinks(user, tb)
          tb.add_action(self.models.tickets.RefTickets)
          ...
          tb.add_action(
              self.models.tickets.AllTickets.insert_action,
              label=_("Submit a ticket"))
          ...
          a = self.models.users.MySettings.default_action
          tb.add_instance_action(user, action=a, label=_("My settings"))


The front end basically calls :meth:`lino.core.Site.get_quicklinks` to retrieve
and then render this information.

>>> q = settings.SITE.get_quicklinks(user)
>>> print(menu2rst(q))
Reference Tickets, Active tickets, All tickets, Submit a ticket, My settings

The object returned by  :meth:`get_quicklinks <lino.core.Site.get_quicklinks>`
is an instance of :class:`lino.core.menus.Toolbar`.

>>> q.__class__
<class 'lino.core.menus.Toolbar'>


Welcome messages
================

As the application developer you have several methods to define welcome
messages:

- Set :attr:`welcome_message_when_count
  <lino.core.actors.Actor.welcome_message_when_count>` of some table
  to some value (usually ``0``).

  For example the :mod:`lino_xl.lib.tickets` uses this to define the
  "You have X items in Tickets to triage" message.

- Define a **custom welcome message** using
  :meth:`dd.add_welcome_handler
  <lino.core.site.Site.add_welcome_handler>`.

  For example the "You are busy with..." message in :ref:`noi` is
  :mod:`lino_xl.lib.working.models`.  Or
  :mod:`lino_xl.lib.stars.models` defines the "Your stars are"
  message.

The :xfile:`admin_main.html` calls :meth:`get_welcome_messages
<lino.core.site.Site.get_welcome_messages>`.  This code inserts the "welcome
messages" for this user on this site. :meth:`get_welcome_messages
<lino.core.site.Site.get_welcome_messages>` returns an etree element (see
:mod:`etgen.html`).

>>> print(tostring(settings.SITE.get_welcome_messages(ar)))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
<p><span><a href="Detail">Jean</a> is working on: <a title="Föö fails to bar
when baz" href="Detail">#1 (⚹ Föö fails to bar when
baz)</a>.</span><br/><span><a href="Detail">Luc</a> is working on: <a title="Föö
fails to bar when baz" href="Detail">#1 (⚹ Föö fails to bar when
baz)</a>.</span><br/><span><a href="Detail">Mathieu</a> is working on: <a
title="Föö fails to bar when baz" href="Detail">#1 (⚹ Föö fails to bar when
baz)</a>.</span></p><span>You have <b>15 items in Tickets to
triage</b>.</span><span>You have <b>7 items in New user applications</b>.</span>




.. _dev.dasboard:

The dashboard
=============

As the :term:`application developer` you define which actors are available as
:term:`dashboard item` for your application.  You can do this in two different
ways:

- override the :meth:`get_dashboard_items
  <lino.core.plugin.Plugin.get_dashboard_items>` of your :class:`Plugin
  <lino.core.plugin.Plugin>` classes.

- override the
  :meth:`get_dashboard_items
  <lino.core.site.Site.get_dashboard_items>`
  of your :class:`Site <lino.core.site.Site>` class.

This list is *hard-coded* per application and *applies to all users*. But Lino
respects view permissions, i.e. an item will appear only if the user has
permission to see it. For each dashboard item you can specify certain options to
influence how Lino renders them. For example they usually don't appear if the
table contains no data.

Independently of how you define the dashboard items for your application, you
can additionally opt to install the :mod:`lino.modlib.dashboard` plugin.


List of available dashboard items
=================================

The list of available dashboard items exists also without this plugin.

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


See :doc:`/specs/dashboard`.



Behind the scenes
=================

The content of the main window is generated from the :xfile:`admin_main.html`
template.

.. xfile:: admin_main_base.html
.. xfile:: admin_main.html

This is the template used to generate the content of the main window.
It is split into two files :srcref:`admin_main.html
<lino/config/admin_main.html>` and :srcref:`admin_main_base.html
<lino/config/admin_main_base.html>`.

For illustration compare the content of the latter template with its
result in the following screenshots (taken from the :mod:`noi1e
<lino_book.projects.noi1e>` demo project which runs :ref:`noi`).

.. figure:: /specs/noi/admin_main_000.png
   :width: 80 %

   Main window for AnonymousUser.

.. figure:: /specs/noi/admin_main_900.png
   :width: 80 %

   Main window for user ``robin``.

Customizing the main window
===========================

You may define a custom :xfile:`admin_main.html` template, as we did
in :doc:`/dev/polls/index`. But this was rather an exercise for pedagogical
reasons than something we would recommend to do for application developers.

You may even go further and override the :meth:`get_main_html
<lino.core.site.Site.get_main_html>` method of your :class:`Site
<lino.core.site.Site>` class to return your own html.
