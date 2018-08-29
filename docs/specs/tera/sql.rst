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
    
>>> import lino
>>> lino.startup('lino_book.projects.lydia.settings.demo')
>>> from lino.api.doctest import *

Startup
=======

During startup there are a few SQL queries:

>>> show_sql_queries()  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +SKIP
SELECT excerpts_excerpttype.id, excerpts_excerpttype.name, excerpts_excerpttype.build_method, excerpts_excerpttype.template, excerpts_excerpttype.attach_to_email, excerpts_excerpttype.email_template, excerpts_excerpttype.certifying, excerpts_excerpttype.remark, excerpts_excerpttype.body_template, excerpts_excerpttype.content_type_id, excerpts_excerpttype.primary, excerpts_excerpttype.backward_compat, excerpts_excerpttype.print_recipient, excerpts_excerpttype.print_directly, excerpts_excerpttype.shortcut, excerpts_excerpttype.name_de, excerpts_excerpttype.name_fr FROM excerpts_excerpttype
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 16
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 69
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 69
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 58
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 65
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 67
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 68
SELECT django_content_type.id, django_content_type.app_label, django_content_type.model FROM django_content_type WHERE django_content_type.id = 52

.. _specs.tera.sql.AccountingReport:

AccountingReport
================

Now we do a single request to :class:`AccountingReport
<lino_xl.lib.ledger.AccountingReport>` and look at the SQL that Lino
emits.

To understand the following, you should also look at the source code
(of the :class:`AccountsBalance <lino_xl.lib.ledger.AccountingReport>`
class in :mod:`lino_xl.lib.ledger`) and read the Django documentation
about `Using aggregates within a Subquery expression
<https://docs.djangoproject.com/en/1.11/ref/models/expressions/#using-aggregates-within-a-subquery-expression>`__.

>>> # test_client.force_login(rt.login('robin').user)
>>> url = 'api/ledger/AccountingReport/-99998'
>>> url += "?fmt=json&pv=1&pv=3&pv=true&pv=true&pv=true&pv=true&pv=true&pv=true&pv=true&pv=true&pv=true"
>>> r = demo_get('robin', url)

>>> show_sql_summary()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
========================= =======
 table                     count
------------------------- -------
 django_session            1
 ledger_account          4
 ledger_accountingperiod   9
 users_user                1
========================= =======
<BLANKLINE>

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
