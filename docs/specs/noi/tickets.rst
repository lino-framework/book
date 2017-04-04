.. _noi.specs.tickets:

=============================
Ticket management in Lino Noi
=============================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_tickets
    Or:
    $ python -m atelier.doctest_utf8 docs/specs/tickets.rst
    
    doctest init:
    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.demo')
    >>> from lino.api.doctest import *


This document specifies the ticket management functions implemented in
:mod:`lino_xl.lib.tickets` (as used by Lino Noi).

.. contents::
  :local:


What is a ticket?
=================


.. currentmodule:: lino_xl.lib.tickets

.. class:: Ticket

    A **Ticket** is the smallest unit of work. It is a concrete
    question or problem handled formulated by a user.


    The user may be a system user or an end user represented by a
    system user.

    A Ticket is always related to one and only one Project.  It may be
    related to other tickets which may belong to other projects.


    .. attribute:: user

        The user who entered this ticket and is responsible for
        managing it.

    .. attribute:: end_user

        The end user who is asking for help.

    .. attribute:: assigned_to

        No longer used. The user who is working on this ticket.

        If this field is empty and :attr:`project` is not empty, then
        default value is taken from :attr:`Project.assign_to`.

    .. attribute:: state

        The state of this ticket. See :class:`TicketStates
        <lino_xl.lib.tickets.choicelists.TicketStates>`

    .. attribute:: waiting_for

        What to do next. An unformatted one-line text which describes
        what this ticket is waiting for.

    .. attribute:: upgrade_notes

        A formatted text field meant for writing instructions for the
        hoster's site administrator when doing an upgrade where this
        ticket is being deployed.

    .. attribute:: description

        A complete and concise description of the ticket. This should
        describe in more detail what this ticket is about. If the
        ticket has evolved during time, it should reflect the latest
        version.

        The description can contain *memo commands* defined by the
        application.

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

        How urgent this ticket is. This should be a value between 0
        and 100.

    .. attribute:: rating

        How the author rates this ticket.

    .. attribute:: reporting_type

        An indication about who is going to pay for work on this
        project.  See :class:`ReportingTypes`.



Lifecycle of a ticket
=====================

The :attr:`state <lino_xl.lib.tickets.models.Ticket.state>` of a
ticket has one of the following values:

>>> rt.show(tickets.TicketStates)
======= =========== ========== ======== ========
 value   name        text       Symbol   Active
------- ----------- ---------- -------- --------
 10      new         New        ⛶        Yes
 15      talk        Talk       ☎        Yes
 20      opened      Open       ☉        Yes
 22      started     Started    ⚒        Yes
 30      sleeping    Sleeping   ☾        No
 40      ready       Ready      ☐        Yes
 50      closed      Closed     ☑        No
 60      cancelled   Refused    ☒        No
======= =========== ========== ======== ========
<BLANKLINE>

There is also a "modern" series of symbols, which can be enabled
site-wide in :attr:`lino.core.site.Site.use_new_unicode_symbols`.

You can see this table in your web interface using
:menuselection:`Explorer --> Tickets --> States`.

.. >>> show_menu_path(tickets.TicketStates)
   Explorer --> Tickets --> States

See :class:`lino_xl.lib.tickets.choicelists.TicketStates` for more
information about every state.

Above table in German:

>>> rt.show(tickets.TicketStates, language="de")
====== =========== =============== ======== =======
 Wert   name        Text            Symbol   Aktiv
------ ----------- --------------- -------- -------
 10     new         Neu             ⛶        Ja
 15     talk        Besprechen      ☎        Ja
 20     opened      Offen           ☉        Ja
 22     started     Gestartet       ⚒        Ja
 30     sleeping    Schläft         ☾        Nein
 40     ready       Bereit          ☐        Ja
 50     closed      Abgeschlossen   ☑        Nein
 60     cancelled   Abgelehnt       ☒        Nein
====== =========== =============== ======== =======
<BLANKLINE>

And in French (not yet fully translated):

>>> rt.show(tickets.TicketStates, language="fr")
======= =========== ========== ======== ========
 value   name        text       Symbol   Active
------- ----------- ---------- -------- --------
 10      new         Nouveau    ⛶        Oui
 15      talk        Talk       ☎        Oui
 20      opened      Open       ☉        Oui
 22      started     Started    ⚒        Oui
 30      sleeping    Sleeping   ☾        Non
 40      ready       Ready      ☐        Oui
 50      closed      Closed     ☑        Non
 60      cancelled   Refusé     ☒        Non
