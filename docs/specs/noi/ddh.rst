.. doctest docs/specs/noi/ddh.rst
.. _noi.specs.ddh:

=============================
Deletion handlers in Lino Noi
=============================

..  doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.team.settings.doctests')
    >>> from lino.api.doctest import *


Here is a list of foreign keys in :ref:`noi` and their on_delete
behaviour. See also :doc:`/dev/delete`.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_foreign_keys())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- cal.Calendar :
  - PROTECT : cal.Subscription.calendar, system.SiteConfig.site_calendar
- cal.Event :
  - CASCADE : cal.Guest.event
- cal.EventType :
  - PROTECT : cal.Event.event_type, cal.EventPolicy.event_type, cal.RecurrentEvent.event_type, system.SiteConfig.default_event_type, users.User.event_type
- cal.GuestRole :
  - PROTECT : cal.Guest.role
- cal.Room :
  - PROTECT : cal.Event.room
- comments.Comment :
  - PROTECT : comments.Comment.reply_to
- comments.CommentType :
  - PROTECT : comments.Comment.comment_type
- contacts.Company :
  - PROTECT : cal.Event.company, cal.Room.company, contacts.Role.company, excerpts.Excerpt.company, system.SiteConfig.site_company, tickets.Site.company, working.ServiceReport.company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr
  - PROTECT : lists.Member.partner, tickets.Ticket.end_user, working.ServiceReport.interesting_for
- contacts.Person :
  - CASCADE : users.User.person_ptr
  - PROTECT : cal.Event.contact_person, cal.Guest.partner, cal.Room.contact_person, contacts.Role.person, excerpts.Excerpt.contact_person, tickets.Site.contact_person, working.ServiceReport.contact_person
- contacts.RoleType :
  - PROTECT : cal.Event.contact_role, cal.Room.contact_role, contacts.Role.type, excerpts.Excerpt.contact_role, tickets.Site.contact_role, working.ServiceReport.contact_role
- contenttypes.ContentType :
  - PROTECT : cal.Event.owner_type, cal.Task.owner_type, changes.Change.master_type, changes.Change.object_type, checkdata.Problem.owner_type, comments.Comment.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, notify.Message.owner_type, uploads.Upload.owner_type
- countries.Country :
  - PROTECT : contacts.Partner.country, countries.Place.country
- countries.Place :
  - PROTECT : contacts.Partner.city, contacts.Partner.region, countries.Place.parent
- django_mailbox.Mailbox :
  - PROTECT : django_mailbox.Message.mailbox
- django_mailbox.Message :
  - PROTECT : django_mailbox.Message.in_reply_to, django_mailbox.MessageAttachment.message
- excerpts.Excerpt :
  - SET_NULL : working.ServiceReport.printed_by
- excerpts.ExcerptType :
  - PROTECT : excerpts.Excerpt.excerpt_type
- github.Repository :
  - PROTECT : github.Commit.repository
- lists.List :
  - PROTECT : lists.Member.list
- lists.ListType :
  - PROTECT : lists.List.list_type
- tickets.Site :
  - CASCADE : tickets.Subscription.site, working.SiteSummary.master
  - PROTECT : tickets.Ticket.site
- tickets.Ticket :
  - PROTECT : django_mailbox.Message.ticket, github.Commit.ticket, tickets.Link.child, tickets.Link.parent, tickets.Ticket.duplicate_of, working.Session.ticket
- tickets.TicketType :
  - PROTECT : tickets.Ticket.ticket_type
- uploads.UploadType :
  - PROTECT : uploads.Upload.type
- uploads.Volume :
  - PROTECT : uploads.Upload.volume
- users.User :
  - CASCADE : tickets.Subscription.user, working.UserSummary.master
  - PROTECT : cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, changes.Change.user, checkdata.Problem.user, comments.Comment.user, dashboard.Widget.user, excerpts.Excerpt.user, github.Commit.user, notify.Message.user, social_django.UserSocialAuth.user, tickets.Ticket.assigned_to, tickets.Ticket.last_commenter, tickets.Ticket.reporter, tickets.Ticket.user, tinymce.TextFieldTemplate.user, uploads.Upload.user, users.Authority.authorized, users.Authority.user, working.ServiceReport.user, working.Session.user
- working.SessionType :
  - PROTECT : working.Session.session_type
<BLANKLINE>
