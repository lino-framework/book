.. doctest docs/specs/voga/roger.rst
.. _voga.specs.roger:

=================================
The ``roger`` demo project
=================================

The :mod:`lino_book.projects.roger` demo project illustrates some local
customizations.


.. contents::
   :local:

.. include:: /../docs/shared/include/tested.rst

>>> from lino import startup
>>> startup('lino_book.projects.roger.settings.doctests')
>>> from lino.api.doctest import *

A customized management of membership fees
==========================================

In :mod:`lino_book.projects.roger` they have the following rules for
handling memberships:

- Membership costs 15€  per year.
- Members get a discount on enrolments to courses.
- Customers can freely decide whether they want to be members or not.
- They become member by paying the membership fee.

To handle these rules, we have an additional field :attr:`member_until
<lino_voga.lib.roger.courses.models.Pupil.member_until>` on
each pupil.

There is a custom data checker
:class:`lino_voga.lib.roger.courses.models.MemberChecker`


>>> dd.demo_date()
datetime.date(2015, 5, 22)


>>> rt.show(courses.Pupils)
... #doctest: +ELLIPSIS +REPORT_UDIFF
======================================== ================================= ================== ============ ===== ===== ======== ==============
 Name                                     Address                           Participant Type   Section      LFV   CKK   Raviva   Mitglied bis
---------------------------------------- --------------------------------- ------------------ ------------ ----- ----- -------- --------------
 Hans Altenberg (MEL)                     Aachener Straße, 4700 Eupen       Member                          Yes   No    No       31/12/2015
 Annette Arens (MEC)                      Alter Malmedyer Weg, 4700 Eupen   Helper                          No    Yes   No       31/12/2015
 Laurent Bastiaensen (ME)                 Am Berg, 4700 Eupen               Non-member                      No    No    No       31/12/2015
 Bernd Brecht (ME)                        Aachen, Germany                   Member                          No    No    No       31/12/2015
 Ulrike Charlier (ME)                     Auenweg, 4700 Eupen               Helper                          No    No    No       31/12/2015
 Dorothée Demeulenaere (ME)               Auf'm Rain, 4700 Eupen            Non-member                      No    No    No       31/12/2016
 ...
 Hedi Radermacher (ME)                    4730 Raeren                       Non-member                      No    No    No       31/12/2015
 Jean Radermacher (ME)                    4730 Raeren                       Member                          No    No    No       31/12/2015
 Marie-Louise Vandenmeulenbos (MEC)       Amsterdam, Netherlands            Helper                          No    Yes   No       31/12/2015
 Didier di Rupo (MS)                      4730 Raeren                       Non-member         Herresbach   No    No    No
 Erna Ärgerlich (ME)                      4730 Raeren                       Member                          No    No    No       31/12/2015
 Otto Östges (MCS)                        4730 Raeren                       Helper             Eynatten     No    Yes   No
======================================== ================================= ================== ============ ===== ===== ======== ==============
<BLANKLINE>


>>> print(dd.plugins.ledger.suppress_movements_until)
None

>>> rt.show(checkdata.ProblemsByChecker, 'courses.MemberChecker')
============= ====================================== ==========================================
 Responsible   Database object                        Message
------------- -------------------------------------- ------------------------------------------
 Robin Rood    *Karl Kaivers (ME)*                    Member until 2015-12-31, but no payment.
 Robin Rood    *Laura Laschet (ME)*                   Member until 2015-12-31, but no payment.
 Robin Rood    *Josefine Leffin (MEL)*                Member until 2015-12-31, but no payment.
 Robin Rood    *Marie-Louise Meier (ME)*              Member until 2015-12-31, but no payment.
 Robin Rood    *Alfons Radermacher (ME)*              Member until 2015-12-31, but no payment.
 Robin Rood    *Christian Radermacher (MEL)*          Member until 2015-12-31, but no payment.
 Robin Rood    *Edgard Radermacher (ME)*              Member until 2015-12-31, but no payment.
 Robin Rood    *Guido Radermacher (ME)*               Member until 2015-12-31, but no payment.
 Robin Rood    *Hedi Radermacher (ME)*                Member until 2015-12-31, but no payment.
 Robin Rood    *Jean Radermacher (ME)*                Member until 2015-12-31, but no payment.
 Robin Rood    *Erna Ärgerlich (ME)*                  Member until 2015-12-31, but no payment.
 Robin Rood    *Jean Dupont (ME)*                     Member until 2015-12-31, but no payment.
 Robin Rood    *Marie-Louise Vandenmeulenbos (MEC)*   Member until 2015-12-31, but no payment.
 Robin Rood    *Bernd Brecht (ME)*                    Member until 2015-12-31, but no payment.
 Robin Rood    *Jérôme Jeanémart (ME)*                Member until 2015-12-31, but no payment.
