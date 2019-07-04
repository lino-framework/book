.. doctest docs/specs/tickets.rst
.. _xl.specs.tickets:

===============================
``tickets`` (Ticket management)
===============================

The :mod:`lino_xl.lib.tickets` plugin adds functionality for managing tickets.

.. contents::
  :local:

.. currentmodule:: lino_xl.lib.tickets

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *


Overview
========

A `ticket <Tickets>`_ is a question, issue or problem reported by a human who
asks us for help.  It is the smallest unit for organizing our work.

This plugins also installs :doc:`comments`. Users can comment on a ticket.

Tickets are grouped into sites_. Users must be **subscribed** to a *site* in
order to report tickets on a site. All the subscribers of a site will get
notified about new tickets, changes and new comments to a ticket. The site* of
a *ticket* indicates who is going to watch changes on that ticket.


Tickets
=======

A **ticket** is a concrete question or problem formulated by a human who asks
our team to work on it and find an answer or solution.

The **author** of a ticket is the user who created it.  The author can
optionally specify an **end user**, which means that they created the ticket in
behalf* of that external person.

A ticket can be **assigned** to a given user who is "responsible" for working
on it.  It can be reassigned to another user.  Users can "take" an unassigned
ticket.


.. class:: Ticket

    The Django model used to represent a *ticket*.

    A ticket has the following database fields.

    Different relations to users:

    .. attribute:: user

        The author or reporter of this ticket. The user who reported this
        ticket to the database and is responsible for managing it.

    .. attribute:: end_user

        The end user who is asking for help.  This may be an external person
        who is not registered as a system user.

    .. attribute:: assigned_to

        The user who has been assigned to work on this ticket.

    Descriptive fields:

    .. attribute:: description

        A complete and concise description of the ticket. This should
        describe in more detail what this ticket is about. If the
        ticket has evolved during time, it should reflect the latest
        version.

        The description can contain *memo commands* defined by the
        application.

    .. attribute:: site

        The site this ticket belongs to.
        You can select only sites you are subscribed to.


    .. attribute:: upgrade_notes

        A formatted text field meant for writing instructions for the
        hoster's site administrator when doing an upgrade where this
        ticket is being deployed.


    .. attribute:: waiting_for

        What to do next. An unformatted one-line text which describes
        what this ticket is waiting for.

    .. attribute:: state

        The state of this ticket. See :class:`TicketStates`.

    Relations to other tickets:

    .. attribute:: duplicate_of

        A pointer to another ticket which is regarded as the first occurence of
        the same problem.

        A ticket with a non-empty :attr:`duplicate_of` field can be called a
        "duplicate".  The number (primary key) of a duplicate is theoretically
        higher than the number of the ticket it duplicates.

        The :attr:`state` of a duplicate does not automatically become
        that of the duplicated ticket.  Each ticket continues to have
        its own state. Example: Some long time ago, with Mathieu, we
        agreed that ticket #100 can go to *Sleeping*. Now Aurélie
        reported the same problem again as #904. This means that we
        should talk about it. And even before talking with her, I'd
        like to have a look at the code in order to estimate whether
        it is difficult or not, so I set the state of #904 to ToDo.

    .. attribute:: deadline

        Specify that the ticket must be done for a given date.

        TODO: Triagers should have a table of tickets having this
        field non-empty and are still in an active state.

    .. attribute:: priority

        How urgent this ticket is.

        Choicelist field pointing to :class:`lino_xl.lib.xl.Priorities`.

    .. attribute:: rating

        How the author rates the work which has been done on this ticket.

    .. attribute:: reporting_type

        An indication about who is going to pay for work on this
        site.  See :class:`ReportingTypes`.

Ticket state
============

The **state** of a ticket expresses in which phase of its life cycle this
ticket is.

You can see which ticket states are defined on your site
using :menuselection:`Explorer --> Tickets --> Ticket states`.

..  >>> show_menu_path(tickets.TicketStates)
    Explorer --> Tickets --> Ticket states

See :class:`lino_noi.lib.tickets.TicketStates` for a real world example.

.. class:: TicketStates

    The choicelist for the :attr:`state <Ticket.state>` of a ticket.



