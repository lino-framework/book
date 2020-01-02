.. doctest docs/specs/tera/db.rst
.. _specs.tera.db:

===============================
Database structure in Lino Tera
===============================

.. contents::
   :local:
   :depth: 2

.. include:: /../docs/shared/include/tested.rst

>>> import lino
>>> lino.startup('lino_book.projects.lydia.settings.doctests')
>>> from lino.api.doctest import *


Complexity factors
==================

>>> print(analyzer.show_complexity_factors())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 46 plugins
- 98 models
- 22 user roles
- 4 user types
- 375 views
- 27 dialog actions
<BLANKLINE>


The database models
===================

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
46 apps: lino, staticfiles, about, ipdict, jinja, bootstrap3, extjs, printing, system, contenttypes, gfks, office, xl, excerpts, courses, users, dashboard, countries, contacts, households, clients, healthcare, products, memo, checkdata, weasyprint, uploads, ledger, bevats, vat, sales, cal, invoicing, sepa, finan, ana, sheets, topics, notes, appypod, export_excel, tinymce, tera, teams, lists, sessions.
98 models:
=========================== ============================== ========= =======
 Name                        Default table                  #fields   #rows
--------------------------- ------------------------------ --------- -------
 ana.Account                 ana.Accounts                   6         20
 ana.AnaAccountInvoice       ana.Invoices                   20        35
 ana.InvoiceItem             ana.InvoiceItemTable           10        55
 bevats.Declaration          bevats.Declarations            28        3
 cal.Calendar                cal.Calendars                  6         1
 cal.DailyPlannerRow         cal.DailyPlannerRows           7         3
 cal.Event                   cal.OneEvent                   25        363
 cal.EventPolicy             cal.EventPolicies              20        6
 cal.EventType               cal.EventTypes                 23        6
 cal.Guest                   cal.Guests                     7         280
 cal.GuestRole               cal.GuestRoles                 6         2
 cal.RecurrentEvent          cal.RecurrentEvents            22        15
 cal.RemoteCalendar          cal.RemoteCalendars            7         0
 cal.Room                    cal.Rooms                      9         0
 cal.Subscription            cal.Subscriptions              4         0
 cal.Task                    cal.Tasks                      19        0
 checkdata.Problem           checkdata.Problems             6         0
 clients.ClientContact       clients.ClientContacts         7         0
 clients.ClientContactType   clients.ClientContactTypes     5         0
 contacts.Company            contacts.Companies             30        30
 contacts.CompanyType        contacts.CompanyTypes          7         16
 contacts.Partner            contacts.Partners              28        105
 contacts.Person             contacts.Persons               35        69
 contacts.Role               contacts.Roles                 4         0
 contacts.RoleType           contacts.RoleTypes             4         5
 contenttypes.ContentType    gfks.ContentTypes              3         98
 countries.Country           countries.Countries            6         8
 countries.Place             countries.Places               9         78
 courses.Course              courses.Activities             44        52
 courses.Enrolment           courses.Enrolments             15        78
 courses.Line                courses.Lines                  25        3
 courses.Slot                courses.Slots                  5         0
 courses.Topic               courses.Topics                 4         0
 dashboard.Widget            dashboard.Widgets              5         0
 excerpts.Excerpt            excerpts.Excerpts              12        0
 excerpts.ExcerptType        excerpts.ExcerptTypes          17        9
 finan.BankStatement         finan.BankStatements           16        4
 finan.BankStatementItem     finan.BankStatementItemTable   10        263
 finan.JournalEntry          finan.FinancialVouchers        14        1
 finan.JournalEntryItem      finan.JournalEntryItemTable    10        4
 finan.PaymentOrder          finan.PaymentOrders            15        4
 finan.PaymentOrderItem      finan.PaymentOrderItemTable    10        29
 gfks.HelpText               gfks.HelpTexts                 4         2
 healthcare.Plan             healthcare.Plans               4         5
 healthcare.Rule             healthcare.Rules               6         0
 healthcare.Situation        healthcare.Situations          6         0
 households.Household        households.Households          31        6
 households.Member           households.Members             14        12
 households.Type             households.Types               4         6
 invoicing.Area              invoicing.Areas                6         3
 invoicing.Item              invoicing.Items                9         16
 invoicing.Plan              invoicing.Plans                8         1
 invoicing.SalesRule         invoicing.SalesRules           3         6
 invoicing.Tariff            invoicing.Tariffs              7         2
 ledger.Account              ledger.Accounts                21        27
 ledger.AccountingPeriod     ledger.AccountingPeriods       7         6
 ledger.FiscalYear           ledger.FiscalYears             5         6
 ledger.Journal              ledger.Journals                25        10
 ledger.LedgerInfo           ledger.LedgerInfoTable         2         0
 ledger.MatchRule            ledger.MatchRules              3         27
 ledger.Movement             ledger.Movements               13        901
 ledger.PaymentTerm          ledger.PaymentTerms            11        8
 ledger.Voucher              ledger.Vouchers                9         257
 lists.List                  lists.Lists                    7         8
 lists.ListType              lists.ListTypes                4         3
 lists.Member                lists.Members                  5         105
 notes.EventType             notes.EventTypes               8         1
 notes.Note                  notes.Notes                    17        100
 notes.NoteType              notes.NoteTypes                11        3
 products.PriceRule          products.PriceRules            7         3
 products.Product            products.Products              14        5
 products.ProductCat         products.ProductCats           6         2
 sales.InvoiceItem           sales.InvoiceItems             15        372
 sales.PaperType             sales.PaperTypes               5         2
 sales.VatProductInvoice     sales.Invoices                 27        210
 sepa.Account                sepa.Accounts                  6         31
 sessions.Session            sessions.SessionTable          3         ...
 sheets.AccountEntry         sheets.AccountEntryTable       7         17
 sheets.AnaAccountEntry      sheets.AnaAcountEntries        7         20
 sheets.Item                 sheets.Items                   9         25
 sheets.ItemEntry            sheets.ItemEntryTable          7         15
 sheets.PartnerEntry         sheets.PartnerEntryTable       8         47
 sheets.Report               sheets.Reports                 6         1
 system.SiteConfig           system.SiteConfigs             10        1
 teams.Team                  teams.Teams                    5         2
 tera.Client                 tera.Clients                   45        58
 tera.LifeMode               tera.LifeModes                 4         0
 tera.Procurer               tera.Procurers                 4         0
 tinymce.TextFieldTemplate   tinymce.TextFieldTemplates     5         2
 topics.Interest             topics.Interests               6         86
 topics.Topic                topics.Topics                  8         3
 uploads.Upload              uploads.Uploads                11        0
 uploads.UploadType          uploads.UploadTypes            8         1
 uploads.Volume              uploads.Volumes                5         0
 users.Authority             users.Authorities              3         0
 users.User                  users.AllUsers                 21        6
 vat.InvoiceItem             vat.InvoiceItemTable           9         0
 vat.VatAccountInvoice       vat.Invoices                   20        0
