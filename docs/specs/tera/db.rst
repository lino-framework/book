.. doctest docs/specs/tera/db.rst
.. _specs.tera.db:

===============================
Database structure in Lino Voga
===============================

.. doctest init:

    >>> import lino
    >>> lino.startup('lino_book.projects.lydia.settings.doctests')
    >>> from lino.api.doctest import *




The database structure
======================

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
45 apps: lino, staticfiles, about, jinja, bootstrap3, extjs, printing, system, contenttypes, gfks, users, office, xl, countries, properties, contacts, households, clients, phones, humanlinks, products, cal, accounts, weasyprint, ledger, vat, sales, invoicing, courses, sepa, finan, bevats, ana, topics, notes, lists, extensible, excerpts, appypod, export_excel, checkdata, tinymce, tera, teams, sessions.
88 models:
=========================== ============================== ========= =======
 Name                        Default table                  #fields   #rows
--------------------------- ------------------------------ --------- -------
 accounts.Account            accounts.Accounts              21        15
 accounts.Group              accounts.Groups                6         6
 ana.Account                 ana.Accounts                   7         15
 ana.AnaAccountInvoice       ana.Invoices                   19        35
 ana.Group                   ana.Groups                     5         5
 ana.InvoiceItem             ana.InvoiceItemTable           10        55
 bevats.Declaration          bevats.Declarations            28        3
 cal.Calendar                cal.Calendars                  6         1
 cal.DailyPlannerRow         cal.DailyPlannerRows           7         3
 cal.Event                   cal.OneEvent                   24        173
 cal.EventPolicy             cal.EventPolicies              19        6
 cal.EventType               cal.EventTypes                 19        4
 cal.Guest                   cal.Guests                     6         0
 cal.GuestRole               cal.GuestRoles                 4         1
 cal.Priority                cal.Priorities                 5         4
 cal.RecurrentEvent          cal.RecurrentEvents            21        15
 cal.RemoteCalendar          cal.RemoteCalendars            7         0
 cal.Room                    cal.Rooms                      8         0
 cal.Subscription            cal.Subscriptions              4         0
 cal.Task                    cal.Tasks                      18        0
 checkdata.Problem           checkdata.Problems             6         0
 clients.ClientContact       clients.ClientContacts         7         0
 clients.ClientContactType   clients.ClientContactTypes     5         0
 contacts.Company            contacts.Companies             29        25
 contacts.CompanyType        contacts.CompanyTypes          7         16
 contacts.Partner            contacts.Partners              27        136
 contacts.Person             contacts.Persons               34        97
 contacts.Role               contacts.Roles                 4         0
 contacts.RoleType           contacts.RoleTypes             4         5
 contenttypes.ContentType    gfks.ContentTypes              3         88
 countries.Country           countries.Countries            6         8
 countries.Place             countries.Places               9         78
 courses.Course              courses.Activities             34        59
 courses.CourseType          courses.CourseTypes            5         0
 courses.Enrolment           courses.Enrolments             17        59
 courses.Line                courses.Lines                  25        3
 courses.Slot                courses.Slots                  5         0
 courses.Topic               courses.Topics                 4         0
 excerpts.Excerpt            excerpts.Excerpts              12        0
 excerpts.ExcerptType        excerpts.ExcerptTypes          17        9
 finan.BankStatement         finan.BankStatements           16        1
 finan.BankStatementItem     finan.BankStatementItemTable   10        6
 finan.JournalEntry          finan.FinancialVouchers        14        0
 finan.JournalEntryItem      finan.JournalEntryItemTable    10        0
 finan.PaymentOrder          finan.PaymentOrders            15        4
 finan.PaymentOrderItem      finan.PaymentOrderItemTable    10        40
 gfks.HelpText               gfks.HelpTexts                 4         2
 households.Household        households.Households          31        14
 households.Member           households.Members             14        63
 households.Type             households.Types               4         6
 humanlinks.Link             humanlinks.Links               4         59
 invoicing.Item              invoicing.Items                10        0
 invoicing.Plan              invoicing.Plans                6         1
 ledger.AccountingPeriod     ledger.AccountingPeriods       7         5
 ledger.Journal              ledger.Journals                24        8
 ledger.MatchRule            ledger.MatchRules              3         12
 ledger.Movement             ledger.Movements               13        260
 ledger.PaymentTerm          ledger.PaymentTerms            11        8
 ledger.Voucher              ledger.Vouchers                9         67
 lists.List                  lists.Lists                    7         8
 lists.ListType              lists.ListTypes                4         3
 lists.Member                lists.Members                  5         0
 notes.EventType             notes.EventTypes               8         1
 notes.Note                  notes.Notes                    17        100
 notes.NoteType              notes.NoteTypes                11        3
 phones.ContactDetail        phones.ContactDetails          7         15
 products.Product            products.Products              14        3
 products.ProductCat         products.ProductCats           5         0
 properties.PropChoice       properties.PropChoices         6         2
 properties.PropGroup        properties.PropGroups          4         0
 properties.PropType         properties.PropTypes           8         3
 properties.Property         properties.Properties          6         0
 sales.InvoiceItem           sales.InvoiceItems             15        48
 sales.PaperType             sales.PaperTypes               5         2
 sales.VatProductInvoice     sales.Invoices                 24        24
 sepa.Account                sepa.Accounts                  6         31
 sessions.Session            sessions.SessionTable          3         ...
 system.SiteConfig           system.SiteConfigs             10        1
 teams.Team                  teams.Teams                    5         2
 tera.Client                 tera.Clients                   61        59
 tinymce.TextFieldTemplate   tinymce.TextFieldTemplates     5         2
 topics.Interest             topics.Interests               6         0
 topics.Topic                topics.Topics                  9         0
 topics.TopicGroup           topics.TopicGroups             5         0
 users.Authority             users.Authorities              3         0
 users.User                  users.Users                    20        6
 vat.InvoiceItem             vat.InvoiceItemTable           9         0
 vat.VatAccountInvoice       vat.Invoices                   19        0