============= ====================================== ==========================================
<BLANKLINE>

>>> acc = rt.models.ledger.CommonAccounts.membership_fees.get_object()
>>> print(acc)
(7310) Membership fees

>>> rt.show(ledger.MovementsByAccount, acc)
============ ============== ===================================== ======= ============ =============
 Value date   Voucher        Description                           Debit   Credit       Match
------------ -------------- ------------------------------------- ------- ------------ -------------
 22/12/2015   *CSH 5/2015*   *Faymonville Luc*                             15,00        **CSH 5:1**
 22/12/2015   *CSH 5/2015*   *Groteclaes Gregory*                          15,00        **CSH 5:2**
 22/12/2015   *CSH 5/2015*   *Hilgers Hildegard*                           15,00        **CSH 5:3**
 22/12/2015   *CSH 5/2015*   *Jacobs Jacqueline*                           15,00        **CSH 5:4**
 22/12/2015   *CSH 5/2015*   *Jonas Josef*                                 15,00        **CSH 5:5**
 22/11/2015   *CSH 4/2015*   *Dobbelstein-Demeulenaere Dorothée*           15,00        **CSH 4:1**
 22/11/2015   *CSH 4/2015*   *Emonts Daniel*                               15,00        **CSH 4:3**
 22/11/2015   *CSH 4/2015*   *Engels Edgar*                                15,00        **CSH 4:4**
 22/11/2015   *CSH 4/2015*   *Evers Eberhart*                              15,00        **CSH 4:2**
 22/10/2015   *CSH 3/2015*   *Demeulenaere Dorothée*                       15,00        **CSH 3:2**
 22/10/2015   *CSH 3/2015*   *Dericum Daniel*                              15,00        **CSH 3:1**
 22/02/2015   *CSH 2/2015*   *Charlier Ulrike*                             15,00        **CSH 2:1**
 22/01/2015   *CSH 1/2015*   *Altenberg Hans*                              15,00        **CSH 1:2**
 22/01/2015   *CSH 1/2015*   *Arens Annette*                               15,00        **CSH 1:1**
 22/01/2015   *CSH 1/2015*   *Bastiaensen Laurent*                         15,00        **CSH 1:3**
                             **Balance -225.00 (15 movements)**            **225,00**
============ ============== ===================================== ======= ============ =============
<BLANKLINE>



Database structure
==================

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_db_overview())
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
42 apps: lino, staticfiles, about, jinja, printing, system, contenttypes, gfks, memo, react, users, office, xl, countries, contacts, lists, beid, checkdata, cal, courses, products, rooms, excerpts, weasyprint, uploads, ledger, bevats, vat, sales, invoicing, finan, sepa, notes, outbox, voga, export_excel, calview, wkhtmltopdf, appypod, changes, publisher, sessions.
83 models:
========================== ============================== ========= =======
 Name                       Default table                  #fields   #rows
