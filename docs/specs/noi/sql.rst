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

>>> r = demo_get('robin','api/tickets/Tickets', fmt='json')

>> r = demo_get('robin','api/tickets/Tickets', fmt='json', limit=1)
>> res = test_client.get('/api/tickets/Tickets?fmt=json&limit=1')
>> res = check_json_result(res)
>> rmu(res.keys())
['count', 'rows', 'no_data_text', 'success', 'title', 'param_values']
>> len(res['rows'])
1

>>> show_sql_summary()
===================== =======
 table                 count
--------------------- -------
 django_content_type   1
 django_session        1
 stars_star            22
 tickets_site          7
 tickets_ticket        2
 users_user            1
 working_session       15
===================== =======
<BLANKLINE>

>>> show_sql_queries()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP


To verify whether the slave summary panels are being computed:

>>> for f in rt.models.tickets.Tickets.wildcard_data_elems():
...     print(f)  #doctest: +REPORT_UDIFF
tickets.Ticket.id
tickets.Ticket.modified
tickets.Ticket.created
tickets.Ticket.ref
tickets.Ticket.user
tickets.Ticket.assigned_to
tickets.Ticket.private
tickets.Ticket.priority
tickets.Ticket.closed
tickets.Ticket.planned_time
tickets.Ticket.project
tickets.Ticket.site
tickets.Ticket.topic
tickets.Ticket.summary
tickets.Ticket.description
tickets.Ticket.upgrade_notes
tickets.Ticket.ticket_type
tickets.Ticket.duplicate_of
tickets.Ticket.end_user
tickets.Ticket.state
tickets.Ticket.deadline
tickets.Ticket.reported_for
tickets.Ticket.fixed_for
tickets.Ticket.reporter
tickets.Ticket.waiting_for
tickets.Ticket.feedback
tickets.Ticket.standby
tickets.Ticket.fixed_since
lino.core.model.Model.workflow_buttons
lino.core.model.Model.mobile_item
lino.core.model.Model.overview
lino.mixins.Created.created_natural

    

