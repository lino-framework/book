.. _specs.tera.sql:

===================================
Exploring SQL activity in Lino Tera
===================================

..  How to test only this document:
    $ doctest docs/specs/tera/sql.rst

This document explores why AccountingReport is slow.
It is also a demo of
the :func:`show_sql_queries <lino.api.doctest.show_sql_queries>`
function.

We use the :mod:`lino_book.projects.lydia` demo database.
    
>>> import lino
>>> lino.startup('lino_book.projects.lydia.settings.demo')
>>> from lino.api.doctest import *

During startup there are a few SQL queries:

>>> show_sql_queries()  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
SELECT "excerpts_excerpttype"."id", "excerpts_excerpttype"."name", "excerpts_excerpttype"."build_method", "excerpts_excerpttype"."template", "excerpts_excerpttype"."attach_to_email", "excerpts_excerpttype"."email_template", "excerpts_excerpttype"."certifying", "excerpts_excerpttype"."remark", "excerpts_excerpttype"."body_template", "excerpts_excerpttype"."content_type_id", "excerpts_excerpttype"."primary", "excerpts_excerpttype"."backward_compat", "excerpts_excerpttype"."print_recipient", "excerpts_excerpttype"."print_directly", "excerpts_excerpttype"."shortcut", "excerpts_excerpttype"."name_de", "excerpts_excerpttype"."name_fr" FROM "excerpts_excerpttype"
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 16
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 70
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 70
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 59
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 66
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 68
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 69
SELECT "django_content_type"."id", "django_content_type"."app_label", "django_content_type"."model" FROM "django_content_type" WHERE "django_content_type"."id" = 53


Now we do a single request and look at the SQL that Lino emits 
in order to build the response . 

>>> # test_client.force_login(rt.login('robin').user)
>>> url = 'api/ledger/AccountingReport/-99998'
>>> url += "?fmt=json&pv=1&pv=3&pv=true&pv=true&pv=true&pv=true&pv=true&pv=true&pv=true&pv=true"
>>> r = demo_get('robin', url)

>>> show_sql_queries()
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF -SKIP
SELECT ... FROM "django_session" ...
SELECT ... FROM "users_user" WHERE "users_user"."id" = 1
SELECT ... FROM "ledger_accountingperiod" WHERE "ledger_accountingperiod"."id" = 1
SELECT ... FROM "ledger_accountingperiod" WHERE "ledger_accountingperiod"."id" = 3
SELECT ... GROUP BY V0."account_id") = '0') ORDER BY "accounts_group"."ref" ASC, "accounts_account"."ref" ASC
SELECT ... FROM "system_siteconfig" WHERE "system_siteconfig"."id" = 1
SELECT ... FROM "accounts_account" WHERE "accounts_account"."id" = 1
SELECT ... GROUP BY V0."partner_id") = '0') ORDER BY "contacts_partner"."name" ASC, "contacts_partner"."id" ASC
SELECT ... FROM "accounts_account" WHERE "accounts_account"."id" = 2
SELECT ... GROUP BY V0."partner_id") = '0') ORDER BY "contacts_partner"."name" ASC, "contacts_partner"."id" ASC
SELECT ... FROM "users_user" WHERE "users_user"."username" = 'robin'
