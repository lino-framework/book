.. _noi.specs.tickets:

=============================
Ticket management in Lino Noi
=============================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_tickets
    
    doctest init:
    >>> import lino
    >>> lino.startup('lino_noi.projects.team.settings.demo')
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
======= =========== =========== ======== ========
 value   name        text        Symbol   Active
------- ----------- ----------- -------- --------
 10      new         New         ⛶        Yes
 15      talk        Talk        ☎        Yes
 20      opened      Open        ☉        Yes
 22      started     Started     ⚒        Yes
 30      sleeping    Sleeping    ☾        No
 40      ready       Ready       ☐        Yes
 50      closed      Closed      ☑        No
 60      cancelled   Cancelled   ☒        No
======= =========== =========== ======== ========
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
 60     cancelled   Storniert       ☒        Nein
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
 60      cancelled   Annulé     ☒        Non
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
 ID   Summary             Author    Topic          Actions        Project
---- ------------------- --------- -------------- -------------- ---------
 5    Cannot create Foo   Mathieu   Lino Welfare   **Sleeping**
 3    Baz sucks           Luc       Lino Voga      **Open**
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
 ID    Summary                 Project
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
... #doctest: -REPORT_UDIFF
===== =========================================== ==========
 ID    Summary                                     Project
----- ------------------------------------------- ----------
 116   Ticket 116                                  research
 115   Ticket 115                                  docs
 113   Ticket 113                                  linö
 112   Ticket 112                                  shop
 111   Ticket 111                                  research
 110   Ticket 110                                  docs
 108   Ticket 108                                  linö
 107   Ticket 107                                  shop
 106   Ticket 106                                  research
 105   Ticket 105                                  docs
 103   Ticket 103                                  linö
 102   Ticket 102                                  shop
 101   Ticket 101                                  research
 100   Ticket 100                                  docs
 98    Ticket 98                                   linö
 97    Ticket 97                                   shop
 96    Ticket 96                                   research
 95    Ticket 95                                   docs
 93    Ticket 93                                   linö
 92    Ticket 92                                   shop
 91    Ticket 91                                   research
 90    Ticket 90                                   docs
 88    Ticket 88                                   linö
 87    Ticket 87                                   shop
 86    Ticket 86                                   research
 85    Ticket 85                                   docs
 83    Ticket 83                                   linö
 82    Ticket 82                                   shop
 81    Ticket 81                                   research
 80    Ticket 80                                   docs
 78    Ticket 78                                   linö
 77    Ticket 77                                   shop
 76    Ticket 76                                   research
 75    Ticket 75                                   docs
 73    Ticket 73                                   linö
 72    Ticket 72                                   shop
 71    Ticket 71                                   research
 70    Ticket 70                                   docs
 68    Ticket 68                                   linö
 67    Ticket 67                                   shop
 66    Ticket 66                                   research
 65    Ticket 65                                   docs
 63    Ticket 63                                   linö
 62    Ticket 62                                   shop
 61    Ticket 61                                   research
 60    Ticket 60                                   docs
 58    Ticket 58                                   linö
 57    Ticket 57                                   shop
 56    Ticket 56                                   research
 55    Ticket 55                                   docs
 53    Ticket 53                                   linö
 52    Ticket 52                                   shop
 51    Ticket 51                                   research
 50    Ticket 50                                   docs
 48    Ticket 48                                   linö
 47    Ticket 47                                   shop
 46    Ticket 46                                   research
 45    Ticket 45                                   docs
 43    Ticket 43                                   linö
 42    Ticket 42                                   shop
 41    Ticket 41                                   research
 40    Ticket 40                                   docs
 38    Ticket 38                                   linö
 37    Ticket 37                                   shop
 36    Ticket 36                                   research
 35    Ticket 35                                   docs
 33    Ticket 33                                   linö
 32    Ticket 32                                   shop
 31    Ticket 31                                   research
 30    Ticket 30                                   docs
 28    Ticket 28                                   linö
 27    Ticket 27                                   shop
 26    Ticket 26                                   research
 25    Ticket 25                                   docs
 23    Ticket 23                                   linö
 22    Ticket 22                                   shop
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
============================================================== ========================================
 Description                                                    Actions