Sites
=====

A **site** is a place where work is being done.  Sites can be anything your
team uses for grouping their tickets into more long-term "tasks" or "projects".
Zulip calls them "streams", Slack calls them "Channels".


.. class:: Site

    The Django model representing a *site*.

    .. attribute:: description
    .. attribute:: reporting_type
    .. attribute:: state
    .. attribute:: ref
    .. attribute:: name
    .. attribute:: company
    .. attribute:: contact_person
    .. attribute:: deadline

.. class:: Sites

    .. attribute:: watcher
    .. attribute:: show_exposed
    .. attribute:: state
           
.. class:: MySites

    Shows the sites for which I have a subscription.

    Sleeping and closed sites are not shown by default.
    
List of the sites in our demo database:

>>> rt.show(tickets.Sites)
=========== ============= ======== ======== ============= ====
 Reference   Designation   Client   Remark   Workflow      ID
----------- ------------- -------- -------- ------------- ----
             pypi          pypi              **⛶ Draft**   3
             welket        welket            **⛶ Draft**   1
             welsch        welsch            **⛶ Draft**   2
=========== ============= ======== ======== ============= ====
<BLANKLINE>

List of sites to which Jean is subscribed:

>>> rt.login("jean").show(tickets.MySites)
===================== ============= =============
 Site                  Description   Workflow
--------------------- ------------- -------------
 `welsch <Detail>`__                 **⛶ Draft**
===================== ============= =============
<BLANKLINE>


List of tickets which have not yet been assigned to a site:

>>> pv = dict(has_site=dd.YesNo.no)
>>> rt.show(tickets.AllTickets, param_values=pv)
... #doctest: -REPORT_UDIFF +ELLIPSIS
===== ============================================== ========== =============== ======
 ID    Summary                                        Priority   Workflow        Site
----- ---------------------------------------------- ---------- --------------- ------
 110   Why is foo so bar                              Normal     **☐ Ready**
 90    No more foo when bar is gone                   Normal     **☎ Talk**
 70    'NoneType' object has no attribute 'isocode'   Normal     **☐ Ready**
 40    How can I see where bar?                       Normal     **☒ Refused**
 20    Why is foo so bar                              Normal     **⚒ Working**
===== ============================================== ========== =============== ======
<BLANKLINE>


Subscriptions
=============
           
           
.. class:: Subscription

    The Django model representing a *subscription*.

    .. attribute:: site

        The site.
                   
    .. attribute:: user

        The user.
                   
    .. attribute:: primary

        Whether this is the primary subscription of this user.

        Checking this field will automatically uncheck any 
        previous primary subscriptions.
           


Ticket types
============

A **ticket type**, or the type of a *ticket*, is a way to classify that ticket.
This information may be used in service reports or statistics defined by the
application.

You can configure the list of ticket types via :menuselection:`Configure -->
Tickets --> Ticket types`.

..  >>> show_menu_path(tickets.TicketTypes)
    Configure --> Tickets --> Ticket types

The :fixture:`demo` fixture defines the following ticket types.

>>> rt.show(tickets.TicketTypes)
============= ================== ================== ================
 Designation   Designation (de)   Designation (fr)   Reporting type
------------- ------------------ ------------------ ----------------
 Bugfix        Bugfix             Bugfix
 Enhancement   Enhancement        Enhancement
 Upgrade       Upgrade            Upgrade
============= ================== ================== ================
<BLANKLINE>


