.. doctest docs/specs/noi/tickets.rst
.. _noi.specs.tickets:

======================================
``tickets`` (Ticket management in Noi)
======================================

The :mod:`lino_noi.lib.tickets` plugin
extends :mod:`lino_xl.lib.tickets` to make it collaborate with :mod:`lino_noi.lib.working`.

.. contents::
  :local:

.. currentmodule:: lino_noi.lib.tickets

.. include:: /include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.team.settings.demo')
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
      - **Sessions** (working_SessionsByTicket) [visible for consultant hoster developer senior admin]
  - **Comments** (comments_CommentsByRFC) [visible for user consultant hoster developer senior admin]
- **More** (more):
  - (more_1):
    - (more1):
      - (more1_1): **Created** (created), **Modified** (modified), **Fixed since** (fixed_since)
      - (more1_2): **State** (state), **Reference** (ref), **Duplicate of** (duplicate_of), **Deadline** (deadline)
    - **Duplicates** (DuplicatesByTicket)
  - (more_2): **Resolution** (upgrade_notes), **Dependencies** (tickets_LinksByTicket) [visible for senior admin], **Uploads** (uploads_UploadsByController) [visible for user consultant hoster developer senior admin]
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