-------------------------------------------------------------- ----------------------------------------
 `#115 (Ticket 115) <Detail>`__                                 [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑]
 `#106 (Ticket 106) <Detail>`__                                 [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑]
 `#102 (Ticket 102) <Detail>`__                                 [▶] [★] **Ready** → [☎] [☑]
 `#100 (Ticket 100) <Detail>`__                                 [▶] [★] **Started** → [☾] [☎] [☐] [☑]
 `#97 (Ticket 97) <Detail>`__                                   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#91 (Ticket 91) <Detail>`__                                   [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑]
 `#82 (Ticket 82) <Detail>`__                                   [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑]
 `#78 (Ticket 78) <Detail>`__                                   [▶] [★] **Ready** → [☎] [☑]
 `#76 (Ticket 76) <Detail>`__                                   [▶] [★] **Started** → [☾] [☎] [☐] [☑]
 `#73 (Ticket 73) <Detail>`__                                   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#67 (Ticket 67) <Detail>`__                                   [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑]
 `#58 (Ticket 58) <Detail>`__                                   [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑]
 `#54 (Ticket 54) <Detail>`__                                   [▶] [★] **Ready** → [☎] [☑]
 `#52 (Ticket 52) <Detail>`__                                   [▶] [★] **Started** → [☾] [☎] [☐] [☑]
 `#49 (Ticket 49) <Detail>`__                                   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#43 (Ticket 43) <Detail>`__                                   [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑]
 `#34 (Ticket 34) <Detail>`__                                   [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑]
 `#30 (Ticket 30) <Detail>`__                                   [▶] [★] **Ready** → [☎] [☑]
 `#28 (Ticket 28) <Detail>`__                                   [▶] [★] **Started** → [☾] [☎] [☐] [☑]
 `#25 (Ticket 25) <Detail>`__                                   [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
 `#19 (Ticket 19) <Detail>`__                                   [▶] [★] **Open** → [☾] [☎] [⚒] [☐] [☑]
 `#10 (Where can I find a Foo when bazing Bazes?) <Detail>`__   [▶] [★] **Talk** → [☾] [☉] [⚒] [☐] [☑]
 `#6 (Sell bar in baz) <Detail>`__                              [▶] [★] **Ready** → [☎] [☑]
 `#4 (Foo and bar don't baz) <Detail>`__                        [▶] [★] **Started** → [☾] [☎] [☐] [☑]
 `#1 (Föö fails to bar when baz) <Detail>`__                    [▶] [★] **New** → [☾] [☎] [☉] [⚒] [☐]
============================================================== ========================================
<BLANKLINE>


Sites
=====

Lino Noi has a list of all sites for which we do support:

>>> rt.show(tickets.Sites)
============= ========= ======== ====
 Designation   Partner   Remark   ID
------------- --------- -------- ----
 pypi          pypi               3
 welket        welket             1
 welsch        welsch             2
============= ========= ======== ====
<BLANKLINE>

A ticket may or may not be "local", i.e. specific to a given site.
When a ticket is site-specific, we simply assign the `site` field.  We
can see all local tickets for a given site object:

>>> welket = tickets.Site.objects.get(name="welket")
>>> rt.show(tickets.TicketsBySite, welket)
... #doctest: -REPORT_UDIFF -SKIP
===== =========================== ======== ============== ========== ==========
 ID    Summary                     Author   Topic          Actions    Project
----- --------------------------- -------- -------------- ---------- ----------
 115   Ticket 115                  Jean     Lino Voga      **Open**   docs
 97    Ticket 97                   Jean     Lino Welfare   **New**    shop
 91    Ticket 91                   Jean     Lino Voga      **Open**   research
 73    Ticket 73                   Jean     Lino Welfare   **New**    linö
 67    Ticket 67                   Jean     Lino Voga      **Open**   shop
 49    Ticket 49                   Jean     Lino Welfare   **New**    téam
 43    Ticket 43                   Jean     Lino Voga      **Open**   linö
 25    Ticket 25                   Jean     Lino Welfare   **New**    docs
 19    Ticket 19                   Jean     Lino Voga      **Open**   téam
 1     Föö fails to bar when baz   Jean     Lino Welfare   **New**    linö
===== =========================== ======== ============== ========== ==========
<BLANKLINE>


Note that the above table shows no state change actions in the
Actions column because it is being requested by anonymous. For an
authenticated developer it looks like this:

>>> rt.login('luc').show(tickets.TicketsBySite, welket)
... #doctest: -REPORT_UDIFF -SKIP
===== =========================== ======== ============== ================== ==========
 ID    Summary                     Author   Topic          Actions            Project
----- --------------------------- -------- -------------- ------------------ ----------
 115   Ticket 115                  Jean     Lino Voga      [▶] [★] **Open**   docs
 97    Ticket 97                   Jean     Lino Welfare   [▶] [★] **New**    shop
 91    Ticket 91                   Jean     Lino Voga      [▶] [★] **Open**   research
 73    Ticket 73                   Jean     Lino Welfare   [▶] [★] **New**    linö
 67    Ticket 67                   Jean     Lino Voga      [▶] [★] **Open**   shop
 49    Ticket 49                   Jean     Lino Welfare   [▶] [★] **New**    téam
 43    Ticket 43                   Jean     Lino Voga      [▶] [★] **Open**   linö
 25    Ticket 25                   Jean     Lino Welfare   [▶] [★] **New**    docs
 19    Ticket 19                   Jean     Lino Voga      [▶] [★] **Open**   téam
 1     Föö fails to bar when baz   Jean     Lino Welfare   [★] **New**        linö
===== =========================== ======== ============== ================== ==========
<BLANKLINE>



Milestones
==========

Every site can have its list of "milestones" or "releases". A
milestone is when a site gets an upgrade of the software which is
running there. 

A milestone is not necessary an *official* release of a new
version. It just means that you release some changed software to the
users of that site.

.. the following test is skipped because the width of the "Printed"
   column changes

>>> rt.show('deploy.Milestones')
... #doctest: -REPORT_UDIFF +ELLIPSIS +NORMALIZE_WHITESPACE -SKIP
========== ========== ============== ============ ========
 Label      Project    Expected for   Reached      Closed
---------- ---------- -------------- ------------ --------
 20150503   docs       03/05/2015     03/05/2015   No
 20150505   research   05/05/2015     05/05/2015   No
 20150507   shop       07/05/2015     07/05/2015   No
 20150509   linö       09/05/2015     09/05/2015   No
 20150511   téam       11/05/2015     11/05/2015   No
 20150513   docs       13/05/2015     13/05/2015   No
 20150515   research   15/05/2015     15/05/2015   No
            shop       23/05/2015                  No
========== ========== ============== ============ ========
<BLANKLINE>


>>> shop = tickets.Project.objects.get(ref="shop")
>>> rt.show('deploy.MilestonesByProject', shop)
... #doctest: -REPORT_UDIFF
========== ============== ============ ========
 Label      Expected for   Reached      Closed
---------- -------------- ------------ --------
 20150507   07/05/2015     07/05/2015   No
            23/05/2015                  No
========== ============== ============ ========
<BLANKLINE>


Deployments (Wishes)
=====================

Every milestone has its list of "deployments", i.e. the tickets that
are being fixed when this milestone is reached.

The demo database currently does not have any deployments:

>>> rt.show(rt.actors.deploy.Deployments)
... #doctest: -REPORT_UDIFF +ELLIPSIS +NORMALIZE_WHITESPACE
==== ========= ================================================= =================== ========
 ID   No.       Ticket                                            Milestone           Remark
---- --------- ------------------------------------------------- ------------------- --------
 1    1         #1 (Föö fails to bar when baz)                    20150503@docs
 9    2         #11 (Class-based Foos and Bars?)                  20150503@docs
 17   3         #22 (Ticket 22)                                   20150503@docs
 25   4         #33 (Ticket 33)                                   20150503@docs
 33   5         #43 (Ticket 43)                                   20150503@docs
 ...
 24   3         #31 (Ticket 31)                                   #8@shop
 32   4         #42 (Ticket 42)                                   #8@shop
 40   5         #53 (Ticket 53)                                   #8@shop
 48   6         #63 (Ticket 63)                                   #8@shop
 56   7         #74 (Ticket 74)                                   #8@shop
 64   8         #85 (Ticket 85)                                   #8@shop
 72   9         #95 (Ticket 95)                                   #8@shop
 80   10        #106 (Ticket 106)                                 #8@shop
      **517**
==== ========= ================================================= =================== ========
<BLANKLINE>




Release notes
=============

Lino Noi has an excerpt type for printing a milestone.  This was used
to produce *release notes*.

>>> obj = deploy.Milestone.objects.get(pk=7)
>>> rt.show(rt.actors.deploy.DeploymentsByMilestone, obj)
======== ====== ============================ ======= ========
 No.      Move   Ticket                       State   Remark
-------- ------ ---------------------------- ------- --------
 1               #9 (Foo never matches Bar)   New
 2               #19 (Ticket 19)              Open
 3               #30 (Ticket 30)              Ready
 4               #41 (Ticket 41)              New
 5               #51 (Ticket 51)              Open
 6               #62 (Ticket 62)              Ready
 7               #73 (Ticket 73)              New
 8               #83 (Ticket 83)              Open
 9               #94 (Ticket 94)              Ready
 10              #105 (Ticket 105)            New
 11              #115 (Ticket 115)            Open
 **66**
======== ====== ============================ ======= ========
<BLANKLINE>

>>> rt.show(clocking.OtherTicketsByMilestone, obj) #doctest: +SKIP
No data to display

>>> url = '/choices/deploy/DeploymentsByTicket/milestone'
>>> show_choices('robin', url)
#8@shop
20150503@docs
20150505@research
20150507@shop
20150509@linö
20150511@téam
20150513@docs
20150515@research

>>> show_choices('robin', url+"?query=0507")
20150507@shop

>>> show_choices('robin', url+"?query=2015050")
20150503@docs
20150505@research
20150507@shop
20150509@linö




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
==== ================= ================================ ============================
 ID   Dependency type   Parent                           Child
---- ----------------- -------------------------------- ----------------------------
 1    Requires          #1 (Föö fails to bar when baz)   #2 (Bar is not always baz)
==== ================= ================================ ============================
<BLANKLINE>


Comments
========

Comments on private tickets are not shown to anonymous users:

>>> rt.show(comments.Comments, column_names="id user owner")
==== ================= =================================================
 ID   Author            Ticket
---- ----------------- -------------------------------------------------
 1    Jean              #1 (Föö fails to bar when baz)
 4    Romain Raffault   #4 (Foo and bar don't baz)
 6    Robin Rood        #6 (Sell bar in baz)
 7    Jean              #7 (No Foo after deleting Bar)
 8    Luc               #8 (Is there any Bar in Foo?)
 10   Romain Raffault   #10 (Where can I find a Foo when bazing Bazes?)
 11   Rolf Rompen       #11 (Class-based Foos and Bars?)
 12   Robin Rood        #12 (Foo cannot bar)
==== ================= =================================================
<BLANKLINE>

The same list seen by marc

>>> rt.login('luc').show('comments.Comments', column_names="id user owner")
==== ================= =================================================
 ID   Author            Ticket
---- ----------------- -------------------------------------------------
 1    Jean              #1 (Föö fails to bar when baz)
 2    Luc               #2 (Bar is not always baz)
 3    Mathieu           #3 (Baz sucks)
 4    Romain Raffault   #4 (Foo and bar don't baz)
 5    Rolf Rompen       #5 (Cannot create Foo)
 6    Robin Rood        #6 (Sell bar in baz)
 7    Jean              #7 (No Foo after deleting Bar)
 8    Luc               #8 (Is there any Bar in Foo?)
 9    Mathieu           #9 (Foo never matches Bar)
 10   Romain Raffault   #10 (Where can I find a Foo when bazing Bazes?)
 11   Rolf Rompen       #11 (Class-based Foos and Bars?)
 12   Robin Rood        #12 (Foo cannot bar)
==== ================= =================================================
<BLANKLINE>


>>> obj = tickets.Ticket.objects.get(pk=6)
>>> rt.show(comments.CommentsByRFC, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
<ul><li><a href="Detail" title="Created ...">...</a> by <em>Robin Rood</em> <a href="#" onclick="toggle_visibility('comment-6');" title="Hide">&#8284;</a><div id=comment-6>...</div></li></ul>



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
| site            | Site            | Select a site if you want to see only tickets for this site.  |
+-----------------+-----------------+---------------------------------------------------------------+
| project         | Project         |                                                               |
+-----------------+-----------------+---------------------------------------------------------------+
| state           | State           | Only rows having this state.                                  |
+-----------------+-----------------+---------------------------------------------------------------+
| deployed_to     | Milestone       |                                                               |
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
    - (general1_3): **Site** (site), **Topic** (topic), **Project** (project)
    - (general1_4): **Actions** (workflow_buttons), **Private** (private)
    - (bottom_box) [visible for user consultant hoster developer senior admin]:
      - (bottom_box_1): **Wanted skills** (DemandsByDemander), **Votes** (VotesByVotable)
      - (bottom_box_2): **Wishes** (DeploymentsByTicket), **Sessions** (SessionsByTicket) [visible for consultant hoster developer senior admin]
  - **Comments** (CommentsByRFC)
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


