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

>>> from lino import startup
>>> startup('lino_book.projects.max.settings.demo')
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

    .. attribute:: ticket_type

        The type of this ticket. The site administrator can configure the list
        of available ticket types.

    .. attribute:: upgrade_notes

        A formatted text field meant for writing instructions for the
        hoster's site administrator when doing an upgrade where this
        ticket is being deployed.


    .. attribute:: waiting_for

        What to do next. An unformatted one-line text which describes
        what this ticket is waiting for.

    .. attribute:: state

        The workflow state of this ticket.

        The list of available states (:class:`TicketStates`) is defined by the
        :term:`application developer` but may have :doc:`local modifications
        </admin/choicelists>`.

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

>>> rt.show(tickets.TicketStates)
======= =========== ========== ============= ========
 value   name        text       Button text   Active
------- ----------- ---------- ------------- --------
 10      new         New        ⚹             Yes
 15      talk        Talk       ☎             Yes
 20      opened      Open       ☉             Yes
 22      working     Working    ⚒             Yes
 30      sleeping    Sleeping   ☾             No
 40      ready       Ready      ☐             Yes
 50      closed      Closed     ☑             No
 60      cancelled   Refused    ☒             No
======= =========== ========== ============= ========
<BLANKLINE>


.. class:: TicketStates

    The choicelist for the :attr:`state <Ticket.state>` of a ticket.

    .. attribute:: new

        Somebody reported this ticket, but there was no response yet. The
        ticket needs to be triaged.

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

  Base class for all Sites tables.

    .. attribute:: watcher
    .. attribute:: show_exposed
    .. attribute:: state

.. class:: MySites

    Shows the sites for which I have a subscription.

    Sleeping and closed sites are not shown by default.

.. class:: AllSites

    Shows all sites in explorer menu.


Ticket types
============

A **ticket type**, or the type of a *ticket*, is a way to classify that ticket.
This information may be used in service reports or statistics defined by the
application.

You can configure the list of ticket types via :menuselection:`Configure -->
Tickets --> Ticket types`.

..  >>> show_menu_path(tickets.TicketTypes)
    Configure --> Tickets --> Ticket types


.. class:: TicketType

    The Django model used to represent a *ticket type*.

    .. attribute:: name

    .. attribute:: reporting_type

        Which *reporting type* to use in a service report.
        See :class:ReportingTypes`.

.. class:: TicketTypes

    The list of all ticket types.





The state of a site
===================

>>> rt.show(tickets.SiteStates)
... #doctest: +REPORT_UDIFF +ELLIPSIS
======= ========== ========== ============= =========
 value   name       text       Button text   Exposed
------- ---------- ---------- ------------- ---------
 10      draft      Draft      ⚹             Yes
 20      active     Active     ⚒             Yes
 30      stable     Stable     ☉             Yes
 40      sleeping   Sleeping   ☾             No
 50      closed     Closed     ☑             No
======= ========== ========== ============= =========
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
======= ============ ============
 value   name         text
------- ------------ ------------
 10      requires     Requires
 20      triggers     Triggers
 30      suggests     Suggests
 40      obsoletes    Obsoletes
 50      duplicates   Duplicates
======= ============ ============
<BLANKLINE>




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
 10     new         Neu              ⚹             Ja
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
