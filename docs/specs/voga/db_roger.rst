.. doctest docs/specs/voga/db_roger.rst
.. _voga.specs.db_roger:

===============================
Database structure in Lino Voga
===============================

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.roger.settings.doctests')
    >>> from lino.api.doctest import *




The database structure
======================

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
43 apps: lino, staticfiles, about, jinja, bootstrap3, extjs, printing, system, users, office, xl, countries, cosi, contacts, lists, beid, contenttypes, gfks, checkdata, cal, products, rooms, accounts, weasyprint, ledger, vat, sales, invoicing, courses, finan, sepa, bevats, notes, uploads, outbox, excerpts, voga, export_excel, extensible, wkhtmltopdf, appypod, changes, sessions.
77 models:
========================== ============================== ========= =======
 Name                       Default table                  #fields   #rows
-------------------------- ------------------------------ --------- -------
 accounts.Account           accounts.Accounts              19        15
 accounts.Group             accounts.Groups                6         6
 bevats.Declaration         bevats.Declarations            28        15
 cal.Calendar               cal.Calendars                  6         8
 cal.Event                  cal.OneEvent                   23        1161
 cal.EventPolicy            cal.EventPolicies              19        6
 cal.EventType              cal.EventTypes                 18        9
 cal.Guest                  cal.Guests                     6         0
 cal.GuestRole              cal.GuestRoles                 4         3
 cal.Priority               cal.Priorities                 5         4
 cal.RecurrentEvent         cal.RecurrentEvents            21        16
 cal.RemoteCalendar         cal.RemoteCalendars            7         0
 cal.Room                   cal.AllRooms                   10        7
 cal.Subscription           cal.Subscriptions              4         35
 cal.Task                   cal.Tasks                      17        0
 changes.Change             changes.Changes                10        0
 checkdata.Problem          checkdata.Problems             6         20
 contacts.Company           contacts.Companies             27        31
 contacts.CompanyType       contacts.CompanyTypes          7         16
 contacts.Partner           contacts.Partners              25        103
 contacts.Person            contacts.Persons               42        72
 contacts.Role              contacts.Roles                 4         0
 contacts.RoleType          contacts.RoleTypes             4         5
 contenttypes.ContentType   gfks.ContentTypes              3         77
 countries.Country          countries.Countries            6         8
 countries.Place            countries.Places               9         78
 courses.Course             courses.Activities             33        26
 courses.CourseType         courses.CourseTypes            5         0
 courses.Enrolment          courses.Enrolments             17        95
 courses.Line               courses.Lines                  25        10
 courses.Pupil              courses.Pupils                 51        35
 courses.PupilType          courses.PupilTypes             5         3
 courses.Slot               courses.Slots                  5         0
 courses.Teacher            courses.Teachers               44        9
 courses.TeacherType        courses.TeacherTypes           5         4
 courses.Topic              courses.Topics                 4         5
 excerpts.Excerpt           excerpts.Excerpts              11        ...
 excerpts.ExcerptType       excerpts.ExcerptTypes          17        15
 finan.BankStatement        finan.BankStatements           16        21
 finan.BankStatementItem    finan.BankStatementItemTable   10        129
 finan.JournalEntry         finan.FinancialVouchers        14        0
 finan.JournalEntryItem     finan.JournalEntryItemTable    10        0
 finan.PaymentOrder         finan.PaymentOrders            15        16
 finan.PaymentOrderItem     finan.PaymentOrderItemTable    10        112
 gfks.HelpText              gfks.HelpTexts                 4         2
 invoicing.Item             invoicing.Items                10        7
 invoicing.Plan             invoicing.Plans                7         1
 ledger.AccountingPeriod    ledger.AccountingPeriods       7         17
 ledger.Journal             ledger.Journals                23        8
 ledger.MatchRule           ledger.MatchRules              3         12
 ledger.Movement            ledger.Movements               12        854
 ledger.PaymentTerm         ledger.PaymentTerms            11        8
 ledger.Voucher             ledger.Vouchers                9         258
 lists.List                 lists.Lists                    7         8
 lists.ListType             lists.ListTypes                4         3
 lists.Member               lists.Members                  5         0
 notes.EventType            notes.EventTypes               8         1
 notes.Note                 notes.Notes                    16        100
 notes.NoteType             notes.NoteTypes                11        3
 outbox.Attachment          outbox.Attachments             4         0
 outbox.Mail                outbox.Mails                   8         0
 outbox.Recipient           outbox.Recipients              6         0
 products.Product           products.Products              14        11
 products.ProductCat        products.ProductCats           5         5
 rooms.Booking              rooms.Bookings                 23        3
 sales.InvoiceItem          sales.InvoiceItems             15        114
 sales.PaperType            sales.PaperTypes               5         2
 sales.VatProductInvoice    sales.Invoices                 24        87
 sepa.Account               sepa.Accounts                  6         38
 sessions.Session           sessions.SessionTable          3         ...
 system.SiteConfig          system.SiteConfigs             11        1
 uploads.Upload             uploads.Uploads                9         0
 uploads.UploadType         uploads.UploadTypes            8         0
 users.Authority            users.Authorities              3         0
 users.User                 users.Users                    18        6
 vat.InvoiceItem            vat.InvoiceItemTable           9         187
 vat.VatAccountInvoice      vat.Invoices                   19        119