======= =========== ========== ======== ========
<BLANKLINE>


Note that a ticket also has a checkbox for marking it as :attr:`closed
<lino_xl.lib.tickets.models.Ticket.closed>`.  This means that a ticket
can be marked as "closed" in any of above states.  We don't use this for the moment and are not sure
whether this is a cool feature (:ticket:`372`).

- :attr:`standby <lino_xl.lib.tickets.models.Ticket.standby>`



Projects
========

The :attr:`project <lino_xl.lib.tickets.models.Ticket.project>` of a
ticket is used to specify "who is going to pay" for it. Lino Noi does
not issue invoices, so it uses this information only for reporting
about it and helping with the decision about whether and how worktime
is being invoiced to the customer.  But the invoicing itself is not
currently a goal of Lino Noi.

So a **project** is something for which somebody is possibly willing
to pay money.

>>> rt.show(tickets.Projects)
=========== =============== ======== ========= =========
 Reference   Name            Parent   Company   Private
----------- --------------- -------- --------- ---------
 docs        Documentatión   linö     pypi      No
 linö        Framewörk                welket    No
 research    Research        docs     welket    No
 shop        Shop                     welsch    No
 téam        Téam            linö     welsch    Yes
=========== =============== ======== ========= =========
<BLANKLINE>


>>> rt.show(tickets.TopLevelProjects)
=========== =========== ======== ================
 Reference   Name        Parent   Children
----------- ----------- -------- ----------------
 linö        Framewörk            *téam*, *docs*
 shop        Shop
=========== =========== ======== ================
<BLANKLINE>


Developers can start working on tickets without specifying a project
(i.e. without knowing who is going to pay for their work).  

But after some time every ticket should get assigned to some
project. You can see a list of tickets which have not yet been
assigned to a project:

>>> pv = dict(has_project=dd.YesNo.no)
>>> rt.show(tickets.Tickets, param_values=pv)
... #doctest: +REPORT_UDIFF
==== =================== ========= ============== ============== =========
 ID   Summary             Author    Topic          Actions        Mission
---- ------------------- --------- -------------- -------------- ---------
 5    Cannot create Foo   Jean      Lino Welfare   **Sleeping**
 3    Baz sucks           Mathieu   Lino Voga      **Open**
==== =================== ========= ============== ============== =========
<BLANKLINE>


Distribution of tickets per project
===================================

In our demo database, tickets are distributed over the different
projects as follows (not a realistic distribution):

>>> for p in tickets.Project.objects.all():
...         print p.ref, p.tickets_by_project.count()
linö 23
téam 23
docs 23
research 23
shop 22



Private tickets
===============

Tickets are private by default. But when they are assigned to a public
project, then their privacy is removed.

So the private tickets are (1) those in project "téam" and (2) those
without project:

>>> pv = dict(show_private=dd.YesNo.yes)
>>> rt.show(tickets.Tickets, param_values=pv,
...     column_names="id summary project")
... #doctest: -REPORT_UDIFF
===== ======================= =========
 ID    Summary                 Mission
----- ----------------------- ---------
 114   Ticket 114              téam
 109   Ticket 109              téam
 104   Ticket 104              téam
 99    Ticket 99               téam
 94    Ticket 94               téam
 89    Ticket 89               téam
 84    Ticket 84               téam
 79    Ticket 79               téam
 74    Ticket 74               téam
 69    Ticket 69               téam
 64    Ticket 64               téam
 59    Ticket 59               téam
 54    Ticket 54               téam
 49    Ticket 49               téam
 44    Ticket 44               téam
 39    Ticket 39               téam
 34    Ticket 34               téam
 29    Ticket 29               téam
 24    Ticket 24               téam
 19    Ticket 19               téam
 14    Bar cannot baz          téam
 9     Foo never matches Bar   téam
 5     Cannot create Foo
 3     Baz sucks
 2     Bar is not always baz   téam
===== ======================= =========
<BLANKLINE>



And these are the public tickets:

>>> pv = dict(show_private=dd.YesNo.no)
>>> rt.show(tickets.Tickets, param_values=pv,
...     column_names="id summary project")
... #doctest: -REPORT_UDIFF +ELLIPSIS
===== =========================================== ==========
 ID    Summary                                     Mission
