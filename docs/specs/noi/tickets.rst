.. doctest docs/specs/noi/tickets.rst
.. _noi.specs.tickets:

======================================
``tickets`` (Ticket management in Noi)
======================================

The :mod:`lino_noi.lib.tickets` plugin extends :mod:`lino_xl.lib.tickets` to
make it collaborate with :mod:`lino_noi.lib.working`.

In :ref:`noi` the *site* of a *ticket* also indicates "who is going to pay" for
our work. Lino Noi uses this information when generating a service report.




.. contents::
  :local:

.. currentmodule:: lino_noi.lib.tickets

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
      - **Description** (description)
    - (general1b):
      - (general1b_1): **Author** (user), **End user** (end_user)
      - (general1b_2): **Assigned to** (assigned_to), **Private** (private)
      - (general1b_3): **Priority** (priority), **Planned time** (planned_time)
      - (general1b_4): **Regular** (regular_hours), **Extra** (extra_hours), **Free** (free_hours)
      - **Sessions** (working_SessionsByTicket) [visible for contributor developer admin]
  - **Comments** (comments_CommentsByRFC)
- **More** (more):
  - (more_1):
    - (more1):
      - (more1_1): **Created** (created), **Modified** (modified), **Fixed since** (fixed_since)
      - (more1_2): **State** (state), **Reference** (ref), **Duplicate of** (duplicate_of), **Deadline** (deadline)
    - **Duplicates** (DuplicatesByTicket)
  - (more_2): **Resolution** (upgrade_notes), **Dependencies** (tickets_LinksByTicket) [visible for developer admin], **Uploads** (uploads_UploadsByController) [visible for customer contributor developer admin]
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

In :ref:`noi` we use the following ticket states.

>>> rt.show(tickets.TicketStates)
======= =========== ========== ============= ========
 value   name        text       Button text   Active
------- ----------- ---------- ------------- --------
 10      new         New        ⛶             Yes
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
