.. doctest docs/specs/noi/working.rst
.. _specs.clocking:
.. _noi.specs.clocking:

==================
Work time tracking
==================

.. doctest init:

    >>> from lino import startup
    >>> startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *

.. currentmodule:: lino_xl.lib.working
     
The :mod:`lino_xl.lib.working` adds functionality for managing work
sessions.  A **work session** is when a user works on a "ticket" for a
given lapse of time.

What a ticket exactly is, is defined by :attr:`ticket_model
<Plugin.ticket_model>`. Theoretically it
can be any model which implements :class:`Workable`.
In :ref:`noi` this points to
:class:`tickets.Ticket <lino_xl.lib.tickets.Ticket>`. 
:mod:`lino_noi.lib.working` extends the library plugin.
     

Note that the demo data is on fictive demo date **May 23, 2015**:

>>> dd.today()
datetime.date(2015, 5, 23)


Sessions
========


>>> rt.show(working.Sessions, limit=15)
... #doctest: -REPORT_UDIFF
================================== ========= ============ ============ ============ ========== ============ ========= =========== =================
 Ticket                             Worker    Start date   Start time   End Date     End Time   Break Time   Summary   Duration    Ticket #
---------------------------------- --------- ------------ ------------ ------------ ---------- ------------ --------- ----------- -----------------
 #1 (⛶ Föö fails to bar when baz)   Jean      23/05/2015   09:00:00                                                                `#1 <Detail>`__
 #1 (⛶ Föö fails to bar when baz)   Luc       23/05/2015   09:00:00                                                                `#1 <Detail>`__
 #1 (⛶ Föö fails to bar when baz)   Mathieu   23/05/2015   09:00:00                                                                `#1 <Detail>`__
 #2 (☎ Bar is not always baz)       Jean      22/05/2015   09:00:00     22/05/2015   11:18:00                          2:18        `#2 <Detail>`__
 #2 (☎ Bar is not always baz)       Luc       22/05/2015   09:00:00     22/05/2015   12:29:00                          3:29        `#2 <Detail>`__
 #2 (☎ Bar is not always baz)       Mathieu   22/05/2015   09:00:00     22/05/2015   12:53:00                          3:53        `#2 <Detail>`__
 #4 (⚒ Foo and bar don't baz)       Mathieu   20/05/2015   09:05:00     20/05/2015   09:17:00                          0:12        `#4 <Detail>`__
 #3 (☉ Baz sucks)                   Jean      20/05/2015   09:00:00     20/05/2015   10:30:00                          1:30        `#3 <Detail>`__
 #3 (☉ Baz sucks)                   Luc       20/05/2015   09:00:00     20/05/2015   09:37:00                          0:37        `#3 <Detail>`__
 #3 (☉ Baz sucks)                   Mathieu   20/05/2015   09:00:00     20/05/2015   09:05:00                          0:05        `#3 <Detail>`__
 #4 (⚒ Foo and bar don't baz)       Jean      19/05/2015   09:00:00     19/05/2015   09:10:00                          0:10        `#4 <Detail>`__
 #4 (⚒ Foo and bar don't baz)       Luc       19/05/2015   09:00:00     19/05/2015   10:02:00                          1:02        `#4 <Detail>`__
 #5 (☾ Cannot create Foo)           Mathieu   19/05/2015   09:00:00     19/05/2015   11:18:00                          2:18        `#5 <Detail>`__
 **Total (13 rows)**                                                                                                   **15:34**
================================== ========= ============ ============ ============ ========== ============ ========= =========== =================
<BLANKLINE>


Some sessions are on private tickets:

>>> from django.db.models import Q
>>> rt.show(working.Sessions, column_names="ticket user duration ticket__project", filter=Q(ticket__private=True))
... #doctest: -REPORT_UDIFF
============================== ========= =========== =========
 Ticket                         Worker    Duration    Mission
------------------------------ --------- ----------- ---------
 #2 (☎ Bar is not always baz)   Jean      2:18        téam
 #2 (☎ Bar is not always baz)   Luc       3:29        téam
 #2 (☎ Bar is not always baz)   Mathieu   3:53        téam
 #3 (☉ Baz sucks)               Jean      1:30
 #3 (☉ Baz sucks)               Luc       0:37
 #3 (☉ Baz sucks)               Mathieu   0:05
 #5 (☾ Cannot create Foo)       Mathieu   2:18
 **Total (7 rows)**                       **14:10**
============================== ========= =========== =========
<BLANKLINE>


Worked hours
============

This table shows the last seven days, one row per day, with your
working hours.

>>> rt.login('jean').show(working.WorkedHours)
... #doctest: -REPORT_UDIFF
====================================== ========== ========== ====== ==========
 Description                            Regular    Extra      Free   Total
