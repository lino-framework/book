.. doctest docs/specs/tera/db.rst
.. _specs.tera.db:

===============================
Database structure in Lino Tera
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
43 apps: lino, staticfiles, about, jinja, bootstrap3, extjs, printing, system, contenttypes, gfks, courses, users, dashboard, office, xl, countries, contacts, households, clients, healthcare, products, vat, sales, cal, invoicing, weasyprint, ledger, sepa, finan, bevats, ana, sheets, topics, notes, excerpts, appypod, export_excel, checkdata, tinymce, tera, teams, lists, sessions.
93 models:
=========================== ============================== ========= =======
 Name                        Default table                  #fields   #rows
--------------------------- ------------------------------ --------- -------
 ana.Account                 ana.Accounts                   6         20
 ana.AnaAccountInvoice       ana.Invoices                   20        35
 ana.InvoiceItem             ana.InvoiceItemTable           10        55
 bevats.Declaration          bevats.Declarations            28        3
 cal.Calendar                cal.Calendars                  6         1
 cal.DailyPlannerRow         cal.DailyPlannerRows           7         3
 cal.Event                   cal.OneEvent                   25        693
 cal.EventPolicy             cal.EventPolicies              19        6
 cal.EventType               cal.EventTypes                 21        5
 cal.Guest                   cal.Guests                     7         780
 cal.GuestRole               cal.GuestRoles                 5         2
 cal.Priority                cal.Priorities                 5         4
 cal.RecurrentEvent          cal.RecurrentEvents            21        15
 cal.RemoteCalendar          cal.RemoteCalendars            7         0
 cal.Room                    cal.Rooms                      8         0
 cal.Subscription            cal.Subscriptions              4         0
 cal.Task                    cal.Tasks                      18        0
 checkdata.Problem           checkdata.Problems             6         0
 clients.ClientContact       clients.ClientContacts         7         0
 clients.ClientContactType   clients.ClientContactTypes     5         0
 contacts.Company            contacts.Companies             27        25
 contacts.CompanyType        contacts.CompanyTypes          7         16
 contacts.Partner            contacts.Partners              25        100
 contacts.Person             contacts.Persons               32        69
 contacts.Role               contacts.Roles                 4         0
 contacts.RoleType           contacts.RoleTypes             4         5
 contenttypes.ContentType    gfks.ContentTypes              3         93
 countries.Country           countries.Countries            6         8
 countries.Place             countries.Places               9         78
 courses.Course              courses.Activities             42        52
 courses.Enrolment           courses.Enrolments             16        78
 courses.Line                courses.Lines                  25        3
 courses.Slot                courses.Slots                  5         0
 courses.Topic               courses.Topics                 4         0
 dashboard.Widget            dashboard.Widgets              5         0
 excerpts.Excerpt            excerpts.Excerpts              12        0
 excerpts.ExcerptType        excerpts.ExcerptTypes          17        10
 finan.BankStatement         finan.BankStatements           16        4
 finan.BankStatementItem     finan.BankStatementItemTable   10        186
 finan.JournalEntry          finan.FinancialVouchers        14        0
 finan.JournalEntryItem      finan.JournalEntryItemTable    10        0
 finan.PaymentOrder          finan.PaymentOrders            15        4
 finan.PaymentOrderItem      finan.PaymentOrderItemTable    10        40
 gfks.HelpText               gfks.HelpTexts                 4         2
 healthcare.Plan             healthcare.Plans               6         0
 healthcare.Rule             healthcare.Rules               4         0
 households.Household        households.Households          28        6
 households.Member           households.Members             14        12
 households.Type             households.Types               4         6
 invoicing.Item              invoicing.Items                9         44
 invoicing.Plan              invoicing.Plans                7         1
 invoicing.SalesRule         invoicing.SalesRules           3         6
 invoicing.Tariff            invoicing.Tariffs              7         1
 ledger.Account              ledger.Accounts                20        27
 ledger.AccountingPeriod     ledger.AccountingPeriods       7         6
 ledger.FiscalYear           ledger.FiscalYears             5         6
 ledger.Journal              ledger.Journals                23        8
 ledger.LedgerInfo           ledger.LedgerInfoTable         2         0
 ledger.MatchRule            ledger.MatchRules              3         16
 ledger.Movement             ledger.Movements               13        738
 ledger.PaymentTerm          ledger.PaymentTerms            11        8
 ledger.Voucher              ledger.Vouchers                9         212
 lists.List                  lists.Lists                    7         8
 lists.ListType              lists.ListTypes                4         3
 lists.Member                lists.Members                  5         0
 notes.EventType             notes.EventTypes               8         1
 notes.Note                  notes.Notes                    17        100
 notes.NoteType              notes.NoteTypes                11        3
 products.Product            products.Products              14        4
 products.ProductCat         products.ProductCats           5         2
 sales.InvoiceItem           sales.InvoiceItems             15        467
 sales.PaperType             sales.PaperTypes               5         2
 sales.VatProductInvoice     sales.Invoices                 25        166
 sepa.Account                sepa.Accounts                  6         31
 sessions.Session            sessions.SessionTable          3         ...
 sheets.AccountEntry         sheets.AccountEntryTable       7         16
 sheets.AnaAccountEntry      sheets.AnaAcountEntries        7         20
 sheets.Item                 sheets.Items                   9         25
 sheets.ItemEntry            sheets.ItemEntryTable          7         15
 sheets.PartnerEntry         sheets.PartnerEntryTable       8         70
 sheets.Report               sheets.Reports                 6         1
 system.SiteConfig           system.SiteConfigs             10        1
 teams.Team                  teams.Teams                    5         2
 tera.Client                 tera.Clients                   43        58
 tera.LifeMode               tera.LifeModes                 4         0
 tera.Procurer               tera.Procurers                 4         0
 tinymce.TextFieldTemplate   tinymce.TextFieldTemplates     5         2
 topics.Interest             topics.Interests               6         86
 topics.Topic                topics.Topics                  8         3
 users.Authority             users.Authorities              3         0
 users.User                  users.Users                    21        6
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
  - PROTECT : cal.Event.event_type, cal.EventPolicy.event_type, cal.RecurrentEvent.event_type, courses.Line.event_type, system.SiteConfig.default_event_type, users.User.event_type
