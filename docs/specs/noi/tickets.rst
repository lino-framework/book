.. doctest docs/specs/noi/tickets.rst
.. _noi.specs.tickets:

======================================
``tickets`` (Ticket management in Noi)
======================================

The :mod:`lino_noi.lib.tickets` plugin extends :mod:`lino_xl.lib.tickets` to
make it collaborate with :mod:`lino_noi.lib.working`.

In :ref:`noi` the *site* of a *ticket* also indicates "who is going to pay" for
our work. Lino Noi uses this information when generating a service report.


.. currentmodule:: lino_noi.lib.tickets


.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *



Tickets
=======

Here is a textual description of the fields and their layout used in
the detail window of a ticket.

>>> from lino.utils.diag import py2rst
>>> print(py2rst(tickets.AllTickets.detail_layout, True))
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
(main) [visible for all]:
- **General** (general_1):
  - (general1_1):
    - (general1a):
      - (general1a_1): **Summary** (summary), **ID** (id)
      - (general1a_2): **Site** (site), **Ticket type** (ticket_type)
      - **Workflow** (workflow_buttons)
      - **Dependencies** (tickets_LinksByTicket) [visible for developer admin]
    - (general1b):
      - (general1b_1): **Author** (user), **End user** (end_user)
      - (general1b_2): **Assign to** (quick_assign_to), **Private** (private)
      - (general1b_3): **Priority** (priority), **Planned time** (planned_time)
      - (general1b_4): **Regular** (regular_hours), **Extra** (extra_hours), **Free** (free_hours)
      - **Sessions** (working_SessionsByTicket) [visible for contributor developer admin]
  - **Comments** (comments.CommentsByRFC)
- **More** (more):
  - (more_1):
    - (more1):
      - (more1_1): **Created** (created), **Modified** (modified), **Fixed since** (fixed_since)
      - (more1_2): **State** (state), **Assigned to** (assigned_to), **Reference** (ref), **Duplicate of** (duplicate_of), **Deadline** (deadline)
    - **Duplicates** (DuplicatesByTicket)
  - (more_2): **Resolution** (upgrade_notes), **Description** (description), **Upload files** (uploads_UploadsByController) [visible for customer contributor developer admin]
  - **Checks** (tickets.CheckListItemsByTicket) [visible for customer contributor developer admin]
- **Mentions** (comments_CommentsByMentioned)
<BLANKLINE>


.. class:: Ticket

    The Django model used to represent a *ticket* in Noi. Adds some fields and
    methods.

    .. attribute:: assigned_to

        The user who is working on this ticket.

    .. attribute:: site

        The site this ticket belongs to.
        You can select only sites you are subscribed to.


Screenshots
===========

.. image:: tickets.Ticket.merge.png


The life cycle of a ticket
==========================

In :ref:`noi` we use the default tickets workflow defined  in
:class:`lino_xl.lib.tickets.TicketStates`.


Sites
=====

The list of the sites in our demo database depends on who is looking at it.
Anonymous users can see only public sites:

>>> rt.show(tickets.Sites)
=========== ============= ======== ================ ======== ============== ====
 Reference   Designation   Client   Contact person   Remark   Workflow       ID
----------- ------------- -------- ---------------- -------- -------------- ----
 bugs        bugs                                             **⚒ Active**   5
 docs        docs                                             **⚒ Active**   4
 pypi        pypi                                             **⚒ Active**   3
=========== ============= ======== ================ ======== ============== ====
<BLANKLINE>

>>> rt.login("marc").show(tickets.Sites)
=========== ===================== ===================== ================ ======== ================================ ====
 Reference   Designation           Client                Contact person   Remark   Workflow                         ID
----------- --------------------- --------------------- ---------------- -------- -------------------------------- ----
 bugs        bugs                                                                  **⚒ Active** → [⛶] [☉] [☾] [☑]   5
 docs        docs                                                                  **⚒ Active**                     4
 pypi        pypi                                                                  **⚒ Active**                     3
 welsch      Bäckerei Ausdemwald   Bäckerei Ausdemwald   Annette Arens             **⚒ Active** → [⛶] [☉] [☾] [☑]   2
=========== ===================== ===================== ================ ======== ================================ ====
<BLANKLINE>

>>> rt.login("jean").show(tickets.Sites)
=========== ===================== ===================== ================ ======== ================================ ====
 Reference   Designation           Client                Contact person   Remark   Workflow                         ID