-------------------------------------- ---------- ---------- ------ ----------
 **Sat 23/05/2015** (`#1 <Detail>`__)   0:01                         0:01
 **Fri 22/05/2015** (`#2 <Detail>`__)   2:18                         2:18
 **Thu 21/05/2015**                                                  0:00
 **Wed 20/05/2015** (`#3 <Detail>`__)              1:30              1:30
 **Tue 19/05/2015** (`#4 <Detail>`__)   0:10                         0:10
 **Mon 18/05/2015**                                                  0:00
 **Sun 17/05/2015**                                                  0:00
 **Total (7 rows)**                     **2:29**   **1:30**          **3:59**
====================================== ========== ========== ====== ==========
<BLANKLINE>


In the "description" column you see a list of the tickets on which you
worked that day. This is a convenient way to continue some work you
started some days ago.

.. 
    Find the users who worked on more than one mission:
    >>> for u in users.User.objects.all():
    ...     qs = tickets.Project.objects.filter(tickets_by_project__sessions_by_ticket__user=u).distinct()
    ...     if qs.count() > 1:
    ...         print("{} {} {}".format(str(u.username), "worked on", [o for o in qs]))
    jean worked on [Project #1 ('lin\xf6'), Project #2 ('t\xe9am'), Project #3 ('docs')]
    luc worked on [Project #1 ('lin\xf6'), Project #2 ('t\xe9am'), Project #3 ('docs')]
    mathieu worked on [Project #1 ('lin\xf6'), Project #2 ('t\xe9am'), Project #3 ('docs')]

    Render this table to HTML in order to reproduce :ticket:`523`:

    >>> url = "/api/working/WorkedHours?"
    >>> url += "_dc=1442341081053&cw=430&cw=83&cw=83&cw=83&cw=83&cw=83&cw=83&ch=&ch=&ch=&ch=&ch=&ch=&ch=&ci=description&ci=vc0&ci=vc1&ci=vc2&ci=vc3&ci=vc4&ci=vc5&name=0&pv=16.05.2015&pv=23.05.2015&pv=7&an=show_as_html&sr="
    >>> test_client.force_login(rt.login('jean').user)
    >>> res = test_client.get(url, REMOTE_USER="jean")
    >>> json.loads(res.content.decode())
    {u'open_url': u'/bs3/working/WorkedHours?limit=15', u'success': True}


    The html version of this table table has only 5 rows (4 data rows and
    the total row) because valueless rows are not included by default:

    >>> ar = rt.login('jean')
    >>> u = ar.get_user()
    >>> ar = working.WorkedHours.request(user=u)
    >>> ar = ar.spawn(working.WorkedHours)
    >>> lst = list(ar)
    >>> len(lst)
    7
    >>> e = ar.table2xhtml()
    >>> len(e.findall('./tbody/tr'))
    5




Service Report
==============

A service report (:class:`ServiceReport`) is a document which reports
about the hours invested during a given date range.  It can be
addressed to a recipient (a user) and in that case will consider only
the tickets for which this user has specified interest.

It currently contains two tables:

- a list of tickets, with invested time (i.e. the sum of durations
  of all sessions that lie in the given data range)
- a list of projects, with invested time and list of the tickets that
  are assigned to this project.

This report can serve as a base for writing invoices.


>>> obj = working.ServiceReport.objects.get(pk=1)
>>> obj.printed_by.build_method
<BuildMethods.weasy2html:weasy2html>


>>> obj.interesting_for
Partner #108 ('welket')

>>> rt.show(working.SessionsByReport, obj)
... #doctest: -REPORT_UDIFF +SKIP
==================== ============ ========== ============ ================== ========== ======= ======
 Start date           Start time   End Time   Break Time   Description        Regular    Extra   Free
-------------------- ------------ ---------- ------------ ------------------ ---------- ------- ------
 23/05/2015           09:00:00                             `#1 <Detail>`__    0:01
 22/05/2015           09:00:00     12:29:00                `#11 <Detail>`__   3:29
 20/05/2015           09:00:00     09:05:00                `#6 <Detail>`__    0:05
 **Total (3 rows)**                                                           **3:35**
==================== ============ ========== ============ ================== ========== ======= ======
<BLANKLINE>

Note that there are sessions without a duration. That's because

>>> rt.show(working.TicketsByReport, obj)
... #doctest: -REPORT_UDIFF
==== ========================================================= ========= ======= ========== ======= ======
 ID   Description                                               Mission   State   Regular    Extra   Free
---- --------------------------------------------------------- --------- ------- ---------- ------- ------
 1    `#1 (⛶ Föö fails to bar when baz) <Detail>`__  by *Luc*   linö      New     0:03
                                                                                  **0:03**
==== ========================================================= ========= ======= ========== ======= ======
<BLANKLINE>


The :class:`ProjectsByReport` table lists
all projects and the time invested.

>>> rt.show(working.ProjectsByReport, obj)
==================== ====== ================= ========== ======= ======
 Reference            Name   Tickets           Regular    Extra   Free
-------------------- ------ ----------------- ---------- ------- ------
 téam                 Téam   `#2 <Detail>`__   9:40
 **Total (1 rows)**                            **9:40**
==================== ====== ================= ========== ======= ======
<BLANKLINE>


Reporting type
==============

The :attr:`reporting_type` of a project indicates how the client is
going to pay for the work done.

The default implementation offers three choices "Worker", "Employer"
and "Customer". "Worker" is for volunteer work and "private fun" where
the worker does not get paid by anybody.  "Employer" is when working
time should be reported to the employer (but no customer is going to
pay for it directly).  "Customer" is when working time should be
reported to the customer.

>>> rt.show(working.ReportingTypes)
======= ========= =========
 value   name      text
------- --------- ---------
 10      regular   Regular
 20      extra     Extra
 30      free      Free
======= ========= =========
<BLANKLINE>


The local site admin can adapt above list to the site's needs. He also
defines a default reporting type:

>>> dd.plugins.working.default_reporting_type
<ReportingTypes.regular:10>


Reference
=========

.. class:: Plugin
.. class:: SessionType
           
    The type of a :class:`Session`.
    
.. class:: Session

    A **Session** is when a user works during a given lapse of time on
    a given Ticket.

    Extreme case of a session:

    - I start to work on an existing ticket #1 at 9:23.  A customer phones
      at 10:17 with a question. I create #2.  That call is interrupted
      several times by the customer himself.  During the first
      interruption another customer calls, with another problem (ticket
      #3) which we solve together within 5 minutes.  During the second
      interruption of #2 (which lasts 7 minutes) I make a coffee break.

      During the third interruption I continue to analyze the
      customer's problem.  When ticket #2 is solved, I decided that
      it's not worth to keep track of each interruption and that the
      overall session time for this ticket can be estimated to 0:40.

      ::

        Ticket start end    Pause  Duration
        #1      9:23 13:12  0:45
        #2     10:17 11:12  0:12       0:43
        #3     10:23 10:28             0:05


    .. attribute:: start_date

        The date when you started to work.

    .. attribute:: start_time

        The time (in `hh:mm`) when you started working on this
        session.

        This is your local time according to the time zone specified
        in your preferences.

    .. attribute:: end_date

        Leave this field blank if it is the same date as start_date.

    .. attribute:: end_time

        The time (in `hh:mm`) when the worker stopped to work.
        
        An empty :attr:`end_time` means that the user is still busy
        with that session, the session is not yet closed.

        :meth:`end_session` sets this to the current time.


    .. attribute:: break_time
    
       The time (in `hh:mm`) to remove from the duration resulting
       from the difference between :attr:`start_time` and
       :attr:`end_time`.

    .. attribute:: faculty

       The faculty that has been used during this session. On a new
       session this defaults to the needed faculty currently specified
       on the ticket.


.. class:: Sessions
           
.. class:: SessionsByTicket
           
    The "Sessions" panel in the detail of a ticket.

    .. attribute:: slave_summary

        This panel shows:

.. class:: MySessions
           
.. class:: MySessionsByDate

           
.. class:: StartTicketSession
           
    Start a session on this ticket.

.. class:: EndTicketSession
           
    Close this session, i.e. stop working it for now.

    Common base for :class:`EndThisSession` and
    :class:`EndTicketSession`.

    
.. class:: EndTicketSession
           
    End your running session on this ticket. 
    
.. class:: EndThisSession
           
    Close this session, i.e. stop working on that ticket now.

           

.. class:: Workable
           
    Base class for things that workers can work on. 

    The model specified in :attr:`ticket_model <Plugin.ticket_model>`
    must be a subclass of this.
    
    For example, in :ref:`noi` tickets are workable.

    .. method:: is_workable_for
                
        Return True if the given user can start a working session on this
        object.

                
    .. method:: on_worked
                
        This is automatically called when a work session has been created
        or modified.

                
    .. method:: start_session

        See :class:`StartTicketSession`.
        
    .. method:: end_session

        See :class:`EndTicketSession`.
        
           
.. class:: ServiceReport

    A **service report** is a document used in various discussions with
    a stakeholder.

    Defined in :mod:`lino_noi.lib.working`.

    .. attribute:: user

        This can be empty and will then show the working time of all
        users.


    .. attribute:: start_date
    .. attribute:: end_date
    .. attribute:: interesting_for
    .. attribute:: ticket_state

    .. attribute:: printed
        See :attr:`lino.modlib.exerpts.mixins.Certifiable.printed`

           
           
.. class:: ProjectsByReport
           
.. class:: ShowMySessionsByDay
           
    Show all sessions on the same day.
    


.. class:: TicketHasSessions

    Select only tickets for which there has been at least one session
    during the given period.

    This is added as item to :class:`lino_xl.lib.tickets.TicketEvents`.

           
.. class:: ProjectHasSessions
           
    Select only projects for which there has been at least one session
    during the given period.

    This is added as item to :class:`lino_xl.lib.tickets.ProjectEvents`.
    
.. class:: Worker

    A user who is candidate for working on a ticket.

           