=========================== ============================== ========= =======
<BLANKLINE>


Foreign Keys and their `on_delete` setting
==========================================

Here is a list of foreign keys in :ref:`tera` and their on_delete
behaviour. See also :doc:`/dev/delete`.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_foreign_keys())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- accounts.Account :
  - PROTECT : ana.InvoiceItem.account, finan.BankStatement.item_account, finan.BankStatementItem.account, finan.JournalEntry.item_account, finan.JournalEntryItem.account, finan.PaymentOrder.item_account, finan.PaymentOrderItem.account, ledger.Journal.account, ledger.MatchRule.account, ledger.Movement.account, vat.InvoiceItem.account
- accounts.Group :
  - PROTECT : accounts.Account.group
- ana.Account :
  - PROTECT : accounts.Account.ana_account, ana.InvoiceItem.ana_account, ledger.Movement.ana_account
- ana.AnaAccountInvoice :
  - CASCADE : ana.InvoiceItem.voucher
- ana.Group :
  - PROTECT : ana.Account.group
- cal.Calendar :
  - PROTECT : cal.Subscription.calendar, system.SiteConfig.site_calendar
- cal.Event :
  - CASCADE : cal.Guest.event
- cal.EventType :
  - PROTECT : cal.Event.event_type, cal.EventPolicy.event_type, cal.RecurrentEvent.event_type, courses.Line.event_type, system.SiteConfig.default_event_type, users.User.event_type
- cal.GuestRole :
  - PROTECT : cal.Guest.role, courses.Line.guest_role
- cal.Priority :
  - PROTECT : cal.Event.priority
- cal.Room :
  - PROTECT : cal.Event.room, courses.Course.room
- clients.ClientContactType :
  - PROTECT : clients.ClientContact.type, contacts.Partner.client_contact_type
- contacts.Company :
  - PROTECT : cal.Room.company, clients.ClientContact.company, contacts.Role.company, courses.Line.company, excerpts.Excerpt.company, ledger.Journal.partner, notes.Note.company, system.SiteConfig.site_company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr, courses.Course.partner, households.Household.partner_ptr, phones.ContactDetail.partner, sepa.Account.partner
  - PROTECT : ana.AnaAccountInvoice.partner, bevats.Declaration.partner, clients.ClientContact.client, contacts.Partner.invoice_recipient, finan.BankStatementItem.partner, finan.JournalEntryItem.partner, finan.PaymentOrderItem.partner, invoicing.Item.partner, invoicing.Plan.partner, ledger.Movement.partner, lists.Member.partner, sales.VatProductInvoice.partner, users.User.partner, vat.VatAccountInvoice.partner
- contacts.Person :
  - CASCADE : tera.Client.person_ptr
  - PROTECT : cal.Guest.partner, cal.Room.contact_person, clients.ClientContact.contact_person, contacts.Role.person, courses.Enrolment.pupil, courses.Line.contact_person, excerpts.Excerpt.contact_person, households.Member.person, humanlinks.Link.child, humanlinks.Link.parent, notes.Note.contact_person
