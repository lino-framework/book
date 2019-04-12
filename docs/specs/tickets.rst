.. doctest docs/specs/noi/tickets.rst
.. _xl.specs.tickets:

===============================
``tickets`` (Ticket management)
===============================

The :mod:`lino_xl.lib.tickets` plugin adds functionality for managing
tickets and projects.

.. contents::
  :local:

.. currentmodule:: lino_xl.lib.tickets

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *


Overview
========

A **ticket** is a concrete question or problem formulated by a user. The user
may be a system user or an end user represented by a system user.  It is the
smallest unit of work.

A **site** is a place where work is being done. Zulip calls it "stream", Slack
calls it "Channel" A site can be anything your team uses for grouping their
tickets into more long-term "tasks" or "projects".

The *site* of a *ticket* indicates who is going to read that ticket.  All the
subscribers of a site will get notified about every new comment.

The *site* of a *ticket* also indicates "who is going to pay" for it.
Lino Noi does not issue invoices, so it uses this information only for
reporting about it and helping with the decision about whether and how
worktime is being invoiced to the customer.



Tickets
=======

.. class:: Ticket

    The Django model used to represent a *ticket*.

    A ticket has the following database fields.

    Different relations to users:

    .. attribute:: user

        The author. The user who reported this ticket to the database
        and is responsible for managing it.

    .. attribute:: end_user

        The end user who is asking for help.

    Descriptive fields:

    .. attribute:: description

        A complete and concise description of the ticket. This should
        describe in more detail what this ticket is about. If the
        ticket has evolved during time, it should reflect the latest
        version.

        The description can contain *memo commands* defined by the
        application.

    .. attribute:: upgrade_notes

        A formatted text field meant for writing instructions for the
        hoster's site administrator when doing an upgrade where this
        ticket is being deployed.


    .. attribute:: state

        The state of this ticket. See :class:`TicketStates
        <lino_xl.lib.tickets.choicelists.TicketStates>`

    .. attribute:: waiting_for

        What to do next. An unformatted one-line text which describes
        what this ticket is waiting for.

    .. attribute:: duplicate_of

        A pointer to the ticket which is the cause of this ticket.

        A ticket with a non-empty :attr:`duplicate_of` field can be
        called a "duplicate".  The number of a duplicate is
        theoretically higher than the number of the ticket it
        duplicates.

        The :attr:`state` of a duplicate does not automatically become
        that of the duplicated ticket.  Each ticket continues to have
        its own state. Example: Some long time ago, with Mathieu, we
        agreed that ticket #100 can go to *Sleeping*. Now Aurélie
        reported the same problem again as #904. This means that we
        should talk about it. And even before talking with her, I'd
        like to have a look at the code in order to estimate whether
        it is difficult or not, so I set the state of #904 to ToDo.

        Wouldn't it be preferrable to replace the :attr:`duplicate_of
        field by a :class:`LinkType
        <lino_xl.lib.tickets.choicelists.LinkTypes>` called
        "Duplicated/Duplicated by"?  No. We had this before and
        preferred the field, because a field is at least one click
        less, and because we *want* users to define a clear hiearchy
        with a clear root ticket. You can have a group of tickets
        which are all direct or indirect duplicates of this "root of
        all other problems".

    .. attribute:: deadline

        Specify that the ticket must be done for a given date.

        TODO: Triagers should have a table of tickets having this
        field non-empty and are still in an active state.

    .. attribute:: priority

        How urgent this ticket is.

        Choicelist field pointing to :class:`lino_xl.lib.xl.Priorities`.

    .. attribute:: rating

        How the author rates this ticket.

    .. attribute:: reporting_type

        An indication about who is going to pay for work on this
        site.  See :class:`ReportingTypes`.

    .. attribute:: site

        The site this ticket belongs to.
        You can select only sites you are subscribed to.


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

           

Ticket types
============

.. class:: TicketType

    .. attribute:: name

    .. attribute:: reporting_type

.. class:: TicketTypes
           

Ticket states
=============

You can see the table of ticket states in your web interface using the
following menu command:

>>> show_menu_path(tickets.TicketStates)
Explorer --> Tickets --> Ticket states


