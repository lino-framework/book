.. doctest docs/specs/tera/sql.rst
.. _specs.tera.sql:

===================================
Exploring SQL activity in Lino Tera
===================================

This document explores some SQL requests in Lino Tera.
It is also a demo of
the :func:`show_sql_queries <lino.api.doctest.show_sql_queries>`
function.

We use the :mod:`lino_book.projects.lydia` demo database.

>>> from lino import startup
>>> startup('lino_book.projects.lydia.settings.demo')
>>> from lino.api.doctest import *

Startup
=======

During startup there are a few SQL queries caused by
:func:`lino_xl.lib.excerpts.models.set_excerpts_actions`, which is called during
startup as a :data:`lino.core.signals.pre_analyze` handler:

>>> show_sql_queries()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
SELECT excerpts_excerpttype.id, excerpts_excerpttype.name, excerpts_excerpttype.build_method,
  excerpts_excerpttype.template, excerpts_excerpttype.attach_to_email,
  excerpts_excerpttype.email_template, excerpts_excerpttype.certifying,
  excerpts_excerpttype.remark, excerpts_excerpttype.body_template,
  excerpts_excerpttype.content_type_id, excerpts_excerpttype.primary,
  excerpts_excerpttype.backward_compat, excerpts_excerpttype.print_recipient,
  excerpts_excerpttype.print_directly, excerpts_excerpttype.shortcut,
  excerpts_excerpttype.name_de, excerpts_excerpttype.name_fr FROM excerpts_excerpttype
ORDER BY excerpts_excerpttype.id ASC
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = ... LIMIT 21

TODO: explain why `django_content_type.id` is not always the same.

>>> reset_sql_queries()

.. _specs.tera.sql.AccountingReport:


Now we run some action and look at the SQL queries resulting from it.

We run the :meth:`run_update_plan` action of an accounting report
(:class:`sheets.Report <lino_xl.lib.sheets.Report>`).  You might want
to read the Django documentation about `Using aggregates within a
Subquery expression
<https://docs.djangoproject.com/en/3.1/ref/models/expressions/#using-aggregates-within-a-subquery-expression>`__.

>>> ses = rt.login("robin")
>>> obj = rt.models.sheets.Report.objects.get(pk=1)

>>> reset_sql_queries()
>>> obj.run_update_plan(ses)
>>> show_sql_summary()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
========================= =========== =======
 table                     stmt_type   count
------------------------- ----------- -------
                           INSERT      99
                           UNKNOWN     4
 ana_account               SELECT      22
 cal_event                 SELECT      99
 cal_task                  SELECT      99
 checkdata_problem         SELECT      99
 contacts_partner          SELECT      53
 django_content_type       SELECT      13
 excerpts_excerpt          SELECT      99
 invoicing_item            SELECT      99
 ledger_account            SELECT      25
 ledger_accountingperiod   SELECT      2
 notes_note                SELECT      99
 sales_invoiceitem         SELECT      99
 sheets_accountentry       DELETE      1
 sheets_accountentry       SELECT      7
 sheets_anaaccountentry    DELETE      1
 sheets_anaaccountentry    SELECT      6
 sheets_item               SELECT      17
 sheets_itementry          DELETE      1
 sheets_itementry          SELECT      9
 sheets_partnerentry       DELETE      1
 sheets_partnerentry       SELECT      1
 sheets_report             SELECT      99
 topics_interest           SELECT      99
 uploads_upload            SELECT      99
========================= =========== =======
<BLANKLINE>


TODO: above output shows some bug with parsing the statements, and
then we must explain why there are so many select statements in
unrelated tables (e.g. notes_note).

Here is an untested simplified log of the full SQL queries:

>>> show_sql_queries()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP
SELECT ... FROM django_session WHERE (...)
SELECT users_user.id, ... FROM users_user WHERE users_user.id = 1
SELECT ... FROM ledger_accountingperiod WHERE ledger_accountingperiod.id = 1
SELECT ... FROM ledger_accountingperiod WHERE ledger_accountingperiod.id = 3
SELECT accounts_account.id, ...,
  (SELECT CAST(SUM(V0.amount) AS NUMERIC) AS total FROM ledger_movement V0
    INNER JOIN ledger_voucher V2 ON (V0.voucher_id = V2.id)
      WHERE (V0.account_id = (accounts_account.id)
        AND V2.accounting_period_id IN (SELECT U0.id AS Col1 FROM ledger_accountingperiod U0 WHERE U0.ref < '2015-01')
        AND V0.dc = 0)
        GROUP BY V0.account_id)
   AS old_c,
   (SELECT ...) AS during_d,
   (SELECT ...) AS during_c,
   (SELECT ...) AS old_d
   FROM accounts_account
     LEFT OUTER JOIN accounts_group ON (accounts_account.group_id = accounts_group.id)
       WHERE NOT ((SELECT CAST(SUM(V0.amount) AS NUMERIC) AS total FROM ledger_movement V0
         INNER JOIN ledger_voucher V2 ON (V0.voucher_id = V2.id)
         WHERE (V0.account_id = (accounts_account.id)
           AND V2.accounting_period_id IN (SELECT U0.id AS Col1 FROM ledger_accountingperiod U0 WHERE U0.ref < '2015-01')
           AND V0.dc = 0)
           GROUP BY V0.account_id) = '0'
       AND (...) = '0' AND (... = '0' AND (...) = '0')
   ORDER BY accounts_group.ref ASC, accounts_account.ref ASC
SELECT ... FROM system_siteconfig WHERE system_siteconfig.id = 1
SELECT ... FROM accounts_account WHERE accounts_account.id = 1
SELECT contacts_partner.id, ...,
  (SELECT CAST(SUM(V0.amount) AS NUMERIC) AS total
      FROM ledger_movement V0 INNER JOIN ledger_voucher V3 ON (V0.voucher_id = V3.id)
        WHERE (V0.partner_id = (contacts_partner.id) AND V0.account_id = 1
        AND V3.accounting_period_id IN (...) AND V0.dc = 0)
        GROUP BY V0.partner_id) AS old_c,
  (SELECT ...) AS during_d,
  (SELECT ...) AS during_c,
  (SELECT ...) AS old_d
  FROM contacts_partner
  WHERE NOT (...)
  ORDER BY contacts_partner.name ASC, contacts_partner.id ASC
SELECT ... FROM accounts_account WHERE accounts_account.id = 2
SELECT contacts_partner.id, contacts_partner.email, ...
  (SELECT CAST(SUM(V0.amount) AS NUMERIC) AS total
     FROM ledger_movement V0
     INNER JOIN ledger_voucher V3 ON (V0.voucher_id = V3.id)
       WHERE (V0.partner_id = (contacts_partner.id) AND V0.account_id = 2
         AND V3.accounting_period_id IN (...) AND V0.dc = 0)
       GROUP BY V0.partner_id)
    AS old_c,
  (SELECT ...) AS during_c,
  (SELECT ...) AS old_d
  FROM contacts_partner
  WHERE NOT (...)
  ORDER BY contacts_partner.name ASC, contacts_partner.id ASC
SELECT ... FROM users_user WHERE users_user.username = 'robin'