-------------------------- ------------------------------ --------- -------
 bevats.Declaration         bevats.Declarations            28        15
 cal.Calendar               cal.Calendars                  6         8
 cal.Event                  cal.OneEvent                   23        1171
 cal.EventPolicy            cal.EventPolicies              20        6
 cal.EventType              cal.EventTypes                 23        10
 cal.Guest                  cal.Guests                     6         0
 cal.GuestRole              cal.GuestRoles                 5         3
 cal.RecurrentEvent         cal.RecurrentEvents            22        16
 cal.RemoteCalendar         cal.RemoteCalendars            7         0
 cal.Room                   cal.AllRooms                   11        7
 cal.Subscription           cal.Subscriptions              4         35
 cal.Task                   cal.Tasks                      18        0
 calview.DailyPlannerRow    calview.DailyPlannerRows       7         2
 changes.Change             changes.Changes                10        0
 checkdata.Problem          checkdata.Problems             6         21
 contacts.Company           contacts.Companies             26        31
 contacts.CompanyType       contacts.CompanyTypes          7         16
 contacts.Partner           contacts.Partners              24        103
 contacts.Person            contacts.Persons               42        72
 contacts.Role              contacts.Roles                 4         3
 contacts.RoleType          contacts.RoleTypes             5         5
 contenttypes.ContentType   gfks.ContentTypes              3         83
 countries.Country          countries.Countries            6         8
 countries.Place            countries.Places               9         78
 courses.Course             courses.Activities             34        26
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
 excerpts.ExcerptType       excerpts.ExcerptTypes          17        14
 finan.BankStatement        finan.BankStatements           16        21
 finan.BankStatementItem    finan.BankStatementItemTable   9         164
 finan.JournalEntry         finan.FinancialVouchers        14        0
 finan.JournalEntryItem     finan.JournalEntryItemTable    9         0
 finan.PaymentOrder         finan.PaymentOrders            15        16
 finan.PaymentOrderItem     finan.PaymentOrderItemTable    9         127
 gfks.HelpText              gfks.HelpTexts                 4         2
 invoicing.Area             invoicing.Areas                6         1
 invoicing.Item             invoicing.Items                9         5
 invoicing.Plan             invoicing.Plans                8         1
 invoicing.SalesRule        invoicing.SalesRules           3         4
 invoicing.Tariff           invoicing.Tariffs              7         3
 ledger.Account             ledger.Accounts                18        21
 ledger.AccountingPeriod    ledger.AccountingPeriods       7         17
 ledger.FiscalYear          ledger.FiscalYears             5         7
 ledger.Journal             ledger.Journals                25        10
 ledger.LedgerInfo          ledger.LedgerInfoTable         2         0
 ledger.MatchRule           ledger.MatchRules              3         33
 ledger.Movement            ledger.Movements               11        939
 ledger.PaymentTerm         ledger.PaymentTerms            11        8
 ledger.Voucher             ledger.AllVouchers             8         268
 lists.List                 lists.Lists                    7         8
 lists.ListType             lists.ListTypes                4         3
 lists.Member               lists.Members                  5         103
 notes.EventType            notes.EventTypes               8         1
 notes.Note                 notes.Notes                    16        100
 notes.NoteType             notes.NoteTypes                11        3
 outbox.Attachment          outbox.Attachments             4         0
 outbox.Mail                outbox.Mails                   8         0
 outbox.Recipient           outbox.Recipients              6         0
 products.PriceRule         products.PriceRules            4         0
 products.Product           products.Products              14        11
 products.ProductCat        products.ProductCats           6         5
 rooms.Booking              rooms.Bookings                 24        3
 sales.InvoiceItem          sales.InvoiceItems             15        174
 sales.PaperType            sales.PaperTypes               5         2
 sales.VatProductInvoice    sales.Invoices                 27        97
 sepa.Account               sepa.Accounts                  6         26
 sessions.Session           sessions.SessionTable          3         ...
 system.SiteConfig          system.SiteConfigs             11        1
 uploads.Upload             uploads.Uploads                11        0
 uploads.UploadType         uploads.UploadTypes            8         1
 uploads.Volume             uploads.Volumes                5         0
 users.Authority            users.Authorities              3         0
 users.User                 users.AllUsers                 18        6
 vat.InvoiceItem            vat.InvoiceItemTable           9         187
 vat.VatAccountInvoice      vat.Invoices                   20        119
========================== ============================== ========= =======
<BLANKLINE>


Foreign Keys and their `on_delete` setting
==========================================

Here is a list of foreign keys in :ref:`voga` and their on_delete
behaviour. See also :doc:`/dev/delete`.

>>> from lino.utils.diag import analyzer
>>> print(analyzer.show_foreign_keys())
... #doctest: +NORMALIZE_WHITESPACE +REPORT_UDIFF
- cal.Calendar :
  - PROTECT : cal.Room.calendar, cal.Subscription.calendar, system.SiteConfig.site_calendar
- cal.Event :
  - CASCADE : cal.Guest.event
- cal.EventType :
  - PROTECT : cal.Event.event_type, cal.EventPolicy.event_type, cal.RecurrentEvent.event_type, courses.Line.event_type, products.PriceRule.selector, rooms.Booking.event_type, system.SiteConfig.default_event_type, users.User.event_type
- cal.GuestRole :
  - PROTECT : cal.Guest.role, courses.Line.guest_role, system.SiteConfig.pupil_guestrole
- cal.Room :
  - PROTECT : cal.Event.room, courses.Course.room, rooms.Booking.room
- contacts.Company :
  - PROTECT : cal.Room.company, contacts.Role.company, courses.Line.company, excerpts.Excerpt.company, ledger.Journal.partner, notes.Note.company, rooms.Booking.company, system.SiteConfig.site_company
- contacts.CompanyType :
  - PROTECT : contacts.Company.type
- contacts.Partner :
  - CASCADE : contacts.Company.partner_ptr, contacts.Person.partner_ptr, invoicing.SalesRule.partner, sepa.Account.partner
  - PROTECT : bevats.Declaration.partner, finan.BankStatementItem.partner, finan.JournalEntryItem.partner, finan.PaymentOrderItem.partner, invoicing.Item.partner, invoicing.Plan.partner, invoicing.SalesRule.invoice_recipient, ledger.Movement.partner, lists.Member.partner, outbox.Recipient.partner, sales.VatProductInvoice.partner, users.User.partner, vat.VatAccountInvoice.partner