----------- --------------------- --------------------- ---------------- -------- -------------------------------- ----
 bugs        bugs                                                                  **⚒ Active** → [⛶] [☉] [☾] [☑]   5
 docs        docs                                                                  **⚒ Active** → [⛶] [☉] [☾] [☑]   4
 pypi        pypi                                                                  **⚒ Active** → [⛶] [☉] [☾] [☑]   3
 welket      Rumma & Ko OÜ         Rumma & Ko OÜ         Andreas Arens             **⚒ Active** → [⛶] [☉] [☾] [☑]   1
 welsch      Bäckerei Ausdemwald   Bäckerei Ausdemwald   Annette Arens             **⚒ Active** → [⛶] [☉] [☾] [☑]   2
=========== ===================== ===================== ================ ======== ================================ ====
<BLANKLINE>

>>> rt.login("mathieu").show(tickets.Sites)
=========== ============= ======== ================ ======== ================================ ====
 Reference   Designation   Client   Contact person   Remark   Workflow                         ID
----------- ------------- -------- ---------------- -------- -------------------------------- ----
 bugs        bugs                                             **⚒ Active**                     5
 docs        docs                                             **⚒ Active**                     4
 pypi        pypi                                             **⚒ Active** → [⛶] [☉] [☾] [☑]   3
=========== ============= ======== ================ ======== ================================ ====
<BLANKLINE>


List of sites to which Jean is "subscribed" (i.e. that are assigned to a team
where Jean is member):

>>> rt.login("jean").show(tickets.MySites)
=================== ============= ================================
 Site                Description   Workflow
------------------- ------------- --------------------------------
 `pypi <Detail>`__                 **⚒ Active** → [⛶] [☉] [☾] [☑]
=================== ============= ================================
<BLANKLINE>

List of tickets that have not yet been assigned to a site:

>>> pv = dict(has_site=dd.YesNo.no)
>>> rt.login("robin").show(tickets.AllTickets, param_values=pv)
... #doctest: -REPORT_UDIFF +ELLIPSIS
===== ============================================== ========== ================================== ======
 ID    Summary                                        Priority   Workflow                           Site
----- ---------------------------------------------- ---------- ---------------------------------- ------
 110   Why is foo so bar                              Normal     [▶] **☐ Ready** → [☒]
 108   No more foo when bar is gone                   Normal     [▶] **⚒ Working** → [☾] [☐] [☒]
 100   Cannot delete foo                              Normal     [▶] **⚒ Working** → [☾] [☐] [☒]
 94    How can I see where bar?                       Normal     [▶] **☐ Ready** → [☒]
 90    No more foo when bar is gone                   Normal     [▶] **☎ Talk** → [☾] [☉] [☐] [☒]
 80    Foo never bars                                 Normal     [▶] **☒ Refused**
 70    'NoneType' object has no attribute 'isocode'   Normal     [▶] **☐ Ready** → [☒]
 66    Irritating message when bar                    Normal     [▶] **☎ Talk** → [☾] [☉] [☐] [☒]
 60    Default account in invoices per partner        Normal     [▶] **⚒ Working** → [☾] [☐] [☒]
 52    'NoneType' object has no attribute 'isocode'   Normal     [▶] **⚒ Working** → [☾] [☐] [☒]
 50    Misc optimizations in Baz                      Normal     [▶] **☎ Talk** → [☾] [☉] [☐] [☒]
 40    How can I see where bar?                       Normal     [▶] **☒ Refused**
 38    Why is foo so bar                              Normal     [▶] **☐ Ready** → [☒]
 30    Irritating message when bar                    Normal     [▶] **☐ Ready** → [☒]
 24    Default account in invoices per partner        Normal     [▶] **☒ Refused**
 20    Why is foo so bar                              Normal     [▶] **⚒ Working** → [☾] [☐] [☒]
 10    Where can I find a Foo when bazing Bazes?      Normal     [▶] **☎ Talk** → [☾] [☉] [☐] [☒]
===== ============================================== ========== ================================== ======
<BLANKLINE>

