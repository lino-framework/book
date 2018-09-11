.. doctest docs/specs/noi/sql.rst
   
.. _specs.noi.sql:

==================================
Exploring SQL activity in Lino Noi
==================================

This document shows why Jane is so slow when displaying tickets.
It is also a demo of
the :func:`show_sql_queries <lino.api.doctest.show_sql_queries>`
function.

We use the :mod:`lino_book.projects.team` demo database.
    
>>> import lino
>>> lino.startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *

During startup there were two SQL queries:

>>> show_sql_queries()  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
SELECT ... FROM excerpts_excerpttype
SELECT ... FROM django_content_type WHERE django_content_type.id = ...


Now we do a single request to :class:`Tickets`. And look at all the
SQL that poor Django must do in order to return a single row. 

>>> reset_sql_queries()
>>> r = demo_get('robin','api/tickets/Tickets', fmt='json')

>> r = demo_get('robin','api/tickets/Tickets', fmt='json', limit=1)
>> res = test_client.get('/api/tickets/Tickets?fmt=json&limit=1')
>> res = check_json_result(res)
>> rmu(res.keys())
['count', 'rows', 'no_data_text', 'success', 'title', 'param_values']
>> len(res['rows'])
1

>>> show_sql_summary()
================= =========== =======
 table             stmt_type   count
----------------- ----------- -------
 django_session    SELECT      1
 tickets_site      SELECT      7
 tickets_ticket    SELECT      2
 users_user        SELECT      1
 working_session   SELECT      15
================= =========== =======
<BLANKLINE>

>>> show_sql_queries()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP


To verify whether the slave summary panels are being computed:

>>> for f in sorted([str(f) for f in rt.models.tickets.Tickets.wildcard_data_elems()]):
...     print(f)  #doctest: +REPORT_UDIFF
lino.core.model.Model.mobile_item
lino.core.model.Model.overview
lino.core.model.Model.workflow_buttons
lino.mixins.Created.created_natural
tickets.Ticket.assigned_to
tickets.Ticket.closed
tickets.Ticket.created
tickets.Ticket.deadline
tickets.Ticket.description
tickets.Ticket.duplicate_of
tickets.Ticket.end_user
tickets.Ticket.feedback
tickets.Ticket.fixed_since
tickets.Ticket.id
tickets.Ticket.modified
tickets.Ticket.planned_time
tickets.Ticket.priority
tickets.Ticket.private
tickets.Ticket.project
tickets.Ticket.ref
tickets.Ticket.reporter
tickets.Ticket.site
tickets.Ticket.standby
tickets.Ticket.state
tickets.Ticket.summary
tickets.Ticket.ticket_type
tickets.Ticket.topic
tickets.Ticket.upgrade_notes
tickets.Ticket.user
tickets.Ticket.waiting_for

    

