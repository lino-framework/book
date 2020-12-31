.. doctest docs/specs/noi/users.rst
.. _noi.specs.user:

======================================
``users`` (User management in Noi)
======================================

.. currentmodule:: lino_noi.lib.users

The :mod:`lino_noi.lib.users` plugin extends :mod:`lino_xl.lib.online.users` for
Lino Noi.


.. contents::
  :local:

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.noi1e.settings.demo')
>>> from lino.api.doctest import *


Here are the users of the demo site.

>>> rt.show('users.UsersOverview')
========== ===================== ==========
 Username   User type             Language
---------- --------------------- ----------
 jean       400 (Developer)       en
 luc        400 (Developer)       en
 marc       100 (Customer)        en
 mathieu    200 (Contributor)     en
 robin      900 (Administrator)   en
 rolf       900 (Administrator)   de
 romain     900 (Administrator)   fr
========== ===================== ==========
<BLANKLINE>


User types
==========

A :ref:`noi` site has the following user types:

>>> rt.show(users.UserTypes)
======= =============== ===============
 value   name            text
------- --------------- ---------------
 000     anonymous       Anonymous
 100     customer user   Customer
 200     contributor     Contributor
 400     developer       Developer
 900     admin           Administrator
======= =============== ===============
<BLANKLINE>

Note that "Customer" has two internal names.

>>> users.UserTypes.customer is users.UserTypes.user
True


A **customer** is somebody who uses some part of the software being developed by
the team. This is usually the contact person of a customer.

A **contributor** can submit tickets, work on them and discuss with other team
members.  But does not see confidential data.

A **developer** is a trusted contributor who can do almost everything except
managing other users.

Here is a list of user types of those who can work on tickets:

>>> from lino_xl.lib.working.roles import Worker
>>> UserTypes = rt.models.users.UserTypes
>>> [p.name for p in UserTypes.items()
...     if p.has_required_roles([Worker])]
['contributor', 'developer', 'admin']

And here are those who don't work:

>>> [p for p in UserTypes.get_list_items()
...    if not p.has_required_roles([Worker])]
[<users.UserTypes.anonymous:000>, <users.UserTypes.customer:100>]


User roles and permissions
==========================

Here is the :class:`lino.modlib.users.UserRoles` table for :ref:`noi`:

>>> rt.show(users.UserRoles)
================================ ===== ===== ===== ===== =====
 Name                             000   100   200   400   900
-------------------------------- ----- ----- ----- ----- -----
 cal.CalendarReader               ☑
 comments.CommentsReader          ☑     ☑     ☑     ☑     ☑
 comments.CommentsStaff                             ☑     ☑
 comments.CommentsUser                  ☑     ☑     ☑     ☑
 comments.PrivateCommentsReader                     ☑     ☑
 contacts.ContactsStaff                                   ☑
 contacts.ContactsUser                        ☑     ☑     ☑
 core.SiteUser                          ☑     ☑     ☑     ☑
 courses.CoursesUser                          ☑     ☑     ☑
 excerpts.ExcerptsStaff                             ☑     ☑
 excerpts.ExcerptsUser                        ☑     ☑     ☑
 ledger.LedgerStaff                                       ☑
 noi.Anonymous                    ☑
 noi.Contributor                              ☑     ☑     ☑
 noi.Customer                           ☑     ☑     ☑     ☑
 noi.Developer                                      ☑     ☑
 noi.SiteAdmin                                            ☑
 office.OfficeStaff                                       ☑
 office.OfficeUser                      ☑     ☑     ☑     ☑
 products.ProductsStaff                                   ☑
 tickets.Reporter                       ☑     ☑     ☑     ☑
 tickets.Searcher                 ☑     ☑     ☑     ☑     ☑
 tickets.TicketsStaff                               ☑     ☑
 tickets.Triager                                    ☑     ☑
 users.Helper                                 ☑     ☑     ☑
 votes.VotesStaff                                         ☑
 votes.VotesUser                        ☑     ☑     ☑     ☑
 working.Worker                               ☑     ☑     ☑
================================ ===== ===== ===== ===== =====
<BLANKLINE>



Users
=====

The following shows a list of all windows in :ref:`noi`  and who can see them:

