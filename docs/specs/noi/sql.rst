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
SELECT excerpts_excerpttype.id, excerpts_excerpttype.name, excerpts_excerpttype.build_method, excerpts_excerpttype.template, excerpts_excerpttype.attach_to_email, excerpts_excerpttype.email_template, excerpts_excerpttype.certifying, excerpts_excerpttype.remark, excerpts_excerpttype.body_template, excerpts_excerpttype.content_type_id, excerpts_excerpttype.primary, excerpts_excerpttype.backward_compat, excerpts_excerpttype.print_recipient, excerpts_excerpttype.print_directly, excerpts_excerpttype.shortcut, excerpts_excerpttype.name_de, excerpts_excerpttype.name_fr FROM excerpts_excerpttype ORDER BY excerpts_excerpttype.id ASC
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ...
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ...


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
lino_noi.lib.tickets.models.Ticket.created_natural
lino_noi.lib.tickets.models.Ticket.mobile_item
lino_noi.lib.tickets.models.Ticket.overview
lino_noi.lib.tickets.models.Ticket.workflow_buttons
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

    