=========================== ============================== ========= =======
<BLANKLINE>



Foreign Keys and their `on_delete` setting
==========================================

Here is a list of foreign keys in :ref:`tera` and their on_delete
behaviour. See also :doc:`/dev/delete`.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_foreign_keys())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- ana.Account :
  - PROTECT : ana.InvoiceItem.ana_account, ledger.Account.ana_account, ledger.Movement.ana_account, sheets.AnaAccountEntry.ana_account
- ana.AnaAccountInvoice :
  - CASCADE : ana.InvoiceItem.voucher
- cal.Calendar :
  - PROTECT : cal.Subscription.calendar, system.SiteConfig.site_calendar
- cal.Event :
  - CASCADE : cal.Guest.event
- cal.EventType :
  - PROTECT : cal.Event.event_type, cal.EventPolicy.event_type, cal.RecurrentEvent.event_type, courses.Line.event_type, products.PriceRule.event_type, system.SiteConfig.default_event_type, users.User.event_type
- cal.GuestRole :
  - PROTECT : cal.Guest.role, courses.Enrolment.guest_role, courses.Line.guest_role
- cal.Room :
  - PROTECT : cal.Event.room, courses.Course.room
- clients.ClientContactType :
  - PROTECT : clients.ClientContact.type, contacts.Partner.client_contact_type
- contacts.Company :
  - PROTECT : cal.Room.company, clients.ClientContact.company, contacts.Role.company, courses.Line.company, excerpts.Excerpt.company, healthcare.Plan.provider, ledger.Journal.partner, notes.Note.company, system.SiteConfig.site_company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr, courses.Course.partner, households.Household.partner_ptr, invoicing.SalesRule.partner, sepa.Account.partner
  - PROTECT : ana.AnaAccountInvoice.partner, bevats.Declaration.partner, clients.ClientContact.client, finan.BankStatementItem.partner, finan.JournalEntryItem.partner, finan.PaymentOrderItem.partner, invoicing.Item.partner, invoicing.Plan.partner, invoicing.SalesRule.invoice_recipient, ledger.Movement.partner, lists.Member.partner, sales.VatProductInvoice.partner, sheets.PartnerEntry.partner, users.User.partner, vat.VatAccountInvoice.partner
- contacts.Person :
  - CASCADE : tera.Client.person_ptr
  - PROTECT : cal.Guest.partner, cal.Room.contact_person, clients.ClientContact.contact_person, contacts.Role.person, courses.Enrolment.pupil, courses.Line.contact_person, excerpts.Excerpt.contact_person, healthcare.Situation.client, households.Member.person, notes.Note.contact_person
- contacts.RoleType :
  - PROTECT : cal.Room.contact_role, clients.ClientContact.contact_role, contacts.Role.type, courses.Line.contact_role, excerpts.Excerpt.contact_role, notes.Note.contact_role
- contenttypes.ContentType :
  - PROTECT : cal.Event.owner_type, cal.Task.owner_type, checkdata.Problem.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, invoicing.Item.generator_type, notes.Note.owner_type, sales.InvoiceItem.invoiceable_type, topics.Interest.owner_type, uploads.Upload.owner_type