========================== ============================== ========= =======
<BLANKLINE>


Foreign Keys and their `on_delete` setting
==========================================

Here is a list of foreign keys in :ref:`voga` and their on_delete
behaviour. See also :doc:`/dev/delete`.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_foreign_keys())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- accounts.Account :
  - PROTECT : finan.BankStatement.item_account, finan.BankStatementItem.account, finan.JournalEntry.item_account, finan.JournalEntryItem.account, finan.PaymentOrder.item_account, finan.PaymentOrderItem.account, ledger.Journal.account, ledger.MatchRule.account, ledger.Movement.account, vat.InvoiceItem.account
- accounts.Group :
  - PROTECT : accounts.Account.group
- cal.Calendar :
  - PROTECT : cal.Room.calendar, cal.Subscription.calendar, system.SiteConfig.site_calendar
- cal.Event :
  - CASCADE : cal.Guest.event
- cal.EventType :
  - PROTECT : cal.Event.event_type, cal.EventPolicy.event_type, cal.RecurrentEvent.event_type, courses.Line.event_type, rooms.Booking.event_type, system.SiteConfig.default_event_type, users.User.event_type
- cal.GuestRole :
  - PROTECT : cal.Guest.role, courses.Line.guest_role, system.SiteConfig.pupil_guestrole
- cal.Priority :
  - PROTECT : cal.Event.priority
- cal.Room :
  - PROTECT : cal.Event.room, courses.Course.room, rooms.Booking.room
- contacts.Company :
  - PROTECT : cal.Room.company, contacts.Role.company, courses.Line.company, excerpts.Excerpt.company, ledger.Journal.partner, notes.Note.company, rooms.Booking.company, system.SiteConfig.site_company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr, sepa.Account.partner
  - PROTECT : bevats.Declaration.partner, contacts.Partner.invoice_recipient, finan.BankStatementItem.partner, finan.JournalEntryItem.partner, finan.PaymentOrderItem.partner, invoicing.Item.partner, invoicing.Plan.partner, ledger.Movement.partner, lists.Member.partner, outbox.Recipient.partner, sales.VatProductInvoice.partner, users.User.partner, vat.VatAccountInvoice.partner
- contacts.Person :
  - CASCADE : courses.Pupil.person_ptr, courses.Teacher.person_ptr
  - PROTECT : cal.Guest.partner, cal.Room.contact_person, contacts.Role.person, courses.Line.contact_person, excerpts.Excerpt.contact_person, notes.Note.contact_person, rooms.Booking.contact_person
- contacts.RoleType :
  - PROTECT : cal.Room.contact_role, contacts.Role.type, courses.Line.contact_role, excerpts.Excerpt.contact_role, notes.Note.contact_role, rooms.Booking.contact_role
- contenttypes.ContentType :
  - PROTECT : cal.Event.owner_type, cal.Task.owner_type, changes.Change.master_type, changes.Change.object_type, checkdata.Problem.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, notes.Note.owner_type, outbox.Attachment.owner_type, outbox.Mail.owner_type, sales.InvoiceItem.invoiceable_type, uploads.Upload.owner_type
