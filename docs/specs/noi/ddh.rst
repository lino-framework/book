.. doctest docs/specs/noi/ddh.rst
.. _noi.specs.ddh:

=============================
Deletion handlers in Lino Noi
=============================

.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.team.settings.demo')
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
  - PROTECT : comments.Comment.reply_to, comments.Mention.comment
- comments.CommentType :
  - PROTECT : comments.Comment.comment_type
- contacts.Company :
  - PROTECT : cal.Event.company, cal.Room.company, contacts.Role.company, excerpts.Excerpt.company, ledger.Journal.partner, system.SiteConfig.site_company, tickets.Site.company, working.ServiceReport.company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr, invoicing.SalesRule.partner
  - PROTECT : invoicing.Item.partner, invoicing.Plan.partner, invoicing.SalesRule.invoice_recipient, ledger.Movement.partner, lists.Member.partner, sales.VatProductInvoice.partner, vat.VatAccountInvoice.partner, working.ServiceReport.interesting_for
- contacts.Person :
  - CASCADE : users.User.person_ptr
  - PROTECT : cal.Event.contact_person, cal.Guest.partner, cal.Room.contact_person, contacts.Role.person, excerpts.Excerpt.contact_person, tickets.Site.contact_person, tickets.Ticket.end_user, working.ServiceReport.contact_person
- contacts.RoleType :
  - PROTECT : cal.Event.contact_role, cal.Room.contact_role, contacts.Role.type, excerpts.Excerpt.contact_role, tickets.Site.contact_role, working.ServiceReport.contact_role
- contenttypes.ContentType :
  - PROTECT : cal.Event.owner_type, cal.Task.owner_type, changes.Change.master_type, changes.Change.object_type, checkdata.Problem.owner_type, comments.Comment.owner_type, comments.Mention.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, invoicing.Item.generator_type, notify.Message.owner_type, sales.InvoiceItem.invoiceable_type, uploads.Upload.owner_type
- countries.Country :
  - PROTECT : contacts.Partner.country, countries.Place.country
- countries.Place :
  - PROTECT : contacts.Partner.city, contacts.Partner.region, countries.Place.parent
- django_mailbox.Mailbox :
  - PROTECT : django_mailbox.Message.mailbox
- django_mailbox.Message :
  - PROTECT : django_mailbox.Message.in_reply_to, django_mailbox.MessageAttachment.message
- excerpts.Excerpt :
  - SET_NULL : sales.VatProductInvoice.printed_by, working.ServiceReport.printed_by
- excerpts.ExcerptType :
  - PROTECT : excerpts.Excerpt.excerpt_type
- github.Repository :
  - PROTECT : github.Commit.repository
- groups.Group :
  - CASCADE : groups.Membership.group
  - PROTECT : tickets.Site.group
- invoicing.Area :
  - PROTECT : invoicing.Plan.area
- invoicing.Plan :
  - PROTECT : invoicing.Item.plan
- invoicing.Tariff :
  - PROTECT : products.Product.tariff
- ledger.Account :
  - PROTECT : ledger.Journal.account, ledger.MatchRule.account, ledger.Movement.account, vat.InvoiceItem.account
- ledger.AccountingPeriod :
  - PROTECT : ledger.Voucher.accounting_period
- ledger.FiscalYear :
  - PROTECT : ledger.AccountingPeriod.year
- ledger.Journal :
  - CASCADE : ledger.MatchRule.journal
  - PROTECT : invoicing.Area.journal, ledger.Voucher.journal
- ledger.PaymentTerm :
  - PROTECT : contacts.Partner.payment_term, sales.VatProductInvoice.payment_term, vat.VatAccountInvoice.payment_term
- ledger.Voucher :
  - CASCADE : ledger.Movement.voucher
  - PROTECT : sales.VatProductInvoice.voucher_ptr, vat.VatAccountInvoice.voucher_ptr
- lists.List :
  - CASCADE : lists.Member.list
- lists.ListType :
  - PROTECT : lists.List.list_type
- products.Product :
  - PROTECT : products.PriceRule.product, sales.InvoiceItem.product
- products.ProductCat :
  - PROTECT : products.Product.cat
- sales.PaperType :
  - PROTECT : invoicing.SalesRule.paper_type, sales.VatProductInvoice.paper_type
- sales.VatProductInvoice :
  - CASCADE : sales.InvoiceItem.voucher
  - SET_NULL : invoicing.Item.invoice
- tickets.Site :
  - CASCADE : working.SiteSummary.master
  - PROTECT : tickets.Ticket.site
- tickets.Ticket :
  - CASCADE : tickets.Link.child, tickets.Link.parent
  - PROTECT : django_mailbox.Message.ticket, github.Commit.ticket, tickets.CheckListItem.ticket, tickets.Ticket.duplicate_of, working.Session.ticket
- tickets.TicketType :
  - PROTECT : tickets.Ticket.ticket_type
- uploads.UploadType :
  - PROTECT : uploads.Upload.type
- uploads.Volume :
  - PROTECT : ledger.Journal.uploads_volume, uploads.Upload.volume
- users.User :
  - CASCADE : groups.Membership.user, ledger.LedgerInfo.user, working.UserSummary.master
  - PROTECT : cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, changes.Change.user, checkdata.Problem.user, comments.Comment.user, comments.Mention.user, dashboard.Widget.user, excerpts.Excerpt.user, github.Commit.user, groups.Group.user, invoicing.Plan.user, ledger.Voucher.user, notify.Message.user, social_django.UserSocialAuth.user, tickets.Ticket.assigned_to, tickets.Ticket.last_commenter, tickets.Ticket.reporter, tickets.Ticket.user, tinymce.TextFieldTemplate.user, uploads.Upload.user, users.Authority.authorized, users.Authority.user, working.ServiceReport.user, working.Session.user
- vat.VatAccountInvoice :
  - CASCADE : vat.InvoiceItem.voucher
- working.SessionType :
  - PROTECT : products.PriceRule.selector, working.Session.session_type
<BLANKLINE>



Deleting
========

>>> d = get_json_dict('robin', "contacts/Persons/167", an='delete_selected', sr=167)
>>> print(d['message'])
Cannot delete Partner Östges Otto because 1 List memberships refer to it.

>>> d = get_json_dict('robin', "lists/Lists/1", an='delete_selected', sr=1)
>>> print(d['message'])
You are about to delete 1 Partner List
(Announcements)
as well as all related volatile records (12 List memberships). Are you sure?