- contacts.Person :
  - CASCADE : courses.Pupil.person_ptr, courses.Teacher.person_ptr
  - PROTECT : cal.Guest.partner, cal.Room.contact_person, contacts.Role.person, courses.Line.contact_person, excerpts.Excerpt.contact_person, notes.Note.contact_person, rooms.Booking.contact_person
- contacts.RoleType :
  - PROTECT : cal.Room.contact_role, contacts.Role.type, courses.Line.contact_role, excerpts.Excerpt.contact_role, notes.Note.contact_role, rooms.Booking.contact_role
- contenttypes.ContentType :
  - PROTECT : cal.Event.owner_type, cal.Task.owner_type, changes.Change.master_type, changes.Change.object_type, checkdata.Problem.owner_type, excerpts.Excerpt.owner_type, excerpts.ExcerptType.content_type, gfks.HelpText.content_type, invoicing.Item.generator_type, notes.Note.owner_type, outbox.Attachment.owner_type, outbox.Mail.owner_type, sales.InvoiceItem.invoiceable_type, uploads.Upload.owner_type
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
- invoicing.Area :
  - PROTECT : invoicing.Plan.area
- invoicing.Plan :
  - PROTECT : invoicing.Item.plan
- invoicing.Tariff :
  - PROTECT : products.Product.tariff
- ledger.Account :
  - PROTECT : finan.BankStatement.item_account, finan.BankStatementItem.account, finan.JournalEntry.item_account, finan.JournalEntryItem.account, finan.PaymentOrder.item_account, finan.PaymentOrderItem.account, ledger.Journal.account, ledger.MatchRule.account, ledger.Movement.account, vat.InvoiceItem.account
- ledger.AccountingPeriod :
  - PROTECT : bevats.Declaration.end_period, bevats.Declaration.start_period, ledger.Voucher.accounting_period
- ledger.FiscalYear :
  - PROTECT : ledger.AccountingPeriod.year
- ledger.Journal :
  - CASCADE : ledger.MatchRule.journal
  - PROTECT : invoicing.Area.journal, ledger.Voucher.journal
- ledger.PaymentTerm :
  - PROTECT : bevats.Declaration.payment_term, contacts.Partner.payment_term, courses.Course.payment_term, sales.VatProductInvoice.payment_term, vat.VatAccountInvoice.payment_term
- ledger.Voucher :
  - CASCADE : ledger.Movement.voucher
  - PROTECT : bevats.Declaration.voucher_ptr, finan.BankStatement.voucher_ptr, finan.JournalEntry.voucher_ptr, finan.PaymentOrder.voucher_ptr, sales.VatProductInvoice.voucher_ptr, vat.VatAccountInvoice.voucher_ptr
- lists.List :
  - CASCADE : lists.Member.list
- lists.ListType :
  - PROTECT : lists.List.list_type
- notes.EventType :
  - PROTECT : notes.Note.event_type, system.SiteConfig.system_note_type
- notes.NoteType :
  - PROTECT : notes.Note.type
- outbox.Mail :
  - CASCADE : outbox.Attachment.mail, outbox.Recipient.mail
- products.Product :
  - PROTECT : cal.Room.fee, courses.Course.fee, courses.Enrolment.fee, courses.Enrolment.option, courses.Line.fee, products.PriceRule.product, sales.InvoiceItem.product
- products.ProductCat :
  - PROTECT : courses.Line.fees_cat, courses.Line.options_cat, products.Product.cat
- sales.PaperType :
  - PROTECT : courses.Course.paper_type, invoicing.SalesRule.paper_type, sales.VatProductInvoice.paper_type
- sales.VatProductInvoice :
  - CASCADE : sales.InvoiceItem.voucher
  - SET_NULL : invoicing.Item.invoice
- sepa.Account :
  - PROTECT : finan.PaymentOrderItem.bank_account, ledger.Journal.sepa_account
- uploads.UploadType :
  - PROTECT : uploads.Upload.type
- uploads.Volume :
  - PROTECT : ledger.Journal.uploads_volume, uploads.Upload.volume
- users.User :
  - CASCADE : ledger.LedgerInfo.user
  - PROTECT : cal.Event.assigned_to, cal.Event.user, cal.RecurrentEvent.user, cal.Subscription.user, cal.Task.user, changes.Change.user, checkdata.Problem.user, courses.Course.user, courses.Enrolment.user, excerpts.Excerpt.user, invoicing.Plan.user, ledger.Voucher.user, notes.Note.user, outbox.Mail.user, rooms.Booking.user, uploads.Upload.user, users.Authority.authorized, users.Authority.user
- vat.VatAccountInvoice :
  - CASCADE : vat.InvoiceItem.voucher
<BLANKLINE>


.. Here is the output of :func:`walk_menu_items
   <lino.api.doctests.walk_menu_items>` for this database.

    >>> walk_menu_items('rolf', severe=False)
    ... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF +SKIP
