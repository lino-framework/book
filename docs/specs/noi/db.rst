.. doctest docs/specs/noi/db.rst
.. _noi.specs.db:

===========================
Lino Noi database structure
===========================

This document describes the database structure.


.. contents::
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.team.settings.doctests')
>>> from lino.api.doctest import *


Complexity factors
==================

>>> print(analyzer.show_complexity_factors())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 44 plugins
- 64 models
- 21 user roles
- 5 user types
- 236 views
- 16 dialog actions
<BLANKLINE>



Dependencies
============

>>> dd.is_installed('products')
False

>>> dd.plugins.tickets
lino_noi.lib.tickets (extends_models=['Ticket', 'Site'])

>>> dd.plugins.working
lino_xl.lib.working



The database models
===================


>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
44 apps: lino, staticfiles, about, social_django, jinja, bootstrap3, extjs, printing, system, contenttypes, gfks, office, xl, countries, contacts, users, noi, cal, calview, excerpts, memo, comments, changes, tickets, summaries, checkdata, working, lists, notify, uploads, export_excel, tinymce, smtpd, weasyprint, appypod, dashboard, github, userstats, groups, rest_framework, restful, django_mailbox, mailbox, sessions.
64 models:
================================== ================================ ========= =======
 Name                               Default table                    #fields   #rows
---------------------------------- -------------------------------- --------- -------
 cal.Calendar                       cal.Calendars                    6         1
 cal.Event                          cal.OneEvent                     26        113
 cal.EventPolicy                    cal.EventPolicies                20        6
 cal.EventType                      cal.EventTypes                   23        4
 cal.Guest                          cal.Guests                       6         0
 cal.GuestRole                      cal.GuestRoles                   5         0
 cal.RecurrentEvent                 cal.RecurrentEvents              22        15
 cal.RemoteCalendar                 cal.RemoteCalendars              7         0
 cal.Room                           cal.Rooms                        9         0
 cal.Subscription                   cal.Subscriptions                4         0
 cal.Task                           cal.Tasks                        18        0
 calview.DailyPlannerRow            calview.DailyPlannerRows         7         2
 changes.Change                     changes.Changes                  10        0
 checkdata.Problem                  checkdata.Problems               6         0
 comments.Comment                   comments.Comments                12        168
 comments.CommentType               comments.CommentTypes            4         0
 comments.Mention                   comments.Mentions                7         0
 contacts.Company                   contacts.Companies               22        13
 contacts.CompanyType               contacts.CompanyTypes            7         16
 contacts.Partner                   contacts.Partners                20        89
 contacts.Person                    contacts.Persons                 27        76
 contacts.Role                      contacts.Roles                   4         5
 contacts.RoleType                  contacts.RoleTypes               5         5
 contenttypes.ContentType           gfks.ContentTypes                3         64
 countries.Country                  countries.Countries              6         8
 countries.Place                    countries.Places                 9         78
 dashboard.Widget                   dashboard.Widgets                5         0
 django_mailbox.Mailbox             mailbox.Mailboxes                6         1
 django_mailbox.Message             mailbox.Messages                 15        7
 django_mailbox.MessageAttachment   mailbox.MessageAttachments       4         1
 excerpts.Excerpt                   excerpts.Excerpts                11        2
 excerpts.ExcerptType               excerpts.ExcerptTypes            17        2
 gfks.HelpText                      gfks.HelpTexts                   4         2
 github.Commit                      github.Commits                   14        0
 github.Repository                  github.Repositories              4         0
 groups.Group                       groups.Groups                    7         3
 groups.Membership                  groups.Memberships               4         7
 lists.List                         lists.Lists                      7         8
 lists.ListType                     lists.ListTypes                  4         3
 lists.Member                       lists.Members                    5         89
 notify.Message                     notify.Messages                  11        7
 sessions.Session                   sessions.SessionTable            3         ...
 social_django.Association          social_django.AssociationTable   7         0
 social_django.Code                 social_django.CodeTable          5         0
 social_django.Nonce                social_django.NonceTable         4         0
 social_django.Partial              social_django.PartialTable       6         0
 social_django.UserSocialAuth       users.SocialAuths                5         0
 system.SiteConfig                  system.SiteConfigs               9         1
 tickets.Link                       tickets.Links                    4         1
 tickets.Site                       tickets.Sites                    16        5
 tickets.Ticket                     tickets.Tickets                  28        116
 tickets.TicketType                 tickets.TicketTypes              5         3
 tinymce.TextFieldTemplate          tinymce.TextFieldTemplates       5         2
 uploads.Upload                     uploads.Uploads                  11        0
 uploads.UploadType                 uploads.UploadTypes              8         0
 uploads.Volume                     uploads.Volumes                  5         0
 users.Authority                    users.Authorities                3         0
 users.User                         users.AllUsers                   47        7
 userstats.UserStat                 userstats.UserStats              4         36
 working.ServiceReport              working.ServiceReports           10        1
 working.Session                    working.Sessions                 14        13
 working.SessionType                working.SessionTypes             4         1
 working.SiteSummary                working.SiteSummaries            9         15
 working.UserSummary                working.UserSummaries            7         252
================================== ================================ ========= =======
<BLANKLINE>
