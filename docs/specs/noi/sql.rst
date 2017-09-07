.. _specs.noi.sql:

=============================
Exploring SQL activity
=============================

This document shows why Jane is so slow when displaying tickets.
It is also a demo of
the :func:`show_sql_queries <lino.api.doctest.show_sql_queries>`
function.

How to test only this document::

    $ doctest docs/specs/noi/sql.rst

We use the :mod:`lino_book.projects.team` demo database.
    
>>> import lino
>>> lino.startup('lino_book.projects.team.settings.demo')
>>> from lino.api.doctest import *

During startup there were two SQL queries:

>>> show_sql_queries()  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
SELECT "excerpts_excerpttype"."id", "excerpts_excerpttype"."name",
    "excerpts_excerpttype"."build_method",
    "excerpts_excerpttype"."template",
    "excerpts_excerpttype"."attach_to_email",
    "excerpts_excerpttype"."email_template",
    "excerpts_excerpttype"."certifying", "excerpts_excerpttype"."remark",
    "excerpts_excerpttype"."body_template",
    "excerpts_excerpttype"."content_type_id",
    "excerpts_excerpttype"."primary",
    "excerpts_excerpttype"."backward_compat",
    "excerpts_excerpttype"."print_recipient",
    "excerpts_excerpttype"."print_directly",
    "excerpts_excerpttype"."shortcut", "excerpts_excerpttype"."name_de",
    "excerpts_excerpttype"."name_fr" FROM "excerpts_excerpttype"
SELECT "django_content_type"."id", "django_content_type"."app_label",
    "django_content_type"."model" FROM "django_content_type" WHERE
    "django_content_type"."id" = 46

Now we do a single request to :class:`AllTickets`, with `limit=1` so
that it retrieves only one row. Now look at all the SQL that poor
Django must do in order to return a single row. And keep in mind that
every row causes a similar set of SQL queries.

>>> r = demo_get('robin','api/tickets/AllTickets', fmt='json', limit=1)
>>> show_sql_queries()  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
SELECT "django_session"."session_key",
    "django_session"."session_data", "django_session"."expire_date" FROM
    "django_session" WHERE ("django_session"."session_key" =
    '...' AND "django_session"."expire_date"
    > '...')
SELECT "contacts_partner"."id", "contacts_partner"."email",
    "contacts_partner"."language", "contacts_partner"."url",
    "contacts_partner"."phone", "contacts_partner"."gsm",
    "contacts_partner"."fax", "contacts_partner"."country_id",
    "contacts_partner"."city_id", "contacts_partner"."zip_code",
    "contacts_partner"."region_id", "contacts_partner"."addr1",
    "contacts_partner"."street_prefix", "contacts_partner"."street",
    "contacts_partner"."street_no", "contacts_partner"."street_box",
    "contacts_partner"."addr2", "contacts_partner"."prefix",
    "contacts_partner"."name", "contacts_partner"."remarks",
    "contacts_person"."partner_ptr_id", "contacts_person"."title",
    "contacts_person"."first_name", "contacts_person"."middle_name",
    "contacts_person"."last_name", "contacts_person"."gender",
    "contacts_person"."birth_date", "users_user"."person_ptr_id",
    "users_user"."modified", "users_user"."created",
    "users_user"."password", "users_user"."last_login",
    "users_user"."timezone", "users_user"."username",
    "users_user"."user_type", "users_user"."initials",
    "users_user"."callme_mode", "users_user"."verification_code",
    "users_user"."user_state", "users_user"."access_class",
    "users_user"."event_type_id",
    "users_user"."open_session_on_new_ticket",
    "users_user"."notify_myself", "users_user"."mail_mode",
    "users_user"."github_username" FROM "users_user" INNER JOIN
    "contacts_person" ON ("users_user"."person_ptr_id" =
    "contacts_person"."partner_ptr_id") INNER JOIN "contacts_partner" ON
    ("contacts_person"."partner_ptr_id" = "contacts_partner"."id") WHERE
    "users_user"."person_ptr_id" = '100'