Ticket types
============

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
 Normal     `#50 (☎ Misc optimizations in Baz) <Detail>`__                       Jean                                                  [▶] **☎ Talk** → [☾] [☉] [☐] [☒]
 Normal     `#43 (☉ 'NoneType' object has no attribute 'isocode') <Detail>`__    Luc                                                   [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal     `#36 (⚒ No more foo when bar is gone) <Detail>`__                    Mathieu                                               [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal     `#22 (☐ How can I see where bar?) <Detail>`__                        Jean                                                  [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal     `#1 (⛶ Föö fails to bar when baz) <Detail>`__                                                                              [✋] [■] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
========== ==================================================================== ============= ============== ========= ======= ====== =============================================
<BLANKLINE>


The backlog
===========

The :class:`TicketsBySite` panel shows all the tickets for a given site. It is
a scrum backlog.

>>> welket = tickets.Site.objects.get(ref="welket")
>>> rt.login("robin").show(tickets.TicketsBySite, welket)
... #doctest: +REPORT_UDIFF -SKIP +ELLIPSIS +NORMALIZE_WHITESPACE
===================== ==================================================================== ============== ========== ======= ====== =============================================
 Priority              Ticket                                                               Planned time   Regular    Extra   Free   Workflow
--------------------- -------------------------------------------------------------------- -------------- ---------- ------- ------ ---------------------------------------------
 Normal                `#114 (☎ Default account in invoices per partner) <Detail>`__                                                 [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#106 (☎ 'NoneType' object has no attribute 'isocode') <Detail>`__                                            [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#91 (☉ Cannot delete foo) <Detail>`__                                                                        [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal                `#84 (⚒ Irritating message when bar) <Detail>`__                                                              [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#82 (☎ Cannot delete foo) <Detail>`__                                                                        [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#81 (⛶ No more foo when bar is gone) <Detail>`__                                                             [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 Normal                `#74 (☎ Why is foo so bar) <Detail>`__                                                                        [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#68 (⚒ Misc optimizations in Baz) <Detail>`__                                                                [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#62 (☐ Foo never bars) <Detail>`__                                                                           [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal                `#58 (☎ How can I see where bar?) <Detail>`__                                                                 [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#51 (☉ Default account in invoices per partner) <Detail>`__                                                  [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal                `#44 (⚒ Foo never bars) <Detail>`__                                                                           [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#42 (☎ Default account in invoices per partner) <Detail>`__                                                  [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#41 (⛶ Misc optimizations in Baz) <Detail>`__                                                                [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 Normal                `#36 (⚒ No more foo when bar is gone) <Detail>`__                                                             [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#18 (☎ No more foo when bar is gone) <Detail>`__                                                             [▶] **☎ Talk** → [☾] [☉] [⚒] [☐] [☑] [☒]
 Normal                `#14 (☐ Bar cannot baz) <Detail>`__                                                                           [▶] **☐ Ready** → [☎] [☑] [☒]
 Normal                `#12 (⚒ Foo cannot bar) <Detail>`__                                                                           [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#11 (☉ Class-based Foos and Bars?) <Detail>`__                                                               [▶] **☉ Open** → [☾] [☎] [⚒] [☐] [☑] [☒]
 Normal                `#4 (⚒ Foo and bar don't baz) <Detail>`__                                           1:24                      [▶] **⚒ Working** → [☾] [☎] [☐] [☑] [☒]
 Normal                `#1 (⛶ Föö fails to bar when baz) <Detail>`__                                                                 [✋] [▶] **⛶ New** → [☾] [☎] [☉] [⚒] [☐] [☑]
 **Total (21 rows)**                                                                                       **1:24**
===================== ==================================================================== ============== ========== ======= ====== =============================================
<BLANKLINE>


Note that anonymous cannot see tickets without a site.

>>> rt.show(tickets.TicketsBySite, welket)
... #doctest: +REPORT_UDIFF -SKIP +ELLIPSIS +NORMALIZE_WHITESPACE
No data to display

Links between tickets
=====================

>>> rt.show(tickets.Links)
... #doctest: +REPORT_UDIFF
==== ================= ================================== ==============================
 ID   Dependency type   Parent                             Child
---- ----------------- ---------------------------------- ------------------------------
 1    Requires          #1 (⛶ Föö fails to bar when baz)   #2 (☎ Bar is not always baz)
==== ================= ================================== ==============================
<BLANKLINE>


Filtering tickets
=================

:ref:`noi` modifies the list of the parameters you can use for filterings
tickets be setting a custom :attr:`params_layout`.

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