.. class:: TicketType

    The Django model used to represent a *ticket type*.

    .. attribute:: name

    .. attribute:: reporting_type

        Which *reporting type* to use in a service report.
        See :class:ReportingTypes`.

.. class:: TicketTypes

    The list of all ticket types.




Deciding what to do next
========================

Show all active tickets reported by me.

>>> rt.login('jean').show(tickets.MyTickets)
... #doctest: -REPORT_UDIFF
========== ==================================================================== ============= ============== ========= ======= ====== =============================================
 Priority   Ticket                                                               Assigned to   Planned time   Regular   Extra   Free   Workflow
---------- -------------------------------------------------------------------- ------------- -------------- --------- ------- ------ ---------------------------------------------
 Normal     `#113 (⛶ Misc optimizations in Baz) <Detail>`__                                                                            [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 Normal     `#106 (☎ 'NoneType' object has no attribute 'isocode') <Detail>`__   Jean                                                  [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal     `#99 (☉ No more foo when bar is gone) <Detail>`__                    Luc                                                   [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal     `#92 (⚒ Why is foo so bar) <Detail>`__                               Mathieu                                               [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal     `#78 (☐ Default account in invoices per partner) <Detail>`__         Jean                                                  [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal     `#57 (⛶ Irritating message when bar) <Detail>`__                                                                           [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 Normal     `#50 (☎ Misc optimizations in Baz) <Detail>`__                       Jean                                                  [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal     `#43 (☉ 'NoneType' object has no attribute 'isocode') <Detail>`__    Luc                                                   [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal     `#36 (⚒ No more foo when bar is gone) <Detail>`__                    Mathieu                                               [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal     `#22 (☐ How can I see where bar?) <Detail>`__                        Jean                                                  [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal     `#1 (⛶ Föö fails to bar when baz) <Detail>`__                                                                              [✋] [■] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
========== ==================================================================== ============= ============== ========= ======= ====== =============================================
<BLANKLINE>


The state of a site
===================

>>> rt.show(tickets.SiteStates)
... #doctest: +REPORT_UDIFF +ELLIPSIS
======= ========== ========== ============= =========
 value   name       text       Button text   Exposed
------- ---------- ---------- ------------- ---------
 10      draft      Draft      ⛶             Yes
 20      active     Active     ⚒             Yes
 30      stable     Stable     ☉             Yes
 40      sleeping   Sleeping   ☾             No
 50      closed     Closed     ☑             No
======= ========== ========== ============= =========
<BLANKLINE>



The backlog
===========

The :class:`TicketsBySite` panel shows all the tickets for a given site. It is
a scrum backlog.

>>> welket = tickets.Site.objects.get(name="welket")
>>> rt.show(tickets.TicketsBySite, welket)
... #doctest: +REPORT_UDIFF -SKIP +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ========================================================= ============== =========== ======= ====== ===============
 Priority              Ticket                                                    Planned time   Regular     Extra   Free   Workflow
--------------------- --------------------------------------------------------- -------------- ----------- ------- ------ ---------------
 Normal                *#116 (⚒ Foo never bars)*                                                                           **⚒ Working**
 Normal                *#115 (☉ 'NoneType' object has no attribute 'isocode')*                                             **☉ Open**
 Normal                *#114 (☎ Default account in invoices per partner)*                                                  **☎ Talk**
 Normal                *#108 (⚒ No more foo when bar is gone)*                                                             **⚒ Working**
 Normal                *#106 (☎ 'NoneType' object has no attribute 'isocode')*                                             **☎ Talk**
 Normal                *#102 (☐ Irritating message when bar)*                                                              **☐ Ready**
 Normal                *#98 (☎ Foo never bars)*                                                                            **☎ Talk**
 ...
 Normal                *#12 (⚒ Foo cannot bar)*                                                                            **⚒ Working**
 Normal                *#10 (☎ Where can I find a Foo when bazing Bazes?)*                                                 **☎ Talk**
 Normal                *#6 (☐ Sell bar in baz)*                                                                            **☐ Ready**
 Normal                *#4 (⚒ Foo and bar don't baz)*                                           1:24                       **⚒ Working**
 Normal                *#2 (☎ Bar is not always baz)*                                           9:40                       **☎ Talk**
 Normal                *#1 (⛶ Föö fails to bar when baz)*                                                                  **⛶ New**
 **Total (46 rows)**                                                                            **11:04**
===================== ========================================================= ============== =========== ======= ====== ===============
<BLANKLINE>

Note that the above table shows no state change actions in the
`Workflow` column.  That's because in this doctest it is being
requested by anonymous. For an authenticated developer it looks like
this:

>>> rt.login("robin").show(tickets.TicketsBySite, welket)
... #doctest: +REPORT_UDIFF -SKIP +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ==================================================================== ============== =========== ======= ====== =============================================
 Priority              Ticket                                                               Planned time   Regular     Extra   Free   Workflow