>>> print(analyzer.show_window_permissions())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
- about.About.show : visible for all
- cal.Calendars.detail : visible for admin
- cal.Calendars.insert : visible for admin
- cal.EntriesByGuest.insert : visible for customer contributor developer admin
- cal.EventTypes.detail : visible for admin
- cal.EventTypes.insert : visible for admin
- cal.EventTypes.merge_row : visible for admin
- cal.Events.detail : visible for admin
- cal.Events.insert : visible for admin
- cal.GuestRoles.detail : visible for admin
- cal.GuestRoles.merge_row : visible for admin
- cal.Guests.detail : visible for nobody
- cal.Guests.insert : visible for nobody
- cal.RecurrentEvents.detail : visible for admin
- cal.RecurrentEvents.insert : visible for admin
- cal.Rooms.detail : visible for admin
- cal.Rooms.insert : visible for admin
- cal.Tasks.detail : visible for admin
- cal.Tasks.insert : visible for admin
- calview.DailyView.detail : visible for customer contributor developer admin
- calview.MonthlyView.detail : visible for customer contributor developer admin
- calview.WeeklyView.detail : visible for customer contributor developer admin
- changes.Changes.detail : visible for admin
- checkdata.Checkers.detail : visible for admin
- checkdata.Problems.detail : visible for customer contributor developer admin
- comments.CommentTypes.detail : visible for developer admin
- comments.CommentTypes.insert : visible for developer admin
- comments.Comments.detail : visible for customer contributor developer admin
- comments.Comments.insert : visible for customer contributor developer admin
- comments.CommentsByRFC.insert : visible for customer contributor developer admin
- contacts.Companies.detail : visible for contributor developer admin
- contacts.Companies.insert : visible for contributor developer admin
- contacts.Companies.merge_row : visible for admin
- contacts.Partners.merge_row : visible for admin
- contacts.Persons.detail : visible for contributor developer admin
- contacts.Persons.insert : visible for contributor developer admin
- contacts.Persons.merge_row : visible for admin
- countries.Countries.detail : visible for admin
- countries.Countries.insert : visible for admin
- countries.Places.detail : visible for admin
- countries.Places.insert : visible for admin
- excerpts.ExcerptTypes.detail : visible for developer admin
- excerpts.ExcerptTypes.insert : visible for developer admin
- excerpts.Excerpts.detail : visible for contributor developer admin
- gfks.ContentTypes.detail : visible for admin
- github.Commits.detail : visible for customer contributor developer admin
- github.Repositories.detail : visible for developer admin
- github.Repositories.insert : visible for developer admin
- groups.Groups.detail : visible for customer contributor developer admin
- groups.Groups.insert : visible for customer contributor developer admin
- groups.Groups.merge_row : visible for admin
- groups.Memberships.detail : visible for customer contributor developer admin
- groups.Memberships.insert : visible for customer contributor developer admin
- invoicing.Plans.detail : visible for admin
- invoicing.SalesRules.detail : visible for admin
- ledger.AccountingPeriods.merge_row : visible for admin
- ledger.Accounts.detail : visible for admin
- ledger.Accounts.insert : visible for admin
- ledger.Accounts.merge_row : visible for admin
- ledger.FiscalYears.merge_row : visible for admin
- ledger.Journals.detail : visible for admin
- ledger.Journals.insert : visible for admin
- ledger.Journals.merge_row : visible for admin
- ledger.PaymentTerms.detail : visible for admin
- ledger.PaymentTerms.merge_row : visible for admin
- ledger.Situation.show : visible for admin
- lists.Lists.detail : visible for contributor developer admin
- lists.Lists.insert : visible for contributor developer admin
- lists.Lists.merge_row : visible for admin
- lists.Members.detail : visible for contributor developer admin
- lists.MembersByPartner.insert : visible for contributor developer admin
- mailbox.Mailboxes.detail : visible for customer contributor developer admin
- mailbox.Mailboxes.insert : visible for customer contributor developer admin
- mailbox.MessageAttachments.detail : visible for customer contributor developer admin
- mailbox.Messages.detail : visible for customer contributor developer admin
- products.ProductCats.detail : visible for admin
- products.Products.detail : visible for admin
- products.Products.insert : visible for admin
- sales.InvoiceItems.detail : visible for admin
- sales.InvoiceItems.insert : visible for admin
- sales.Invoices.detail : visible for admin
- sales.Invoices.insert : visible for admin
- sales.InvoicesByJournal.insert : visible for admin
- system.SiteConfigs.detail : visible for admin
- tickets.Links.detail : visible for developer admin
- tickets.Links.insert : visible for developer admin
- tickets.Sites.detail : visible for customer contributor developer admin
- tickets.Sites.insert : visible for customer contributor developer admin
- tickets.Sites.merge_row : visible for admin
- tickets.TicketTypes.detail : visible for developer admin
- tickets.Tickets.detail : visible for all
- tickets.Tickets.insert : visible for customer contributor developer admin
- tickets.Tickets.merge_row : visible for admin
- tickets.Tickets.spawn_ticket : visible for all
- tinymce.TextFieldTemplates.detail : visible for admin
- tinymce.TextFieldTemplates.insert : visible for admin
- uploads.UploadTypes.detail : visible for admin
- uploads.UploadTypes.insert : visible for admin
- uploads.Uploads.detail : visible for customer contributor developer admin
- uploads.Uploads.insert : visible for customer contributor developer admin
- uploads.UploadsByController.insert : visible for customer contributor developer admin
- uploads.Volumes.detail : visible for admin
- uploads.Volumes.insert : visible for admin
- uploads.Volumes.merge_row : visible for admin
- users.AllUsers.change_password : visible for admin
- users.AllUsers.detail : visible for admin
- users.AllUsers.insert : visible for admin
- users.AllUsers.merge_row : visible for admin
- users.AllUsers.send_welcome_email : visible for admin
- users.AllUsers.verify : visible for admin
- users.NewUsers.send_welcome_email : visible for admin
- users.OtherUsers.detail : visible for customer contributor developer admin
- users.Register.insert : visible for customer contributor developer admin
- users.UsersOverview.sign_in : visible for all
- vat.Invoices.detail : visible for admin
- vat.Invoices.insert : visible for admin
- vat.InvoicesByJournal.insert : visible for admin
- working.ServiceReports.detail : visible for contributor developer admin
- working.ServiceReports.insert : visible for contributor developer admin
- working.Sessions.detail : visible for contributor developer admin
- working.Sessions.insert : visible for contributor developer admin
- working.SiteSummaries.detail : visible for customer contributor developer admin
- working.UserSummaries.detail : visible for customer contributor developer admin
- working.WorkedHours.detail : visible for customer contributor developer admin
<BLANKLINE>
