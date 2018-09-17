.. _lino.coming:
.. _v18.9:

==============
Coming version
==============

We plan to release the following as version 18.9.

Changes since 18.8
==================

New features visible to end-users:

- A new implementation of the Accounting Report.
  :class:`sheets.Report <lino_xl.lib.sheets.Report>` replaces the
  :class:`ledger.AccountingReport
  <lino_xl.lib.ledger.AccountingReport>`.  It now includes subtotals,
  analytic accounts balances, balance sheet and income statement.
  It is no longer a virtual table but
  a :class:`lino.modlib.users.UserPlan`.

- Optimizations in :mod:`lino_xl.lib.cal` :class:`OverdueAppointments
  <lino_xl.lib.cal.OverdueAppointments>` : the default view no longer
  includes today, it stops yesterday.  Because today's appointments
  are shown by :class:`lino_xl.lib.cal.MyAppointmentsToday`.
         
  

Database changes

- Subclasses of :class:`lino.mixins.refs.Referrable` now always have
  `max_length=200`.

Internal changes:

- release tags in 18.8 were missing in the git repo because atelier
  did not yet push them.

- New model mixin :class:`lino.mixins.refs.StructuredReferrable`.
  
- New model mixin :class:`lino.modlib.users.UserPlan`.

- plain html tables now use ``class="text-cell"`` instead of a
  hard-coded set of attributes  ``align="left"``.

- The :meth:`lino.core.renderer.HtmlRenderer.table2story` method now
  yields a sequence of elements instead of returning a single one.  

- We have a new method :meth:`lino.core.requests.BaseRequest.show_story`
  which is used in the template for the report
  (:xfile:`ledger/Report/default.weazy.html`).

- in :mod:`lino.api.doctest`, show_sql_queries and show_sql_summary no
  longer call reset_sql_queries.

- we continued to improve the documentation

- :func:`lino.api.doctest.show_sql_summary` now supports INSERT INTO
  and DELETE FROM statements. It now uses `sqlparse
  <https://sqlparse.readthedocs.io/en/latest/>`__.

  
Warning
=======
  
Make sure to notify us if you run a production site using one of these
applications.  We provide automatic database migration to future
versions only for applications with at least one registered production
site.


