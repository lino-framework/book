.. doctest docs/specs/noi/db.rst
.. _noi.specs.db:

======================
The database structure
======================

..  doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *

This document describes the database structure.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
43 apps: lino, staticfiles, about, social_django, jinja, bootstrap3, extjs, printing, system, contenttypes, gfks, office, xl, countries, contacts, users, noi, cal, extensible, topics, excerpts, comments, changes, tickets, summaries, working, lists, notify, uploads, export_excel, tinymce, smtpd, weasyprint, appypod, checkdata, dashboard, github, userstats, rest_framework, restful, django_mailbox, mailbox, sessions.
66 models:
================================== ================================ ========= =======
 Name                               Default table                    #fields   #rows
---------------------------------- -------------------------------- --------- -------
 cal.Calendar                       cal.Calendars                    6         1
 cal.DailyPlannerRow                cal.DailyPlannerRows             7         3
 cal.Event                          cal.OneEvent                     26        113
 cal.EventPolicy                    cal.EventPolicies                19        6
 cal.EventType                      cal.EventTypes                   19        3
 cal.Guest                          cal.Guests                       6         0
 cal.GuestRole                      cal.GuestRoles                   4         0
 cal.Priority                       cal.Priorities                   5         4
 cal.RecurrentEvent                 cal.RecurrentEvents              21        15
 cal.RemoteCalendar                 cal.RemoteCalendars              7         0
 cal.Room                           cal.Rooms                        8         0
 cal.Subscription                   cal.Subscriptions                4         0
 cal.Task                           cal.Tasks                        17        0
 changes.Change                     changes.Changes                  10        0
 checkdata.Problem                  checkdata.Problems               6         0
 comments.Comment                   comments.Comments                10        12
 comments.CommentType               comments.CommentTypes            4         0
 contacts.Company                   contacts.Companies               22        5
 contacts.CompanyType               contacts.CompanyTypes            7         16
 contacts.Partner                   contacts.Partners                20        12
 contacts.Person                    contacts.Persons                 27        7
 contacts.Role                      contacts.Roles                   4         0
 contacts.RoleType                  contacts.RoleTypes               4         5
 contenttypes.ContentType           gfks.ContentTypes                3         66
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
 lists.List                         lists.Lists                      7         8
 lists.ListType                     lists.ListTypes                  4         3
 lists.Member                       lists.Members                    5         0
 notify.Message                     notify.Messages                  11        6
 sessions.Session                   sessions.SessionTable            3        ...
 social_django.Association          social_django.AssociationTable   7         0
 social_django.Code                 social_django.CodeTable          5         0
 social_django.Nonce                social_django.NonceTable         4         0
 social_django.Partial              social_django.PartialTable       6         0
 social_django.UserSocialAuth       users.SocialAuths                5         0
 system.SiteConfig                  system.SiteConfigs               9         1
 tickets.Link                       tickets.Links                    4         1
 tickets.Project                    tickets.Projects                 18        0
 tickets.ProjectType                tickets.ProjectTypes             4         0
 tickets.Site                       tickets.Sites                    8         3
 tickets.Subscription               tickets.Subscriptions            4         12
 tickets.Ticket                     tickets.Tickets                  26        116
 tickets.TicketType                 tickets.TicketTypes              5         3
 tinymce.TextFieldTemplate          tinymce.TextFieldTemplates       5         2
 topics.Interest                    topics.Interests                 6         12
 topics.Topic                       topics.Topics                    9         4
 topics.TopicGroup                  topics.TopicGroups               5         0
 uploads.Upload                     uploads.Uploads                  9         0
 uploads.UploadType                 uploads.UploadTypes              8         0
 users.Authority                    users.Authorities                3         0
 users.User                         users.Users                      47        6
 userstats.UserStat                 userstats.UserStats              5         36
 working.ServiceReport              working.ServiceReports           10        1
 working.Session                    working.Sessions                 14        13
 working.SessionType                working.SessionTypes             4         1
 working.SiteSummary                working.Summaries                17        3
================================== ================================ ========= =======
<BLANKLINE>


>>> print(analyzer.show_complexity_factors())
- 43 plugins
- 66 models
- 233 views
- 7 user types
- 70 dialog actions
<BLANKLINE>