SELECT "tickets_ticket"."id", "tickets_ticket"."modified",
    "tickets_ticket"."created", "tickets_ticket"."ref",
    "tickets_ticket"."user_id", "tickets_ticket"."assigned_to_id",
    "tickets_ticket"."private", "tickets_ticket"."priority",
    "tickets_ticket"."closed", "tickets_ticket"."planned_time",
    "tickets_ticket"."project_id", "tickets_ticket"."site_id",
    "tickets_ticket"."topic_id", "tickets_ticket"."summary",
    "tickets_ticket"."description", "tickets_ticket"."upgrade_notes",
    "tickets_ticket"."ticket_type_id", "tickets_ticket"."duplicate_of_id",
    "tickets_ticket"."end_user_id", "tickets_ticket"."state",
    "tickets_ticket"."deadline", "tickets_ticket"."reported_for_id",
    "tickets_ticket"."fixed_for_id", "tickets_ticket"."reporter_id",
    "tickets_ticket"."waiting_for", "tickets_ticket"."feedback",
    "tickets_ticket"."standby" FROM "tickets_ticket" ORDER BY
    "tickets_ticket"."id" DESC LIMIT 1
SELECT "contacts_partner"."id", "contacts_partner"."email",
    "contacts_partner"."language", "contacts_partner"."url",
    "contacts_partner"."phone", "contacts_partner"."gsm",
    "contacts_partner"."fax", "contacts_partner"."country_id",
    "contacts_partner"."city_id", "contacts_partner"."zip_code",
    "contacts_partner"."region_id", "contacts_partner"."addr1",
    "contacts_partner"."street_prefix", "contacts_partner"."street",
    "contacts_partner"."street_no", "contacts_partner"."street_box",
    "contacts_partner"."addr2", "contacts_partner"."prefix",
    "contacts_partner"."name", "contacts_partner"."remarks",
    "contacts_person"."partner_ptr_id", "contacts_person"."title",
    "contacts_person"."first_name", "contacts_person"."middle_name",
    "contacts_person"."last_name", "contacts_person"."gender",
    "contacts_person"."birth_date", "users_user"."person_ptr_id",
    "users_user"."modified", "users_user"."created",
    "users_user"."password", "users_user"."last_login",
    "users_user"."timezone", "users_user"."username",
    "users_user"."user_type", "users_user"."initials",
    "users_user"."callme_mode", "users_user"."verification_code",
    "users_user"."user_state", "users_user"."access_class",
    "users_user"."event_type_id",
    "users_user"."open_session_on_new_ticket",
    "users_user"."notify_myself", "users_user"."mail_mode",
    "users_user"."github_username" FROM "users_user" INNER JOIN
    "contacts_person" ON ("users_user"."person_ptr_id" =
    "contacts_person"."partner_ptr_id") INNER JOIN "contacts_partner" ON
    ("contacts_person"."partner_ptr_id" = "contacts_partner"."id") WHERE
    "users_user"."person_ptr_id" = 104
SELECT "topics_topic"."id", "topics_topic"."ref",
    "topics_topic"."name", "topics_topic"."description",
    "topics_topic"."topic_group_id", "topics_topic"."description_de",
    "topics_topic"."description_fr", "topics_topic"."name_de",
    "topics_topic"."name_fr" FROM "topics_topic" WHERE "topics_topic"."id"
    = 1
SELECT COUNT(*) AS "__count" FROM "clocking_session" WHERE
    ("clocking_session"."ticket_id" = 116 AND
    "clocking_session"."end_time" IS NULL AND "clocking_session"."user_id"
    = 100)
SELECT COUNT(*) AS "__count" FROM "clocking_session" WHERE
    ("clocking_session"."ticket_id" = 116 AND
    "clocking_session"."end_time" IS NULL AND "clocking_session"."user_id"
    = 100)
SELECT "django_content_type"."id", "django_content_type"."app_label",
    "django_content_type"."model" FROM "django_content_type" WHERE
    ("django_content_type"."model" = 'ticket' AND
    "django_content_type"."app_label" = 'tickets')
SELECT COUNT(*) AS "__count" FROM "stars_star" WHERE
    ("stars_star"."owner_type_id" = 39 AND "stars_star"."owner_id" = 116
    AND "stars_star"."user_id" = 100 AND "stars_star"."master_id" IS NULL)
SELECT COUNT(*) AS "__count" FROM "stars_star" WHERE
    ("stars_star"."owner_type_id" = 39 AND "stars_star"."owner_id" = 116
    AND "stars_star"."user_id" = 100 AND "stars_star"."master_id" IS NULL)
SELECT COUNT(*) AS "__count" FROM "stars_star" WHERE
    ("stars_star"."owner_type_id" = 39 AND "stars_star"."user_id" = 100
    AND "stars_star"."owner_id" = 116)