.. class:: TicketStates

    The choicelist of possible values for the :attr:`state
    <Ticket.state>` of a ticket.

    Default choices are:

    .. attribute:: new

        Somebody reported this ticket, but there was no response so
        far.
        The ticket needs to be triaged.

    .. attribute:: talk

        Some worker needs discussion with the author.  We don't yet
        know exactly what to do with it.

    .. attribute:: todo

        The ticket is confirmed and we are working on it.
        It appears in the todo list of somebody (either the assigned
        worker, or our general todo list)

    .. attribute:: testing

        The ticket is theoretically done, but we want to confirm this
        somehow, and it is not clear who should do the next step. If
        it is clear that the author should do the testing, then you
        should rather set the ticket to :attr:`talk`. If it is clear
        that you (the assignee) must test it, then leave the ticket at
        :attr:`todo`.

    .. attribute:: sleeping

        Waiting for some external event. We didn't decide what to do
        with it.

    .. attribute:: ready

        The ticket is basically :attr:`done`, but some detail still
        needs to be done by the :attr:`user` (e.g. testing,
        confirmation, documentation,..)

    .. attribute:: done

        The ticket has been done.

    .. attribute:: cancelled

        It has been decided that we won't fix this ticket.

In a default configuration it defines the following choices:

>>> rt.show(tickets.TicketStates)
======= =========== ========== ============= ========
 value   name        text       Button text   Active
------- ----------- ---------- ------------- --------
 10      new         New        ⛶             Yes
 15      talk        Talk       ☎             Yes
 20      opened      Open       ☉             Yes
 22      started     Started    ⚒             Yes
 30      sleeping    Sleeping   ☾             No
 40      ready       Ready      ☐             Yes
 50      closed      Closed     ☑             No
 60      cancelled   Refused    ☒             No
======= =========== ========== ============= ========
<BLANKLINE>

There is also a "modern" series of symbols, which can be enabled
site-wide in :attr:`lino.core.site.Site.use_new_unicode_symbols`.
   
If :attr:`use_new_unicode_symbols
<lino.core.site.Site.use_new_unicode_symbols>` is True, ticket states
are represented using symbols from the `Miscellaneous Symbols and
Pictographs
<https://en.wikipedia.org/wiki/Miscellaneous_Symbols_and_Pictographs>`__
block, otherwise we use the more widely supported symbols from
`Miscellaneous Symbols
<https://en.wikipedia.org/wiki/Miscellaneous_Symbols>`
`fileformat.info
<http://www.fileformat.info/info/unicode/block/miscellaneous_symbols/list.htm>`__.

            


- :attr:`standby <lino_xl.lib.tickets.models.Ticket.standby>`




Sites
=====


>>> rt.login("jean").show(tickets.MySites)
===================== ============= =============
 Site                  Description   Workflow
--------------------- ------------- -------------
 `welsch <Detail>`__                 **⛶ Draft**
===================== ============= =============
<BLANKLINE>



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
 20    Why is foo so bar                              Normal     **⚒ Started**