- countries.Country :
  - PROTECT : contacts.Partner.country, contacts.Person.birth_country, contacts.Person.nationality, countries.Place.country
- countries.Place :
  - PROTECT : contacts.Partner.city, contacts.Partner.region, countries.Place.parent
- courses.Course :
  - PROTECT : courses.Enrolment.course, invoicing.Plan.course
- courses.CourseType :
  - PROTECT : courses.Line.course_type
- courses.Line :
  - PROTECT : courses.Course.line
- courses.Pupil :
  - PROTECT : courses.Enrolment.pupil
- courses.PupilType :
  - PROTECT : courses.Pupil.pupil_type
- courses.Slot :
  - PROTECT : courses.Course.slot
- courses.Teacher :
  - PROTECT : courses.Course.teacher
- courses.TeacherType :
  - PROTECT : courses.Teacher.teacher_type
- courses.Topic :
  - PROTECT : courses.Line.topic
- excerpts.Excerpt :
  - SET_NULL : bevats.Declaration.printed_by, courses.Enrolment.printed_by, finan.BankStatement.printed_by, finan.JournalEntry.printed_by, finan.PaymentOrder.printed_by, sales.VatProductInvoice.printed_by
- excerpts.ExcerptType :
  - PROTECT : excerpts.Excerpt.excerpt_type
- finan.BankStatement :
  - CASCADE : finan.BankStatementItem.voucher
- finan.JournalEntry :
  - CASCADE : finan.JournalEntryItem.voucher
- finan.PaymentOrder :
  - CASCADE : finan.PaymentOrderItem.voucher
- invoicing.Plan :
  - PROTECT : invoicing.Item.plan
- ledger.AccountingPeriod :
  - PROTECT : bevats.Declaration.end_period, bevats.Declaration.start_period, ledger.Voucher.accounting_period
- ledger.Journal :
  - PROTECT : invoicing.Plan.journal, ledger.MatchRule.journal, ledger.Voucher.journal
- ledger.PaymentTerm :
  - PROTECT : bevats.Declaration.payment_term, contacts.Partner.payment_term, courses.Course.payment_term, sales.VatProductInvoice.payment_term, vat.VatAccountInvoice.payment_term
- ledger.Voucher :
  - CASCADE : ledger.Movement.voucher
  - PROTECT : bevats.Declaration.voucher_ptr, finan.BankStatement.voucher_ptr, finan.JournalEntry.voucher_ptr, finan.PaymentOrder.voucher_ptr, sales.VatProductInvoice.voucher_ptr, vat.VatAccountInvoice.voucher_ptr
- lists.List :
  - PROTECT : lists.Member.list
- lists.ListType :
  - PROTECT : lists.List.list_type
- notes.EventType :
  - PROTECT : notes.Note.event_type, system.SiteConfig.system_note_type
- notes.NoteType :
  - PROTECT : notes.Note.type
- outbox.Mail :
  - CASCADE : outbox.Attachment.mail, outbox.Recipient.mail
- products.Product :
  - PROTECT : cal.Room.fee, courses.Course.fee, courses.Enrolment.fee, courses.Enrolment.option, courses.Line.fee, sales.InvoiceItem.product
- products.ProductCat :
  - PROTECT : courses.Line.fees_cat, courses.Line.options_cat, products.Product.cat
- sales.PaperType :
  - PROTECT : contacts.Partner.paper_type, courses.Course.paper_type, sales.VatProductInvoice.paper_type
- sales.VatProductInvoice :
  - CASCADE : sales.InvoiceItem.voucher
  - SET_NULL : invoicing.Item.invoice
- sepa.Account :
  - PROTECT : finan.PaymentOrderItem.bank_account, ledger.Journal.sepa_account
- uploads.UploadType :
  - PROTECT : uploads.Upload.type
- users.User :
  - PROTECT : cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, changes.Change.user, checkdata.Problem.user, courses.Course.user, courses.Enrolment.user, excerpts.Excerpt.user, invoicing.Plan.user, ledger.Voucher.user, notes.Note.user, outbox.Mail.user, rooms.Booking.user, uploads.Upload.user, users.Authority.authorized, users.Authority.user
- vat.VatAccountInvoice :
  - CASCADE : vat.InvoiceItem.voucher
<BLANKLINE>