SELECT COUNT(*) AS "__count" FROM "stars_star" WHERE
    ("stars_star"."owner_type_id" = 39 AND "stars_star"."user_id" = 100
    AND "stars_star"."owner_id" = 116)
SELECT "tickets_project"."id", "tickets_project"."ref",
    "tickets_project"."parent_id", "tickets_project"."start_date",
    "tickets_project"."end_date", "tickets_project"."company_id",
    "tickets_project"."contact_person_id",
    "tickets_project"."contact_role_id", "tickets_project"."private",
    "tickets_project"."closed", "tickets_project"."planned_time",
    "tickets_project"."name", "tickets_project"."assign_to_id",
    "tickets_project"."type_id", "tickets_project"."description",
    "tickets_project"."srcref_url_template",
    "tickets_project"."changeset_url_template",
    "tickets_project"."reporting_type" FROM "tickets_project" WHERE
    "tickets_project"."id" = 4
SELECT "contacts_partner"."id", "contacts_partner"."email",
    "contacts_partner"."language", "contacts_partner"."url",
    "contacts_partner"."phone", "contacts_partner"."gsm",
    "contacts_partner"."fax", "contacts_partner"."country_id",
    "contacts_partner"."city_id", "contacts_partner"."zip_code",
    "contacts_partner"."region_id", "contacts_partner"."addr1",
    "contacts_partner"."street_prefix", "contacts_partner"."street",
    "contacts_partner"."street_no", "contacts_partner"."street_box",
    "contacts_partner"."addr2", "contacts_partner"."prefix",
    "contacts_partner"."name", "contacts_partner"."remarks",
    "contacts_person"."partner_ptr_id", "contacts_person"."title",
    "contacts_person"."first_name", "contacts_person"."middle_name",
    "contacts_person"."last_name", "contacts_person"."gender",
    "contacts_person"."birth_date", "users_user"."person_ptr_id",
    "users_user"."modified", "users_user"."created",
    "users_user"."password", "users_user"."last_login",
    "users_user"."timezone", "users_user"."username",
    "users_user"."user_type", "users_user"."initials",
    "users_user"."callme_mode", "users_user"."verification_code",
    "users_user"."user_state", "users_user"."access_class",
    "users_user"."event_type_id",
    "users_user"."open_session_on_new_ticket",
    "users_user"."notify_myself", "users_user"."mail_mode",
    "users_user"."github_username" FROM "users_user" INNER JOIN
    "contacts_person" ON ("users_user"."person_ptr_id" =
    "contacts_person"."partner_ptr_id") INNER JOIN "contacts_partner" ON
    ("contacts_person"."partner_ptr_id" = "contacts_partner"."id") WHERE
    "users_user"."person_ptr_id" = 104
SELECT "tickets_tickettype"."id", "tickets_tickettype"."name",
    "tickets_tickettype"."name_de", "tickets_tickettype"."name_fr" FROM
    "tickets_tickettype" WHERE "tickets_tickettype"."id" = 2
SELECT "faculties_demand"."id", "faculties_demand"."skill_id",
    "faculties_demand"."demander_id", "faculties_demand"."importance" FROM
    "faculties_demand" WHERE "faculties_demand"."demander_id" = 116
SELECT "faculties_faculty"."id", "faculties_faculty"."seqno",
    "faculties_faculty"."parent_id", "faculties_faculty"."name",
    "faculties_faculty"."affinity", "faculties_faculty"."skill_type_id",
    "faculties_faculty"."remarks", "faculties_faculty"."name_de",
    "faculties_faculty"."name_fr" FROM "faculties_faculty" WHERE
    "faculties_faculty"."id" = 2
SELECT "faculties_faculty"."id", "faculties_faculty"."seqno",
    "faculties_faculty"."parent_id", "faculties_faculty"."name",
    "faculties_faculty"."affinity", "faculties_faculty"."skill_type_id",
    "faculties_faculty"."remarks", "faculties_faculty"."name_de",
    "faculties_faculty"."name_fr" FROM "faculties_faculty" WHERE
    "faculties_faculty"."id" = 5
SELECT "faculties_demand"."id", "faculties_demand"."skill_id",
    "faculties_demand"."demander_id", "faculties_demand"."importance" FROM
    "faculties_demand" WHERE "faculties_demand"."demander_id" = 116