----- ------------------------------------------- ----------
 116   Ticket 116                                  research
 115   Ticket 115                                  docs
 113   Ticket 113                                  linö
 112   Ticket 112                                  shop
 111   Ticket 111                                  research
 110   Ticket 110                                  docs
 108   Ticket 108                                  linö
 107   Ticket 107                                  shop
 ...
 21    Ticket 21                                   research
 20    Ticket 20                                   docs
 18    Ticket 18                                   linö
 17    Ticket 17                                   shop
 16    How to get bar from foo                     research
 15    Bars have no foo                            docs
 13    Bar cannot foo                              linö
 12    Foo cannot bar                              shop
 11    Class-based Foos and Bars?                  research
 10    Where can I find a Foo when bazing Bazes?   docs
 8     Is there any Bar in Foo?                    linö
 7     No Foo after deleting Bar                   shop
 6     Sell bar in baz                             research
 4     Foo and bar don't baz                       docs
 1     Föö fails to bar when baz                   linö
===== =========================================== ==========
<BLANKLINE>


There are 20 private and 96 public tickets in the demo database.

>>> tickets.Ticket.objects.filter(private=True).count()
20
>>> tickets.Ticket.objects.filter(private=False).count()
96

My tickets
==========

>>> rt.login('jean').show(tickets.MyTickets)
... #doctest: +REPORT_UDIFF
================================================= ============================================
 Description                                       Actions
------------------------------------------------- --------------------------------------------
 `#116 (⚒ Ticket 116) <Detail>`__                  [▶] [★] **Started** → [☾] [☎] [☐] [☑] [☒]
 `#113 (⛶ Ticket 113) <Detail>`__                  [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#107 (☉ Ticket 107) <Detail>`__                  [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 `#98 (☎ Ticket 98) <Detail>`__                    [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 `#94 (☐ Ticket 94) <Detail>`__                    [▶] [★] **Ready** → [☎] [☑] [☒]
 `#92 (⚒ Ticket 92) <Detail>`__                    [▶] [★] **Started** → [☾] [☎] [☐] [☑] [☒]
 `#89 (⛶ Ticket 89) <Detail>`__                    [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#83 (☉ Ticket 83) <Detail>`__                    [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 `#74 (☎ Ticket 74) <Detail>`__                    [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 `#70 (☐ Ticket 70) <Detail>`__                    [▶] [★] **Ready** → [☎] [☑] [☒]
 `#68 (⚒ Ticket 68) <Detail>`__                    [▶] [★] **Started** → [☾] [☎] [☐] [☑] [☒]
 `#65 (⛶ Ticket 65) <Detail>`__                    [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#59 (☉ Ticket 59) <Detail>`__                    [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 `#50 (☎ Ticket 50) <Detail>`__                    [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 `#46 (☐ Ticket 46) <Detail>`__                    [▶] [★] **Ready** → [☎] [☑] [☒]
 `#44 (⚒ Ticket 44) <Detail>`__                    [▶] [★] **Started** → [☾] [☎] [☐] [☑] [☒]
 `#41 (⛶ Ticket 41) <Detail>`__                    [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#35 (☉ Ticket 35) <Detail>`__                    [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 `#26 (☎ Ticket 26) <Detail>`__                    [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 `#22 (☐ Ticket 22) <Detail>`__                    [▶] [★] **Ready** → [☎] [☑] [☒]
 `#20 (⚒ Ticket 20) <Detail>`__                    [▶] [★] **Started** → [☾] [☎] [☐] [☑] [☒]
 `#17 (⛶ Ticket 17) <Detail>`__                    [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#11 (☉ Class-based Foos and Bars?) <Detail>`__   [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 `#2 (☎ Bar is not always baz) <Detail>`__         [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
================================================= ============================================
<BLANKLINE>


Sites
=====

Lino Noi has a list of all sites for which we do support:

>>> rt.show(cal.Rooms)
==== ============= ================== ================== ============= ================ ================ =============
 ID   Designation   Designation (de)   Designation (fr)   Responsible   Contact person   represented as   Description
---- ------------- ------------------ ------------------ ------------- ---------------- ---------------- -------------
 1    welket
 2    welsch
 3    pypi
==== ============= ================== ================== ============= ================ ================ =============
<BLANKLINE>

A ticket may or may not be "local", i.e. specific to a given site.
When a ticket is site-specific, we simply assign the `site` field.  We
can see all local tickets for a given site object:

>>> welket = cal.Room.objects.get(name="welket")
>>> rt.show(tickets.TicketsBySite, welket)
... #doctest: -REPORT_UDIFF -SKIP
===== =========================== ======== ============== ========== ==========
 ID    Summary                     Author   Topic          Actions    Mission
----- --------------------------- -------- -------------- ---------- ----------
 115   Ticket 115                  Luc      Lino Voga      **Open**   docs
 97    Ticket 97                   Luc      Lino Welfare   **New**    shop
 91    Ticket 91                   Luc      Lino Voga      **Open**   research
 73    Ticket 73                   Luc      Lino Welfare   **New**    linö
 67    Ticket 67                   Luc      Lino Voga      **Open**   shop
 49    Ticket 49                   Luc      Lino Welfare   **New**    téam
 43    Ticket 43                   Luc      Lino Voga      **Open**   linö
 25    Ticket 25                   Luc      Lino Welfare   **New**    docs
 19    Ticket 19                   Luc      Lino Voga      **Open**   téam
 1     Föö fails to bar when baz   Luc      Lino Welfare   **New**    linö
===== =========================== ======== ============== ========== ==========
<BLANKLINE>


Note that the above table shows no state change actions in the
Actions column because it is being requested by anonymous. For an
authenticated developer it looks like this:

>>> rt.login('luc').show(tickets.TicketsBySite, welket)
... #doctest: -REPORT_UDIFF -SKIP
===== =========================== ======== ============== ============================================ ==========
 ID    Summary                     Author   Topic          Actions                                      Mission
----- --------------------------- -------- -------------- -------------------------------------------- ----------
 115   Ticket 115                  Luc      Lino Voga      [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]   docs
 97    Ticket 97                   Luc      Lino Welfare   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]        shop
 91    Ticket 91                   Luc      Lino Voga      [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]   research
 73    Ticket 73                   Luc      Lino Welfare   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]        linö
 67    Ticket 67                   Luc      Lino Voga      [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]   shop
 49    Ticket 49                   Luc      Lino Welfare   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]        téam
 43    Ticket 43                   Luc      Lino Voga      [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]   linö
 25    Ticket 25                   Luc      Lino Welfare   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]        docs
 19    Ticket 19                   Luc      Lino Voga      [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑] [☒]   téam
 1     Föö fails to bar when baz   Luc      Lino Welfare   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]        linö