===== ============================================== ========== =============== ======
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
 Normal     `#92 (⚒ Why is foo so bar) <Detail>`__                               Mathieu                                               [▶] **⚒ Started** → [☾] [☎] [☐] [☑] [☒]
 Normal     `#78 (☐ Default account in invoices per partner) <Detail>`__         Jean                                                  [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal     `#57 (⛶ Irritating message when bar) <Detail>`__                                                                           [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 Normal     `#50 (☎ Misc optimizations in Baz) <Detail>`__                       Jean                                                  [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal     `#43 (☉ 'NoneType' object has no attribute 'isocode') <Detail>`__    Luc                                                   [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal     `#36 (⚒ No more foo when bar is gone) <Detail>`__                    Mathieu                                               [▶] **⚒ Started** → [☾] [☎] [☐] [☑] [☒]
 Normal     `#22 (☐ How can I see where bar?) <Detail>`__                        Jean                                                  [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal     `#1 (⛶ Föö fails to bar when baz) <Detail>`__                                                                              [✋] [■] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
========== ==================================================================== ============= ============== ========= ======= ====== =============================================
<BLANKLINE>



The backlog
===========

The :class:`TicketsBySite` panel shows all the tickets for a given site.

>>> welket = tickets.Site.objects.get(name="welket")
>>> rt.show(tickets.TicketsBySite, welket)
... #doctest: +REPORT_UDIFF -SKIP +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ========================================================= ============== =========== ======= ====== ===============
 Priority              Ticket                                                    Planned time   Regular     Extra   Free   Workflow
--------------------- --------------------------------------------------------- -------------- ----------- ------- ------ ---------------
 Normal                *#116 (⚒ Foo never bars)*                                                                           **⚒ Started**
 Normal                *#115 (☉ 'NoneType' object has no attribute 'isocode')*                                             **☉ Open**
 Normal                *#114 (☎ Default account in invoices per partner)*                                                  **☎ Talk**
 Normal                *#108 (⚒ No more foo when bar is gone)*                                                             **⚒ Started**
 Normal                *#106 (☎ 'NoneType' object has no attribute 'isocode')*                                             **☎ Talk**
 Normal                *#102 (☐ Irritating message when bar)*                                                              **☐ Ready**
 Normal                *#98 (☎ Foo never bars)*                                                                            **☎ Talk**
 ...
 Normal                *#12 (⚒ Foo cannot bar)*                                                                            **⚒ Started**
 Normal                *#10 (☎ Where can I find a Foo when bazing Bazes?)*                                                 **☎ Talk**
 Normal                *#6 (☐ Sell bar in baz)*                                                                            **☐ Ready**
 Normal                *#4 (⚒ Foo and bar don't baz)*                                           1:24                       **⚒ Started**
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
 Normal                `#116 (⚒ Foo never bars) <Detail>`__                                                                           [▶] **⚒ Started** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#115 (☉ 'NoneType' object has no attribute 'isocode') <Detail>`__                                             [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal                `#114 (☎ Default account in invoices per partner) <Detail>`__                                                  [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#108 (⚒ No more foo when bar is gone) <Detail>`__                                                             [▶] **⚒ Started** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#106 (☎ 'NoneType' object has no attribute 'isocode') <Detail>`__                                             [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#102 (☐ Irritating message when bar) <Detail>`__                                                              [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal                `#98 (☎ Foo never bars) <Detail>`__                                                                            [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 ...
 Normal                `#6 (☐ Sell bar in baz) <Detail>`__                                                                            [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal                `#4 (⚒ Foo and bar don't baz) <Detail>`__                                           1:24                       [▶] **⚒ Started** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#2 (☎ Bar is not always baz) <Detail>`__                                           9:40                       [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#1 (⛶ Föö fails to bar when baz) <Detail>`__                                                                  [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 **Total (46 rows)**                                                                                       **11:04**
===================== ==================================================================== ============== =========== ======= ====== =============================================
<BLANKLINE>



Links between tickets
=====================


.. class:: Link
.. class:: Links
.. class:: LinksByTicket
.. class:: LinkType
.. class:: LinkTypes

    The possible values of a :class:`Link`.

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

Comments are shown even to anonymous users:

>>> rt.show(comments.Comments, column_names="id user owner")
==== ================= ================================================================
 ID   Author            Controlled by
---- ----------------- ----------------------------------------------------------------
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
==== ================= ================================================================
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
| user               | Author             | The author. The user who reported this ticket to the database         |
|                    |                    | and is responsible for managing it.                                   |
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

    
.. class:: Plugin
           
    See also :class:`lino.core.plugin.Plugin`

    .. attribute:: end_user_model
    .. attribute:: site_model
                   
    .. attribute:: milestone_model

        The model to be used for representing "milestones". Until
        20170331 this was hard-coded to `deploy.Milestone`. Now Lino
        Noi uses `courses.Course`.




Other languages
===============

The ticket states in German:

>>> rt.show(tickets.TicketStates, language="de")
====== =========== =============== ============= =======
 Wert   name        Text            Button text   Aktiv
------ ----------- --------------- ------------- -------
 10     new         Neu             ⛶             Ja
 15     talk        Besprechen      ☎             Ja
 20     opened      Offen           ☉             Ja
 22     started     Gestartet       ⚒             Ja
 30     sleeping    Schläft         ☾             Nein
 40     ready       Bereit          ☐             Ja
 50     closed      Abgeschlossen   ☑             Nein
 60     cancelled   Abgelehnt       ☒             Nein
====== =========== =============== ============= =======
<BLANKLINE>