- contacts.RoleType :
  - PROTECT : cal.Room.contact_role, clients.ClientContact.contact_role, contacts.Role.type, courses.Line.contact_role, excerpts.Excerpt.contact_role, notes.Note.contact_role
- contenttypes.ContentType :
  - PROTECT : cal.Event.owner_type, cal.Task.owner_type, checkdata.Problem.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, notes.Note.owner_type, sales.InvoiceItem.invoiceable_type, topics.Interest.owner_type
- countries.Country :
  - PROTECT : contacts.Partner.country, countries.Place.country, tera.Client.nationality
- countries.Place :
  - PROTECT : contacts.Partner.city, contacts.Partner.region, countries.Place.parent
- courses.Course :
  - PROTECT : cal.Event.project, cal.Task.project, courses.Enrolment.course, excerpts.Excerpt.project, notes.Note.project, topics.Interest.partner
- courses.CourseType :
  - PROTECT : courses.Line.course_type
- courses.Line :
  - PROTECT : courses.Course.line, tera.Client.needed_course
- courses.Slot :
  - PROTECT : courses.Course.slot
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
- households.Household :
  - CASCADE : households.Member.household
- households.Type :
  - PROTECT : households.Household.type
- invoicing.Plan :
  - PROTECT : invoicing.Item.plan
- ledger.AccountingPeriod :
  - PROTECT : bevats.Declaration.end_period, bevats.Declaration.start_period, ledger.Voucher.accounting_period
- ledger.Journal :
  - PROTECT : invoicing.Plan.journal, ledger.MatchRule.journal, ledger.Voucher.journal
- ledger.PaymentTerm :
  - PROTECT : ana.AnaAccountInvoice.payment_term, bevats.Declaration.payment_term, contacts.Partner.payment_term, courses.Course.payment_term, sales.VatProductInvoice.payment_term, vat.VatAccountInvoice.payment_term
- ledger.Voucher :
  - CASCADE : ledger.Movement.voucher
  - PROTECT : ana.AnaAccountInvoice.voucher_ptr, bevats.Declaration.voucher_ptr, finan.BankStatement.voucher_ptr, finan.JournalEntry.voucher_ptr, finan.PaymentOrder.voucher_ptr, sales.VatProductInvoice.voucher_ptr, vat.VatAccountInvoice.voucher_ptr
- lists.List :
  - PROTECT : lists.Member.list
- lists.ListType :
  - PROTECT : lists.List.list_type
- notes.EventType :
  - PROTECT : notes.Note.event_type, system.SiteConfig.system_note_type
- notes.NoteType :
  - PROTECT : notes.Note.type
- products.Product :
  - PROTECT : courses.Course.fee, courses.Enrolment.fee, courses.Enrolment.option, courses.Line.fee, sales.InvoiceItem.product
- products.ProductCat :
  - PROTECT : courses.Line.fees_cat, courses.Line.options_cat, products.Product.cat
- properties.PropGroup :
  - PROTECT : properties.Property.group
- properties.PropType :
  - PROTECT : properties.PropChoice.type, properties.Property.type
- sales.PaperType :
  - PROTECT : contacts.Partner.paper_type, courses.Course.paper_type, sales.VatProductInvoice.paper_type
- sales.VatProductInvoice :
  - CASCADE : sales.InvoiceItem.voucher
  - SET_NULL : invoicing.Item.invoice
- sepa.Account :
  - PROTECT : finan.PaymentOrderItem.bank_account, ledger.Journal.sepa_account
- teams.Team :
  - PROTECT : contacts.Partner.team, ledger.Journal.team, users.User.team
- tera.Client :
  - PROTECT : tera.Client.obsoletes
- topics.Topic :
  - PROTECT : topics.Interest.topic
- topics.TopicGroup :
  - PROTECT : topics.Topic.topic_group
- users.User :
  - PROTECT : cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, checkdata.Problem.user, courses.Course.teacher, courses.Course.user, courses.Enrolment.user, excerpts.Excerpt.user, invoicing.Plan.user, ledger.Voucher.user, notes.Note.user, tera.Client.user, tinymce.TextFieldTemplate.user, users.Authority.authorized, users.Authority.user
- vat.VatAccountInvoice :
  - CASCADE : vat.InvoiceItem.voucher
<BLANKLINE>