===== =========================== ======== ============== ============================================ ==========
<BLANKLINE>



Milestones
==========

Every site can have its list of "milestones". A milestone is when
something happens on a given site at a given time, and when a given
group of people are working for preparing this.  In Scrum this is
called a sprint.

A typical case of a milestone is an upgrade of the software that is
running on a given site.  A milestone is not necessary an *official*
release of a new version.

>>> rt.show('courses.Courses')
... #doctest: -REPORT_UDIFF +ELLIPSIS +NORMALIZE_WHITESPACE -SKIP
============ ================== =============== ============ ======== ===========
 Start date   Enrolments until   Activity line   Instructor   Room     Actions
------------ ------------------ --------------- ------------ -------- -----------
 15/05/2015                      Sprint                       welket   **Draft**
 13/05/2015                      Sprint                       welsch   **Draft**
 11/05/2015                      Sprint                       welket   **Draft**
 09/05/2015                      Sprint                       welsch   **Draft**
 07/05/2015                      Sprint                       welket   **Draft**
 05/05/2015                      Sprint                       welsch   **Draft**
 03/05/2015                      Sprint                       welket   **Draft**
============ ================== =============== ============ ======== ===========
<BLANKLINE>



Wishes
======

Every milestone has its list of wishes ("deployments"), i.e. the
tickets that are being fixed when this milestone is reached.

The demo database has the following wishes:

>>> rt.show(rt.actors.deploy.Deployments)
... #doctest: -REPORT_UDIFF +ELLIPSIS +NORMALIZE_WHITESPACE
==== ========= =================================================== ========== ======== ===========
 ID   No.       Ticket                                              Event      Remark   Wish type