SELECT "faculties_faculty"."id", "faculties_faculty"."seqno",
    "faculties_faculty"."parent_id", "faculties_faculty"."name",
    "faculties_faculty"."affinity", "faculties_faculty"."skill_type_id",
    "faculties_faculty"."remarks", "faculties_faculty"."name_de",
    "faculties_faculty"."name_fr" FROM "faculties_faculty" WHERE
    "faculties_faculty"."id" = 2
SELECT "faculties_faculty"."id", "faculties_faculty"."seqno",
    "faculties_faculty"."parent_id", "faculties_faculty"."name",
    "faculties_faculty"."affinity", "faculties_faculty"."skill_type_id",
    "faculties_faculty"."remarks", "faculties_faculty"."name_de",
    "faculties_faculty"."name_fr" FROM "faculties_faculty" WHERE
    "faculties_faculty"."id" = 5
SELECT "faculties_competence"."id", "faculties_competence"."seqno",
    "faculties_competence"."user_id", "faculties_competence"."faculty_id",
    "faculties_competence"."end_user_id",
    "faculties_competence"."affinity",
    "faculties_competence"."description" FROM "faculties_competence" WHERE
    "faculties_competence"."faculty_id" IN (2, 5)
SELECT "contacts_partner"."id", "contacts_partner"."email",
    "contacts_partner"."language", "contacts_partner"."url",
    "contacts_partner"."phone", "contacts_partner"."gsm",
    "contacts_partner"."fax", "contacts_partner"."country_id",
    "contacts_partner"."city_id", "contacts_partner"."zip_code",
    "contacts_partner"."region_id", "contacts_partner"."addr1",
    "contacts_partner"."street_prefix", "contacts_partner"."street",
    "contacts_partner"."street_no", "contacts_partner"."street_box",
    "contacts_partner"."addr2", "contacts_partner"."prefix",
    "contacts_partner"."name", "contacts_partner"."remarks" FROM
    "contacts_partner" WHERE "contacts_partner"."id" = 105
SELECT "contacts_partner"."id", "contacts_partner"."email",
    "contacts_partner"."language", "contacts_partner"."url",
    "contacts_partner"."phone", "contacts_partner"."gsm",
    "contacts_partner"."fax", "contacts_partner"."country_id",
    "contacts_partner"."city_id", "contacts_partner"."zip_code",
    "contacts_partner"."region_id", "contacts_partner"."addr1",
    "contacts_partner"."street_prefix", "contacts_partner"."street",
    "contacts_partner"."street_no", "contacts_partner"."street_box",
    "contacts_partner"."addr2", "contacts_partner"."prefix",
    "contacts_partner"."name", "contacts_partner"."remarks" FROM
    "contacts_partner" WHERE "contacts_partner"."id" = 100
SELECT COUNT(*) AS "__count" FROM "tickets_ticket"
SELECT "contacts_partner"."id", "contacts_partner"."email",
    "contacts_partner"."language", "contacts_partner"."url",
    "contacts_partner"."phone", "contacts_partner"."gsm",
    "contacts_partner"."fax", "contacts_partner"."country_id",
    "contacts_partner"."city_id", "contacts_partner"."zip_code",
    "contacts_partner"."region_id", "contacts_partner"."addr1",
    "contacts_partner"."street_prefix", "contacts_partner"."street",
    "contacts_partner"."street_no", "contacts_partner"."street_box",
    "contacts_partner"."addr2", "contacts_partner"."prefix",
    "contacts_partner"."name", "contacts_partner"."remarks",
    "contacts_person"."partner_ptr_id", "contacts_person"."title",
    "contacts_person"."first_name", "contacts_person"."middle_name",
    "contacts_person"."last_name", "contacts_person"."gender",
    "contacts_person"."birth_date", "users_user"."person_ptr_id",
    "users_user"."modified", "users_user"."created",
    "users_user"."password", "users_user"."last_login",
    "users_user"."timezone", "users_user"."username",
    "users_user"."user_type", "users_user"."initials",
    "users_user"."callme_mode", "users_user"."verification_code",
    "users_user"."user_state", "users_user"."access_class",
    "users_user"."event_type_id",
    "users_user"."open_session_on_new_ticket",
    "users_user"."notify_myself", "users_user"."mail_mode",
    "users_user"."github_username" FROM "users_user" INNER JOIN
    "contacts_person" ON ("users_user"."person_ptr_id" =
    "contacts_person"."partner_ptr_id") INNER JOIN "contacts_partner" ON
    ("contacts_person"."partner_ptr_id" = "contacts_partner"."id") WHERE
    "users_user"."username" = 'robin'