- cal.GuestRole :
  - PROTECT : cal.Guest.role, courses.Enrolment.guest_role, courses.Line.guest_role
- cal.Priority :
  - PROTECT : cal.Event.priority
- cal.Room :
  - PROTECT : cal.Event.room, courses.Course.room
- clients.ClientContactType :
  - PROTECT : clients.ClientContact.type, contacts.Partner.client_contact_type
- contacts.Company :
  - PROTECT : cal.Room.company, clients.ClientContact.company, contacts.Role.company, courses.Line.company, excerpts.Excerpt.company, healthcare.Plan.provider, ledger.Journal.partner, notes.Note.company, system.SiteConfig.site_company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr, courses.Course.partner, households.Household.partner_ptr, invoicing.SalesRule.partner, sepa.Account.partner, sheets.PartnerEntry.partner
  - PROTECT : ana.AnaAccountInvoice.partner, bevats.Declaration.partner, clients.ClientContact.client, finan.BankStatementItem.partner, finan.JournalEntryItem.partner, finan.PaymentOrderItem.partner, invoicing.Item.partner, invoicing.Plan.partner, invoicing.SalesRule.invoice_recipient, ledger.Movement.partner, lists.Member.partner, sales.VatProductInvoice.partner, users.User.partner, vat.VatAccountInvoice.partner
- contacts.Person :
  - CASCADE : tera.Client.person_ptr
  - PROTECT : cal.Guest.partner, cal.Room.contact_person, clients.ClientContact.contact_person, contacts.Role.person, courses.Enrolment.pupil, courses.Line.contact_person, excerpts.Excerpt.contact_person, households.Member.person, notes.Note.contact_person
- contacts.RoleType :
  - PROTECT : cal.Room.contact_role, clients.ClientContact.contact_role, contacts.Role.type, courses.Line.contact_role, excerpts.Excerpt.contact_role, notes.Note.contact_role
- contenttypes.ContentType :
  - PROTECT : cal.Event.owner_type, cal.Task.owner_type, checkdata.Problem.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, invoicing.Item.generator_type, notes.Note.owner_type, sales.InvoiceItem.invoiceable_type, topics.Interest.owner_type
- countries.Country :
  - PROTECT : contacts.Partner.country, countries.Place.country, tera.Client.nationality
- countries.Place :
  - PROTECT : contacts.Partner.city, contacts.Partner.region, countries.Place.parent
- courses.Course :
  - PROTECT : cal.Event.project, cal.Task.project, courses.Enrolment.course, excerpts.Excerpt.project, invoicing.Plan.course, notes.Note.project, topics.Interest.partner
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
  - PROTECT : courses.Course.healthcare_plan, healthcare.Rule.plan
- households.Household :
  - CASCADE : households.Member.household
- households.Type :
  - PROTECT : households.Household.type
- invoicing.Plan :
  - PROTECT : invoicing.Item.plan
- invoicing.Tariff :
  - PROTECT : products.Product.tariff
- ledger.Account :
  - CASCADE : sheets.AccountEntry.account
  - PROTECT : ana.InvoiceItem.account, finan.BankStatement.item_account, finan.BankStatementItem.account, finan.JournalEntry.item_account, finan.JournalEntryItem.account, finan.PaymentOrder.item_account, finan.PaymentOrderItem.account, ledger.Journal.account, ledger.MatchRule.account, ledger.Movement.account, vat.InvoiceItem.account
- ledger.AccountingPeriod :
  - PROTECT : bevats.Declaration.end_period, bevats.Declaration.start_period, ledger.Voucher.accounting_period, sheets.Report.end_period, sheets.Report.start_period
- ledger.FiscalYear :
  - PROTECT : ledger.AccountingPeriod.year
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
  - PROTECT : courses.Course.fee, courses.Enrolment.fee, courses.Enrolment.option, courses.Line.fee, healthcare.Rule.client_fee, healthcare.Rule.provider_fee, sales.InvoiceItem.product, users.User.prepayment_product
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
  - CASCADE : sheets.ItemEntry.item
  - PROTECT : ledger.Account.sheet_item
- sheets.Report :
  - PROTECT : sheets.AccountEntry.report, sheets.AnaAccountEntry.report, sheets.ItemEntry.report, sheets.PartnerEntry.report
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
- users.User :
  - CASCADE : ledger.LedgerInfo.user
  - PROTECT : cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, checkdata.Problem.user, courses.Course.teacher, courses.Course.user, courses.Enrolment.user, dashboard.Widget.user, excerpts.Excerpt.user, invoicing.Plan.user, ledger.Voucher.user, notes.Note.user, sheets.Report.user, tera.Client.user, tinymce.TextFieldTemplate.user, users.Authority.authorized, users.Authority.user
- vat.VatAccountInvoice :
  - CASCADE : vat.InvoiceItem.voucher
<BLANKLINE>


>>> print(analyzer.show_complexity_factors())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- 43 plugins
- 93 models
- 21 user roles
- 4 user types
- 348 views
- 26 dialog actions
<BLANKLINE>