--------------------- -------------------------------------------------------------------- -------------- ----------- ------- ------ ---------------------------------------------
 Normal                `#116 (⚒ Foo never bars) <Detail>`__                                                                           [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#115 (☉ 'NoneType' object has no attribute 'isocode') <Detail>`__                                             [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal                `#114 (☎ Default account in invoices per partner) <Detail>`__                                                  [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#108 (⚒ No more foo when bar is gone) <Detail>`__                                                             [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#106 (☎ 'NoneType' object has no attribute 'isocode') <Detail>`__                                             [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#102 (☐ Irritating message when bar) <Detail>`__                                                              [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal                `#98 (☎ Foo never bars) <Detail>`__                                                                            [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 ...
 Normal                `#6 (☐ Sell bar in baz) <Detail>`__                                                                            [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal                `#4 (⚒ Foo and bar don't baz) <Detail>`__                                           1:24                       [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#2 (☎ Bar is not always baz) <Detail>`__                                           9:40                       [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#1 (⛶ Föö fails to bar when baz) <Detail>`__                                                                  [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 **Total (46 rows)**                                                                                       **11:04**
===================== ==================================================================== ============== =========== ======= ====== =============================================
<BLANKLINE>



Links between tickets
=====================

.. class:: Link
.. class:: LinkType

.. class:: Links
.. class:: LinksByTicket

.. class:: LinkTypes

    A choicelist with the possible link types.

    .. attribute:: requires

        The parent ticket requires the child ticket.
    
    .. attribute:: triggers

        The parent ticket triggers the child ticket.
    
    .. attribute:: deploys

        The parent ticket is a deployment which deploys the child ticket.

        Release notes are a printout of a deployment ticket which
        lists the deployed tickets.


>>> rt.show(tickets.LinkTypes)
... #doctest: +REPORT_UDIFF
======= =========== ===========
 value   name        text
------- ----------- -----------
 10      requires    Requires
 20      triggers    Triggers
 30      suggests    Suggests
 40      obsoletes   Obsoletes
======= =========== ===========
<BLANKLINE>




>>> rt.show(tickets.Links)
... #doctest: +REPORT_UDIFF
==== ================= ================================== ==============================
 ID   Dependency type   Parent                             Child
---- ----------------- ---------------------------------- ------------------------------
 1    Requires          #1 (⛶ Föö fails to bar when baz)   #2 (☎ Bar is not always baz)
==== ================= ================================== ==============================
<BLANKLINE>


Comments
========

In :ref:`noi` comments are visible even to anonymous users:

>>> rt.show(comments.Comments, column_names="id user owner")
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
==== ================= ===================================================================
 ID   Author            Controlled by
---- ----------------- -------------------------------------------------------------------
 1    Jean              `#1 (⛶ Föö fails to bar when baz) <Detail>`__
 2    Luc               `#2 (☎ Bar is not always baz) <Detail>`__
 3    Marc              `#3 (☉ Baz sucks) <Detail>`__
 4    Mathieu           `#4 (⚒ Foo and bar don't baz) <Detail>`__
 5    Romain Raffault   `#5 (☾ Cannot create Foo) <Detail>`__
 6    Rolf Rompen       `#6 (☐ Sell bar in baz) <Detail>`__
 7    Robin Rood        `#7 (☑ No Foo after deleting Bar) <Detail>`__
 8    Jean              `#8 (☒ Is there any Bar in Foo?) <Detail>`__
 9    Luc               `#9 (⛶ Foo never matches Bar) <Detail>`__
 10   Marc              `#10 (☎ Where can I find a Foo when bazing Bazes?) <Detail>`__
 11   Mathieu           `#11 (☉ Class-based Foos and Bars?) <Detail>`__
 12   Romain Raffault   `#12 (⚒ Foo cannot bar) <Detail>`__
 13   Rolf Rompen       `#13 (☾ Bar cannot foo) <Detail>`__
 14   Robin Rood        `#14 (☐ Bar cannot baz) <Detail>`__
 15   Jean              `#15 (☑ Bars have no foo) <Detail>`__
 ...
 80   Marc              `#80 (☒ Foo never bars) <Detail>`__
 81   Mathieu           `#81 (⛶ No more foo when bar is gone) <Detail>`__
 82   Romain Raffault   `#82 (☎ Cannot delete foo) <Detail>`__
 83   Rolf Rompen       `#83 (☉ Why is foo so bar) <Detail>`__
 84   Robin Rood        `#84 (⚒ Irritating message when bar) <Detail>`__
==== ================= ===================================================================
<BLANKLINE>



>>> obj = tickets.Ticket.objects.get(pk=2)
>>> rt.login('luc').show(comments.CommentsByRFC, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
<p><b>Write comment</b></p><ul><li><a ...>...</a> by <a href="Detail">Luc</a> [<b> Reply </b>] <a ...>⁜</a><div id="comment-2"><p>Very confidential comment</p></div></li></ul>



Filtering tickets
=================

This is a list of the parameters you can use for filterings tickets.

>>> show_fields(tickets.AllTickets, all=True)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
+--------------------+--------------------+-----------------------------------------------------------------------+
| Internal name      | Verbose name       | Help text                                                             |
+====================+====================+=======================================================================+
| user               | Author             | The author or reporter of this ticket. The user who reported this     |
|                    |                    | ticket to the database and is responsible for managing it.            |
+--------------------+--------------------+-----------------------------------------------------------------------+
| end_user           | End user           | Only rows concerning this end user.                                   |
+--------------------+--------------------+-----------------------------------------------------------------------+
| assigned_to        | Assigned_to        | Only tickets with this user assigned.                                 |
+--------------------+--------------------+-----------------------------------------------------------------------+
| not_assigned_to    | Not assigned to    | Only that this user is not assigned to.                               |
+--------------------+--------------------+-----------------------------------------------------------------------+
| interesting_for    | Interesting for    | Only tickets interesting for this partner.                            |
+--------------------+--------------------+-----------------------------------------------------------------------+
| site               | Site               | Select a site if you want to see only tickets for this site.          |
+--------------------+--------------------+-----------------------------------------------------------------------+
| has_site           | Has site           | Show only (or hide) tickets which have a site assigned.               |
+--------------------+--------------------+-----------------------------------------------------------------------+
| state              | State              | Only rows having this state.                                          |
+--------------------+--------------------+-----------------------------------------------------------------------+
| priority           | Priority           | Only rows having this priority.                                       |
+--------------------+--------------------+-----------------------------------------------------------------------+
| show_assigned      | Assigned           | Show only (or hide) tickets that are assigned to somebody.            |
+--------------------+--------------------+-----------------------------------------------------------------------+
| show_active        | Active             | Show only (or hide) tickets which are active (i.e. state is Talk      |
|                    |                    | or ToDo).                                                             |
+--------------------+--------------------+-----------------------------------------------------------------------+
| show_todo          | To do              | Show only (or hide) tickets which are todo (i.e. state is New         |
|                    |                    | or ToDo).                                                             |
+--------------------+--------------------+-----------------------------------------------------------------------+
| show_private       | Private            | Show only (or hide) tickets that are marked private.                  |
+--------------------+--------------------+-----------------------------------------------------------------------+
| start_date         | Date from          | Start of observed date range                                          |
+--------------------+--------------------+-----------------------------------------------------------------------+
| end_date           | until              | End of observed date range                                            |
+--------------------+--------------------+-----------------------------------------------------------------------+
| observed_event     | Observed event     |                                                                       |
+--------------------+--------------------+-----------------------------------------------------------------------+
| has_ref            | Has reference      |                                                                       |
+--------------------+--------------------+-----------------------------------------------------------------------+
| last_commenter     | Commented Last     | Only tickets that have this use commenting last.                      |
+--------------------+--------------------+-----------------------------------------------------------------------+
| not_last_commenter | Not Commented Last | Only tickets where this use is not the last commenter.                |
+--------------------+--------------------+-----------------------------------------------------------------------+
| subscriber         | Site Subscriber    | Limit tickets to tickets that have a site this user is subscribed to. |
+--------------------+--------------------+-----------------------------------------------------------------------+




Plugin configuration
====================

See :class:`lino_xl.lib.tickets.Plugin`.


Discussions
===========


Should we replace the :attr:`Ticket.duplicate_of` field by a link type (an
additional choice in :class:`LinkTypes`) called "Duplicated/Duplicated by"? No.
We had this before and preferred the field, because a field is at least one
click less, and because we *want* users to define a clear hierarchy with a
clear root ticket. You can have a group of tickets which are all direct or
indirect duplicates of this "root of all other problems".

Sometimes there is nothing to do for a ticket, but it is not "sleeping" because
it might become active at any moment when some kind of event happens. (e.g. a
customer answers a callback, a server error occurs again). Should we introduce
a new state "Waiting" to differentiate such tickets from those who went asleep
due to lack of attention? Rather not. That's what "Sleeping" (also) means. A
sleeping ticket can wake up any time. We just don't want to be reminded about
it all the time. One challenge is that when the "trigger" occurs which would
wake up the sleeping ticket. At that moment we don't want to create a new
ticket just because we forgot about the sleeping one. To avoid this we must
currently simply search in "All tickets" before creating a new one.


Other languages
===============

The ticket states in German:

>>> rt.show(tickets.TicketStates, language="de")
====== =========== ================ ============= =======
 Wert   name        Text             Button text   Aktiv
------ ----------- ---------------- ------------- -------
 10     new         Neu              ⛶             Ja
 15     talk        Besprechen       ☎             Ja
 20     opened      Offen            ☉             Ja
 22     working     In Bearbeitung   ⚒             Ja
 30     sleeping    Schläft          ☾             Nein
 40     ready       Bereit           ☐             Ja
 50     closed      Abgeschlossen    ☑             Nein
 60     cancelled   Abgelehnt        ☒             Nein
====== =========== ================ ============= =======
<BLANKLINE>



Views reference
===============

There are many tables used to show lists of tickets.

.. class:: Tickets

    Base class for all tables of tickets.

    .. attribute:: site

        Select a site if you want to see only tickets for this site.

    .. attribute:: show_private

        Show only (or hide) tickets that are marked private.

    .. attribute:: show_todo

        Show only (or hide) tickets which are todo (i.e. state is New
        or ToDo).

    .. attribute:: show_active

        Show only (or hide) tickets which are active (i.e. state is Talk
        or ToDo).

    .. attribute:: show_assigned

        Show only (or hide) tickets that are assigned to somebody.

    .. attribute:: has_site

        Show only (or hide) tickets which have a site assigned.

    .. attribute:: feasable_by

        Show only tickets for which the given supplier is competent.


.. class:: AllTickets

    Shows all tickets.

.. class:: RefTickets

    Shows all tickets that have a reference.

.. class:: PublicTickets

    Shows all public tickets.

.. class:: TicketsToTriage

    Shows tickets that need to be triaged.  Currently this is
    equivalent to those having their state set to :attr:`new
    <TicketStates.new>`.

.. class:: TicketsToTalk

.. class:: TicketsNeedingMyFeedback

    Shows tickets that are waiting for my feedback.

    These are tickets in state Talk where you are not the last commenter.
    Only tickets on sites that you are subscribed to.
    Includes tickets with no comments.

.. class:: MyTicketsNeedingFeedback

    Shows tickets assigned to me and waiting for feedback from others.

    Shows tickets of sites that you are subscribed to which are in state Talk
    where you are the last commenter.

.. class:: UnassignedTickets
.. class:: ActiveTickets

    Show all tickets that are in an active state.

.. class:: MyTickets

    Show all active tickets reported by me.



.. class:: TicketsByEndUser
.. class:: TicketsByType

.. class:: DuplicatesByTicket

    Shows the tickets which are marked as duplicates of this
    (i.e. whose `duplicate_of` field points to this ticket.


.. class:: TicketsSummary

    Abstract base class for ticket tables with a summary.

.. class:: MyTicketsToWork

    Show all active tickets assigned to me.

.. class:: TicketsBySite