---- --------- --------------------------------------------------- ---------- -------- -----------
 1    1         #1 (⛶ Föö fails to bar when baz)                    20150503
 2    1         #2 (☎ Bar is not always baz)                        20150505
 3    1         #3 (☉ Baz sucks)                                    20150507
 4    1         #5 (☾ Cannot create Foo)                            20150509
 5    1         #6 (☐ Sell bar in baz)                              20150511
 6    1         #7 (☑ No Foo after deleting Bar)                    20150513
 7    1         #9 (⛶ Foo never matches Bar)                        20150515
 8    2         #10 (☎ Where can I find a Foo when bazing Bazes?)   20150503
 9    2         #11 (☉ Class-based Foos and Bars?)                  20150505
 10   2         #13 (☾ Bar cannot foo)                              20150507
 11   2         #14 (☐ Bar cannot baz)                              20150509
 12   2         #15 (☑ Bars have no foo)                            20150511
 ...
 77   11        #102 (☐ Ticket 102)                                 20150515
 78   12        #103 (☑ Ticket 103)                                 20150503
 79   12        #105 (⛶ Ticket 105)                                 20150505
 80   12        #106 (☎ Ticket 106)                                 20150507
 81   12        #107 (☉ Ticket 107)                                 20150509
 82   12        #109 (☾ Ticket 109)                                 20150511
 83   12        #110 (☐ Ticket 110)                                 20150513
 84   12        #111 (☑ Ticket 111)                                 20150515
 85   13        #113 (⛶ Ticket 113)                                 20150503
 86   13        #114 (☎ Ticket 114)                                 20150505
 87   13        #115 (☉ Ticket 115)                                 20150507
      **585**
==== ========= =================================================== ========== ======== ===========
<BLANKLINE>




Release notes
=============

>>> url = '/choices/deploy/DeploymentsByTicket/milestone'
>>> show_choices('robin', url)
20150515
20150513
20150511
20150509
20150507
20150505
20150503


>>> show_choices('robin', url+"?query=0507")
20150507

>>> show_choices('robin', url+"?query=2015050")
... #doctest: +SKIP
20150503
20150505
20150507
20150509



Dependencies between tickets
============================


.. class:: LinkTypes

    The possible values of a :class:`lino_xl.lib.tickets.Link`.

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

Comments are not shown to anonymous users:

>>> rt.show(comments.Comments, column_names="id user owner")
==== ================= ===================================================
 ID   Author            Ticket
---- ----------------- ---------------------------------------------------
 1    Jean              #1 (⛶ Föö fails to bar when baz)
 4    Romain Raffault   #4 (⚒ Foo and bar don't baz)
 6    Robin Rood        #6 (☐ Sell bar in baz)
 7    Jean              #7 (☑ No Foo after deleting Bar)
 8    Luc               #8 (☒ Is there any Bar in Foo?)
 10   Romain Raffault   #10 (☎ Where can I find a Foo when bazing Bazes?)
 11   Rolf Rompen       #11 (☉ Class-based Foos and Bars?)
 12   Robin Rood        #12 (⚒ Foo cannot bar)
==== ================= ===================================================
<BLANKLINE>

The same list seen by marc

>>> rt.login('luc').show('comments.Comments', column_names="id user owner")
==== ================= ===================================================
 ID   Author            Ticket
---- ----------------- ---------------------------------------------------
 1    Jean              #1 (⛶ Föö fails to bar when baz)
 2    Luc               #2 (☎ Bar is not always baz)
 3    Mathieu           #3 (☉ Baz sucks)
 4    Romain Raffault   #4 (⚒ Foo and bar don't baz)
 5    Rolf Rompen       #5 (☾ Cannot create Foo)
 6    Robin Rood        #6 (☐ Sell bar in baz)
 7    Jean              #7 (☑ No Foo after deleting Bar)
 8    Luc               #8 (☒ Is there any Bar in Foo?)
 9    Mathieu           #9 (⛶ Foo never matches Bar)
 10   Romain Raffault   #10 (☎ Where can I find a Foo when bazing Bazes?)
 11   Rolf Rompen       #11 (☉ Class-based Foos and Bars?)
 12   Robin Rood        #12 (⚒ Foo cannot bar)
==== ================= ===================================================
<BLANKLINE>