- countries.Country :
  - PROTECT : contacts.Partner.country, countries.Place.country, tera.Client.nationality
- countries.Place :
  - PROTECT : contacts.Partner.city, contacts.Partner.region, countries.Place.parent
- courses.Course :
  - CASCADE : topics.Interest.partner
  - PROTECT : cal.Event.project, cal.Task.project, courses.Enrolment.course, excerpts.Excerpt.project, invoicing.Plan.course, notes.Note.project
- courses.Line :
  - PROTECT : courses.Course.line
- courses.Slot :
  - PROTECT : courses.Course.slot
- courses.Topic :
  - PROTECT : courses.Line.topic
- excerpts.Excerpt :
  - SET_NULL : bevats.Declaration.printed_by, courses.Enrolment.printed_by, finan.BankStatement.printed_by, finan.JournalEntry.printed_by, finan.PaymentOrder.printed_by, sales.VatProductInvoice.printed_by, sheets.Report.printed_by
- excerpts.ExcerptType :
  - PROTECT : excerpts.Excerpt.excerpt_type
- finan.BankStatement :
  - CASCADE : finan.BankStatementItem.voucher
- finan.JournalEntry :
  - CASCADE : finan.JournalEntryItem.voucher
- finan.PaymentOrder :
  - CASCADE : finan.PaymentOrderItem.voucher
- healthcare.Plan :
  - PROTECT : courses.Course.healthcare_plan, healthcare.Rule.plan, healthcare.Situation.healthcare_plan
- households.Household :
  - CASCADE : households.Member.household
- households.Type :
  - PROTECT : households.Household.type
- invoicing.Area :
  - PROTECT : invoicing.Plan.area
- invoicing.Plan :
  - PROTECT : invoicing.Item.plan
- invoicing.Tariff :
  - PROTECT : products.Product.tariff
- ledger.Account :
  - PROTECT : ana.InvoiceItem.account, finan.BankStatement.item_account, finan.BankStatementItem.account, finan.JournalEntry.item_account, finan.JournalEntryItem.account, finan.PaymentOrder.item_account, finan.PaymentOrderItem.account, ledger.Journal.account, ledger.MatchRule.account, ledger.Movement.account, sheets.AccountEntry.account, vat.InvoiceItem.account
- ledger.AccountingPeriod :
  - PROTECT : bevats.Declaration.end_period, bevats.Declaration.start_period, ledger.Voucher.accounting_period, sheets.Report.end_period, sheets.Report.start_period
- ledger.FiscalYear :
  - PROTECT : ledger.AccountingPeriod.year
- ledger.Journal :
  - CASCADE : ledger.MatchRule.journal
  - PROTECT : invoicing.Area.journal, ledger.Voucher.journal
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
  - PROTECT : courses.Enrolment.option, courses.Line.fee, healthcare.Rule.client_fee, healthcare.Rule.provider_fee, products.PriceRule.fee, sales.InvoiceItem.product, users.User.cash_daybook
- products.ProductCat :
  - PROTECT : courses.Line.fees_cat, courses.Line.options_cat, products.Product.cat
- sales.PaperType :
  - PROTECT : courses.Course.paper_type, invoicing.SalesRule.paper_type, sales.VatProductInvoice.paper_type
- sales.VatProductInvoice :
  - CASCADE : sales.InvoiceItem.voucher
  - SET_NULL : invoicing.Item.invoice
- sepa.Account :
  - PROTECT : finan.PaymentOrderItem.bank_account, ledger.Journal.sepa_account
- sheets.Item :
  - PROTECT : ledger.Account.sheet_item, sheets.ItemEntry.item
- sheets.Report :
  - CASCADE : sheets.AccountEntry.report, sheets.AnaAccountEntry.report, sheets.ItemEntry.report, sheets.PartnerEntry.report
- teams.Team :
  - PROTECT : courses.Course.team, users.User.team
- tera.Client :
  - PROTECT : tera.Client.obsoletes
- tera.LifeMode :
  - PROTECT : tera.Client.life_mode
- tera.Procurer :
  - PROTECT : courses.Course.procurer
- topics.Topic :
  - PROTECT : topics.Interest.topic
- uploads.UploadType :
  - PROTECT : uploads.Upload.type
- uploads.Volume :
  - PROTECT : ledger.Journal.uploads_volume, uploads.Upload.volume
- users.User :
  - CASCADE : ledger.LedgerInfo.user
  - PROTECT : cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, checkdata.Problem.user, courses.Course.teacher, courses.Course.user, courses.Enrolment.user, dashboard.Widget.user, excerpts.Excerpt.user, invoicing.Plan.user, ledger.Voucher.user, notes.Note.user, sheets.Report.user, tera.Client.user, tinymce.TextFieldTemplate.user, uploads.Upload.user, users.Authority.authorized, users.Authority.user
- vat.VatAccountInvoice :
  - CASCADE : vat.InvoiceItem.voucher
<BLANKLINE>
