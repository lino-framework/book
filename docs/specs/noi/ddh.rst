.. _noi.specs.ddh:

=============================
Preventing accidental deletes
=============================

.. How to test only this document:

    $ python setup.py test -s tests.SpecsTests.test_ddh
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *


Foreign Keys and their `on_delete` setting
==========================================

Here is the output of :meth:`lino.utils.diag.Analyzer.show_foreign_keys` in
Lino Noi:


>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_foreign_keys())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- blogs.EntryType :
  - PROTECT : blogs.Entry.entry_type
- cal.Calendar :
  - PROTECT : cal.Subscription.calendar, system.SiteConfig.site_calendar
- cal.Event :
  - CASCADE : cal.Guest.event
- cal.EventType :
  - PROTECT : cal.Event.event_type, cal.EventPolicy.event_type, cal.RecurrentEvent.event_type, system.SiteConfig.default_event_type, users.User.event_type
- cal.GuestRole :
  - PROTECT : cal.Guest.role
- cal.Priority :
  - PROTECT : cal.Event.priority
- cal.Room :
  - PROTECT : cal.Event.room, meetings.Meeting.room, tickets.Ticket.site
- clocking.SessionType :
  - PROTECT : clocking.Session.session_type
- comments.Comment :
  - PROTECT : comments.Comment.reply_to
- comments.CommentType :
  - PROTECT : comments.Comment.comment_type
- contacts.Company :
  - PROTECT : cal.Event.company, cal.Room.company, clocking.ServiceReport.company, contacts.Role.company, excerpts.Excerpt.company, system.SiteConfig.site_company, tickets.Project.company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr, faculties.Competence.end_user
  - PROTECT : cal.Guest.partner, clocking.ServiceReport.interesting_for, lists.Member.partner, tickets.Ticket.end_user, topics.Interest.partner
- contacts.Person :
  - CASCADE : users.User.person_ptr
  - PROTECT : cal.Event.contact_person, cal.Room.contact_person, clocking.ServiceReport.contact_person, contacts.Role.person, excerpts.Excerpt.contact_person, tickets.Project.contact_person
- contacts.RoleType :
  - PROTECT : cal.Event.contact_role, cal.Room.contact_role, clocking.ServiceReport.contact_role, contacts.Role.type, excerpts.Excerpt.contact_role, tickets.Project.contact_role
- contenttypes.ContentType :
  - PROTECT : blogs.Entry.owner_type, cal.Event.owner_type, cal.Task.owner_type, changes.Change.master_type, changes.Change.object_type, comments.Comment.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, notify.Message.owner_type, stars.Star.owner_type, topics.Interest.owner_type, uploads.Upload.owner_type
- countries.Country :
  - PROTECT : contacts.Partner.country, countries.Place.country
- countries.Place :
  - PROTECT : contacts.Partner.city, contacts.Partner.region, countries.Place.parent
- django_mailbox.Mailbox :
  - PROTECT : django_mailbox.Message.mailbox
- django_mailbox.Message :
  - PROTECT : django_mailbox.Message.in_reply_to, django_mailbox.MessageAttachment.message
- excerpts.Excerpt :
  - SET_NULL : clocking.ServiceReport.printed_by
- excerpts.ExcerptType :
  - PROTECT : excerpts.Excerpt.excerpt_type
- faculties.Faculty :
  - PROTECT : clocking.Session.faculty, faculties.Competence.faculty, faculties.Demand.skill, faculties.Faculty.parent
- faculties.SkillType :
  - PROTECT : faculties.Faculty.skill_type
- lists.List :
  - PROTECT : lists.Member.list
- lists.ListType :
  - PROTECT : lists.List.list_type
- meetings.Meeting :
  - PROTECT : deploy.Deployment.deferred_to, deploy.Deployment.milestone, tickets.Ticket.fixed_for, tickets.Ticket.reported_for
- tickets.Project :
  - PROTECT : tickets.Project.parent, tickets.Ticket.project
- tickets.ProjectType :
  - PROTECT : tickets.Project.type
- tickets.Ticket :
  - CASCADE : faculties.Demand.demander
  - PROTECT : clocking.Session.ticket, deploy.Deployment.ticket, django_mailbox.Message.ticket, tickets.Link.child, tickets.Link.parent, tickets.Ticket.duplicate_of
- tickets.TicketType :
  - PROTECT : tickets.Ticket.ticket_type
- topics.Topic :
  - PROTECT : tickets.Ticket.topic, topics.Interest.topic
- topics.TopicGroup :
  - PROTECT : topics.Topic.topic_group
- uploads.UploadType :
  - PROTECT : uploads.Upload.type
- users.User :
  - CASCADE : faculties.Competence.user
  - PROTECT : blogs.Entry.user, cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, changes.Change.user, clocking.ServiceReport.user, clocking.Session.user, comments.Comment.user, dashboard.Widget.user, excerpts.Excerpt.user, meetings.Meeting.user, notify.Message.user, stars.Star.user, tickets.Project.assign_to, tickets.Ticket.assigned_to, tickets.Ticket.reporter, tickets.Ticket.user, tinymce.TextFieldTemplate.user, uploads.Upload.user, users.Authority.authorized, users.Authority.user
<BLANKLINE>