>>> obj = tickets.Ticket.objects.get(pk=2)
>>> rt.login('luc').show(comments.CommentsByRFC, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
<p><b>Write comment</b></p><ul><li><a href="Detail" title="Created ...">...</a> by <a href="Detail">Luc</a> [<b> Reply </b>] <a href="#" onclick="toggle_visibility('comment-2');" title="Hide">&#8284;</a><div id=comment-2><p>Very confidential comment</p></div></li></ul>



Filtering tickets
=================


>>> show_fields(tickets.Tickets)
+-----------------+-----------------+---------------------------------------------------------------+
| Internal name   | Verbose name    | Help text                                                     |
+=================+=================+===============================================================+
| user            | Author          |                                                               |
+-----------------+-----------------+---------------------------------------------------------------+
| end_user        | End user        | Only rows concerning this end user.                           |
+-----------------+-----------------+---------------------------------------------------------------+
| assigned_to     | Voted by        | Only tickets having a vote by this user.                      |
+-----------------+-----------------+---------------------------------------------------------------+
| not_assigned_to | Not voted by    | Only tickets having no vote by this user.                     |
+-----------------+-----------------+---------------------------------------------------------------+
| interesting_for | Interesting for | Only tickets interesting for this partner.                    |
+-----------------+-----------------+---------------------------------------------------------------+
| site            | Room            | Select a site if you want to see only tickets for this site.  |
+-----------------+-----------------+---------------------------------------------------------------+
| project         | Mission         |                                                               |
+-----------------+-----------------+---------------------------------------------------------------+
| state           | State           | Only rows having this state.                                  |
+-----------------+-----------------+---------------------------------------------------------------+
| deployed_to     | Event           |                                                               |
+-----------------+-----------------+---------------------------------------------------------------+
| has_project     | Has project     | Show only (or hide) tickets which have a project assigned.    |
+-----------------+-----------------+---------------------------------------------------------------+
| show_assigned   | Assigned        | Whether to show assigned tickets                              |
+-----------------+-----------------+---------------------------------------------------------------+
| show_active     | Active          | Whether to show active tickets                                |
+-----------------+-----------------+---------------------------------------------------------------+
| show_deployed   | Deployed        | Whether to show tickets with at least one deployment          |
+-----------------+-----------------+---------------------------------------------------------------+
| show_todo       | To do           | Show only (or hide) tickets which are todo (i.e. state is New |
|                 |                 | or ToDo).                                                     |
+-----------------+-----------------+---------------------------------------------------------------+
| show_private    | Private         | Show only (or hide) tickets that are marked private.          |
+-----------------+-----------------+---------------------------------------------------------------+
| start_date      | Period from     | Start date of observed period                                 |
+-----------------+-----------------+---------------------------------------------------------------+
| end_date        | until           | End date of observed period                                   |
+-----------------+-----------------+---------------------------------------------------------------+
| observed_event  | Observed event  |                                                               |
+-----------------+-----------------+---------------------------------------------------------------+
| topic           | Topic           |                                                               |
+-----------------+-----------------+---------------------------------------------------------------+
| feasable_by     | Feasable by     | Show only tickets for which the given supplier is competent.  |
+-----------------+-----------------+---------------------------------------------------------------+



The detail layout of a ticket
=============================

Here is a textual description of the fields and their layout used in
the detail window of a ticket.

>>> from lino.utils.diag import py2rst
>>> print(py2rst(tickets.Tickets.detail_layout, True))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
(main) [visible for all]:
- **General** (general_1):
  - (general1):
    - (general1_1): **Summary** (summary), **ID** (id)
    - (general1_2): **Author** (user), **End user** (end_user), **Deadline** (deadline)
    - (general1_3): **Room** (site), **Topic** (topic), **Mission** (project)
    - (general1_4): **Actions** (workflow_buttons), **Private** (private)
    - (bottom_box) [visible for user consultant hoster developer senior admin]:
      - (bottom_box_1): **Wanted skills** (DemandsByDemander), **Votes** (VotesByVotable)
      - (bottom_box_2): **Wishes** (DeploymentsByTicket), **Sessions** (SessionsByTicket) [visible for consultant hoster developer senior admin]
  - **Comments** (CommentsByRFC) [visible for user consultant hoster developer senior admin]
- **More** (more):
  - (more_1):
    - (more1):
      - (more1_1): **Created** (created), **Modified** (modified), **Reported for** (reported_for), **Ticket type** (ticket_type)
      - (more1_2): **State** (state), **Duplicate of** (duplicate_of), **Planned time** (planned_time), **Priority** (priority)
    - **Duplicates** (DuplicatesByTicket)
  - (more_2): **Description** (description), **Resolution** (upgrade_notes), **Dependencies** (LinksByTicket) [visible for senior admin]
- **History** (changes.ChangesByMaster) [visible for senior admin]
- **Uploads** (UploadsByController) [visible for user consultant hoster developer senior admin]
<BLANKLINE>



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


